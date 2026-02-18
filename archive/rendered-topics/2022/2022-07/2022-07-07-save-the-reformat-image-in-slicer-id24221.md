# Save the reformat image in Slicer

**Topic ID**: 24221
**Date**: 2022-07-07
**URL**: https://discourse.slicer.org/t/save-the-reformat-image-in-slicer/24221

---

## Post #1 by @Shahin (2022-07-07 14:12 UTC)

<p>After spinning an image in different axes, how to save the reformatted image as a .nii file?</p>

---

## Post #2 by @muratmaga (2022-07-07 17:00 UTC)

<aside class="quote no-group" data-username="Shahin" data-post="1" data-topic="24221">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shahin/48/15728_2.png" class="avatar"> Shahin:</div>
<blockquote>
<p>After spinning an image in different axes,</p>
</blockquote>
</aside>
<p>it is not clear how you mean by “spining image in different axes”. if you use <code>Transforms</code> module, you should harden you transform (right click on volume, and choose harden Transform), and save it as nii.</p>
<p>If you used `Mouse Interaction’ widget to rotate the slice views, then you haven’t done anything to your data, you can’t really save that to the disk.</p>

---

## Post #3 by @lassoan (2022-07-07 18:00 UTC)

<p>I find that interactive reslicing of an image is the easiest by using Crop Volume module. You can rotate the ROI as described here: <a href="https://discourse.slicer.org/t/saving-a-select-view-as-a-dicom-file/24227/2" class="inline-onebox">Saving a select view as a DICOM file - #2 by lassoan</a></p>

---

## Post #4 by @Shahin (2022-07-08 07:21 UTC)

<p>I work with the “Reformat” widget. You can either you mouse interaction or sliders on the widget to transform the box of the image. I need to save the image in the new-generated box after reformatting it.</p>
<p>The “Transforms” widget may also work. But, when I change the values (e.g., Rotation), I cannot visulaize the result of that (the rotated image). Then, I do not know what I saving.</p>
<p>So, I do not know if I have explained it properly, but I need to rotate the image and save the result in the new box as a new image.<br>
Any method might suggest for that?</p>
<p>Bests,<br>
Shahin</p>

---

## Post #5 by @lassoan (2022-07-10 13:53 UTC)

<p>Have you tried the method that I described at the post linked above? It requires manual alignment of the ROI or a short Python code snippet that does this adjustment automatically.</p>
<p>We don’t provide a convenient GUI for this because this is not commonly needed (if any module needs the current image slice it can easily retrieve it). What is the clinical problem that you would like to solve? What approach/tools do you plan to use for it?</p>

---

## Post #6 by @ma_apan (2025-03-21 13:43 UTC)

<p>Hi everyone<br>
I have the same or at least a similar problem. I would like to register a brain atlas on my 3d mrt images in order to subsequently perform a BET. However, the atlas and my images are not aligned in the same way. I have therefore tried to reformat the atlas with the reformat module. Here I can first arrange the planes in the correct axes and then rotate them so that the format matches my images.<br>
however, I also have the problem that I cannot save these reformatted slices.<br>
I have already tried the transform module and crop volume model, but it just won’t work.<br>
Can anyone help me?<br>
Many thanks in advance</p>

---
