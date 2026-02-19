---
topic_id: 13642
title: "Issue With 3D Tee From Ge Vivid E95 In 3D Slicer"
date: 2020-09-23
url: https://discourse.slicer.org/t/13642
---

# Issue With 3D TEE from GE Vivid E95 in 3D Slicer

**Topic ID**: 13642
**Date**: 2020-09-23
**URL**: https://discourse.slicer.org/t/issue-with-3d-tee-from-ge-vivid-e95-in-3d-slicer/13642

---

## Post #1 by @melaughlin (2020-09-23 04:44 UTC)

<p>Hi all,</p>
<p>I am trying to extract a patient’s left ventricle geometry from 3D TEE using the GE Vivid E95. I have been trying to use 3DSlicer with SlicerHeart but am having some issues importing the DICOM files I received from the hospital we are working with. Is there a specific procedure for how the data should be exported from the machine to be able to be used in 3DSlicer and SlicerHeart? I am wondering if they saved it in some weird way and that’s why I am having issues. See attached for what it looks like after I go to “load data” and then choose a file to import (not sure why the colors are so weird and not in black/white!). Also, when I try to do “load DICOM” instead of “load data”, it gives me an error saying it cannot load: unnamed series as a scalar volume.</p>
<p>Thank you in advance!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1f9036c3975fc5d4b9881293d17e01db89819b48.png" data-download-href="/uploads/short-url/4vdMgvco1fFucv07rrrpvCgeRTi.png?dl=1" title="3DTEEDICOMImportExample" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/f/1f9036c3975fc5d4b9881293d17e01db89819b48_2_690x374.png" alt="3DTEEDICOMImportExample" data-base62-sha1="4vdMgvco1fFucv07rrrpvCgeRTi" width="690" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/f/1f9036c3975fc5d4b9881293d17e01db89819b48_2_690x374.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/f/1f9036c3975fc5d4b9881293d17e01db89819b48_2_1035x561.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/f/1f9036c3975fc5d4b9881293d17e01db89819b48_2_1380x748.png 2x" data-dominant-color="6D858D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3DTEEDICOMImportExample</span><span class="informations">1918×1041 180 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2020-09-23 14:06 UTC)

<p>This is just a plain 2D ultrasound screenshot import. If you want to load 3D ultrasound from GE Vivid systems then you need to install SlicerHeart extension and use Image3dAPI as described here: <a href="https://github.com/SlicerHeart/SlicerHeart#loading-various-3d4d-ultrasound-images-using-image3dapi">https://github.com/SlicerHeart/SlicerHeart#loading-various-3d4d-ultrasound-images-using-image3dapi</a></p>

---

## Post #3 by @melaughlin (2020-09-23 16:04 UTC)

<p>So is the issue that I’m just not importing the data correctly or do the files I have not actually contain 3D echo data? We asked the hospital for an example of 3D echo of a pediatric heart and this is what they sent us - see below file.</p>
<aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/images/favicon-vflUeLeeY.ico" class="site-icon" width="16" height="16">
      <a href="https://www.dropbox.com/s/9ytst1cj2rqeejn/02a88e66.dcm?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>
  <article class="onebox-body">
    <img src="https://www.dropbox.com/static/images/spectrum-icons/generated/content/content-unknown-large.png" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://www.dropbox.com/s/9ytst1cj2rqeejn/02a88e66.dcm?dl=0" target="_blank" rel="noopener nofollow ugc">02a88e66.dcm</a></h3>

<p>Shared with Dropbox</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #4 by @lassoan (2020-09-23 19:11 UTC)

<p>This file does not seem to contain 3D information, it is just a screen capture of a replayed 3D acquisition. It shows up nicely in recent Slicer Preview Release, but it is not usable for much, other than just viewing:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1e855eeba9dd7336dcc3cd7d6bce56530a10d23e.jpeg" data-download-href="/uploads/short-url/4m04jVg1xeiDxuFb5TmZGQi5Kp0.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1e855eeba9dd7336dcc3cd7d6bce56530a10d23e_2_690x441.jpeg" alt="image" data-base62-sha1="4m04jVg1xeiDxuFb5TmZGQi5Kp0" width="690" height="441" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1e855eeba9dd7336dcc3cd7d6bce56530a10d23e_2_690x441.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1e855eeba9dd7336dcc3cd7d6bce56530a10d23e_2_1035x661.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1e855eeba9dd7336dcc3cd7d6bce56530a10d23e_2_1380x882.jpeg 2x" data-dominant-color="262526"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2256×1444 500 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>You need to ask the clinicians to export the image differently.</p>

---

## Post #5 by @issakomi (2020-09-24 16:02 UTC)

<p>Above answer is, of course, absolute correct. Just for completeness and to advocate a little <em>Ultrasound Multi-frame Image Storage</em> IOD, there are also 2 <em>calibrated regions</em> (green at the screenshot below) for measurement and <em>cine</em> module to view 2D+t animation correctly. Both are seldom supported by viewers. Good news are that <em>YBR_FULL_422</em> fix is here now (correct colors)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/75e72d1428f783d58b6892bd32a1e0a970960443.jpeg" data-download-href="/uploads/short-url/gP19HHah0QK6iLHJo2Phnqy78Ov.jpeg?dl=1" title="20200924-162436" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/75e72d1428f783d58b6892bd32a1e0a970960443_2_690x475.jpeg" alt="20200924-162436" data-base62-sha1="gP19HHah0QK6iLHJo2Phnqy78Ov" width="690" height="475" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/75e72d1428f783d58b6892bd32a1e0a970960443_2_690x475.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/75e72d1428f783d58b6892bd32a1e0a970960443.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/75e72d1428f783d58b6892bd32a1e0a970960443.jpeg 2x" data-dominant-color="1A1B1C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">20200924-162436</span><span class="informations">1001×690 116 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/edd177cca3a557a16a6f9440d6010bbc10e33b1d.jpeg" data-download-href="/uploads/short-url/xVPWuZ3QEaqJasOVdv8DNRMdwkd.jpeg?dl=1" title="sl2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/edd177cca3a557a16a6f9440d6010bbc10e33b1d_2_690x300.jpeg" alt="sl2" data-base62-sha1="xVPWuZ3QEaqJasOVdv8DNRMdwkd" width="690" height="300" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/edd177cca3a557a16a6f9440d6010bbc10e33b1d_2_690x300.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/edd177cca3a557a16a6f9440d6010bbc10e33b1d.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/edd177cca3a557a16a6f9440d6010bbc10e33b1d.jpeg 2x" data-dominant-color="5A6068"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">sl2</span><span class="informations">866×377 101 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @lassoan (2020-09-24 16:14 UTC)

<aside class="quote no-group" data-username="issakomi" data-post="5" data-topic="13642">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/i/b9e5f3/48.png" class="avatar"> issakomi:</div>
<blockquote>
<p>there are also 2 <em>calibrated regions</em> (green at the screenshot below) for measurement and <em>cine</em> module</p>
</blockquote>
</aside>
<p>It would be easy to load calibrated regions as multivolume (so that it can be played as a cine acquisition) and applying spacing. We haven’t worked on this because nobody has requested this feature.</p>
<p>Probably the reason is that 2D ultrasound image frames usually come without position/orientation information and covered with burnt-in annotations, so even the calibrated regions are not usable for anything else than simple 2D measurements. However, these simple 2D measurements can be easily doable in any software, including software running on the ultrasound cart, so people don’t use Slicer for this.</p>
<p>The situation is similar for XA image sequences - it would be very easy to add support for them in Slicer, but we haven’t heard from anyone who would need it.</p>

---
