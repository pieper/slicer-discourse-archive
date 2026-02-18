# Segmentation is very pixelated.

**Topic ID**: 29019
**Date**: 2023-04-20
**URL**: https://discourse.slicer.org/t/segmentation-is-very-pixelated/29019

---

## Post #1 by @Muggs (2023-04-20 03:50 UTC)

<p>Hello All,</p>
<p>VERY new to this. My segments are really pixelated, like LEGO’s.</p>
<p>Anyway to reduce the palatalization when creating segments for STL export?</p>
<p>Muggs</p>

---

## Post #2 by @lassoan (2023-04-20 03:54 UTC)

<p>Most probably your input volume was very anisotropic that you can fix by cropping and resampling the volume to be isotropic using Crop volume module. You can find more detailed explanation and more instructions in the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#generated-surface-contains-step-artifacts">segmentation FAQ in the Slicer documentation</a>.</p>

---
