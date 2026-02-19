---
topic_id: 22259
title: "Unexpected 3D Volume Generated"
date: 2022-03-02
url: https://discourse.slicer.org/t/22259
---

# unexpected 3d volume generated

**Topic ID**: 22259
**Date**: 2022-03-02
**URL**: https://discourse.slicer.org/t/unexpected-3d-volume-generated/22259

---

## Post #1 by @mann (2022-03-02 12:32 UTC)

<p>Hi all,<br>
I tried to develop cerebral arteries using DSA dicom having multiple slices of axial view. I patched the files using dicom patcher module. And then imported as Dicom data. But the sagittal and coronal views developed looks somewhat skewed. Then I tried to apply threshold to the region of interest and the resulted 3d model is having square and rectangular cross section instead of circular or oval.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b5f8d5623225b2ea89c048a23f95363cb6203579.jpeg" data-download-href="/uploads/short-url/pXNxP10gVM3nlgQK90JF7BHFrVT.jpeg?dl=1" title="Screenshot 2022-03-02 161633" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b5f8d5623225b2ea89c048a23f95363cb6203579_2_690x376.jpeg" alt="Screenshot 2022-03-02 161633" data-base62-sha1="pXNxP10gVM3nlgQK90JF7BHFrVT" width="690" height="376" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b5f8d5623225b2ea89c048a23f95363cb6203579_2_690x376.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b5f8d5623225b2ea89c048a23f95363cb6203579_2_1035x564.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b5f8d5623225b2ea89c048a23f95363cb6203579_2_1380x752.jpeg 2x" data-dominant-color="5A5A6D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2022-03-02 161633</span><span class="informations">1920×1047 197 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d7af3c9897b3018b5aa7b6d29718d343aa03e75.jpeg" data-download-href="/uploads/short-url/dkXPo0BqQ3RCzuYyfBB29AOR0Gh.jpeg?dl=1" title="LBH" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5d7af3c9897b3018b5aa7b6d29718d343aa03e75_2_690x414.jpeg" alt="LBH" data-base62-sha1="dkXPo0BqQ3RCzuYyfBB29AOR0Gh" width="690" height="414" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5d7af3c9897b3018b5aa7b6d29718d343aa03e75_2_690x414.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5d7af3c9897b3018b5aa7b6d29718d343aa03e75_2_1035x621.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d7af3c9897b3018b5aa7b6d29718d343aa03e75.jpeg 2x" data-dominant-color="8891B3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">LBH</span><span class="informations">1123×674 86.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/49e6156d915e924d6b2f26574b8d6e5ac8782ed1.jpeg" data-download-href="/uploads/short-url/axJO3ENIFjJc3FJfmLJEMcee7nP.jpeg?dl=1" title="VJK11" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/49e6156d915e924d6b2f26574b8d6e5ac8782ed1_2_690x489.jpeg" alt="VJK11" data-base62-sha1="axJO3ENIFjJc3FJfmLJEMcee7nP" width="690" height="489" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/49e6156d915e924d6b2f26574b8d6e5ac8782ed1_2_690x489.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/49e6156d915e924d6b2f26574b8d6e5ac8782ed1_2_1035x733.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/49e6156d915e924d6b2f26574b8d6e5ac8782ed1.jpeg 2x" data-dominant-color="8D94B9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">VJK11</span><span class="informations">1089×773 73.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Operating system: Windows 10<br>
Slicer version:4.11.20210226<br>
Expected behavior: Cerebral arteries with oval or circular cross section<br>
Actual behavior: Cerebral arteries in the developed 3d models shows rectangular or square shapes</p>

---

## Post #2 by @pieper (2022-03-02 13:54 UTC)

<p>It looks like you have variable slice spacing and need to enable acquisition geometry regularization option.  These links should help.</p>
<aside class="quote quote-modified" data-post="1" data-topic="19001">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/understanding-ct-image-spacing-and-acquisition-geometry-regularization/19001">Understanding CT Image spacing and Acquisition geometry regularization</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category --style-square " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
    </div>
  </div>
  <blockquote>
    Dear all, 
"Images are not equally spaced (a difference of 0.6 vs 0.3 was detected)’ 
Why does this error occur? What causes the acquisition of acquired irregular geometry? is it something to do with CT machine, protocol, technique or just a problem with exporting the data? 
with Acquisition geometry regularization correction transform applied,  I tried to harden the transformation and I expected the corrected version of the image to persist but it changed to the original? is this the expected b…
  </blockquote>
</aside>

<aside class="onebox allowlistedgeneric" data-onebox-src="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#basic-usage">
  <header class="source">

      <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#basic-usage" target="_blank" rel="noopener">slicer.readthedocs.io</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#basic-usage" target="_blank" rel="noopener">DICOM — 3D Slicer  documentation</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @mann (2022-03-04 09:07 UTC)

<p>Hi,<br>
I enabled the acquisition geometry regularization option in Edit&gt;Application Settings&gt; Dicom.<br>
After that I restarted Slicer App. But the results were the same.<br>
Also I couldn’t find the Dicom plugin option in slicer version 4.11.20210226<br>
I am new to Slicer 3d.</p>
<p>Thanks<br>
Manjunath<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d94d5a701ada4fc475bfa8c106bbfe75d6aec5aa.jpeg" data-download-href="/uploads/short-url/v0ll3QzoDQmOOuFA69HSoB6ksFI.jpeg?dl=1" title="Screenshot 2022-03-04 143636" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d94d5a701ada4fc475bfa8c106bbfe75d6aec5aa_2_690x388.jpeg" alt="Screenshot 2022-03-04 143636" data-base62-sha1="v0ll3QzoDQmOOuFA69HSoB6ksFI" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d94d5a701ada4fc475bfa8c106bbfe75d6aec5aa_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d94d5a701ada4fc475bfa8c106bbfe75d6aec5aa_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d94d5a701ada4fc475bfa8c106bbfe75d6aec5aa_2_1380x776.jpeg 2x" data-dominant-color="3F3E45"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2022-03-04 143636</span><span class="informations">1920×1080 220 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @mann (2022-03-04 10:13 UTC)

<p>Hi,<br>
I tried resampling data. And made the the image dimensions 1024, 1024,1028 by changing the image spacing from 1mm,1mm, 1mm to 1mm, 1mm, 0.5mm.</p>
<p>But the problem still persists, when I develop the 3d volume the cross section of vessels are still rectangular<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/20e392989729fb214d07a970d7c35f88897c9da3.jpeg" alt="Screenshot 2022-03-04 154103" data-base62-sha1="4GWQLY6A1Wh1KwpoO5QzAHJqzwT" width="577" height="429"></p>

---

## Post #5 by @pieper (2022-03-04 14:31 UTC)

<p>It sounds like these files have been modified in some way because it’s rare that data that comes directly from any medical scanner would have this kind of issues.  I suggest tracing back to wherever you got them to see if you can get originals.</p>

---
