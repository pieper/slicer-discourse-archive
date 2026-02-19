---
topic_id: 18063
title: "Vmtk Centerline Extraction Vs Cgal Mesh Skeletonization"
date: 2021-06-10
url: https://discourse.slicer.org/t/18063
---

# VMTK Centerline extraction vs. CGAL mesh skeletonization

**Topic ID**: 18063
**Date**: 2021-06-10
**URL**: https://discourse.slicer.org/t/vmtk-centerline-extraction-vs-cgal-mesh-skeletonization/18063

---

## Post #1 by @Zemleroi (2021-06-10 13:24 UTC)

<p>Hi,<br>
How does the vmtk centerline extraction method compare with CGAL’s <a href="https://doc.cgal.org/latest/Surface_mesh_skeletonization/index.html" rel="noopener nofollow ugc">Triangulated Surface Mesh Skeletonization</a>? Does the method implemented in CGAL work less well on tubular geometry?</p>

---

## Post #2 by @lassoan (2021-06-10 23:16 UTC)

<p>VMTK has two centerline extraction algorithms.</p>
<p>One is simple skeletonization, which is probably similar to what is implemented in CGAL.</p>
<p>The other is centerline extraction, which does a lot more. It reconstructs realistic vessel geometry at branching points (taking into account flow direction and radius). It can also detect vessel endpoints automatically that the user can add/remove them as needed (e.g., to exclude small or irrelevant branches), provides connectivity information (parent/children for each branch) and standardized coordinate system defined on the curve.</p>
<p>A very important additional difference that most parts of CGAL (including the vessel skeletonization module) comes with a restrictive GPL license. You need to buy a commercial license if you want to use it in a product. In contrast, VMTK comes with BSD license, which allows unrestricted use, even for commercial applications.</p>

---

## Post #3 by @Zemleroi (2021-06-11 11:19 UTC)

<p>Thank you for your answer!<br>
I thought that vessel endpoints had to be indicated by the user in VMTK, is it only the Slicer plugin that finds endpoints automatically?<br>
I have a further question about the reference frame associated with the centerline (not sure if it should go into a separate topic): does it then already integrate information on the local base plane? What I mean is let’s say I have a tubular structure with one side of it less convex (compressed, flattened). The plane of the compressed side changes along the length of the structure. Will the reference frame of the centerline track this plane? Or would it be independent of that plane?</p>

---

## Post #4 by @lassoan (2021-06-11 12:29 UTC)

<aside class="quote no-group" data-username="Zemleroi" data-post="3" data-topic="18063">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/z/9de053/48.png" class="avatar"> Zemleroi:</div>
<blockquote>
<p>is it only the Slicer plugin that finds endpoints automatically?</p>
</blockquote>
</aside>
<p>Automatic endpoint detection is a VMTK feature, it is just not used in the VMTK centerline examples. We added to the Extract Centerline module in Slicer for the user’s convenience.</p>
<aside class="quote no-group" data-username="Zemleroi" data-post="3" data-topic="18063">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/z/9de053/48.png" class="avatar"> Zemleroi:</div>
<blockquote>
<p>The plane of the compressed side changes along the length of the structure. Will the reference frame of the centerline track this plane? Or would it be independent of that plane?</p>
</blockquote>
</aside>
<p>The coordinate system tries to minimize the torsion. It does not depend on the shape of the cross-section but only on the curvature of the centerline curve.</p>
<p>You can use the coordinate transform that VMTK provides to extract vessel cross-section images, detect the flat side in this 2D image, and get the direction in 3D by applying the inverse of the VMTK-given transform.</p>
<p>You may also find Curved Planar Reformat module useful (in Sandbox extension). This module can straighten the vessel by placing vessel cross-sections in a straight column. It also provides and invertible “straightening” transform, so any measurements that you make in the straightened space can be transformed back easily to the curved space.</p>

---

## Post #5 by @Zemleroi (2021-06-11 15:16 UTC)

<p>The last feature sounds great!<br>
I currently use VMTK just for centerline extraction and export it to Rhino for measurement, since I have to measure NURBS curves traced over the mesh, based on the centerline extracted with VMTK and the calculated local baseplanes. Am I right that measurements on such curves (relative coordinates and curvature) are best done in 3d modelling software rather than in Slicer or directly from Python?</p>

---

## Post #6 by @lassoan (2021-06-11 15:26 UTC)

<p>If you make measurements on image inputs, then measurements are best done in imaging software because then you can verify that your final points and surfaces match the actual input image (not some extracted, potentially noisy surfaces or centerlines).</p>
<p>Moreover, you need to use imaging software anyway for importing and segmenting the images, and it is a huge advantage if you can do everything in that software instead of switching to another one.</p>
<p>Slicer has additional advantages that it is completely free, even for commercial use, and fully customizable and extensible using Python scripting. So, you can implement your complete workflow, from image import to visualization final result in one place, automating all the steps that are easy to automate, and add graphical user interface for any additional inputs for things that are hard to make fully automatic.</p>
<p>In Slicer, you can work directly on polygonal meshes (define curves over the mesh, cut and combine meshes, etc), so you can avoid the NURBS conversion step. It has certainly advantages if you can represent your geometry with a nice and simple NURBS, but the conversion from real-life, complex, noisy polygon meshes that are common in biomedical imaging it is not always trivial to create an accurate NURBS representation.</p>

---

## Post #7 by @Zemleroi (2021-06-11 15:34 UTC)

<p>Right, in my case I am actually working from scanned 3d data, so I do not have to do any segmentation. The reason I need NURBS curves interpolated on the mesh rather than polylines is to be able to do statistics on their curvature, so I don’t think that part can be avoided. But I’ll see if maybe an opensource Rhino library, rather than Rhino itself, can be incorporated into the workflow.</p>

---

## Post #8 by @lassoan (2021-06-11 16:49 UTC)

<p>You can get curvature of the curves in Slicer, just enable one of the curvature metrics in Markups module’s measurement section. Analytic curve is computed using b-spline or Kochanek spline interpolation or polynomial approximation instead of NURBS, but this should not matter, as the shape is determined from the dense set of control points. You can visualize the curvature and access it as a numpy array.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/ebeec60e20a6c9b84025e156dd54f1a99d2cdd80.png" data-download-href="/uploads/short-url/xF9M5Yrv4arSk8J23vqdSeOQC0E.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ebeec60e20a6c9b84025e156dd54f1a99d2cdd80_2_690x399.png" alt="image" data-base62-sha1="xF9M5Yrv4arSk8J23vqdSeOQC0E" width="690" height="399" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ebeec60e20a6c9b84025e156dd54f1a99d2cdd80_2_690x399.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ebeec60e20a6c9b84025e156dd54f1a99d2cdd80_2_1035x598.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ebeec60e20a6c9b84025e156dd54f1a99d2cdd80_2_1380x798.png 2x" data-dominant-color="CBCCE4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2254×1306 269 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>If you must use NURBS interpolation for some reason then there are many Python packages to choose from. In Slicer we used <a href="https://pypi.org/project/geomdl/">geomdl</a> for a few projects and it works well.</p>

---

## Post #9 by @Zemleroi (2021-06-12 06:58 UTC)

<p>Thank you very much for useful advice! This may really simplify my workflow. I will definitely try it in Slicer.</p>

---
