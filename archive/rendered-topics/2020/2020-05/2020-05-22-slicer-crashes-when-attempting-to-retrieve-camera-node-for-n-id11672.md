# Slicer crashes when attempting to retrieve camera node for non-existent 3D view

**Topic ID**: 11672
**Date**: 2020-05-22
**URL**: https://discourse.slicer.org/t/slicer-crashes-when-attempting-to-retrieve-camera-node-for-non-existent-3d-view/11672

---

## Post #1 by @mikebind (2020-05-22 21:08 UTC)

<p>The following command entered at the Python interactor of a newly opened Slicer crashes the program and the window closes:</p>
<p><code>    camNode = slicer.modules.cameras.logic().GetViewActiveCameraNode(slicer.app.layoutManager.threeDWidget(1).mrmlViewNode())</code></p>
<p>This works fine if the view exists; for example</p>
<p><code>    camNode = slicer.modules.cameras.logic().GetViewActiveCameraNode(layoutManager.threeDWidget(0).mrmlViewNode())</code></p>
<p>does not crash Slicer and just returns the camera node for 3D View 1.  I discovered this bug when I accidentally forgot to subtract 1 from the view index and requested the camera node for a view which did not exist, and lost my work in Slicer up to that point since the last time I saved.</p>

---

## Post #2 by @lassoan (2020-05-22 21:22 UTC)

<p>Thanks for reporting this. In general, Python-wrapped C++ code is still just C++ code, which crashes if it gets invalid pointers or you try to access items out of bounds of an array, but we can harden specific calls by adding more checks and declaring item counts at the Python interface.</p>

---

## Post #3 by @mikebind (2020-05-22 23:57 UTC)

<p>Got it.  That makes sense.</p>

---

## Post #4 by @lassoan (2020-05-23 05:31 UTC)

<p>FYI, I’ve pushed a <a href="https://github.com/Slicer/Slicer/commit/b6a93a75501393c2b033b490cc3e7bfd642d98da">fix</a> for this crash.</p>

---
