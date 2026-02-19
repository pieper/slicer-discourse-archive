---
topic_id: 29317
title: "Calculate The Volume Of Cerebrospinal Fluid And The Volume O"
date: 2023-05-06
url: https://discourse.slicer.org/t/29317
---

#  calculate the volume of cerebrospinal fluid and the volume of intracranial hemorrhage

**Topic ID**: 29317
**Date**: 2023-05-06
**URL**: https://discourse.slicer.org/t/calculate-the-volume-of-cerebrospinal-fluid-and-the-volume-of-intracranial-hemorrhage/29317

---

## Post #1 by @duan (2023-05-06 14:23 UTC)

<p>Excuse me, Can you help me？I have some questions.Can 3Dslicer calculate the volume of cerebrospinal fluid and the volume of intracranial hemorrhage? If it can be calculated, which section of 3Dslicer needs to be used? I am currently using is threshold segmentation to calculate them. Is the segmentation of cerebrospinal fluid or cerebral hemorrhage lesions obtained by inputting the window width range of cerebrospinal fluid or cerebral hemorrhage lesions within the threshold range accurate?</p>

---

## Post #2 by @pieper (2023-05-06 14:43 UTC)

<p>Based on this image in <a href="https://discourse.slicer.org/t/threshold-in-the-segment-editor/29316/2">your other post</a>, it seems you are using scans of a printed film, so probably the image data is not calibrated.  You may be able to get a rough idea of the size based on appearance of the various tissue types.  Be sure to confirm that the sizes of the voxels have been accounted for when calculating the volume (e.g. you should know the spacing between the slices, perhaps by looking at the text annotations, and you can adjust for the pixel spacing by measuring a known distance in the slice plane, such as a ruler printed on the film).</p>

---
