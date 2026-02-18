# Merging masks of nifti format and assigning conductivities to each

**Topic ID**: 34401
**Date**: 2024-02-19
**URL**: https://discourse.slicer.org/t/merging-masks-of-nifti-format-and-assigning-conductivities-to-each/34401

---

## Post #1 by @savvy73 (2024-02-19 17:54 UTC)

<p>Hi, I have masks of different regions of brain in niftii format. I want to combine all the masks and assign conductivities to the same after which I need to mesh the output. I wanted to know if it can be done using 3D slicer. Your help is very much appriciated</p>

---

## Post #2 by @muratmaga (2024-02-20 00:35 UTC)

<aside class="quote no-group" data-username="savvy73" data-post="1" data-topic="34401">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/da6949/48.png" class="avatar"> savvy73:</div>
<blockquote>
<p>I have masks of different regions of brain in niftii format.</p>
</blockquote>
</aside>
<p>If these are from the same brain, they you can load each mask as a segmentation, and then use the <code>Segmentations</code> module to copy them into a single segmentation. See the user documentation</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html</a></p>

---

## Post #4 by @savvy73 (2024-02-21 02:45 UTC)

<p>Thank you for your response. I tried doing it, but the output file is missing some segments. I am attaching the images below.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a16b86f250f504817f72013e9dd801465f47251c.png" data-download-href="/uploads/short-url/n1ZfpuloL1xmrqITMALRLnpXYW8.png?dl=1" title="Screenshot from 2024-02-21 03-31-25" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a16b86f250f504817f72013e9dd801465f47251c_2_690x431.png" alt="Screenshot from 2024-02-21 03-31-25" data-base62-sha1="n1ZfpuloL1xmrqITMALRLnpXYW8" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a16b86f250f504817f72013e9dd801465f47251c_2_690x431.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a16b86f250f504817f72013e9dd801465f47251c_2_1035x646.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a16b86f250f504817f72013e9dd801465f47251c_2_1380x862.png 2x" data-dominant-color="AFAAB3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2024-02-21 03-31-25</span><span class="informations">1920×1200 418 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d8b201fbd5da6bcba732a178d1c707a44803378b.png" data-download-href="/uploads/short-url/uUYvPJWKWJQst64QwQutK4OEZtN.png?dl=1" title="Screenshot from 2024-02-21 03-43-59" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d8b201fbd5da6bcba732a178d1c707a44803378b_2_690x392.png" alt="Screenshot from 2024-02-21 03-43-59" data-base62-sha1="uUYvPJWKWJQst64QwQutK4OEZtN" width="690" height="392" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d8b201fbd5da6bcba732a178d1c707a44803378b_2_690x392.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d8b201fbd5da6bcba732a178d1c707a44803378b_2_1035x588.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d8b201fbd5da6bcba732a178d1c707a44803378b_2_1380x784.png 2x" data-dominant-color="A8A4AE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2024-02-21 03-43-59</span><span class="informations">1850×1053 119 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>What I am trying to do is to add the masks and label them in a single file after which I can assign conductivities to do simulations. The segmentations after adding all the masks are what I want. Is there a way to label them? Also, I am not sure why the output is missing segments.</p>

---

## Post #5 by @muratmaga (2024-02-21 03:17 UTC)

<p>I can’t tell what labels are missing from your screenshots. I am not seeing any spaces in segmentation.</p>
<p>You can rename them in whichever you like, double click the segment names and enter your text. You can also use the Terminology module and use standard DICOM anatomical terms to label your segments.</p>

---
