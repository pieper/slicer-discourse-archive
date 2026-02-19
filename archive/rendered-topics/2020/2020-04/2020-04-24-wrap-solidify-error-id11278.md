---
topic_id: 11278
title: "Wrap Solidify Error"
date: 2020-04-24
url: https://discourse.slicer.org/t/11278
---

# Wrap Solidify error

**Topic ID**: 11278
**Date**: 2020-04-24
**URL**: https://discourse.slicer.org/t/wrap-solidify-error/11278

---

## Post #1 by @SHRABANI_GHOSH (2020-04-24 00:23 UTC)

<p>Hi,</p>
<p>I am trying to use wrap solidify extension. And I am following these steps</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://lassoan.github.io/SlicerSegmentationRecipes/CTSkullStripping/">
  <header class="source">

      <a href="https://lassoan.github.io/SlicerSegmentationRecipes/CTSkullStripping/" target="_blank" rel="noopener nofollow ugc">3D Slicer segmentation recipes</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://lassoan.github.io/SlicerSegmentationRecipes/CTSkullStripping/" target="_blank" rel="noopener nofollow ugc">Overview</a></h3>

  <p>Recipes for common medical image segmentation tasks using 3D Slicer</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>But when I am using apply button I am getting this error. Why I am getting this error?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3fb463e575ada9cccd74e1a433a0c0149ef14fcc.jpeg" data-download-href="/uploads/short-url/95yz1u1tzjcMWIjkRNA7kXEVOBS.jpeg?dl=1" title="4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3fb463e575ada9cccd74e1a433a0c0149ef14fcc_2_690x325.jpeg" alt="4" data-base62-sha1="95yz1u1tzjcMWIjkRNA7kXEVOBS" width="690" height="325" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3fb463e575ada9cccd74e1a433a0c0149ef14fcc_2_690x325.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3fb463e575ada9cccd74e1a433a0c0149ef14fcc_2_1035x487.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3fb463e575ada9cccd74e1a433a0c0149ef14fcc_2_1380x650.jpeg 2x" data-dominant-color="979799"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">4</span><span class="informations">1442×680 122 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2020-04-24 00:26 UTC)

<p>You need to set some content in the segment that you would like to solidify. In CT images, you can segment the skin surface or all the bones using simple thresholding (using Threshold effect).</p>
<p>See these segmentation recipes for step-by-step instructions:</p>
<ul>
<li><a href="https://lassoan.github.io/SlicerSegmentationRecipes/CTSkullStripping/">https://lassoan.github.io/SlicerSegmentationRecipes/CTSkullStripping/</a></li>
<li><a href="https://lassoan.github.io/SlicerSegmentationRecipes/SkinSurface2/">https://lassoan.github.io/SlicerSegmentationRecipes/SkinSurface2/</a></li>
</ul>

---

## Post #3 by @SHRABANI_GHOSH (2020-04-24 16:10 UTC)

<p>Hi,</p>
<p>I follower the instruction your suggested. When I tried with the outer surface option, the wrap solidify worked. But I sill can see the holes in the bone labels. Screenshopt attached.<br>
Does this functionality helps to fill the holes?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/484c635677fcf93ccd308b7d6a4b32bb1901f1a3.jpeg" data-download-href="/uploads/short-url/ajA2nX4GhFRZRTftajryGh4Fws3.jpeg?dl=1" title="4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/484c635677fcf93ccd308b7d6a4b32bb1901f1a3_2_690x371.jpeg" alt="4" data-base62-sha1="ajA2nX4GhFRZRTftajryGh4Fws3" width="690" height="371" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/484c635677fcf93ccd308b7d6a4b32bb1901f1a3_2_690x371.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/484c635677fcf93ccd308b7d6a4b32bb1901f1a3_2_1035x556.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/484c635677fcf93ccd308b7d6a4b32bb1901f1a3.jpeg 2x" data-dominant-color="888988"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">4</span><span class="informations">1345×725 156 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @SHRABANI_GHOSH (2020-04-24 16:16 UTC)

