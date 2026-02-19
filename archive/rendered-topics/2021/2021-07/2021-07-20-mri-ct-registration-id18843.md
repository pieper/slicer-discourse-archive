---
topic_id: 18843
title: "Mri Ct Registration"
date: 2021-07-20
url: https://discourse.slicer.org/t/18843
---

# MRI CT Registration

**Topic ID**: 18843
**Date**: 2021-07-20
**URL**: https://discourse.slicer.org/t/mri-ct-registration/18843

---

## Post #1 by @HodaGH (2021-07-20 22:24 UTC)

<p>Hello,</p>
<p>I have tried a few techniques to register pelvic bones rigidly from MRI to CT image of one patient. For all I put the CT as the fixed image.<br>
First tried Mutual Information registration with cropping the dark areas with this ROI for both CT and MRI (elastix setting: 1000 iteration and 3000 samples)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/65c995acbb89782dcf8e046a86f6201acd893df5.png" data-download-href="/uploads/short-url/ews7ikCXNfupw6C0yFEUUJrctZb.png?dl=1" title="MRI-ROI1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/65c995acbb89782dcf8e046a86f6201acd893df5_2_690x219.png" alt="MRI-ROI1" data-base62-sha1="ews7ikCXNfupw6C0yFEUUJrctZb" width="690" height="219" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/65c995acbb89782dcf8e046a86f6201acd893df5_2_690x219.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/65c995acbb89782dcf8e046a86f6201acd893df5_2_1035x328.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/65c995acbb89782dcf8e046a86f6201acd893df5.png 2x" data-dominant-color="393939"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">MRI-ROI1</span><span class="informations">1096×348 198 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7d84caa2daa2b6b299a4c0798b4e758bd4788e55.png" data-download-href="/uploads/short-url/hUobG9hH3ENhDv31QFwkG75g3wp.png?dl=1" title="ct-ROI1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d84caa2daa2b6b299a4c0798b4e758bd4788e55_2_690x199.png" alt="ct-ROI1" data-base62-sha1="hUobG9hH3ENhDv31QFwkG75g3wp" width="690" height="199" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d84caa2daa2b6b299a4c0798b4e758bd4788e55_2_690x199.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d84caa2daa2b6b299a4c0798b4e758bd4788e55_2_1035x298.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7d84caa2daa2b6b299a4c0798b4e758bd4788e55.png 2x" data-dominant-color="535353"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ct-ROI1</span><span class="informations">1087×314 208 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Second MI (last settings) on original images after a fiducial registration and third with multi metric registration with three MI on original images. For three techniques the result was the same and is shown with the segmented bone from CT over MRI which is not completely correct<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89f4309713a888a10c9652c779cfaf1857323b0d.png" alt="p5-fiducialMI" data-base62-sha1="jGoAr6vEuU477Mq2nVAROe453zL" width="600" height="358"></p>
<p>I also used a mask for the above ROI but the result is not much different:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/8555adf7f4337a7ad6aec7b78c61fb84c20bb1f3.png" data-download-href="/uploads/short-url/j1x4pEHq9kMvqKBjDYKHG4gurgn.png?dl=1" title="ROImask" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8555adf7f4337a7ad6aec7b78c61fb84c20bb1f3_2_690x345.png" alt="ROImask" data-base62-sha1="j1x4pEHq9kMvqKBjDYKHG4gurgn" width="690" height="345" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8555adf7f4337a7ad6aec7b78c61fb84c20bb1f3_2_690x345.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/8555adf7f4337a7ad6aec7b78c61fb84c20bb1f3.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/8555adf7f4337a7ad6aec7b78c61fb84c20bb1f3.png 2x" data-dominant-color="333331"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ROImask</span><span class="informations">825×413 133 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>on another try did the MI registration with cropped images after the cropped MRI was hardened with a fiducial registration transform and also used masking<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b58e6cc56c26cb598e60bc5d9f23bcba756ae45.png" data-download-href="/uploads/short-url/1CnIOKkaYN4te9BR02rZ4zn2OsR.png?dl=1" title="fiducialcropedmaskedMI" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b58e6cc56c26cb598e60bc5d9f23bcba756ae45_2_690x335.png" alt="fiducialcropedmaskedMI" data-base62-sha1="1CnIOKkaYN4te9BR02rZ4zn2OsR" width="690" height="335" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b58e6cc56c26cb598e60bc5d9f23bcba756ae45_2_690x335.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b58e6cc56c26cb598e60bc5d9f23bcba756ae45.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b58e6cc56c26cb598e60bc5d9f23bcba756ae45.png 2x" data-dominant-color="1D1D1B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">fiducialcropedmaskedMI</span><span class="informations">822×400 158 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Forth tried Normalized MI (5 resolution levels, recursive pyramid, 10000 samples, (NumberOfHistogramBins 16 32 64) and (MaximumNumberOfIterations 4096 2048 1024 512 256) for which the result is this, right side is off:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e9fcd491895da0e00ec1e68702e89fa7079b3ddc.png" data-download-href="/uploads/short-url/xnWW6kOzSJ5Hhx2mjxBtrnhBei0.png?dl=1" title="Screen Shot 2021-07-20 at 4.17.20 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e9fcd491895da0e00ec1e68702e89fa7079b3ddc_2_690x338.png" alt="Screen Shot 2021-07-20 at 4.17.20 PM" data-base62-sha1="xnWW6kOzSJ5Hhx2mjxBtrnhBei0" width="690" height="338" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e9fcd491895da0e00ec1e68702e89fa7079b3ddc_2_690x338.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e9fcd491895da0e00ec1e68702e89fa7079b3ddc.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e9fcd491895da0e00ec1e68702e89fa7079b3ddc.png 2x" data-dominant-color="333332"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-07-20 at 4.17.20 PM</span><span class="informations">959×471 169 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Fifth was piecewise registration on only left femur as white crop ROI shows, default setting but 2000 iteration and 5000 samples in elastix, still a bit off as shows on the axial and sagittal views :<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7e261d25e24ed02eb5a9d436ad0f40634c1eb1b5.png" data-download-href="/uploads/short-url/hZXOPtFQNUbdxfSfSyHjEbTmBtX.png?dl=1" title="Screen Shot 2021-07-20 at 3.48.31 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7e261d25e24ed02eb5a9d436ad0f40634c1eb1b5_2_690x302.png" alt="Screen Shot 2021-07-20 at 3.48.31 PM" data-base62-sha1="hZXOPtFQNUbdxfSfSyHjEbTmBtX" width="690" height="302" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7e261d25e24ed02eb5a9d436ad0f40634c1eb1b5_2_690x302.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7e261d25e24ed02eb5a9d436ad0f40634c1eb1b5_2_1035x453.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7e261d25e24ed02eb5a9d436ad0f40634c1eb1b5.png 2x" data-dominant-color="343534"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-07-20 at 3.48.31 PM</span><span class="informations">1180×518 221 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Fiducial-Model registration for which the result is very similar to fiducial registration only:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/375586bad1a95bab1f449aff171a297accd8e07a.png" data-download-href="/uploads/short-url/7Tvv0oi90bJlT2NYA2c8yu8fM82.png?dl=1" title="Screen Shot 2021-07-20 at 4.11.19 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/375586bad1a95bab1f449aff171a297accd8e07a_2_690x348.png" alt="Screen Shot 2021-07-20 at 4.11.19 PM" data-base62-sha1="7Tvv0oi90bJlT2NYA2c8yu8fM82" width="690" height="348" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/375586bad1a95bab1f449aff171a297accd8e07a_2_690x348.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/375586bad1a95bab1f449aff171a297accd8e07a.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/375586bad1a95bab1f449aff171a297accd8e07a.png 2x" data-dominant-color="272727"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-07-20 at 4.11.19 PM</span><span class="informations">940×475 135 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Now I have a few questions:<br>
1- why does Mutual Information registration messes up the fiducial registration result, doesn’t fiducial initialization supposed to increase the accuracy?<br>
2- Can the result of piecewise registration be used for further analysis? I mean is this result considered a good registration?<br>
3- I followed the tutorial for surface registration from SlicerIGT to do the fiducial-model registration, there they wanted to register the stylus on the segment but here I want to register the MRI on the CT segmented bone. Because the 30-40 points that I specify on the segment and register with fiducial-model registration module are completely separate from the fiducials used for the fiducial registration wizard makes me wonder if it make sense to use this technique?<br>
4- Overall am I missing something ? is there anything that I can improve?<br>
Thank you very much in advance.</p>

---

## Post #2 by @lassoan (2021-07-20 22:34 UTC)

<p>Are these images of a live human patient? lf they are, then you cannot register the images rigidly, because the legs will not be in the same pose in the CT and MRI.</p>
<p>Is there a big time difference (months or years) or interventions performed between the imaging sessions?</p>
<p>What is the goal of the registration? What accuracy do you need and where do you need high accuracy?</p>

---

## Post #3 by @HodaGH (2021-07-20 22:50 UTC)

<p>Thank you Dr. Lassoan,</p>
<p>Yes they’re humans, so you’re saying even if I register the pelvis and the femur separately like the piecewise registration above rigid registration won’t work?</p>
<p>The time difference is a lot around 6-8 years. How can this impact the result?</p>
<p>We would like to assess the relation of bone density from the CT, cartilage from the MRI and bone remodeling from PET which is already aligned with MRI (taken with the same equipment) in the subchondral bone of femur head and acetabulum  in Femoroacetabular Impingement patients.<br>
I wasn’t told a specific accuracy but my RMSE’s are around 4 to 9 mm in different patients, is this acceptable ?</p>
<p>Thank you.</p>

---

## Post #4 by @lassoan (2021-07-21 02:02 UTC)

<aside class="quote no-group" data-username="HodaGH" data-post="3" data-topic="18843">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/858c86/48.png" class="avatar"> HodaGH:</div>
<blockquote>
<p>The time difference is a lot around 6-8 years. How can this impact the result?</p>
</blockquote>
</aside>
<p>This means that the shape of the bones might change. Therefore, you may consider adding a deformable registration step after the rigid registration.</p>
<aside class="quote no-group" data-username="HodaGH" data-post="1" data-topic="18843">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/858c86/48.png" class="avatar"> HodaGH:</div>
<blockquote>
<p>why does Mutual Information registration messes up the fiducial registration result, doesn’t fiducial initialization supposed to increase the accuracy?</p>
</blockquote>
</aside>
<p>Since the legs move between the image acquisitions, there is no single rigid (or even deformable registration) that can align the pelvis and both legs. When you did the manual registration then you ensured that the registration is accurate at the prescribed positions, but the automatic image-based registration tried to align everything at once, which was impossible.</p>
<aside class="quote no-group" data-username="HodaGH" data-post="1" data-topic="18843">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/858c86/48.png" class="avatar"> HodaGH:</div>
<blockquote>
<p>Can the result of piecewise registration be used for further analysis? I mean is this result considered a good registration?</p>
</blockquote>
</aside>
<p>Yes. Registration of a single bone can be very accurate (depends on the image resolution and on the MRI imaging protocol), and everything that is rigidly attached to it will be registered accurately, too.</p>
<aside class="quote no-group" data-username="HodaGH" data-post="1" data-topic="18843">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/858c86/48.png" class="avatar"> HodaGH:</div>
<blockquote>
<p>I followed the tutorial for surface registration from SlicerIGT to do the fiducial-model registration, there they wanted to register the stylus on the segment but here I want to register the MRI on the CT segmented bone. Because the 30-40 points that I specify on the segment and register with fiducial-model registration module are completely separate from the fiducials used for the fiducial registration wizard makes me wonder if it make sense to use this technique?</p>
</blockquote>
</aside>
<p>If you segment the exact same structure on CT and MRI then you can use SegmentRegistration extension to align them. However, it may be hard to segment the same on these two imaging modalities, because you usually see very different things (depending on the MRI imaging protocol).</p>
<aside class="quote no-group" data-username="HodaGH" data-post="1" data-topic="18843">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/858c86/48.png" class="avatar"> HodaGH:</div>
<blockquote>
<p>Overall am I missing something ? is there anything that I can improve?<br>
Thank you very much in advance.</p>
</blockquote>
</aside>
<p>I would recommend to crop the image to one bone at a time. If there are bones nearby you can specify a mask to make sure they are ignored.</p>
<p>Try SlicerElastix or SlicerANTs extensions, because BRAINS registration typically requires extensive parameter tuning.</p>
<aside class="quote no-group" data-username="HodaGH" data-post="3" data-topic="18843">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/858c86/48.png" class="avatar"> HodaGH:</div>
<blockquote>
<p>I wasn’t told a specific accuracy but my RMSE’s are around 4 to 9 mm in different patients, is this acceptable ?</p>
</blockquote>
</aside>
<p>If you register bones then you can expect that your accuracy will be approximately the same as the resolution of your image. So, most likely you should be able to get a smaller error than 4-9mm (about 1mm should be feasible if the diameter of image voxels in both MRI and CT are less than a millimeter).</p>

---
