# Disable middle-mouse drag for markups

**Topic ID**: 28356
**Date**: 2023-03-13
**URL**: https://discourse.slicer.org/t/disable-middle-mouse-drag-for-markups/28356

---

## Post #1 by @JASON (2023-03-13 21:14 UTC)

<p>Hello, I am placing many markup points on a surface in the 3D view. Occasionally I middle-mouse drag to pan the 3D view and I accidentally end up dragging all the control points for the node. This operation is not undo-able as far as I can tell.  Is there any way to disable middle-mouse drag for markups, but leave the control points unlocked for editing?</p>

---

## Post #2 by @muratmaga (2023-03-13 21:46 UTC)

<p>There are two ways to mitigate this problem. Either per point basis or for all points in the markup object.</p>
<ol>
<li>
<p>After placing the markup point in correct position, you can click the lock button next to it in the control points table. You won’t be able to reposition this landmark until you unlock it. (red highlight)</p>
</li>
<li>
<p>You can click the lock button (on the left) to disable to any interaction with any of the control points in the markups list. You can still new points to add to list, but cannot move them. (blue highlight)</p>
</li>
</ol>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d8341ea8639d4b35f391954862034f4d7ba9ddc9.png" alt="image" data-base62-sha1="uQCNzYpT4IoZN7RvWPRm0CQHwcV" width="637" height="488"></p>

---

## Post #3 by @pieper (2023-03-13 22:05 UTC)

<p>If you find yourself doing this a lot, you could assign <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#customize-keyboard-shortcuts">a keyboard shortcut</a> that locks/unlocks the current node.</p>
<p>This thread should help: <a href="https://github.com/Slicer/Slicer/issues/4576" class="inline-onebox">Undo feature for Markups module · Issue #4576 · Slicer/Slicer · GitHub</a></p>

---

## Post #4 by @JASON (2023-03-13 22:11 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> Thanks for the insight.  I have over a thousand points and I need to leave them unlocked for editing, but I discovered that if even a single control point is locked, then middle-mouse dragging of all control points is disabled.<br>
In my case I just leave the first point locked and this allows me to continue editing while avoiding the unwanted behavior of accidently dragging points when panning the 3D view.</p>

---

## Post #5 by @muratmaga (2023-03-13 22:16 UTC)

<p>You mean</p>
<aside class="quote no-group" data-username="JASON" data-post="4" data-topic="28356">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jason/48/13419_2.png" class="avatar"> JASON:</div>
<blockquote>
<p>but I discovered that if even a single control point is locked, then middle-mouse dragging of all control points is disabled.</p>
</blockquote>
</aside>
<p>You mean you drag all the points together when you accidentally drag one? If that’s the case, I remember a bug like that, which I thought was fixed sometime ago. What version of Slicer are you using?</p>
<p>The alternative if to define a key (e.g., l for lock) as <a class="mention" href="/u/pieper">@pieper</a> suggested, so that you don’t have to interact with the menus (which slows you down).</p>

---

## Post #6 by @JASON (2023-03-13 22:32 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> I do believe that left-click to drag a single point and middle-click to drag all points within a node is the intended behavior (I’m on Slicer v5.3.0).<br>
The idea of assigning a shortcut to lock / unlock the node every time I want to pan in the 3D view is reasonable solution, but In my case I think I’ll go with leaving the first point in the list locked and all other points unlocked.  This way I can continue editing without accidentally middle-mouse dragging all my points.<br>
Thanks for the ideas!</p>

---

## Post #7 by @muratmaga (2023-03-13 23:07 UTC)

<aside class="quote no-group" data-username="JASON" data-post="6" data-topic="28356">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jason/48/13419_2.png" class="avatar"> JASON:</div>
<blockquote>
<p>I do believe that left-click to drag a single point and middle-click to drag all points within a node is the intended behavior (I’m on Slicer v5.3.0).</p>
</blockquote>
</aside>
<p>No from my perspective that’s a bug, and a costly one, as you cannot undo it! I am surprised it is not fixed. The same functionality can easily achieved by putting the markup list under a transform object and doing the same via transforms.</p>
<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a>, I think this is an accident waiting to happen. What’s the use case behind this that overcomes the risk it creates.</p>

---

## Post #8 by @lassoan (2023-03-13 23:21 UTC)

<p>Definition of a bug: a feature that cannot be turned off.</p>
<p>This feature can be turned off by mapping the middle-button click-and-drag interaction event to no widget event. It requires Python scripting, so you may argue that it cannot be turned off. Maybe we should make these event mappings adjustable via some GUI.</p>
<p>Alternatively, you can enable undo/redo for markups.</p>

---

## Post #9 by @muratmaga (2023-03-13 23:31 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="28356">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Alternatively, you can enable undo/redo for markups.</p>
</blockquote>
</aside>
<p>That would be the most useful thing. How do you do that?</p>

---

## Post #10 by @jamesobutler (2023-03-13 23:36 UTC)

<p>This post has information on markups undo/redo</p>
<aside class="quote quote-modified" data-post="11" data-topic="20140">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/new-markups-functionality-retains-unset-control-point-positions/20140/11">New Markups functionality retains unset control point positions</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Actually, the undo functionality is already available in Slicer. You can enable undo/redo for fiducial nodes by copy-pasting these lines into the Python console: 
# Enable undo for the scene

slicer.mrmlScene.SetUndoOn()

# Enable undo for markups fiducial nodes

defaultMarkupsNode = slicer.mrmlScene.GetDefaultNodeByClass("vtkMRMLMarkupsFiducialNode")
if not defaultMarkupsNode:
    defaultMarkupsNode = slicer.vtkMRMLMarkupsFiducialNode()
    slicer.mrmlScene.AddDefaultNode(defaultMarkupsNode)

…
  </blockquote>
</aside>


---

## Post #11 by @muratmaga (2023-03-14 00:03 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="10" data-topic="28356">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>This post has information on markups undo/redo</p>
</blockquote>
</aside>
<p>I meant making it widely available for the users, not just for developers.</p>

---
