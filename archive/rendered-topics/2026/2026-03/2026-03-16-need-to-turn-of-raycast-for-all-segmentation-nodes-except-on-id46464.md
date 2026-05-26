---
topic_id: 46464
title: "Need to turn of raycast for all segmentation node's except one in 3D view"
date: 2026-03-16
url: https://discourse.slicer.org/t/46464
last_bumped: 2026-03-18T09:24:53.290Z
---

# Need to turn of raycast for all segmentation node's except one in 3D view

**Topic ID**: 46464
**Date**: 2026-03-16
**URL**: https://discourse.slicer.org/t/need-to-turn-of-raycast-for-all-segmentation-nodes-except-one-in-3d-view/46464

---

## Post #1 by @Victor_Wayne (2026-03-16 09:20 UTC)

<p>Hello,</p>
<p>I have a target tissue segmented using the Segment editor. And I have more than 150 ellipsoidal segmentation nodes in the scene and visible in the 3D views. And I have to draw a line on the views. When I draw the line I want it to snap on the target segmentation. But when there are lot ellipsoidal segmentation the dragging an snapping of the line becomes significantly slower. How can I make slicer stop ray casting the ellipsoidal segmentation nodes? I don’t want to hide the ellipsoidal probes. It needs to be visible. Is there any flags for this?</p>
<p>Thanks for your help in advance.</p>

---

## Post #2 by @cpinter (2026-03-16 14:07 UTC)

<p>I think so, at least it definitely works with model nodes. If you right-click the node in the Data module (subject hierarchy) you’ll see an option called “Selectable”. If you turn it off, then 3D picking will be disabled. Note that you can only do this at node level, so if you need to snap on a segment but not on others, you may need to split them into two nodes.</p>
<p>Let me know if this doesn’t work on segmentations - I think it should.</p>

---

## Post #3 by @Victor_Wayne (2026-03-17 05:20 UTC)

<p>Thanks for replying.<br>
I am not seeing an option called Selectable for both segmentation node and model node.</p>
<p>When I right click on a segmentation node or model node in the subject hierarchy tree view of the Data module I am seeing  the options Rename, Clone, Delete, Remove closed Surface Representation, Export Visible Segments to Model, Export Visible Segments to Binary Labelmap, Create Child Folder</p>
<p>And when I right click on a model nodeI am seeing the options for Rename, Clone, Delete, Edit Properties, Convert Model to Segmentation node, Export to file, Export to DICOM, Create Child Folder, Show empty folder.<br>
That’s it.</p>
<p>And I cannot find a setting like selectable in the edit property section of a model node or a segmentation node.</p>
<p>I am only working with segmentation nodes. I want to set a flag programmatically to those ellipsoidal segmentation node so that slicer doesn’t ray cast those segmentation nodes.</p>

---

## Post #4 by @cpinter (2026-03-17 10:22 UTC)

<p>You’re right, I forgot that the “Selectable” option is added by the Virtual Reality extension. If you install it you’ll have that checkbox and then you can disable point picking.</p>

---

## Post #5 by @Victor_Wayne (2026-03-17 11:24 UTC)

<p>I need to programmatically turn off point picking. How can I do that? The scene could contain 100s of ellipsoidal probes. I can’t expect the user to turn of selectable to every probe one by one.</p>

---

## Post #6 by @cpinter (2026-03-17 13:01 UTC)

<p>Understood. It is quite simple:</p>
<pre><code class="lang-auto">s = getNode('Segmentation')
s.SetSelectable(False)
</code></pre>

---

## Post #8 by @Victor_Wayne (2026-03-18 09:24 UTC)

<p>Thank you for your help. It worked.</p>

---
