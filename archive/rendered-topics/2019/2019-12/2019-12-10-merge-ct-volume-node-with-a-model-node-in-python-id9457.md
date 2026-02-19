---
topic_id: 9457
title: "Merge Ct Volume Node With A Model Node In Python"
date: 2019-12-10
url: https://discourse.slicer.org/t/9457
---

# Merge CT volume node with a model node in python

**Topic ID**: 9457
**Date**: 2019-12-10
**URL**: https://discourse.slicer.org/t/merge-ct-volume-node-with-a-model-node-in-python/9457

---

## Post #1 by @talmazov (2019-12-10 04:17 UTC)

<p>I know 3D slicer can merge two volume/slice nodes from separate CT data but is it possible to merge an PLY/STL loaded model node with a CT volume/slice node?</p>

---

## Post #2 by @pieper (2019-12-10 14:12 UTC)

<p>Yes, you can load PLY/STL models and display them with the CT.  But because those formats don’t define a reference space they may not align.  See <a href="https://discourse.slicer.org/t/incorrect-overlay-of-vti-and-stl-from-the-same-dicom-series/6828/4">this post</a> for example.</p>

---

## Post #3 by @talmazov (2019-12-11 02:31 UTC)

<p>Not quite what I was referring to. For example, we obtain 2 nodes as such<br>
ply_node = slicer.util.getNode(‘model_name’)<br>
ct_node = slicer.util.getNode(‘ct_name’)<br>
merged_node = merge(ply_node, ct_node)<br>
such that merged_node contains the image/volume data from both nodes</p>

---

## Post #4 by @lassoan (2019-12-11 03:50 UTC)

<p>How do you envision combining models and volumes? Would you like to end up with a model or a volume?</p>
<p>You can import a model into a segmentation and then use Segment Editor’s Mask volume effect (provided by SegmentEditorExtraEffects extension) to paste the segment into the volume.</p>

---

## Post #5 by @talmazov (2019-12-17 23:44 UTC)

<p>hey, i found have this from the nightly script repository</p>
<blockquote>
<p>meshVolumeNode = getNode(mesh_model)<br>
seg = slicer.mrmlScene.AddNewNodeByClass(‘vtkMRMLSegmentationNode’)<br>
slicer.modules.segmentations.logic().ImportModelToSegmentationNode(meshVolumeNode, seg)<br>
seg.CreateClosedSurfaceRepresentation()<br>
slicer.mrmlScene.RemoveNode(meshVolumeNode)</p>
</blockquote>
<p>once i have a segment volume node, how can i merge it with a CT volume node?<br>
also what is the function SetAndObserveImageData used for? the VTK documentation doesn’t explain much.</p>
<p>I’m working on an extension that builds around panoramic reconstruction which essentially straightens a volume: <a href="https://discourse.slicer.org/t/slice-rotation-in-viewport-when-using-setslicetorasbyntp-in-python/7191/2" class="inline-onebox">Slice rotation in viewport when using SetSliceToRASByNTP in python - #2 by lassoan</a><br>
but i also want this reconstruction to incorporate mesh models so im trying to merge volumes - im not sure if this is the correct approach to this.</p>
<p>thanks!</p>

---

## Post #6 by @lassoan (2019-12-18 01:25 UTC)

<aside class="quote no-group quote-modified" data-username="talmazov" data-post="5" data-topic="9457">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/talmazov/48/3966_2.png" class="avatar"> talmazov:</div>
<blockquote>
<p>I’m working on an extension that builds around panoramic reconstruction which essentially straightens a volume: <a href="https://discourse.slicer.org/t/slice-rotation-in-viewport-when-using-setslicetorasbyntp-in-python/7191/2">Slice rotation in viewport when using SetSliceToRASByNTP in python</a><br>
but i also want this reconstruction to incorporate mesh models so im trying to merge volumes - im not sure if this is the correct approach to this.</p>
</blockquote>
</aside>
<p>OK, this explains everything.</p>
<p>You can create 3D panoramic reconstructions using this recently added module: <a href="https://discourse.slicer.org/t/how-to-implement-cpr-curved-plannar-reconstruction-from-centerline/9456/3" class="inline-onebox">How to implement CPR (curved planar reconstruction) from centerline? - #3 by lassoan</a></p>
<p>To display models in the same way, you can import the model to segmentation node, from there export as a labelmap volume node, and then apply curved planar reconstruction to the labelmap volume.</p>
<p>An alternative approach would be to create a grid transform from the transformed corner points of the slices, but this would require a little bit of Python scripting. This method would be particularly useful for transforming sparse point sets (landmark points, lines, curves), which cannot be well represented by image volumes. It would be nice if you could work on this we can help you to get started.</p>

