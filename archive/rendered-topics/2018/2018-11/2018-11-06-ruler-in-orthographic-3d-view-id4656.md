# Ruler in (orthographic) 3D view

**Topic ID**: 4656
**Date**: 2018-11-06
**URL**: https://discourse.slicer.org/t/ruler-in-orthographic-3d-view/4656

---

## Post #1 by @stephan (2018-11-06 15:38 UTC)

<p>Operating system: Win 7 64 bit<br>
Slicer version: 4.10.0<br>
Expected behavior: Ruler button in 3D view inserts ruler into (orthographic) 3D view<br>
Actual behaviour:<br>
Neither “thin” nor “thick” ruler makes a ruler appear. The ruler menu item is marked as active, though.<br>
Toggling between perspective and orthographic view doesn’t help, either.<br>
Nor does showing/hiding the 3D cube and/or axis labels make the ruler appear.</p>
<p>This is probably a rarely used feature, and probably a measurement between two points of interest serves most purposes better. But in this case I simply need a rough size marker in a 3D scene, and so a ruler similar to those in the slice views would be perfect.</p>
<p>Am I missing something or is the feature simply broken at the moment?</p>
<p>Thanks<br>
Stephan</p>

---

## Post #2 by @stephan (2018-11-06 15:42 UTC)

<p>It was a user error. <img src="https://emoji.discourse-cdn.com/twitter/confounded.png?v=6" title=":confounded:" class="emoji" alt=":confounded:"><br>
Literally moments after posting this, I realized that a white ruler on white background simply can’t be seen. So I reset my 3D background to the blue default, and there it is.</p>
<p>It would be nice, however, if the ruler would adapt to the background color (i.e. being drawn in black if the background is white).</p>

---

## Post #3 by @cpinter (2018-11-06 16:00 UTC)

<p>Indeed. Just 10 minutes ago I was struggling to read the length measurement of a ruler:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d9a742615edf914626d46c4f2620f00c3f1a9be9.png" alt="image" data-base62-sha1="v3rXFMewpCQHFWCOFc1g3rkbeCR" width="105" height="59"></p>
<p>The current state of the module that also contains the ruler functionality (i.e. Annotations) is that it’s deprecated, and thus not maintained, especially considering convenience features such as this. There has been quite a push to re-create annotation tools (ruler, angle measurement, even splines) recently, but it has proven to be technologically quite challenging (due to the VTK widget infrastructure). Hopefully in the next several months there can be some progress made on this. Fingers crossed!</p>
<p>Btw thanks for reporting the issue and also following up on it.</p>

---

## Post #4 by @lassoan (2018-11-06 16:37 UTC)

<p>Just to clarify, <a class="mention" href="/u/cpinter">@cpinter</a> referred to <em>annotation</em> ruler as not maintained.</p>
<p>View rulers (see below) are stable and fully maintained.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/4264cb13dea4850919b59e1b5a7476d9adb2b5fd.jpeg" alt="image" data-base62-sha1="9tlsCxsj0PFiIwVLYlSl7zkYClf" width="381" height="326"></p>
<p>We could make them appear with shadowing to make them visible over both dark and bright background - I’ve added a <a href="https://issues.slicer.org/view.php?id=4651">feature request</a> for this. Most likely it will be implemented if more users ask for it, a funded project will need it, or somebody volunteers his/her time to implement it and send a pull request.</p>

---

## Post #5 by @stephan (2018-11-06 16:53 UTC)

<p>Thanks <a class="mention" href="/u/cpinter">@cpinter</a> and <a class="mention" href="/u/lassoan">@lassoan</a>.<br>
Yes, I was referring to the view ruler/scale as shown in <a class="mention" href="/u/lassoan">@lassoan</a>’s reply.<br>
Shadowing seems a good solution.</p>

---

