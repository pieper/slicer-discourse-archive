---
topic_id: 2525
title: "Performing Tractography With Multiple Rois"
date: 2018-04-05
url: https://discourse.slicer.org/t/2525
---

# Performing tractography with multiple ROIs

**Topic ID**: 2525
**Date**: 2018-04-05
**URL**: https://discourse.slicer.org/t/performing-tractography-with-multiple-rois/2525

---

## Post #1 by @lsmith (2018-04-05 21:35 UTC)

<p>Hi! I’m an RA and quite new to 3D slicer. My lab is working on using DTI data to map motor pathways in the brain. We are wanting to define regions of interest in the motor cortex and the brainstem and see the fibers that pass through both ROIs. I’ve figured out how to track the fiber tracts separately, but when I’ve tried defining multiple ROIs through the segment editor and tracking the fibers, we get the feeling the fibers are passing through ROI 1 OR ROI 2 rather than ROI 1 AND ROI 2. As of right now, I’ve been primarily using the segment editor and tractography seeding, and occasionally have used the ROI fiber selection for outliers. If you have any tips/a better way to go about this process, I would appreciate any help! Thank you!</p>

---

## Post #2 by @timeanddoctor (2018-04-06 11:26 UTC)

<p>you can use segment 1 and segment 2, and segment 1 union segment2.(mask)</p>

---

## Post #3 by @lsmith (2018-04-06 13:34 UTC)

<p>Good to know. Sorry, but where are these options located?</p>

---

## Post #4 by @ihnorton (2018-04-10 18:28 UTC)

<p>Hi <a class="mention" href="/u/lsmith">@lsmith</a>, after seeding, you can use the “Tractography ROI Selection” module to do inclusion/exclusion operations based on several ROIs. Please see <a href="http://dmri.slicer.org/tutorials/Slicer-4.8/FiberBundleSelectionAndScalarMeasurement.pdf">this tutorial</a>. Hope that helps!</p>

---
