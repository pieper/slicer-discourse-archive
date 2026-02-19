---
topic_id: 8624
title: "Easiest Method Of 3D Modeling Of A Sacrum"
date: 2019-09-30
url: https://discourse.slicer.org/t/8624
---

# Easiest method of 3D modeling of a sacrum

**Topic ID**: 8624
**Date**: 2019-09-30
**URL**: https://discourse.slicer.org/t/easiest-method-of-3d-modeling-of-a-sacrum/8624

---

## Post #1 by @mccarthyvetsurg (2019-09-30 13:57 UTC)

<p>Hello Slicer community!</p>
<p>I am new to slicer and have been trying to isolate a sacrum from the rest of the pelvis and surrounding lumbar vertebra.  Is there a better way to select the individual bone without including the pelvis and other soft tissues?  Is it better to create the segmentation based off the ROI around the region of interest or to use the threshold method and scissor the region out?</p>
<p>I understand about creating a threshold to isolate the bone and to use scissors to cut away excess pelvis, soft tissue, etc., however, we need the selected image to be filled all of the way with the segmentation.</p>
<p>Currently the process is that we cut out the sacrum using the scissors tool and go slice by slice to either paint or trace to fill in the bone to create a solid sacrum in the coronoal, sagital and axial views of the CT scan.  As you can imagine, this is extremely time consuming.</p>
<p>The utilization of this is to be able to visualize the internal bone sacral anatomy and if the medullary region (inner portion of the bone) is not selected, the 3d model is very sloppy internally with our modelling software.</p>

---

## Post #2 by @lassoan (2019-10-02 01:54 UTC)

<p>There are definitely much easier ways to do this segmentation. Tips in this recent discussion should help: <a href="https://discourse.slicer.org/t/detailed-threshold-and-smoothing-documentation/8602" class="inline-onebox">detailed threshold and smoothing documentation</a></p>
<p>You can also learn a lot of tricks from <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Segmentation" rel="nofollow noopener">segmentation tutorials and recipes</a>.</p>

---
