---
topic_id: 23205
title: "Optical Marker Tracking And Outputting Positional Data"
date: 2022-04-30
url: https://discourse.slicer.org/t/23205
---

# Optical marker tracking and outputting positional data

**Topic ID**: 23205
**Date**: 2022-04-30
**URL**: https://discourse.slicer.org/t/optical-marker-tracking-and-outputting-positional-data/23205

---

## Post #1 by @jh3chu (2022-04-30 01:18 UTC)

<p>Hello,</p>
<p>New to Slicer and Python and am currently working on a project using the the optical marker tracking from PLUS and visualizing it with the SlicerIGT module.</p>
<p>I currently have a .mha sequence file saved tracking the transformation matrices of the markers (done using the Perk Tutor Transform Recorder). Is there a module that can calculate velocity and acceleration based on a sequence of transformation matrices? If not, would creating a module/script to read in the .mha file for the velocity and acceleration calculation be the easiest way to approach this?</p>
<p>Any help would be greatly appreciated!<br>
Thanks,<br>
Jonathan</p>

---

## Post #2 by @ungi (2022-04-30 13:27 UTC)

<p>Hi, the Perk Evaluator module in the Perk Tutor extension has some metrics. If you look at the source code, you will see that it was designed to make it easy to add additional metrics. Velocity and acceleration change over time, so there would not be a single value for a recording. But you could add metrics that calculate e.g. average velocity and average acceleration over the course of the whole sequence.</p>

---
