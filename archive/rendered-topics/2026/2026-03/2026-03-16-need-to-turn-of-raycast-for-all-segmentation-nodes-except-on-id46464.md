---
topic_id: 46464
title: "Need To Turn Of Raycast For All Segmentation Nodes Except On"
date: 2026-03-16
url: https://discourse.slicer.org/t/46464
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
