---
topic_id: 29733
title: "Updating Segmentationnode With Oversampled Labelmap"
date: 2023-05-30
url: https://discourse.slicer.org/t/29733
---

# Updating segmentationNode with oversampled labelmap

**Topic ID**: 29733
**Date**: 2023-05-30
**URL**: https://discourse.slicer.org/t/updating-segmentationnode-with-oversampled-labelmap/29733

---

## Post #1 by @danpak94 (2023-05-30 18:18 UTC)

<p>Hello,</p>
<p>I’m trying to do the following:<br>
(1) oversample a labelmap<br>
(2) modify it in the higher resolution voxel space<br>
(3) update the segmentation node with the modified labelmap</p>
<p>I figured out (1) and (2), but I couldn’t find info on (3).</p>
<p>Any help would be greatly appreciated.</p>
<p>Below is a demo of what I mean:</p>
<pre><code class="lang-auto">def apply_oversampling_on_segmentationNode(segmentationNode, inputVolumeNode, oversampling_factor):
    segmentationGeometryLogic = slicer.vtkSlicerSegmentationGeometryLogic()
    if segmentationGeometryLogic.GetOversamplingFactor() != oversampling_factor:
        segmentationGeometryLogic.SetInputSegmentationNode(segmentationNode)
        segmentationGeometryLogic.SetSourceGeometryNode(inputVolumeNode)
        segmentationGeometryLogic.SetOversamplingFactor(oversampling_factor)
        segmentationGeometryLogic.CalculateOutputGeometry()
        geometryImageData = segmentationGeometryLogic.GetOutputGeometryImageData()
        geometryString = slicer.vtkSegmentationConverter.SerializeImageGeometry(geometryImageData)
        segmentationNode.GetSegmentation().SetConversionParameter(slicer.vtkSegmentationConverter.GetReferenceImageGeometryParameterName(), geometryString)
        segmentationGeometryLogic.ResampleLabelmapsInSegmentationNode()
    else:
        geometryImageData = segmentationGeometryLogic.GetOutputGeometryImageData()
    return geometryImageData

def get_dims_spacing_origin_from_vtkImageData(geometryImageData):
    dims = geometryImageData.GetDimensions()
    spacing = geometryImageData.GetSpacing()
    origin = geometryImageData.GetOrigin()
    return dims, spacing, origin

def modifySegment(segmentArray):
    # some random modification
    return np.clip(segmentArray + np.random.rand(*segmentArray.shape), 0, 1)

# (1) works
geometryImageData = apply_oversampling_on_segmentationNode(segmentationNode, inputVolumeNode, oversampling_factor=3)
dims, spacing, origin = get_dims_spacing_origin_from_vtkImageData(geometryImageData) # I can use this to get the correct closed surface representation

# (2) works
segmentId = segmentationNode.GetSegmentation().GetSegmentIdBySegmentName(segment_name)
segmentArray = slicer.util.arrayFromSegmentInternalBinaryLabelmap(segmentationNode, segmentId)

newSegmentArray = modifySegment(segmentArray.copy())

# (3) how do I do this properly??
slicer.util.updateSegmentBinaryLabelmapFromArray(newSegmentArray, segmentationNode, segmentId, referenceVolumeNode=inputVolumeNode)
</code></pre>

---

## Post #2 by @lassoan (2023-05-30 19:36 UTC)

<p>See a complete solution in this topic (using vtkSlicerSegmentationGeometryLogic):</p>
<aside class="quote" data-post="4" data-topic="26411">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/resample-segments-in-segmentation-using-python-scripting/26411/4">Resample segments in segmentation using Python scripting</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    This should resample all the segments in the segmentation using the current geometry: 
segmentationNode = getNode('Segmentation')
segGeomLogic = slicer.vtkSlicerSegmentationGeometryLogic()
segGeomLogic.SetInputSegmentationNode(segmentationNode)
segGeomLogic.SetSourceGeometryNode(segmentationNode)
segGeomLogic.CalculateOutputGeometry()
segGeomLogic.ResampleLabelmapsInSegmentationNode()
  </blockquote>
</aside>


---

## Post #3 by @danpak94 (2023-05-30 20:39 UTC)

<p>Thank you for the response.</p>
<p>This actually looks like a repeat of my posted code: <code>apply_oversampling_on_segmentationNode</code></p>
<p>I want to add a new <em>modified</em> oversampled labelmap to segmentationNode.</p>
<p>How can I do this properly?</p>

---

## Post #4 by @lassoan (2023-05-30 20:53 UTC)

