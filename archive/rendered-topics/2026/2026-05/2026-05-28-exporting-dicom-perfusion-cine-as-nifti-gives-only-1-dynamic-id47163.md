---
topic_id: 47163
title: "Exporting DICOM perfusion/cine as NIfTI gives only 1 dynamic (but Slicer shows 150 frames)"
date: 2026-05-28
url: https://discourse.slicer.org/t/47163
last_bumped: 2026-05-28T19:37:10.090Z
---

# Exporting DICOM perfusion/cine as NIfTI gives only 1 dynamic (but Slicer shows 150 frames)

**Topic ID**: 47163
**Date**: 2026-05-28
**URL**: https://discourse.slicer.org/t/exporting-dicom-perfusion-cine-as-nifti-gives-only-1-dynamic-but-slicer-shows-150-frames/47163

---

## Post #1 by @Demy (2026-05-28 19:37 UTC)

<p>Hi everyone,<br>
I am loading a DICOM perfusion/cine MRI dataset into 3D Slicer.<br>
In the DICOM browser, the series summary shows:</p>
<ul>
<li>
<p><strong>Modality:</strong> MR</p>
</li>
<li>
<p><strong>Size:</strong> 180 × 208</p>
</li>
<li>
<p><strong>Count:</strong> 150 frames</p>
</li>
</ul>
<p>So Slicer correctly detects that this is a <strong>150‑frame multivolume</strong>.</p>
<p>When I load the data, I can scroll through all 150 frames. However, when I try to export the dataset as NIfTI, Slicer only saves <strong>one dynamic</strong>.  The resulting NIfTI has the following shape: [180, 208, 1].</p>

---