---

## Post #7 by @talmazov (2019-12-18 03:40 UTC)

<p>Woa this is really neat! I didn’t realize this feature had been implemented. Ultimately I’m trying to do implant planning so having the an stl/ply mesh representation of the implant shown in the pan tomographic representation would be really useful.<br>
Can I merge segmentation with ct node in order to use it as an input volume for CPR?<br>
Or can multiple volume node inputs be implemented?</p>

---

## Post #8 by @lassoan (2019-12-18 06:35 UTC)

<p>You can “paint” an STL model into a CT by importing the STL model into a segmentation then use Mask volume effect (provided by SegmentEditorExtraEffects extension) in Segment Editor module.</p>
<p>Model painted into CBCT volume using Mask volume effect:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2ab3503f9a1895d3cdb79825ce9f972b7d5a13c5.jpeg" data-download-href="/uploads/short-url/65Kekl1pUKp1MWEQ7elwrS762XP.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2ab3503f9a1895d3cdb79825ce9f972b7d5a13c5_2_690x438.jpeg" alt="image" data-base62-sha1="65Kekl1pUKp1MWEQ7elwrS762XP" width="690" height="438" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2ab3503f9a1895d3cdb79825ce9f972b7d5a13c5_2_690x438.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2ab3503f9a1895d3cdb79825ce9f972b7d5a13c5_2_1035x657.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2ab3503f9a1895d3cdb79825ce9f972b7d5a13c5_2_1380x876.jpeg 2x" data-dominant-color="BFBDBD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2256×1434 695 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #9 by @talmazov (2019-12-20 17:21 UTC)

<p>The Mask Volume works beautifully with the CPR extension. One caveat I have though is that when I use mask volume, the segment color turns gray once projected onto the CT volume. so when I use the CPR extension to transform the gray color of the segment blends against the gray values of the CT volume.<br>
any workaround for that?</p>

---

## Post #10 by @lassoan (2019-12-20 17:42 UTC)

<aside class="quote no-group" data-username="talmazov" data-post="9" data-topic="9457">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/talmazov/48/3966_2.png" class="avatar"> talmazov:</div>
<blockquote>
<p>when I use the CPR extension to transform the gray color of the segment blends against the gray values of the CT volume.<br>
any workaround for that?</p>
</blockquote>
</aside>
<p>In mask volume effect, you can pick the gray color intensity. Probably you want to set a high value to indicate that the implant is very dense material.</p>

---

## Post #11 by @talmazov (2019-12-21 14:36 UTC)

<p>hey,<br>
i saw on the nightly script repository an example on how to access scripted modules. I want to access the mask volume effect, i am trying this<br>
slicer.modules.segmenteditoreffect.widgetRepresentation().maskVolumeWithSegment()<br>
but i get that module ‘modules’ has no attribute ‘segmenteditoreffect’</p>

---

## Post #12 by @lassoan (2019-12-21 14:40 UTC)

<p>You can learn from these examples how to use Segment Editor effects from scripts: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script</a></p>

---

## Post #13 by @talmazov (2020-09-23 02:16 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="9457">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>An alternative approach would be to create a grid transform from the transformed corner points of the slices, but this would require a little bit of Python scripting. This method would be particularly useful for transforming sparse point sets (landmark points, lines, curves), which cannot be well represented by image volumes. It would be nice if you could work on this we can help you to get started.</p>
</blockquote>
</aside>
<p>Hey,<br>
I am working on an extension that would greatly benefit from being able to accomplish this - transforming any model object outline when straightening out the volume along the path. Any pointers where to begin?<br>
I implemented the mask workaround you suggested but it is insufficient, as you mentioned, in visualizing sparse point sets like model outlines, points and lines.</p>

