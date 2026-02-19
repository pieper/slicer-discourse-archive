---
topic_id: 43646
title: "Difficulty Registering Pre And Post Surgery Cbct Datasets Wi"
date: 2025-07-08
url: https://discourse.slicer.org/t/43646
---

# Difficulty Registering Pre- and Post-Surgery CBCT Datasets without Fiducials

**Topic ID**: 43646
**Date**: 2025-07-08
**URL**: https://discourse.slicer.org/t/difficulty-registering-pre-and-post-surgery-cbct-datasets-without-fiducials/43646

---

## Post #1 by @A_C (2025-07-08 12:45 UTC)

<p>Hi all,</p>
<p>I’m currently working on a project involving two DICOM datasets acquired via CBCT (cone-beam CT). The first dataset was taken before a surgical procedure, and the second one after a tooth extraction. Unfortunately, I don’t have any external fiducial markers in the images, so I’m using IGT Wizard Registration based on anatomical landmarks.</p>
<p>Despite using a relatively high number of fiducial points (10), it seems very difficult to achieve a good overlap between the two scans. The registration always appears slightly off.</p>
<p>Could the issue be related to the inherent limitations of CBCT, such as reduced accuracy or image quality in the peripheral regions? Or is there something else I might be missing?</p>
<p>Any suggestions or shared experiences would be greatly appreciated!</p>
<p>Thanks in advance,<br>
Anna</p>

---

## Post #2 by @pieper (2025-07-08 21:32 UTC)

<p>Did you try just the regular registration flow with General Registration?  There is pre-post CBCT in the SampleData you can test with.  You may need to mask out the moving parts (neck/jaw).</p>

---
