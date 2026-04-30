---
topic_id: 46870
title: "Monai 3Dseg Brain Glioma Segmentation Error"
date: 2026-04-29
url: https://discourse.slicer.org/t/46870
---

# MONAI 3DSeg - Brain Glioma segmentation error

**Topic ID**: 46870
**Date**: 2026-04-29
**URL**: https://discourse.slicer.org/t/monai-3dseg-brain-glioma-segmentation-error/46870

---

## Post #1 by @Samim_Zaheer (2026-04-29 15:46 UTC)

<p>Operating system: macOS<br>
Slicer version: 5.10.0<br>
Expected behavior: Glioma Segmentation<br>
Actual behavior: RuntimeError: affine matrix of all images should be the same for channel-wise concatenation.</p>

---

## Post #2 by @Samim_Zaheer (2026-04-29 17:09 UTC)

<p>Hi,<br>
I am trying the glioma segmentation with MONAI Auto3D seg, but it is giving an error as below. I couldn’t figure out the problem.</p>
<p>RuntimeError: affine matrix of all images should be the same for channel-wise concatenation. Got [[ 9.74883212e-01 6.86834358e-02 2.28715149e-01 -1.05612617e+02]</p>
<p>aise RuntimeError(f"applying transform {transform}") from e</p>
<p>RuntimeError: applying transform</p>
<p>Processing failed with error code [1].</p>

---
