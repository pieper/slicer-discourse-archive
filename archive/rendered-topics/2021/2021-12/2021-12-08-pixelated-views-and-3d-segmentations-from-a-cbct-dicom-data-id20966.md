---
topic_id: 20966
title: "Pixelated Views And 3D Segmentations From A Cbct Dicom Data"
date: 2021-12-08
url: https://discourse.slicer.org/t/20966
---

# Pixelated views and 3D segmentations from a cbct dicom data

**Topic ID**: 20966
**Date**: 2021-12-08
**URL**: https://discourse.slicer.org/t/pixelated-views-and-3d-segmentations-from-a-cbct-dicom-data/20966

---

## Post #1 by @tarikau (2021-12-08 13:31 UTC)

<p>Hello,<br>
I’m trying to segment maxillary sinus from a dicom data taken from cone beam computed tomography device. I open a patient file, three kinds of images appear on the left screen (unnamed series - imageOrientationPatient 1, 2 and 3). When I click eye symbols right to it (let’s say imageOrientationPatient 3), axial view is clear but other two are pixelated as you can see on image number 1.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5f61974b4d4be70c2a4ecb0c3e9f681d4b120d8f.png" data-download-href="/uploads/short-url/dBMrJVbkBDiJFce3vUJCA497OJ9.png?dl=1" title="number 1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5f61974b4d4be70c2a4ecb0c3e9f681d4b120d8f_2_690x358.png" alt="number 1" data-base62-sha1="dBMrJVbkBDiJFce3vUJCA497OJ9" width="690" height="358" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5f61974b4d4be70c2a4ecb0c3e9f681d4b120d8f_2_690x358.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5f61974b4d4be70c2a4ecb0c3e9f681d4b120d8f.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5f61974b4d4be70c2a4ecb0c3e9f681d4b120d8f.png 2x" data-dominant-color="9A9AAA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">number 1</span><span class="informations">999×519 105 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Then I finish my segmentation using paint tool from SegmentEditor (haven’t tried Threshold tool yet). The results are again pixelated for the other two views and also for the 3D view as you can see on image number 2.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cbc1c097c81e316a21ef3465a96d30b3283375e3.png" data-download-href="/uploads/short-url/t4w2pCBYv1Q6o0dKP5mIH308Y3p.png?dl=1" title="number 2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cbc1c097c81e316a21ef3465a96d30b3283375e3_2_690x320.png" alt="number 2" data-base62-sha1="t4w2pCBYv1Q6o0dKP5mIH308Y3p" width="690" height="320" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cbc1c097c81e316a21ef3465a96d30b3283375e3_2_690x320.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cbc1c097c81e316a21ef3465a96d30b3283375e3_2_1035x480.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cbc1c097c81e316a21ef3465a96d30b3283375e3.png 2x" data-dominant-color="848597"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">number 2</span><span class="informations">1038×482 120 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Also if i change my master volume to see coronal or sagittal view clearly, my painted area become disoriented as you can see on the image number 3.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/41448707f1b02a9c88d1eac281f3949b7a1a2f94.png" data-download-href="/uploads/short-url/9jnR0BqA7FkiLH5P9jT02gBUTDS.png?dl=1" title="number 3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/41448707f1b02a9c88d1eac281f3949b7a1a2f94_2_690x317.png" alt="number 3" data-base62-sha1="9jnR0BqA7FkiLH5P9jT02gBUTDS" width="690" height="317" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/41448707f1b02a9c88d1eac281f3949b7a1a2f94_2_690x317.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/41448707f1b02a9c88d1eac281f3949b7a1a2f94_2_1035x475.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/41448707f1b02a9c88d1eac281f3949b7a1a2f94.png 2x" data-dominant-color="848597"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">number 3</span><span class="informations">1201×553 131 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
How can solve these problems? Thanks in advance.</p>

---

## Post #2 by @lassoan (2021-12-10 13:34 UTC)

<p>This kind of reconstructions are good for humans to review but not well suited for 3D reconstruction. See this post for more details:</p>
<aside class="quote quote-modified" data-post="2" data-topic="2941">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/combining-volumes-what-am-i-missing/2941/2">Combining volumes - what am I missing?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    In general, these multiple low-resolution acquisitions are not well suited for any 3D processing, so the best would be to acquire proper 3D volume, with as isotropic spacing (cubic voxel shape) as possible. 
You may try to find toolkits that can create an isotropic super-resolution image from multiple low-resolution sweeps, but this is a difficult image reconstruction problem, so there are no standard solutions. Have a look at this post <a href="https://discourse.slicer.org/t/import-volume-by-projections/2871/6">Import volume by projections</a> for info on a toolkit that mig…
  </blockquote>
</aside>

<p>CBCT volumes are usually reconstructed as a single isotropic volume (same spacing value along all axes). The software that created the reconstructions should have an option to create a single high-resolution reconstruction.</p>

---

## Post #3 by @tarikau (2021-12-11 14:00 UTC)

<p>Thank you for explanation. What I understand from explanation is that there isn’t enough files to reconstruct a 3D volume. (By the way, I tried my chance on ITK-SNAP as well and the problem still remains.) So, I have two questions:</p>
<ol>
<li>if I had more dicom files, would 3D reconstruction be better?</li>
<li>if not, what are my alternative options (I didn’t really understand the parts you explained alternative ways) ?<br>
Thx</li>
</ol>

---

## Post #4 by @lassoan (2021-12-11 15:18 UTC)

<p>A CBCT imaging device acquires a set of x-ray projection images from different angles. Then an algorithm reconstructs 3D volume at the requested resolution. Usually the imaging technologist chooses the resolution to be isotropic (same along all axes).</p>
<p>I don’t know why the  technologist decided to reconstruct  3 anisotropic volumes in your case. I would recommend to go back to the technologist and ask him to reconstruct a single high-resolution isotropic volume (hopefully the original raw data is still available).</p>

---

## Post #5 by @tarikau (2021-12-11 17:35 UTC)

<p>I’ve just checked the image information and it seems voxels are isotropric. I’m sharing a screenshot.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/869fb8800f3c3a585866bb51abeba2a7bfd68316.png" alt="voxel size" data-base62-sha1="jcWbe28oyavifsLRAjYsXkjOQPc" width="248" height="146"></p>

---

## Post #6 by @tarikau (2021-12-11 21:06 UTC)

<p>I think I finally understood what is the problem. When CBCT viewing program (i-dixel) is giving dicom data, it changes voxel size and makes it anisotropic as you said before. I’ll get in touch with the tech guys, thx!</p>

---
