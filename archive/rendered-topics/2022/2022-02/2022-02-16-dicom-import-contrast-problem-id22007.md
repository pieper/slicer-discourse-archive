---
topic_id: 22007
title: "Dicom Import Contrast Problem"
date: 2022-02-16
url: https://discourse.slicer.org/t/22007
---

# DICOM import contrast problem

**Topic ID**: 22007
**Date**: 2022-02-16
**URL**: https://discourse.slicer.org/t/dicom-import-contrast-problem/22007

---

## Post #1 by @AsliBeriL (2022-02-16 23:11 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.11.20210226</p>
<p>Dear 3D Slicer experts,</p>
<p>I searched for the answer to my question but couldn’t find it. When I add a new patient (MRI stacks), the contrast of the slices looks very clear. However, when I look at it from Radiant, the contrast is quite normal. Where could the problem be?</p>
<p>Thanks in advance</p>

---

## Post #2 by @pieper (2022-02-16 23:13 UTC)

<p>Can you describe what you mean by “clear” - is that a good thing or a bad thing?  Maybe you just need to adjust the window/level - you can do that with the mouse mode in the toolbar or go to the Volumes module and select the image for adjustment.</p>

---

## Post #3 by @AsliBeriL (2022-02-16 23:21 UTC)

<p>MRI sections look very light colored. I’ve added a screenshot for better understanding. I tried both with the mouse and in the volumes module, but the result didn’t change.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad9ac1315edacc3f71d9f13328c552b9793a9f15.jpeg" data-download-href="/uploads/short-url/oLMa5tWIFzgWkkR6eyCNTwyGAyV.jpeg?dl=1" title="Ekran Alıntısı" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ad9ac1315edacc3f71d9f13328c552b9793a9f15_2_690x355.jpeg" alt="Ekran Alıntısı" data-base62-sha1="oLMa5tWIFzgWkkR6eyCNTwyGAyV" width="690" height="355" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ad9ac1315edacc3f71d9f13328c552b9793a9f15_2_690x355.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ad9ac1315edacc3f71d9f13328c552b9793a9f15_2_1035x532.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ad9ac1315edacc3f71d9f13328c552b9793a9f15_2_1380x710.jpeg 2x" data-dominant-color="A9A9AF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Ekran Alıntısı</span><span class="informations">1600×825 129 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @pieper (2022-02-16 23:23 UTC)

<p>Hmm, looks like a normal enough scan.  Did you try clicking the presets?</p>

---

## Post #5 by @AsliBeriL (2022-02-16 23:36 UTC)

<p>Sorry, i don’t know where the presets are. If you’re talking about the window / level presets option above, it’s not clickable</p>

---

## Post #6 by @AsliBeriL (2022-02-17 08:53 UTC)

<p>Yes, there is no problem when I click on presets in volume rendering. But I didn’t understand why the original series looked like this. Does anyone know the solution to the problem? <img src="https://emoji.discourse-cdn.com/twitter/expressionless.png?v=12" title=":expressionless:" class="emoji" alt=":expressionless:" loading="lazy" width="20" height="20"></p>

---

## Post #7 by @lassoan (2022-02-18 16:50 UTC)

<p>Please try the latest Slicer Preview Release and let us know if the default window/level looks good.</p>
<p>If you are interested in the details:</p>
<p>Slicer uses the window/level setting that is stored in the DICOM file. The result may be different from Radiant, because Radiant is a 2D viewer (with some 3D features), so it treats each 2D slice separately, and so it displays each slice with a different window/level (that was saved for that slice). However, Slicer shows that data set in 3D and so it must use the same window/level for every slice.</p>
<p>In latest Slicer Stable Release the window/level of the first slice was used for all slices, which in some cases was not optimal (because the first slice can be empty, e.g., above the head). Recent Slicer Preview Releases use the middle slice instead, which has a more representative window/level.</p>

---

## Post #8 by @AsliBeriL (2022-02-19 12:02 UTC)

<p>I downloaded preview release (version 4.13.0) and it works! As you said i think the locations of the slices can be different.</p>
<p>Thanks for your interest and answer <a class="mention" href="/u/lassoan">@lassoan</a> !</p>

---
