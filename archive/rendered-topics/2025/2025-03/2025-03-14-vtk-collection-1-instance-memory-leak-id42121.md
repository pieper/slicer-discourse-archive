---
topic_id: 42121
title: "Vtk Collection 1 Instance Memory Leak"
date: 2025-03-14
url: https://discourse.slicer.org/t/42121
---

# Vtk collection 1 instance memory leak

**Topic ID**: 42121
**Date**: 2025-03-14
**URL**: https://discourse.slicer.org/t/vtk-collection-1-instance-memory-leak/42121

---

## Post #1 by @Derek_Wang (2025-03-14 01:21 UTC)

<p>in 3d slicer ScriptedLoadableModuleWidget class, setup is to load the widget,when exitting from slicer,what method will be called to prevent memory leak</p>

---

## Post #2 by @lassoan (2025-03-14 01:33 UTC)

<p>When you call a “factory” mehtod that returns a new <code>vtkCollection</code> object then you need to call <code>UnRegister(None)</code> on that object to prevent memory leaks. See more information <a href="https://slicer.readthedocs.io/en/latest/developer_guide/advanced_topics.html#factory-methods">here</a>.</p>

---

## Post #3 by @Derek_Wang (2025-03-14 08:36 UTC)

<p>Thanks a lot for the help.</p>

---

## Post #4 by @Derek_Wang (2025-03-15 00:06 UTC)

<p>self.segmentEditorWidget.exit()<br>
self.segmentEditorWidget.setSegmentationNode(None)<br>
self.segmentEditorWidget.setMRMLScene(None)<br>
self.segmentationNode.UnRegister(None)<br>
slicer.mrmlScene.RemoveNode(self.segmentationNode)<br>
self.segmentEditorWidget.deleteLater()</p>

---
