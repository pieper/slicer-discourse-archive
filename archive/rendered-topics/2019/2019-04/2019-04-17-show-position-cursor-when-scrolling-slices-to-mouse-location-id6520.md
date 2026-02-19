---
topic_id: 6520
title: "Show Position Cursor When Scrolling Slices To Mouse Location"
date: 2019-04-17
url: https://discourse.slicer.org/t/6520
---

# Show position cursor when scrolling slices to mouse location

**Topic ID**: 6520
**Date**: 2019-04-17
**URL**: https://discourse.slicer.org/t/show-position-cursor-when-scrolling-slices-to-mouse-location/6520

---

## Post #1 by @Leon (2019-04-17 08:13 UTC)

<p>Hi,</p>
<p>When you press ‘shift’ and hover the cursor/mouse over a slice, Slicer automatically updates the mouse location in all the other slices, including the 3D-view. But unfortunately I can’tsee the exact position of the cursor these other slices. I need this option to, for instance, check small structures in the different slices.</p>
<p>Is there a way to make the cursor position visible by means of a markerlike a cross, dot, or whatever?</p>
<p>Regards,<br>
Léon</p>

---

## Post #2 by @Leon (2019-04-17 08:30 UTC)

<p>Maybe some additional information; I’m want to hover over structures in the 3D-view to see what these look like in the 3 other planes.</p>
<p>I noticed that, when for instance using the paintbrush in the segmentation editor, you can see the position of the brush in the other slices and 3D-view as a circle or stripe, but if you want to zoom in on this in one of the other slices, it’s not possible for it goes away.</p>
<p>Can I keep the position visible after hovering?</p>

---

## Post #3 by @Leon (2019-04-17 12:00 UTC)

<p>I’ve found a workaround.<br>
When I turn on ‘Edit in 3D views’ my cursor is visible in the 3D view, as well as in the other slices as a ball. Now I can edit the segmentation, although with the 3D view on, my system slows down very much.</p>
<p>Is this the way it should be done, or is there some other way that’s more convinient?</p>

---

## Post #4 by @pieper (2019-04-17 14:12 UTC)

<p>Sounds like you could use the Crosshairs:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.10/SlicerApplication/MouseandKeyboardShortcuts#Crosshairs" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/4.10/SlicerApplication/MouseandKeyboardShortcuts#Crosshairs</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf58384d98d00eeb5570a1e57ae164725b9bb904.png" data-download-href="/uploads/short-url/riIcQrPrff8OynBIgUhM6krOFKs.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf58384d98d00eeb5570a1e57ae164725b9bb904_2_690x317.png" alt="image" data-base62-sha1="riIcQrPrff8OynBIgUhM6krOFKs" width="690" height="317" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf58384d98d00eeb5570a1e57ae164725b9bb904_2_690x317.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf58384d98d00eeb5570a1e57ae164725b9bb904_2_1035x475.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf58384d98d00eeb5570a1e57ae164725b9bb904_2_1380x634.png 2x" data-dominant-color="605D66"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1388×638 208 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @roozbehshams (2019-04-17 14:24 UTC)

<p>This is a bit off topic but is there a way to do the same but without holding the shift key? It would be easier to go through volumes inspecting them without constantly holding the shift key.</p>

---

## Post #6 by @lassoan (2019-04-17 15:59 UTC)

<p>In recent Slicer nightly versions all the keyboard and mouse gestures can be remapped to any actions, so it would be easy to change this (and at some point we may even expose this feature to users). However, it is not clear for me, what would you find easier than holding down Shift key while moving the mouse?</p>

---

## Post #7 by @roozbehshams (2019-04-17 16:38 UTC)

<p>I know this is situational, but it was something I was looking into as a small UX improvement. Instead of hold shift to follow, it would be press shift to toggle follow/unfollow. or some other button, even a UI button.</p>
<p>In our case it would be to verify registration, to have moving and fixed volume side by side and scroll through it with the cross-hair. This would reduce keyboard interactions in the OR.</p>

---

## Post #8 by @lassoan (2019-04-17 17:20 UTC)

<aside class="quote no-group" data-username="roozbehshams" data-post="7" data-topic="6520">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/roozbehshams/48/1544_2.png" class="avatar"> roozbehshams:</div>
<blockquote>
<p>In our case it would be to verify registration, to have moving and fixed volume side by side and scroll through it with the cross-hair. This would reduce keyboard interactions in the OR.</p>
</blockquote>
</aside>
<p>There are so many other way of doing this. For example, have you tried “Compare Volumes” module? You may find “Layer Reveal Cursor” particularly useful.</p>
<p>You can also add custom code to move the crosshair whenever the cursor is moved and activate/deactivate with a shortcut (probably less than 10 lines of code in total).</p>

---

## Post #9 by @roozbehshams (2019-04-17 17:39 UTC)

<p>Yes I’ve that, it looked interesting.</p>
<p>Thanks, I’ll look into it, I wanted to see if there’s an established way of doing this or not; should be easy enough to do.</p>
<p>PS. Sorry for hijacking this thread for a while <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #10 by @Leon (2019-04-18 05:48 UTC)

<p><span class="mention">@Steve</span>.<br>
Yes, that’s exactly what I meant!<br>
I also ‘discovered’ this myself this morning, even before I checked the forum. All the times it was right there without me noticing it.</p>

---
