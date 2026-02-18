# Apply Transforms in only 1 segment

**Topic ID**: 32804
**Date**: 2023-11-14
**URL**: https://discourse.slicer.org/t/apply-transforms-in-only-1-segment/32804

---

## Post #1 by @SANTIAGO_PENDON_MING (2023-11-14 10:13 UTC)

<p>Hi to everyone <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>In this case I’m struggling with transformations and Segmentations. The problem is the following one:</p>
<p>-I’m trying to apply by code a linear transformation to a specific segment contained in a segmentation with more than one segment.</p>
<p>As far as I know, transforms module only allows apply transformations to segmentation nodes.</p>
<p>Can I transform only one segment?</p>
<p>Thanks a lot.</p>

---

## Post #2 by @pieper (2023-11-14 13:23 UTC)

<aside class="quote no-group" data-username="SANTIAGO_PENDON_MING" data-post="1" data-topic="32804">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/santiago_pendon_ming/48/66060_2.png" class="avatar"> SANTIAGO_PENDON_MING:</div>
<blockquote>
<p>Can I transform only one segment?</p>
</blockquote>
</aside>
<p>No, you would need to move it to a new segmentation, apply the transform, and then move it back.</p>

---
