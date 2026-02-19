---
topic_id: 30915
title: "Dynamic Modeler Plane Cut Type Affecting Number Of Points In"
date: 2023-08-01
url: https://discourse.slicer.org/t/30915
---

# Dynamic modeler plane cut type affecting number of points in output models

**Topic ID**: 30915
**Date**: 2023-08-01
**URL**: https://discourse.slicer.org/t/dynamic-modeler-plane-cut-type-affecting-number-of-points-in-output-models/30915

---

## Post #1 by @Jeff_Zeyl (2023-08-01 18:45 UTC)

<p>In the plane cut option in Dynamic Modeler module, I found that if two models are chosen in the output nodes simultaneously, the number of points is identical between the two output models when inspected (Slicer 5.2.2 on Windows). The models show a difference in surface area, volume, and number of cells but not number of points. In the 3D view they also look fine.</p>
<p>If, instead, the same result is achieved in a two-step process (i.e. leaving one of the output models as None for one of the positive and negative components), the new models have different number of points, similar to the other model properties.</p>
<p>I’m later calculating thickness from the cut pieces, and the identical number of points becomes problematic with the simultaneous option. The second way is a workaround but just reporting in case this is a bug.</p>

---

## Post #2 by @Sunderlandkyl (2023-08-01 20:15 UTC)

<p>It looks like the unused points from the original surface aren’t being removed from the cut output.<br>
I’ll take a look at it.</p>

---

## Post #3 by @lassoan (2023-08-02 04:17 UTC)

<p>Keeping unused points in the output is useful because it allows you to keep referring to the same point by the same ID after cutting. You can remove unused points anytime using Surface Toolbox “Clean” operation (or using vtkCleanPolyData filter).</p>
<p>If you can demonstrate unused points cause problems then we could remove the unused points automatically (you could then add a pedigree point ID array to preserve original point IDs), but if it does not actually cause you problems then it may be better to preserve the current behavior.</p>

---
