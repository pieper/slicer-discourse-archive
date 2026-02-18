# crop volume problem

**Topic ID**: 7316
**Date**: 2019-06-26
**URL**: https://discourse.slicer.org/t/crop-volume-problem/7316

---

## Post #1 by @mertdurdagi (2019-06-26 14:44 UTC)

<p>Hello there,</p>
<p>When I am done with volume rendering, to create a cropped sub volume, I used crop volume. It works in other computers but in my pc, it does create a new sub volume but it does not show the cropped segments. This is why, I cannot edit afterwards. If this is a problem sourced by the path of the application (maybe because of a special character), could you help me about how to get rid of that?</p>

---

## Post #2 by @lassoan (2019-06-27 05:00 UTC)

<aside class="quote no-group" data-username="mertdurdagi" data-post="1" data-topic="7316">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/bbe5ce/48.png" class="avatar"> mertdurdagi:</div>
<blockquote>
<p>it does create a new sub volume but it does not show the cropped segments</p>
</blockquote>
</aside>
<p>What cropped segments you would expect to see? Could you attach a screenshot and explain on that where you expect to see what?</p>
<aside class="quote no-group" data-username="mertdurdagi" data-post="1" data-topic="7316">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/bbe5ce/48.png" class="avatar"> mertdurdagi:</div>
<blockquote>
<p>This is why, I cannot edit afterwards</p>
</blockquote>
</aside>
<p>What would you like to edit?</p>

---

## Post #3 by @mertdurdagi (2019-07-02 10:07 UTC)

<p>I figured it out. The problem is really the path. When your username in your PC has a special letter, the 3D Slicer cannot understand what it is and the path seems wrong. This is why, the process cannot be completed. By creating another user in the computer, the problem can be solved.</p>

---
