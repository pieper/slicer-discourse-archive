---
topic_id: 17528
title: "Export What Is Seen In The Viewport As A Png Shot"
date: 2021-05-08
url: https://discourse.slicer.org/t/17528
---

# Export what is seen in the viewport as a PNG shot?

**Topic ID**: 17528
**Date**: 2021-05-08
**URL**: https://discourse.slicer.org/t/export-what-is-seen-in-the-viewport-as-a-png-shot/17528

---

## Post #1 by @NoobForSlicer (2021-05-08 14:38 UTC)

<p>Is there a way to export one shot of what is seen in the viewport as a PNG image file?</p>
<p>I know I could take a screenshot but it would be really great to have it losless and to have an ability to set the resolution or something…</p>
<p>Not losing quality is the most important thing…<br>
If I zoom in or zoom out, voxels are stretched or shrunk and then PrtScrn takes that what is seen. It can be done good… its just not the best and cleanest approach</p>

---

## Post #2 by @muratmaga (2021-05-08 17:16 UTC)

<p>Enable the capture toolbar (if it is not already there), maximize your slicer window set your views/scene as you want to capture and follow the screenshot below</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2a7480db5ebd183d1e5e7871877df75c98871a5a.png" data-download-href="/uploads/short-url/63zEYZNlrjzJA6JEVS4rRsoTpou.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2a7480db5ebd183d1e5e7871877df75c98871a5a_2_509x499.png" alt="image" data-base62-sha1="63zEYZNlrjzJA6JEVS4rRsoTpou" width="509" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2a7480db5ebd183d1e5e7871877df75c98871a5a_2_509x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2a7480db5ebd183d1e5e7871877df75c98871a5a.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2a7480db5ebd183d1e5e7871877df75c98871a5a.png 2x" data-dominant-color="CBCACD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">564×554 45.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @lassoan (2021-05-10 04:05 UTC)

<p>Content of a view is rendered for display. The content is not maximum quality (bit depth is just 3x8 bit RGB, window/level and various overlaid information are burnt in, the image is interpolated to fit on the screen or zoomed in to show more details.</p>
<p>If all you need is a resliced foreground or background volume then you can use the slice view’s reslice filters as shown in <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#extract-randomly-oriented-slabs-of-given-shape-from-a-volume">this example</a>.</p>

---
