---
topic_id: 25277
title: "Overlay Mri Images Define Volume And Segment Bone"
date: 2022-09-14
url: https://discourse.slicer.org/t/25277
---

# overlay mri images, define volume and segment bone

**Topic ID**: 25277
**Date**: 2022-09-14
**URL**: https://discourse.slicer.org/t/overlay-mri-images-define-volume-and-segment-bone/25277

---

## Post #1 by @johanna (2022-09-14 18:49 UTC)

<p>Hello dear community!<br>
I am rather new to 3d slicer and also in the research with images-game. I feel like my problem is quite basic but I could’nt find an existing answer so please excuse me if its already out there.</p>
<p>I have MRI images of the face of one patient at 6 different times with a healing extraction socket in the lower jaw. I want roughly, to manually overlay the images, define one volume for all of them in the area i’m interested in and then, for each time, segment the bone within the predefined volume.</p>
<p>My problem unfortunately already starts by overlapping the images. In the ‘Transform’ tool I only seem to be able to see one image at a time. When I look at some of the images there, they also seem to be tilted although they are not tilted when I look at them ‘normally’ (when the top left says ‘DICOM’ instead of ‘Transform’) Maybe anyone has an idea why that is?<br>
Thank you very much already!<br>
Johanna</p>
<p>Slicer version: 4.11.20210226</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9d5b443c61f8f89f5d8f822cddc1214bf0b0be3b.jpeg" data-download-href="/uploads/short-url/ms2v23kJGBvLeRLUjdnGvj9uUXh.jpeg?dl=1" title="Bildschirmfoto 2022-09-14 um 18.53.32" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9d5b443c61f8f89f5d8f822cddc1214bf0b0be3b_2_690x463.jpeg" alt="Bildschirmfoto 2022-09-14 um 18.53.32" data-base62-sha1="ms2v23kJGBvLeRLUjdnGvj9uUXh" width="690" height="463" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9d5b443c61f8f89f5d8f822cddc1214bf0b0be3b_2_690x463.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9d5b443c61f8f89f5d8f822cddc1214bf0b0be3b_2_1035x694.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9d5b443c61f8f89f5d8f822cddc1214bf0b0be3b_2_1380x926.jpeg 2x" data-dominant-color="2D2B2B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Bildschirmfoto 2022-09-14 um 18.53.32</span><span class="informations">1920×1289 123 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/652fbe6b557a2ebdacf9aa22779670456a34711c.jpeg" data-download-href="/uploads/short-url/er8vWo1JzGYkmRBNTq6bHvtAfwg.jpeg?dl=1" title="Bildschirmfoto 2022-09-14 um 18.55.18" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/652fbe6b557a2ebdacf9aa22779670456a34711c_2_690x463.jpeg" alt="Bildschirmfoto 2022-09-14 um 18.55.18" data-base62-sha1="er8vWo1JzGYkmRBNTq6bHvtAfwg" width="690" height="463" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/652fbe6b557a2ebdacf9aa22779670456a34711c_2_690x463.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/652fbe6b557a2ebdacf9aa22779670456a34711c_2_1035x694.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/652fbe6b557a2ebdacf9aa22779670456a34711c_2_1380x926.jpeg 2x" data-dominant-color="1F1E1E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Bildschirmfoto 2022-09-14 um 18.55.18</span><span class="informations">1920×1291 97.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2022-09-15 17:35 UTC)

<p>It sounds like you are describing what we call registration.  This page is a good place to start: <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html" class="inline-onebox">Registration — 3D Slicer documentation</a></p>

---

## Post #3 by @johanna (2022-09-15 17:44 UTC)

<p>Thank you very much for your answer - I read this page and I tried following manual registration and registration via BRAINS. Weirdly it works with some of my MRIs and not with some others. The problem already starts when I try to put one image in the background and one in the front. 2 of my 6 images just didn’t appear when moving the switch, the others did.<br>
With the ones that did function first I registered two, saved the volume and than registered the next on the saved volume. Is this the best way to register more than just 2 images?<br>
have a nice day!</p>

---

## Post #4 by @pieper (2022-09-15 17:59 UTC)

<p>Typically you would select one time point, maybe the most recent, and then register each of the other timepoints into the space of the selected time point.  Sometimes these pairwise registrations fail to converge, but for the same subject rigid registration should be robust even if there’s been some change in a local area.  The easiest way in my experience is with the Data module.  Right click on the image you want to move and pick “Register this” and then right click on the target volume and select rigid registration from the registration submenu.  This takes you into the General Registration module with the defaults set so you just click Apply.  This should work well if I’m understanding the data you are working with.  Just do this once for each of the five image pairs.</p>

