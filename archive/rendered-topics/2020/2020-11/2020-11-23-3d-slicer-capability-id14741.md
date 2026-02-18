# 3d slicer capability

**Topic ID**: 14741
**Date**: 2020-11-23
**URL**: https://discourse.slicer.org/t/3d-slicer-capability/14741

---

## Post #1 by @flaviu2 (2020-11-23 12:04 UTC)

<p>Hello all of you. I saw here the amazing features of 3d slicer: <a href="https://www.youtube.com/watch?v=cTeDRISpad8&amp;t=166s" rel="noopener nofollow ugc">https://www.youtube.com/watch?v=cTeDRISpad8&amp;t=166s</a></p>
<p>Excellent.</p>
<p>I wonder if 3d slicer, actually VTK has the same handling features like this software: <a href="https://www.youtube.com/watch?v=m8QRhYQtuts" rel="noopener nofollow ugc">https://www.youtube.com/watch?v=m8QRhYQtuts</a></p>
<p>The second one, Exocad, is accepting STL files only (as far as I know), so<br>
the comparison is not right, but Exocad can handle the 3d objects more handy.</p>
<p><em>My question is:</em> can 3D slicer/VTK add some meshes over a 3D object and this meshes could marked as arbitrary text ? What kind of technology uses Exocad to solve this ?</p>

---

## Post #2 by @lassoan (2021-09-09 02:24 UTC)

<p>Slicer has all the general features (import CBCT image, import surface scan, register them to each other, segment teeth, nerve, generate curved planar reformat views, panoramic X-ray, insert teeth models, design 3D-printable surgical guide, engrave/emboss text, etc.), but the workflow and GUI widgets are not as nicely optimized for this particular procedure as in exocad, and Slicer does not have an implant catalog.</p>
<aside class="quote no-group" data-username="flaviu2" data-post="1" data-topic="14741">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/74df32/48.png" class="avatar"> flaviu2:</div>
<blockquote>
<p>can 3D slicer/VTK add some meshes over a 3D object and this meshes could marked as arbitrary text ? What kind of technology uses Exocad to solve this ?</p>
</blockquote>
</aside>
<p>You can already draw text on segmentations (Engrave effect). You can easily implement text drawing on models, too (generate 3D text model the same way as in the Engrave effect and then add or subtract from the model using Combine models module - in Sandbox extension).</p>
<div class="youtube-onebox lazy-video-container" data-video-id="aOZXwFgcRsY" data-video-title="Draw text on 3D models using Segment editor Engrave tool" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=aOZXwFgcRsY" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/aOZXwFgcRsY/maxresdefault.jpg" title="Draw text on 3D models using Segment editor Engrave tool" width="" height="">
  </a>
</div>


---