---

## Post #14 by @lassoan (2020-09-23 02:21 UTC)

<p>I’ve already implemented this in Curved Planar Reformat module. It can now create a transform that you can use to transform implants, landmark points, models, etc. between the original and straightened volume.</p>

---

## Post #15 by @talmazov (2020-09-25 00:20 UTC)

<p>Hey,<br>
Amazing piece of code from the Curve Planar Reformat module. I managed to implement it and it works well.<br>
I have arch form intraoral models and those transform really well. when i add a cylindrical implant type object however, it not transformed how i expected. this happens w/ simple cylinder of only a few vertices, as well as higher density cylinder-type meshes</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/7674855a78e6f7c46731a917e7a15eefc002874f.jpeg" data-download-href="/uploads/short-url/gTTZ9MkjHh4gANzSUvYtdmSmD4b.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7674855a78e6f7c46731a917e7a15eefc002874f_2_453x500.jpeg" alt="image" data-base62-sha1="gTTZ9MkjHh4gANzSUvYtdmSmD4b" width="453" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7674855a78e6f7c46731a917e7a15eefc002874f_2_453x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7674855a78e6f7c46731a917e7a15eefc002874f_2_679x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7674855a78e6f7c46731a917e7a15eefc002874f_2_906x1000.jpeg 2x" data-dominant-color="312F31"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1168×1289 374 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I am not quite sure why some objects do not transform as well. you can see that the implant is centered over the curve. any thoughts?<br>
I set transformSpacingFactor = 0.1 in your code, i can’t tell if it improved things. should i made the value even smaller?</p>
<p>Thanks!</p>

---

## Post #16 by @lassoan (2020-09-25 01:12 UTC)

<p>If the slice size is too large or curve resolution is too fine then in some regions you can have transform that maps the same point into different positions (the displacement field folds into itself). In these regions the transforms in not invertible.</p>
<p>To reduce these ambiguously mapped regions, decrease <code>Slice size</code>. If necessary <code>Curve resolution</code> can be slightly increased as well (it controls how densely the curve is sampled to generate the displacement field, if samples are farther from each other then it may reduce chance of contradicting samples).</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8e50fee58f58d8c0a6f3bc9a7f53a2ef6a873b87.png" alt="image" data-base62-sha1="kiZkF5yo0spM5JTHEEpAp920oJ1" width="561" height="379"></p>
<p>You can quickly validate the transform, by going to Transforms module and in Display/Visualization section check all 3 checkboxes, the straightened image as <code>Region</code> and visualization mode to <code>Grid</code>.</p>
<p>For example, this transform results in a smooth displacement field, it is invertible in the visualized region:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/045048696d683fffafbea801edeb05cc1349abd5.png" data-download-href="/uploads/short-url/C9UJH78k6tC2pmAXHSqHcnHzRr.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/045048696d683fffafbea801edeb05cc1349abd5_2_690x420.png" alt="image" data-base62-sha1="C9UJH78k6tC2pmAXHSqHcnHzRr" width="690" height="420" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/045048696d683fffafbea801edeb05cc1349abd5_2_690x420.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/045048696d683fffafbea801edeb05cc1349abd5_2_1035x630.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/045048696d683fffafbea801edeb05cc1349abd5_2_1380x840.png 2x" data-dominant-color="9E9497"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1375 639 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If the slice size is increased then folding occurs:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fdfffd96e1dbc2e84485e9b2c6bce54169736860.png" data-download-href="/uploads/short-url/AeZfX8pqa4lURFdwn8ePBH5F0oE.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fdfffd96e1dbc2e84485e9b2c6bce54169736860_2_489x500.png" alt="image" data-base62-sha1="AeZfX8pqa4lURFdwn8ePBH5F0oE" width="489" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fdfffd96e1dbc2e84485e9b2c6bce54169736860_2_489x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fdfffd96e1dbc2e84485e9b2c6bce54169736860_2_733x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fdfffd96e1dbc2e84485e9b2c6bce54169736860_2_978x1000.png 2x" data-dominant-color="55373B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1200×1225 382 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Probably you can find a parameter set that works for a large group of patients. Maybe one parameter set works for all, but maybe you need to have a few different presets (small, medium, large)</p>

