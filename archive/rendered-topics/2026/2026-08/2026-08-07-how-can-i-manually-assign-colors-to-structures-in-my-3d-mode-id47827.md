---
topic_id: 47827
title: "How can I manually assign colors to structures in my 3D Model?"
date: 2026-08-07
url: https://discourse.slicer.org/t/47827
last_bumped: 2026-08-10T09:53:32.119Z
---

# How can I manually assign colors to structures in my 3D Model?

**Topic ID**: 47827
**Date**: 2026-08-07
**URL**: https://discourse.slicer.org/t/how-can-i-manually-assign-colors-to-structures-in-my-3d-model/47827

---

## Post #1 by @Nonso (2026-08-07 14:38 UTC)

<p>Operating system: Windows 11 Pro<br>
Slicer version: 5.10.0<br>
Expected behavior:<br>
Actual behavior: I imported a segmented model in .nrrd format, from MIB. After creating a model in 3D Slicer, using the model maker, most of the structures of interest were red in color (automatically assigned). This makes it difficult to comprehend the structures of interest. Is there any way I can manually assign colors to the structures in the 3D model?</p>

---

## Post #2 by @viktoriyanavrotskaya (2026-08-10 09:53 UTC)

<p>Yeah, this usually happens because Model Maker keyed the colors off label values that mostly collapsed to one. Easiest fix: go to the Models module, select each model node in the list, and change the color under Display. You can set each structure individually there. If they’re all merged into one model, you may need to re-run Model Maker with a proper color table so each label gets its own color.</p>

---
