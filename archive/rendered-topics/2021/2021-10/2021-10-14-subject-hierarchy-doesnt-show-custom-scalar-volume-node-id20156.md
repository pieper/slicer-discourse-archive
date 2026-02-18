# Subject hierarchy doesn't show custom scalar volume node

**Topic ID**: 20156
**Date**: 2021-10-14
**URL**: https://discourse.slicer.org/t/subject-hierarchy-doesnt-show-custom-scalar-volume-node/20156

---

## Post #1 by @keri (2021-10-14 18:42 UTC)

<p>Hi,</p>
<p>I’m making first steps in developing custom nodes.<br>
I’ve created <code>vtkMRMLSeis3DStackNode</code> inherited from <code>vtkMRMLSeis3DStackNode</code>. I registered it using <code>scene-&gt;RegisterNodeClass(vtkSmartPointer&lt;vtkMRMLSeis3DStackNode&gt;::New());</code>.</p>
<p>When I add to scene my node I only can see it in data module - &gt; “All nodes”.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dc034fa3e32d14b61b03bfa660e4657ab544d4a3.png" alt="image" data-base62-sha1="vok8wuL5BLh3hynNGUisyF8vZAf" width="484" height="365"></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/00736fd022e874c550bb24ae12b0306fdfb8865e.jpeg" alt="image" data-base62-sha1="3ZjYiAARzwhG0Na2pKiwpvhmMu" width="458" height="357"></p>
<p>I can’t find it in “Subject hierarchy” neither in “Volumes” module</p>

---

## Post #2 by @keri (2021-10-15 01:17 UTC)

<p>My negligence let me down again…<br>
The typo was in header file: I accidently typed <code>vtkTypeMacro(vtkMRMLSeis3DStackNode,vtkMRMLTransformableNode);</code> instead of <code>vtkTypeMacro(vtkMRMLSeis3DStackNode,vtkMRMLScalarVolumeNode);</code></p>
<p>Now I can see my volume on the scene.</p>

---

## Post #3 by @cpinter (2021-10-15 09:15 UTC)

<p>Thanks for the update!</p>

---
