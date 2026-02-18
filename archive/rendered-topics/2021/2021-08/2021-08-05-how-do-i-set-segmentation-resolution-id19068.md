# How do I set segmentation resolution

**Topic ID**: 19068
**Date**: 2021-08-05
**URL**: https://discourse.slicer.org/t/how-do-i-set-segmentation-resolution/19068

---

## Post #1 by @Alberto_Paredes (2021-08-05 02:40 UTC)

<p>Operating system: Windows 10<br>
Slicer version: Slicer 4.11.20210226<br>
Question: I am completely new to 3D Slicer. I was working on a segmentation and when trying to make it hollow, I was not able to with my desired shell thickness because it is not feasible at the current resolution. I believe I have to adjust the “master volume”, but I do not know how. Can you please tell me how I can adjust the resolution of my segmentation, and can you explain to me more about this “master volume”</p>

---

## Post #2 by @muratmaga (2021-08-05 03:22 UTC)

<p>If you are new to 3D Slicer, please read these two docs. It will help you greatly learning the segment editor.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html</a></p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html</a></p>
<p>What you want is doable and there are two ways to go about it:</p>
<ol>
<li>You can user the Crop Volume module on your master volume (and choose something like 0.5 scaling), to increase the voxel resolution of a new volume. Then you can use this new volume as your master volume in the segmentation.</li>
<li>If you already started with the segmentation, you can use the Segmentation Geometry option, and use oversampling (something like 2). You can think of it subdividing every voxel in segmentation by half in each dimension.</li>
</ol>
<p>Which one works better for you depends on your use case. If you can already see the boundaries you need to see in your master volume, but simply need more voxels in the segmentation to make the margin operations work, probably <span class="hashtag">#2</span> would be fine for you.</p>

---

## Post #3 by @Alberto_Paredes (2021-08-05 15:22 UTC)

<p>Thank you for your response! I want to go with option 2, but I do not see the Segmentation Geometry option. In the “Segmentation editor” page that is in the link you provided there is a section called “Segmentation is not accurate enough” and I think “Option B” is the same solution you are suggesting. There it says to “Click <em>Specify geometry</em> button in Segment Editor any time to specify smaller spacing.”<br>
However, I do not see the <em>Specify Geometry</em> button on the Segment Editor Module either.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/13f4536d96b025546617821630445030d72eeb62.jpeg" data-download-href="/uploads/short-url/2Qwxl5QJlei5CR64jnjniZrDG3E.jpeg?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/13f4536d96b025546617821630445030d72eeb62_2_303x500.jpeg" alt="Capture" data-base62-sha1="2Qwxl5QJlei5CR64jnjniZrDG3E" width="303" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/13f4536d96b025546617821630445030d72eeb62_2_303x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/13f4536d96b025546617821630445030d72eeb62_2_454x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/13f4536d96b025546617821630445030d72eeb62_2_606x1000.jpeg 2x" data-dominant-color="EDEDED"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">621×1023 78.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @muratmaga (2021-08-05 20:21 UTC)

<p>Your screenshot is cutting the top part of the module. It is this small button above the segments list:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/17b38e2d9e891f3bb593ec3e32e031a051fb2caf.png" data-download-href="/uploads/short-url/3nFG08BQnJYsWiGaDSdeJ36UGar.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/17b38e2d9e891f3bb593ec3e32e031a051fb2caf.png" alt="image" data-base62-sha1="3nFG08BQnJYsWiGaDSdeJ36UGar" width="551" height="499" data-dominant-color="383C3E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">649×588 31.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
