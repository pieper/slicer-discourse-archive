# Error: Image Slices Are Not Equally Spaced When Loading DICOM Files in 3D Slicer

**Topic ID**: 40900
**Date**: 2024-12-30
**URL**: https://discourse.slicer.org/t/error-image-slices-are-not-equally-spaced-when-loading-dicom-files-in-3d-slicer/40900

---

## Post #1 by @dslee313 (2024-12-30 08:13 UTC)

<p>Hi,</p>
<p>I am trying to load a DICOM dataset into 3D Slicer, but I am encountering the following error message<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b75a57f6a10a4f82101e27da5da8391a4da6ad06.png" data-download-href="/uploads/short-url/qa0W7hj07DaN93avp7Vjk5kRCVE.png?dl=1" title="스크린샷(9)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b75a57f6a10a4f82101e27da5da8391a4da6ad06_2_690x388.png" alt="스크린샷(9)" data-base62-sha1="qa0W7hj07DaN93avp7Vjk5kRCVE" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b75a57f6a10a4f82101e27da5da8391a4da6ad06_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b75a57f6a10a4f82101e27da5da8391a4da6ad06_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b75a57f6a10a4f82101e27da5da8391a4da6ad06_2_1380x776.png 2x" data-dominant-color="79797F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">스크린샷(9)</span><span class="informations">1920×1080 284 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d7124b3f5257bcdb993fd9be69c90442804c490f.png" data-download-href="/uploads/short-url/uGBQKaJOC3A3kOs8pXYibYYAj3F.png?dl=1" title="스크린샷(11)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d7124b3f5257bcdb993fd9be69c90442804c490f_2_690x388.png" alt="스크린샷(11)" data-base62-sha1="uGBQKaJOC3A3kOs8pXYibYYAj3F" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d7124b3f5257bcdb993fd9be69c90442804c490f_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d7124b3f5257bcdb993fd9be69c90442804c490f_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d7124b3f5257bcdb993fd9be69c90442804c490f_2_1380x776.png 2x" data-dominant-color="E1EAF0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">스크린샷(11)</span><span class="informations">1920×1080 163 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This dataset works perfectly in other software like InVesalius and Mimics without any issues, but in 3D Slicer, some of the slices seem to be missing or not properly aligned after loading.</p>
<p>Here is some additional information about the dataset and my setup:</p>
<ul>
<li>The dataset is CBCT (Cone-Beam CT) data.</li>
<li>I am using 3D Slicer version 5.6.2.</li>
<li>In the DICOM module, the series loads as “Unnamed Series [Scalar Volume],” and the error message appears in the warnings section.</li>
<li>The “Acquisition geometry regularization” is set to the default (“apply regularization transform”).</li>
</ul>
<p>I would like to know:</p>
<ol>
<li>Why is this issue occurring in 3D Slicer, while the same dataset works in other software?</li>
<li>Is there a specific setting or preprocessing step I should follow to fix this?</li>
<li>How can I load this dataset correctly without losing any slices or data?</li>
</ol>
<p>I have attached screenshots of the error message and the loaded volume for reference.</p>
<p>Any help would be greatly appreciated!</p>
<p>Thank you in advance!</p>

---

## Post #2 by @pieper (2024-12-31 16:09 UTC)

<p>Generally this kind of message reflects real issues with your data (not conformant to the standard) or there are dicom objects that don’t correspond to things that Slicer can display (like dose reports or similar).  Since your data was de-identified, its hard to tell from your screenshots.</p>
<p>If you have publicly shareable data that replicates the issues people may be able to give you more specific feedback.</p>
<p>You can refer to the troubleshooting guide for more information:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#troubleshooting">https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#troubleshooting</a></p>

---
