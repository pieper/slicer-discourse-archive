---
topic_id: 8449
title: "Create Cylinder Shell Shaped Segment"
date: 2019-09-16
url: https://discourse.slicer.org/t/8449
---

# Create cylinder shell shaped segment

**Topic ID**: 8449
**Date**: 2019-09-16
**URL**: https://discourse.slicer.org/t/create-cylinder-shell-shaped-segment/8449

---

## Post #1 by @giovform (2019-09-16 18:17 UTC)

<p>Hello, I am using the following code to create a cylinder shell, for segmentation. Running it causes the 3DSlicer to close. Any ideas on why is this happening?</p>
<pre><code>    segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
    segmentationNode.CreateDefaultDisplayNodes()  # only needed for display
    segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(inputVolume)

    segmentationCylinder1 = vtk.vtkCylinderSource()
    segmentationCylinder1.SetRadius(1.02 * diameter / 2)
    segmentationCylinder1.SetHeight(len(slicer.util.arrayFromVolume(inputVolume)) * inputVolume.GetSpacing()[2] * 1.2)
    segmentationCylinder1.SetResolution(100)

    segmentationCylinder2 = vtk.vtkCylinderSource()
    segmentationCylinder2.SetRadius(0.98 * diameter / 2)
    segmentationCylinder2.SetHeight(len(slicer.util.arrayFromVolume(inputVolume)) * inputVolume.GetSpacing()[2] * 1.5)
    segmentationCylinder2.SetResolution(100)

    filter = vtk.vtkBooleanOperationPolyDataFilter()
    filter.SetOperationToDifference()
    filter.SetInputData(0, segmentationCylinder1.GetOutput());
    filter.SetInputData(1, segmentationCylinder2.GetOutput());

    filter.Update()
    segmentationNode.AddSegmentFromClosedSurfaceRepresentation(filter.GetOutput(), "Segmentation", [0.0, 1.0, 0.0])
</code></pre>
<p>I am suspecting it’s a problem with VTK itself, not Slicer.</p>

---

## Post #2 by @giovform (2019-09-16 19:43 UTC)

<p>Oh well, I ended up constructing the cylinder shell using vtkRotationalExtrusionFilter, but the segmentation result was not I was expecting. I’ll post a screenshot of what I got:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/90927b906b9a460b740edc7b97dca462e9c4289e.png" data-download-href="/uploads/short-url/kCWAN7iK4aYuCuLh1kyYausFk8C.png?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/90927b906b9a460b740edc7b97dca462e9c4289e_2_690x439.png" alt="Screenshot" data-base62-sha1="kCWAN7iK4aYuCuLh1kyYausFk8C" width="690" height="439" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/90927b906b9a460b740edc7b97dca462e9c4289e_2_690x439.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/90927b906b9a460b740edc7b97dca462e9c4289e_2_1035x658.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/90927b906b9a460b740edc7b97dca462e9c4289e.png 2x" data-dominant-color="5D6973"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">1301×829 141 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I wanted to segment just inside the thin shell volume, but I got the whole cylinder instead. Any suggestions?</p>

---

## Post #3 by @lassoan (2019-09-17 04:28 UTC)

<aside class="quote no-group" data-username="giovform" data-post="1" data-topic="8449">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/giovform/48/4687_2.png" class="avatar"> giovform:</div>
<blockquote>
<p>Hello, I am using the following code to create a cylinder shell, for segmentation. Running it causes the 3DSlicer to close. Any ideas on why is this happening?</p>
</blockquote>
</aside>
<p>Unfortunately, Boolean operations in VTK do not work robustly. There have been a few alternatives developed but they are not yet in VTK master.</p>
<aside class="quote no-group" data-username="giovform" data-post="2" data-topic="8449">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/giovform/48/4687_2.png" class="avatar"> giovform:</div>
<blockquote>
<p>I ended up constructing the cylinder shell using vtkRotationalExtrusionFilter</p>
</blockquote>
</aside>
<p>Probably you would need to use vktLinearExtrusionFilter instead (with appending two circles, one with clockwise and the other with counter-clockwise ordered points). But if you don’t need sharp edges then you can create a shell from a cylinder using vtkImplicitModeller:</p>
<pre data-code-wrap="python"><code class="lang-python">cyl = vtk.vtkCylinderSource()
cyl.SetRadius(20.0)
cyl.SetHeight(60.0)
cyl.SetResolution(60)
cyl.CappingOff()

