---
topic_id: 20484
title: "Add Ability To Safely Disengage Unintentionally Dragged Hand"
date: 2021-11-04
url: https://discourse.slicer.org/t/20484
---

# Add ability to safely disengage unintentionally dragged handle

**Topic ID**: 20484
**Date**: 2021-11-04
**URL**: https://discourse.slicer.org/t/add-ability-to-safely-disengage-unintentionally-dragged-handle/20484

---

## Post #1 by @DIV (2021-11-04 02:22 UTC)

<p>In the 3D viewport a common operation would be to use the mouse to rotate by <strong>left-clicking</strong> (or, strictly speaking, left-button-pressing) <strong>&amp; dragging</strong>.  The same sequence is also used for other tasks, though, such as resizing a ROI, or moving a fiducial marker (from the the the <strong>Markups</strong> module.</p>
<p>It has happened to me occasionally that I have intended to rotate the 3D view, but ended up inadvertently grabbing the handle of a ROI or a fiducial marker.  In such cases I’d like to be able to safely disengage the handle without making a change.  In other applications a similar action can be accomplished by pressing the <code>Esc</code> key on the keyboard before the mouse button is released.</p>
<p>Currently it is possible to lock marker positions, but they are unlocked by default, and some users must also like to have the ability to drag the marker positions from time to time.  A ROI can be hidden, but sometimes a user will want it to be visible while also rotating the 3D view.</p>
<p><em>The converse</em><br>
On some other occasions I might have wanted to resize the ROI, but ended up accidentally rotating the 3D view.  (Maybe it could happen to some users attempting to drag a marker too.)  Likewise in this converse situation it would be helpful to be able to disengage the view rotation safely, without changing it, by pressing the <code>Esc</code> key before the mouse button is released.</p>
<p>The other option, of course, would be a global <code>Undo</code> functionality, but I imagine that would be a bigger job.</p>
<p>—DIV</p>

---

## Post #2 by @lassoan (2021-11-04 03:24 UTC)

<p>During dragging the control point position or the view, the node parameters are updated immediately, so disengaging by Esc key would not help (the original state would not be restored). We could implement saving and restoring the state of the fiducial, but that is not trivial. We’d better spend that time with polishing up the global undo/redo feature in Slicer and enable it for markups - see details <a href="https://github.com/Slicer/Slicer/issues/4576#issuecomment-960420752">here</a>.</p>

---

## Post #3 by @pieper (2021-11-04 15:25 UTC)

<p>It would be nice if each of the widgets remembered the state at the start of the interaction and reset it if the escape key is pressed.  This doesn’t seem like a lot of complexity since it would be localized to the event handler code.</p>

---

## Post #4 by @lassoan (2021-11-04 17:46 UTC)

<p>Automatically reverting <em>all</em> changes that happened to a node during time of drag-and-drop could cause serious problems (any module can make any changes during the drag-and-drop and they would not expect all those changes to be reverted because a point was moved and point move was cancelled).</p>
<p>We could store and revert selected properties of the node (such as control point position, orientation, position status, autocreated flag), but instead of spending time with implementing and testing this, I think it would be better to provide the solution that users actually want: enabling undo/redo for markups.</p>

---

## Post #5 by @pieper (2021-11-04 18:08 UTC)

<p>I agree that finishing undo/redo is a worthwhile goal.</p>
<p>Regarding move events, if any code is updating continuously while the move it happening then it won’t be a problem for it to get another move event that resets the location to the start of the move.  If the code is just watching for the end of a move then it won’t matter if it’s cancelled.</p>

---

## Post #6 by @DIV (2021-11-08 07:46 UTC)

<p>I agree that both would be valuable.</p>
<p>Allowing <code>Esc</code> to disengage could <em>potentially</em> have some performance benefit, if re-computations could be avoided;  it’s also more immediate, and has the benefit of not needing a mouse manoeuvre or hotkey combination.<br>
Furthermore, I’m not sure how you intend/envisage implementing the ‘global’ undo.  Are you contemplating that it would even be keeping track of zoom/pan along with rotation in 3D port and slice number selection in slice viewports?  I’m not entirely sure whether that’s how users would want/expect it implemented, and it’s certainly not how all other applications work.  For instance, in Microsoft’s Office suite the <code>undo</code> button applies to distinct actions (such as typing a word), rather than view settings (<em>e.g.</em> cursor position, page/sheet/slide magnification) associated with ‘banal’ actions such as cursoring or scrolling.  .<br>
Yet <code>Esc</code> to disengage unintentional rotation in the 3D view could be useful, and intuitive, I feel.</p>

---

## Post #7 by @lassoan (2021-11-09 02:32 UTC)

<aside class="quote no-group" data-username="DIV" data-post="6" data-topic="20484">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/div/48/12816_2.png" class="avatar"> DIV:</div>
<blockquote>
<p>I’m not sure how you intend/envisage implementing the ‘global’ undo</p>
</blockquote>
</aside>
<p>Global undo is already implemented in Slicer and used in specific projects. It is hard to implement it to work as expected for all nodes and all situations.</p>
<aside class="quote no-group" data-username="DIV" data-post="6" data-topic="20484">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/div/48/12816_2.png" class="avatar"> DIV:</div>
<blockquote>
<p>Are you contemplating that it would even be keeping track of zoom/pan along with rotation in 3D port and slice number selection in slice viewports?</p>
</blockquote>
</aside>
<p>Slicer’s undo infrastructure is configurable so that you can choose what to include or exclude. We had projects where including view parameters in the undo history was a requirement, but for the reasons that you described I agree that in general it is better to exclude them.</p>

---

## Post #8 by @DIV (2021-11-24 06:43 UTC)

<p>An issue has been created at <a href="https://github.com/Slicer/Slicer/issues/6038" class="inline-onebox" rel="noopener nofollow ugc">Add ability to safely release unintentionally dragged handle · Issue #6038 · Slicer/Slicer · GitHub</a> .</p>

---
