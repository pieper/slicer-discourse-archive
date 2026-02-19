---
topic_id: 30680
title: "Segmenting Ischemic Stroke Lesions Based On Adc Threshold"
date: 2023-07-19
url: https://discourse.slicer.org/t/30680
---

# Segmenting ischemic stroke lesions based on ADC threshold

**Topic ID**: 30680
**Date**: 2023-07-19
**URL**: https://discourse.slicer.org/t/segmenting-ischemic-stroke-lesions-based-on-adc-threshold/30680

---

## Post #1 by @lvdw (2023-07-19 15:51 UTC)

<p>Operating system: MacOS<br>
Slicer version: 5,2,2</p>
<p>I’m not sure if this issue isn’t solved elsewhere but I couldn’t find it. I’m rather new to Slicer. I would like to segment ischemic strokes based on sb1000 and ADC, but I would like to put an ADC threshold on ≤620 ×10−6 mm2/s using the threshold tool. I have done so (see screenshot: red is ADC threshold 0-620.00, green is the semi-manually segmented lesion mostly based on sb1000 thresholds and manually corrected with visual inspection of the  ADC).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6a372bf8ac4dce4d21e8dfa2bc159a2c46ff6f64.jpeg" data-download-href="/uploads/short-url/f9CODSi7TBeCdL3hXwiSklRENOk.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6a372bf8ac4dce4d21e8dfa2bc159a2c46ff6f64_2_690x384.jpeg" alt="image" data-base62-sha1="f9CODSi7TBeCdL3hXwiSklRENOk" width="690" height="384" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6a372bf8ac4dce4d21e8dfa2bc159a2c46ff6f64_2_690x384.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6a372bf8ac4dce4d21e8dfa2bc159a2c46ff6f64_2_1035x576.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6a372bf8ac4dce4d21e8dfa2bc159a2c46ff6f64_2_1380x768.jpeg 2x" data-dominant-color="383431"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1070 142 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/360876f44975580d3ad0f213a7954637fb579bb3.jpeg" data-download-href="/uploads/short-url/7HZUY7mc9q3ZCrbNEX5Ybz8vrqj.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/360876f44975580d3ad0f213a7954637fb579bb3_2_690x384.jpeg" alt="image" data-base62-sha1="7HZUY7mc9q3ZCrbNEX5Ybz8vrqj" width="690" height="384" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/360876f44975580d3ad0f213a7954637fb579bb3_2_690x384.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/360876f44975580d3ad0f213a7954637fb579bb3_2_1035x576.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/360876f44975580d3ad0f213a7954637fb579bb3_2_1380x768.jpeg 2x" data-dominant-color="383431"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1070 143 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I feel like this could be correct (and my manual segmentation based on sb1000 was far to generous) but I’m not sure if this is actually the correct way to set that threshold. Usually I load sb1000 and ADC images separately, but would it make a difference to recalculate the ADC from sb1000 and sb0 with slicer when possible? I struggle to do that correctly and to be able to set a threshold there.</p>

---

## Post #2 by @lassoan (2023-07-21 14:13 UTC)

<p>It is correct to use multiple images to perform a segmentation. Setting the threshold based on visually feedback (the preview shown in slice views) is reasonable, too.</p>

---
