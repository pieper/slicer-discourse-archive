---
topic_id: 1353
title: "Reformat View From Fiducial Points Ac Pc"
date: 2017-11-02
url: https://discourse.slicer.org/t/1353
---

# Reformat view from fiducial points (AC-PC)

**Topic ID**: 1353
**Date**: 2017-11-02
**URL**: https://discourse.slicer.org/t/reformat-view-from-fiducial-points-ac-pc/1353

---

## Post #1 by @Andras_Jakab (2017-11-02 16:02 UTC)

<p>Dear Slicer community,</p>
<p>I would like to ask if there is a way to control and reformat the views (for example, the red/axial) to be parallel to the AC-PC plane, if AC and PC points are fiducials that are placed in the scene. Is there a python solution or command for this?<br>
So, not re-sampling the image to ac-pc parallel slices, but rather just to change the view, while the user does segmentation.</p>
<p>Thanks a lot<br>
Best regards<br>
Andras</p>

---

## Post #2 by @lassoan (2017-11-02 16:12 UTC)

<p>You can use <code>Reformat</code> module to reorient slice views.</p>
<p>You can compute AC-PC plane transform using <code>ACPC Transform</code> module.</p>
<p>Note that if you paint with circle (2D) brush on oblique slices or if the slice view is positioned at segment boundaries then you may see striping artifacts. These artifacts should disappear as you complete your segmentation.</p>
<p>To avoid seeing these temporary artifacts, you may create a transformed - and potentially resampled - copy of your volume using Crop volume module (resampling mode enabled, clipping ROI transformed by ACPC transform) and use that as master volume for segmentation. When you completed the segmentation, you may export segments to a using your original volume as reference. Let me know if anything is unclear or you cannot achieve what you would like to do.</p>

---

## Post #3 by @Andras_Jakab (2017-11-03 08:21 UTC)

<p>Thanks a lot Andras<br>
I would like to reformulate my question.<br>
We are developing an extension to Slicer, and I would like to ask if someone could suggest a solution to lock the view to be parallel to the AC-PC plane (after the user defines the two points) with “one button”, without the user having to go through the ac-pc transformation module and the view reformat thing manually.</p>

---

## Post #4 by @lassoan (2017-11-03 16:05 UTC)

<p>If you don’t want to do any programming, then use <code>Volume Reslice Driver</code> module (available in SlicerIGT extension) to align your slice views using the computed AC-PC transform (you probably have to invert the transform in Transforms module, as you apply it to the slice views and not to the volume).</p>
<p>If you have your own module already, then you can set the slice view orientations directly as described here: <a href="https://discourse.slicer.org/t/rotating-slice-around-axis-of-model/916/2">Rotating Slice around Axis of Model</a> (using <code>SetSliceToRASByNTP</code> or <code>SetSliceToRAS</code> method).</p>

---
