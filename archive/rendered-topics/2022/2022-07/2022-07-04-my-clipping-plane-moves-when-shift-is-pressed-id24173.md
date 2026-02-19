---
topic_id: 24173
title: "My Clipping Plane Moves When Shift Is Pressed"
date: 2022-07-04
url: https://discourse.slicer.org/t/24173
---

# My clipping plane moves when shift is pressed

**Topic ID**: 24173
**Date**: 2022-07-04
**URL**: https://discourse.slicer.org/t/my-clipping-plane-moves-when-shift-is-pressed/24173

---

## Post #1 by @Niels (2022-07-04 20:19 UTC)

<p>For my module i am moving my mouse on the surface of a 3D model while holding shift (to get the surface coordinates)</p>
<p>But when I define a clipping plane on my model the clipping plane is moved/updated then doing this.</p>
<p>I expected to have the clipping plane stay at the location I have positioned it to.<br>
Can I disable this behaviour?</p>

---

## Post #2 by @lassoan (2022-07-04 22:34 UTC)

<p>The default behavior is that the cursor moves slices. You can disable it using the cursor button on the toolbar by choosing the <code>No jump slices</code> option:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8e5fb51ec0e9d3fd620a881b57d8bdbef2632f7b.png" data-download-href="/uploads/short-url/kjuQTCbDqEJrHb5nGsuH6EMYcBR.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8e5fb51ec0e9d3fd620a881b57d8bdbef2632f7b.png" alt="image" data-base62-sha1="kjuQTCbDqEJrHb5nGsuH6EMYcBR" width="393" height="500" data-dominant-color="353538"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">452×575 17.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
