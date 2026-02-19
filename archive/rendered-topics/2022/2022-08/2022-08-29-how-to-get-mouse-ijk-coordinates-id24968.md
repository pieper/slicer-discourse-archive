---
topic_id: 24968
title: "How To Get Mouse Ijk Coordinates"
date: 2022-08-29
url: https://discourse.slicer.org/t/24968
---

# How to get mouse IJK coordinates?

**Topic ID**: 24968
**Date**: 2022-08-29
**URL**: https://discourse.slicer.org/t/how-to-get-mouse-ijk-coordinates/24968

---

## Post #1 by @sunshine (2022-08-29 03:27 UTC)

<p>Hi everyone,</p>
<p>I am trying to write my first module using MarkUp PointList. And I would like to use a label in UI to show the real-time mouse position, both RAS and IJK, just like the screenshot below.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/76894bdfb765f78d838f9b07fc7b4932422a79b9.png" data-download-href="/uploads/short-url/gUCuQZgLXXxrysCKL8zY82lOcRP.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/76894bdfb765f78d838f9b07fc7b4932422a79b9_2_690x303.png" alt="image" data-base62-sha1="gUCuQZgLXXxrysCKL8zY82lOcRP" width="690" height="303" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/76894bdfb765f78d838f9b07fc7b4932422a79b9_2_690x303.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/76894bdfb765f78d838f9b07fc7b4932422a79b9_2_1035x454.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/76894bdfb765f78d838f9b07fc7b4932422a79b9.png 2x" data-dominant-color="999898"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1043×459 26.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I found the RAS coordinates using</p>
<pre><code class="lang-auto">crosshairNode.GetCursorPositionRAS(ras)
</code></pre>
<p>What are the functions I should use to retrieve the mouse IJK coordinates?</p>
<p>Thank you very much in advance!</p>

---

## Post #2 by @lassoan (2022-08-29 03:44 UTC)

<p>The DataProbe is implemented in Python, so you can copy-paste the code snippet that computes voxel coordinates from slice XYZ - see <a href="https://github.com/Slicer/Slicer/blob/8fb7ade53e7e4bbb68aea6cb28ef62920d1edcdc/Modules/Scripted/DataProbe/DataProbe.py#L191-L255">here</a>.</p>

---
