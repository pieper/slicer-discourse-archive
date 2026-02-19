---
topic_id: 44295
title: "Resamping For Ct With Different Voxel Can I Still Compare Ct"
date: 2025-09-01
url: https://discourse.slicer.org/t/44295
---

# Resamping for CT with different voxel, can I still compare CTs of two patients with different voxel sizes/number of voxel per axis

**Topic ID**: 44295
**Date**: 2025-09-01
**URL**: https://discourse.slicer.org/t/resamping-for-ct-with-different-voxel-can-i-still-compare-cts-of-two-patients-with-different-voxel-sizes-number-of-voxel-per-axis/44295

---

## Post #1 by @CS1 (2025-09-01 06:20 UTC)

<p>Hi there, as I was trying to train my nnunet model, I was having quite some issues with broadcasting due to images having different sizes/voxels/pixels. As I was looking into this, I realised different CTs of my patients have different spacing, aka voxel size, and different dimensions, aka different numbers of voxels along each axis. This has got me really confused. If a CT has bigger voxel sizes, does it mean it will subsequently have fewer voxels along each axis? e.g. Patient A who has 1x1x1 voxel size will have more voxels per axis, whereas patient B who has 2x2x2 voxel size will have less voxels per axis.</p>
<p>From what I can find, volume calculated by 3D slicer is using the formula “volume = voxel size x number of voxel.”, if voxel size and number of voxel along each axis does not have a linear relationship, does it mean I will have to resample the two CT images to make sure they have consistent voxel sizes etc. before I could compare them?</p>
<p>Sorry for this dumb question, but this has got me really confused..Thank you, I would greatly appreciate any input!</p>

---

## Post #2 by @cpinter (2025-09-01 09:11 UTC)

<aside class="quote no-group" data-username="CS1" data-post="1" data-topic="44295">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/cs1/48/80852_2.png" class="avatar"> CS1:</div>
<blockquote>
<p>If a CT has bigger voxel sizes, does it mean it will subsequently have fewer voxels along each axis? e.g. Patient A who has 1x1x1 voxel size will have more voxels per axis, whereas patient B who has 2x2x2 voxel size will have less voxels per axis.</p>
</blockquote>
</aside>
<p>Yes, in a volume with isotropic 2mm spacing, one voxel would contain 2x2x2=8 voxels of another volume with an isotropic 1mm voxel size.</p>
<p>If you want to compare quantitatively (voxel by voxel), then you need to resample. Slicer has various modules for this, the most comprehensive one being Crop Volume.</p>
<p>If you want to compare visually, then you don’t need to resample. But in any case you will need to register the two volumes so that they overlap meaningfully.</p>

---

## Post #3 by @CS1 (2025-09-03 20:37 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/50dc4aa78ffc89eb5a865cf831e4f127ba281589.png" data-download-href="/uploads/short-url/bxkaysbOgCfaF584UOnJEnNNNDH.png?dl=1" title="屏幕截图 2025-09-04 052919" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/50dc4aa78ffc89eb5a865cf831e4f127ba281589.png" alt="屏幕截图 2025-09-04 052919" data-base62-sha1="bxkaysbOgCfaF584UOnJEnNNNDH" width="588" height="235"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">屏幕截图 2025-09-04 052919</span><span class="informations">588×235 3.51 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/749b52f7f1bcaa84404d53a494c7438d3d5a4cfb.png" data-download-href="/uploads/short-url/gDyalBXebazXUyaNRMUGrEp6nuX.png?dl=1" title="屏幕截图 2025-09-04 061652" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/749b52f7f1bcaa84404d53a494c7438d3d5a4cfb.png" alt="屏幕截图 2025-09-04 061652" data-base62-sha1="gDyalBXebazXUyaNRMUGrEp6nuX" width="585" height="318"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">屏幕截图 2025-09-04 061652</span><span class="informations">585×318 4.29 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I see, thank you so much! For example let’s say for these two images, Am I correct to understand that</p>
<p>Spacing = voxel size， 0.7 = higher resolution, smaller voxel v.s. 0.86 larger voxel</p>
<p>Dimensions = matrix 512 x 512 x depth/thickness 3.0 /- which doesn’t really matter to the actual volume but more like how the scan was “sliced” in 3 dimensions irrelevant to the voxel size ( aka unlike if you have a small voxel you will have more number hence bigger dimensions)</p>
<p>And if I were to compare to two CT scans, for example, of their liver volume I will have to rescale them based off their voxel size so the dimensions reflect the actual number of voxel per volume?</p>

---

## Post #4 by @cpinter (2025-09-04 10:20 UTC)

<aside class="quote no-group" data-username="CS1" data-post="3" data-topic="44295">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/cs1/48/80852_2.png" class="avatar"> CS1:</div>
<blockquote>
<p>Spacing = voxel size， 0.7 = higher resolution, smaller voxel v.s. 0.86 larger voxel</p>
</blockquote>
</aside>
<p>Correct.</p>
<aside class="quote no-group" data-username="CS1" data-post="3" data-topic="44295">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/cs1/48/80852_2.png" class="avatar"> CS1:</div>
<blockquote>
<p>depth/thickness 3.0 /- which doesn’t really matter to the actual volume but more like how the scan was “sliced” in 3 dimensions irrelevant to the voxel size ( aka unlike if you have a small voxel you will have more number hence bigger dimensions)</p>
</blockquote>
</aside>
<p>Slice thickness is the third dimension, not inferior in any way to the in-plane resolution. If you have larger spacing between the slices, your voxels are “taller”. In fact, voxel means “3D pixel”. We don’t have a series of slices, but we have a 3D array of 3D voxels.</p>
<aside class="quote no-group" data-username="CS1" data-post="3" data-topic="44295">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/cs1/48/80852_2.png" class="avatar"> CS1:</div>
<blockquote>
<p>compare to two CT scans, for example, of their liver volume I will have to rescale them based off their voxel size so the dimensions reflect the actual number of voxel per volume?</p>
</blockquote>
</aside>
<p>Not necessary. You can segment the liver in 3D and use the Segment Statistics module to get its volume in mm3. I recommend starting to read the Slicer documentation; every basic concept is explained there, which seem to be new to you. It will be a good place to start, and then you can ask specific questions about things you cannot find there.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://slicer.readthedocs.io/en/latest/">
  <header class="source">

      <a href="https://slicer.readthedocs.io/en/latest/" target="_blank" rel="noopener">slicer.readthedocs.io</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://slicer.readthedocs.io/en/latest/" target="_blank" rel="noopener">Welcome to 3D Slicer’s documentation! — 3D Slicer  documentation</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
