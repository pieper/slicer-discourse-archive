---
topic_id: 46520
title: "3D Rendering Makes Whole Screen Glitch"
date: 2026-03-20
url: https://discourse.slicer.org/t/46520
---

# 3D rendering makes whole screen glitch

**Topic ID**: 46520
**Date**: 2026-03-20
**URL**: https://discourse.slicer.org/t/3d-rendering-makes-whole-screen-glitch/46520

---

## Post #1 by @naomic2 (2026-03-20 17:34 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1c57380c665e6a5bf8b843f76bf7243ffef309ab.png" data-download-href="/uploads/short-url/42IeyUo9aXXuwaNkCBbONUVNUXV.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c57380c665e6a5bf8b843f76bf7243ffef309ab_2_690x298.png" alt="image" data-base62-sha1="42IeyUo9aXXuwaNkCBbONUVNUXV" width="690" height="298" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c57380c665e6a5bf8b843f76bf7243ffef309ab_2_690x298.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c57380c665e6a5bf8b843f76bf7243ffef309ab_2_1035x447.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c57380c665e6a5bf8b843f76bf7243ffef309ab_2_1380x596.png 2x" data-dominant-color="484849"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">3089×1336 47.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>When I’m in Segmentation Editor and I press “Show 3D” the screen glitches between something like this image and normal. When I have all of my segments deselected with Show 3D on, the screen is also normal. I’m not really sure what’s going on. I am using V 5.10. A team member added new segmentations since the last time I opened the file. What do you think the problem could be? Has anyone seen this before? Thanks.</p>

---

## Post #2 by @mikebind (2026-03-20 19:51 UTC)

<p>To explore, I would try:</p>
<ul>
<li>zoom way out or way in</li>
<li>see if you can narrow it down to a particular segment</li>
<li>turn on or off “Shadows visibility” (in pushpin menu on 3D view)</li>
<li>try toggling between orthographic and perspective view (in pushpin menu on 3D view)</li>
<li>in the Segmentations module, try removing and recreating the “Closed surface” representation</li>
<li>Try turning off surface smoothing in Segment Editor module (in dropdown on “Show 3D” button)</li>
</ul>
<p>The results can help narrow down where the problem might be (or might make it go away).</p>

---
