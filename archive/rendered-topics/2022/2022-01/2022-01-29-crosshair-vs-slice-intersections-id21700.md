---
topic_id: 21700
title: "Crosshair Vs Slice Intersections"
date: 2022-01-29
url: https://discourse.slicer.org/t/21700
---

# Crosshair vs Slice Intersections

**Topic ID**: 21700
**Date**: 2022-01-29
**URL**: https://discourse.slicer.org/t/crosshair-vs-slice-intersections/21700

---

## Post #1 by @jamesobutler (2022-01-29 21:16 UTC)

<p>What is the difference between the “Crosshair” versus using “Slice Intersections”? They seem to be the same type thing, but they are two different objects so it is a bit confusing about which one to use.</p>
<p>There is the Crosshair toolbar where the default action for the QToolButton toggles the visibility of the Crosshair. However I see more recommendations for users to turn on Slice Intersections which is a menu option buried at the bottom of the menu in the Crosshair toolbar. There is also a checkbox in the Markups module for turning on Slice Intersections. So it seems that Slice Intersections is the preferred option, but is not the default action of the QToolButton in the Crosshair toolbar.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/90c22ba873ac86a2a4e0ca35eb54b981e273e4f4.png" data-download-href="/uploads/short-url/kEALnBIpoziBoQxF5LuvHPXrC6M.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/90c22ba873ac86a2a4e0ca35eb54b981e273e4f4_2_690x369.png" alt="image" data-base62-sha1="kEALnBIpoziBoQxF5LuvHPXrC6M" width="690" height="369" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/90c22ba873ac86a2a4e0ca35eb54b981e273e4f4_2_690x369.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/90c22ba873ac86a2a4e0ca35eb54b981e273e4f4_2_1035x553.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/90c22ba873ac86a2a4e0ca35eb54b981e273e4f4_2_1380x738.png 2x" data-dominant-color="97969A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1918×1026 335 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @jamesobutler (2022-01-29 21:22 UTC)

<p>In my Slicer custom application I already make the modification to make Slice Intersection the default action for the QToolButton, but I still don’t quite understand the difference of when to use Crosshair vs Slice Intersections.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/143644ef6afd3fc97cfe55f57cc6020110795eb1.png" alt="image" data-base62-sha1="2SNOT9Wtvkietkah6Ohz5sgFRZv" width="273" height="353"></p>

---

## Post #3 by @pll_llq (2022-01-30 14:48 UTC)

<p>I’ve tried slice intersections in yesterday’s nightly and it seems that <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#turn-on-slice-intersections" rel="noopener nofollow ugc">this snippet</a> doesn’t work any more so I moved to using crosshair</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f91c07aea9020fbeb1bc199e5d9218cc5c3144d.png" data-download-href="/uploads/short-url/icwUsJmry1xSEEsIr2tryD6AXNz.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f91c07aea9020fbeb1bc199e5d9218cc5c3144d_2_690x123.png" alt="image" data-base62-sha1="icwUsJmry1xSEEsIr2tryD6AXNz" width="690" height="123" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f91c07aea9020fbeb1bc199e5d9218cc5c3144d_2_690x123.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f91c07aea9020fbeb1bc199e5d9218cc5c3144d_2_1035x184.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f91c07aea9020fbeb1bc199e5d9218cc5c3144d.png 2x" data-dominant-color="3A3640"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1232×220 39.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @cpinter (2022-01-31 14:02 UTC)

<p><a class="mention" href="/u/pll_llq">@pll_llq</a> Good catch! This is the correct snippet now:</p>
<pre><code class="lang-auto">sliceDisplayNodes = slicer.util.getNodesByClass("vtkMRMLSliceDisplayNode")
for sliceDisplayNode in sliceDisplayNodes:
  sliceDisplayNode.SetIntersectingSlicesVisibility(1)
</code></pre>
<p>We’ll update it in the doc.</p>

---

## Post #5 by @cpinter (2022-01-31 14:06 UTC)

