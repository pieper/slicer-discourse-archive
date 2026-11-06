---
topic_id: 48748
title: "Controlling Chordal Decimation & Preventing Non-Manifold Edges When Exporting 3D Slicer Segmentations to CAD STEP/STL"
date: 2026-11-06
url: https://discourse.slicer.org/t/48748
last_bumped: 2026-11-06T05:11:01.148Z
---

# Controlling Chordal Decimation & Preventing Non-Manifold Edges When Exporting 3D Slicer Segmentations to CAD STEP/STL

**Topic ID**: 48748
**Date**: 2026-11-06
**URL**: https://discourse.slicer.org/t/controlling-chordal-decimation-preventing-non-manifold-edges-when-exporting-3d-slicer-segmentations-to-cad-step-stl/48748

---

## Post #1 by @cadguide (2026-11-06 05:11 UTC)

<p>When converting segmented DICOM anatomical volumes (such as patient-specific cranial implants or orthopedic surgical guides) from 3D Slicer’s Segment Editor into closed STL meshes for downstream CAD modeling, Flying Edges smoothing often produces dense triangle counts that overwhelm parametric B-Rep kernels.</p>
<p>To preserve sub-millimeter anatomical fidelity while ensuring 100% manifold edges for boolean operations:</p>
<pre data-code-wrap="python"><code class="lang-python">segmentationNode = getNode('Segmentation')
exporter = slicer.vtkSlicerSegmentationsModuleLogic()
# Verify surface decimation preserves closed manifold topology
surfaceMesh = segmentationNode.GetClosedSurfaceInternalRepresentation('Bone_Segment')
featureEdges = vtk.vtkFeatureEdges()
featureEdges.SetInputData(surfaceMesh)
featureEdges.BoundaryEdgesOn()
featureEdges.NonManifoldEdgesOn()
featureEdges.Update()
print("Open/Non-manifold edge count:", featureEdges.GetOutput().GetNumberOfCells())
</code></pre>
<p>Before importing anatomical STL meshes into SolidWorks or FreeCAD for fixture design, you can also audit triangle aspect ratios and chordal deflection tolerances using our browser-based <a href="https://cadguide.tools/toolbox/3d-printing-chordal-deviation" rel="noopener nofollow ugc">CADGuide.tools 3D Printing Chordal Deviation &amp; STL Checker</a>.</p>
<p>What surface smoothing factor in 3D Slicer 5.6+ gives the cleanest quad-remeshing baseline for reverse-engineering into NURBS patches?</p>

---

## Post #2 by @discourse_ai_spam (2026-11-06 05:11 UTC)



---
