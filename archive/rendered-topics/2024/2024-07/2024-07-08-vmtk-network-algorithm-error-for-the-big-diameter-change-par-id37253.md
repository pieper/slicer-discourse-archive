# Vmtk Network algorithm error for the big diameter change part

**Topic ID**: 37253
**Date**: 2024-07-08
**URL**: https://discourse.slicer.org/t/vmtk-network-algorithm-error-for-the-big-diameter-change-part/37253

---

## Post #1 by @gang_fang (2024-07-08 09:29 UTC)

<p>Dear , all and developers<br>
I use the network extraction for the vessel model with big aneursym , but the network line go outside of the surface , seem not right. Is there solution for this situation?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/3932c0de07b02448f0e79628c782a9d4bf75f768.png" data-download-href="/uploads/short-url/89ZXaTBPAdgMGSEV0xAJudgEVGU.png?dl=1" title="err" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/3932c0de07b02448f0e79628c782a9d4bf75f768_2_628x500.png" alt="err" data-base62-sha1="89ZXaTBPAdgMGSEV0xAJudgEVGU" width="628" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/3932c0de07b02448f0e79628c782a9d4bf75f768_2_628x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/3932c0de07b02448f0e79628c782a9d4bf75f768_2_942x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/3932c0de07b02448f0e79628c782a9d4bf75f768.png 2x" data-dominant-color="6E727F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">err</span><span class="informations">1029×819 258 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2024-07-08 13:54 UTC)

<p>Does centerline extraction work well?<br>
Can you share the model so that we can do some more testing?</p>

---

## Post #3 by @gang_fang (2024-07-09 05:21 UTC)

<p>It is vmtk network extraction output, I use the vmtknetworkextraction script.<br>
Very grateful for your support. Look forward to your feedback.<br>
Here is the STL model link:<br>
<a href="https://drive.google.com/file/d/1RTZhFll643_bbPVBan98wSCbNUL2fVPl/view?usp=drive_link" rel="noopener nofollow ugc">https://drive.google.com/file/d/1RTZhFll643_bbPVBan98wSCbNUL2fVPl/view?usp=drive_link</a></p>

---

## Post #4 by @gang_fang (2024-07-09 05:25 UTC)

<p>yes, If I use "vmtkcenterlines " and select two points near and far, it appear normal like:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/98b6dff20b493f21ee08d9501b262487f8e4b288.jpeg" data-download-href="/uploads/short-url/lMYnJZxu2oeOUAWzqJaKhuxdnsY.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/8/98b6dff20b493f21ee08d9501b262487f8e4b288_2_577x500.jpeg" alt="image" data-base62-sha1="lMYnJZxu2oeOUAWzqJaKhuxdnsY" width="577" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/8/98b6dff20b493f21ee08d9501b262487f8e4b288_2_577x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/8/98b6dff20b493f21ee08d9501b262487f8e4b288_2_865x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/98b6dff20b493f21ee08d9501b262487f8e4b288.jpeg 2x" data-dominant-color="646777"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">884×766 38.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>but the network is</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/147f57994c1797b11e040e371af0d0e829185b48.jpeg" data-download-href="/uploads/short-url/2Vknu1hZQN4WB0eVpqxPrzXMznq.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/147f57994c1797b11e040e371af0d0e829185b48_2_487x500.jpeg" alt="image" data-base62-sha1="2Vknu1hZQN4WB0eVpqxPrzXMznq" width="487" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/147f57994c1797b11e040e371af0d0e829185b48_2_487x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/147f57994c1797b11e040e371af0d0e829185b48_2_730x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/147f57994c1797b11e040e371af0d0e829185b48.jpeg 2x" data-dominant-color="646878"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">804×825 44.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
