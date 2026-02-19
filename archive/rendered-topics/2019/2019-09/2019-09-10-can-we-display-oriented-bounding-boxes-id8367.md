---
topic_id: 8367
title: "Can We Display Oriented Bounding Boxes"
date: 2019-09-10
url: https://discourse.slicer.org/t/8367
---

# Can we display oriented bounding boxes?

**Topic ID**: 8367
**Date**: 2019-09-10
**URL**: https://discourse.slicer.org/t/can-we-display-oriented-bounding-boxes/8367

---

## Post #1 by @kab (2019-09-10 15:44 UTC)

<p>I have several oriented bounding boxes I have generated. Is there a way to plot and/or edit these in Slicer?</p>
<p>That is, I have a set of 8 vertices corresponding to an oriented box in the same image space as my volumes. Can I plot these points with lines between them?</p>
<p>I am happy to code this for use with Slicer’s python interpreter if someone can point me in the right direction.</p>
<p>CropVolume works great for axis-aligned bounding boxes, but I could not find a way to rotate the box.</p>

---

## Post #2 by @lassoan (2019-09-10 17:04 UTC)

<p>You can display oriented boxes as model nodes or as annotation ROI nodes.</p>
<p>You can orient them by applying a transform to the node. In case of models, you may create them already oriented (e.g., create the box using vtkCubeSource and rotate using vtkTransformPolyDataFilter) and then you don’t need to use a transform node.</p>
<p>To edit, you can enable Transform/Display/Interaction/Visible in 3D view. This allows translation, rotation, and resizing in 3D. To allow editing in slice views as well, you need to use ROI node (and you may keep the transform interactor for rotation only).</p>

---
