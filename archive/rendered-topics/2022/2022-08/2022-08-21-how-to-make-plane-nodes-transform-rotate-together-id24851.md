# How to make plane nodes transform/rotate together

**Topic ID**: 24851
**Date**: 2022-08-21
**URL**: https://discourse.slicer.org/t/how-to-make-plane-nodes-transform-rotate-together/24851

---

## Post #1 by @seanchoi0519 (2022-08-21 10:05 UTC)

<p>Hello, I am trying to find a way to grab 2 planes (generated from markups module) and if I move 1 plane, I can make the other plane move by the identical x,y,z as well as rotation amount</p>
<p>How can I do this programmatically? assuming I have displayNodes of both planes.<br>
Thanks in advance!</p>

---

## Post #3 by @seanchoi0519 (2022-08-21 13:49 UTC)

<p>After some research, I think the best way to do this would be by adding an observer of some sort to track the movement of one of the planes - then move them in sync. Would this be the way to go?<br>
Any other solutions are also welcome <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #4 by @lassoan (2022-11-13 15:18 UTC)

<p>You can find an example of how to rotate view planes together (for simulating x-view for heart valve imaging) in SlicerHeart extension’s <a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/ValveView/ValveView.py">ValveView module</a>.</p>

---
