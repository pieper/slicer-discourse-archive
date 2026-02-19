---
topic_id: 23598
title: "Quick Question About Non Conventional Coordinate System"
date: 2022-05-26
url: https://discourse.slicer.org/t/23598
---

# Quick question about non conventional coordinate system

**Topic ID**: 23598
**Date**: 2022-05-26
**URL**: https://discourse.slicer.org/t/quick-question-about-non-conventional-coordinate-system/23598

---

## Post #1 by @scarpma (2022-05-26 18:04 UTC)

<p>Hello, I have a quick question:</p>
<p>is it possible that a nifti with an affine matrix of this kind</p>
<p>[<br>
[1,0,0,0],<br>
[0,0,1,0],<br>
[0,1,0,0],<br>
[0,0,0,1]<br>
]</p>
<p>is not correctly read by 3dslicer ?</p>
<p>This kind of matrix corresponds to an array which has some kind of “RSA” orientation, and not the standard “RAS” one.</p>

---

## Post #2 by @pieper (2022-05-26 18:13 UTC)

<p>For 3D nifti files slicer relies on ITK’s reader, which is pretty well tested and works on most files I have seen.  But people do use the nifti format in a lot of ways so it’s possible that are “valid” in one program may not load the same in another program.</p>

---

## Post #3 by @lassoan (2022-05-26 23:49 UTC)

<aside class="quote no-group" data-username="scarpma" data-post="1" data-topic="23598">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/scarpma/48/13161_2.png" class="avatar"> scarpma:</div>
<blockquote>
<p>This kind of matrix corresponds to an array which has some kind of “RSA” orientation, and not the standard “RAS” one.</p>
</blockquote>
</aside>
<p>The affine matrix in Nifti defines the transform between voxel coordinate system (IJK) and the RAS anatomical coordinate system. Regardless of the matrix content, the target coordinate system is always RAS (never RSA, etc.). Axis directions of the IJK coordinate system may happen to coincide with some anatomical axis directions, but it does not have any consequence - the image acquisition system is free to choose any coordinate system as IJK coordinate system, it just has to set the voxel values in the image accordingly.</p>
<aside class="quote no-group" data-username="scarpma" data-post="1" data-topic="23598">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/scarpma/48/13161_2.png" class="avatar"> scarpma:</div>
<blockquote>
<p>[[1,0,0,0],<br>
[0,0,1,0],<br>
[0,1,0,0],<br>
[0,0,0,1]]</p>
</blockquote>
</aside>
<p>This matrix has a determinant of &lt;0, which means that the voxel coordinate system is a left-handed coordinate system. This is probably permitted, but unusual. What software generated this image?</p>

---

## Post #4 by @scarpma (2022-05-27 07:39 UTC)

<p>Thank you both for the quick answers.</p>
<p>Actually, I think there’s something strange in the file itself. Opening it with Slicer gives the wrong orientation. The axial and coronal views are exchanged.</p>
<p>Having noticed this, I opened the nifti file in python to inspect the affine matrix and I found this strange matrix. I tried to change manually the affine matrix of the file to a diagonal one and loading it back in slicer, but nothing changed.</p>
<p>So I thought that maybe the original affine matrix was right, but slicer couldn’t read it.</p>
<p>I don’t know what kind of software generated this. I tried to open the original dicom with slicer and the orientation is again wrong. I don’t know what’s happening here…</p>

---

## Post #5 by @lassoan (2022-05-27 14:49 UTC)

<aside class="quote no-group" data-username="scarpma" data-post="4" data-topic="23598">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/scarpma/48/13161_2.png" class="avatar"> scarpma:</div>
<blockquote>
<p>I tried to open the original dicom with slicer and the orientation is again wrong</p>
</blockquote>
</aside>
<p>Then it is quite likely that there is something wrong with that DICOM data set. Where is that DICOM image from? Can you share it (upload somewhere and post the link here)?</p>

---
