# Reproducible Slicer crash deleting MarkupsROINodes from subject hierarchy

**Topic ID**: 36007
**Date**: 2024-05-08
**URL**: https://discourse.slicer.org/t/reproducible-slicer-crash-deleting-markupsroinodes-from-subject-hierarchy/36007

---

## Post #1 by @mikebind (2024-05-08 21:15 UTC)

<p>I get a reproducible Slicer application crash following these steps:</p>
<p>Open Slice (scene is empty)<br>
Run</p>
<pre><code class="lang-auto">roiNode1 = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsROINode")
roiNode1.SetSize((100, 100, 100))
roiNode2 = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsROINode")
roiNode2.SetSize((50, 50, 50))
</code></pre>
<p>Select both ROI nodes in the subject hierarchy, right click, and select Delete.  After a brief pause, Slicer crashes.</p>
<p>If I don’t set the size I don’t get a crash.  If I create the ROIs using the GUI, I don’t get the crash.  I’m using Slicer 5.7.0-2024-05-1 on Windows.<br>
Also, if there is only one ROI node, deleting it doesn’t cause a crash, so perhaps it has something to do with iterating over multiple objects to delete. Also, since deleting multiple ROIs which were created via GUI does not cause the crash, I would guess that maybe there is something incompletely initialized about those created via AddNewNodeByClass.</p>

---

## Post #2 by @mikebind (2024-05-08 22:37 UTC)

<p>No crash on the same sequence of actions in 5.6.1, so it must be due to a change introduced between 5.6.1 and 5.7.0-2024-05-01</p>

---

## Post #3 by @Sunderlandkyl (2024-05-09 13:19 UTC)

<p>Thanks for reporting! I am working on a fix.</p>

---

## Post #4 by @Sunderlandkyl (2024-05-10 13:36 UTC)

<p>Fixed in <a href="https://github.com/Slicer/Slicer/pull/7736" class="inline-onebox" rel="noopener nofollow ugc">BUG: Fix crash when deleting multiple markups in subject hierarchy by Sunderlandkyl · Pull Request #7736 · Slicer/Slicer · GitHub</a>.</p>

---
