# Intersection between two models (vtkMRMLModelNode)

**Topic ID**: 625
**Date**: 2017-07-05
**URL**: https://discourse.slicer.org/t/intersection-between-two-models-vtkmrmlmodelnode/625

---

## Post #1 by @robmbar (2017-07-05 02:39 UTC)

<p>Hello Slicer developers,</p>
<p>I am looking for a way of updating a model, cutting the intersection of two models (vtkMRMLModelNode) as shown in the image.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/2199d4e2ab7153a78d454fef6d02611049ed8f9a.PNG" data-download-href="/uploads/short-url/4Nfl1MoyuzgYH1gWSIt0cpA71zQ.PNG?dl=1" title="CaptureSlicer.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/2199d4e2ab7153a78d454fef6d02611049ed8f9a_2_641x500.PNG" width="641" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/2199d4e2ab7153a78d454fef6d02611049ed8f9a_2_641x500.PNG, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/2199d4e2ab7153a78d454fef6d02611049ed8f9a_2_961x750.PNG 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/2199d4e2ab7153a78d454fef6d02611049ed8f9a_2_1282x1000.PNG 2x" data-dominant-color="76797C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">CaptureSlicer.PNG</span><span class="informations">1749×1363 184 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Basically, I would like to remove the corner of the cube according to the intersection between the cube and the sphere. There is a Merge Module that joins the both models. Here, I want that to remove the intersection between the models. Do someone know how can I face it?</p>
<p>Thank you so much,<br>
Roberto Barbosa</p>

---

## Post #2 by @lassoan (2017-07-05 02:44 UTC)

<p>Using <code>Segmentations</code> module: create a <code>Segmentation</code> node and import both models into it. Then go to <code>Segment editor</code> module and using <code>Logical operators</code> effect compute the intersection. Export the resulting segment to model node using <code>Segmentations</code> module.</p>
<p>You need to select a <code>Master volume</code> for the <code>Segment editor</code> module to work. If you don’t have any image then just load <em>any</em> volume (anything in the <code>Sample data</code> module will do) and adjust its extent and resolution using Crop volumes mode.</p>

---

## Post #3 by @robmbar (2017-07-05 18:23 UTC)

<p>Thank you so much for your quick reply and the important information provided, Andras Lasso. However, I am not being able to perform that. I followed your tips, I have downloaded the CTChest Sample Data once I did not have any volume, imported the both models into a segmentation node and selected the Segment Editor. Here, I selected the CTChest as Master volume and when I press the logical operators button appears this dialogue box window:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/df86a3a5eb9948326c0197253882ece51e286c55.png" alt="image" data-base62-sha1="vToWebrIWuMadFcx1H66R3t7zX7" width="564" height="363"></p>
<p>After that, the models are reshaped, as shown in the next image, and the operators don’t work.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/d7cd71e9ad247f022a443c9cb8af21bef94b6fd2.jpg" data-download-href="/uploads/short-url/uN4OPXvTXXofu2DXzNvLqvSnqDM.jpg?dl=1" title="CaptureSlicer2.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/d7cd71e9ad247f022a443c9cb8af21bef94b6fd2_2_608x500.jpg" width="608" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/d7cd71e9ad247f022a443c9cb8af21bef94b6fd2_2_608x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/d7cd71e9ad247f022a443c9cb8af21bef94b6fd2_2_912x750.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/d7cd71e9ad247f022a443c9cb8af21bef94b6fd2_2_1216x1000.jpg 2x" data-dominant-color="6398A6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">CaptureSlicer2.jpg</span><span class="informations">1468×1207 143 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2017-07-05 19:28 UTC)

<p>I’ve just tried it and it works well, but there are a few things to pay attention to:</p>
<ul>
<li>Use the latest nightly version.</li>
<li>CTChest volume’s spacing is quite high (resolution is low) and they are different on each axis. You must use <code>Crop volume</code> module to make the spacing values smaller (finer resolution, by lowering <code>Spacing scale</code>) and same along all axes (by enabling <code>Isotropic spacing</code>). Adjust the extent of the volume to be just as big as you need it, by click-and-dragging sides of the ROI widget in slice views.</li>
<li>After importing the models into segmentation node, hide or delete the models.</li>
<li>In <code>Segment Editor</code> <code>Logical operators</code> effect, make sure you select one segment in the segment list above and another segment in the segment list (“Intersect with segment”) below.</li>
<li>After clicking Apply, hide or delete the other segment so that you can clearly see the intersection.</li>
</ul>

---

## Post #5 by @robmbar (2017-07-06 01:05 UTC)

<p>Thank you! Now it’s clear to me. It works well! I’ve played with the tools in the logical operators and I’ve concluded that the right operator to my application is the subtraction. Thus, I can remove from the cube, all the intersection volume and keep the sphere intact.<br>
It would be great to implement the python code to perform this procedure in my module. Could you point me in the right direction to achieve that?</p>

---

## Post #6 by @lassoan (2017-07-06 01:58 UTC)

<p>Thanks for the update. I’m glad it worked. See this page for examples of how to use Segment Editor effects in your own module: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script</a></p>

---