---

## Post #17 by @Ackta (2023-02-16 16:28 UTC)

<p>Hi, can you explain how can i convert implant from ct to cpr?Thanks</p>

---

## Post #18 by @lassoan (2023-02-16 18:55 UTC)

<p>You can transform the implant model from the original CT to the straightened image by applying the straightening transform to the implant model.</p>

---

## Post #19 by @talmazov (2023-02-16 19:02 UTC)

<p>CT to CPR? What is CPR format, I haven’t heard of it before?</p>

---

## Post #20 by @Ackta (2023-02-17 15:23 UTC)

<p>Thanks for the  replay,but i cannot integrate the implant in to the Original CBCT</p>

---

## Post #21 by @Ackta (2023-02-17 16:04 UTC)

<p>CPR is Curve Plane Reformat,Please Can you explain me how did you have reformatted the image with th model and the implant, i`m not able to do that.</p>

---

## Post #22 by @talmazov (2023-02-17 18:25 UTC)

<p>Lines 530-650</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/dentsoft-foundation/slicerPano/blob/aec57df0ae56b8566fb1fab94673a2baca47bbb6/SlicerPano/SlicerPano/SlicerPano.py#L530">
  <header class="source">

      <a href="https://github.com/dentsoft-foundation/slicerPano/blob/aec57df0ae56b8566fb1fab94673a2baca47bbb6/SlicerPano/SlicerPano/SlicerPano.py#L530" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/dentsoft-foundation/slicerPano/blob/aec57df0ae56b8566fb1fab94673a2baca47bbb6/SlicerPano/SlicerPano/SlicerPano.py#L530" target="_blank" rel="noopener nofollow ugc">dentsoft-foundation/slicerPano/blob/aec57df0ae56b8566fb1fab94673a2baca47bbb6/SlicerPano/SlicerPano/SlicerPano.py#L530</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="520" style="counter-reset: li-counter 519 ;">
          <li>    sliceToRas.DeepCopy(transform.GetMatrix())</li>
          <li>    sliceNode.UpdateMatrices()</li>
          <li>
          <li>  sliceNode.Modified()</li>
          <li>
          <li>  widget = slicer.app.layoutManager().sliceWidget(viewNode)</li>
          <li>  view = widget.sliceView()</li>
          <li>  view.forceRender()</li>
          <li>
          <li># adapted from the Curved Planar Reformat extension - Andras Lasso &amp; Jean-Christophe Fillion-Robin</li>
          <li class="selected">def straightenVolume(self, outputStraightenedVolume, curveNode, volumeNode, sliceSizeMm, outputSpacingMm, rotationAngleDeg=0.0):</li>
          <li>  """</li>
          <li>  Compute straightened volume (useful for example for visualization of curved vessels)</li>
          <li>  """</li>
          <li>  originalCurvePoints = curveNode.GetCurvePointsWorld()</li>
          <li>  sampledPoints = vtk.vtkPoints()</li>
          <li>  if not slicer.vtkMRMLMarkupsCurveNode.ResamplePoints(originalCurvePoints, sampledPoints, outputSpacingMm[2], False):</li>
          <li>    return False</li>
          <li>
          <li>  sliceExtent = [int(sliceSizeMm[0]/outputSpacingMm[0]), int(sliceSizeMm[1]/outputSpacingMm[1])]</li>
          <li>  inputSpacing = volumeNode.GetSpacing()</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #23 by @Ackta (2023-02-19 21:33 UTC)

<p>i1ve installed slicer pano, but my menu are completley different from the video.i work with 3d slicer 5.2.1.<br>
Thanks</p>

---
