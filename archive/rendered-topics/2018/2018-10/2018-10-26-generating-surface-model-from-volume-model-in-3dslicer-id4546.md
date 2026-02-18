# Generating Surface model from volume model in 3DSlicer

**Topic ID**: 4546
**Date**: 2018-10-26
**URL**: https://discourse.slicer.org/t/generating-surface-model-from-volume-model-in-3dslicer/4546

---

## Post #1 by @kantzoul (2018-10-26 17:43 UTC)

<p>Hi again,</p>
<p>Following up on the volume fix of the Tympanic membrane model. So I want to extract it (Tympanic membrane) as a surface only and not as a volume. I want to model it as a shell structure.</p>
<p>Kind regards,</p>
<p>Kyprianos</p>

---

## Post #2 by @lassoan (2018-11-01 16:11 UTC)

<p>Segment Editor can only create volumetric segmentation, represented by labelmap or closed surface. In general, this matches reality well (because everything is volumetric in real life).</p>
<p>However, if you want to create abstract models, such as a truly infinitely thin membrane, then you need to use other tools, too.</p>
<p>Probably the simplest solution would be to export the closed surface mesh and edit it (keep only front/back side, fill holes, smooth, etc.) in a mesh modeler, such as Blender or MeshMixer.</p>

---

## Post #3 by @kantzoul (2018-11-13 20:52 UTC)

<p>In the past, other students who worked on this project inquired about this to you. In response, you shared with them a python script which I have attached to this post, and I had also previously referred to in the posting prior to this concerning medical alignment. However I am running into an error as mentioned in the previous posting.</p>
<p>I should note that we do not want to do this necessarily with segment editor.</p>
<p>Python Script:</p>
<pre><code class="lang-auto">volumeNode = getNode('Name of TMlabelmap i.e. SUSAN_SEGMENTATION_R43.nii.nii.nii')
pointFromVolume = vtk.vtkImageDataGeometryFilter()
pointFromVolume.SetInputConnection(volumeNode.GetImageDataConnection())
threshold = vtk.vtkThresholdPoints()
threshold.SetInputConnection(pointFromVolume.GetOutputPort())
threshold.ThresholdByUpper(0.5)
reconstructSurface = vtk.vtkDelaunay2D()
reconstructSurface.SetInputConnection(threshold.GetOutputPort()) reconstructSurface.SetProjectionPlaneMode(vtk.VTK_BEST_FITTING_PLANE)
smoothSurface = vtk.vtkWindowedSincPolyDataFilter()
smoothSurface.SetInputConnection(reconstructSurface.GetOutputPort())
modelsLogic = slicer.modules.models.logic()
modelNode = modelsLogic.AddModel(smoothSurface.GetOutputPort())
modelNode.GetDisplayNode().BackfaceCullingOff() 
</code></pre>
<p>Error message:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d82c9ad12783f99f16d22078aad8079bcbed5014.png" alt="slicer%20python%20error" data-base62-sha1="uQmHkqhrnvQ4ms42wOBvapG5fz6" width="616" height="211"></p>

---

## Post #4 by @lassoan (2018-11-13 21:06 UTC)

<p>In Python, string literals must be enclosed in parentheses. Change <code>getNode(SUSAN...nrrd)</code> to <code>getNode("SUSAN...nrrd")</code>.</p>

---