<p>I am sharing my data file here. Could you please look into it. That will be really helpful.</p>
<p><a href="https://drive.google.com/drive/folders/1s1W06mB6EIyTfMsKf86K3-l6zuTimxFx?usp=sharing" class="onebox" target="_blank" rel="nofollow noopener">https://drive.google.com/drive/folders/1s1W06mB6EIyTfMsKf86K3-l6zuTimxFx?usp=sharing</a></p>

---

## Post #5 by @lassoan (2020-04-24 18:09 UTC)

<p>If you see a “hole” on a slice then it does not mean that it is actually a hole in 3D. It may be just a concavity that may show up in a hole in a certain intersection, but if you look at it on other slices (hold down Shift key while moving the mouse pointer to see the same point in all image slices, you can also enable crosshair display by clicking on the crosshair icon in the toolbar) then you’ll see what it is.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6bbe1bfcc5f32f2c5ef3f2ef68621424f5d26b73.jpeg" data-download-href="/uploads/short-url/fn8oASkXzYhE1vTC7x9RJsHmrEn.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6bbe1bfcc5f32f2c5ef3f2ef68621424f5d26b73_2_690x408.jpeg" alt="image" data-base62-sha1="fn8oASkXzYhE1vTC7x9RJsHmrEn" width="690" height="408" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6bbe1bfcc5f32f2c5ef3f2ef68621424f5d26b73_2_690x408.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6bbe1bfcc5f32f2c5ef3f2ef68621424f5d26b73_2_1035x612.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6bbe1bfcc5f32f2c5ef3f2ef68621424f5d26b73_2_1380x816.jpeg 2x" data-dominant-color="A1A59F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1334 731 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>You may still have holes in the final result at places where the surface becomes very thin. To fix those, you can use Crop volume module to resample the input volume to have finer and isotropic resolution by setting spacing scale to a value &lt;1 (e.g. 0.5).</p>
<p>Note that there are a few issues with your data set:</p>
<p>It seems that your image has been imported from DICOM incorrectly. What software did you use to import it? If it comes from a CBCT then you may need to run the image through DICOM patcher and/or set the correct spacing in Volumes module / Volume information / Image spacing section. Currently, LR and AP spacing seems 2-3x larger than reality (if it is a human skull) and IS spacing is relatively lower (by a factor of 1.5-2x). Fix this before doing anything else with your volume.</p>
<p>The volume seems to be pre-processed by some strange algorithm and made very noisy (lots of quantization noise; CTs are normally 16-bit images, but this one is just 8). After thresholding, you can reduce effect of this noise by removing small speckles by using Smoothing effect with Median method.</p>

---

## Post #6 by @SHRABANI_GHOSH (2020-04-25 03:17 UTC)

<p>Thank you so much for your help. I really appreciate your time.  It was not in dicom format. I downloaded the png sequences from below link(you need to open it in Microsoft edge). Which is isotropic. In this link they also have the label images as well of different (bone , Holes). I have labeled with these two labeled images.<br>
<a href="http://headneckbrainspine.com/web_flash/newmodules/skull%20base%20CT.swf" class="onebox" target="_blank" rel="noopener nofollow ugc">http://headneckbrainspine.com/web_flash/newmodules/skull%20base%20CT.swf</a></p>
<p>I have availed the original ct images downloaded from the website in the shared drive folder.(axct folder)<br>
<a href="https://drive.google.com/drive/folders/1s1W06mB6EIyTfMsKf86K3-l6zuTimxFx?usp=sharing" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/drive/folders/1s1W06mB6EIyTfMsKf86K3-l6zuTimxFx?usp=sharing</a></p>
<p>I did a resampling. Okay, I will do the resampling with spacing values 0.5 on your suggestion. I did not do any other pre-processing accept doing resampling. I did use smoothing effect but I have seen a lot of islands and noises in the surface extraction. (The screenshot)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e7f6b11fe93149b1202576031e053c66e6aa556.png" data-download-href="/uploads/short-url/bcqezqoKK6QTW1rh3qHVhAaOjjw.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4e7f6b11fe93149b1202576031e053c66e6aa556_2_479x499.png" alt="image" data-base62-sha1="bcqezqoKK6QTW1rh3qHVhAaOjjw" width="479" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4e7f6b11fe93149b1202576031e053c66e6aa556_2_479x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4e7f6b11fe93149b1202576031e053c66e6aa556_2_718x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e7f6b11fe93149b1202576031e053c66e6aa556.png 2x" data-dominant-color="595887"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">954×995 113 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I am getting back to you after doing a threshold and smoothing.</p>

