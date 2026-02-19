---
topic_id: 6777
title: "Error In Cropping Dti Volume"
date: 2019-05-13
url: https://discourse.slicer.org/t/6777
---

# Error in Cropping DTI Volume

**Topic ID**: 6777
**Date**: 2019-05-13
**URL**: https://discourse.slicer.org/t/error-in-cropping-dti-volume/6777

---

## Post #1 by @erkara (2019-05-13 21:46 UTC)

<p>Operating system: Linux 5.0.13-1, Opensuse<br>
Slicer version: 4.11<br>
Hi all<br>
I am trying to crop a DTI volume with Crop Volume module, it is  a  *.nhdr file.<br>
Here is the screenshot: <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05186770f4f0ee78bbf5b4714c33f55749db8e32.png" data-download-href="/uploads/short-url/J4FIl7JZ31Wi61k9M1D6uYGY6u.png?dl=1" title="CropDTI" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/05186770f4f0ee78bbf5b4714c33f55749db8e32_2_690x388.png" alt="CropDTI" data-base62-sha1="J4FIl7JZ31Wi61k9M1D6uYGY6u" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/05186770f4f0ee78bbf5b4714c33f55749db8e32_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/05186770f4f0ee78bbf5b4714c33f55749db8e32_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/05186770f4f0ee78bbf5b4714c33f55749db8e32_2_1380x776.png 2x" data-dominant-color="A2A3B0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">CropDTI</span><span class="informations">1920×1080 318 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>but when I hit  “apply”, it does nothing. In fact, a cropped volume appears in “Data” section but slicer says it is invalid.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e3b8521d40a99859f968a1dea0df42adf7ad87b8.png" data-download-href="/uploads/short-url/wuvi3mhq33wwYdLFpMfzfQVSveU.png?dl=1" title="mis" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e3b8521d40a99859f968a1dea0df42adf7ad87b8_2_690x388.png" alt="mis" data-base62-sha1="wuvi3mhq33wwYdLFpMfzfQVSveU" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e3b8521d40a99859f968a1dea0df42adf7ad87b8_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e3b8521d40a99859f968a1dea0df42adf7ad87b8_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e3b8521d40a99859f968a1dea0df42adf7ad87b8_2_1380x776.png 2x" data-dominant-color="A1A3B0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">mis</span><span class="informations">1920×1080 310 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Am I missing some theoretical info like " you cant crop a DTI volume" ? Thanks for the help!</p>

---

## Post #2 by @lassoan (2019-05-13 23:35 UTC)

<p>You can find the error message in the application log (red X icon in the lower-right corner): “CropVolume: Diffusion tensor volumes are not supported by this module”.</p>
<p>It would not be too hard to add DTI support to this module, but for now you need to do a workaround: crop a scalar or DWI volume using “Crop volume” module then use that as “Reference volume” in “Resample DTI volume” module.</p>

---

## Post #3 by @erkara (2019-05-14 00:12 UTC)

<p>Thanks for the prompt response <a class="mention" href="/u/lassoan">@lassoan</a>. However I dont have DWI volume for this data set. As far as I know, mathematically we cant go DTI–&gt;DWI. I used this module for dwi images but I dont know how to proceed in this case. Can you refer to any answer or tutorial by any chance? Thanks for your time again.</p>

---

## Post #4 by @lassoan (2019-05-14 00:24 UTC)

<p>You can generate a reference volume from any volume e.g., download MRHead example, go to Crop volume module, choose MRHead as Input volume, enable interpolated cropping, enable isotropic spacing, optionally change the spacing scale, set the ROI, then click Apply. Then use the generated cropped volume as reference volume in “Resample DTI volume” module.</p>

---

## Post #5 by @erkara (2019-05-16 05:54 UTC)

<p>I think I did it. Thanks for letting me know about that module <a class="mention" href="/u/lassoan">@lassoan</a> Especially tensor correction section has been so helpful in our research.</p>

---
