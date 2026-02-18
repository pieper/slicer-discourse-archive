# How the tensor is stored in NRRD

**Topic ID**: 34084
**Date**: 2024-02-01
**URL**: https://discourse.slicer.org/t/how-the-tensor-is-stored-in-nrrd/34084

---

## Post #1 by @Yixun_Liu (2024-02-01 12:03 UTC)

<p>Hi,<br>
I use the 3DSlicer Diffusion module to load DWI, estimate its tensor and then store the tensor image into NRRD. I want to know how the tensor is stored in NRRD?<br>
Is it stored as 6 upper triangle elements of the 3x3 tensor matrix or the lower triangle or others?<br>
I also want to know which VTK class can be used to correctly load the tensor image?</p>
<p>Thanks.<br>
Yixun</p>

---

## Post #2 by @pieper (2024-02-01 15:36 UTC)

<p><a href="https://teem.sourceforge.net/nrrd/format.html" class="onebox" target="_blank" rel="noopener">https://teem.sourceforge.net/nrrd/format.html</a></p>

---

## Post #3 by @Yixun_Liu (2024-02-06 04:30 UTC)

<p>Thank you very much！</p>

---
