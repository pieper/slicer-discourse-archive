---
topic_id: 40986
title: "Export Brainstorm Seeg Coordinates To 3D Slicer"
date: 2025-01-07
url: https://discourse.slicer.org/t/40986
---

# Export Brainstorm seeg coordinates to 3D Slicer

**Topic ID**: 40986
**Date**: 2025-01-07
**URL**: https://discourse.slicer.org/t/export-brainstorm-seeg-coordinates-to-3d-slicer/40986

---

## Post #1 by @stephanejean (2025-01-07 14:26 UTC)

<p>Hello, I have been using 3D slicer for a while now, I would like to export SEEG contact location generate to brainstorm into 3D slicer and convert each contacts into a segment sphere using the xyz coordinates. Is it possible?</p>
<p>I have tried by changing the xyz naming convention into RAS, and then importing the contacts as points using the markups pluggin and it worked, however i can’t transfrom each point into a segment. The markup to model pliggin can only change the points in a connecting curve of tube shape. I want it to remain as location segmented points. Thanks</p>

---

## Post #2 by @lassoan (2025-01-07 14:53 UTC)

<p>Probably the easiest is to describe this using a short Python code snippet. You can generate the code snippet with any AI assistant, you don’t need to know programming or much about Slicer.</p>
<p>For example, I got a working code with giving the following prompts to the free <a href="https://copilot.microsoft.com">Microsoft Copilot</a>:</p>
<blockquote>
<p>write a Python code snippet that converts a markup fiducial list to a segmentation so that at each markup control point position a small sphere shape segment is added</p>
</blockquote>
<p>It almost gave correct result, but it hallucinated a non-existent function, so I tried to make correct itself just by copying the error message that I saw in the Python console in Slicer.</p>
<blockquote>
<p>I got the error: AttributeError: ‘vtkSlicerSegmentationsModuleLogicPython.vtkSlicerS’ object has no attribute ‘CreateLabelmapVolumeFromModel’</p>
</blockquote>
<blockquote>
<p>I got the error: AttributeError: module ‘slicer.util’ has no attribute ‘createLabelVolumeFromModel’</p>
</blockquote>
<blockquote>
<p>I got the error: AttributeError: ‘vtkSegmentationCorePython.vtkSegmentation’ object has no attribute ‘AddSegmentFromClosedSurfaceRepresentation’</p>
</blockquote>
<blockquote>
<p>I got the error: AttributeError: module ‘slicer.util’ has no attribute ‘updateSegmentFromModelPolyData’</p>
</blockquote>
<p>It still did not find the correct converter function, so at this point I decided that I will point it to the Slicer script repository.</p>
<blockquote>
<p>Use examples on this page: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html" class="inline-onebox">Script repository — 3D Slicer documentation</a></p>
</blockquote>
<p>It still did not get it right, so I pinpointed the relevant section.</p>
<blockquote>
<p>Use the code snippet in the section “Create segmentation from a model node”</p>
</blockquote>
<p>This finally generated working code! It was not perfect in that it created an empty segment for each point, so I asked it to correct itself.</p>
<blockquote>
<p>It created an extra empty segment for each point. Please update the code so that it does not generate those extra empty segments.</p>
</blockquote>
<p>Now this generated code that worked perfectly:</p>
<pre data-code-wrap="python"><code class="lang-python">import slicer
import vtk

# Create a segmentation node
segmentation_node = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
segmentation = segmentation_node.GetSegmentation()

# Get the markup fiducial node
markup_node = slicer.util.getNode('F')
n_control_points = markup_node.GetNumberOfFiducials()

# Define sphere parameters
sphere_radius = 5.0  # Adjust the radius as needed
sphere_resolution = 50

# Create a model node for the sphere
sphere_model_node = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLModelNode")
sphere_model_node.SetName("SphereModel")

for i in range(n_control_points):
    # Get the control point position
    position = [0.0, 0.0, 0.0]
    markup_node.GetNthFiducialPosition(i, position)
    
    # Create the sphere
    sphere = vtk.vtkSphereSource()
    sphere.SetCenter(position)
    sphere.SetRadius(sphere_radius)
    sphere.SetThetaResolution(sphere_resolution)
    sphere.SetPhiResolution(sphere_resolution)
    sphere.Update()
    
    # Update the model node with the sphere polydata
    sphere_model_node.SetAndObservePolyData(sphere.GetOutput())
    
    # Add model to segmentation as a new segment
    slicer.modules.segmentations.logic().ImportModelToSegmentationNode(sphere_model_node, segmentation_node)
    
