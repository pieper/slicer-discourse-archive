---
topic_id: 27140
title: "How To Control Mesh Size On The Boundary"
date: 2023-01-09
url: https://discourse.slicer.org/t/27140
---

# How to control mesh size on the boundary

**Topic ID**: 27140
**Date**: 2023-01-09
**URL**: https://discourse.slicer.org/t/how-to-control-mesh-size-on-the-boundary/27140

---

## Post #1 by @ZSoltani (2023-01-09 21:32 UTC)

<p>HI ALL,</p>
<p>After segmentation and exporting the volume, I need to mesh it using Gmsh. My problem is that in the stl fine, the size of triangles on the outer surface of the volume is so small (even on the flat surfaces). So even though in Gmsh I changed the size of volume elements to a courser value, it keeps the size of boundary surface elements the same as the stl input file (see the attached image)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/567c23a5faa571c7b0cdff6a55d8fc3f06d27656.jpeg" data-download-href="/uploads/short-url/cl51PHhRaMbM9tosonDP0FZGEse.jpeg?dl=1" title="Screenshot from 2023-01-09 10-30-15" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/567c23a5faa571c7b0cdff6a55d8fc3f06d27656_2_690x337.jpeg" alt="Screenshot from 2023-01-09 10-30-15" data-base62-sha1="cl51PHhRaMbM9tosonDP0FZGEse" width="690" height="337" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/567c23a5faa571c7b0cdff6a55d8fc3f06d27656_2_690x337.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/567c23a5faa571c7b0cdff6a55d8fc3f06d27656_2_1035x505.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/567c23a5faa571c7b0cdff6a55d8fc3f06d27656_2_1380x674.jpeg 2x" data-dominant-color="2E9C6A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2023-01-09 10-30-15</span><span class="informations">1920×939 459 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I appreciate any suggestion to solve this.</p>
<p>Thank you.</p>
<p>Zahra</p>

---

## Post #2 by @pieper (2023-01-09 21:53 UTC)

<p>Hi <a class="mention" href="/u/zsoltani">@ZSoltani</a> - Try using the Surface Toolbox to reduce the complexity of the surface mesh.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/surfacetoolbox.html#uniform-remeshing" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/surfacetoolbox.html#uniform-remeshing</a></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/529209e8e675dec5f2ce10b827ac28c173723d4d.png" alt="image" data-base62-sha1="bMs2qbtXUnK0aGpKXKGFFpq2yrb" width="495" height="228"></p>

---

## Post #3 by @ZSoltani (2023-01-10 15:53 UTC)

<p>Thank you <a class="mention" href="/u/pieper">@pieper</a>! That was very helpful. Below is the image after applying this technique.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/ed4dc99fc7ab91a361fd2646208ff556602e3e5b.png" data-download-href="/uploads/short-url/xRhOOJcV4iYa8hS2V7MTlLtWQnp.png?dl=1" title="Screenshot from 2023-01-10 05-51-33" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/ed4dc99fc7ab91a361fd2646208ff556602e3e5b_2_690x429.png" alt="Screenshot from 2023-01-10 05-51-33" data-base62-sha1="xRhOOJcV4iYa8hS2V7MTlLtWQnp" width="690" height="429" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/ed4dc99fc7ab91a361fd2646208ff556602e3e5b_2_690x429.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/ed4dc99fc7ab91a361fd2646208ff556602e3e5b_2_1035x643.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/ed4dc99fc7ab91a361fd2646208ff556602e3e5b_2_1380x858.png 2x" data-dominant-color="9ED4CA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2023-01-10 05-51-33</span><span class="informations">1591×991 93.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thanks,</p>
<p>Zahra</p>

---
