# Change shell thickness

**Topic ID**: 15081
**Date**: 2020-12-16
**URL**: https://discourse.slicer.org/t/change-shell-thickness/15081

---

## Post #1 by @Hamid (2020-12-16 01:47 UTC)

<p>I made a thick shell with t=2mm using “Hollow”. How can I add thickness to the shell for example I want to get the 5 mm thick(add 3 mm to the exist shell)? There are some limitation to get back to the original lumen so I have to work on the 2 mm shell to get the 5mm thickness.I need this additional 3mm thickness to be added to the outer surface of the shell.<br>
When I use Hollow to do this for one more time the result is not what I want!!</p>

---

## Post #2 by @lassoan (2020-12-16 02:08 UTC)



---

## Post #3 by @lassoan (2020-12-16 02:12 UTC)

<p>You can fill the inside of the shell (so that it is solid again) and then run the Hollow effect again.</p>
<p>If the shell is watertight (you did not cut it open) then you can fill it right away using Islands effect’s Add island method.</p>
<p>If it is open then you can plug in the open ends (for example, using Paint effect), then use Islands effect. Or, if the shape is mostly convex, then you can fill internal holes using Wrap Solidify effect (provided by SurfaceWrapSolidify extension).</p>

---

## Post #4 by @Hamid (2021-12-01 17:28 UTC)

<p>I want to give a lumen a thickness of less than 1 mm. Is it possible to do in Slicer 3D? If so how? the minimum thickness I can get is 1.5 mm!<br>
Many thanks</p>

---

## Post #5 by @lassoan (2021-12-01 17:34 UTC)

<p>The minimum wall thickness that you can represent in the binary labelmap representation of a segmentation is a single voxel. If your voxel size is 1.5mm then the minimum wall thickness is 1.5mm.</p>
<p>You can either <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#segmentation-is-not-accurate-enough">increase the resolution of the segmentation</a> or export the segmentation to a model and use Hollow tool in Dynamic Modeler module (in a recent Slicer Preview Release).</p>

---

## Post #7 by @Hamid (2021-12-03 23:26 UTC)

<p>I want to modify a STL file in Slicer 3D, but when I open the stl file in the software the "segment editor " is inactive. How can I modify my stl file in Slicer?</p>

---

## Post #8 by @Hamid (2021-12-03 23:27 UTC)

<p>Many thanks for the answer</p>

---

## Post #9 by @lassoan (2021-12-04 03:33 UTC)

<p>You need to select a master volume before editing (that defines the origin, spacing, and axis directions of the editable labelmap representation of the segment). See detailed instructions <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#editing-a-segmentation-imported-from-model-surface-mesh-file">here</a>.</p>

---

## Post #10 by @Hamid (2021-12-06 15:11 UTC)

<p>Thank you so much. It works now</p>

---

## Post #11 by @Hamid (2022-10-28 15:39 UTC)

<p>Hello,<br>
What would be the best way to resolve this in Slicer5.03?<br>
I’m using the Hollow to create a shell, but for the thickness lower than 1 mm it says not feasible at this resolution. I need the thickness of 0.5 mm.<br>
Many thanks in advance</p>

---

## Post #12 by @lassoan (2022-10-28 17:13 UTC)

<p>You need to increase the resolution of the segmentation. See instructions <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#segmentation-is-not-accurate-enough">here</a>.</p>

---

## Post #13 by @Hamid (2022-10-28 18:09 UTC)

<p>when, I select my source geometry from there the spacing options are inactive, but by increasing the oversampling factor the spacing values can be changed to a desired value. The problem is, my 3D lumen will be disappeared when click on ok.</p>

---

## Post #14 by @Hamid (2022-10-28 20:38 UTC)

<p>I got that.<br>
By setting the oversampling factor to 2, spacing values can be changed to 0.5 mm. which is my interest. The problem is, the smoothness of new lumen drastically decreased. Any solution to this? Two snapshots of before and after the process are attached. Is the only way using the smoothing?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cb5fd360b0cfec9272a76283608c8241c10dd932.jpeg" data-download-href="/uploads/short-url/t18eocSme4ddtZvTs1DEuokBPZ8.jpeg?dl=1" title="after" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb5fd360b0cfec9272a76283608c8241c10dd932_2_372x500.jpeg" alt="after" data-base62-sha1="t18eocSme4ddtZvTs1DEuokBPZ8" width="372" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb5fd360b0cfec9272a76283608c8241c10dd932_2_372x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cb5fd360b0cfec9272a76283608c8241c10dd932.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cb5fd360b0cfec9272a76283608c8241c10dd932.jpeg 2x" data-dominant-color="6B8E95"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">after</span><span class="informations">545×731 57.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6baaa2a7e4f35228d0ec4ac9da0f56e63429a0c6.png" data-download-href="/uploads/short-url/fmsFMD91uTV23Oh33L0Pil8dBMq.png?dl=1" title="before" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6baaa2a7e4f35228d0ec4ac9da0f56e63429a0c6_2_377x500.png" alt="before" data-base62-sha1="fmsFMD91uTV23Oh33L0Pil8dBMq" width="377" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6baaa2a7e4f35228d0ec4ac9da0f56e63429a0c6_2_377x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6baaa2a7e4f35228d0ec4ac9da0f56e63429a0c6.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6baaa2a7e4f35228d0ec4ac9da0f56e63429a0c6.png 2x" data-dominant-color="6C8E96"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">before</span><span class="informations">548×726 75.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #15 by @lassoan (2022-10-30 02:16 UTC)

<p>After changing the voxel size you must apply smoothing effect to eliminate aliasing caused by oversampling.</p>
<p>You can avoid smoothing by increasing the segmentation’s resolution before painting anything.</p>

---
