# Slice views get reset when updated from cli output in a segment editor effect

**Topic ID**: 26782
**Date**: 2022-12-17
**URL**: https://discourse.slicer.org/t/slice-views-get-reset-when-updated-from-cli-output-in-a-segment-editor-effect/26782

---

## Post #1 by @Alex_Gilman (2022-12-17 02:34 UTC)

<p>Operating system: linux (ubuntu 20.04)<br>
Slicer version: 5.2.1<br>
Expected behavior: slice views are not reset, only segments change<br>
Actual behavior: slice views are re-centered</p>
<p>My scripted segment editor effect sends segments to a cli module for modification. After the cli completes, the existing segmentation gets updated from the returned labelmap:</p>
<pre><code class="lang-auto">segmentationNode = self.scriptedEffect.parameterSetNode().GetSegmentationNode()
slicer.vtkSlicerSegmentationsModuleLogic.ImportLabelmapToSegmentationNode(
    self.output_labelmap_volume,
    segmentationNode,
    structure_segment_ids
)
</code></pre>
<p>The segments get updated appropriately, but in the process the slice views get reset to the center of the reference volume. The same code run in a Jupyter notebook outside of a segment editor effect does not reset the slice views. What could be the cause of this resetting? Is there a way to set up the segment editor effect or the input or output volume nodes to prevent it?</p>

---

## Post #2 by @lassoan (2022-12-17 14:06 UTC)

<p>You can set <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.cli.runSync"><code>update_display=False</code></a> to prevent automatic display of CLI execution results.</p>

---

## Post #3 by @Alex_Gilman (2022-12-17 15:32 UTC)

<p>That was it! Thank you very much.</p>

---
