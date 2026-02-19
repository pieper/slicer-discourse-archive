---
topic_id: 44060
title: "Shaped Based Or Label Gaussian Interpolator For Segmentation"
date: 2025-08-12
url: https://discourse.slicer.org/t/44060
---

# Shaped-based or label gaussian interpolator for segmentation upsampling

**Topic ID**: 44060
**Date**: 2025-08-12
**URL**: https://discourse.slicer.org/t/shaped-based-or-label-gaussian-interpolator-for-segmentation-upsampling/44060

---

## Post #1 by @sulli419 (2025-08-12 22:49 UTC)

<p>For a 3d volume of low resolution images, I have 3 different segmented classes. Because of the low resolution, the edges of the segments look rather jagged. I know that in fact, the ground truth of my image has rather smooth and continuous edges (the edges of brain regions). I would like a way to artificially upsample and smoothen my segmentations, ideally retaining the joint tightness (as in the joint smoothening function). The issue is that interpolating or blurring the discrete segmentation mask values results in intermediate pixel classes, but if I use “nearest neighbor” it retains the jaggedness of the image.  (p.s., it is not possible for me to draw the segmentations again from an upsampled raw volume).</p>
<p>Something like this might be close to what I’m after:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://examples.itk.org/src/core/imagefunction/resamplesegmentedimage/documentation">
  <header class="source">
      <img src="https://examples.itk.org/_static/itk_favicon.ico" class="site-icon" alt="" width="16" height="16">

      <a href="https://examples.itk.org/src/core/imagefunction/resamplesegmentedimage/documentation" target="_blank" rel="noopener nofollow ugc">examples.itk.org</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://examples.itk.org/src/core/imagefunction/resamplesegmentedimage/documentation" target="_blank" rel="noopener nofollow ugc">Resample Segmented Image —  v5.4.0</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Label-Gaussian (multi-label) interpolator (above)<br>
or even<br>
Generic multi-label interpolator module</p>
<p>Does 3d slicer have any built in tools or workflows to implement this?</p>

---

## Post #2 by @pieper (2025-08-12 23:12 UTC)

<p>The smoothing tool in the Segment Editor should do what you need.  Or you can install itk in Slicer and use it directly too.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b4be151a0e7ac58d883bdb653abf6edbc1269658.jpeg" data-download-href="/uploads/short-url/pMVc3iuoc9zVuENXQ3waXkW7RAA.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b4be151a0e7ac58d883bdb653abf6edbc1269658_2_462x500.jpeg" alt="image" data-base62-sha1="pMVc3iuoc9zVuENXQ3waXkW7RAA" width="462" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b4be151a0e7ac58d883bdb653abf6edbc1269658_2_462x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b4be151a0e7ac58d883bdb653abf6edbc1269658.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b4be151a0e7ac58d883bdb653abf6edbc1269658.jpeg 2x" data-dominant-color="E3E4E4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">611×660 143 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @sulli419 (2025-08-13 17:48 UTC)

<p>Thanks for your message.  Apologies, I realized I didn’t emphasize that the “jaggedness” was arising specifically from not having enough pixels in the segments (see image below) because the original volume was also pixelated.  I actually had some luck with clicking on the “segmentation geometry” button in the segmentation editor, and increasing the sampling by a factor of 2.  Next, on the upsampled segments, I ran the joint smoothening tool.</p>
<p>Still curious how to try more of the ITK methods (like gaussian interpolator).  I can’t find ITK extensions for slicer.  Any advice on how to get these?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/eba07c0213b2fe3218dba6c671707e69f52508be.png" data-download-href="/uploads/short-url/xCs2AIKZpm3aZtoCG7J3eIkpjPw.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/eba07c0213b2fe3218dba6c671707e69f52508be.png" alt="image" data-base62-sha1="xCs2AIKZpm3aZtoCG7J3eIkpjPw" width="271" height="233"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">271×233 2.31 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0c0da0384663641bc155133559f29464718a5735.png" data-download-href="/uploads/short-url/1ICVdG0qkiySv0HyGgKvMvvsx01.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0c0da0384663641bc155133559f29464718a5735.png" alt="image" data-base62-sha1="1ICVdG0qkiySv0HyGgKvMvvsx01" width="541" height="302"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">541×302 40.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @pieper (2025-08-13 18:02 UTC)

<p>Yes, upsampling should help in this case.</p>
<p>ITK is used a lot under the hood in Slicer, plus there’s the SimpleFilters module that exposes a lot of features.</p>
<p>You can run <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html">arbitrary scripts with SimpleITK</a> too, and I understand now that the ITK python package can be used directly, although I haven’t had a reason to try that out and see what the difference are.</p>

---