## Post #6 by @aiden.zhu (2020-01-06 22:31 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> <a class="mention" href="/u/lassoan">@lassoan</a> a quick question about  the 3D-view ruler:</p>
<p>Right after I do " threeDView.resetFocalPoint() " in python, I would like to have a ruler scaled in the same level as all other 3-slice-views. Say, in the slice-viewers, I have a ruler of 5mm, then I would like to have a same one in the 3D-viewer. So via python, is there a way to automatically set up the ruler in the 3D-viewer  to match them inside the slice-viewers?</p>
<p>Thanks a lot.</p>

---

## Post #7 by @lassoan (2020-01-07 00:01 UTC)

<p>You can add an observer to the slice node and whenever it is changed, run this script:</p>
<pre><code class="lang-python"># Get scale factor from slice view
sliceNode = slicer.mrmlScene.GetNodeByID('vtkMRMLSliceNodeRed')
sliceNodeFovMm = sliceNode.GetFieldOfView()[1]
sliceNodeFovPixels = sliceNode.GetDimensions()[1]
viewScaleMmPerPixel = sliceNodeFovMm/float(sliceNodeFovPixels)

# Set scale factor in 3D view
threeDview = slicer.app.layoutManager().threeDWidget(0).threeDView()
viewHeightPixels = threeDview.renderWindow().GetSize()[1]
cameraNode = slicer.modules.cameras.logic().GetViewActiveCameraNode(threeDview.mrmlViewNode())
viewHeightMm = viewHeightPixels * viewScaleMmPerPixel
cameraNode.SetParallelScale(viewHeightMm/2.0)
</code></pre>

---

## Post #8 by @aiden.zhu (2020-01-07 15:41 UTC)

<p>Thank you so much. It works wonderfully well after I just set up a connection:</p>
<pre><code class="lang-python">layoutManager = slicer.app.layoutManager()
layoutManager.layoutChanged.connect(self.autoZoomOf3DViewer) 

  
def autoZoomOf3DViewer(self):
      
      #old_layout = slicer.app.layoutManager().layout
      #slicer.app.layoutManager().layout = slicer.vtkMRMLLayoutNode.SlicerLayoutFourUpView

      # Get scale factor from slice view
      sliceNode = slicer.mrmlScene.GetNodeByID('vtkMRMLSliceNodeRed')
      sliceNodeFovMm = sliceNode.GetFieldOfView()[1]
      sliceNodeFovPixels = sliceNode.GetDimensions()[1]
      viewScaleMmPerPixel = sliceNodeFovMm/float(sliceNodeFovPixels)

      # Set scale factor in 3D view threeDview==&gt;threeDView
      threeDView = slicer.app.layoutManager().threeDWidget(0).threeDView()
      threeDView.resetFocalPoint() 
      viewHeightPixels = threeDView.renderWindow().GetSize()[1]
      cameraNode = slicer.modules.cameras.logic().GetViewActiveCameraNode(threeDView.mrmlViewNode())
      viewHeightMm = viewHeightPixels * viewScaleMmPerPixel
      cameraNode.SetParallelScale(viewHeightMm/2.0)
</code></pre>

---

## Post #9 by @Andreza (2021-12-06 18:58 UTC)

<p>I’m trying to put the ruler bar, but the scale of the ruler is wrong (the whole animal has about 5cm and when I try zooming at one piece of the animal (p.e. cranial bones), the software shows them as 25cm). How can I adjust it?</p>

---

## Post #10 by @muratmaga (2021-12-06 19:41 UTC)

<p>Slicer reports whatever is in the data. There is no calibration of the ruler. You need to correct the scale of the data. If this is a 3D volume, go to volumes module and check the image spacing and cross-reference to the known pixel spacing of the data.</p>
<p>If it is a 3D model given to you, you need to find what units those were in…</p>

---

## Post #11 by @Andreza (2021-12-09 16:22 UTC)

<p>Thank you. It is a reconstruction 3D that I did from the slices (2D images), I know the pixel resolution is 9, but I don’t know the image spacing. I didn’t find the cross-reference in the software too (just the image dimensions, spacing and origin)</p>

---

## Post #12 by @muratmaga (2021-12-09 16:58 UTC)

