---
topic_id: 9094
title: "How To Export Segmentation Label From Volume To Surface Mesh"
date: 2019-11-09
url: https://discourse.slicer.org/t/9094
---

# How to export segmentation label from volume to surface mesh on the fly?

**Topic ID**: 9094
**Date**: 2019-11-09
**URL**: https://discourse.slicer.org/t/how-to-export-segmentation-label-from-volume-to-surface-mesh-on-the-fly/9094

---

## Post #1 by @ButuiHu (2019-11-09 10:08 UTC)

<p>I’m trying to computes and displays surface-to-surface distance between two triangle meshes using <a href="https://www.nitrc.org/projects/meshmetric3d" rel="nofollow noopener">3DMeshMetric</a>, which need a vtk format input. So I create one using model maker module in 3D Slicer. But it seems that model maker module generates newer version of vtk data file format which is not supported in 3DMeshMetric, I got unknown keyword error when load the vtk files. Then I try ITK-SNAP’s segmentation export, and it works well. How could I do this job with python script using SimpleITK, VTK or some other similar packages, so that I could convert many volume to vtk file needed in 3DMeshMetric?</p>
<p>I notice that there is a Model to Model distance module in 3D Slicer, which might be the same as 3DMeshMetric. However, I found the visualization of suface distance is more fancy with a colorbar.</p>

---

## Post #2 by @lassoan (2019-11-09 13:55 UTC)

<p>Some software have problems with binary mesh files, so you can try to uncheck “Compression” option in Save dialog when exporting.</p>
<p>Yes, you can compute surface metrics within Slicer, too. You can show any color scheme, show color bar, etc. See some more info <a href="https://discourse.slicer.org/t/colour-map-for-model-comparison/8446">here</a>.</p>

---

## Post #3 by @ButuiHu (2019-12-07 10:49 UTC)

<p>Yeah, I have tried uncheck the ‘Compression’ option. But 3DMeshMetric complains that there are unrecognized keywords “METADATA” and “INFORMATION”. After manually delete these lines, it works.</p>

---

## Post #4 by @lassoan (2019-12-07 12:00 UTC)

<aside class="quote no-group" data-username="ButuiHu" data-post="3" data-topic="9094">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/butuihu/48/2386_2.png" class="avatar"> ButuiHu:</div>
<blockquote>
<p>3DMeshMetric complains that there are unrecognized keywords “METADATA” and “INFORMATION”</p>
</blockquote>
</aside>
<p>This seems to be a bug in 3DMeshMetric. Report these errors to its developers, they should be able to fix this very easily.</p>

---