<p>To reflect on the actual topic, I have a hard time finding a usage for the crosshair too. It is a singleton, and so there is a single crosshair in the application, sort of like a “current point of interest” as I interpret it. The one thing I can think of where crosshair is more than slice intersections is that it is visible in 3D. Maybe we should add a checkbox for slice intersection visiblity in 3D and get rid of crosshairs altogether?</p>

---

## Post #6 by @pieper (2022-01-31 22:12 UTC)

<p>I do think these are two distinct concepts:</p>
<ul>
<li>
<p>crosshair is a single point in space</p>
</li>
<li>
<p>slice intersections show where other slices are located on a slice view</p>
</li>
</ul>
<p>There’s no reason to assume that the slices intersect or are orthogonal.  Or that there are only two other slices to display in a given slice view.  It can be useful to show the current crosshair even when it doesn’t crosshair even when it doesn’t reflect the current slice location.  E.g. use shift-mousemove to position the slices and crosshair pick a reference point in 3D.  Then use the slider to scroll the slices and crosshair stays at reference point and doesn’t follow, which can be handy.</p>

---

## Post #7 by @jamesobutler (2022-01-31 22:42 UTC)

<p>Is “Crosshair” then similar to my action of me dropping a control point of a Point List which represents a single point in space to mark a reference point and which I can click on to jump slice offsets to quickly get back to my reference point?</p>

---

## Post #8 by @pieper (2022-01-31 22:54 UTC)

<p>Yes, but more transient and without requiring you to delete the point to cleanup.</p>

---

## Post #9 by @jamesobutler (2022-01-31 23:26 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> If you think crosshair usage and slice intersection usage are two distinct concepts, do you think these two things should be separated in the GUI? They are currently in the same QToolButton menu as part of the “Crosshair Selection” toolbar. Should their options be in the same toolbar, but in their own QToolButton (and own menu)? Or are they distinct enough to warrant separate ToolBars where you could hide one of these toolbars, yet still see the other?</p>

---

## Post #10 by @pieper (2022-02-01 00:05 UTC)

<p>I don’t have a strong position on this, I just wanted to point out that yes, they are different.  I think they were just added on the same toolbar menu to save space and because they are somewhat similar.  Now that there’s more functionality in the slice intersections maybe they should have a more independent place.</p>

---

## Post #11 by @DIV (2022-02-02 05:42 UTC)

<aside class="quote no-group" data-username="pieper" data-post="6" data-topic="21700">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>E.g. use shift-mousemove to position the slices and crosshair pick a reference point in 3D.</p>
</blockquote>
</aside>
<p>I sometimes follow a procedure a bit like that.  But then if I’ve zoomed in on (say) Slice <code>Y</code> to one location, then then move (through <code>Shift</code>+mouse-move on the 3D view or a different Slice) the cross-hairs to a new location, I get frustrated that the point will often be outside of the current FoV for Slice <code>Y</code>.  That means I either need to</p>
<ul>
<li>zoom back out until I can identify the new location, pan to ~centre on the new location, and zoom back in (tedious, and typically resulting in a zoom that isn’t precisely the same as the original zoom);  or</li>
<li>progressively pan to where I ‘think’ the new location roughly is (tedious if the new location is far outside the current FoV, so that many mouse drags are required, and I might not immediately head in quite the right direction).</li>
</ul>
<aside class="quote no-group" data-username="jamesobutler" data-post="7" data-topic="21700" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Is “Crosshair” then similar to my action of me dropping a control point of a Point List which represents a single point in space to mark a reference point and which I can click on to jump slice offsets to quickly get back to my reference point?</p>
</blockquote>
</aside>
<p>So is there an existing functionality that I’m missing to centre the Slices and/or 3D view on either the current cross-hairs or the current intersection — either while they are being modified (instantaneously &amp; automatically)† or afterwards (upon user request), without modifying the respective zoom levels?</p>
<p>—DIV</p>
<p>† In this case, the centring wouldn’t/couldn’t be implemented on the pane in which the mouse is being controlled.</p>

---