<p>In most cases pixel resolution is the same as image spacing. How you tried putting 0.009, 0.009, 0.009 as your image spacing in the volumes module and see if the ruler issue gets corrected.</p>

---

## Post #13 by @Andreza (2022-02-01 13:22 UTC)

<p>It didn’t work. There is no difference in the ruler bar. The pixel size is 8.72, so I wrote 0.008, 0.008, 0.008, nothing changed. Then I tried with 0.00872, the same result, so I wrote 0.009 and also nothing changed.</p>

---

## Post #14 by @muratmaga (2022-02-01 17:45 UTC)

<p>Did you reset the field of view after you change the spacing? Alternatively, you can toggle the visibility of the volume in the Data module for the changes to take effect.</p>

---

## Post #15 by @Andreza (2022-02-10 20:00 UTC)

<p>Yes, I did. Nothing changed. I’m using a TIFF file and one NRRD file, none of them I can change the ruler bar. I also tried in a DCM file, and the result was the same.</p>

---

## Post #16 by @muratmaga (2022-02-10 20:06 UTC)

<p>There must be something amiss in the steps: This is a sample data from Slicer, which has slice spacing of 1,1,1.3mm. I made a clone of this, and edited the image spacing to be 0.5, 0.5, 0.625 (half of the original), and then hit the FOV button and you can see the ruler is different and scaled correctly. I suspect you are missing a step in between. Perhaps try with the same data first, and see that it works.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/45dbaa6cce94436b5016a4b51c3e82feacd40cd0.png" data-download-href="/uploads/short-url/9XZzMnrgQcbxeGsGPfsS8Zgx0Pu.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/45dbaa6cce94436b5016a4b51c3e82feacd40cd0_2_536x500.png" alt="image" data-base62-sha1="9XZzMnrgQcbxeGsGPfsS8Zgx0Pu" width="536" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/45dbaa6cce94436b5016a4b51c3e82feacd40cd0_2_536x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/45dbaa6cce94436b5016a4b51c3e82feacd40cd0_2_804x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/45dbaa6cce94436b5016a4b51c3e82feacd40cd0_2_1072x1000.png 2x" data-dominant-color="BBBBBA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1509×1407 248 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #17 by @Andreza (2022-02-11 14:15 UTC)

<p>It worked in 2D images!<br>
I realized that I didn’t do one step you told me to (hit the FOV button).<br>
Thank you so much.</p>

---

## Post #18 by @Andreza (2022-02-15 13:55 UTC)

<p>But I tried for 3D model, and it didn’t work. Do you know what could be?</p>

---

## Post #19 by @muratmaga (2022-02-15 15:28 UTC)

<p>You have to be in the orthographic projection for ruler to show in 3d view. You are probably in perspective rendering mode.</p>

---

## Post #20 by @Andreza (2022-02-15 16:31 UTC)

<p>No, I’m in the orthographic projection already. The ruler bar in 2D imagens shows correctly the scale (for example 5mm), but the reconstruction of the structure shows 25cm, for example.<br>
The same occurs when I’m using the ruler to measures structures in the 3D model.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e2df60442840f51e4ea440acdc68204c7a9e9f8.jpeg" data-download-href="/uploads/short-url/21r9E34liGdDys9iIYtEtjfCnkA.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0e2df60442840f51e4ea440acdc68204c7a9e9f8_2_690x482.jpeg" alt="image" data-base62-sha1="21r9E34liGdDys9iIYtEtjfCnkA" width="690" height="482" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0e2df60442840f51e4ea440acdc68204c7a9e9f8_2_690x482.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0e2df60442840f51e4ea440acdc68204c7a9e9f8_2_1035x723.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e2df60442840f51e4ea440acdc68204c7a9e9f8.jpeg 2x" data-dominant-color="BFBDC1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1319×923 201 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #21 by @muratmaga (2022-02-15 17:05 UTC)

<p>This means the scale of the 3D data (these segmentation) are wrong. Did you create them after you modified the image spacing of your volume or before? Because if you created them before, they will have the wrong scale.</p>

---

