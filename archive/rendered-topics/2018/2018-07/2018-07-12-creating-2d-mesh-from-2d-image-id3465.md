---
topic_id: 3465
title: "Creating 2D Mesh From 2D Image"
date: 2018-07-12
url: https://discourse.slicer.org/t/3465
---

# Creating 2D mesh from 2D image

**Topic ID**: 3465
**Date**: 2018-07-12
**URL**: https://discourse.slicer.org/t/creating-2d-mesh-from-2d-image/3465

---

## Post #1 by @Joseph (2018-07-12 02:26 UTC)

<p>From what I can tell, Slicer is used to generate a 3d mesh from 2d images.  However, I simply want to segment a 2d image and then create a 2d mesh in order to do a 2d finite element analysis using FEA software.  Is this possible?</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2018-07-12 02:40 UTC)

<p>You can have single-slice image, which is essentially a 2D image. You should be able to segment the image, too. However, I think you would need to write some custom Python script to generate 2D mesh, using VTK filters (e.g. Delaunay triangulation).</p>

---
