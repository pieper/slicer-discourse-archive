# Elastix: generated output image doesn't align with applied and hardend transform 

**Topic ID**: 33147
**Date**: 2023-11-30
**URL**: https://discourse.slicer.org/t/elastix-generated-output-image-doesnt-align-with-applied-and-hardend-transform/33147

---

## Post #1 by @ekls (2023-11-30 13:55 UTC)

<p>Hi,<br>
I’m quite new to slicer so maybe there‘s a very simple answer to my problem.</p>
<p>I’m currently using Elastix to registrate brain MRIs.<br>
The genereated output volume looks perfectly fine but applying the transform to the original image and it’s segmentation it looks completely different from the output volume.</p>
<p>I already looked up the other topics and found out I need to harden the transform, but still, it doesn’t match.</p>
<p>Output volume<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/84bd677c7bf6b91bd013b9948ca75ec36e61ce26.png" data-download-href="/uploads/short-url/iWgP0UMcV4xPr4oCjy6L92MCYke.png?dl=1" title="output volume" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84bd677c7bf6b91bd013b9948ca75ec36e61ce26_2_638x500.png" alt="output volume" data-base62-sha1="iWgP0UMcV4xPr4oCjy6L92MCYke" width="638" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84bd677c7bf6b91bd013b9948ca75ec36e61ce26_2_638x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/84bd677c7bf6b91bd013b9948ca75ec36e61ce26.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/84bd677c7bf6b91bd013b9948ca75ec36e61ce26.png 2x" data-dominant-color="595858"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">output volume</span><span class="informations">756×592 82 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Original data moving-MRI before applying transform<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8fc0124b78ce4452fa3d28dc596ffecfd3c8d2ed.png" data-download-href="/uploads/short-url/kvFMWN8UPZEXRUEjl6Ogbar4lY1.png?dl=1" title="original_mri" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8fc0124b78ce4452fa3d28dc596ffecfd3c8d2ed_2_690x499.png" alt="original_mri" data-base62-sha1="kvFMWN8UPZEXRUEjl6Ogbar4lY1" width="690" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8fc0124b78ce4452fa3d28dc596ffecfd3c8d2ed_2_690x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8fc0124b78ce4452fa3d28dc596ffecfd3c8d2ed.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8fc0124b78ce4452fa3d28dc596ffecfd3c8d2ed.png 2x" data-dominant-color="212020"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">original_mri</span><span class="informations">756×547 114 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Moving-MRI after applying transform and hardening transform<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/29a30e38a1324287daa12fc2d057a4cd3ba729c1.png" data-download-href="/uploads/short-url/5WkV74VN9LRyADcLYaH2w2qcmPf.png?dl=1" title="mri_transformed_and_hardend" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/29a30e38a1324287daa12fc2d057a4cd3ba729c1.png" alt="mri_transformed_and_hardend" data-base62-sha1="5WkV74VN9LRyADcLYaH2w2qcmPf" width="605" height="500" data-dominant-color="282828"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">mri_transformed_and_hardend</span><span class="informations">756×624 76.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you so much for your help!</p>

---

## Post #2 by @ekls (2023-12-06 18:07 UTC)

<p>I’m so sorry but I’m still looking for help. Could anyone possibly tell me what I’m doing wrong?</p>
<p>Thank you !</p>

---
