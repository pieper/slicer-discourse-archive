---
topic_id: 34052
title: "Adjusting Segment Threshold"
date: 2024-01-30
url: https://discourse.slicer.org/t/34052
---

# Adjusting Segment Threshold

**Topic ID**: 34052
**Date**: 2024-01-30
**URL**: https://discourse.slicer.org/t/adjusting-segment-threshold/34052

---

## Post #1 by @jamieawren (2024-01-30 21:14 UTC)

<p>Hi Everyone,</p>
<p>I set a minimum threshold of 200 to use as a mask to create segments on CT data. I’ve realized that 200 was too high for my data, and I would like to readjust the threshold downward. Is there a way to do this automatically, or do I need to redo the segments?</p>
<p>Thank you!</p>

---

## Post #2 by @muratmaga (2024-01-30 21:37 UTC)

<p>If you have multiple segments all derived from an initial globally thresholded segment, I don’t think there is an easy way of doing this. Depending on how complex segmentation was, manually retouching them may even take longer than creating from scratch, using your new threshold range.</p>

---

## Post #3 by @lassoan (2024-01-31 00:04 UTC)

<p>If you just want to add nearby regions to the segment then you can:</p>
<ul>
<li>set the new range as “Editable intensity range” (in masking settings section at the bottom), and then</li>
<li>use “Margin” effect to add voxels around the segment (masking settings will ensure that only those voxels will be added to the segment that are in the specified intensity range)</li>
</ul>

---

## Post #4 by @jamieawren (2024-01-31 23:52 UTC)

<p>Thank you both for your replies!</p>
<p>The segments are very simple. Just a threshold mask used with the 20mm sphere brush in the paint segments editor to segment out portions of human crania. I just realized I need the threshold well below 200, and I was hoping there was a simple way to adjust/reset the threshold of an existing segment to avoid having to redo the work. Not months and months of work, but still about a week’s worth of time.</p>
<p>Jamie</p>

---

## Post #5 by @muratmaga (2024-02-01 00:59 UTC)

<p>If its that simple, then you can try what <a class="mention" href="/u/lassoan">@lassoan</a> suggested above. Maybe also you can closing filter (smoothing), again with the editable intensity range enabled to capture internal structure that wasn’t part of the original intensity range. Or similar to your original approach use the brush to capture missing ranges selectively.</p>

---

## Post #6 by @jamieawren (2024-02-01 02:17 UTC)

<p>I misunderstood <a class="mention" href="/u/lassoan">@lassoan</a> 's reply! You both saved my bacon!! Thank you so, so, very much!!! It’s behaving almost perfectly! It changes the existing segments feret diameter a smidge, but well within acceptable limits. I cannot thank you enough!</p>

---

## Post #7 by @lassoan (2024-02-01 08:43 UTC)

<p>Awesome. Thanks for letting us know that the idea worked.</p>

---
