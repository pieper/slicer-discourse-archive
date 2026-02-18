# Advice on scan acquisition and/or volume processing

**Topic ID**: 29406
**Date**: 2023-05-10
**URL**: https://discourse.slicer.org/t/advice-on-scan-acquisition-and-or-volume-processing/29406

---

## Post #1 by @Jonathan_Millard (2023-05-10 18:56 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/138dba3739df92c5fb4510a6274c1f3dd40396ea.png" data-download-href="/uploads/short-url/2MYIJsxnYiChhgLG3ULwcN6ZTMm.png?dl=1" title="Screenshot 2023-05-10 142116" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/138dba3739df92c5fb4510a6274c1f3dd40396ea_2_690x375.png" alt="Screenshot 2023-05-10 142116" data-base62-sha1="2MYIJsxnYiChhgLG3ULwcN6ZTMm" width="690" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/138dba3739df92c5fb4510a6274c1f3dd40396ea_2_690x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/138dba3739df92c5fb4510a6274c1f3dd40396ea_2_1035x562.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/138dba3739df92c5fb4510a6274c1f3dd40396ea_2_1380x750.png 2x" data-dominant-color="393132"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-05-10 142116</span><span class="informations">1812×986 303 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I am having issues with generating a smooth segment with sufficient enough resolution to serve my purposes. I have a skull scanned in a medical setting. The Volumes module reports the dimensions are 512x512x44 and the spacing is 0.488281mm x 0.488281mm x 5mm. Based on similar support threads, this seems to be related to the fact that this is anisotropic (?). I have found support threads that seem to indicate that this may be an intrinsic property of the scan related to common radiology strategies to reduce radiation/scan time, but (unfortunately for me) results in an anisotropic scan which is not useful for segmentation purposes in 3Dslicer. Here is my question:</p>
<p>Can one somehow fix this problem by using the “Resample Scalar Volume” module and/or the “Crop Volume” module (or some other technique)? Based on feedback on a similar thread, I attempted using the Crop Volume module, selecting “Isotropic spacing” and “B-spline” (this resulted in spacing: 0.48mmx0.48mmx0.48mm &amp; dimensions: 512x512x450), but unfortunately the resulting segment is still isn’t great (see green segment).</p>
<p>I really enjoy using 3DSlicer and I have found there to be many potential research opportunities using patient scans; however, I frequently find this to be a hurdle in obtaining segments which are morphologically accurate enough for research purposes. I suppose for scans that I acquire myself I can simply request an isometric scan(?); however, this may not help with other databases of patient scan data.</p>
<p>Any help or advice would be very greatly appreciated. Also, I would be very interested in learning more from resources which go into further detail on this subject so I can develop better strategies for scan acquisition and/or scan processing prior to segmentation etc. THANK YOU SO MUCH <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f4c9f18e5c6aa32eca260eeee6db07b4ae379e0.png" data-download-href="/uploads/short-url/2blk0RVRJ3mLmRmHAyUgEJfRlN6.png?dl=1" title="Screenshot 2023-05-10 144706" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f4c9f18e5c6aa32eca260eeee6db07b4ae379e0_2_481x500.png" alt="Screenshot 2023-05-10 144706" data-base62-sha1="2blk0RVRJ3mLmRmHAyUgEJfRlN6" width="481" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f4c9f18e5c6aa32eca260eeee6db07b4ae379e0_2_481x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f4c9f18e5c6aa32eca260eeee6db07b4ae379e0_2_721x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f4c9f18e5c6aa32eca260eeee6db07b4ae379e0.png 2x" data-dominant-color="758D85"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-05-10 144706</span><span class="informations">737×766 329 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @muratmaga (2023-05-10 19:13 UTC)

<aside class="quote no-group" data-username="Jonathan_Millard" data-post="1" data-topic="29406">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/b4bc9f/48.png" class="avatar"> Jonathan_Millard:</div>
<blockquote>
<p>Can one somehow fix this problem by using the “Resample Scalar Volume” module and/or the “Crop Volume” module (or some other technique)? Based on feedback on a similar thread, I attempted using the Crop Volume module, selecting “Isotropic spacing” and “B-spline” (this resulted in spacing: 0.48mmx0.48mmx0.48mm &amp; dimensions: 512x512x450), but unfortunately the resulting segment is still isn’t great (see green segment).</p>
</blockquote>
</aside>
<p>Unfortunately you have 10 times less information in the Z plane (0.48mm vs 5mm). Interpolation techniques are not going to give you what is not present in the data. that’s reality of working with clinical data for research projects.</p>
<p>If you can find datasets, 1-2mm slice spacing, then you will have much better looking interpolated data.</p>

---

## Post #3 by @Jonathan_Millard (2023-05-10 19:29 UTC)

<p>Understood! Thank you, Murat!</p>
<p>I wanted to exhaust my options to see if I could get a “good enough” segment from this scan, but it seems very clear that a difference of this magnitude simply can’t be reconciled for my purposes. Thank you very much, this information will greatly inform my strategies moving forward.</p>
<p>With gratitude,<br>
Jon</p>

---
