---
topic_id: 25438
title: "3D Measurements Of Abdominal Aortic Aneurysms Workflow"
date: 2022-09-26
url: https://discourse.slicer.org/t/25438
---

# 3D measurements of abdominal aortic aneurysms workflow

**Topic ID**: 25438
**Date**: 2022-09-26
**URL**: https://discourse.slicer.org/t/3d-measurements-of-abdominal-aortic-aneurysms-workflow/25438

---

## Post #1 by @pablomartin (2022-09-26 15:42 UTC)

<p>Hello all, I am new to slicer community. I need to process and perform measurements on a set of DICOM CTs of patients with AAAs. What would be the recommended workflow and tips? Currently I am manually segmenting using grow from seeds, extracting the centerline with vmtk module and then performing cross section analysis.<br>
Many thanks in advance!</p>

---

## Post #2 by @pieper (2022-09-26 16:09 UTC)

<p>I would say that’s a pretty good workflow.  I don’t know of anything more automated than that, although once you have a good dataset of segmentations you might consider training a MONAI Label model.  It would be helpful if you also included thrombus and calcifications.</p>

---
