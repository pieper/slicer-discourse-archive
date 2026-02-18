# Saving image file in .mha format

**Topic ID**: 11703
**Date**: 2020-05-26
**URL**: https://discourse.slicer.org/t/saving-image-file-in-mha-format/11703

---

## Post #1 by @YolkandWhite (2020-05-26 03:45 UTC)

<p>Hi I have an easy question about .mha file format.</p>
<p>I have an original image file in .png format</p>
<p>I loaded that file to 3D slicer and saved it in .mha format.</p>
<p>and than image size got largen.</p>
<p>The original .png file was (864, 91)</p>
<p>and transformed .mha file was (1, 2848, 300, 4)</p>
<p>how did it became 4 dimensional?</p>
<p>and how did it got bigger??</p>

---

## Post #2 by @lassoan (2020-05-26 03:51 UTC)

<p>Dimensions of the png and mha are completely unrelated, so I don’t see how this mha could be a result of saving the input png. Which Slicer version are you using? Can you share the input .png file?</p>

---

## Post #3 by @YolkandWhite (2020-05-26 04:12 UTC)

<p>Thank you for replying</p>
<p>My 3D slicer version is 4.10.2</p>
<p>Here is my input png file output mha file</p>
<p>and could you tell me why dimension of does two are not related?</p>
<p>2020년 5월 26일 (화) 오후 1:01, Andras Lasso via 3D Slicer Community &lt;<a href="mailto:slicer@discoursemail.com">slicer@discoursemail.com</a>&gt;님이 작성:</p>
<p>(Attachment sinogram1.mha is missing)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8eb808d3d019484eecb312ae91caceb3d027870.png" data-download-href="/uploads/short-url/sFq3pV3Il0xTwh9dr50EnS2Nvyw.png?dl=1" title="sinogram1.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c8eb808d3d019484eecb312ae91caceb3d027870_2_300x500.png" alt="sinogram1.png" data-base62-sha1="sFq3pV3Il0xTwh9dr50EnS2Nvyw" width="300" height="500" data-dominant-color="C6C6C6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">sinogram1.png</span><span class="informations">300×2848 63.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2020-05-26 04:39 UTC)

<p>The png you attached has a size of 300x2848 (not 864x91), it is loaded and saved to mha correctly (tested with recent Slicer-4.11 version).</p>
<p>By the way, loading a sinogram into Slicer will not be useful. You first need to reconstruct it into a 3D volume using <a href="http://www.openrtk.org/">RTK</a> or similar software.</p>

---

## Post #5 by @lassoan (2021-07-01 06:18 UTC)

<p>A post was split to a new topic: <a href="/t/save-ultrasound-images-in-mha-format/18449">Save ultrasound images in mha format</a></p>

---
