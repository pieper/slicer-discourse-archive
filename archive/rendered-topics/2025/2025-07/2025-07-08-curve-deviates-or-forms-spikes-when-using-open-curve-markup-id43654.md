---
topic_id: 43654
title: "Curve Deviates Or Forms Spikes When Using Open Curve Markup"
date: 2025-07-08
url: https://discourse.slicer.org/t/43654
---

# Curve deviates or forms spikes when using Open Curve Markup Tool

**Topic ID**: 43654
**Date**: 2025-07-08
**URL**: https://discourse.slicer.org/t/curve-deviates-or-forms-spikes-when-using-open-curve-markup-tool/43654

---

## Post #1 by @LJW (2025-07-08 12:46 UTC)

<p>Hi,</p>
<p>I’m using the Open Curve Markup Tool in 3D Slicer to create curves on a surface model, such as between the mesial and distal papilla of a tooth. To support this, I’m also calculating and visualizing minimum curvature using the following Python code in the Python Interactor:</p>
<pre><code class="lang-auto">-----------------------------------------------------------------
modelNode = getNode('DB')

import vtk
curv = vtk.vtkCurvatures()
curv.SetInputData(modelNode.GetPolyData())
curv.SetCurvatureTypeToMinimum()

modelNode.SetPolyDataConnection(curv.GetOutputPort())
modelNode.GetDisplayNode().SetActiveScalar("Minimum_Curvature", vtk.vtkAssignAttribute.POINT_DATA)
modelNode.GetDisplayNode().SetScalarVisibility(True)
-----------------------------------------------------------------
</code></pre>
<p>In the Markups module (Create open curve markup), I’m setting:</p>
<ul>
<li>Curve type: Shortest distance on surface</li>
<li>Model node: the surface model</li>
<li>Cost function: Inverse squared</li>
<li>Weighting: distance / curvature</li>
</ul>
<p>The problem is that the generated curve sometimes deviates in unexpected directions, even when the path seems straightforward. When I try to correct it by manually adding control points (Ctrl + click), the curve often becomes worse, with sharp spikes or unnatural shapes.</p>
<p>Is there any way to prevent this kind of behavior or improve the curve stability when editing?</p>
<p>Thanks.</p>

---
