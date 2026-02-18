# Registering whole body CT with a SPECT/CT

**Topic ID**: 11317
**Date**: 2020-04-27
**URL**: https://discourse.slicer.org/t/registering-whole-body-ct-with-a-spect-ct/11317

---

## Post #1 by @Gunjan_Kayal (2020-04-27 16:04 UTC)

<p>Hi,</p>
<p>When we try to perform the elastic registration (using Elastix), the whole body model is cropped to the size of the real SPECT/CT. We need to preserve the whole body and resample this whole body as per the real SPECT/CT.<br>
Could someone help me with the registration of a whole body CT model with a real SPECT/CT?<br>
I attach a screenshot of the whole body model with SPECT/CT for better understanding.</p>
<p>Thank you.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/905ad546942618e0593e3943dcc04e635a43a820.jpeg" data-download-href="/uploads/short-url/kB1mCdDcEEbj6h2fe4UdUCYqvJe.jpeg?dl=1" title="Screenshot 2020-04-27 at 17.40.31 (2)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/905ad546942618e0593e3943dcc04e635a43a820_2_690x388.jpeg" alt="Screenshot 2020-04-27 at 17.40.31 (2)" data-base62-sha1="kB1mCdDcEEbj6h2fe4UdUCYqvJe" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/905ad546942618e0593e3943dcc04e635a43a820_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/905ad546942618e0593e3943dcc04e635a43a820_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/905ad546942618e0593e3943dcc04e635a43a820_2_1380x776.jpeg 2x" data-dominant-color="939399"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2020-04-27 at 17.40.31 (2)</span><span class="informations">1920×1080 282 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2020-04-27 16:25 UTC)

<p>Elastix cannot extrapolate the segmentation, but Slicer can. Instead of asking Elastix to create a resampled output image, apply the computed transform to the whole body CT using Transforms module.</p>

---
