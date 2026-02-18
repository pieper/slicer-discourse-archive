# Change the size of interaction handles programmatically

**Topic ID**: 24889
**Date**: 2022-08-23
**URL**: https://discourse.slicer.org/t/change-the-size-of-interaction-handles-programmatically/24889

---

## Post #1 by @seanchoi0519 (2022-08-23 17:04 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/1868f96b3ab0634e7bf1f8776f73b5c3a6e73e2e.jpeg" data-download-href="/uploads/short-url/3tWmFEBHh5VeVr9P2qLBKdTtix0.jpeg?dl=1" title="Screen Shot 2022-08-24 at 3.02.57 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/1868f96b3ab0634e7bf1f8776f73b5c3a6e73e2e_2_640x500.jpeg" alt="Screen Shot 2022-08-24 at 3.02.57 AM" data-base62-sha1="3tWmFEBHh5VeVr9P2qLBKdTtix0" width="640" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/1868f96b3ab0634e7bf1f8776f73b5c3a6e73e2e_2_640x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/1868f96b3ab0634e7bf1f8776f73b5c3a6e73e2e_2_960x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/1868f96b3ab0634e7bf1f8776f73b5c3a6e73e2e_2_1280x1000.jpeg 2x" data-dominant-color="B7BEB2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2022-08-24 at 3.02.57 AM</span><span class="informations">1314×1026 236 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Hello, would there be a way to reduce the size of these interaction handles via python programmatically?</p>
<p>Thanks a lot</p>

---

## Post #2 by @seanchoi0519 (2022-08-23 17:05 UTC)

<p>Better yet, would it be possible to make the interaction handles appear only<br>
when I click on the plane node?</p>
<p>Thanks a lot</p>

---

## Post #3 by @Sunderlandkyl (2022-08-23 17:10 UTC)

<p>The code to change the interaction handle size is:</p>
<pre data-code-wrap="python"><code class="lang-python">getNode("P").GetDisplayNode().SetInteractionHandleScale(1.0)
</code></pre>
<aside class="quote no-group" data-username="seanchoi0519" data-post="2" data-topic="24889">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/seanchoi0519/48/10354_2.png" class="avatar"> seanchoi0519:</div>
<blockquote>
<p>Better yet, would it be possible to make the interaction handles appear only<br>
when I click on the plane node?</p>
</blockquote>
</aside>
<p>I’m currently working on a node “Focus” improvement that adds this exact feature. No ETA at this time.</p>

---
