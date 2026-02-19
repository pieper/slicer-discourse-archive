---
topic_id: 30494
title: "I Am Having Trouble With Error Codes When Analyzing A Series"
date: 2023-07-10
url: https://discourse.slicer.org/t/30494
---

# I am having trouble with error codes when analyzing a series of images.

**Topic ID**: 30494
**Date**: 2023-07-10
**URL**: https://discourse.slicer.org/t/i-am-having-trouble-with-error-codes-when-analyzing-a-series-of-images/30494

---

## Post #1 by @mikiN (2023-07-10 12:33 UTC)

<p>I am analyzing images with CTlunganalyzer. When I try to analyze the second person’s data in succession, I get the error code “failed to compute results: ‘None Type’ object has no attribute ‘LookupValue’”. I have no choice but to exit the 3D slicer once.</p>
<p>Can someone please help me?</p>

---

## Post #2 by @rbumm (2023-07-10 13:48 UTC)

<p>Thank you for the feedback.<br>
How do you analyze the second person’s data in detail?<br>
Are you closing the scene, then loading new data, then starting LungCTSegmenter and -Analyzer again?</p>

---

## Post #3 by @rbumm (2023-07-10 19:46 UTC)

<p>We pushed an update <a href="https://github.com/rbumm/SlicerLungCTAnalyzer/commit/f77147e59a972637f4a23eea3b9c49ed738ae711">f77147e</a> to make subsequent segmentations a bit more fail-proof.<br>
There is now a check for the existence of CT volume and lung segmentation with right and left lung segment detection when you press “Compute results”.</p>
<p>Please try it out after an update via the extension manager in 1-2 days.</p>

---

## Post #4 by @mikiN (2023-07-10 23:22 UTC)

<p>Thank you for your reply.<br>
I tried the method myself several times. As a result, perhaps I had incorrectly set the lung segmentation and base CT with different people. Therefore, I have solved the problem!</p>
<p>Thank you for sharing the update.</p>

---
