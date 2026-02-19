---
topic_id: 37177
title: "Exporting Only Coronal Slices To Dicom"
date: 2024-07-03
url: https://discourse.slicer.org/t/37177
---

# Exporting only coronal slices to DICOM?

**Topic ID**: 37177
**Date**: 2024-07-03
**URL**: https://discourse.slicer.org/t/exporting-only-coronal-slices-to-dicom/37177

---

## Post #1 by @hannaho (2024-07-03 14:17 UTC)

<p>Hi all,</p>
<p>I have produced some fused image volumes I would like to share with my colleagues who don’t have Slicer and need them as DICOM files. I’ve been able to export them ok, except for some reason they only see the axial slices when they open the file. We actually only care about coronal slices.</p>
<p>Is there a way I can change the volume into just a series of coronal slices and export that as DICOM?</p>
<p>Thanks!</p>

---

## Post #2 by @pieper (2024-07-03 14:21 UTC)

<p>This module should work for that: <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/orientscalarvolume.html" class="inline-onebox">Orient Scalar Volume — 3D Slicer documentation</a></p>

---
