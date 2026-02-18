# RAS to LPS transform for older models

**Topic ID**: 13724
**Date**: 2020-09-28
**URL**: https://discourse.slicer.org/t/ras-to-lps-transform-for-older-models/13724

---

## Post #1 by @muratmaga (2020-09-28 04:39 UTC)

<p>We have a bunch of models (and associated landmarks) that were exported from Slicer 4-5 years ago. Instead of trying to remember to set the coordinate to RAS each time when loading them, we would like to convert them to LPS, so that they continue to line up with the landmarks.</p>
<p>So just loading them as RAS, and then simply re-saving them is the appropriate conversion procedure?</p>

---

## Post #2 by @lassoan (2020-09-28 04:46 UTC)

<p>If a model is in RAS coordinate system and the coordinate system is not stored in the files then you need to select “RAS” when you load it (in “Add data” window). When you save this model, it will be saved in RAS coordinate system (to cause minimal change in the file), but the coordinate system will be stored in it. If you want to save as LPS then you need to change the coordinate system in its storage node:</p>
<pre><code class="lang-auto">getNode('SomeNode').GetStorageNode().SetCoordinateSystem(slicer.vtkMRMLStorageNode.CoordinateSystemLPS)
</code></pre>

---
