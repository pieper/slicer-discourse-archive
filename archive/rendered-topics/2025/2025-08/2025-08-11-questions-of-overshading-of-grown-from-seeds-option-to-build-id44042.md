# Questions of overshading of Grown from seeds option to build up bronchus model

**Topic ID**: 44042
**Date**: 2025-08-11
**URL**: https://discourse.slicer.org/t/questions-of-overshading-of-grown-from-seeds-option-to-build-up-bronchus-model/44042

---

## Post #1 by @jamesgyh (2025-08-11 06:39 UTC)

<p>Hi everyone here, after I checked the video <a href="https://www.youtube.com/watch?v=9iiOBmaP8bA" rel="noopener nofollow ugc">https://www.youtube.com/watch?v=9iiOBmaP8bA</a> of growing from seeds, I immediately started up my trial on my CT case, however, even though I zoomed in a lot on the small bronchi, the airway build always takes part from the lung, and the smaller bronchi can’t be built nicely. How can I fix these problems?</p>

---

## Post #2 by @lassoan (2025-08-11 06:47 UTC)

<p>It should be no problem segmenting up to 3-4 generations (level of branching) of bronchi, which should be sufficient for surgical planning. Up to how many generations are you trying to segment?Can you post a few screenshots?</p>
<p>One thing to pay attention when you correct seeds in low-contrast areas that you always need to paint on both sides of the boundary (when you paint a bit of “airway” inside a bronchus then always paint a bit of “parenchyma” outside the bronchus to prevent leaking).</p>
<p>I would also recommend to check out fully automatic “AI” segmentation tools (LungCTAnalyzer, MONAIAuto3DSeg, TotalSegmentator, DensityLungSegmentation), as you may find that they offer good enough segmentation for your use case.</p>

---

## Post #3 by @jamesgyh (2025-08-11 10:16 UTC)

<p>Thank you for ur answer, that is a nice advice on painting parenchyma around the small bronchus, I struggled with the problem of leaking so much before, as I was following only the Lung, airway, and others for seeds growing. And I will try the AI segmentation tool today.</p>

---

## Post #4 by @jamesgyh (2025-08-11 10:21 UTC)

<p>By the way, May I kindly ask if there is any possible downloading link for the AI tool LungCTSegmentor as I am also watching youtube videos about that but nothing available in the extensions</p>

---

## Post #5 by @eNable_Polska (2025-08-13 18:12 UTC)

<aside class="onebox githubrepo" data-onebox-src="https://github.com/Slicer/SlicerLungCTAnalyzer">
  <header class="source">

      <a href="https://github.com/Slicer/SlicerLungCTAnalyzer" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/4b58263b05cd9edeee2b4d5e3320c0c9/Slicer/SlicerLungCTAnalyzer" class="thumbnail">

  <h3><a href="https://github.com/Slicer/SlicerLungCTAnalyzer" target="_blank" rel="noopener nofollow ugc">GitHub - Slicer/SlicerLungCTAnalyzer: This is a 3D Slicer extension for segmentation and...</a></h3>

    <p><span class="github-repo-description">This is a 3D Slicer extension for segmentation and spatial reconstruction of infiltrated, collapsed, and emphysematous areas in lung CT. </span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #6 by @Arash1 (2025-08-13 21:35 UTC)

<p>Hello</p>
<p>Few questions</p>
<ol>
<li>What is your image spacing? and have you tried resampling?</li>
<li>Have you tried <a href="https://github.com/Slicer/SlicerAirwaySegmentation#airway-segmentation" rel="noopener nofollow ugc">Slicer/SlicerAirwaySegmentation: CLI module for airway segmentation starting from chest CT images</a></li>
<li>What about <a href="https://discourse.slicer.org/t/new-extension-monai-auto3dseg-raise-the-bar-in-ai-medical-image-segmentation/35680">New extension: MONAI Auto3DSeg - raise the bar in AI medical image segmentation - Announcements - 3D Slicer Community</a></li>
</ol>

---

## Post #7 by @jamesgyh (2025-08-14 12:16 UTC)

<p>Hi, my previous image spacing is 1.5mm, which is a bit too thick. I also tried the airway segmentation model, but the result is weird as it doesn’t only contain the airway but also the whole lung.</p>

---

## Post #8 by @Arash1 (2025-08-14 12:29 UTC)

<p>1.5 is Alright but with lung I wouldn’t expect fine details. If you use MONAI, the LUNGS task uses a 1.5 mm resampling but if you resample your image beforehand you will be able to extract more details but might require smoothing.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97b86c527390c97ca5b7ed47e546fcacb890e0f2.jpeg" data-download-href="/uploads/short-url/lEbdOmhuFuVVBpw5UiyO3pb1QEG.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97b86c527390c97ca5b7ed47e546fcacb890e0f2_2_690x343.jpeg" alt="image" data-base62-sha1="lEbdOmhuFuVVBpw5UiyO3pb1QEG" width="690" height="343" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97b86c527390c97ca5b7ed47e546fcacb890e0f2_2_690x343.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97b86c527390c97ca5b7ed47e546fcacb890e0f2_2_1035x514.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97b86c527390c97ca5b7ed47e546fcacb890e0f2.jpeg 2x" data-dominant-color="F5F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1284×640 54.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
