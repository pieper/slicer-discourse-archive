# How to create sphere-shaped segment?

**Topic ID**: 26968
**Date**: 2022-12-29
**URL**: https://discourse.slicer.org/t/how-to-create-sphere-shaped-segment/26968

---

## Post #1 by @akmal871026 (2022-12-29 02:11 UTC)

<p>Dear Sir,</p>
<p>I want to create an ROI sphere in my image so that I can get the counts in ROI created.</p>
<p>This means that I can adjustable the sphere volume due to radius or something else.</p>
<p>Does any extension have it?</p>

---

## Post #2 by @jamesobutler (2022-12-29 04:47 UTC)

<p>The “Paint” Segment Editor effect has a sphere mode where you can set the size of the sphere. Then you can get the statistics of this sphere using the Segment Statistics module.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#paint" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#paint</a></p>

---

## Post #3 by @akmal871026 (2022-12-30 16:14 UTC)

<p>But, the diameter is in %. I don’t know the value in mm of the diameter.</p>
<p>What I want is can set the diameter of the sphere to 37mm and so on.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0ded5c2a9518a2ca1bf8eca2bf2d67df06f7b9c4.jpeg" data-download-href="/uploads/short-url/1ZcKpHWvtQkNXNqfIReAqyeVHnK.jpeg?dl=1" title="WhatsApp Image 2022-12-31 at 12.10.44 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0ded5c2a9518a2ca1bf8eca2bf2d67df06f7b9c4_2_388x500.jpeg" alt="WhatsApp Image 2022-12-31 at 12.10.44 AM" data-base62-sha1="1ZcKpHWvtQkNXNqfIReAqyeVHnK" width="388" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0ded5c2a9518a2ca1bf8eca2bf2d67df06f7b9c4_2_388x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0ded5c2a9518a2ca1bf8eca2bf2d67df06f7b9c4.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0ded5c2a9518a2ca1bf8eca2bf2d67df06f7b9c4.jpeg 2x" data-dominant-color="F3F4F5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">WhatsApp Image 2022-12-31 at 12.10.44 AM</span><span class="informations">445×572 42.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @muratmaga (2022-12-30 19:17 UTC)

<aside class="quote no-group" data-username="akmal871026" data-post="3" data-topic="26968">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/akmal871026/48/11642_2.png" class="avatar"> akmal871026:</div>
<blockquote>
<p>the diameter is in %.</p>
</blockquote>
</aside>
<p>Click the % button on the right to switch to mm.</p>

---

## Post #5 by @akmal871026 (2022-12-31 12:09 UTC)

<p>Thank you very much for your reply</p>

---
