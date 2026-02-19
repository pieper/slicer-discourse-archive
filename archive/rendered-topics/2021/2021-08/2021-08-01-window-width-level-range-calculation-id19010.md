---
topic_id: 19010
title: "Window Width Level Range Calculation"
date: 2021-08-01
url: https://discourse.slicer.org/t/19010
---

# Window width/level range calculation

**Topic ID**: 19010
**Date**: 2021-08-01
**URL**: https://discourse.slicer.org/t/window-width-level-range-calculation/19010

---

## Post #1 by @siyuan (2021-08-01 07:16 UTC)

<p>Hi, recently I found the automatic adjustion of window width and level using a selected region in Slicer was quite useful. I want to implement it in my own way in python using SimpleITK. I’ve checked VTK website but found littile information there. Here is what I found in the forum (a simlilar topic <a href="https://discourse.slicer.org/t/how-to-change-window-level-programmatically/9043" class="inline-onebox">How to change window/level programmatically</a>) and locate the algorithm right here: <a href="https://github.com/Kitware/VTK/blob/6a9c565da01bcd6295d0bcbb66c0a9d0d2eaa69e/Imaging/Statistics/vtkImageHistogramStatistics.cxx" class="inline-onebox" rel="noopener nofollow ugc">VTK/vtkImageHistogramStatistics.cxx at 6a9c565da01bcd6295d0bcbb66c0a9d0d2eaa69e · Kitware/VTK · GitHub</a></p>

---

## Post #2 by @siyuan (2021-08-01 17:02 UTC)

<p>I was wondering whether the range is calculated based on the histogram or simply min-max value of selected region.</p>

---

## Post #3 by @jamesobutler (2021-08-01 19:33 UTC)

<p>Window/Level based on selection area is discussed at <a href="https://discourse.slicer.org/t/feedback-requested-how-to-improve-mouse-interaction-in-views/6420/12" class="inline-onebox">Feedback requested: How to improve mouse interaction in views? - #12 by lassoan</a></p>
<p>Auto Window/Level was changed from a histogram bimodal analysis to a fixed percentile based method. It was updated in Slicer as <a href="https://github.com/Slicer/Slicer/commit/bc0d938c639cb7c3d87a816cf24b3be73542c09b" class="inline-onebox" rel="noopener nofollow ugc">ENH: Improved automatic scalar volume display window/level computation · Slicer/Slicer@bc0d938 · GitHub</a></p>

---

## Post #5 by @siyuan (2021-08-02 17:26 UTC)

<p>Thanks lot. It wll be of great help if you can explain the idea behind the auto-windowing method of selection area. <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=10" title=":smiley:" class="emoji" alt=":smiley:"></p>

---
