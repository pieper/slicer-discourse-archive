---
topic_id: 47607
title: "Extract slice view rotations? (For applying to crop volume ROI)"
date: 2026-07-13
url: https://discourse.slicer.org/t/47607
last_bumped: 2026-07-13T17:01:21.446Z
---

# Extract slice view rotations? (For applying to crop volume ROI)

**Topic ID**: 47607
**Date**: 2026-07-13
**URL**: https://discourse.slicer.org/t/extract-slice-view-rotations-for-applying-to-crop-volume-roi/47607

---

## Post #1 by @hherhold (2026-07-13 13:46 UTC)

<p>Is there a way to extract the rotation transform of slice views rotated using ctrl-alt-left-click-and-drag? It would be super handy to be able to take that and paste it into a transform to apply to a crop volume ROI. It’s easy enough to just rotate the ROI by hand and get it close, but I was wondering if a quick python snippet to extract the rotation angles and make a quick transform would be doable.</p>

---

## Post #2 by @chir.set (2026-07-13 17:01 UTC)

<p>May be you are referring to the <em>SlicerToRAS</em> matrix of a slice node.</p>
<pre><code class="lang-auto">sliceNode = slicer.app.layoutManager().sliceWidget("Red").mrmlSliceNode()
mx = sliceNode.GetSliceToRAS()
t = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLTransformNode")
t.ApplyTransformMatrix(mx)
</code></pre>
<p>Apply the MRML transform node to the ROI node in the <code>Transforms module</code> and tell us if that’s what you meant.</p>

---