---

## Post #7 by @lassoan (2020-04-25 04:00 UTC)

<p>What is the end goal of your project?</p>

---

## Post #8 by @SHRABANI_GHOSH (2020-04-25 04:31 UTC)

<p>To create a deformable surface model of cranium foramina which can be warped onto patient skull ct image to identify the boundary of the cranial foramina. Before this the steps are:</p>
<ol>
<li>Multi-material 2-simplex is going to applied for the surface extraction to create triangular bone and hole mesh.</li>
<li>Decimation is needed to control resolution and to solve problem of producing tractable nonrigid registration–without a coarse-to-fine approach, the fine mesh can become easily entangled in false minima. ( I am going to use ACVD for the decimation by keeping the shared boundary(hole and bone ) intact:: that is why I need a smooth simple bone mesh)</li>
<li>A deformable model registration at first with bone mesh and later hole mesh with patient ct data.</li>
</ol>

---

## Post #9 by @lassoan (2020-04-25 15:38 UTC)

<p>Images that you downloaded from <a href="http://headneckbrainspine.com">http://headneckbrainspine.com</a> are quite bad quality screenshots. You can get proper CTs from various medical image databases. For example, check out head CT images in <a href="https://www.cancerimagingarchive.net/nbia-search/?CollectionCriteria=CPTAC-HNSCC">TCIA’s head and neck cancer (CPTAC-HNSCC) colletion</a>. They were acquired 20 years ago, still better quality than the image you got from that training website. Due to better dose efficiency and improvement of image reconstruction methods, most likely you can get even better quality images (lower noise, maybe even higher resolution) from current CT scanners. I would highly recommend to ask for images from your clinical collaborators that are acquired with today’s technology.</p>
<p>If you need the foramina then you need to enable “carve holes” and set the value lower than the smallest holes you want to preserve. If you are interested in segmenting very delicate structures then you may need to oversample your volume. For example, to reliable segment a 2mm hole, you need 0.4mm but preferable about 0.2mm resolution in your binary labelmap. If your input CT does not have this high resolution then you can oversample it using Crop volume module. To handle such high resolution images, you may either need to reduce your region of interest size or use strong computer, with lots of RAM (about 10x more than your cropped volume size).</p>

---

## Post #10 by @SHRABANI_GHOSH (2020-04-26 16:13 UTC)

<p>Thank you so much for your insights. But if I use other ct images, I don’t have the segmented label images for that those ct images. Only the headneckbrainspine has segmented label images for bone and holes. That is the limitation that I cannot use other ct images.</p>
<p>I have added one folder axatlas (segmented label bone image) and axforamenmagnum(segmented hole label image) for example.<br>
<a href="https://drive.google.com/drive/folders/1oq9F9exKBsq-Mn7JFFY0ojwaLxUGq4ZB?usp=sharing" class="onebox" target="_blank" rel="nofollow noopener">https://drive.google.com/drive/folders/1oq9F9exKBsq-Mn7JFFY0ojwaLxUGq4ZB?usp=sharing</a></p>

---

## Post #11 by @lassoan (2020-04-26 17:16 UTC)

<p>You can segment any CT image using Segment Editor module.</p>

---