---

## Post #5 by @johanna (2022-09-15 18:12 UTC)

<p>Thank you! this is definitely way easier compared to what I was trying. Funnily I works with the pairs that have worked before and shows an error i’ll attach with the two pairings that didn’t work before. And what is the best way to combine the five pairs (t0 and tx) afterwards in your opinion? I have to save it as a volume if I want to define a volume within for all of the time point later, right?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f1e7df61620c005ea89387f91b5e53f26ab2afb.jpeg" data-download-href="/uploads/short-url/bhV32ypYtFKoSpzQQkczveOj7o7.jpeg?dl=1" title="Bildschirmfoto 2022-09-15 um 20.05.19" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f1e7df61620c005ea89387f91b5e53f26ab2afb_2_690x446.jpeg" alt="Bildschirmfoto 2022-09-15 um 20.05.19" data-base62-sha1="bhV32ypYtFKoSpzQQkczveOj7o7" width="690" height="446" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f1e7df61620c005ea89387f91b5e53f26ab2afb_2_690x446.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f1e7df61620c005ea89387f91b5e53f26ab2afb_2_1035x669.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f1e7df61620c005ea89387f91b5e53f26ab2afb_2_1380x892.jpeg 2x" data-dominant-color="2F2E2F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Bildschirmfoto 2022-09-15 um 20.05.19</span><span class="informations">1920×1243 139 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @pieper (2022-09-15 18:38 UTC)

<p>Yes, post the errors and we can probably suggest workarounds.</p>
<p>Regarding combining the volumes, it depends on what you want to do in the end.  If you want to measure something like the amount of healing you could make segmentations at each time point, subtract them all from the baseline, and use Segment Statistics to quantify the amount of new growth detectible in each scan.  Or you could put them in a Sequence to see an animation of the change.</p>

---

## Post #7 by @johanna (2022-09-15 19:38 UTC)

<p>The error says:<br>
eneral Registration (BRAINS) standard error:</p>
<p>ExceptionObject caught !</p>
<p>itk::ExceptionObject (0x7fe1e3906d20)</p>
<p>Location: “unknown”</p>
<p>File: /Volumes/D/S/S-1-build/ITK/Modules/Registration/Metricsv4/include/itkMattesMutualInformationImageToImageMetricv4.hxx</p>
<p>Line: 316</p>
<p>Description: itk::ERROR: itk::ERROR: MattesMutualInformationImageToImageMetricv4(0x7fe1e39078f0): All samples map outside moving image buffer. The images do not sufficiently overlap. They need to be initialized to have more overlap before this metric will work. For instance, you can align the image centers by translation.</p>
<p>Exception during registration:</p>
<p>itk::ExceptionObject (0x7fe1e3906d20)</p>
<p>Location: “unknown”</p>
<p>File: /Volumes/D/S/S-1-build/BRAINSTools/BRAINSCommonLib/BRAINSFitHelperTemplate.hxx</p>
<p>Line: 611</p>
<p>Description: itk::ERROR: Exception caught during registration:</p>
<p>itk::ExceptionObject (0x7fe1e3904100)</p>
<p>Location: “unknown”</p>
<p>File: /Volumes/D/S/S-1-build/ITK/Modules/Registration/Metricsv4/include/itkMattesMutualInformationImageToImageMetricv4.hxx</p>
<p>Line: 316</p>
<p>Description: itk::ERROR: itk::ERROR: MattesMutualInformationImageToImageMetricv4(0x7fe1e39078f0): All samples map outside moving image buffer. The images do not sufficiently overlap. They need to be initialized to have more overlap before this metric will work. For instance, you can align the image centers by translation.</p>
<p>regarding combining: I want to measure the bone around the healing socket. I thought about defining a volume as described in my first post because I want to make sure that the mesial-distal expansion is the same at each time and then segment the bone within that area. Does that make sense to you?</p>
<p>Thank you some much for all your quick and helpful answers!</p>

---

## Post #8 by @pieper (2022-09-15 20:30 UTC)

<p>In that case you can try one of the initialization modes.  Probably CenterOfROIAlign would work.  If you still have trouble you can make a transform that aligns them approximately and set that as the initialization transform.  Be sure to look at the FAQ and use case library links from the documentation for more context on what these mean.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b70b9e79bdf93ebe419e135e74af5848387a9c97.png" alt="image" data-base62-sha1="q7igMSPw2cUv0nHnpwUH0sOg23R" width="589" height="160"></p>

---
