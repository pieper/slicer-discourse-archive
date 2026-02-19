---
topic_id: 9817
title: "Connecting Function To Ending Of Mouse Hovering Over Fiducia"
date: 2020-01-14
url: https://discourse.slicer.org/t/9817
---

# Connecting function to ending of mouse hovering over fiducial event without activate control point set

**Topic ID**: 9817
**Date**: 2020-01-14
**URL**: https://discourse.slicer.org/t/connecting-function-to-ending-of-mouse-hovering-over-fiducial-event-without-activate-control-point-set/9817

---

## Post #1 by @jdp (2020-01-14 21:34 UTC)

<p>I am using markups to put down fiducial markers and am coding in python. Using python I can “set” an active control point by, (A) clicking with the mouse, or (B) in a python line of code as follows:</p>
<p>slicer.util.getNode(“F”).GetDisplayNode().SetActiveControlPoint()</p>
<p>However, in the process of learning slicer, I have also notice two capabilities with the fiducial node display object. 1 - when an active control point is set it then becomes “green” highlighted. 2 - I also see when the mouse hovers over a fiducial control point without clicking it also becomes active. It is this second observation that I would like to expand upon in my code by creating a function that executes after a hovering event over a fiducial ends. My questions are:</p>
<p>Is there a way I can create a listener, i.e., observer, for when my hover over a fiducial ends and how do I do this? In other words, moving the mouse after hovering (and without activating the control point) I would like to have an observer connected to a function script. Is there an easy workaround for slicer?</p>

---

## Post #2 by @lassoan (2020-01-14 21:39 UTC)

<p>You can add an observer to the markups display node to get notification about a control activated/deactivated. You can add observer to the markups node to get notification about point position change (including current point that is being placed) or add an observer to the crosshair node to get current mouse position. See examples in <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository">script repository</a>.</p>

---

## Post #3 by @jdp (2020-01-16 01:32 UTC)

<p>Thank you, <a class="mention" href="/u/lassoan">@lassoan</a>.</p>
<p>For others: I achieved my goal by first creating an observer using “PointStartInteractionEvent” that would activate when I clicked on a fiducial point. This click would then activate a sub-observer that would listen for mouse movement using crosshair as suggested. On mouse movement I excuted my function and then quickly closed the observer connected to the mouse movement using crosshair.</p>

---

## Post #4 by @lassoan (2020-01-16 01:48 UTC)

<p>Thanks for sharing what worked for you. Note that if you activate “point placement” mode then all the necessary events are emitted from markups node (since the previewed control point position follows the mouse pointer).</p>

---
