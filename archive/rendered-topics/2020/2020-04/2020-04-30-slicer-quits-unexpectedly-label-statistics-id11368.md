---
topic_id: 11368
title: "Slicer Quits Unexpectedly Label Statistics"
date: 2020-04-30
url: https://discourse.slicer.org/t/11368
---

# Slicer quits unexpectedly - Label statistics

**Topic ID**: 11368
**Date**: 2020-04-30
**URL**: https://discourse.slicer.org/t/slicer-quits-unexpectedly-label-statistics/11368

---

## Post #1 by @LearningSlicerYay (2020-04-30 17:41 UTC)

<p><strong>Slicer Version:</strong> 4.10.2<br>
<strong>OS:</strong> Ubuntu</p>
<p>Hi everyone,</p>
<p>I’m not sure if this is the same issue <a href="https://discourse.slicer.org/t/slicer-quits-unexpectedly/11333">as this thread,</a> but Slicer has been quitting on me unexpectedly as well. Particularly, every time I try to calculate label statistics from a scalar map (mean diffusivity, in particular). I do not get this issue when I try with the other maps of interest (in this case, FA, Trace, RA, Parallel and Perpendicular Diffusivity).</p>
<p>Any help would be greatly appreciated - thank you!</p>

---

## Post #2 by @lassoan (2020-04-30 18:39 UTC)

<p>Label statistics module is superseded by Segment statistics module. Can you try if you experience any problems using Segment Statistics module on a recent Slicer Preview Release?</p>

---

## Post #3 by @LearningSlicerYay (2020-04-30 19:07 UTC)

<p>Hi Andras,</p>
<p>I downloaded 4.11.0 and installed the dMRI plugin. When I try to open MRML scenes that have the MeanDiffusivity label map created, Slicer crashes. It can open scenes that do not have the MeanDiffusivity label map, but when I try to make it (to test the segment statistics module), again it crashes. Not sure what the issue is.</p>
<p>I went back to 4.10.2 and it can be calculated with Segment statistics though, which is great.</p>
<p>Thanks for your help.</p>

---

## Post #4 by @lassoan (2020-04-30 19:33 UTC)

<p>Can you share a scene that causes Slicer-4.11 to crash so that we can investigate and fix the issue? Does Slicer-4.11 work correctly if instead of loading the scene file (.mrml) you just load the MeanDiffusivity label map and other files?</p>

---

## Post #5 by @LearningSlicerYay (2020-04-30 20:12 UTC)

<p>Hi Andras,</p>
<p>I don’t think I can share the scenes I was working with, but I was able to replicate the problem using the DTI tutorial data from the 3DSlicer group. Is there a place I can upload it?</p>
<p>Using both my data the the tutorial data, I was unable to open the mean diffusivity files on 4.11 - still crashes. FA and the other scalar maps work fine though.</p>

---

## Post #6 by @lassoan (2020-04-30 20:23 UTC)

<p>Yes, please upload that scene to onedrive/dropbox/googledrive and post the link here. Thanks!</p>

---

## Post #7 by @LearningSlicerYay (2020-04-30 20:38 UTC)

<p><a href="https://drive.google.com/file/d/1KX0ulWO-sqjcwrZpc10e17CNAHk7tlaT/view?usp=sharing" rel="nofollow noopener">Here you go.</a></p>

---

## Post #8 by @lassoan (2020-05-01 13:36 UTC)

<p>Mean diffusivity image contains invalid floating-point value (NaN), which causes a VTK filter (vtkImageHistogramStatistics) to crash when it tries to figure out a good default window/level value. I’ve fixed that problem in VTK now, it’ll just take a few days to get that integrated into Slicer (you can track progress <a href="https://github.com/Slicer/Slicer/issues/4907">here</a>).</p>
<p>How did you compute this mean diffusivity image? It would be probably better to change that algorithm to not have NaN values in the result (e.g., replace by 0 or -1), as such values rarely used and may cause unexpected behavior in various software.</p>

---

## Post #9 by @LearningSlicerYay (2020-05-01 14:45 UTC)

<p>Hi Andras,</p>
<p>Brilliant! Thank you for the fix, eager to see it integrated. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>I actually just use the SlicerDMRI plugin to compute the mean diffusivity map. Under Diffusion -&gt; Quantify -&gt; Diffusion Tensor Scalar Maps. I then choose my DTI and create the map. I’ve tried maybe half the maps, but only this one causes the issue so far.</p>

---

## Post #10 by @lassoan (2020-05-01 15:36 UTC)

<p>Could you please report the issue here: <a href="https://github.com/SlicerDMRI/SlicerDMRI/issues">https://github.com/SlicerDMRI/SlicerDMRI/issues</a><br>
Thank you!</p>

---
