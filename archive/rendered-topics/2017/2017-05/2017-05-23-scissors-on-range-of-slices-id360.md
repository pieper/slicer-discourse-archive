---
topic_id: 360
title: "Scissors On Range Of Slices"
date: 2017-05-23
url: https://discourse.slicer.org/t/360
---

# Scissors on range of slices

**Topic ID**: 360
**Date**: 2017-05-23
**URL**: https://discourse.slicer.org/t/scissors-on-range-of-slices/360

---

## Post #1 by @hherhold (2017-05-23 04:12 UTC)

<p>I usually find the scissors tool to be the greatest thing since sliced bread (no pun intended). Sometimes I want to use it only on a range of slices - The only way I’ve found to do this effectively is to make a mask and use that as the editable area when using the scissors tool. Is there a quicker way to do this?</p>
<p>Thanks!</p>
<p>-Hollister</p>

---

## Post #2 by @lassoan (2017-05-23 04:15 UTC)

<p>I think using masking is the simplest way to restrict scissors. Do you have any better suggestion?</p>

---

## Post #3 by @hherhold (2017-05-23 12:21 UTC)

<p>It would be useful to be able to use the scissors starting at a slice and continuing only in a given direction, say downward, to do a “cutaway”. There are other ways of doing this, like you mentioned, using masking, so “directional scissors” would be more of a convenience.</p>

---

## Post #4 by @muratmaga (2017-05-23 17:50 UTC)

<p>I second the request that  for slices specifying the physical length would be a very useful addition to the tool. E.g. start on the slice the outline was drawn, and say +/- 10mms, or actual slice counts in that plane. …</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/677f06bdf711468707faf594c72c7993f90d2513.png" data-download-href="/uploads/short-url/eLzkAGZovUCazoJL65K1uagmWFJ.png?dl=1" title="77C3A3DB5AF54B56A741600A3E5A8000.png"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/677f06bdf711468707faf594c72c7993f90d2513.png" width="690" height="0" data-dominant-color="BFCDDB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">77C3A3DB5AF54B56A741600A3E5A8000.png</span><span class="informations">708×1 83 Bytes</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @lassoan (2017-05-24 13:24 UTC)

<p>I’ve added the option of restricting cutting in slice view to one side of the slice plane or to a specified thickness around the slice plane. It’ll be available in tomorrow’s nightly build. Let me know if this fulfills your needs.</p>

---

## Post #6 by @hherhold (2017-05-24 14:06 UTC)

<p>Will do. Thanks!!!</p>
<p>-Hollister</p>

---

## Post #7 by @muratmaga (2017-05-24 17:11 UTC)

<p>Awesome, thank you.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/677f06bdf711468707faf594c72c7993f90d2513.png" data-download-href="/uploads/short-url/eLzkAGZovUCazoJL65K1uagmWFJ.png?dl=1" title="77C3A3DB5AF54B56A741600A3E5A8000.png"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/677f06bdf711468707faf594c72c7993f90d2513.png" width="690" height="0" data-dominant-color="BFCDDB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">77C3A3DB5AF54B56A741600A3E5A8000.png</span><span class="informations">708×1 83 Bytes</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @hherhold (2017-05-24 22:04 UTC)

<p>Wow, this works great!</p>
<p>Thank you very much!</p>
<p>-Hollister</p>

---

## Post #9 by @BreadBoxGuy (2019-11-20 08:35 UTC)

<p>I have a hollow model and I would like to use the scissors so they cut only through one layer and not through the whole model. Is that possible?</p>

---

## Post #10 by @Juicy (2019-11-20 08:45 UTC)

<p>You could try this <a href="https://github.com/lassoan/SlicerSegmentationRecipes/blob/master/Craniotomy/README.md" rel="nofollow noopener">Segmentation Recipie</a> for a craniotomy which sounds like what you are describing</p>

---

## Post #11 by @Francesca_Lo_Iacono (2022-10-06 09:55 UTC)

<p>Hi ! How can I use this option?</p>

---

## Post #12 by @lassoan (2022-10-06 19:02 UTC)

<p>You can find the option in Segment Editor → Scissors effect options:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/8863013a76aed9025c4f2be36f7f32dbf4636494.png" data-download-href="/uploads/short-url/jsx3gTIJgbFfXQ7aqbTgLL0OYyo.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/8863013a76aed9025c4f2be36f7f32dbf4636494_2_517x500.png" alt="image" data-base62-sha1="jsx3gTIJgbFfXQ7aqbTgLL0OYyo" width="517" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/8863013a76aed9025c4f2be36f7f32dbf4636494_2_517x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/8863013a76aed9025c4f2be36f7f32dbf4636494_2_775x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/8863013a76aed9025c4f2be36f7f32dbf4636494_2_1034x1000.png 2x" data-dominant-color="3D4041"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1157×1118 85.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #13 by @lassoan (2023-03-21 02:18 UTC)



---
