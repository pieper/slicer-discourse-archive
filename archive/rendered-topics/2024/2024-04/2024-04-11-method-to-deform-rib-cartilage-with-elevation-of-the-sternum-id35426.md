---
topic_id: 35426
title: "Method To Deform Rib Cartilage With Elevation Of The Sternum"
date: 2024-04-11
url: https://discourse.slicer.org/t/35426
---

# Method to deform rib cartilage with elevation of the sternum in pectus excavatum

**Topic ID**: 35426
**Date**: 2024-04-11
**URL**: https://discourse.slicer.org/t/method-to-deform-rib-cartilage-with-elevation-of-the-sternum-in-pectus-excavatum/35426

---

## Post #1 by @Mark_Ryan (2024-04-11 06:10 UTC)

<p>I’ve been successfully modeling the thoracic skeleton and rib cartilage for a while now for planning Nuss procedures in pectus excavatum patients. What I would like to do is model the correction of deformed cartilage that occurs when the sternum is elevated . I have been trying to this by using armatures in Blander, but it just occurred to me that there might be a way to natively do this within 3D slicer.</p>
<p>Ideally the amount of shear/deformation of bony structures should be minimal relative to the rib cartilage. I saw mentions of something similar using the Osteotomy Module extension. Do you think this would be possible in 3D Slicer or am I better off using animation tools in Blender?</p>

---

## Post #2 by @pieper (2024-04-11 19:22 UTC)

<p>At this point you may be better off in Blender for that.  There’s some early prototype work at incorporating deformable anatomy in Slicer but probably not mature enough for general use.</p>

---

## Post #3 by @Mark_Ryan (2024-04-12 15:58 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8bebef808ef1fdf705a6cbfb7a046884dd801dd9.jpeg" data-download-href="/uploads/short-url/jXNRc6HeU0dohHeuflrumcvwQpb.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8bebef808ef1fdf705a6cbfb7a046884dd801dd9_2_488x499.jpeg" alt="image" data-base62-sha1="jXNRc6HeU0dohHeuflrumcvwQpb" width="488" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8bebef808ef1fdf705a6cbfb7a046884dd801dd9_2_488x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8bebef808ef1fdf705a6cbfb7a046884dd801dd9_2_732x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8bebef808ef1fdf705a6cbfb7a046884dd801dd9_2_976x998.jpeg 2x" data-dominant-color="3B3B3B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1822×1864 253 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I’m trying.  This stuff is hard! Every time I deform the sternum it rips the ribs off the spine.  Will get there eventually.</p>

---

## Post #4 by @lassoan (2024-04-13 15:55 UTC)

<p>You can get approximate deformations in Slicer using thin-plate-spline transform as shown here:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="GfDDQykH1iY" data-video-title="Soft tissue deformation simulation" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=GfDDQykH1iY" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/GfDDQykH1iY/maxresdefault.jpg" title="Soft tissue deformation simulation" width="" height="">
  </a>
</div>

<p>Basic armature based animation in Blender would do unconstrained piecewise rigid deformation followed by geometry-based morhping, so it would not be more physically accurate than a simple point-pair-driven thin-plate-spline transform.</p>
<p>If you want to compute physics-based deformation then you would need to use a simulation software, such as OpenSIM or a mechanical modeling software, such as FEBio. However, setting up a simulation in these systems would take huge effort and they would still be quite inaccurate, as you don’t have accurate patient-specific material properties.</p>

---

## Post #5 by @Higor (2024-11-08 19:28 UTC)

<p>Hey Mark,<br>
I’m new in 3D Slicer, and I’m trying to learn how to plan my Nuss procedures with it.<br>
I successfully did the reconstruction of the rib cage, cartilages and sternum, and it helps, but would be great if I have actually a way to predict how the result will be with the bars in place, or the ideal spot for their position.</p>
<p>Would you mind sharing how are you doing your planning?</p>
<p>Thank you!</p>

---

## Post #6 by @Mark_Ryan (2025-05-15 00:02 UTC)

<p>Sorry I didn’t realize there were messages in this thing (or at least how to check them). Most I’ve been able to do so far is measure a curved line using the markups tool as to where I think the bars are going to end up, which is usually level with the outer rim of the defect. From there it provides a measurement so I can size my bars appropriately. Can also use a plane tool to map the entry and exit points from the thorax to help with marking out bar location. Have been looking into different tools to deform the chest model but it’s harder than I thought it would be</p>

---
