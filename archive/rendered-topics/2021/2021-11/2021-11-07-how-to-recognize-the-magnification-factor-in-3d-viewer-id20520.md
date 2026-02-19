---
topic_id: 20520
title: "How To Recognize The Magnification Factor In 3D Viewer"
date: 2021-11-07
url: https://discourse.slicer.org/t/20520
---

# How to recognize the magnification factor in 3D Viewer

**Topic ID**: 20520
**Date**: 2021-11-07
**URL**: https://discourse.slicer.org/t/how-to-recognize-the-magnification-factor-in-3d-viewer/20520

---

## Post #1 by @tsinesh (2021-11-07 17:45 UTC)

<p>I want to place two 3D models side by side. I want them to have the same magnification factor in the 3D Viewer so that I can compare them visually.<br>
Where do I get the magnification factor?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/53a07622ff724d413df27372a7ea6fb7be52d0f4.png" data-download-href="/uploads/short-url/bVNpRzYzT3q6C7CP2ne5I7goWWw.png?dl=1" title="zoom" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/53a07622ff724d413df27372a7ea6fb7be52d0f4_2_690x388.png" alt="zoom" data-base62-sha1="bVNpRzYzT3q6C7CP2ne5I7goWWw" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/53a07622ff724d413df27372a7ea6fb7be52d0f4_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/53a07622ff724d413df27372a7ea6fb7be52d0f4_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/53a07622ff724d413df27372a7ea6fb7be52d0f4_2_1380x776.png 2x" data-dominant-color="EFE7E7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">zoom</span><span class="informations">1920×1080 265 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thank you for your help</p>

---

## Post #2 by @lassoan (2021-11-07 18:28 UTC)

<p>You can click the link view button to make the two views use exactly the same camera settings.</p>
<p>Note that if you use perspective projection (this is the default) then there is no constant zoom factor (size depends on distance from camera). Therefore, if you want to show the scene from different directions then you need to switch to parallel (a.k.a. orthogonal) projection mode.</p>

---
