---
topic_id: 42538
title: "Imported Segmentation Does Not Show On Dicom File Image"
date: 2025-04-11
url: https://discourse.slicer.org/t/42538
---

# Imported segmentation does not show on DICOM file image

**Topic ID**: 42538
**Date**: 2025-04-11
**URL**: https://discourse.slicer.org/t/imported-segmentation-does-not-show-on-dicom-file-image/42538

---

## Post #1 by @maysan1 (2025-04-11 17:20 UTC)

<p>Hello, I am using Slicer 5.9.0.<br>
I have created a segmentation on one dicom file of a certain volume. Then saved it as a seg.nrrd file. I am now trying to import it to another dicom file of another volume. It can be imported but does not show up on the image…<br>
I have tried to align the volume of the files by changing “image spacing” and “image origin” under “volumes”. This does not help.</p>
<p>How do I proceed?</p>

---

## Post #2 by @cpinter (2025-04-15 14:33 UTC)

<p>It is probably not enough to change the origin and spacing to register the segmentation to the new slice. Typically for registration we create a transform as parent of the object we need to align with the new data, and change the transform. You provided very little detail, but based on what I understand what I’d do is first to visualize both the new slice and the segmentation in 3D, and see the relationship between the two. Maybe before I delve into more assumptions you could do this and post a screenshot?</p>

---
