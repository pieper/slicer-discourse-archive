---
topic_id: 21045
title: "Surface Triangulation In Models"
date: 2021-12-14
url: https://discourse.slicer.org/t/21045
---

# Surface triangulation in Models

**Topic ID**: 21045
**Date**: 2021-12-14
**URL**: https://discourse.slicer.org/t/surface-triangulation-in-models/21045

---

## Post #1 by @Karthik (2021-12-14 04:09 UTC)

<p>Hi.<br>
I am using Slicer 4.11.20210226 in ubuntu 20.04<br>
I have written a module that takes input a volume and markups and outputs a Model (surface). When I look at the Model it appeares smooth, but if I save it as an .stl file and reload it back into Slicer, it appeares triangulated. I have observed that in general, when I give triangulated surface as input to my other module, it gives better results than when the surface is not triangulated. So it is important for me to understand what the triangulation does. The surface also appears to be inflated once I save and reload it back again.</p>
<p>This is original surface (Model) in 3d view<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ce79dbbf4eda06c8d1e10f284dab9b5852f79bd3.png" data-download-href="/uploads/short-url/tszreGy5kmnlEtNreo5z5Wp14UH.png?dl=1" title="before saving" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce79dbbf4eda06c8d1e10f284dab9b5852f79bd3_2_690x478.png" alt="before saving" data-base62-sha1="tszreGy5kmnlEtNreo5z5Wp14UH" width="690" height="478" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce79dbbf4eda06c8d1e10f284dab9b5852f79bd3_2_690x478.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce79dbbf4eda06c8d1e10f284dab9b5852f79bd3_2_1035x717.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ce79dbbf4eda06c8d1e10f284dab9b5852f79bd3.png 2x" data-dominant-color="A3A4A4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">before saving</span><span class="informations">1345×933 81.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This is after saving as .stl and relading back into Slicer as Model in 3d view<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8c3253c40a06da749f9f6f598ec040e9834f4e64.png" data-download-href="/uploads/short-url/k0eFCUyoSSKQPWH5M3g3sVkdHPC.png?dl=1" title="after saving and reloading" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c3253c40a06da749f9f6f598ec040e9834f4e64_2_690x478.png" alt="after saving and reloading" data-base62-sha1="k0eFCUyoSSKQPWH5M3g3sVkdHPC" width="690" height="478" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c3253c40a06da749f9f6f598ec040e9834f4e64_2_690x478.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c3253c40a06da749f9f6f598ec040e9834f4e64_2_1035x717.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8c3253c40a06da749f9f6f598ec040e9834f4e64.png 2x" data-dominant-color="9D9F9D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">after saving and reloading</span><span class="informations">1345×933 49.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Why does triangulation happen when I just save and reload the file?<br>
What difference does this make to the surface object?<br>
Is this only a visible difference or is there some change in the data?</p>

---

## Post #2 by @lassoan (2021-12-14 14:23 UTC)

<p>The faceted appearance due to using flat shading, because smooth Gouraud or Phong shading would requires surface normals. STL files cannot store surface normals, therefore when you save your mesh into this format then surface normals is lost.</p>
<p>You can either use a different file format (ply, vtk, obj, …) or recompute the normals using the Surface Toolbox module.</p>

---