modeller = vtk.vtkImplicitModeller()
modeller.SetInputConnection(cyl.GetOutputPort())
modeller.SetAdjustDistance(0.20) # make sure the thickened model fits in output bounds

thickness = 5.0
contourFilter = vtk.vtkContourFilter()
contourFilter.SetInputConnection(modeller.GetOutputPort())
contourFilter.SetValue(0, thickness/2.0)
contourFilter.Update()

segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
segmentationNode.CreateDefaultDisplayNodes() 
segmentationNode.AddSegmentFromClosedSurfaceRepresentation(contourFilter.GetOutput(), "Cylinder", [0.0, 1.0, 0.0])
</code></pre>

---

## Post #4 by @giovform (2019-09-17 13:01 UTC)

<p>It worked. The following line was causing trouble though (the cylinder was rendered in separated strips), and I just deleted:</p>
<pre><code>modeller.SetAdjustDistance(0.20)
</code></pre>
<p>Thanks again Andras,</p>
<p>Giovanni</p>

---

## Post #5 by @lassoan (2019-09-17 13:39 UTC)

<aside class="quote no-group" data-username="giovform" data-post="4" data-topic="8449">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/giovform/48/4687_2.png" class="avatar"> giovform:</div>
<blockquote>
<p>It worked. The following line was causing trouble though (the cylinder was rendered in separated strips), and I just deleted:</p>
<pre><code class="lang-auto">modeller.SetAdjustDistance(0.20)
</code></pre>
</blockquote>
</aside>
<p>This parameter was necessary to avoid clipping of sides when cylinder radius was 20, height 60, and thickness 5. If you have thinner wall or different aspect ratio then size adjustment may not be needed and/or you need to change other parameters from their default (e.g., resolution).</p>

---

## Post #6 by @giovform (2019-10-07 20:42 UTC)

<p>Hello Andras, I noticed that even if I increase the cylinder resolution a lot (using .SetResolution(…)), it still seems to reach a max resolution (I get rough edges, more than two pixels in some places). I would like a finer segmentation… is that possible?</p>

---

## Post #7 by @lassoan (2019-10-07 21:17 UTC)

<p>The cylinder resolution should not matter much. You need to make fine enough the resolution of the segmentation’s labelmap representation. You can click on the segmentation geometry button (next to the master volume selector) to adjust this resolution.</p>

---

## Post #8 by @giovform (2019-10-08 16:14 UTC)

<p>I’ll place some pictures of what I am getting. I tried to set the resolution as you told, but no success. I could only downgrade the resolution, not get a finer one for the segmentation cylinder.</p>
<p>Here is the original volume rendered, it is smooth:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a2cf8a2fb3685b84cda5dec7d2cea5cbf02ed994.png" data-download-href="/uploads/short-url/nei08jtkNYUiJf6v9jY26beAh5W.png?dl=1" title="Anota%C3%A7%C3%A3o%202019-10-08%20130835" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a2cf8a2fb3685b84cda5dec7d2cea5cbf02ed994_2_690x424.png" alt="Anota%C3%A7%C3%A3o%202019-10-08%20130835" data-base62-sha1="nei08jtkNYUiJf6v9jY26beAh5W" width="690" height="424" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a2cf8a2fb3685b84cda5dec7d2cea5cbf02ed994_2_690x424.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a2cf8a2fb3685b84cda5dec7d2cea5cbf02ed994.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a2cf8a2fb3685b84cda5dec7d2cea5cbf02ed994.png 2x" data-dominant-color="3D3D3D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Anota%C3%A7%C3%A3o%202019-10-08%20130835</span><span class="informations">734×452 95.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Here is the segmentation cylinder created:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c2cbd5f7e9c6363d878becd2ccc7d885a74acde3.png" alt="Anota%C3%A7%C3%A3o%202019-10-08%20131144" data-base62-sha1="rNflq2GldYK3VnLN2EEzgokVvH5" width="630" height="476"></p>
<p>And here is the resulting volume extracted using a Mask:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/efea4416cc61d26c8d88d907626bf0bf15440bdd.png" data-download-href="/uploads/short-url/yeo1JvTs5AUBhnQRkHRHLnEuhI1.png?dl=1" title="Anota%C3%A7%C3%A3o%202019-10-08%20131302" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/efea4416cc61d26c8d88d907626bf0bf15440bdd_2_643x500.png" alt="Anota%C3%A7%C3%A3o%202019-10-08%20131302" data-base62-sha1="yeo1JvTs5AUBhnQRkHRHLnEuhI1" width="643" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/efea4416cc61d26c8d88d907626bf0bf15440bdd_2_643x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/efea4416cc61d26c8d88d907626bf0bf15440bdd.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/efea4416cc61d26c8d88d907626bf0bf15440bdd.png 2x" data-dominant-color="4A4B56"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Anota%C3%A7%C3%A3o%202019-10-08%20131302</span><span class="informations">663×515 94.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>As you can see, it is very different from the segmentation surface and the original volume. It has lost its “resolution”.</p>
<p>I tried smoothing the segmentation, using the segment editor, but also no success. Any ideas?</p>
<p>Thanks!</p>

