# Select visibility of specific vtkMRMLScalarVolumeNode

**Topic ID**: 28264
**Date**: 2023-03-09
**URL**: https://discourse.slicer.org/t/select-visibility-of-specific-vtkmrmlscalarvolumenode/28264

---

## Post #1 by @shimashah (2023-03-09 20:29 UTC)

<p>Operating system: MacOS 12.6<br>
Slicer version:5.0.3</p>
<p>When I load DICOM to the Subject hierarchy scene, there are multiple vtkMRMLScalarVolumeNodes and all are invisible. I need to select one specific one of them here, and then in the Master volume select the same volume. (The name of the volume changes every time I load the DICOM to the scene with the same code). I see previous posts referring to <strong>qSlicerSubjectHierarchyVolumesPlugin.cxx</strong>. Is there any python code that works in Python interactor?</p>

---

## Post #2 by @ebrahim (2023-03-12 08:49 UTC)

<p>For changing the visibility of a vtkMRMLScalarVolumeNode called <code>volume_node</code> from python:</p>
<pre><code class="lang-py">shNode = slicer.mrmlScene.GetSubjectHierarchyNode()
itemID = shNode.GetItemByDataNode(volume_node)
slicer.qSlicerSubjectHierarchyVolumesPlugin().setDisplayVisibility(itemID, 0) # 0 or 1 for visibility
</code></pre>

---
