---
topic_id: 2942
title: "3D Print With The Various Areas From A Free Surfer Parcellat"
date: 2018-05-27
url: https://discourse.slicer.org/t/2942
---

# 3D print with the various areas from a free surfer parcellation map

**Topic ID**: 2942
**Date**: 2018-05-27
**URL**: https://discourse.slicer.org/t/3d-print-with-the-various-areas-from-a-free-surfer-parcellation-map/2942

---

## Post #1 by @williamthe5thc (2018-05-27 13:10 UTC)

<p>Question, if I’m wanting to make a 3D print, how can I use the parcellation map to be able to have them different colored after printing.  ( or in other words after I have the brain 3D printed is there a stencil that I can use to be able to spray paint each area (e.g. v1, s1, brocca’s area) of the brain; or have it broken into each piece in the STL so I can slightly change the layer that’s printed so that it stands out easier when it’s printed.)</p>
<p>For reference, I’m using the default Bert data set.</p>
<p>Does this make sense?</p>

---

## Post #2 by @timeanddoctor (2018-05-28 03:49 UTC)

<p>can you have a capture screen picture for that model with different colors. We printed dual-color with a printer machine which surporting the colors printing</p>

---

## Post #3 by @williamthe5thc (2018-05-28 04:14 UTC)

<p>If you look down in the bottom of <a href="https://www.slicer.org/w/images/f/fe/FreeSurferCourse_Slicer3-4_SoniaPujol.pdf" rel="nofollow noopener">this</a> tutorial and search for “Visualizing Parcellation Maps”, it will show the brain with a bunch of different areas colored, I’m wanting to get it exported to an STL with each of the colors preserved.  Although as far as I am aware you can only 3D print with up to two different colors currently… unless you want to get super fancy…</p>
<p>Also I’m using the bert data set, as are they.</p>

---

## Post #6 by @Chris_Rorden (2019-09-21 11:52 UTC)

<p>For color <strong>volume</strong> printing, you may want to look at <a href="https://github.com/SlicerFab/SlicerFab" rel="noopener nofollow ugc">SlicerFab</a> and <a href="https://discourse.slicer.org/t/printing-volume-renderings-in-plastic/3017">this post</a>.</p>
<p>For color <strong>surface</strong> printing (e.g. FreeSurfer), I would look at ShapeWays support for color VRML files. The image below shows their matte sandstone (which I prefer to their glossy sandstone). The sandstone has a nice mass, and printing just one hemisphere provides a flat side that is nice for a paperweight.</p>
<p>You can create VRML format meshes with Surfice, which you can get from <a href="https://www.nitrc.org/projects/surfice/" rel="noopener nofollow ugc">NITRC</a> or <a href="https://github.com/neurolabusc/surf-ice/releases" rel="noopener nofollow ugc">GitHub</a>. The model I show below was created by selecting the  Scripting/Python/basic_paint_surface menu item and then choosing the Advanced/SaveMesh menu item. You can also create this type of mesh from the graphical interface. Finally, for an example of FreeSurfer brain regions (e.g. annot files), you can use File/Open to open the “/fs/lh.curv” mesh and select Overlays/AddOverlays to select the “/fs/boggle.annot”, which will create the mesh below with the <a href="https://mindboggle.info/data.html" rel="noopener nofollow ugc">MindBoggle</a> map.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/33703c7d480760ff4b5b40b2b1efc1433e456a2c.jpeg" data-download-href="/uploads/short-url/7l2OBc9OZ5AH3TAhaIMT15097pG.jpeg?dl=1" title="IMG_1438" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/33703c7d480760ff4b5b40b2b1efc1433e456a2c_2_368x500.jpeg" alt="IMG_1438" data-base62-sha1="7l2OBc9OZ5AH3TAhaIMT15097pG" width="368" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/33703c7d480760ff4b5b40b2b1efc1433e456a2c_2_368x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/33703c7d480760ff4b5b40b2b1efc1433e456a2c_2_552x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/33703c7d480760ff4b5b40b2b1efc1433e456a2c_2_736x1000.jpeg 2x" data-dominant-color="8F614C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_1438</span><span class="informations">755×1024 137 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b4531aed15872d576ea7d14321b42512f10fbd30.jpeg" data-download-href="/uploads/short-url/pJdZNlrcRMFLx2gMQanA0oONkWY.jpeg?dl=1" title="boggle" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b4531aed15872d576ea7d14321b42512f10fbd30_2_680x500.jpeg" alt="boggle" data-base62-sha1="pJdZNlrcRMFLx2gMQanA0oONkWY" width="680" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b4531aed15872d576ea7d14321b42512f10fbd30_2_680x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b4531aed15872d576ea7d14321b42512f10fbd30_2_1020x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b4531aed15872d576ea7d14321b42512f10fbd30.jpeg 2x" data-dominant-color="98969F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">boggle</span><span class="informations">1024×752 99.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
