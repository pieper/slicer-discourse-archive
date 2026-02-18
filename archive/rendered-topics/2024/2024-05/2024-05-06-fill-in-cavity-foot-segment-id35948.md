# Fill in Cavity - foot segment

**Topic ID**: 35948
**Date**: 2024-05-06
**URL**: https://discourse.slicer.org/t/fill-in-cavity-foot-segment/35948

---

## Post #1 by @Jamie_Huang (2024-05-06 15:57 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc8c304d56fca7c3415ff271a5b15e6836842f42.jpeg" data-download-href="/uploads/short-url/tbvKVgCAeh2PNUm9dPcMe5z6v3I.jpeg?dl=1" title="Screenshot 2024-05-05 at 9.52.41 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/cc8c304d56fca7c3415ff271a5b15e6836842f42_2_283x500.jpeg" alt="Screenshot 2024-05-05 at 9.52.41 PM" data-base62-sha1="tbvKVgCAeh2PNUm9dPcMe5z6v3I" width="283" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/cc8c304d56fca7c3415ff271a5b15e6836842f42_2_283x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/cc8c304d56fca7c3415ff271a5b15e6836842f42_2_424x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/cc8c304d56fca7c3415ff271a5b15e6836842f42_2_566x1000.jpeg 2x" data-dominant-color="576469"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-05-05 at 9.52.41 PM</span><span class="informations">879×1552 74.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>So I am segmenting the bones of the foot and if I set a lowthreshold it will pick up lots of soft tissue making island function hard to use. If i set a high threshold, the bones edges are missing therefore creating big cavities that I don’t really how to fix. I am just transitioning from mimics to 3d slicer so if anyone knows any tip that would be extremely helpful</p>

---

## Post #2 by @pieper (2024-05-06 16:23 UTC)

<p>Try WrapSolidify: <a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify" class="inline-onebox">GitHub - sebastianandress/Slicer-SurfaceWrapSolidify: 3D Slicer extension which contains a Segment Editor Effect that solidifies and extracts the surface of a segmentation</a></p>
<aside class="quote no-group" data-username="Jamie_Huang" data-post="1" data-topic="35948">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamie_huang/48/68167_2.png" class="avatar"> Jamie_Huang:</div>
<blockquote>
<p>transitioning from mimics to 3d slicer</p>
</blockquote>
</aside>
<p>Let us know if you find other things harder or easier in Slicer or find any missing features.</p>

---
