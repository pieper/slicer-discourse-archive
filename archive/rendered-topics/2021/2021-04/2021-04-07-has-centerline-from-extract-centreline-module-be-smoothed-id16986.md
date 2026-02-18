# Has Centerline from Extract centreline module be smoothed?

**Topic ID**: 16986
**Date**: 2021-04-07
**URL**: https://discourse.slicer.org/t/has-centerline-from-extract-centreline-module-be-smoothed/16986

---

## Post #1 by @Ge_Tang (2021-04-07 16:26 UTC)

<p>I want to do the geometric analysis. The VMTK tutorial described that the centerline goes through a Laplacian smoothing filter first and then computes the derivatives and the related quantities (<a href="http://www.vmtk.org/tutorials/GeometricAnalysis.html" class="inline-onebox" rel="noopener nofollow ugc">Geometric Analysis | vmtk - the Vascular Modelling Toolkit</a>). I did not found the smoothing in the ExtractCenterline.py (<a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/ExtractCenterline/ExtractCenterline.py" class="inline-onebox" rel="noopener nofollow ugc">SlicerExtension-VMTK/ExtractCenterline.py at master · vmtk/SlicerExtension-VMTK · GitHub</a>)<br>
I am not sure if I understand the code well. Could you give me some advice?<br>
Thank you so much!<br>
Ge Tang</p>

---

## Post #2 by @lassoan (2021-04-14 05:28 UTC)

<p>It is not smoothed. You can smooth the centerline by getting it as a curve node from Extract centerline, then use Markups module / Resample.</p>

---
