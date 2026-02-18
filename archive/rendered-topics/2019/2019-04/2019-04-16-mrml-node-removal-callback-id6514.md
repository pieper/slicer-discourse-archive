# MRML node removal callback

**Topic ID**: 6514
**Date**: 2019-04-16
**URL**: https://discourse.slicer.org/t/mrml-node-removal-callback/6514

---

## Post #1 by @michalikthomas (2019-04-16 16:30 UTC)

<p>How to correctly register a callback for MRML node removal (specifically <code>vtkMRMLModelNode</code> and <code>vtkMRMLMarkupsFiducialNode</code>) in python scripted module?</p>

---

## Post #2 by @lassoan (2019-04-16 17:03 UTC)

<p>You can observe <a href="https://apidocs.slicer.org/master/classvtkMRMLScene.html#a8ccb4e378bdb987a4e95ac6cc1067c94a2a51ee0218f53512c95cbc94d5e4dab4" rel="nofollow noopener">vtkMRMLScene.NodeAboutToBeRemoved</a> event. See an example how to observe a scene event in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Show_volume_rendering_automatically_when_a_volume_is_loaded" rel="nofollow noopener">script repository</a>.</p>

---
