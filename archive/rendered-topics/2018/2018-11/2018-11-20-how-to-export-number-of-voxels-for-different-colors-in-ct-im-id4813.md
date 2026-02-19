---
topic_id: 4813
title: "How To Export Number Of Voxels For Different Colors In Ct Im"
date: 2018-11-20
url: https://discourse.slicer.org/t/4813
---

# How to export number of voxels for different colors in CT images after segmentation?

**Topic ID**: 4813
**Date**: 2018-11-20
**URL**: https://discourse.slicer.org/t/how-to-export-number-of-voxels-for-different-colors-in-ct-images-after-segmentation/4813

---

## Post #1 by @sali (2018-11-20 14:44 UTC)

<p>Dear experts</p>
<p>I segmented the human Brain with the editor modules for 100 slices of CT images, manually, now, I need to extract the number of voxels for each color with python or …, how can I do that?<br>
Thanks</p>

---

## Post #2 by @lassoan (2018-11-20 15:37 UTC)

<p>Are you interested in the volume of a segment?</p>

---

## Post #3 by @sali (2018-11-20 16:15 UTC)

<p>Dear Andras,<br>
I exactly need to know the number of voxels(row and column) of each color(segmented parts in each slice), because, I used these CTs as geometry and I have the distributed energy in each voxel of each slice in a text file. Now,I want to calculate the energy distributed in each part.</p>

---

## Post #4 by @mag (2018-11-20 19:36 UTC)

<p>Have you tried Segment Statistics already? It returns a lot of information including number of voxels of each segment in a segmentation. You can find it under “Quantification” and all you have to do is select which volume you are working on and which segmentation and it will produce a table with the results.</p>

---

## Post #5 by @lassoan (2018-11-21 00:11 UTC)

<aside class="quote no-group" data-username="sali" data-post="3" data-topic="4813">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/53a042/48.png" class="avatar"> sali:</div>
<blockquote>
<p>I used these CTs as geometry and I have the distributed energy in each voxel of each slice in a text file</p>
</blockquote>
</aside>
<p>If you can save this information in nrrd file format (a plain binary volume and a text file that describes size, position, spacing, etc.) then you can nicely visualize it in Slicer and if you set that as input for Segment Statistics module then you’ll get statistics, such as mean/max/average energy per segment.</p>

---

## Post #6 by @sali (2018-11-26 10:35 UTC)

<p>Thanks for your help and sorry for the late reply,<br>
but the “Quantification”  just gave me the volume of that segment, not the number of voxels !!! which one should I use? segment statistic?</p>

---

## Post #7 by @sali (2018-11-26 10:41 UTC)

<p>Thanks for your help,<br>
yes, I save these segments in .nrrd file format, and I converted  these binary files as .png file with python, but i could not get good result, is there another way to analyze these data which can find the number of voxels for each segment in each slice?</p>

---

## Post #8 by @lassoan (2018-11-26 14:30 UTC)

<p>Segment statistics gives you the number of voxels. If you need number of voxels (cross-section area by slice) then you can find a readily usable solution here: <a href="https://discourse.slicer.org/t/using-numpy-reslice-to-get-slices-of-segment/2257/3">Using numpy reslice to get slices of segment</a></p>

---
