---
topic_id: 44013
title: "Transparent Background In Screen Capture Module"
date: 2025-08-07
url: https://discourse.slicer.org/t/44013
---

# Transparent background in screen capture module

**Topic ID**: 44013
**Date**: 2025-08-07
**URL**: https://discourse.slicer.org/t/transparent-background-in-screen-capture-module/44013

---

## Post #1 by @JaredAmudeo (2025-08-07 20:54 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e8c75786bfc2c9af0df43af0e5927b57d1694415.png" data-download-href="/uploads/short-url/xdfRoqRrrT53FXfmT0cz1FhAIo5.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e8c75786bfc2c9af0df43af0e5927b57d1694415.png" alt="image" data-base62-sha1="xdfRoqRrrT53FXfmT0cz1FhAIo5" width="296" height="500" data-dominant-color="39393A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">621×1046 35.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Hi! Could someone help me? I’m trying to make a simple rotation video in 3D view, but no matter what background color or video format I choose, the video appears with a background, not the transparent background as marked. I have orthographic view enabled.</p>

---

## Post #2 by @muratmaga (2025-08-07 21:23 UTC)

<p>perhaphs the codec you chose to output (H.264) doesn’t support transparency?</p>
<p>A google search suggests that might be the case.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b8cca6b15695559c8cdfbc610532c3131fae4efb.png" data-download-href="/uploads/short-url/qmOjGUCScgS6qcBY8lpURvz6o9d.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b8cca6b15695559c8cdfbc610532c3131fae4efb_2_690x253.png" alt="image" data-base62-sha1="qmOjGUCScgS6qcBY8lpURvz6o9d" width="690" height="253" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b8cca6b15695559c8cdfbc610532c3131fae4efb_2_690x253.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b8cca6b15695559c8cdfbc610532c3131fae4efb.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b8cca6b15695559c8cdfbc610532c3131fae4efb.png 2x" data-dominant-color="DDE0E4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">804×295 68.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Instead export them as individual images and check whether the background is indeed transparent in the individual files.</p>

---

## Post #3 by @JaredAmudeo (2025-08-09 09:08 UTC)

<p>Using black background and checking transparent background using GIF work!. thanks</p>

---
