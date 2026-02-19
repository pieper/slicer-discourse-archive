---
topic_id: 15515
title: "Make Stl Into Solid And Smooth Surface"
date: 2021-01-14
url: https://discourse.slicer.org/t/15515
---

# Make stl into solid and smooth surface

**Topic ID**: 15515
**Date**: 2021-01-14
**URL**: https://discourse.slicer.org/t/make-stl-into-solid-and-smooth-surface/15515

---

## Post #1 by @Valentina_Mejia_Gall (2021-01-14 02:22 UTC)

<p>I need to do a finite element analysis, for this I export the STL and I have a surface with several faces or triangles, I need to convert it to solid and the surface is as “smooth” as possible. is there any way to do it in 3D-slicer</p>

---

## Post #2 by @lassoan (2021-01-14 02:32 UTC)

<p>You can use <a href="https://github.com/lassoan/SlicerSegmentMesher#segment-mesher-extension">SegmentMesher extension</a> to created a smoothed volumetric mesh, readily usable for finite element analysis.</p>

---

## Post #3 by @Valentina_Mejia_Gall (2021-01-15 00:13 UTC)

<p>I do it as the tutorial said but I have multiple question.</p>
<p>I need to do a finite element analysis with this model<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/362c6ac734d00da212a0d5868d5856fac0b96e41.png" data-download-href="/uploads/short-url/7JeWGKSOAFUKPp9RDqS1bUyacBb.png?dl=1" title="Screen Shot 2021-01-14 at 7.05.47 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/362c6ac734d00da212a0d5868d5856fac0b96e41_2_690x388.png" alt="Screen Shot 2021-01-14 at 7.05.47 PM" data-base62-sha1="7JeWGKSOAFUKPp9RDqS1bUyacBb" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/362c6ac734d00da212a0d5868d5856fac0b96e41_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/362c6ac734d00da212a0d5868d5856fac0b96e41_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/362c6ac734d00da212a0d5868d5856fac0b96e41_2_1380x776.png 2x" data-dominant-color="A5A3B5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-01-14 at 7.05.47 PM</span><span class="informations">1920×1080 471 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But when I do as the tutorial said, first when i have to select the segmentation its appear as segmentation 1,2,etc. So i dont know exactly which one is the tibia,fibula, etc as i have them label in the segmentation.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97aad8b00f486f3c105bb4d20d1f037191a3c682.png" data-download-href="/uploads/short-url/lDI8mk5Oe52AiqNB3wBKHmg6rOG.png?dl=1" title="Screen Shot 2021-01-14 at 7.01.48 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97aad8b00f486f3c105bb4d20d1f037191a3c682_2_404x500.png" alt="Screen Shot 2021-01-14 at 7.01.48 PM" data-base62-sha1="lDI8mk5Oe52AiqNB3wBKHmg6rOG" width="404" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97aad8b00f486f3c105bb4d20d1f037191a3c682_2_404x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97aad8b00f486f3c105bb4d20d1f037191a3c682.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97aad8b00f486f3c105bb4d20d1f037191a3c682.png 2x" data-dominant-color="ECEEEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-01-14 at 7.01.48 PM</span><span class="informations">591×730 51.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Then when i see the final result, it’s a bit chaotic, the both fibulas have been cut in half, and is not as smooth as i would like to. Is there a way to fix that?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2fb2c6bef1b51e049df0841e00d97a852bbd1c85.png" data-download-href="/uploads/short-url/6NXsZKtmeUVNK5lijC6ryJffxxH.png?dl=1" title="Screen Shot 2021-01-14 at 7.03.17 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2fb2c6bef1b51e049df0841e00d97a852bbd1c85_2_690x388.png" alt="Screen Shot 2021-01-14 at 7.03.17 PM" data-base62-sha1="6NXsZKtmeUVNK5lijC6ryJffxxH" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2fb2c6bef1b51e049df0841e00d97a852bbd1c85_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2fb2c6bef1b51e049df0841e00d97a852bbd1c85_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2fb2c6bef1b51e049df0841e00d97a852bbd1c85_2_1380x776.png 2x" data-dominant-color="A6A2B8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-01-14 at 7.03.17 PM</span><span class="informations">1920×1080 418 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks a lot for the help.<br>
I am basing myself on this program in which they do it directly and apply a smooth and the mesh looks and that’s what I’m aiming to have.</p><div class="youtube-onebox lazy-video-container" data-video-id="HJmWc_-_BrU" data-video-title="How to Mesh a 3D Model | Mimics Innovation Suite" data-video-start-time="101s" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=HJmWc_-_BrU&amp;t=101s" target="_blank" class="video-thumbnail" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/HJmWc_-_BrU/maxresdefault.jpg" title="How to Mesh a 3D Model | Mimics Innovation Suite" width="" height="">
  </a>
</div>


---

## Post #4 by @lassoan (2021-01-15 02:01 UTC)

<p>Default mesh element size is very large so that you start from a quickly generated low-resolution mesh. You need to adjust meshing parameters to fulfill your needs (details, smoothness, number of cells, etc.). These <a href="https://github.com/lassoan/SlicerSegmentMesher#mesh-generation-parameters">parameter descriptions</a> should help, but if something is not clear then let us know.</p>

---

## Post #5 by @Valentina_Mejia_Gall (2021-01-19 02:29 UTC)

<p>Hello Andras,<br>
I have a question, searching in the forum I came across this article about how to save and convert the vkt file into a volumetric mesh, but I don’t know how to manipulate 3dSlicer with code.<br>
Is there a program or a tutorial on how to do that process?</p>
<p>Article</p><aside class="quote" data-post="10" data-topic="1416">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/convert-a-surface-mesh-to-a-volumetric-mesh-in-3d-slicer/1416/10">Convert a surface mesh to a volumetric mesh in 3D Slicer</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    ICEM can import surface meshes (STL files) - see for example <a href="https://www.cfd-online.com/Forums/ansys-meshing/77427-meshing-stl-surface-icem.html" rel="noopener nofollow ugc">this</a> old forum topic. Segment Mesher can generate tetrahedral meshes that you can save in VTK unstructured grid (.vtu) file format. You may need a mesh conversion utility to convert it to a file format that can be read by your FEM software.
  </blockquote>
</aside>


---
