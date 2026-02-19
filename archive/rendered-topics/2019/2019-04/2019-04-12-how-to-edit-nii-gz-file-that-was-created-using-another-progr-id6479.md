---
topic_id: 6479
title: "How To Edit Nii Gz File That Was Created Using Another Progr"
date: 2019-04-12
url: https://discourse.slicer.org/t/6479
---

# How to edit nii.gz file that was created using another program?

**Topic ID**: 6479
**Date**: 2019-04-12
**URL**: https://discourse.slicer.org/t/how-to-edit-nii-gz-file-that-was-created-using-another-program/6479

---

## Post #1 by @Rohan_Bhat (2019-04-12 05:08 UTC)

<p>Hi i followed these steps from a previous post.</p>
<p>Load the DICOM volume using Slicer’s DICOM module. Load the nii.gz file using Add data function - and in the Add data dialog, click Show Options, scroll to the right, and make sure that LabelMap checkbox is selected.</p>
<p>But i am having difficulties with viewing the segmentation and editing it. Currently the segmentation is of the heart and arteries, but i want to just have the coronary arteries. How would i go about doing this.</p>
<p>Thanks</p>

---

## Post #2 by @muratmaga (2019-04-12 14:21 UTC)

<p>There are few more steps involved. You need to convert your labelmap to a segmentation structure so that you can start using the Segment Editor. To do that, go to Segmentations module and find the import labelmaps option.<br>
After that you can switch to Segment Editor and delete (or hide) the segmentation you don’t want.</p>

---

## Post #3 by @Rohan_Bhat (2019-04-13 00:43 UTC)

<p>Thanks, I got it working now.</p>

---