---

## Post #9 by @lassoan (2019-10-08 16:31 UTC)

<p>You need to set the finer resolution in the segmentation before you add the cylinder segment.</p>

---

## Post #10 by @giovform (2019-10-08 17:39 UTC)

<p>Hmm, interesting, I’ve seem to hit a bug. The steps are:</p>
<ul>
<li>
<p>load a volume (DICOM);</p>
</li>
<li>
<p>create a segmentation and change the oversampling factor, of my volume as source geometry, to a value larger than 1.00 (I tried 1.25 and 1.5);</p>
</li>
<li>
<p>use the Scissors tool with a circle, to fill inside. The segmentation indeed becomes smoother than without setting the oversampling;</p>
</li>
<li>
<p>use this segmentation as a Mask, with some fill outside value. The resulting new volume doesn’t appear at all.</p>
</li>
</ul>
<p>I repeated those steps without changing the oversampling factor, and got a resulting volume. These tests were done with Slicer 4.10.2 and Slicer 4.11.0-2019-09-01.</p>

---

## Post #11 by @lassoan (2019-10-08 18:18 UTC)

<p>Do you have any error in the application log?</p>

---

## Post #12 by @giovform (2019-10-08 18:22 UTC)

<p>No. No errors. The masked volume just doesn’t appear.</p>

---

## Post #13 by @lassoan (2019-10-08 18:48 UTC)

<p>I’ve found the issue and fixed it in rev28538 (available tomorrow in Preview Release).</p>
<p>Until then, a workaround is to create segments <em>after</em> you’ve updated the segmentation geometry.</p>

---

## Post #14 by @giovform (2019-10-09 14:02 UTC)

<p>Thank you again Andras. One more question. How could I set the oversampling factor programmatically? I’ve tried this, but got no modifications to my segmentation:</p>
<pre><code>    segmentationGeometryLogic = slicer.vtkSlicerSegmentationGeometryLogic()
    segmentationGeometryLogic.SetInputSegmentationNode(segmentationNode)
    segmentationGeometryLogic.SetOversamplingFactor(0.1)
    segmentationGeometryLogic.SetSourceGeometryNode(inputVolume)
    segmentationGeometryLogic.CalculateOutputGeometry()
</code></pre>
<p>Edit: I have placed this code just after creating my segmentation node, and before creating any segments.</p>

---

## Post #15 by @giovform (2019-10-10 21:35 UTC)

<p>Well, tried other path, I was sure it would work, but now I am kind of out of options. My code is as shown (note that despite telling to show the Segmentation Geometry Widget, it doesn’t appear):</p>
<pre><code>    segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")

    # create segment editor to get access to effects
    segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
    segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
    segmentEditorWidget.show()  # just to check if everything is setup correctly
    slicer.savedWidget = segmentEditorWidget
    segmentEditorNode = slicer.vtkMRMLSegmentEditorNode()
    slicer.mrmlScene.AddNode(segmentEditorNode)
    segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)

    segmentationGeometryWidget = slicer.qMRMLSegmentationGeometryWidget()
    segmentationGeometryWidget.setMRMLScene(slicer.mrmlScene)
    segmentationGeometryWidget.setParent(segmentEditorWidget)
    segmentEditorWidget.show()  # just to check if everything is setup correctly
    segmentationGeometryWidget.setOversamplingFactor(0.05)
    segmentationGeometryWidget.setSegmentationNode(segmentationNode)
    segmentationGeometryWidget.setSourceNode(inputVolume)
    segmentationGeometryWidget.setParent(segmentEditorWidget)
    segmentationGeometryWidget.setReferenceImageGeometryForSegmentationNode()
    segmentationGeometryWidget.updateGeometry()
    segmentationGeometryWidget.update()
</code></pre>
<p>I have called a lot of methods, in the hope they would apply the new Oversampling I wanted to test.</p>

---

## Post #16 by @lassoan (2019-10-10 23:25 UTC)

