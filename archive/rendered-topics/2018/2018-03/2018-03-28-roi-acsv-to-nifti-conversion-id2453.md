---
topic_id: 2453
title: "Roi Acsv To Nifti Conversion"
date: 2018-03-28
url: https://discourse.slicer.org/t/2453
---

# ROI (.acsv) to nifti conversion

**Topic ID**: 2453
**Date**: 2018-03-28
**URL**: https://discourse.slicer.org/t/roi-acsv-to-nifti-conversion/2453

---

## Post #1 by @Vinny (2018-03-28 11:06 UTC)

<p>Hello 3d Slicer forum,</p>
<p>I created a cubic ROI on a T1 image.  It saves as an annotated .csv file, but I’d like to save the cubic ROI in NIFTI format.  Would I have to to plot the cube coordinates using VTK?  Or is there any easier way to do this?</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2018-03-28 11:33 UTC)

<p>You can use Volume Clip extension to create a labelmap volume from an ROI node.</p>
<p>You can also use Segment Editor module’s Scissors effect to quickly create rectangular ROI (Fill inside on one slice, Erase outside on an orthogonal slice) that you can export to a labelmap node.</p>

---
