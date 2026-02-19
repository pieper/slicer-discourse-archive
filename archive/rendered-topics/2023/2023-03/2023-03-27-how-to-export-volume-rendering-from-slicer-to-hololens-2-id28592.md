---
topic_id: 28592
title: "How To Export Volume Rendering From Slicer To Hololens 2"
date: 2023-03-27
url: https://discourse.slicer.org/t/28592
---

# How to export volume rendering from slicer to Hololens 2

**Topic ID**: 28592
**Date**: 2023-03-27
**URL**: https://discourse.slicer.org/t/how-to-export-volume-rendering-from-slicer-to-hololens-2/28592

---

## Post #1 by @Caterina (2023-03-27 09:03 UTC)

<p>Good morning,<br>
I need to export volume rendering from 3d slicer in a format that is compatible with Hololens 2 (stl or obj).<br>
For example, in the screenshot in attach, I can visualize the segmentation (trachea) and the volume rendering (lung). From 3d slicer I can export only the segmentation as stl or obj. Can I also export the volume rendering to visualize it on Hololens 2?<br>
Thanks</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f9e64ca12f33ff35b9f7f74400047f30b102191f.jpeg" data-download-href="/uploads/short-url/zEIiRj4zwEb4snSlIBsXiZLl0ab.jpeg?dl=1" title="Schermata 2023-03-27 alle 11.00.58" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f9e64ca12f33ff35b9f7f74400047f30b102191f_2_690x431.jpeg" alt="Schermata 2023-03-27 alle 11.00.58" data-base62-sha1="zEIiRj4zwEb4snSlIBsXiZLl0ab" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f9e64ca12f33ff35b9f7f74400047f30b102191f_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f9e64ca12f33ff35b9f7f74400047f30b102191f_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f9e64ca12f33ff35b9f7f74400047f30b102191f_2_1380x862.jpeg 2x" data-dominant-color="797D83"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Schermata 2023-03-27 alle 11.00.58</span><span class="informations">1920×1200 157 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2023-03-27 15:34 UTC)

<p>It is not possible to export volume rendering (a rendering technique) into a mesh file format. See more details here:</p>
<aside class="quote quote-modified" data-post="1" data-topic="524">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/b19c9b/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/save-volume-rendering-as-stl-file/524">Save volume rendering as STL file</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hello, I am a new user on 3D slicer. 
I was using the display preset feature under volume rendering, and I was wondering if there is a way to save what I was viewing as an .stl or 3D printable file. 
For example, I was viewing a sample MRI using the CT-cardiac3 preset display. 
When I tried to save that specific 3D preset displayed sample in a .stl file, the option was unavailable. 
I was only able to see .vp (volume property), .txt formats. 
Is there a way to accomplish what I desire in 3D slic…
  </blockquote>
</aside>


---

## Post #3 by @LucasGandel (2023-03-28 11:41 UTC)

<p>For now, an option could be to have a separate VTK-based app to visualize the exported data from 3D Slicer. VTK supports volume rendering inside the Hololens 2 (see <a href="https://www.kitware.com/stream-vtk-to-the-hololens-2/" rel="noopener nofollow ugc">here</a>).</p>

---

## Post #4 by @rbumm (2023-03-28 19:06 UTC)

<p>Nice demos. Thanks Lucas</p>

---
