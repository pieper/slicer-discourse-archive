# Vessel segmentation on version 5.8.1 for mac

**Topic ID**: 42293
**Date**: 2025-03-25
**URL**: https://discourse.slicer.org/t/vessel-segmentation-on-version-5-8-1-for-mac/42293

---

## Post #1 by @AlexM (2025-03-25 12:40 UTC)

<p>Hi,</p>
<p>I am new to 3D slicer and am trying to segment the abdominal aorta for a study.</p>
<p>I have installed the SegmentEditorExtraEffects and SlicerVMTK extensions, and have been following the instructions found in this youtube video (<a href="https://www.youtube.com/watch?v=hm2x5Osn5GE" rel="noopener nofollow ugc">https://www.youtube.com/watch?v=hm2x5Osn5GE</a>) to try generate a 3D model of the segmented aorta.</p>
<p>However, when I try to use the Local Threshold effect, the CT images start flashing slowly (fade bright to dark in a slow strobing effect - making it difficult to assess the anatomy well) and when I try to generate the 3D image (by pressing command + left click over the segment of aorta I have selected with the yellow line) the 3D image generated is the entire abdomen - not the isolated aorta.</p>
<p>I tried installing the latest version of 3D slicer (5.8.1) and this did not fix the problem.<br>
I have also tried using the 3D ‘centre view’ function and this did not help.</p>
<p>Help would be very much appreciated!</p>

---

## Post #2 by @chir.set (2025-03-25 14:00 UTC)

<aside class="quote no-group" data-username="AlexM" data-post="1" data-topic="42293">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/3da27b/48.png" class="avatar"> AlexM:</div>
<blockquote>
<p>for a study.</p>
</blockquote>
</aside>
<p>Assuming you are using a good quality CT scan with contrast intensity range between 300 and 500 in the big arteries, you may use the ‘Flood filling’ effect with a tolerance value between 70 and 110 and a ‘Neighbourhood size’ between 1.5 and 2.5 or more. It usually results in a fast and extended lumen segmentation.</p>
<p>You may also consider the “Quick artery segmentation” module in the SlicerVMTK extension. It proceeds as above and can do a little more in an automated way. 2 or 3 points, a box and off you go.</p>

---