<p>Once the segmentation has the resolution that you need, I would recommend to import the new segments from a labelmap node and delete the old segment (or use Logical operators effect’s Copy method).</p>
<p>You could use <code>slicer.vtkOrientedImageDataResample.ModifyImage</code> to manipulate an existing segment, but it is very hard to do it correctly due to multiple segments sharing a labelmap and further complicated by masking settings.</p>

---

## Post #5 by @danpak94 (2023-06-03 01:18 UTC)

<p>I am able to get the correct resolution using <code>segGeomLogic.ResampleLabelmapsInSegmentationNode()</code>, but when I try to edit the segment with the new resolution (brush, erase, etc.), it seems to return to the original resolution.</p>
<p>How can I prevent this from happening?</p>

---

## Post #6 by @lassoan (2023-06-03 03:29 UTC)

<p>Make sure the master (source) representation is binary labelmap. If it is then give us more information so that we can reproduce what your see and can tell if it is the expected behaviour or something is wrong.</p>

---

## Post #7 by @danpak94 (2023-06-03 11:39 UTC)

<p>If you are referring to the master representation setting as shown below, I believe I do have binary labelmap as my master representation.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b2852fc9c21cf0e181725a12ac60bd34ab482a33.png" alt="image" data-base62-sha1="ptgl8iIBcmL3j6mFvpWFssCfaFR" width="479" height="97"></p>
<p>I’m trying to do the following:</p>
<ol>
<li>Resample label maps programmatically using the code below</li>
<li>Edit the resulting segments with segment editor (brush, erase, etc.)</li>
</ol>
<p>Expected behavior: Labelmap geometry stays as resampled<br>
Observed behavior: Labelmap geometry converts back to the original geometry before resampling<br>
Test: Specifying Geometry using this button (<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b912a202d86be4d7203deb28ae131957df5a8846.png" alt="image" data-base62-sha1="qpefFxG1j31y98RpBMm4lcCRAy2" width="30" height="28">) results in the expected behavior</p>
<pre><code class="lang-auto">segmentationGeometryLogic = slicer.vtkSlicerSegmentationGeometryLogic()
segmentationGeometryLogic.SetInputSegmentationNode(segmentationNode)
segmentationGeometryLogic.SetSourceGeometryNode(inputVolumeNode)
segmentationGeometryLogic.SetOversamplingFactor(oversampling_factor)
segmentationGeometryLogic.CalculateOutputGeometry()
geometryImageData = segmentationGeometryLogic.GetOutputGeometryImageData()
segmentationGeometryLogic.ResampleLabelmapsInSegmentationNode()
</code></pre>

---

## Post #8 by @danpak94 (2023-06-04 12:01 UTC)

<p>With respect to this suggestion:</p>
<ol>
<li>
<p>I successfully created a new segment using <code>slicer.modules.segmentations.logic().ImportLabelmapToSegmentationNode(labelmap_vtkImageData, segmentationNode, segmentName)</code>.</p>
</li>
<li>
<p>But the stored labelmap is clipped to the effective extent. What’s the best way to retrieve the full extent numpy array from the original vtkImageData?</p>
</li>
</ol>

---

## Post #9 by @lassoan (2023-06-04 12:06 UTC)

<aside class="quote no-group" data-username="danpak94" data-post="8" data-topic="29733">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/danpak94/48/18310_2.png" class="avatar"> danpak94:</div>
<blockquote>
<p>What’s the best way to retrieve the full extent numpy array from the original vtkImageData?</p>
</blockquote>
</aside>
<p>I would use convenience functions in <code>slicer.util</code> or specify reference volume for the segmentation export.</p>

---

## Post #10 by @danpak94 (2023-06-05 13:13 UTC)

<p>Note to myself and maybe future developers:</p>
<ol>
<li>I tried to directly work with vtkImageData without creating a new volume node, but everything worked much better if I just create a volume node for the reference geometry.</li>
</ol>
<p>Updating labelmap:<br>
<code> slicer.util.updateSegmentBinaryLabelmapFromArray(segmentArray.transpose([2,1,0]), segmentationNode, segmentId, referenceVolumeNode=geometryVolumeNode)</code></p>
<p>Retrieving labelmap numpy array:<br>
<code>segmentArray = slicer.util.arrayFromSegmentBinaryLabelmap(segmentationNode, segmentId, referenceVolumeNode=geometryVolumeNode)</code></p>
<ol start="2">
<li>For labelmaps with different resolutions, it’s much easier if I just create separate segmentationNodes.</li>
</ol>

---

## Post #11 by @lassoan (2023-06-05 15:35 UTC)

<p>Thanks for sharing your experience. Indeed, it makes things simpler if the reference image geometry that is set in the segmentation is the same as the current segmentation geometry.</p>

---
