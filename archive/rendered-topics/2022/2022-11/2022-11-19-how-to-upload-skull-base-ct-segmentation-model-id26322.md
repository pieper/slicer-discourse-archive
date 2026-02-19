---
topic_id: 26322
title: "How To Upload Skull Base Ct Segmentation Model"
date: 2022-11-19
url: https://discourse.slicer.org/t/26322
---

# How to upload skull base CT segmentation model

**Topic ID**: 26322
**Date**: 2022-11-19
**URL**: https://discourse.slicer.org/t/how-to-upload-skull-base-ct-segmentation-model/26322

---

## Post #1 by @gang_wu (2022-11-19 17:21 UTC)

<p>Operating system:mac<br>
Slicer version:5.0<br>
Expected behavior:<br>
Actual behavior:<br>
Hi<br>
I am a neurosurgeon and have been using 3D slicer for 10 years. Early works focused on anatomical learning with personal terminals. The “segment edit” is a very helpful tools to simulate the job of performing a surgical anatomy. In my opinion, the establishment of a digital simulation anatomy laboratory is very meaningful for the skull base surgeons. However, the segmentation of skull base bones is a time-consuming and laborious work. I’ve already done some of this groundworks. I would like to share my segmentation models of skull base with others. How to upload the anonymized datas? thank you!</p>

---

## Post #2 by @pieper (2022-11-20 17:18 UTC)

<p>Thank you for your offer.  Expert annotations of real data are essential for creating accurate automated segmentation tools.  I haven’t tried segmentation of the skull base, but in other areas of the body it has been possible to train machine learning models based on a few hundred or maybe as few as a few dozen.  The details on exactly how much data is needed depend on the variability of the anatomy and the imaging.</p>
<p>If you are able to create a folder of consistently named images (CT I’d guess) plus segmentation files and make it available via a file sharing service such as dropbox, google drive, or similar then I hope someone could try training a model, e.g. with <a href="https://github.com/Project-MONAI/MONAILabel">MONAI Label</a> or give you feedback about what else might be needed.  Let us know if you want to discuss further details of how to share the data.</p>

---

## Post #3 by @gang_wu (2022-12-02 01:05 UTC)

<p>Hi Pieper<br>
Thank you for your attention. Yes, I want to upload the skull base bone segmental vtk file based on thin scan CT. However, I lack the necessary experience of files uploading. Is there any<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/7430037791a5a0344ff18fb420ae24f23f30e392.jpeg" data-download-href="/uploads/short-url/gzQfOEOCsyjHCulsFTygamv5qQa.jpeg?dl=1" title="Screenshot_1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/7430037791a5a0344ff18fb420ae24f23f30e392_2_533x500.jpeg" alt="Screenshot_1" data-base62-sha1="gzQfOEOCsyjHCulsFTygamv5qQa" width="533" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/7430037791a5a0344ff18fb420ae24f23f30e392_2_533x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/7430037791a5a0344ff18fb420ae24f23f30e392_2_799x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/7430037791a5a0344ff18fb420ae24f23f30e392_2_1066x1000.jpeg 2x" data-dominant-color="827C92"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_1</span><span class="informations">1452×1360 138 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a2e209b2f011e342bb7cf79eed8823a6bf21bd6a.jpeg" data-download-href="/uploads/short-url/neVDjG1l1hw2nFw1ZQDbHAdeeRY.jpeg?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a2e209b2f011e342bb7cf79eed8823a6bf21bd6a_2_533x500.jpeg" alt="Screenshot" data-base62-sha1="neVDjG1l1hw2nFw1ZQDbHAdeeRY" width="533" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a2e209b2f011e342bb7cf79eed8823a6bf21bd6a_2_533x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a2e209b2f011e342bb7cf79eed8823a6bf21bd6a_2_799x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a2e209b2f011e342bb7cf79eed8823a6bf21bd6a_2_1066x1000.jpeg 2x" data-dominant-color="827D94"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">1452×1360 137 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
designated website for uploading? Thanks!</p>

---

## Post #4 by @pieper (2022-12-03 15:51 UTC)

<p>These look very nice <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"> How many do you have?</p>
<p>There are many storage options.  One option is Zenodo, which is used for a similar dataset:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://zenodo.org/record/6802614#.Y4twN-xufa4">
  <header class="source">
      <img src="https://zenodo.org/static/favicon.ico" class="site-icon" width="" height="">

      <a href="https://zenodo.org/record/6802614#.Y4twN-xufa4" target="_blank" rel="noopener">Zenodo</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://zenodo.org/record/6802614#.Y4twN-xufa4" target="_blank" rel="noopener">Dataset with segmentations of 104 important anatomical structures in 1204 CT...</a></h3>

  <p>In 1204 CT images we segmented 104 anatomical structures (27 organs, 59 bones, 10 muscles, 8 vessels) covering a majority of relevant classes for most use cases. The CT images were randomly sampled from clinical routine, thus representing a real...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @Tannadrake (2023-04-26 14:34 UTC)

<p>This segmentation is beautiful. Did you find a find a place to store these models? I would love to take a closer look and potentially 3D print educational models for the residents in my program if you are willing to share them.</p>

---

## Post #6 by @Basil_Berinyuy (2024-12-12 09:33 UTC)

<p>Hi gang_wu, your segmentation looks very beautiful, did you do it manually? or is it automated? could you please run me through how you arrived such results? I have a similar project and this would be super useful. Thank you in advance.</p>

---
