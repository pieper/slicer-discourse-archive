# Extract Transfer Function from Color Table

**Topic ID**: 5489
**Date**: 2019-01-23
**URL**: https://discourse.slicer.org/t/extract-transfer-function-from-color-table/5489

---

## Post #1 by @Valtiel (2019-01-23 19:54 UTC)

<p>Hi!</p>
<p>I’m trying to apply a transfer function to my volume-rendering. I have a custom <code>vtkMRMLColorTableNode</code>, but <code>GetScalarsToColors()</code> always returns a <code>vtkLookupTable</code>. Is there a way to get a <code>vtkTransferFunction</code> out of this?</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2019-01-23 23:44 UTC)

<p>Transfer functions are stored in volume rendering property nodes.</p>

---

## Post #3 by @Hamburgerfinger (2019-01-24 01:24 UTC)

<p>If you just want the colors in your table to be transferred for volume rendering, you can just click the “Sync with Volumes” checkbox in the properties in the Volume Rendering module. Then uncheck it and you can set the opacities, etc.</p>

---

## Post #4 by @Valtiel (2019-02-02 19:05 UTC)

<p>Thanks to you two, I managed to find the correct function in the source code!</p>
<p>The way I did it was as follows:</p>
<ol>
<li>First, get the Volume Rendering Logic via <code>volume_rendering_logic = slicer.modules.volumerendering.logic()</code>.</li>
<li>Then, create the Volume Rendering Node of the Volume Node by using <code>volume_rendering_node = volume_rendering_logic.CreateDefaultVolumeRenderingNodes(volume_node)</code>.</li>
<li>Finally,  “sync” the Display Node of the volume with the Volume Rendering Display Node via <code>volume_logic.CopyDisplayToVolumeRenderingDisplayNode(volume_rendering_node)</code>.</li>
</ol>
<p>Thanks again!</p>

---
