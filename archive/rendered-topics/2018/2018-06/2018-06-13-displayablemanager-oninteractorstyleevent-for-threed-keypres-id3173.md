---
topic_id: 3173
title: "Displayablemanager Oninteractorstyleevent For Threed Keypres"
date: 2018-06-13
url: https://discourse.slicer.org/t/3173
---

# DisplayableManager ::OnInteractorStyleEvent for ThreeD keypress

**Topic ID**: 3173
**Date**: 2018-06-13
**URL**: https://discourse.slicer.org/t/displayablemanager-oninteractorstyleevent-for-threed-keypress/3173

---

## Post #1 by @ihnorton (2018-06-13 21:49 UTC)

<p>We have a DisplayableManager that implements <a href="https://github.com/SlicerDMRI/SlicerDMRI/blob/master/Modules/Loadable/TractographyDisplay/MRMLDM/vtkMRMLTractographyDisplayDisplayableManager.cxx#L97"><code>::OnInteractorStyleEvent</code></a> to respond to key-presses while the mouse is in the ThreeD render frame. In order to actually receive a callback for these events, it seems that I need to click in the ThreeD render frame first, before pressing a key.</p>
<p>Is there some state I can change in order to receive these events after simply mouse-enter, rather than requiring a click first?</p>
<p>(from what I can tell, the vtkInteractorStyle only raises a callback if it sees an observer for a given event… I tried setting a breakpoint in <code>vtkMRMLAbstractDisplayableManager::vtkInternal::UpdateInteractorStyle</code>, but that bp is not hit when I click in the render window, so I’m not sure where the observer might be added/removed…)</p>

---

## Post #2 by @pieper (2018-06-13 22:07 UTC)

<p>This is a longstanding issue - in the past we changed to focus on mouse enter, but on some platforms that caused the window to raise to the front when you move the mouse over it.</p>
<p>The best solution IMO is to use Qt key bindings to get the events and then sort out which window they belong to.</p>

---

## Post #3 by @lassoan (2018-06-13 22:24 UTC)

<p>I think the main issue is that we don’t show which view is “active”. We could change viewer window border or header to indicate that the view is in focus.</p>
<p>This would be a hint for the user and it could be also used for forwarding unprocessed Qt keypress events to viewers. It could be also useful for specifying view-specific actions (such as “Show in active view”).</p>
<p>There is already an Active attribute for view nodes, I guess that was ported over from Slicer 2 or 3.</p>

---

## Post #4 by @ihnorton (2018-06-14 13:43 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="3173">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>This is a longstanding issue - in the past we changed to focus on mouse enter</p>
</blockquote>
</aside>
<p>Ah, ok, it is driven by the Qt widget keyboard focus. Thanks. (This did feel kind of familiar). For my purposes I think I can just set that manually to the ThreeD view when the user enables this short-term interaction mode, at least to reduce the surprise/confusion.</p>
<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="3173">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>on some platforms that caused the window to raise to the front when you move the mouse over it.</p>
</blockquote>
</aside>
<p>I wonder if this has been fixed in more recent Qt versions, because at least according to the <a href="http://doc.qt.io/qt-5/qwidget.html#setFocus">docs</a>, setFocus is only supposed to apply when the window is active. Or maybe we were accidentally calling <code>raise()</code> somewhere too.</p>

---

## Post #5 by @pieper (2018-06-14 20:09 UTC)

<aside class="quote no-group" data-username="ihnorton" data-post="4" data-topic="3173">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ihnorton/48/9_2.png" class="avatar"> ihnorton:</div>
<blockquote>
<p>I wonder if this has been fixed in more recent Qt versions, because at least according to the <a href="http://doc.qt.io/qt-5/qwidget.html#setFocus">docs</a>, setFocus is only supposed to apply when the window is active. Or maybe we were accidentally calling <code>raise()</code> somewhere too.</p>
</blockquote>
</aside>
<p>It was actually in the pre-Qt days (Tk) and it would happen on linux as I recall and was probably a window manager “feature” that setting the focus on a vtkRenderWindow resulted in raising the parent toplevel window.  This wouldn’t be a problem if the user is already interacting with the app, but if you try dynamically track mouse enter / and leave events so that the correct VTK window gets the focus then it’s a problem because those events happen even if the window isn’t in front.  That’s why I’m suggesting (and Andras too I believe) are suggesting that we could track the mouse to know the active window, but use Qt to get the events globally and pass them to the correct viewer.</p>

---

## Post #6 by @lassoan (2018-06-14 21:01 UTC)

<p>I agree with Steve. We should not change the focus just because the mouse hovers over some window. This would be a huge deviation from how widgets are supposed to be used and it would probably cause many problems.</p>

---

## Post #7 by @ihnorton (2018-06-14 22:01 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="3173">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>We should not change the focus just because the mouse hovers over some window</p>
</blockquote>
</aside>
<p>Definitely not advocating that globally. (I’ve used default Motif enough to strongly dislike that interaction style <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20">)</p>
<p>Setting focus myself on a one-off basis after the users clicks the mode checkbox should be sufficient. Thanks.</p>

---
