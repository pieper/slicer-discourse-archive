---
topic_id: 46214
title: "Scissor Tool Not Working"
date: 2026-02-18
url: https://discourse.slicer.org/t/46214
---

# Scissor Tool Not Working

**Topic ID**: 46214
**Date**: 2026-02-18
**URL**: https://discourse.slicer.org/t/scissor-tool-not-working/46214

---

## Post #1 by @jjjooosssiiieee (2026-02-18 17:26 UTC)

<p>I have a university project due tomorrow and am in need of URGENT HELP. I am creating images of mouse organs however once i find my organ i must use the scissor tool to cut away the excess however it is not working. I’ve tried everything i’ve seen online to get it to work and it won’t. I am using version5.10.0. A picture is bellow:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c85a54a8a80d09a6b3054a4f47fd5041f8395e1d.jpeg" data-download-href="/uploads/short-url/sAp1EHPvMNsdcewqhZsK1JrYztr.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c85a54a8a80d09a6b3054a4f47fd5041f8395e1d_2_666x500.jpeg" alt="image" data-base62-sha1="sAp1EHPvMNsdcewqhZsK1JrYztr" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c85a54a8a80d09a6b3054a4f47fd5041f8395e1d_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c85a54a8a80d09a6b3054a4f47fd5041f8395e1d_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c85a54a8a80d09a6b3054a4f47fd5041f8395e1d_2_1332x1000.jpeg 2x" data-dominant-color="8B8986"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1440 560 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @Academy.XRM (2026-02-18 17:50 UTC)

<p>(post deleted by author)</p>

---

## Post #3 by @muratmaga (2026-02-18 18:00 UTC)

<aside class="quote no-group" data-username="jjjooosssiiieee" data-post="1" data-topic="46214">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/3be4f8/48.png" class="avatar"> jjjooosssiiieee:</div>
<blockquote>
<p>I’ve tried everything i’ve seen online to get it to work and it won’t</p>
</blockquote>
</aside>
<p>Image on your 3D view is a volume rendering. Scissors will not function with volume rendering. Turn off your Volume Rendering. Hit Show 3D button in Segment Editor, then try the scissors tool (it works perfectly fine in 5.10)</p>

---

## Post #4 by @lassoan (2026-02-18 22:16 UTC)

<p>If your goal is to remove parts of the image (imaging cradle, other hardware, etc.) then you can apply the Scissor effect result to the image using the <code>Mask Volume</code> effect.</p>
<div class="youtube-onebox lazy-video-container" data-video-id="xZwyW6SaoM4" data-video-title="New &quot;Surface cut&quot; and &quot;Mask volume&quot; tools for 3D Slicer segment editor" data-video-start-time="181" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=xZwyW6SaoM4&amp;t=181" target="_blank" class="video-thumbnail" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/xZwyW6SaoM4/maxresdefault.jpg" title="New &quot;Surface cut&quot; and &quot;Mask volume&quot; tools for 3D Slicer segment editor" width="690" height="388">
  </a>
</div>


---
