# Hollow from inside surface but keep outlet open

**Topic ID**: 16095
**Date**: 2021-02-19
**URL**: https://discourse.slicer.org/t/hollow-from-inside-surface-but-keep-outlet-open/16095

---

## Post #1 by @szhang (2021-02-19 19:09 UTC)

<p>Hello<br>
I have a inner model segment, which can be used as inside surface under “Segment Editor”-&gt;“Hollow”, but how can I keep these outlet still open rather than enclosed? <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b209a53f8805475233fa08310b7bebfd120728b.jpeg" data-download-href="/uploads/short-url/1Ar6pDZ7nofQuNH5HOKYcsIfUIX.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b209a53f8805475233fa08310b7bebfd120728b.jpeg" alt="image" data-base62-sha1="1Ar6pDZ7nofQuNH5HOKYcsIfUIX" width="352" height="500" data-dominant-color="8F8D83"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">359×509 62.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-02-19 19:40 UTC)

<p>When you segment a vessel, it is all just a closed surface, there are no “endpoints” that could be kept open. You can open up branches by using Scissors effect. If you need to process thousands of images or you need to implement a time-constrained workflow where there is no time for manual opening up of vessel endpoints then you can write a small script that uses VMTK extension’s Extract centerline module to automatically detect endpoints and then cuts the mesh (for example, using Dynamic modeler module).</p>

---

## Post #3 by @szhang (2021-02-19 22:57 UTC)

<p>I see, that’s good to know! except I realized the “automatic endpoint detection” get stucked…</p>
<p>At this point, I have obtained another model that properly represent the shape but it is good to know of Dynamic modeler module. Thank you!</p>

---

## Post #4 by @lassoan (2021-02-20 04:27 UTC)

<aside class="quote no-group" data-username="szhang" data-post="3" data-topic="16095">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/bc8723/48.png" class="avatar"> szhang:</div>
<blockquote>
<p>I see, that’s good to know! except I realized the “automatic endpoint detection” get stucked…</p>
</blockquote>
</aside>
<p>I’ve been using the Centerline extraction module for a good while now and have never seen it hanging. I can have a look at what the issue is if you share the segmentation or model node (upload somewhere and post the link).</p>

---
