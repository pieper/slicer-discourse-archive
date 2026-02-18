# Update UI widget after programmatically set values in volume node

**Topic ID**: 28882
**Date**: 2023-04-13
**URL**: https://discourse.slicer.org/t/update-ui-widget-after-programmatically-set-values-in-volume-node/28882

---

## Post #1 by @RonJones (2023-04-13 12:12 UTC)

<p>I adapted the code from the activate hanging protocol example to set the color window/levels. (<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#activate-hanging-protocol-by-keyboard-shortcut" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a>))</p>
<p>The volume updates correctly and shows the correct color levels, but the UI widgets are not updated. Specifically the window/level widgets in the Volume UI.</p>
<p>This code sets the values in the volume</p>
<pre><code class="lang-auto">petNode = slicer.util.getNodesByClass('vtkMRMLScalarVolumeNode'):
petColor = slicer.mrmlScene.GetFirstNodeByName('PET-Heat')
petNode.GetVolumeDisplayNode().SetAndObserveColorNodeID(petColor.GetID())
petNode.GetVolumeDisplayNode().SetWindowLevelMinMax(0, 20)
</code></pre>
<p>How do the UI widgets get notified of the change?</p>
<p>thanks.</p>

---

## Post #2 by @lassoan (2023-04-13 12:14 UTC)

<p>The GUI updates automatically when the MRML nodes are modified. Volumes module probably showed a different volume than what you modified. Or maybe you modified the volume rendering display node. This code snippet changes scalar volume display nodes of all loaded volumes:</p>
<pre><code class="lang-python">petColor = slicer.mrmlScene.GetFirstNodeByName('PET-Heat')
petNodes = slicer.util.getNodesByClass('vtkMRMLScalarVolumeNode')
for petNode in petNodes:
    displayNode = petNode.GetScalarVolumeDisplayNode()
    displayNode.SetAndObserveColorNodeID(petColor.GetID())
    displayNode.SetWindowLevelMinMax(0, 20)
</code></pre>

---

## Post #3 by @RonJones (2023-04-14 04:24 UTC)

<p>Thanks, much appreciated. The UI widgets were being updated.</p>
<p>I worked out I needed to explicitly turn off auto window level before setting the window/level values so they weren’t immediately overridden in the UI widget.</p>
<pre><code class="lang-auto">displayNode = petNode.GetScalarVolumeDisplayNode()
displayNode.SetAndObserveColorNodeID(petColor.GetID())
displayNode.AutoWindowLevelOff()
displayNode.SetWindowLevelMinMax(0, 20)
</code></pre>
<p>It  works now. Thanks.</p>

---
