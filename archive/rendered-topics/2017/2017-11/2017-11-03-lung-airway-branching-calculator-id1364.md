---
topic_id: 1364
title: "Lung Airway Branching Calculator"
date: 2017-11-03
url: https://discourse.slicer.org/t/1364
---

# Lung airway branching calculator

**Topic ID**: 1364
**Date**: 2017-11-03
**URL**: https://discourse.slicer.org/t/lung-airway-branching-calculator/1364

---

## Post #1 by @jbassein (2017-11-03 18:31 UTC)

<p>Hey Guys,</p>
<p>I am trying to calculate the number of airway branch points in the lungs of several patient CT scans. Does anyone know how to do this in a fairly automatic fashion?</p>
<p>I am also looking to calculate the total diameter and wall thickness for a number of airways in a given scan. Any info on how to do this more automatically would be greatly appreciated.</p>
<p>Thanks! Jed</p>

---

## Post #2 by @lassoan (2017-11-03 19:04 UTC)

<p>Have you tried the CIP extension? <a href="https://chestimagingplatform.org/">https://chestimagingplatform.org/</a></p>
<p><a class="mention" href="/u/raul">@raul</a> should be able to help if you cannot figure out how to use it.</p>

---

## Post #3 by @jbassein (2017-11-03 19:50 UTC)

<p>Ya, I am currently working with CIP. But am having trouble doing the analysis I want. If you have done anything similar, I’d love some help/guidance.</p>

---

## Post #4 by @jbassein (2017-11-13 21:41 UTC)

<p>Hello <a class="mention" href="/u/raul">@raul</a></p>
<p>I’m trying to analyze branching and airway diameter. I can render the airways using the Airway segmentation module, but for some reason I only get a partial tree map, going only to 2nd or 3rd generation airways. Ideally, I’d like to look at 4th or 5th generation in most cases. I know I can use the airway inspector to get at diameter of both lumen and conducting airway tissue, but I was wondering If this could get more automatic, such that it calculates the airway lumen and diameter across a given volume, say the volume rendered from the airway segmentation of the conducting airways.</p>

---

## Post #5 by @Alice (2020-08-04 12:35 UTC)

<p>Oh,that’s what I want to do through 3D Slicer.Have you solved it ?</p>

---

## Post #6 by @lassoan (2020-08-04 12:51 UTC)

<p>Extract centerline module in SlicerVMTK extension in very recent Slicer Preview Releases can do this fully automatically. You just need to segment the airways up to that le el you are interested in.</p>
<p>For segmentation, you can try Fast marching effect:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="tJMGe3FMTk0" data-video-title="Airway segmentation from CT in 1 minute using 3D Slicer" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=tJMGe3FMTk0" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/tJMGe3FMTk0/maxresdefault.jpg" title="Airway segmentation from CT in 1 minute using 3D Slicer" width="" height="">
  </a>
</div>

<p>For going further you may try Local threshold or Grow from seeds effects.</p>

---

## Post #7 by @1119 (2020-10-29 02:54 UTC)

<p>Is the selection of thresholds fixed in this process? Or choose based on the quality of the image based on experience.</p>

---

## Post #8 by @lassoan (2020-10-30 19:36 UTC)

<p>Local thresholding effect takes a threshold range to generate seed regions (you can determine it from local threshold computed in a region of interest - see Local histogram section) and then it dynamically adjusts the threshold across the image (if you choose segmentation algorithm -&gt; watershed or grow-from-seeds).</p>

---

## Post #9 by @1119 (2020-11-02 07:03 UTC)

<p>Thank you for your answer. I watched the video above. Through the watershed, I saw that the threshold range is -350. I want to know how this one got it. Is it based on experience?</p>

---

## Post #10 by @lassoan (2020-11-02 17:14 UTC)

<p>You can get the value by visual inspection. If you want to be a bit more reproducible, you can pick the value from the local histogram.</p>

---
