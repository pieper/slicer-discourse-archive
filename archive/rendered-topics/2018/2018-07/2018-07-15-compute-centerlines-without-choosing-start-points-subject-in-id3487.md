# Compute centerlines without choosing start points (subject independent)?

**Topic ID**: 3487
**Date**: 2018-07-15
**URL**: https://discourse.slicer.org/t/compute-centerlines-without-choosing-start-points-subject-independent/3487

---

## Post #1 by @shahrokh (2018-07-15 11:46 UTC)

<p>Hi Slicer Developers</p>
<p>I was able to extract the sections of rods installed in a phantom in MRI images using “Segment Editor” module and “Thresholds” effect.<br>
Its output can be of type “Model”. At now, I want to extract centerlines of these rods using “ Centerline Computation” module. It seems for using this module, I MUST define fiducials as the origins of these centerlines in this module.<br>
The number of these rods is high and doing it depends on the person (subject dependent) and time-consuming. I want to do it without choosing start points as origins. How can I do it?</p>
<p>Please guide me.<br>
Shahrokh.</p>

---

## Post #2 by @lassoan (2018-07-15 14:20 UTC)

<p>VMTK extension’s centerline computation module requires only one root point as input and it returns all centerline endpoints as output.</p>

---

## Post #3 by @lassoan (2018-07-15 15:56 UTC)

<p>There is also a fully automatic MRI phantom registration method (that computes position and orientation of a phantom consisting of sticks fiducials) available in ProstateTracker extension - <a href="https://github.com/SlicerProstate/SliceTracker/blob/master/README.md">https://github.com/SlicerProstate/SliceTracker/blob/master/README.md</a></p>
<p>What is the clinical problem that you are aiming to solve? What organ, disease, imaging modality, and treatment method? We may be able to point you to complete solutions that you can use as is, or adapt to your specific needs.</p>

---

## Post #4 by @lassoan (2021-03-08 20:20 UTC)

<p>2 posts were split to a new topic: <a href="/t/automatic-vessel-endpoints-detection/16435">Automatic vessel endpoints detection</a></p>

---