<p>You never call <code>show()</code> for segmentationGeometryWidget, so it is not displayed. Anyway, you only need qMRMLSegmentationGeometryWidget if you want users to interactively change parameters on a GUI. If you just want to change the geometry from a script (without user interaction) then you can use <a href="https://apidocs.slicer.org/master/classvtkSlicerSegmentationGeometryLogic.html" rel="nofollow noopener">vtkSlicerSegmentationGeometryLogic</a> class instead.</p>

---

## Post #17 by @giovform (2019-10-11 02:28 UTC)

<p>My bad, indeed it was supposed to be a call to show the Geometry Widget… copy, paste and some tiredness I guess. I thought I was supposed to use the Geometry Widget because I am using the Segment Editor Widget to apply some effects, so I went the same route.</p>
<p>Despite that, my first solution, just above my last answer was what you told. The code snippet is:</p>
<pre><code>    # changing the segmentation resolution
    segmentationGeometryLogic = slicer.vtkSlicerSegmentationGeometryLogic()
    segmentationGeometryLogic.SetInputSegmentationNode(segmentationNode)
    segmentationGeometryLogic.SetOversamplingFactor(0.1)
    segmentationGeometryLogic.SetSourceGeometryNode(inputVolume)
    segmentationGeometryLogic.CalculateOutputGeometry()
</code></pre>
<p>This code is inserted before any segments are created, but it doesn’t take effect on my segments added later in the code. I don’t know what else I could set to make it work. I tried to find some example script and searched the forum, but nothing, so I am kinda lost on this matter.</p>

---

## Post #18 by @lassoan (2019-10-11 04:41 UTC)

<p>You calculated the output geometry but did not set it in the segmentation. You can do it like this:</p>
<pre><code class="lang-python">segmentationGeometryLogic = slicer.vtkSlicerSegmentationGeometryLogic()
segmentationGeometryLogic.SetInputSegmentationNode(segmentationNode)
segmentationGeometryLogic.SetSourceGeometryNode(segmentationNode)
segmentationGeometryLogic.SetUserSpacing([0.5,0.5,0.5])
segmentationGeometryLogic.CalculateOutputGeometry()
geometryImageData = segmentationGeometryLogic.GetOutputGeometryImageData()
geometryString = slicer.vtkSegmentationConverter.SerializeImageGeometry(geometryImageData)
segmentationNode.GetSegmentation().SetConversionParameter(
    slicer.vtkSegmentationConverter.GetReferenceImageGeometryParameterName(), geometryString)
</code></pre>
<p>If you just want to prescribe some fixed spacing then you can do it even simpler, just setting the reference image geometry directly. A complete example:</p>
<pre><code class="lang-python"># Create segmentation node

segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
segmentationNode.CreateDefaultDisplayNodes() 

# Set segmentation resolution (for closed surface to binary labelmap conversion)
geometryImageData = slicer.vtkOrientedImageData()
geometryImageData.SetSpacing(0.15, 0.15, 0.15)
geometryString = slicer.vtkSegmentationConverter.SerializeImageGeometry(geometryImageData)
segmentationNode.GetSegmentation().SetConversionParameter(
    slicer.vtkSegmentationConverter.GetReferenceImageGeometryParameterName(), geometryString)

# Add segment from polydata

cyl = vtk.vtkCylinderSource()
cyl.SetRadius(20.0)
cyl.SetHeight(60.0)
cyl.SetResolution(60)
cyl.CappingOff()

modeller = vtk.vtkImplicitModeller()
modeller.SetInputConnection(cyl.GetOutputPort())
modeller.SetAdjustDistance(0.20) # make sure the thickened model fits in output bounds

thickness = 5.0
contourFilter = vtk.vtkContourFilter()
contourFilter.SetInputConnection(modeller.GetOutputPort())
contourFilter.SetValue(0, thickness/2.0)
contourFilter.Update()

segmentationNode.AddSegmentFromClosedSurfaceRepresentation(contourFilter.GetOutput(), "Cylinder", [0.0, 1.0, 0.0])
</code></pre>

---

## Post #19 by @giovform (2019-10-14 16:48 UTC)

<p>It worked Andras. It would be difficult to find this out on my own at my current stage of understanding about the Slicer and VTK. Thank you!</p>

---

## Post #20 by @lassoan (2019-10-14 19:00 UTC)

<p>Segmentation internal labelmap representation geometry is unfortunately quite complicated. We are still improving the API to make common tasks easier to do. For example setting the segment resolution should be achievable by a single line of code (instead of the current 4 lines).</p>

---
