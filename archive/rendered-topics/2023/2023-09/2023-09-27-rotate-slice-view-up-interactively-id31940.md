---
topic_id: 31940
title: "Rotate Slice View Up Interactively"
date: 2023-09-27
url: https://discourse.slicer.org/t/31940
---

# Rotate slice view up interactively

**Topic ID**: 31940
**Date**: 2023-09-27
**URL**: https://discourse.slicer.org/t/rotate-slice-view-up-interactively/31940

---

## Post #1 by @mikebind (2023-09-27 21:45 UTC)

<p>I would like to allow a user to interactively rotate the slice view up direction, similar to how the Ctrl-Alt-Left Drag shortcut allows rotation of lined slice planes, but in this case rotating only the clicked-on slice view, and only within its current plane, about it’s current center.  I think the actual reorientation can be handled pretty easily using <code>SetSliceToRASByNTP()</code>, by keeping the same slice normal and position and varying the ‘T’ vector to set the transverse vector orientation, but I am having trouble figuring out how to implement the click-and-drag functionality.  I want users to be able to hold down a shortcut (say Ctrl-R for example), and then left click and drag on a slice view.  The view should then interactively rotate as the user drags, with the amount of rotation obtained by the angle formed between the line segments connecting the slice center and the the initial click location (the start of the drag) and connecting the slice center and the current mouse location.  I gather that I will need to do something like <code>SetEventTranslationClickAndDrag</code> on some widget (a slice view manager of some kind?), but from the examples I can find (like <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository/gui.html#customize-keyboard-mouse-gestures-in-viewers" rel="noopener nofollow ugc">these</a>), I can’t tell what all the inputs are and how to define the callbacks.  If anyone can provide a little guidance to get me started, I would appreciate it. Thanks!</p>

---

## Post #2 by @pieper (2023-09-27 21:53 UTC)

<p>Handling interactions at the mouse event level is doable, but can be tricky since you need to worry about interaction with other things like segment edtior effects, widgets, mouse modes, etc.  You might be better to add this as a feature to the existing interactive slice planes.  Or make changing the orientation of the slice planes a byproduct of manipulating a markups line or something that already manages mouse behaviors.</p>

---

## Post #3 by @mikebind (2023-09-27 22:12 UTC)

<p>I’d be fine with using a markups point in something like the following way:  Pressing Control-R activates this functionality by creating a set of markups points which is to the right of center in each slice view (since I no longer have any guide for which slice view the user wants to rotate), and then grabbing and moving that point results in rotating that view in plane about its current center.  Then pressing Control-R again removes the created markups points.   I’ll try to get this working.  It does sound simpler than working with mouse events at a lower level, and would still provide the functionality in a pretty straightforward way. Thanks for the suggestion <a class="mention" href="/u/pieper">@pieper</a>, if I get it working I’ll post back here.</p>

---

## Post #4 by @lassoan (2023-09-28 02:18 UTC)

<p>You can also use Reformat module’s Rotation / In-Plane slider. This is what we do in SlicerHeart to align slice view to a valve axis (using two sliders) and nobody is complaining.</p>
<p>If you are not allowed to use a slider then you can add a new widget action to vtkMRMLSliceIntersectionWidget that rotates the current slice (instead of rotating theintersecting slices). You can then map a new widget event (e.g., click-and-drag with some keyboard modifiers) or remap a widget event that you don’t need to do slice rotation. It should be all very straightforward and about 20-30 new lines of code in total.</p>
<p>Another option is to use a markup plane to specify a direction in 3D (you can drag-and-drop and rotate the plane in all the slice and 3D views). When the plane is in good orientation then you can automatically align all the views.</p>
<p>I would also consider doing this fully automatically. Most likely you can use an existing AI model to segment some structures that you can use to determine the anatomical axis directions, or you can train a new model to recognize axis directions.</p>

---

## Post #5 by @mikebind (2023-09-28 05:15 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a> for the ideas.  I actually already use an automatic approach to anatomical orientation (<a href="https://discourse.slicer.org/t/rotate-reformat-slice-view-in-plane/8127/6" class="inline-onebox">Rotate reformat slice view (in plane) - #6 by mikebind</a>) which works very well most of the time.  However, sometimes, for very oblique views, it would actually be better to use some sort of custom rotation, and I’d like to give myself and other users the option to rotate as easily as we can reslice.  This would also be helpful sometimes when, for example, a patient’s head is turned a bit to one side relative to the image volume axes, and it would be nicer just to rotate the axial view in plane so that anterior for the patient is up on the slice view.  This could be accomplished in automated ways or interactive ways of varying complexity, but when it’s just for the aesthetics of screenshots, I’d love to have an easy way to just rotate the view.   The Reformat module in my Slicer doesn’t have a Rotation/In-Plane slider; I see that newer versions do. I have been stuck on 5.2.1 for a while because updates to the Elastix module broke some of my code in &gt;5.2.1 and I haven’t dug into why yet (I don’t think it will be a difficult fix, I just haven’t gotten around to it yet, and I haven’t had a strong enough reason that I needed to update Slicer yet either).  This might now be enough of a reason.</p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="31940">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>you can add a new widget action to vtkMRMLSliceIntersectionWidget that rotates the current slice (instead of rotating theintersecting slices). You can then map a new widget event (e.g., click-and-drag with some keyboard modifiers) or remap a widget event that you don’t need to do slice rotation. It should be all very straightforward and about 20-30 new lines of code in total.</p>
</blockquote>
</aside>
<p>Is this something I can do in python or would it require building Slicer from source?</p>

---

## Post #6 by @lassoan (2023-09-28 11:37 UTC)

<p>You can remap what keyboard/mouse gesture is mapped to what widget action in Python but your can only add new widget action  C++. The feature would be added to Slicer core.</p>

---
