---
topic_id: 308
title: "Patient Position"
date: 2017-05-14
url: https://discourse.slicer.org/t/308
---

# Patient position

**Topic ID**: 308
**Date**: 2017-05-14
**URL**: https://discourse.slicer.org/t/patient-position/308

---

## Post #1 by @djalil92 (2017-05-14 11:15 UTC)

<p>Hi everyone hope you are fine, i have got a problem with patient position of my CBCT which is in fact FFP for first feet prone but when i tried to do a segmentation of the trachea and save this into dicom with the module create a dicom series i got HFS head first supine in stead of FFP what can i do to fix that? thanks in advance.</p>

---

## Post #2 by @lassoan (2017-05-21 17:55 UTC)

<p>Rotate your volume to the correct orientation using Transforms module. When you are done, don’t forget to “harden” the transform on the volume.</p>

---
