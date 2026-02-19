---
topic_id: 17938
title: "Can I Update The Contours On A Dicom Structure File"
date: 2021-06-03
url: https://discourse.slicer.org/t/17938
---

# Can I update the contours on a DICOM structure file?

**Topic ID**: 17938
**Date**: 2021-06-03
**URL**: https://discourse.slicer.org/t/can-i-update-the-contours-on-a-dicom-structure-file/17938

---

## Post #1 by @Kayla (2021-06-03 19:04 UTC)

<p>Hi everyone, I am new to this software and I am wondering if I can achieve the following:</p>
<p>I’ve loaded a DICOM structure file (made in Python) with their respective CT images of a phantom into 3D slicer using SlicerRT extension. Some of the contours I made need adjusting and I’m wondering if 3D slicer can overwrite the new segmentations over the old triplet coordinates in the DICOM RT structure file?</p>
<p>Thank you in advance.</p>

---

## Post #2 by @lassoan (2021-06-03 19:33 UTC)

<p>Yes, sure this should be no problem at all. This is why DICOM RTSTRUCT import/export features in SlicerRT extension and the Segment Editor module were developed for.</p>

---

## Post #3 by @Kayla (2021-06-03 23:11 UTC)

<p>Thanks for your reply. That’s brilliant. I right clicked “Export to DICOM” in the study module, clicked RT as type and exported. It did the trick <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---
