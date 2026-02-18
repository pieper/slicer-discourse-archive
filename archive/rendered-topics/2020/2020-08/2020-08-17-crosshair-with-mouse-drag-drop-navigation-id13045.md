# Crosshair with mouse drag&drop navigation

**Topic ID**: 13045
**Date**: 2020-08-17
**URL**: https://discourse.slicer.org/t/crosshair-with-mouse-drag-drop-navigation/13045

---

## Post #1 by @cpinter (2020-08-17 15:40 UTC)

<p>Hi all,</p>
<p>I am trying to find out how to access the mouse drag&amp;drop navigation feature that the crosshair used to have. I use the latest nightlies, and cannot find the option. In the documentation, in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/MouseandKeyboardShortcuts">first screenshot here</a> it is available, but even in 4.10.2 it is not.</p>
<p>Can someone tell me whether it was removed completely for some reason, or just hidden from the UI but can be evoked programmatically? It would be nice to have it somehow, because for a certain application it is important not to have to use the keyboard, but the shift+move kind of navigation is very useful.</p>
<p>Thank you!</p>

---

## Post #2 by @lassoan (2020-08-17 15:56 UTC)

<p>Drag-and-drop of crosshair was dropped 5-6 years ago. There were some issues and inconsistencies in the interactions and it was easier to remove it than figure out a new operating mode.</p>
<p>Now that we have mouse modes, view widgets, and ability to rotate slice views, it makes sense to implement slice intersection manipulation with drag-and-drop.</p>
<p>Probably we could leave crosshair as is, and make slice intersection lines interactive instead (as it is very hard to find the crosshair in 3D, there is only one of that in the whole scene - not per view group, and it does not support slice rotation). You can implement everything in vtkMRMLSliceIntersectionWidget.</p>
<p>The interaction could be something like this:</p>
<ul>
<li>adjust slice offset of all views if you click near the intersection point</li>
<li>offset a single slice if click on an intersection line a bit farther from the intersection point</li>
<li>rotate slice if clicking near the tip of an intersection line (or maybe Ctrl key + click on an intersection line)</li>
</ul>

---

## Post #3 by @cpinter (2020-08-17 16:04 UTC)

<p>Thanks Andras! I figured it was removed quite a while ago, and indeed couldn’t see much of the logic in the code (other than vtkMRMLCrosshairNode::Navigation, which we should remove btw for 5.0).</p>
<p>OK, if we get to the point where we start implementing the mouse-only crosshair, then I’ll start with your high-level plan and probably ask for more details if I’m stuck. Thanks again!</p>

---
