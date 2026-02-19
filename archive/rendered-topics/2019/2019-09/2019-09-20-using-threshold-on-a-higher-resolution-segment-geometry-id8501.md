---
topic_id: 8501
title: "Using Threshold On A Higher Resolution Segment Geometry"
date: 2019-09-20
url: https://discourse.slicer.org/t/8501
---

# Using threshold on a higher resolution segment geometry

**Topic ID**: 8501
**Date**: 2019-09-20
**URL**: https://discourse.slicer.org/t/using-threshold-on-a-higher-resolution-segment-geometry/8501

---

## Post #1 by @Amine (2019-09-20 04:57 UTC)

<p>Hi, suppose i create a segment from a master volume with 1x1x1mm spacing, and then i use a volume with 4x4x4mm spacing to perform a threshold on that segmentation (keeping its original geometry), the normal slicer behavior is to smooth out the threshold and the resulting image will not have 4x4x4 voxel cubic blocks but a smoothed out 1x1x1 voxels<br>
Is this behavior intended and will it be kept in the following versions? (Its very useful because it uses the maximum resolution of the segmentation’s original geometry and makes a smooth segment out of the low resolution volume instead of just extracting the 4mm voxels and making them into a 4x4x4 voxel cube)</p>

---

## Post #2 by @Sam_Horvath (2019-09-20 13:40 UTC)

<p>I believe that this is the intended behavior.  The representation of the segmentation is initialized from the master volume, and so preserves that resolution.</p>

---

## Post #3 by @Amine (2019-09-20 14:14 UTC)

<p>Segmentation nodes keep the same geometry once created unless it’s changed manually, but what i’m asking about is the behavior of threshold effect (and paint effect too) when a lower resolution volume is used on a high resolution segment. What a pure threshold effect will yield is a “pixelated” ( C) segment (in which each big cube is formed by a lot of voxels since the segmentation is higher resolution) but what it gives instead is a smoothed out segment (D) as if it ran a filter on the volume prior to the thresholding itself.</p>
<p>Furthermore, when a threshold is in preview mode (A) you can see an image so high in resolution that it does not get pixelated by zooming in, and only after it is applied that it will adapt to whatever segmentation geometry was in use, here are some pictures to better clarify:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/ca5937909ebbe7a46a4fbabeeeac0674268dcefa.png" data-download-href="/uploads/short-url/sS3AVNaOZOjM8S4VjLCxzTBSFdM.png?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/ca5937909ebbe7a46a4fbabeeeac0674268dcefa_2_510x500.png" alt="Capture" data-base62-sha1="sS3AVNaOZOjM8S4VjLCxzTBSFdM" width="510" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/ca5937909ebbe7a46a4fbabeeeac0674268dcefa_2_510x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/ca5937909ebbe7a46a4fbabeeeac0674268dcefa_2_765x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/ca5937909ebbe7a46a4fbabeeeac0674268dcefa.png 2x" data-dominant-color="687669"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">898×880 609 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>with:<br>
A) Threshold in preview mode, note the very high resolution (i would say almost vectorial?) preview<br>
B) Original volume threshold (not important here)<br>
C) Very low resolution volume if a “pure” threshold was executed, each big visible voxel thus composed of a lot of smaller ones<br>
D) The actual result with a very low resolution volume if the segmentation is higher in resolution, the very high resolution preview in A was adapted to the segmentation and the result is smooth</p>
<p>so to reformulate my question, is that volume smoothing behavior intended and would it be kept in the next versions as it is very useful</p>

---

## Post #4 by @muratmaga (2019-09-20 14:40 UTC)

<p>This seems quite convoluted. If your goal is to achieve finer representation, is there reason you are not resampling your low-resolution volume to 1x1x1mm?</p>

---

## Post #5 by @Amine (2019-09-20 14:47 UTC)

<p>Thats exactly the issue, with a resampled volume the computing time and power needed is a lot more than using a low resolution one, there is virtually no added benefit with thresholding and painting (although volume rendering does not make use of it) , that’s what makes this feature important to keep</p>

---

## Post #6 by @muratmaga (2019-09-20 14:49 UTC)

<p>I can’t comment whether behavior will be kept in feature, but you can always resample your own labelmap to higher resolution.</p>

---

## Post #7 by @Amine (2019-09-20 14:53 UTC)

<p>Thanks for your answer, Sounds like a good approach for scripted thresholding, for painting that would be cumbersome to keep painting on a labelmap and resampling it (wich is maybe what this function actually does)</p>

---

## Post #8 by @lassoan (2019-09-21 15:33 UTC)

<p>Threshold preview is very high resolution because it is applied on the displayed image slice and the screen resolution is typically much higher than the volume’s original resolution. Since we only compute this high-resolution preview for a few slices, it takes negligible amount of time and memory but to compute it for a full volume it would take about 1000x more time and memory.</p>

---

## Post #9 by @Amine (2019-09-22 00:33 UTC)

<p>Thanks for your reply,<br>
Still how come the output segment is as detailed as the used segmentation geometry allows no matter how low the used volume resolution is? The current behavior is perfect i just wanted to know if it was intentional and would be staying</p>

---

## Post #10 by @lassoan (2019-09-23 21:08 UTC)

<p>When a volume has low resolution, only this fine details are lost. Lower frequency content is restored accurately at arbitrarily fine resolution.</p>

---
