# Can SlicerRadiomics perform Feature selection for 2D imaging?

**Topic ID**: 11903
**Date**: 2020-06-06
**URL**: https://discourse.slicer.org/t/can-slicerradiomics-perform-feature-selection-for-2d-imaging/11903

---

## Post #1 by @LinJP123 (2020-06-06 14:15 UTC)

<p>Operating system:window 10<br>
Slicer version: 4.10.2<br>
Expected behavior:<br>
Actual behavior: Can the SlicerRadiomics perform Feature selection for 2D imaging? And how to set?</p>

---

## Post #2 by @pieper (2020-06-06 20:22 UTC)

<p>Yes. just load a 2D image and Slicer will treat it as a one-slice volume.</p>

---

## Post #3 by @LinJP123 (2020-06-07 04:36 UTC)

<p>Hi Steve!<br>
Thank you for your response. I have other questions. If I load a 2D image, how do I set parameters, such as Resampled voxel size, LoG filter kernel sizes and Wavelet-based features? Or I don’t need to set these parameters.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4ab7f0d7a73ddd4de6ecfe7fa535f2c6fc082778.png" data-download-href="/uploads/short-url/aEZqiokUGlQk8M7nqBhgzP133NS.png?dl=1" title="Snipaste_2020-06-07_12-36-07" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4ab7f0d7a73ddd4de6ecfe7fa535f2c6fc082778.png" alt="Snipaste_2020-06-07_12-36-07" data-base62-sha1="aEZqiokUGlQk8M7nqBhgzP133NS" width="690" height="157" data-dominant-color="F5F5F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Snipaste_2020-06-07_12-36-07</span><span class="informations">827×189 3.02 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Best wishes!<br>
Lin Junpeng</p>

---

## Post #4 by @pieper (2020-06-07 15:06 UTC)

<aside class="quote no-group" data-username="LinJP123" data-post="3" data-topic="11903">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/ce73a5/48.png" class="avatar"> LinJP123:</div>
<blockquote>
<p>If I load a 2D image, how do I set parameters, such as Resampled voxel size, LoG filter kernel sizes and Wavelet-based features?</p>
</blockquote>
</aside>
<p>I’m not sure, but I don’t think it’s any different than in the 3D case - maybe <a class="mention" href="/u/joostjm">@JoostJM</a> can comment.  I think you</p>

---

## Post #5 by @LinJP123 (2020-06-08 03:11 UTC)

<p>Thank you very much!</p>

---

## Post #6 by @JoostJM (2020-06-09 08:11 UTC)

<p>Indeed no difference. The only thing that changes is that for resampledPixelSpacing, you need to fill in only 2 instead of 3 values. Be aware that this assumes truly 2D images. If it fails, carefully read the error message, this often contains clues as to where and how it failed.</p>

---

## Post #7 by @LinJP123 (2020-06-09 09:03 UTC)

<p>OK!  Thank you! I benefited a lot from your reply！</p>

---

## Post #8 by @okanince (2021-06-03 21:13 UTC)

<p>Hello everyone!<br>
I have a similar issue like <a class="mention" href="/u/linjp123">@LinJP123</a> has. I am currently working on 2D ROI from a DICOM volume of CT scan in 3D Slicer. When I try to extract 2D features with voxel resampling as 1,1 and try to add a LoG filter, the system throws error as Wrong dimensionality (2-D) of resampledPixelSpacing, 3-D required.</p>
<p>How can I do pixel resampling and LoG filtering at the same time with 2D images.</p>
<p>Thank you for all your consideration :)<img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #9 by @jamessmith (2021-06-05 18:43 UTC)

<p>Good question and perfect answers to this question. I appreciate that, thanks! <a href="https://scholarsintel.com/" rel="noopener nofollow ugc"><img src="https://emoji.discourse-cdn.com/twitter/handshake.png?v=9" title=":handshake:" class="emoji only-emoji" alt=":handshake:"></a></p>

---
