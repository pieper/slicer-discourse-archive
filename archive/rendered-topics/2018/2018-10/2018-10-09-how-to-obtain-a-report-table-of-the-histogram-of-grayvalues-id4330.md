---
topic_id: 4330
title: "How To Obtain A Report Table Of The Histogram Of Grayvalues"
date: 2018-10-09
url: https://discourse.slicer.org/t/4330
---

# how to obtain a report/table of the histogram of grayvalues 

**Topic ID**: 4330
**Date**: 2018-10-09
**URL**: https://discourse.slicer.org/t/how-to-obtain-a-report-table-of-the-histogram-of-grayvalues/4330

---

## Post #1 by @Nuria (2018-10-09 16:58 UTC)

<p>Hi!</p>
<p>I’m trying to obtain a table with the histogram of gray values of a volume (obtained from a segmentation using the mask volume) but I can’t. At the moment, I only see the plot in the volume module but I need the values. It is possible?</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2018-10-09 17:14 UTC)

<p>A solution is described in this post: <a href="https://discourse.slicer.org/t/histogram-of-volume-in-regions-defined-by-segments/2236">Histogram of volume in regions defined by segments</a></p>

---

## Post #3 by @Nuria (2018-10-09 17:56 UTC)

<p>When I paste the script to my slicer, it crashes, I have the version 4.8.1</p>

---

## Post #4 by @lassoan (2018-10-09 17:57 UTC)

<p>You need to use latest nightly version.</p>

---

## Post #5 by @Nuria (2018-10-09 18:58 UTC)

<p>Thanks! I will try it</p>

---

## Post #6 by @Nuria (2018-10-10 11:25 UTC)

<p>Hi again!</p>
<p>Now I have the latest nightly version, and the script works but I don’t know how to change it to work with my data. I have performed the segmentation (using thresholding values) with the segmentation module, then I have created the mask volume with the segment created and filling outside with 0. But this is all, I don’t know how to call my mask volume and segmentation to obtain the histogram chart and table. Also I would like to know how to obtain the histogram and table of my initial master volume.<br>
Sorry, I have never used python language.</p>

---

## Post #7 by @lassoan (2018-10-10 12:54 UTC)

<p>Run the script as is and modify it step-by-step to see the effect of your changes. I would strongly recommend to copy-paste the code into a Python scripted module (as described in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Programming_Tutorial">programming tutorial</a>) and run it line by line using a <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#How_can_I_use_a_visual_debugger_for_step-by-step_debugging">Python debugger</a>. If you are not confident with Python syntax, then spend a couple of days completing basic Python tutorials.</p>

---

## Post #8 by @Nuria (2018-10-10 13:47 UTC)

<p>Thanks a lot, I will try it</p>

---
