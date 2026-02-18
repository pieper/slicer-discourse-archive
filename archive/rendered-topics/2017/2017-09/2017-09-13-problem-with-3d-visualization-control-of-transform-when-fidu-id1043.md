# Problem with 3D visualization/control of transform when fiducial have been placed in scene

**Topic ID**: 1043
**Date**: 2017-09-13
**URL**: https://discourse.slicer.org/t/problem-with-3d-visualization-control-of-transform-when-fiducial-have-been-placed-in-scene/1043

---

## Post #1 by @Sam_Horvath (2017-09-13 19:51 UTC)

<p>Operating System: Windows 10<br>
Slicer version: 3D Slicer 4.7.0-2017-09-12 (most recent nightly) - Also observed in older versions going back a few months<br>
Expected behavior:  Interactive transform adjustment using the 3D widget should work as normal after a fiducial has been placed<br>
Actual behavior:  After placing a fiducial using the toolbar (thereby creating the fiducial node), the 3D transform widget cannot be translated.  The center point cannot be selected and dragged.  This persists for all new transforms created in the scene, and even after closing the scene.  It is only resolved by restarting slicer.</p>
<p>It seems that something in the interaction logic for the fiducials is making the center control point of the transform widget unselectable.</p>
<p>Thanks,</p>
<p>Sam</p>

---

## Post #2 by @lassoan (2017-09-13 20:28 UTC)

<p>I could reproduce this issue. As a workaround, you can just hold down shift while drag-and-drop to translate the widget.</p>

---

## Post #3 by @Sam_Horvath (2017-09-13 20:50 UTC)

<p>Yep, that is what I am doing for now!  Using that method, I have discovered a probably related issue.  If a transform widget is “obscuring” a fiducial, the fiducial will not be moveable even if the transform widget is not visible.</p>

---

## Post #4 by @lassoan (2017-09-13 21:38 UTC)

<p>I’ve checked the code and it seems that drag-and-drop by clicking the middle is not supposed to work. It only works because the picking manager (that is responsible for assigning a click to a widget action) is not initialized until a fiducial or ROI widget is placed. If I fix the initialization then the transform’s box widget can never be translated using the middle handle because it is inside the box. Similarly, you can only click on the sphere on the sides to scale the transform if you are on the correct side of the box (you cannot click it from behind).</p>
<p>I’ll update the code to make the behavior is consistent (which means translation will always require shift-click). If you need translation without pressing shift key then please <a href="https://issues.slicer.org">submit a feature request</a>.</p>

---

## Post #5 by @Johan_Andruejol (2017-09-14 10:51 UTC)

<p>Thanks Andras for looking into this !</p>
<p>Note that you can also translate the widget by using your middle (i.e.<br>
wheel) button on a mouse.</p>

---
