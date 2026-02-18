# Procrustes alignment 

**Topic ID**: 3144
**Date**: 2018-06-12
**URL**: https://discourse.slicer.org/t/procrustes-alignment/3144

---

## Post #1 by @Pugliese (2018-06-12 04:29 UTC)

<p>Hi, Beatriz and Martin</p>
<p>I was following the tutorial, and I noticed that the rigid-body Procrustes alignment (only translation and/or a rotation) can be used.</p>
<p>I was just wondering how the size would be removed (rescaling step) for a pure shape analysis.</p>
<p>Thanks for the great and very useful tool.</p>

---

## Post #2 by @styner (2018-06-13 14:07 UTC)

<p>Hi Fernando<br>
The SlicerSALT toolkit currently does not allow for “pure” shape analysis, or size-free shape analysis. This based on the main driver for SlicerSALT being biomedical applications, where size-free shape would be extremly hard to interprete. In the code, the procrustes scale normalization is actually being computed, it’s just not applied. As a workaround, you could edit the code yourself and recompile (this is not optimal, I understand).</p>
<p>Martin</p>

---

## Post #3 by @Pugliese (2018-07-08 03:02 UTC)

<p>Thank you very much for the feedback.</p>

---
