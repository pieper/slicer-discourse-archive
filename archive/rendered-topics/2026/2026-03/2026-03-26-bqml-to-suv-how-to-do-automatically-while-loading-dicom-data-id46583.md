---
topic_id: 46583
title: "BQML to SUV (how to do automatically while loading DICOM data)"
date: 2026-03-26
url: https://discourse.slicer.org/t/46583
last_bumped: 2026-04-02T14:40:48.278Z
---

# BQML to SUV (how to do automatically while loading DICOM data)

**Topic ID**: 46583
**Date**: 2026-03-26
**URL**: https://discourse.slicer.org/t/bqml-to-suv-how-to-do-automatically-while-loading-dicom-data/46583

---

## Post #1 by @Divi (2026-03-26 19:00 UTC)

<p>I’m trying to do segmentation and quantification, but my values are too high (maybe its BQML) and I need it to be SUV values. Could you help me on how to do this?</p>

---

## Post #2 by @fedorov (2026-03-26 19:58 UTC)

<p>You can try applying SUV normalization using PET-DICOM Extension!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8b5437bff29792217fdb7dea590220f201496b67.jpeg" data-download-href="/uploads/short-url/jSyNR6Dh9bLjtuEvcFfT7Tlv3zF.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8b5437bff29792217fdb7dea590220f201496b67_2_690x256.jpeg" alt="image" data-base62-sha1="jSyNR6Dh9bLjtuEvcFfT7Tlv3zF" width="690" height="256" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8b5437bff29792217fdb7dea590220f201496b67_2_690x256.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8b5437bff29792217fdb7dea590220f201496b67_2_1035x384.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8b5437bff29792217fdb7dea590220f201496b67_2_1380x512.jpeg 2x" data-dominant-color="E6E6D1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×714 126 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @Divi (2026-04-02 13:44 UTC)

<p>I am already using this extension but still the values are not SUVbw. The values in the segments are also very high in the range of hundreds and thousands and it should be less than 10. Could you tell me if there is any other way?</p>

---

## Post #4 by @pieper (2026-04-02 13:51 UTC)

<p>Describe the source of your data, what format it’s in, and what might have been done to it since the scan was acquired.  It’s very important for you to know the exact history of the data if you want to process it correctly.</p>

---

## Post #5 by @fedorov (2026-04-02 14:40 UTC)

<p>Somewhat related to this is the new initiative to validate various SUV normalization tools against a digital phantom that attempts to mimic what various vendors do <a href="https://github.com/oncoray/suv_computation" class="inline-onebox">GitHub - oncoray/suv_computation: Manual for PET SUV Computation and Digital Reference Objects for its Verification · GitHub</a> - since there is no consistency in how various metadata attributes needed for SUV normalization are encoded in DICOM.</p>
<p>I tested Slicer SUV normalization to prepare submission to that initiative, and you can see the results here: <a href="https://github.com/oncoray/suv_computation/pull/2" class="inline-onebox">Add SUV measurement results using Slicer PET-IndiC QuantitativeIndicesTool by fedorov · Pull Request #2 · oncoray/suv_computation · GitHub</a>. As you can see from those results, Slicer does NOT produce the expected values for quite a few of phantom configurations: <a href="https://github.com/fedorov/suv_computation/blob/bff3dc49e7769691dab386d9f5e5bf60d6abce97/submissions/Slicer-PETIndiC/DRO_Slicer_PETIndiC.csv" class="inline-onebox">suv_computation/submissions/Slicer-PETIndiC/DRO_Slicer_PETIndiC.csv at bff3dc49e7769691dab386d9f5e5bf60d6abce97 · fedorov/suv_computation · GitHub</a>. Unfortunately, the group that introduced Slicer SUV capability is no longer maintaining it to investigate those issues.</p>
<p>Now, I personally do not know enough about the field to tell if phantom is correct and representative, but it is put together by the folks who know a lot more than me, and from the preliminary results presented by the organizers to the current participants (not public), there are some platforms that pass validation for most or all of the configurations.</p>
<p>You could compare the DICOM PET characteristics to those of the phantoms where Slicer failed, and maybe the flavor you have is not covered by the implementation. Hopefully, organizers of that challenge will make the results public eventually, and you will have access to alternative tools to process your data correctly.</p>
<p>But most definitely - before anything - as <a class="mention" href="/u/pieper">@pieper</a> suggested you should make sure your data is in the right format and has not been corrupted.</p>

---