## Post #22 by @Andreza (2022-02-15 17:13 UTC)

<p>I did the segmentation before putting the ruler bar. So, do I have to do the segmentation again to get the correct ruler in 3D image?</p>

---

## Post #23 by @muratmaga (2022-02-15 17:22 UTC)

<p>As you are observing, it is important to check that the imported image stack has the correct image spacing as the first step of your workflow. Since everything else (segmentations → models → measurements) are all dependent on this piece of information. This is especially true if you importing these images from 2D formats like PNG/TIFF etc which doesn’t preserve this information.</p>
<p>You don’t have to redo the segmentation but it will take you a few steps to get them in correct alignment. This is what I would suggest (<a class="mention" href="/u/lassoan">@lassoan</a> is there a simpler fix?)</p>
<ol>
<li>Go to <code>segmentations</code> module export your current segmentation as a label map</li>
<li>After the export right-click on the exported labelmap and choose “Edit Properties”</li>
<li>This will take you <code>Volumes</code> module where you can cross reference the slice spacing, dimensions, and IJK matrix of the master volume and this labelmap. Expand the Volume Information tab (see below). Everything reported for the labelmap should match to that of the master volume. You can use the dropdown button to switch between the original volume and the labelmap. (see below)</li>
<li>Once the labelmap is fixed, you can right click and choose “Convert to labelmap to segmentation”.<br>
This new segmentation should have the right spacing, Delete everything else…</li>
</ol>
<p>Next time, you’d help yourself if you use the <a href="https://github.com/SlicerMorph/Tutorials/blob/main/ImageStacks/README.md"><code>ImageStacks</code> from SlicerMorph</a> extension and then enter the correct spacing in the module and then import the stack.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8c634367e34a069bcbe5503d36f7ab6f31545e4e.png" data-download-href="/uploads/short-url/k1Vw1sYx2gNY1T5Ot4DbbsOvYTA.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8c634367e34a069bcbe5503d36f7ab6f31545e4e.png" alt="image" data-base62-sha1="k1Vw1sYx2gNY1T5Ot4DbbsOvYTA" width="555" height="500" data-dominant-color="F5F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1062×956 29.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #24 by @lassoan (2022-02-15 18:32 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="23" data-topic="4656">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>You don’t have to redo the segmentation but it will take you a few steps to get them in correct alignment. This is what I would suggest (<a class="mention" href="/u/lassoan">@lassoan</a> is there a simpler fix?)</p>
</blockquote>
</aside>
<p>If the segmentation has unit spacing, zero origin, RAS-axis-aligned IJK axes then you can transform it to the correct space by applying the IJKToRAS matrix of the volume. You can type this to the Python console (replace <code>MRHead</code> and <code>Segmentation</code> by the name of the volume and segmentation nodes):</p>
<pre data-code-wrap="python"><code class="lang-python">ijkToRas = vtk.vtkMatrix4x4()
getNode('MRHead').GetIJKToRASMatrix(ijkToRas)
getNode('Segmentation').ApplyTransformMatrix(ijkToRas)
</code></pre>

---

## Post #25 by @Andreza (2022-02-15 19:39 UTC)

<p>I tried 3 times the first step and got the same answer:<br>
The computer has 64 RAM memory and I run the 3D Slicer at an SSD</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/8155c06a7c0f0cb6cd632995cf51f3b99529a196.png" alt="image" data-base62-sha1="is9jzxo0kfidZE4pkIYy6r1PGqa" width="510" height="243"></p>

---

## Post #26 by @muratmaga (2022-02-15 19:47 UTC)

<p><a class="mention" href="/u/andreza">@Andreza</a> when you are reporting an issue, please also report at what step you get this error. Are you following my instructions or <a class="mention" href="/u/lassoan">@lassoan</a>?</p>
<p>This means you have ran out of memory, probably your volume is very big (or you have too many things open at the same time). You can choose to increase the virtual memory (perhaps something like 128GB) as the error says, and rerun the things. It will take slower, but you shouldn’t encounter this problem.</p>

---
