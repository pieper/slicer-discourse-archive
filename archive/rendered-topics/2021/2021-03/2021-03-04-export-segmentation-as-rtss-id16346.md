---
topic_id: 16346
title: "Export Segmentation As Rtss"
date: 2021-03-04
url: https://discourse.slicer.org/t/16346
---

# Export segmentation as RTSS

**Topic ID**: 16346
**Date**: 2021-03-04
**URL**: https://discourse.slicer.org/t/export-segmentation-as-rtss/16346

---

## Post #1 by @CELESTE_ADRAGNA (2021-03-04 01:30 UTC)

<p>Operating system: windows 64bit<br>
Slicer version: 4.9<br>
Expected behavior: export segmentation as RT structure into treatmet planning system (TPS) Eclipse<br>
Actual behavior: error in TPS import</p>
<p>Hi, i’m trying to use slicer to do segmentations on MRI images in order to load these into TPS. RT extension is installed and I’m able to export as RT structure set, but when I import the files into the TPS there’s an error and only the MRI images are loaded but the RTSS fails (the log report says “could not convert DICOM stream SOP instance UID [1.2.826…]”). I’ve also tryed to export a RTSS from the TPS and then edit it on Slicer, but i get similar errors when attempting to import the files back to the TPS). Any thoughts?</p>

---

## Post #2 by @lassoan (2021-03-04 01:54 UTC)

<p>Please switch to the latest Slicer Stable Release and let us know if the problem is still there.</p>

---

## Post #3 by @CELESTE_ADRAGNA (2021-03-10 00:56 UTC)

<p>Hi, thank you for your quick response, but I tried installing the latest stable version and still get errors when trying to import RTSS into eclipse</p>

---

## Post #4 by @lassoan (2021-03-24 16:05 UTC)

<p>There have been some fixes in Plastimatch that I think reached SlicerRT in latest Preview Release. If you still have issues then please compare the output of dcmdump utility on the RTSS created by Slicer and another one that Eclipse can read and tell us what you find.</p>

---
