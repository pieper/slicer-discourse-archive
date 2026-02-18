# Surface Measurements & Model Comparison in 3D Slicer

**Topic ID**: 44264
**Date**: 2025-08-29
**URL**: https://discourse.slicer.org/t/surface-measurements-model-comparison-in-3d-slicer/44264

---

## Post #1 by @Faisal_Alshaikh (2025-08-29 17:05 UTC)

<p>Hello everyone,</p>
<p>I am currently testing 3D Slicer with <strong>surface models exported from the Vectra H2 system (.obj format with texture)</strong>. The models import and display correctly in the 3D view, but I could not find direct options for:</p>
<ul>
<li>
<p><strong>surface-area measurement</strong> of freely selected regions (e.g. around the eyes),</p>
</li>
<li>
<p><strong>automatic difference calculation / distance mapping</strong> between two surface models (e.g. before vs. after treatment).</p>
</li>
</ul>
<p>So far, model comparison seems limited to manual alignment using transforms. I could not find an automatic registration tool or quantitative difference mapping (heatmap) for OBJ surface meshes.</p>
<p>My questions are:</p>
<ul>
<li>
<p>Does 3D Slicer support surface-area measurements for OBJ meshes?</p>
</li>
<li>
<p>Is there a way to perform automatic comparison (registration + difference/heatmap) between two surface models?</p>
</li>
<li>
<p>Are there modules, extensions, or Python scripts that can be used for this workflow?</p>
</li>
</ul>
<p>Any advice, references, or example workflows would be greatly appreciated.</p>
<p>Thank you!</p>

---

## Post #2 by @lassoan (2025-08-29 17:12 UTC)

<p>You can see the surface area of a model in <code>Models</code> module → <code>Information</code> section.</p>
<p>If you are interested in a specific region then you can use <code>Dynamic modeler</code> module to extract a region of the model. There are several tool to choose from: <code>Plane cut</code> defines a region by a one or more planes, <code>Curve cut</code> allows you to specify a surface region by a closed curve, <code>Boundary cut</code> allows using several node types (curves, planes, etc), <code>ROI cut</code> works for markup ROI boxes, <code>Select by points</code> can select a region using Euclidean or geodesic distance from points.</p>
<p>You can compute distances between surfaces using <code>ModelToModelDistance</code> extension.</p>
<p><code>ModelToModelDistance</code> computes distances and stores them as point scalars in the model, which then you can use for computing statistics, crop the model, etc. - using a few Python commands that you can run directly in Slicer’s Python console.</p>

---
