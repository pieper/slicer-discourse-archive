---
topic_id: 15309
title: "Nearby Fiducial Points At Different Slices"
date: 2021-01-01
url: https://discourse.slicer.org/t/15309
---

# Nearby fiducial points at different slices

**Topic ID**: 15309
**Date**: 2021-01-01
**URL**: https://discourse.slicer.org/t/nearby-fiducial-points-at-different-slices/15309

---

## Post #1 by @FatihSogukpinar (2021-01-01 19:56 UTC)

<p>Hi all,</p>
<p>I have a set of fiducial points which have the same anterior/posterior coordinates (but different right/left and sagittal coordinates) and I want to be able to show them in the same coronal slice.<br>
Despite that I see the same AP coordinates in their .fcsv file, when I load them to Slicer and look at them in the Red slice view, they seem to be at slightly different slices (0.1 - 0.2 mm different AP).<br>
What might the reason for that ? How can I carry all of them to the same Coronal slice ?</p>
<p>Thanks !</p>

---

## Post #2 by @FatihSogukpinar (2021-01-07 21:05 UTC)

<p>Any suggestions about this ?<br>
Thanks.</p>

---

## Post #3 by @lassoan (2021-01-07 23:26 UTC)

<p>It is not clear what you want to achieve and what the problem is. A few annotated screenshots and a sample .mrb scene file would help.</p>

---

## Post #4 by @FatihSogukpinar (2021-01-08 02:58 UTC)

<p>Ok, here are some example pics <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf212bdf0f2bae6aad948b1d07337e896a4f88f0.jpeg" data-download-href="/uploads/short-url/rgOgvfjvF2XIP6PitNnI0iTAkU0.jpeg?dl=1" title="slicer1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bf212bdf0f2bae6aad948b1d07337e896a4f88f0_2_546x500.jpeg" alt="slicer1" data-base62-sha1="rgOgvfjvF2XIP6PitNnI0iTAkU0" width="546" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bf212bdf0f2bae6aad948b1d07337e896a4f88f0_2_546x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bf212bdf0f2bae6aad948b1d07337e896a4f88f0_2_819x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bf212bdf0f2bae6aad948b1d07337e896a4f88f0_2_1092x1000.jpeg 2x" data-dominant-color="5E5E5E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer1</span><span class="informations">2097×1917 241 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a3fce40e137ee012de4b8e5805416580da227e2.jpeg" data-download-href="/uploads/short-url/aAQ2dNi1z8zGPMjSQJBFNf7AxxM.jpeg?dl=1" title="slicer2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4a3fce40e137ee012de4b8e5805416580da227e2_2_546x500.jpeg" alt="slicer2" data-base62-sha1="aAQ2dNi1z8zGPMjSQJBFNf7AxxM" width="546" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4a3fce40e137ee012de4b8e5805416580da227e2_2_546x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4a3fce40e137ee012de4b8e5805416580da227e2_2_819x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4a3fce40e137ee012de4b8e5805416580da227e2_2_1092x1000.jpeg 2x" data-dominant-color="5E5E5E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer2</span><span class="informations">2097×1917 240 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8b4823e1f02f21b03cfb16f4a1a10de5b44b78d3.jpeg" data-download-href="/uploads/short-url/jS8Vxb1brA5sHX9HUEG13WsRfmH.jpeg?dl=1" title="slicer3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8b4823e1f02f21b03cfb16f4a1a10de5b44b78d3_2_546x500.jpeg" alt="slicer3" data-base62-sha1="jS8Vxb1brA5sHX9HUEG13WsRfmH" width="546" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8b4823e1f02f21b03cfb16f4a1a10de5b44b78d3_2_546x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8b4823e1f02f21b03cfb16f4a1a10de5b44b78d3_2_819x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8b4823e1f02f21b03cfb16f4a1a10de5b44b78d3_2_1092x1000.jpeg 2x" data-dominant-color="5E5E5E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer3</span><span class="informations">2097×1917 240 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>The fiducials you see in the slices have the same anterior coordinates, but despite that, they are shown in different coronal slices. Those coronal slices are really close (seperated by just 0.1 mm), BUT I want to show all of those points in the “exact” same slice.</p>
<p>How can I achieve this ? This is really  important for me.<br>
Thank you and best regards.</p>

---

## Post #5 by @FatihSogukpinar (2021-01-08 19:03 UTC)

<p>Any suggestions ?<br>
Thanks</p>

---

## Post #6 by @lassoan (2021-01-08 20:28 UTC)

<p>Slicer shows all markups at +/- half slice spacing distance from the current slice plane.</p>
<p>From the images that you attached it seems that your images are not exactly aligned with anatomical axes (the image is slightly rotated). Therefore, slices cut through multiple image slices.</p>
<p>Click <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-view">“Rotate to volume plane” button</a> in the slice view controller to align slice views with your image axes (instead of anatomical axes).</p>

---

## Post #7 by @FatihSogukpinar (2021-01-08 22:41 UTC)

<p>Hmm… Thanks a lot !</p>
<p>Is it possible to obtain the transform matrix for that transformation ?</p>
<p>Thank you.</p>

---

## Post #8 by @lassoan (2021-01-09 04:12 UTC)

<p>You can get the slice view’s position and orientation as a 4x4 homogeneous transformation matrix by calling <code>GetSliceToRAS()</code> method on the slice node.</p>

---

## Post #9 by @lassoan (2021-01-10 22:56 UTC)

<p>A post was split to a new topic: <a href="/t/how-to-transform-fiducial-coordinates-into-image-space/15442">How to transform fiducial coordinates into image space</a></p>

---
