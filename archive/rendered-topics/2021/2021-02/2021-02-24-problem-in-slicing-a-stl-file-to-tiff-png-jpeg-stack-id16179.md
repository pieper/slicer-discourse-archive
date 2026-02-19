---
topic_id: 16179
title: "Problem In Slicing A Stl File To Tiff Png Jpeg Stack"
date: 2021-02-24
url: https://discourse.slicer.org/t/16179
---

# Problem in slicing a stl file to tiff/PNG/jpeg stack

**Topic ID**: 16179
**Date**: 2021-02-24
**URL**: https://discourse.slicer.org/t/problem-in-slicing-a-stl-file-to-tiff-png-jpeg-stack/16179

---

## Post #1 by @Mehrdad (2021-02-24 13:38 UTC)

<p>Dear Support Team,</p>
<p>I have stl file of packing of angular particles. The cubic packing size is 400 voxels and the voxel size is 0.03111 mm. I need to convert the stl file to the tiff stack with 400 slices and a pixel size of 0.03111 mm. I have tried the python script provided by the team in 3d slicer (<a href="https://discourse.slicer.org/t/convert-stl-file-to-high-resolution-tiff-stack/15949/8" class="inline-onebox">Convert STL file to high-resolution TIFF stack - #8 by lassoan</a>) but didn’t get the correct result. It just gave 2 slices after 1 hour and the slices just include a single black point.<br>
I need to know what values should I use in the following parts:<br>
outputVolumeLabelValue, inPlaneResolutionDpi, planeThicknessMm, outputVolumeMarginMm</p>
<p>How would you calculate 25.4 in the following part? What values should I use for my packing?<br>
imageSpacingMm = [25.4/inPlaneResolutionDpi, 25.4/inPlaneResolutionDpi, planeThicknessMm]</p>
<p>I look forward to hearing back from you.</p>
<p>Kind regards,<br>
Mehrdad</p>

---

## Post #2 by @lassoan (2021-02-25 18:34 UTC)

<p>If you have your image spacing defined as mm/pixel instead of inches/pixel (DPI) then you can set that directly in imageSpacingMm. 0.03111mm/pixel = 0.0012248 in/pixel =&gt; 816 pixel/in (DPI), so the default 400 DPI should be OK, but just for initial testing you can try lower resolution (40DPI).</p>
<p>How many points does your STL file contain? Can you share the file so that I can test it?</p>

---

## Post #3 by @Mehrdad (2021-02-26 00:02 UTC)

<p>Hi Lassoan,</p>
<p>Thanks for your advice. What value should I use for outputVolumeLabelValue and outputVolumeMarginMm?</p>
<p>Should imageSpacingMm be [0.03111, 0.03111, 0.03111] in my case?<br>
planeThicknessMm=0.03111?<br>
inPlaneResolutionDpi=400?</p>
<p>How should I share the stl file? I could not attach the stl file.</p>
<p>Thanks for your help. I look forward to hearing back from you.</p>
<p>Kind regards,<br>
Mehrdad</p>

---

## Post #4 by @lassoan (2021-02-26 03:57 UTC)

<aside class="quote no-group" data-username="Mehrdad" data-post="3" data-topic="16179">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/e0b2c6/48.png" class="avatar"> Mehrdad:</div>
<blockquote>
<p>outputVolumeLabelValue</p>
</blockquote>
</aside>
<p>Whatever non-zero value you would like to see in the image inside the model.</p>
<aside class="quote no-group" data-username="Mehrdad" data-post="3" data-topic="16179">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/e0b2c6/48.png" class="avatar"> Mehrdad:</div>
<blockquote>
<p>Should imageSpacingMm be [0.03111, 0.03111, 0.03111] in my case?<br>
planeThicknessMm=0.03111?<br>
inPlaneResolutionDpi=400?</p>
</blockquote>
</aside>
<p>Yes, set <code>imageSpacingMm=[0.03111, 0.03111, 0.03111]</code> directly and remove the now redundant <code>planeThicknessMm</code> and <code>inPlaneResolutionDpi</code> variables.</p>
<aside class="quote no-group" data-username="Mehrdad" data-post="3" data-topic="16179">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/e0b2c6/48.png" class="avatar"> Mehrdad:</div>
<blockquote>
<p>How should I share the stl file? I could not attach the stl file.</p>
</blockquote>
</aside>
<p>Upload to somewhere (dropbox, onedrive, google drive, …) and post the link here.</p>

---
