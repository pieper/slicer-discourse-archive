---
topic_id: 23647
title: "Non Linear Transforms Not Supported For Volume Rendering"
date: 2022-05-30
url: https://discourse.slicer.org/t/23647
---

# Non-linear transforms not supported for volume rendering?

**Topic ID**: 23647
**Date**: 2022-05-30
**URL**: https://discourse.slicer.org/t/non-linear-transforms-not-supported-for-volume-rendering/23647

---

## Post #1 by @muratmaga (2022-05-30 21:49 UTC)

<p>I am using the Fiducial Registration Wizard to make a visual. When I choose the resultant transform as warping and set  to store in a transform (not linear transform), I am getting this error when I try to apply this transform to a volume rendering node.</p>
<pre><code class="lang-auto">Failed to get transformation matrix because transform is not linear

Generic Warning: In /work/Stable/Slicer-0/Libs/MRML/Core/vtkMRMLTransformNode.cxx, line 929
vtkMRMLTransformNode::GetMatrixTransformBetweenNodes failed: expected linear transforms between nodes

Warning: In /work/Stable/Slicer-0/Modules/Loadable/VolumeRendering/MRMLDM/vtkMRMLVolumeRenderingDisplayableManager.cxx, line 754
vtkMRMLVolumeRenderingDisplayableManager (0x68fcd60): GetVolumeTransformToWorld: Non-linear parent transform found for volume node MRHead
</code></pre>
<p>This used to work, but I think there was a different transform type (maybe a grid, or a displacement field as output).</p>

---

## Post #2 by @pieper (2022-05-30 21:55 UTC)

<p>I don’t believe that nonlinear transforms have ever been supported in the volume rendering.  You can harden the volume first though.</p>

---

## Post #3 by @muratmaga (2022-05-31 00:38 UTC)

<p>Thanks. Perhaps I misremember. Probably hardened them…</p>

---
