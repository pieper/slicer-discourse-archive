---
topic_id: 20549
title: "Dcm Images Are Blurry And Poorly Defined"
date: 2021-11-09
url: https://discourse.slicer.org/t/20549
---

# DCM Images are blurry and poorly defined

**Topic ID**: 20549
**Date**: 2021-11-09
**URL**: https://discourse.slicer.org/t/dcm-images-are-blurry-and-poorly-defined/20549

---

## Post #1 by @Maria_Lopes (2021-11-09 17:59 UTC)

<p>Hi. I’m doing my master’s thesis and I´m getting desperat…</p>
<p>When I load the magnetic ressonance images in format dcm, only one plan (coronal, sagittal, axial)  is defined. The images from the other plans are blurry and poorly defined.<br>
In the example, coronal plan is ok, but sagittal and axial are indefined and with poor resolution.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4bc2f48dce72bebb90d041d612dfc856edcbd9f4.jpeg" alt="1" data-base62-sha1="aOdv0f98kZtWyOi4vMod81G0FOQ" width="627" height="336"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d8b5cbab11cac0df4fd3a36d3c5b215998e95905.jpeg" alt="2" data-base62-sha1="uV6CZihfADEtxMM2Yspv9HVe0Dj" width="655" height="273"></p>
<p>And when I go to “Volume rendering”, the volume is not filled, as you can see in the following image.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e6008605abc66802b27d01e7a30bf1ec4c17b48a.jpeg" data-download-href="/uploads/short-url/wOGWgMaZwhBQxPX62ZN6vgupTR0.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e6008605abc66802b27d01e7a30bf1ec4c17b48a_2_690x326.jpeg" alt="image" data-base62-sha1="wOGWgMaZwhBQxPX62ZN6vgupTR0" width="690" height="326" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e6008605abc66802b27d01e7a30bf1ec4c17b48a_2_690x326.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e6008605abc66802b27d01e7a30bf1ec4c17b48a_2_1035x489.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e6008605abc66802b27d01e7a30bf1ec4c17b48a_2_1380x652.jpeg 2x" data-dominant-color="8E8EA0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1918×907 106 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>How can I do to solve this?</p>
<p>Thank you so much for the support.</p>

---

## Post #2 by @pieper (2021-11-10 21:09 UTC)

<p>It looks like you have the same problem discussed here:</p>
<aside class="quote quote-modified" data-post="1" data-topic="2941">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/f19dbf/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/combining-volumes-what-am-i-missing/2941">Combining volumes - what am I missing?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Operating system: Mac - High Sierra 
Slicer version: 4.8.1 
Expected behavior: One perfect, high resolution volume 
Actual behavior: Three volumes, each one being high resolution in only one plane (sagittal, coronal, transverse) 
I have been using 3D Slicer for many months and I’m slowly learning the ropes. I am using it to produce anatomical boney models, and have probably created between 10-15 models. 
After loading CT scans from their DICOM folder I always get several volumes, often with the …
  </blockquote>
</aside>


---
