# Gaussian surface method

**Topic ID**: 27099
**Date**: 2023-01-07
**URL**: https://discourse.slicer.org/t/gaussian-surface-method/27099

---

## Post #1 by @akmal871026 (2023-01-07 15:55 UTC)

<p>Dear all,</p>
<p>Does anyone know, is a method of segmentation using the Fourier surface method in 3D Slicer?</p>
<p>That method mention in this paper, on page 3. DOI: 10.1186/s13550-017-0262-7</p>

---

## Post #2 by @lassoan (2023-01-08 04:00 UTC)

<p>Fitting a parametric surface, and specifically Fourier surface fitting, for smoothing a segmentation is one option, but there are many others. The authors of the paper don’t explain why they chose Fourier surface fitting and did not compare it to other methods, so the choice seems quite arbitrary. Unless this method is very widely used in your field, I would recommend to try other methods that are already available in Slicer and see if they work well enough for you.</p>
<p>A few segment smoothing methods available in Segment Editor’s Smoothing effect.</p>
<p>If you want to do smoothing based on parametric surface fitting then you may try spherical harmonics as it is already available in <a href="https://salt.slicer.org/">SlicerSALT extension</a>.</p>
<p><a class="mention" href="/u/bpaniagua">@bpaniagua</a> <a class="mention" href="/u/muratmaga">@muratmaga</a> do you have any other suggestions?</p>

---
