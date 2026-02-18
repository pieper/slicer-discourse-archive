# Zoom out camera automatically to fit in the segment, how?

**Topic ID**: 17716
**Date**: 2021-05-20
**URL**: https://discourse.slicer.org/t/zoom-out-camera-automatically-to-fit-in-the-segment-how/17716

---

## Post #1 by @NoobForSlicer (2021-05-20 20:09 UTC)

<p>I am interested if there is some way to zoom in/out so that each segment whether big or small, fits right away into the view covering let’s say 70% of the viewport.</p>
<p>In other words, not to manually zoom in and out each time.</p>
<p>I hope this was not too weirdly expressed, but yeah the zoom should change so that the segment can be seen right away… instead of constantly zooming in and out to show it…</p>

---

## Post #2 by @lassoan (2021-05-21 04:24 UTC)

<p>You need to implement a custom action for this (that you can put on the toolbar, in a subject hierarchy right-click menu action, and/or bind to a keyboard shortcut). In the implementation you would need to get the bounds of the segment very similarly how the center is computed in <a href="https://github.com/Slicer/Slicer/blob/74412b71d33e5685cc0b1e97888916f5be52c912/Libs/MRML/Core/vtkMRMLSegmentationNode.cxx#L1027-L1135">vtkMRMLSegmentationNode::GetSegmentCenter</a> method.</p>

---

## Post #3 by @NoobForSlicer (2021-05-21 10:40 UTC)

<p>Hm for that I would need programming skills, I will see if someone knows how to do this and could maybe help me in exchange for some money</p>

---

## Post #4 by @mau_igna_06 (2021-05-21 14:19 UTC)

<blockquote>
<p>Hm for that I would need programming skills, I will see if someone knows how to do this and could maybe help me in exchange for some money</p>
</blockquote>
<p>I think I can help you with that. I’ll send you a private message</p>

---

## Post #5 by @NoobForSlicer (2021-05-21 20:14 UTC)

<p>Here I have found bounding box how to get it, is this code useful for me to learn how to do this?</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-size-position-and-orientation-of-each-segment" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-size-position-and-orientation-of-each-segment</a></p>

---

## Post #6 by @NoobForSlicer (2021-05-21 20:14 UTC)

<p>thank you I have replied in the inbox</p>

---

## Post #7 by @lassoan (2021-05-21 20:28 UTC)

<aside class="quote no-group quote-modified" data-username="NoobForSlicer" data-post="5" data-topic="17716" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/noobforslicer/48/10900_2.png" class="avatar"> NoobForSlicer:</div>
<blockquote>
<p>Here I have found bounding box how to get it, is this code useful for me to learn how to do this?</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-size-position-and-orientation-of-each-segment" class="inline-onebox">Script repository — 3D Slicer documentation</a></p>
</blockquote>
</aside>
<p>Yes, this should be usable, too, to get RAS bounds of segments.</p>

---

## Post #8 by @NoobForSlicer (2021-05-22 05:06 UTC)

<p>Well I guess I have to figure out three more tasks:</p>
<ol>
<li>Get slicer to understand the size and the shape of the viewport</li>
<li>Figure out how to call zoom function for red,green and yellow viewports. I found how to do it for the 3d Camera (<a href="https://discourse.slicer.org/t/zoom-in-or-out-via-python-interactor-version-4-8-0-on-mac/2254" class="inline-onebox">Zoom in or out via python interactor version 4.8.0 on MAC</a>). Considering the movement of Camera and zoom in/out in 3D world is signitifcantly different, I suppose different view/zoom in and out methods are used for red,green and yellow viewport.</li>
<li>Zoom in/out to get bounds of segment fit the viewport</li>
</ol>
<p>To get this done correctly, I will have to spend some time</p>
<p>I will be reading more today and tomorrow and in the next week about this, try to figure it out…</p>

---
