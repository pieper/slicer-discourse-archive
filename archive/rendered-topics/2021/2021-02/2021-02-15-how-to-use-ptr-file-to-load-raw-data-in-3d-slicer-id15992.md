---
topic_id: 15992
title: "How To Use Ptr File To Load Raw Data In 3D Slicer"
date: 2021-02-15
url: https://discourse.slicer.org/t/15992
---

# How to use PTR file to Load raw data in 3D slicer

**Topic ID**: 15992
**Date**: 2021-02-15
**URL**: https://discourse.slicer.org/t/how-to-use-ptr-file-to-load-raw-data-in-3d-slicer/15992

---

## Post #1 by @xiaolin (2021-02-15 09:03 UTC)

<p>Hello,<br>
Would you please help me to solve this problem?<br>
I want to load my CT raw data to slicer which is PTR file. But I tried many times, it didn’t work. Would you please help me to give me some guidance to figure it out?<br>
Thank you in advance!<br>
Xiaolin<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a563c6ca66fcc71d6d66c5abe1c76983c093f9ab.png" data-download-href="/uploads/short-url/nB6yh8qYV8Zgm5DnnA7a3glFD19.png?dl=1" title="WechatIMG8870" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a563c6ca66fcc71d6d66c5abe1c76983c093f9ab_2_690x361.png" alt="WechatIMG8870" data-base62-sha1="nB6yh8qYV8Zgm5DnnA7a3glFD19" width="690" height="361" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a563c6ca66fcc71d6d66c5abe1c76983c093f9ab_2_690x361.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a563c6ca66fcc71d6d66c5abe1c76983c093f9ab_2_1035x541.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a563c6ca66fcc71d6d66c5abe1c76983c093f9ab_2_1380x722.png 2x" data-dominant-color="74747B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">WechatIMG8870</span><span class="informations">2984×1564 607 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2021-02-15 16:55 UTC)

<p>Does this “PTR file” contain imaging data? Is it reconstructed image (voxels in a Cartesian coordinate system)? What device generated it with what settings?</p>

---

## Post #3 by @xiaolin (2021-02-16 08:21 UTC)

<p>I got the PTR file from the CT room, they told me they are the Raw CT data that were generated from Siemens. I tried to load them into the Hospital CT workstation, but they also didn’t work.</p>

---

## Post #4 by @pieper (2021-02-16 13:23 UTC)

<p>You can search the internet for references to this file type.  It seems it’s a proprietary format to store the raw CT signal (before it’s reconstructed into slices).  Slicer doesn’t support this operation, so if you want to use Slicer ask the CT operators to give you the reconstructed images in dicom format.</p>

---

## Post #5 by @xiaolin (2021-02-16 13:33 UTC)

<p>Ok, much appreciate!<br>
I ask my colleague to get the dicom files.<br>
Have a good day.</p>

---
