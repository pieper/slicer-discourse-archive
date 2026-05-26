---
topic_id: 46438
title: "How to handle 3D model that was given to me in DICOM format"
date: 2026-03-12
url: https://discourse.slicer.org/t/46438
last_bumped: 2026-03-17T20:03:25.505Z
---

# How to handle 3D model that was given to me in DICOM format

**Topic ID**: 46438
**Date**: 2026-03-12
**URL**: https://discourse.slicer.org/t/how-to-handle-3d-model-that-was-given-to-me-in-dicom-format/46438

---

## Post #1 by @madsmess (2026-03-12 00:25 UTC)

<p>Hi! I was recently given a 3D model from a cardiologist, but it was given to me as a DICOM file. How could I convert/export this model as an STL or other similar format (OBJ, etc.)? I can view it in slicer, although the view is a bit wonky. I didn’t know 3D models could even be saved in DICOM format, and every time I search to find a solution, the only results I get are if you start from images (CT, etc.) then create the model from that. I only have the 3D model, and not the scans that this model was created from. Any advice is appreciated!</p>

---

## Post #2 by @pieper (2026-03-12 12:16 UTC)

<p>Maybe you can add a screenshot to help us understand what you are seeing.</p>

---

## Post #3 by @mikebind (2026-03-17 20:03 UTC)

<p>Sometimes what is saved to DICOM is essentially a series of screenshots of a model and not actually the data needed to reconstruct the model itself. In this case, it is typically not really feasible to get the STL (building it would be a reconstruction problem rather than a loading problem).</p>

---
