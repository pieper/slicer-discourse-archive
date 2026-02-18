# How can I view displacement field in 3D?

**Topic ID**: 29228
**Date**: 2023-05-01
**URL**: https://discourse.slicer.org/t/how-can-i-view-displacement-field-in-3d/29228

---

## Post #1 by @Luna (2023-05-01 13:38 UTC)

<p>I have two questions</p>
<ol>
<li>I have an nrrd file of my displacement field in 3D which I want to view. I managed to view it in 2D in transforms module but I couldn’t find a way to view it in 3D. How can I view it in 3D?</li>
<li>Is there a way to view the displacement field in glyphs not for every pixel but for example every 20 or 40 pixels?</li>
</ol>

---

## Post #2 by @lassoan (2023-05-01 22:29 UTC)

<aside class="quote no-group" data-username="Luna" data-post="1" data-topic="29228">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/luna/48/11116_2.png" class="avatar"> Luna:</div>
<blockquote>
<p>I have an nrrd file of my displacement field in 3D which I want to view. I managed to view it in 2D in transforms module but I couldn’t find a way to view it in 3D. How can I view it in 3D?</p>
</blockquote>
</aside>
<p>When you load the displacement field, choose “Transform” in the description column. You can then use <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html#display">transform visualization to view the displacement field</a>.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/dbd5a0b3f1c3290ec9a903c1f0b86a2d5e722e65.png" alt="image" data-base62-sha1="vmKgcG3c0iXOaaK2S2hHFdWRsR7" width="378" height="323"></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/aed000637548569f05963c852eabf23ecc109d77.png" alt="image" data-base62-sha1="oWsIHJrdr31QVzFU0oMw3gQFv15" width="378" height="323"></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/11470577e86881987eaa20cdc053e4bfddc6fcd0.png" alt="image" data-base62-sha1="2sQhkDm1FNPjdippa2bUJXVElhK" width="273" height="323"></p>
<aside class="quote no-group" data-username="Luna" data-post="1" data-topic="29228">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/luna/48/11116_2.png" class="avatar"> Luna:</div>
<blockquote>
<p>Is there a way to view the displacement field in glyphs not for every pixel but for example every 20 or 40 pixels?</p>
</blockquote>
</aside>
<p>You can actually do even better: specify the sampling density in physical units, so you don’t need to worry about what was the resolution of the displacement field. You can also change the scale, style, coloring, etc. You can display specific points, slices or volumetric regions as glyphs (or grids, or isosurfaces).</p>

---

## Post #3 by @G_Tom (2023-12-06 19:46 UTC)

<p>I am just wondering, how did you get the warped grid in the last image ? I want to generate a grid like this and plot coordinates of the points of intersection.<br>
How can I achieve this ?</p>

---

## Post #4 by @mikebind (2023-12-06 20:00 UTC)

<p>The warped grid is a visualization option for the transform.  In the Transforms module, open Display → Visualization and select Grid instead of Glyph.</p>

---
