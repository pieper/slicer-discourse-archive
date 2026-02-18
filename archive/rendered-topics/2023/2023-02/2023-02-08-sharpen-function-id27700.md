# Sharpen Function

**Topic ID**: 27700
**Date**: 2023-02-08
**URL**: https://discourse.slicer.org/t/sharpen-function/27700

---

## Post #1 by @chris_nik (2023-02-08 10:33 UTC)

<p>Hello dear Slicer Community,</p>
<p>I have the following question. On other DICOM imaging software (e.g. Planmeca Romexis or Ez3D) there is a “sharpness” slider or a “sharpen” filter with different degrees of sharpness (from “smooth” to “sharp”, s. Fig.1).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ec8430435b01864475af966009d4093a8719dd42.jpeg" data-download-href="/uploads/short-url/xKjTwQdEtdbst88WmKzdT1WwCoq.jpeg?dl=1" title="smooth" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ec8430435b01864475af966009d4093a8719dd42_2_690x368.jpeg" alt="smooth" data-base62-sha1="xKjTwQdEtdbst88WmKzdT1WwCoq" width="690" height="368" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ec8430435b01864475af966009d4093a8719dd42_2_690x368.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ec8430435b01864475af966009d4093a8719dd42_2_1035x552.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ec8430435b01864475af966009d4093a8719dd42_2_1380x736.jpeg 2x" data-dominant-color="232323"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">smooth</span><span class="informations">2350×1256 112 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b0d2aa1156861225bcd69854d26aaf9f59e321ac.jpeg" data-download-href="/uploads/short-url/pefnCI3XLtNkpkeJeITGQaL1ueE.jpeg?dl=1" title="normal" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b0d2aa1156861225bcd69854d26aaf9f59e321ac_2_690x368.jpeg" alt="normal" data-base62-sha1="pefnCI3XLtNkpkeJeITGQaL1ueE" width="690" height="368" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b0d2aa1156861225bcd69854d26aaf9f59e321ac_2_690x368.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b0d2aa1156861225bcd69854d26aaf9f59e321ac_2_1035x552.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b0d2aa1156861225bcd69854d26aaf9f59e321ac_2_1380x736.jpeg 2x" data-dominant-color="232323"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">normal</span><span class="informations">2350×1256 136 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fa6336da7fdf44e9a4f2b7cbe590a52db1da3a6b.jpeg" data-download-href="/uploads/short-url/zJ1VRfLaRenesLjApYi1SwXbq2L.jpeg?dl=1" title="sharpen" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fa6336da7fdf44e9a4f2b7cbe590a52db1da3a6b_2_690x368.jpeg" alt="sharpen" data-base62-sha1="zJ1VRfLaRenesLjApYi1SwXbq2L" width="690" height="368" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fa6336da7fdf44e9a4f2b7cbe590a52db1da3a6b_2_690x368.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fa6336da7fdf44e9a4f2b7cbe590a52db1da3a6b_2_1035x552.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fa6336da7fdf44e9a4f2b7cbe590a52db1da3a6b_2_1380x736.jpeg 2x" data-dominant-color="232323"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">sharpen</span><span class="informations">2350×1256 179 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Fig.1-3: Slicer DICOM training data opened in Ez3D with “smooth” filter, no filter and “sharpen” filter</p>
<p>I have noticed that increasing the sharpness also increases the noise, which however for my purposes is not a problem.</p>
<p>I found that Slicer has a ‘LaplacianSharpeningImageFilter’ in the ‘Simple Filters’ module.<br>
My question is if its effect should be the same as in the above examples (so far it seems so to me, s. Fig.2) and if there are other Slicer functions that correspond to the above mentioned “sharpen” function.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b2434817d8401d50a172385ec67b792eacdee74.png" data-download-href="/uploads/short-url/aIJnweO6ZhzWh5WmMAaJ03V7vmI.png?dl=1" title="sno" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b2434817d8401d50a172385ec67b792eacdee74_2_690x447.png" alt="sno" data-base62-sha1="aIJnweO6ZhzWh5WmMAaJ03V7vmI" width="690" height="447" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b2434817d8401d50a172385ec67b792eacdee74_2_690x447.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b2434817d8401d50a172385ec67b792eacdee74.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b2434817d8401d50a172385ec67b792eacdee74.png 2x" data-dominant-color="535353"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">sno</span><span class="informations">768×498 145 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3bc28c8b5a47517da8f5bd3ac70108a5122062a1.png" data-download-href="/uploads/short-url/8wEZnPidBWtN2hpJ1SPircBBWhP.png?dl=1" title="swith" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3bc28c8b5a47517da8f5bd3ac70108a5122062a1_2_690x449.png" alt="swith" data-base62-sha1="8wEZnPidBWtN2hpJ1SPircBBWhP" width="690" height="449" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3bc28c8b5a47517da8f5bd3ac70108a5122062a1_2_690x449.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3bc28c8b5a47517da8f5bd3ac70108a5122062a1.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3bc28c8b5a47517da8f5bd3ac70108a5122062a1.png 2x" data-dominant-color="464646"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">swith</span><span class="informations">768×500 139 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Fig.2: Similar slice as in Fig.1 opened in Slicer with no filter and ‘LaplacianSharpeningImageFilter’ applied</p>
<p>Regards</p>

---

## Post #2 by @pieper (2023-02-08 13:13 UTC)

<p>Yes, you are on the right track using SimpleFilters.  There are dozens if not hundreds of filters and variants for denoising / sharpening that you can research in the ITK documentation.  Many of these will improve the visual perception of sharpness, but from a quantitative imaging perspective they are altering the data or even throwing away the original signal data that may bias the results of something like segmentation or radiomics, so use them with caution.</p>

---

## Post #3 by @lassoan (2023-02-08 13:30 UTC)

<p>You can try anisotropic diffusion filters, which can suppress noise while preserving more details.</p>

---

## Post #4 by @chris_nik (2023-02-08 13:46 UTC)

<p>Thank you both very much, important information I will keep in mind.</p>

---
