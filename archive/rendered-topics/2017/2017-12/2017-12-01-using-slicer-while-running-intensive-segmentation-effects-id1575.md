---
topic_id: 1575
title: "Using Slicer While Running Intensive Segmentation Effects"
date: 2017-12-01
url: https://discourse.slicer.org/t/1575
---

# Using Slicer while running intensive Segmentation effects

**Topic ID**: 1575
**Date**: 2017-12-01
**URL**: https://discourse.slicer.org/t/using-slicer-while-running-intensive-segmentation-effects/1575

---

## Post #1 by @jamesobutler (2017-12-01 16:20 UTC)

<p>Hi,</p>
<p>I’m a big user of the segment editor and like to use the “Fill Between Slices” and “Smoothing” effect when segmenting tumors in ultrasound volumes. The “Fill Between Slices” is fast (&lt;1 second), but when running “Median” smoothing with the Kernel size that I prefer, there is quite a processing delay.  Slicer will show the busy spinning wheel, but I’m unable to move on and start my next segmentation because Slicer is unresponsive and my CPU is maxed out.  Would it be possible to prevent some of these process intensive effects from blocking the Slicer GUI?  I would like to speed up my segmentation speed especially since I’m segmenting large quantities of ultrasound data from mice studies.</p>
<p>I’m currently using Slicer 4.8.0.</p>
<p>Thanks,<br>
James</p>

---

## Post #2 by @pieper (2017-12-01 16:41 UTC)

<p>Good point James.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> what do you think about making some of these effect asynchronous?  We have for the SimpleFilters module we put all the SimpleITK processes in a separate thread and can apply the same trick for vtk filters (so long as we know they won’t have events that impact the gui or rendering).</p>
<p>Here’s some of the background:</p>
<p><a href="https://na-mic.org/wiki/2013_Project_Week:Threaded_SimpleITK_Modules" class="onebox" target="_blank">https://na-mic.org/wiki/2013_Project_Week:Threaded_SimpleITK_Modules</a></p>
<p><a href="http://slicer-devel-archive.65872.n3.nabble.com/Unlocking-Python-GIL-for-SimpleITK-td4030747.html" class="onebox" target="_blank">http://slicer-devel-archive.65872.n3.nabble.com/Unlocking-Python-GIL-for-SimpleITK-td4030747.html</a></p>

---

## Post #3 by @lassoan (2017-12-01 16:43 UTC)

<p>It could be feasible (the easiest way would be to perform processing in CLI modules, but alternative methods that Steve mentioned should work, too). However, there are a number of items higher on the priority list than allowing background processing in effects.</p>
<p>To address the specific issue of smoothing with large kernels: If you need to use large kernels it may mean that a lower-resolution image could be enough to store the level of details you need. Increasing the voxel size would reduce the number of voxels and the kernel size, so by making the voxel size 2x larger you may get 10-100x speed improvement. You may also consider smoothing all the segments in one step at the end, using joint smoothing method.</p>

---
