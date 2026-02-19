---
topic_id: 35854
title: "A Few Parametric Shapes Controlled By Markups Points"
date: 2024-05-01
url: https://discourse.slicer.org/t/35854
---

# A few parametric shapes controlled by markups points

**Topic ID**: 35854
**Date**: 2024-05-01
**URL**: https://discourse.slicer.org/t/a-few-parametric-shapes-controlled-by-markups-points/35854

---

## Post #1 by @chir.set (2024-05-01 14:11 UTC)

<p>Hello,</p>
<p>I have pushed this <a href="https://github.com/chir-set/SlicerExtraMarkups/tree/ParametricFunctions/Shape/" rel="noopener nofollow ugc">branch</a> in the ExtraMarkups extension. It offers a few parametric shapes that are controlled by 4 markups control points. More parameters are controlled in the module’s widget. They are all vtkParametricFunction derived objects that are already in the VTK library.</p>
<p>I do not intend to merge it in ExtraMarkups’ main branch right away, since this extension is a dependency of SlicerVMTK. The update is relatively big and may hide trouble. It could be merged if it is considered a value-added update by Slicer core developers. People who build Slicer may evaluate this branch any time.</p>
<p>I admit that it’s hard to find a real-world useful application right now. Anyway, it’s there for any purpose.</p>
<p>Thanks for any input and regards.</p>

---
