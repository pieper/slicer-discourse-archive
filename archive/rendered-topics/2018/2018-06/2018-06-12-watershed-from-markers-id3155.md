---
topic_id: 3155
title: "Watershed From Markers"
date: 2018-06-12
url: https://discourse.slicer.org/t/3155
---

# Watershed from markers

**Topic ID**: 3155
**Date**: 2018-06-12
**URL**: https://discourse.slicer.org/t/watershed-from-markers/3155

---

## Post #1 by @vegoria (2018-06-12 18:45 UTC)

<p>Hi!<br>
I’m making my first steps with developing slicer extention and I’ve stuck in one place…<br>
I’ve got MR of sacroiliac. I’m trying to process segmentation of bones using watershed from markers.</p>
<p>I’ve got something like that:</p>
<blockquote>
<p>import SimpleITK as sitk<br>
import numpy as np</p>
<p>para = {‘sigma’:2}<br>
itkimg = sitk.GetImageFromArray(imageArray)<br>
itkimg = sitk.DiscreteGaussian(itkimg, para[‘sigma’])<br>
itkimg = sitk.GradientMagnitude(itkimg)</p>
<p>lineimg = sitk.MorphologicalWatershedFromMarkers(itkimg, itkmarker, markWatershedLine=True)</p>
</blockquote>
<p>where imageArray is numpy array which contains image.</p>
<p>but I need “itkmarker” image - it should be binary image which contains markers… And I have no idea how to get it. Or maybe there is simplier way to run that algorithm? I’ll be grateful for any tips.</p>

---

## Post #2 by @lassoan (2018-06-12 19:33 UTC)

<p>ITK watershed segmentation is implemented in Watershed effect in SegmentEditorExtraEffects extension. The source code is available here: <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/master/SegmentEditorWatershed/SegmentEditorWatershedLib/SegmentEditorEffect.py">https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/master/SegmentEditorWatershed/SegmentEditorWatershedLib/SegmentEditorEffect.py</a></p>
<p>You are free to clone this implementation and modify it to suit your needs, or you can send pull request with proposed enhancements.</p>
<p>You can use this segmentation method without segment editor user interface as shown in these examples: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script</a></p>

---
