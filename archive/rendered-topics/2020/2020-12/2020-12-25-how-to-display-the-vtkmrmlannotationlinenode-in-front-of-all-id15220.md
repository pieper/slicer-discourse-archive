# How to display the vtkMRMLAnnotationLineNode in front of all model node

**Topic ID**: 15220
**Date**: 2020-12-25
**URL**: https://discourse.slicer.org/t/how-to-display-the-vtkmrmlannotationlinenode-in-front-of-all-model-node/15220

---

## Post #1 by @MurphyJOE (2020-12-25 03:38 UTC)

<p>Hello, deverlopers:</p>
<p>I have load several STL files into scene as model node, and create a new mrml annotation line behind the model node.<br>
But, I wanna to display the annotation node always in front of all model nodes, no matter where annotation node locates.</p>
<p>How could I make it?</p>

---

## Post #2 by @lassoan (2020-12-25 21:00 UTC)

<p>This feature has been added to Markups module in recent Slicer Preview Release.</p>
<p>In Markups module’s advanced visualization section you can choose to show occluded parts of markups (lines, curves, etc). You can choose to make occluded part appear semi-transparent, this way you don’t break the 3D rendering: you preserve depth cues, but you can also see and pick markups in all viewing angles.</p>

---
