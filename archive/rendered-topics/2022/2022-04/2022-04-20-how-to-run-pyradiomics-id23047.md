---
topic_id: 23047
title: "How To Run Pyradiomics"
date: 2022-04-20
url: https://discourse.slicer.org/t/23047
---

# How to run Pyradiomics

**Topic ID**: 23047
**Date**: 2022-04-20
**URL**: https://discourse.slicer.org/t/how-to-run-pyradiomics/23047

---

## Post #1 by @Van_Tran_Sang_Huynh (2022-04-20 11:28 UTC)

<p>Hi. I am a student, I am practicing using pyrradiomics for feature extraction. I have installed pyradiomics in python 3.6 (64bit), but I don’t know how to run Pyradiomics, please help. Thank you</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8ee2847b98f5dbdc042f3ee513a98be22e5910ad.jpeg" data-download-href="/uploads/short-url/ko16XO2iz1iS9srvggjT6kPf9dH.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8ee2847b98f5dbdc042f3ee513a98be22e5910ad_2_690x388.jpeg" alt="image" data-base62-sha1="ko16XO2iz1iS9srvggjT6kPf9dH" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8ee2847b98f5dbdc042f3ee513a98be22e5910ad_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8ee2847b98f5dbdc042f3ee513a98be22e5910ad_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8ee2847b98f5dbdc042f3ee513a98be22e5910ad_2_1380x776.jpeg 2x" data-dominant-color="171717"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 135 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8ee2847b98f5dbdc042f3ee513a98be22e5910ad.jpeg" data-download-href="/uploads/short-url/ko16XO2iz1iS9srvggjT6kPf9dH.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8ee2847b98f5dbdc042f3ee513a98be22e5910ad_2_690x388.jpeg" alt="image" data-base62-sha1="ko16XO2iz1iS9srvggjT6kPf9dH" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8ee2847b98f5dbdc042f3ee513a98be22e5910ad_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8ee2847b98f5dbdc042f3ee513a98be22e5910ad_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8ee2847b98f5dbdc042f3ee513a98be22e5910ad_2_1380x776.jpeg 2x" data-dominant-color="171717"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 135 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2022-04-20 13:29 UTC)

<p>Review the documentation and if there’s a specific step that’s not working for you describe exactly what you did and what didn’t work as you expect.</p>
<p><a href="https://pyradiomics.readthedocs.io/en/latest/index.html" class="onebox" target="_blank" rel="noopener">https://pyradiomics.readthedocs.io/en/latest/index.html</a></p>

---

## Post #3 by @Van_Tran_Sang_Huynh (2022-04-23 04:37 UTC)

<p>I’m writing code and trying to extract it, but when it comes to choose 2D array, it crashes. And I’m trying to fix this.</p>
<h1><a name="p-77140-choose-2d-array-1" class="anchor" href="#p-77140-choose-2d-array-1" aria-label="Heading link"></a>choose 2D array</h1>
<p><span class="hashtag-raw">#The</span> memory is referenced and changed, so call it again.<br>
imageName, maskName = getTestCase(‘lung2’)<br>
imageStack = sitk.ReadImage(imageName)<br>
maskSatck = sitk.ReadImage(maskName)</p>
<p><span class="hashtag-raw">#Extract</span> pixels as adarray for parametric image calculations, etc.(Example for the 24th slice)<br>
ndimage = sitk.GetArrayFromImage(imageStack)[24]<br>
ndmask = sitk.GetArrayFromImage(maskStack)[24]</p>
<p><span class="hashtag-raw">#Basically</span>, the data that was originally a DICOM image has a dimension of 3, so it is expanded.<br>
ndimage = np.expand_dims(ndimage, axis=0)<br>
ndmask = np.expand_dims(ndmask, axis=0)</p>
<p>print(ndimage.shape)# (1, 512, 512)Even with force2D, the shape must be 3D.<br>
print(ndmask.shape)# (1, 512, 512)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c145e939bb5c0e1ed363262962886fcebcc292fe.png" data-download-href="/uploads/short-url/rzLW04yJT8LuvA5GeCpRGcpioxw.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c145e939bb5c0e1ed363262962886fcebcc292fe_2_690x388.png" alt="image" data-base62-sha1="rzLW04yJT8LuvA5GeCpRGcpioxw" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c145e939bb5c0e1ed363262962886fcebcc292fe_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c145e939bb5c0e1ed363262962886fcebcc292fe_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c145e939bb5c0e1ed363262962886fcebcc292fe_2_1380x776.png 2x" data-dominant-color="F7F7FD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 407 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @Van_Tran_Sang_Huynh (2022-04-23 04:50 UTC)

