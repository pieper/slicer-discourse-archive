# Implement the mask adjustment function based on threshold in mimics in slicer

**Topic ID**: 37912
**Date**: 2024-08-16
**URL**: https://discourse.slicer.org/t/implement-the-mask-adjustment-function-based-on-threshold-in-mimics-in-slicer/37912

---

## Post #1 by @dream520nb (2024-08-16 10:51 UTC)

<p>Operating system:Windows 10<br>
Slicer version:4.11<br>
Desired effect: The mask function in mimics is adjusted according to the threshold.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/2423dc95eecae5ab498e97a03d17c220674b4c09.jpeg" data-download-href="/uploads/short-url/59I1njx8ZvB4xE1q7IovtWiDzkZ.jpeg?dl=1" title="20240816-172540" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/2423dc95eecae5ab498e97a03d17c220674b4c09_2_690x373.jpeg" alt="20240816-172540" data-base62-sha1="59I1njx8ZvB4xE1q7IovtWiDzkZ" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/2423dc95eecae5ab498e97a03d17c220674b4c09_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/2423dc95eecae5ab498e97a03d17c220674b4c09_2_1035x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/2423dc95eecae5ab498e97a03d17c220674b4c09_2_1380x746.jpeg 2x" data-dominant-color="F0EDEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">20240816-172540</span><span class="informations">1920×1040 172 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/342ff9eafc4b0a63a4ade54d7786d167fae83709.png" data-download-href="/uploads/short-url/7rFCg5drXurLZvS8itkW3X5ZErn.png?dl=1" title="屏幕截图 2024-08-16 172156" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/342ff9eafc4b0a63a4ade54d7786d167fae83709_2_690x485.png" alt="屏幕截图 2024-08-16 172156" data-base62-sha1="7rFCg5drXurLZvS8itkW3X5ZErn" width="690" height="485" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/342ff9eafc4b0a63a4ade54d7786d167fae83709_2_690x485.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/342ff9eafc4b0a63a4ade54d7786d167fae83709_2_1035x727.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/342ff9eafc4b0a63a4ade54d7786d167fae83709.png 2x" data-dominant-color="5A5E52"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">屏幕截图 2024-08-16 172156</span><span class="informations">1126×793 142 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
In mimics, when stl is converted to mask, the edge pixels are automatically adjusted according to the HU of the mapping position.  Moreover, HU can be manually adjusted to achieve a tight fit on ct when the segmulated stl is turned back to mask.   I didn’t find a similar feature, and I was wondering if slicer could achieve the same effect.</p>

---

## Post #2 by @muratmaga (2024-08-16 17:38 UTC)

<p>It is very hard to compare these two images since one is a 3D model and the other is 2D of mask. But from what you have described, this should be available to you through the Editable intensity ranges of Mask tab in whatever effect you are using.</p>
<p>Also, please use a more recent version of Slicer to try these. 4.11 has been discontinued for 3-4 years now.</p>

---

## Post #3 by @dream520nb (2024-08-19 01:40 UTC)

<p>Please look at the following three pictures, where the yellow is the segmented blood vessels, mimics can automatically adapt to the surrounding threshold after importing the label. Fill the blood vessels in red. I want to implement something similar in slicer. What you call adjusting the mask threshold does not achieve the function of changing the mask size<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9fd3f45582fec5f8df0b0775d3abb793cd698a37.png" data-download-href="/uploads/short-url/mNU1JUyVZT3qt0LWG8duTu021SL.png?dl=1" title="p" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9fd3f45582fec5f8df0b0775d3abb793cd698a37.png" alt="p" data-base62-sha1="mNU1JUyVZT3qt0LWG8duTu021SL" width="690" height="479" data-dominant-color="666658"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">p</span><span class="informations">808×562 97.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e99e76ad6ae1f48d3dfbfa7d5b867e48745d1c59.png" data-download-href="/uploads/short-url/xkGKWYgkGPwhL6wDOCaAzTtFsHn.png?dl=1" title="tAndT" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e99e76ad6ae1f48d3dfbfa7d5b867e48745d1c59_2_595x499.png" alt="tAndT" data-base62-sha1="xkGKWYgkGPwhL6wDOCaAzTtFsHn" width="595" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e99e76ad6ae1f48d3dfbfa7d5b867e48745d1c59_2_595x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e99e76ad6ae1f48d3dfbfa7d5b867e48745d1c59.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e99e76ad6ae1f48d3dfbfa7d5b867e48745d1c59.png 2x" data-dominant-color="696058"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">tAndT</span><span class="informations">841×706 127 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/54d7bc38eb0743607c717f4565c6f2221072a57f.png" data-download-href="/uploads/short-url/c6yjIWUNnSdsl4bUTtB16zLeOaH.png?dl=1" title="true" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/54d7bc38eb0743607c717f4565c6f2221072a57f_2_662x500.png" alt="true" data-base62-sha1="c6yjIWUNnSdsl4bUTtB16zLeOaH" width="662" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/54d7bc38eb0743607c717f4565c6f2221072a57f_2_662x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/54d7bc38eb0743607c717f4565c6f2221072a57f.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/54d7bc38eb0743607c717f4565c6f2221072a57f.png 2x" data-dominant-color="665E59"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">true</span><span class="informations">931×703 137 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @muratmaga (2024-08-19 05:22 UTC)

<p>I am not familiar with Mimics, never used the program. What you are describing sounds like smoothing possibly with some dilation  to me  (not sure adapting the surrounding threshold mean). Both of these are available in Slicer.</p>
<p>If the combination of smoothing and dilation does not cover what you are seeking, my suggestion is to create a short a video capture of what you are doing Mimics for us to understand what’s missing.</p>

---

## Post #5 by @lassoan (2024-08-19 08:00 UTC)

<p>If you want to apply corrections that cannot be represented at the segmentation’s resolution (which is set to the source image’s resolution by default) then you can <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#segmentation-is-not-accurate-enough">resample the segmentation to have finer resolution</a>. Increase the segmentation resolution <em>before</em> the dilation that <a class="mention" href="/u/muratmaga">@muratmaga</a> described above.</p>
<p>We are working on fully automatic lung vessel segmentation with <a class="mention" href="/u/rbumm">@rbumm</a> and <a class="mention" href="/u/diazandr3s">@diazandr3s</a>. Probably we’ll have improved results in a couple of months, so check for updates in <a href="https://github.com/lassoan/SlicerMONAIAuto3DSeg">MONAIAuto3DSeg</a> and <a href="https://github.com/rbumm/SlicerLungCTAnalyzer">LungCTAnalyzer</a> extensions. If the automatic segmentation quality is good then should be no need for post-processing.</p>

---
