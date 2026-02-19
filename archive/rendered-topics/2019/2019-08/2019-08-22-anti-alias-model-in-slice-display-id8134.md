---
topic_id: 8134
title: "Anti Alias Model In Slice Display"
date: 2019-08-22
url: https://discourse.slicer.org/t/8134
---

# Anti Alias Model in Slice Display

**Topic ID**: 8134
**Date**: 2019-08-22
**URL**: https://discourse.slicer.org/t/anti-alias-model-in-slice-display/8134

---

## Post #1 by @burnhamd (2019-08-22 21:09 UTC)

<p>I have a 3d model of a tool, which looks quite good in the 3D display, however the projection and intersectional views on the slice displays are pretty ugly as it seems the projections are not anti-aliased.  Is there a way to do this antialiasing?</p>
<p>If not can you point me to how I can display my own 2d image on the viewer and I will simply modify the image based on the transformation of the tool?</p>

---

## Post #2 by @lassoan (2019-08-23 03:24 UTC)

<aside class="quote no-group" data-username="burnhamd" data-post="1" data-topic="8134">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/5fc32e/48.png" class="avatar"> burnhamd:</div>
<blockquote>
<p>I have a 3d model of a tool, which looks quite good in the 3D display, however the projection and intersectional views on the slice displays are pretty ugly as it seems the projections are not anti-aliased. Is there a way to do this antialiasing?</p>
</blockquote>
</aside>
<p>It is not clear for me what do you mean by “pretty ugly”. No anti-aliasing is used in either 2D or 3D views. Can you attach a screenshot?</p>
<aside class="quote no-group" data-username="burnhamd" data-post="1" data-topic="8134">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/5fc32e/48.png" class="avatar"> burnhamd:</div>
<blockquote>
<p>how I can display my own 2d image on the viewer</p>
</blockquote>
</aside>
<p>You can load any image and show it in the slice viewers, but using this to display model/slice intersection does not sound like a good approach.</p>

---