# Remove temporary model node
slicer.mrmlScene.RemoveNode(sphere_model_node)

# Ensure the segmentation displays correctly
segmentation_node.CreateClosedSurfaceRepresentation()
</code></pre>
<p>While having to copy-paste error messages was slightly annoying and ultimately I gave some hints to the chatbot, the whole thing did not take more than 5 minutes and the generated code works and the code quality is not bad at all. And the nice thing is that if you want to do something more or different then you can just keep asking the chatbot to further modify the code.</p>

---

## Post #3 by @stephanejean (2025-01-08 01:18 UTC)

<p>I would like to thank you for the quick and informative answer. I am going to try it and let you know. Thanks again</p>

---

## Post #5 by @stephanejean (2025-01-08 03:54 UTC)

<p>After using my own data and your advice I found this code worked perfectly</p>

---

## Post #6 by @stephanejean (2025-01-08 03:54 UTC)

<p>import slicer<br>
import vtk<br>
import math</p>
<h1><a name="p-121106-volume-of-the-sphere-1" class="anchor" href="#p-121106-volume-of-the-sphere-1" aria-label="Heading link"></a>Volume of the sphere</h1>
<p>sphere_volume = 30  # mm³</p>
<h1><a name="p-121106-calculate-the-radius-2" class="anchor" href="#p-121106-calculate-the-radius-2" aria-label="Heading link"></a>Calculate the radius</h1>
<p>sphere_radius = (3 * sphere_volume / (4 * math.pi)) ** (1/3)</p>
<h1><a name="p-121106-create-a-segmentation-node-3" class="anchor" href="#p-121106-create-a-segmentation-node-3" aria-label="Heading link"></a>Create a segmentation node</h1>
<p>segmentation_node = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLSegmentationNode”)<br>
segmentation = segmentation_node.GetSegmentation()</p>
<h1><a name="p-121106-list-of-provided-positions-4" class="anchor" href="#p-121106-list-of-provided-positions-4" aria-label="Heading link"></a>List of provided positions</h1>
<p>positions = [<br>
(35.49447, 35.492788, -5.868997),<br>
(38.983289, 35.725376, -6.024056),<br>
]</p>
<h1><a name="p-121106-create-spheres-and-add-to-segmentation-5" class="anchor" href="#p-121106-create-spheres-and-add-to-segmentation-5" aria-label="Heading link"></a>Create spheres and add to segmentation</h1>
<p>for i, position in enumerate(positions):<br>
# Create a sphere model node<br>
sphere_model_node = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLModelNode”)<br>
sphere_model_node.SetName(f"Sphere_{i}")</p>
<pre><code># Create the sphere
sphere = vtk.vtkSphereSource()
sphere.SetCenter(position)
sphere.SetRadius(sphere_radius)
sphere.SetThetaResolution(50)
sphere.SetPhiResolution(50)
sphere.Update()

# Update the model node with the sphere polydata
sphere_model_node.SetAndObservePolyData(sphere.GetOutput())

# Add model to segmentation as a new segment
slicer.modules.segmentations.logic().ImportModelToSegmentationNode(sphere_model_node, segmentation_node)
</code></pre>
<h1><a name="p-121106-remove-temporary-model-nodes-6" class="anchor" href="#p-121106-remove-temporary-model-nodes-6" aria-label="Heading link"></a>Remove temporary model nodes</h1>
<p>for i in range(len(positions)):<br>
node = slicer.mrmlScene.GetFirstNodeByClass(“vtkMRMLModelNode”)<br>
slicer.mrmlScene.RemoveNode(node)</p>
<h1><a name="p-121106-ensure-the-segmentation-displays-correctly-7" class="anchor" href="#p-121106-ensure-the-segmentation-displays-correctly-7" aria-label="Heading link"></a>Ensure the segmentation displays correctly</h1>
<p>segmentation_node.CreateClosedSurfaceRepresentation()</p>

---

## Post #7 by @stephanejean (2025-01-08 03:57 UTC)

<p>the only issue is that the processing time is extremely long, even the saving of the 3d slicer scene is long.<br>
Windows 11, 12th Gen Intel(R) Core™ i9-12900   2.40 GHz<br>
RAM 128 GB<br>
3D slicer version 5.2.2</p>

---
