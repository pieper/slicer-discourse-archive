---
topic_id: 34345
title: "Event For Scaling Interaction To Modify Bounds Of Markupspla"
date: 2024-02-15
url: https://discourse.slicer.org/t/34345
---

# Event for Scaling Interaction to modify Bounds of MarkupsPlaneNode?

**Topic ID**: 34345
**Date**: 2024-02-15
**URL**: https://discourse.slicer.org/t/event-for-scaling-interaction-to-modify-bounds-of-markupsplanenode/34345

---

## Post #1 by @Juergen (2024-02-15 17:14 UTC)

<p>Hello,</p>
<p>I’ve been experimenting with <code>vtkMRMLMarkupsPlaneNode.PointModifiedEvent</code> to   control the dimensions of another object, in this case an elliptical cylinder.<br>
The idea is to put the plane of the MarkupsPlane along the major radius vector of the elliptical cross-section of the elliptical cylinder. By dragging the Interaction handles for Scaling of the MarkupsPlane, I can control the major radius of the ellipse and the length of the cylinder.</p>
<p>When I try to use the <code>vtkMRMLMarkupsPlaneNode.PointModifiedEvent</code> to fire an event after dragging the Scaling interaction handles with the mouse, I don’t get an event. As the name suggests, the <code>PointModifiedEvent</code> only fires when I drag the rotation wheel or the center control point to translate.</p>
<p>These two events are still parts of the Interaction handle, yet they trigger <code>PointModifiedEvent</code>. Why does the Scaling handle to modify the bounds of the plane not fire an event?</p>
<p>Is there a workaround to fire an event in this case?</p>
<p>Btw, I guess I need to prevent an infinite event loop, so I first remove the particular callback before I modify the bounds from that callback function. I’ve had Slicer crash sometimes when I don’t get that done right.</p>
<p>Thanks</p>

---
