---
topic_id: 26572
title: "Export An Open Surface With Boundary As Stl"
date: 2022-12-04
url: https://discourse.slicer.org/t/26572
---

# Export an open surface with boundary as STL

**Topic ID**: 26572
**Date**: 2022-12-04
**URL**: https://discourse.slicer.org/t/export-an-open-surface-with-boundary-as-stl/26572

---

## Post #1 by @torquil (2022-12-04 22:08 UTC)

<p>Is it possible to export from 3D Slicer something like a 2d disk or other more general 2d surface that has a boundary, i.e. is not closed such as the STL files you get when exporting segmentations? I need this for later use in other simulation software.</p>
<p>The reason I need something like a disk is because I will measure the flux of a vector field through this surface. The surface will be based on anatomy, so ideally I would like to draw something within 3D Slicer, and export it as an STL file.</p>
<p>For now I have created a thin segmentation, exported the surface as an STL, and then divided it in two using FreeCAD. But it would be better if 3D Slicer could generate such 2d surfaces directly (or one of the extension packages).</p>
<p>Best regards,<br>
Torquil Sørensen<br>
Norway</p>

---

## Post #2 by @lassoan (2022-12-04 23:05 UTC)

<p>There are many ways to define a thin open surface.<br>
One option is to use the Baffle Planner module in SlicerHeart. It is useful if the goal is to have a smooth disk-like surface, mostly constrained by the boundary curve:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="AigTwMYRI1Y" data-video-title="Design surface patches using new Baffle Planner module" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=AigTwMYRI1Y" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/AigTwMYRI1Y/maxresdefault.jpg" title="Design surface patches using new Baffle Planner module" width="" height="">
  </a>
</div>

<p>Another option is to segment the object of interest to get a close surface and then use Curve cut tool in Dynamic modeler module to cut out an open surface patch from it. This is useful if you need to extract anatomical surface with the highest accuracy (you don’t want it to be smooth).</p>
<div class="youtube-onebox lazy-video-container" data-video-id="F6fNMQTxD-4" data-video-title="3D Slicer: Dynamic Modeler - Parametric Surface Editing for Biomedical Applications" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=F6fNMQTxD-4" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/F6fNMQTxD-4/maxresdefault.jpg" title="3D Slicer: Dynamic Modeler - Parametric Surface Editing for Biomedical Applications" width="" height="">
  </a>
</div>

<p>Before simulation, you may want to do uniform resampling of the mesh using Surface Toolbox module.</p>
<p>Is the flux computation for heart valve analysis? We have lots of tools that you might find useful, many of them are already publicly released, some are still in the publish&amp;release pipeline.</p>

---

## Post #3 by @torquil (2022-12-05 10:18 UTC)

<p>Thank you! SlicerHeart was a very simple and good solution. I’m simulating an electric field and want to measure its flux through surfaces placed at different positions in my domain. Usually, the surfaces do not need to come from a segmentation, but it is good to have both possibilities.</p>

---
