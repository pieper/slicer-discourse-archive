---
topic_id: 12301
title: "Loading Dicom Frames As Volume"
date: 2020-06-30
url: https://discourse.slicer.org/t/12301
---

# Loading DICOM frames as volume

**Topic ID**: 12301
**Date**: 2020-06-30
**URL**: https://discourse.slicer.org/t/loading-dicom-frames-as-volume/12301

---

## Post #1 by @mjg (2020-06-30 15:47 UTC)

<p>Hello,</p>
<p>I am trying to load in DICOM frames as a volume; there is no change in position but they are taken at different times to see cardiac muscle contraction. I can’t seem to load the set as a volume through any Slicer methods. I am coding my module in Python. How might I go about this issue in Slicer or Python?</p>
<p>I am using an OSIRIX “cine” DICOM set if that helps!</p>
<p>The normal Slicer DICOM load results in this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f1f09d5758cfbedd321bab40da4e942e8eb1ffb8.png" data-download-href="/uploads/short-url/ywiAg0UtGmqzF1LjcIhGIlDGnsk.png?dl=1" title="Screen Shot 2020-06-30 at 9.37.02 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f1f09d5758cfbedd321bab40da4e942e8eb1ffb8_2_622x500.png" alt="Screen Shot 2020-06-30 at 9.37.02 AM" data-base62-sha1="ywiAg0UtGmqzF1LjcIhGIlDGnsk" width="622" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f1f09d5758cfbedd321bab40da4e942e8eb1ffb8_2_622x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f1f09d5758cfbedd321bab40da4e942e8eb1ffb8_2_933x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f1f09d5758cfbedd321bab40da4e942e8eb1ffb8_2_1244x1000.png 2x" data-dominant-color="575770"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-06-30 at 9.37.02 AM</span><span class="informations">1674×1344 176 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thank you!</p>

---

## Post #2 by @lassoan (2020-06-30 17:48 UTC)

<p>It all looks good, but since it is a single slice, you probably want to align a slice view to the image plane instead of showing the default orthogonal slices, by <a href="https://discourse.slicer.org/t/segmentation-editor-how-to-disable-painting-on-adjacent-slices/1459/4">clicking “Rotate to volume plane” button in the slice view controller</a>.</p>
<p>What do you plan to do with this 2D+t cine image sequence? Just visualize in a slice viewer or segment, quantify, fuse with other images?</p>

---

## Post #3 by @pieper (2020-06-30 18:00 UTC)

<p>By the way, <a href="https://slicer.readthedocs.io">Slicer’s readthedocs</a> has a lot of useful information but is still missing key points.<br>
I noticed that the Rotate to Volume Plane info wasn’t described, so <a href="https://github.com/Slicer/Slicer/commit/ea5f2cc90bdad08d689073b8b7b431adbd7df75a">I added more documentation</a> in hopes that people will be able to figure it out more easily in the future.</p>
<p>It would be great if anyone who learns something new that’s not in the readthedocs would write up a pull request to improve the material.  All you need is a github account and you can edit the files directly in the browser.</p>

---

## Post #4 by @mjg (2020-06-30 18:53 UTC)

<p>Thank you for the help! I can see the single slice now which is good. However, I didn’t explain what I’m trying to do very well. I want to place markups on each frame within Slicer, so I need to load the 2D slices with the time component acting as the third axis. Essentially stacking the DICOM images along an axis so that I could scroll through the set on a slice view and place markups onto each frame. Then I could export the markups with each position along the time axis corresponding to a specific frame.</p>

---

## Post #5 by @lassoan (2020-06-30 19:14 UTC)

<p>If you load this volume as a volume sequence (by setting in menu: Edit / Application settings -&gt; DICOM / Preferred multi-volume format -&gt; volume sequence, then loading the sequence again), then you can replay it as a volume and create time-varying markups on them.</p>
<p>To create a markup that changes in sync with the volume, go to Sequences module, add a new sequence by clicking the green “+” button, choose your markup node as “Proxy node” in the table, and check “Save changes” (to automatically save markups modifications into the time sequence).</p>

---

## Post #6 by @mjg (2020-07-01 15:38 UTC)

<p>Fantastic, thank you! This is very helpful.</p>

---

## Post #7 by @mjg (2020-07-01 15:53 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> 's solution works if the DICOM is loaded with the multi volume plugin. Or the DICOM can be loaded with the scalar volume plugin and check “Allow loading subseries by time” in settings. Then frames can be moved through spatially. Both are great tools!</p>

---