<p>Can you help me about writing code in feature extraction using pyrradiomics. I tried to use the code but failed. Hope your help.</p>
<p><a href="https://pyradiomics.readthedocs.io/en/latest/features.html" class="onebox" target="_blank" rel="noopener nofollow ugc">https://pyradiomics.readthedocs.io/en/latest/features.html</a></p>
<p>Best regards.</p>

---

## Post #5 by @pieper (2022-04-23 18:39 UTC)

<p>The error message says that you haven’t defined <code>maskStack</code>.</p>

---

## Post #6 by @Van_Tran_Sang_Huynh (2022-04-25 07:00 UTC)

<p>Can you show me how to extract features using pyradiomics in python? Please!!!</p>

---

## Post #7 by @pieper (2022-04-25 12:24 UTC)

<p>I’m afraid we seem to be going in a loop here.  I think the documentation is pretty clear, but maybe there’s a specific step that’s not working for you or there’s some conceptual step that isn’t clear.  Maybe looking at <a href="http://sscce.org/">these suggestions</a> will help you formulate a question someone here can help with.</p>
<p><a href="https://pyradiomics.readthedocs.io/en/latest/usage.html" class="onebox" target="_blank" rel="noopener">https://pyradiomics.readthedocs.io/en/latest/usage.html</a></p>

---

## Post #8 by @Van_Tran_Sang_Huynh (2022-04-28 09:15 UTC)

<p>I am having some problems. Can you give me a solution please?</p>
<p>File “C:/Users/Admin/Desktop/vd2.py”, line 18, in <br>
extractor = featureextractor.RadiomicsFeaturesExtractor(params)<br>
AttributeError: module ‘radiomics.featureextractor’ has no attribute ‘RadiomicsFeaturesExtractor’</p>
<p>and if i drop ‘s’ → RadiomicsFeatureExtractor() can’t try pair ‘kwargs’?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/4043b8669cfe79d407c6335db35e33b80eb22beb.png" data-download-href="/uploads/short-url/9avEbK2NZWzxqr5FA2DwXwb2G3F.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4043b8669cfe79d407c6335db35e33b80eb22beb_2_690x388.png" alt="image" data-base62-sha1="9avEbK2NZWzxqr5FA2DwXwb2G3F" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4043b8669cfe79d407c6335db35e33b80eb22beb_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4043b8669cfe79d407c6335db35e33b80eb22beb_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4043b8669cfe79d407c6335db35e33b80eb22beb_2_1380x776.png 2x" data-dominant-color="F9F6F7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 445 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #9 by @JoostJM (2022-05-03 07:30 UTC)

<p>RadiomicsFeaturesExtractor, inputImages etc. are not valid anymore, they are from an older version of PyRadiomics and are renamed etc.</p>
<p>Als to your “kwargs” problem, pleas read the error carefully: It says you are using an outdated syntax. <code>print</code> without parenthesis is not allowed since Python 3.</p>

---

## Post #10 by @Manju_Manju (2022-05-17 12:28 UTC)

<p>Sir Im trying segmentation on 2d images but im not able to get the output table of radiomic feature generator.can you please guide me</p>

---

## Post #13 by @Van_Tran_Sang_Huynh (2022-05-26 15:51 UTC)

<p>I have imported the DICOM file but the ‘mask’ as above is correct or not. If I’m wrong, how do I need to correct it? hope the helping<br>
Best regards.<br>
Sang.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6ea5eaa25b877c8e740b69ded84558eb77ed9b93.png" data-download-href="/uploads/short-url/fMPZLLo9lfaggdPPQPfqEXdWgfh.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6ea5eaa25b877c8e740b69ded84558eb77ed9b93_2_690x388.png" alt="image" data-base62-sha1="fMPZLLo9lfaggdPPQPfqEXdWgfh" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6ea5eaa25b877c8e740b69ded84558eb77ed9b93_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6ea5eaa25b877c8e740b69ded84558eb77ed9b93_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6ea5eaa25b877c8e740b69ded84558eb77ed9b93_2_1380x776.png 2x" data-dominant-color="FBFAFA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 305 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #14 by @Van_Tran_Sang_Huynh (2022-05-31 11:29 UTC)

<p>I have imported the DICOM file but the ‘mask’ as above is correct or not. If I’m wrong, how do I need to correct it? hope the helping<br>
Best regards.<br>
Sang.</p>

---
