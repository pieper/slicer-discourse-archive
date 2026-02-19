---
topic_id: 10188
title: "Meshing Separate Parts In Segmentmesher"
date: 2020-02-10
url: https://discourse.slicer.org/t/10188
---

# Meshing separate parts in SegmentMesher

**Topic ID**: 10188
**Date**: 2020-02-10
**URL**: https://discourse.slicer.org/t/meshing-separate-parts-in-segmentmesher/10188

---

## Post #1 by @Aep93 (2020-02-10 16:23 UTC)

<p>Hello all,<br>
I use SegmentMesher to mesh two segments that are in contact with each other. The slicer gives me just one vtk file (for both segments). I know that I have to use codes such as meshio to convert these files into the format I want, but how should I separate the segments and generate their mesh separately? Because now I get just one file in the slicer for both segments.<br>
Thanks</p>

---

## Post #3 by @Aep93 (2020-02-10 18:10 UTC)

<p>Hello all,<br>
I am using SegmentMesher extension to mesh two different segments that are connected to each other. Actually the reason I am using SegmentMesher is that I want a mesh that is conformal in the boundaries of two objects that are in contact (a mesh that results in having the same nodes in the boundary), and I found SegmentMesher is capable to do that. My problem is that I have to export both of the objects in one model in the slicer and then save both of them as one file (vtk or vtu). I know that I can use codes such as meshio to convert vtk file into a mesh file that can be used in FEA software, but is there any way to separate the objects that I have? Because In fact I have two objects but I get one vtk file in the slicer.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9fc1d69aeab6aa2538c8feb590bbbc9d70fcb434.png" data-download-href="/uploads/short-url/mNhdikEuU4EfzsxqUxCNjPM7gq0.png?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9fc1d69aeab6aa2538c8feb590bbbc9d70fcb434.png" alt="Capture" data-base62-sha1="mNhdikEuU4EfzsxqUxCNjPM7gq0" width="690" height="460" data-dominant-color="826B70"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">1034×690 42.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Thank you for your help.</p>

---

## Post #4 by @lassoan (2020-02-10 18:12 UTC)

<p>In general, you would want to preserve shared point IDs between submeshes, but if you are sure you don’t need that then you split the mesh using this short script: <a href="https://github.com/lassoan/SlicerSegmentMesher/blob/master/README.md#split-mesh-to-submeshes">https://github.com/lassoan/SlicerSegmentMesher/blob/master/README.md#split-mesh-to-submeshes</a></p>

---

## Post #5 by @Aep93 (2020-02-10 18:25 UTC)

<p>Thank you very much for your response. I think that is exactly what I need. Can you please tell me where should I apply this code?<br>
I am new with slicer and I am using the windows GUI.<br>
Thanks for your help.</p>

---

## Post #6 by @lassoan (2020-02-10 18:28 UTC)

<p>You can hit Ctrl-3 to bring up the Python console in Slicer and copy-paste the code there.</p>

---

## Post #7 by @Aep93 (2020-02-10 18:42 UTC)

<p>It is working now. Thank you very much for your help.</p>

---
