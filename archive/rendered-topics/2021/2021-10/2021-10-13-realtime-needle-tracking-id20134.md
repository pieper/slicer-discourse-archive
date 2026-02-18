# Realtime needle tracking

**Topic ID**: 20134
**Date**: 2021-10-13
**URL**: https://discourse.slicer.org/t/realtime-needle-tracking/20134

---

## Post #1 by @riep (2021-10-13 13:22 UTC)

<p>Hi everyone,<br>
We are looking for an application that could use as input a 3D MRI volume and output the location of a needle/probe in the volume. Basically, the algorithm would be looking for straight dark regions in the image. Does someone have already attempted to do that in slicer?</p>
<p>Cheers,<br>
Pierre</p>

---

## Post #2 by @lassoan (2021-10-13 18:50 UTC)

<p>A good number of MRI-guided needle insertion projects in Slicer used some form of needle detection or tracking (<a href="https://www.slicer.org/wiki/Modules:ProstateNav-Documentation-3.4">ProstateNav</a>, <a href="https://github.com/SlicerProstate/SliceTracker">SlicerProstate</a>, <a href="https://github.com/gpernelle/iGyne">iGyne</a>, <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/NeedleFinder">NeedleFinder</a>, <a href="https://github.com/SlicerIGT/SlicerPathReconstruction">PathReconstruction</a>, etc.).</p>
<p>Since MRI acquisition is usually quite slow (need about a minute to get a new 3D volume), and needles are straight, most project went with manual definition of the needle (dropping a fiducial at the tip and a second point along the needle). I think the only exception was the tracking of flexible needles for HDR brachytherapy, because there are many needles to extract at once, so if you are interested in automated detection then check out iGyne and NeedleFinder.</p>
<p>Active tracking has been used in MRI as well (using small receiver coils), but it requires some hardware engineering and it require low-level integration with the MRI scanner. Optical tracking and encoders on a needle guide can also be used but they may be inaccurate due to needle bending.</p>
<p>What is your clinical procedure (biopsy/brachytherapy, prostate/breast/cervix/brain, …) and what is the specific task you are trying to solve (needle position confirmation after placement, real-time visual servoing with MRI scan plane control, …)? What positioning device do you use and how do you register it to the patient?</p>

---

## Post #3 by @riep (2021-10-15 15:35 UTC)

<p>Hi Andreas,<br>
This is already very, very useful.  iGyne and NeedleFinder are probably what we are looking for.<br>
Do give you an overview on the application we have:<br>
We have a 3D scan of the liver performed under breathold where a needle is inserted. I will give feedback in this thread once we have tested those algorithms.<br>
Pierre</p>

---
