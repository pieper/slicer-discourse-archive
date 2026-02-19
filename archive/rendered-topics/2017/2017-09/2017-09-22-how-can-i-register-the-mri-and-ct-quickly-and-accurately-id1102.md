---
topic_id: 1102
title: "How Can I Register The Mri And Ct Quickly And Accurately"
date: 2017-09-22
url: https://discourse.slicer.org/t/1102
---

# How can I register the MRI and CT quickly and accurately?

**Topic ID**: 1102
**Date**: 2017-09-22
**URL**: https://discourse.slicer.org/t/how-can-i-register-the-mri-and-ct-quickly-and-accurately/1102

---

## Post #1 by @hongtao_zhang (2017-09-22 13:05 UTC)

<p>Operating system:windows 10<br>
Slicer version: 4.6.2<br>
Expected behavior: register MRI and CT image accurately<br>
Actual behavior: I can’t use landmark registration to register the image quickly and accurately.<br>
<a href="https://drive.google.com/drive/u/0/folders/0B8dO8C1bNC7AT0tmWFd6M1BRTEE" class="onebox" target="_blank" rel="nofollow noopener">https://drive.google.com/drive/u/0/folders/0B8dO8C1bNC7AT0tmWFd6M1BRTEE</a></p>

---

## Post #2 by @lassoan (2017-09-22 13:30 UTC)

<p>What was the problem? How did you try to register?</p>
<p>If the images don’t overlap in their initial position then it may be difficult to mark the points on them. If that’s the case, I would recommend to align the images manually using Transforms module to make them overlap .</p>
<p>Note that for prostate US/MRI registration Slicer has fully automatic registration modules. <a class="mention" href="/u/cpinter">@cpinter</a> might be able to give more details.</p>

---

## Post #3 by @pieper (2017-09-22 13:37 UTC)

<p>Since this is the same object in two modalities just a doing a rigid registration with BRAINSFit gave a good result.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b8f0893bb6f823e909dc87633fd67646d132ab59.png" data-download-href="/uploads/short-url/qo3crwTiqCKUt87thb1YFxlwJOp.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b8f0893bb6f823e909dc87633fd67646d132ab59_2_629x500.png" alt="image" data-base62-sha1="qo3crwTiqCKUt87thb1YFxlwJOp" width="629" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b8f0893bb6f823e909dc87633fd67646d132ab59_2_629x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b8f0893bb6f823e909dc87633fd67646d132ab59.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b8f0893bb6f823e909dc87633fd67646d132ab59.png 2x" data-dominant-color="F1F1F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">878×697 68.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
