---
topic_id: 42181
title: "Best Way To Map Material Properties From Ct Scan To Element"
date: 2025-03-17
url: https://discourse.slicer.org/t/42181
---

# Best way to map material properties from CT scan to Element

**Topic ID**: 42181
**Date**: 2025-03-17
**URL**: https://discourse.slicer.org/t/best-way-to-map-material-properties-from-ct-scan-to-element/42181

---

## Post #1 by @William_Kuo (2025-03-17 02:36 UTC)

<p>Hi!</p>
<p>I am working on a project to map material properties from CT scans to elements. I have been working on a couple ideas. The goal is to get the density of each tetrahedral element for a mesh of a bone that I got from segmenting in 3D Slicer. The goal is to get a good mix of accuracy and computation time.</p>
<ol>
<li>The easiest one is to select the HU values at each node and average them, then divide by the volume of the tetrahedral to get the density. This has accuracy issues because a lot of voxels are not selected. I’ve coded and tested this already.</li>
<li>Next, I can use a lot of integration points to sample multiple HU values inside the tetrahedral in addition to the nodes of the tetrahedral. This is more computationally expensive but captures more voxels. I’ve coded and tested this already.</li>
<li>Lastly, segment the region of each tetrahedral over the CT scan and find the average HU value. I have not been able to code and automate the segmentation of this part by when providing the four nodes (help here; I couldn’t find relevant examples). This seems by far the slowest option because I would have to segment tens of thousands of tetrahedrals. There’s no way this is computationally efficient.</li>
<li>I use integration fields through integration points from trilinear interpolation. I am not familiar with the math but I do know at the integration points and just integration from the 4 points of the tetrahedral. There has been a study on this and is how Bonemat works. However, I have no clue how to implement this. The math seems hard to implement. I even looked at the python version of Bonemat and I can’t seem to figure it out. Paper: <a href="https://pubmed.ncbi.nlm.nih.gov/14644599/" rel="noopener nofollow ugc">https://pubmed.ncbi.nlm.nih.gov/14644599/</a></li>
</ol>
<p>If you guys have experience with this, let me know! I’d love to learn what’s best and what to implement.</p>

---

## Post #2 by @pieper (2025-03-17 18:15 UTC)

<p>You could create a scalar field with the element IDs and use the <a href="https://vtk.org/doc/nightly/html/classvtkProbeFilter.html#details"><code>vtkProbeFilter</code></a> with the CT grid (or subsampled if you want for efficiency) so you would get the id at each voxel.  Then you can easily integrate.</p>
<p>Keep in mind though that if your elements are fairly large compared to the internal structure of the bone then simply averaging the Hu values won’t account for any differences in internal structure.  You may want to include other features, like the variance or some frequency measure.  But everything is an approximation anyway, so it would be good to have some experimental data to use for comparison of whatever technique you choose.</p>

---

## Post #3 by @William_Kuo (2025-03-17 19:36 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="42181">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>You could create a scalar field with the element IDs and use the <a href="https://vtk.org/doc/nightly/html/classvtkProbeFilter.html#details" rel="noopener nofollow ugc"><code>vtkProbeFilter</code></a> with the CT grid (or subsampled if you want for efficiency) so you would get the id at each voxel. Then you can easily integrate.</p>
</blockquote>
</aside>
<p>Is there a way to do this with 3D Slicer functions?</p>

---

## Post #4 by @pieper (2025-03-17 19:37 UTC)

<p>Yes, if you write a python script, it’s easy to access meshes and volume data as numpy arrays.</p>

---

## Post #5 by @William_Kuo (2025-03-17 19:53 UTC)

<aside class="quote no-group" data-username="pieper" data-post="4" data-topic="42181">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>meshes and volume data</p>
</blockquote>
</aside>
<p>I was able to get the points from my mesh and the volume data; however, I don’t see a scripting example that I could use to extract HU from a tetrahedral region of interest. The closest examples I see use functions that support a cube or a sphere. Do you have some advice?</p>

---

## Post #6 by @pieper (2025-03-17 20:07 UTC)

<p>Here’s an example of using a <code>vtkProbeFilter</code> to extract a regular grid of displacements from a tetrahedral mesh.  Extracting the cell IDs would be similar.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/pieper/SlicerSOFA/blob/69f85ffbf8ea55ae5e8f400636d33cfe670f11ce/Experiments/vertebra.py#L231-L256">
  <header class="source">

      <a href="https://github.com/pieper/SlicerSOFA/blob/69f85ffbf8ea55ae5e8f400636d33cfe670f11ce/Experiments/vertebra.py#L231-L256" target="_blank" rel="noopener">github.com/pieper/SlicerSOFA</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/pieper/SlicerSOFA/blob/69f85ffbf8ea55ae5e8f400636d33cfe670f11ce/Experiments/vertebra.py#L231-L256" target="_blank" rel="noopener">Experiments/vertebra.py</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/pieper/SlicerSOFA/blob/69f85ffbf8ea55ae5e8f400636d33cfe670f11ce/Experiments/vertebra.py#L231-L256" rel="noopener"><code>69f85ffbf</code></a>
</div>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="231" style="counter-reset: li-counter 230 ;">
          <li># Set up probe to calculate grid transform</li>
          <li></li>
          <li>probeGrid = vtk.vtkImageData()</li>
          <li>probeDimension = 10</li>
          <li>probeGrid.SetDimensions(probeDimension, probeDimension, probeDimension)</li>
          <li>probeGrid.AllocateScalars(vtk.VTK_DOUBLE, 1)</li>
          <li>meshBounds = [0]*6</li>
          <li>modelNode.GetRASBounds(meshBounds)</li>
          <li>probeGrid.SetOrigin(meshBounds[0], meshBounds[2], meshBounds[4])</li>
          <li>probeSize = (meshBounds[1] - meshBounds[0], meshBounds[3] - meshBounds[2], meshBounds[5] - meshBounds[4])</li>
          <li>probeGrid.SetSpacing(probeSize[0]/probeDimension, probeSize[1]/probeDimension, probeSize[2]/probeDimension)</li>
          <li></li>
          <li>probeFilter = vtk.vtkProbeFilter()</li>
          <li>probeFilter.SetInputData(probeGrid)</li>
          <li>probeFilter.SetSourceData(modelNode.GetUnstructuredGrid())</li>
          <li>probeFilter.SetPassPointArrays(True)</li>
          <li>probeFilter.Update()</li>
          <li></li>
          <li>probeImage = probeFilter.GetOutputDataObject(0)</li>
          <li>probeArray = vtk.util.numpy_support.vtk_to_numpy(probeImage.GetPointData().GetArray("Displacement"))</li>
      </ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/pieper/SlicerSOFA/blob/69f85ffbf8ea55ae5e8f400636d33cfe670f11ce/Experiments/vertebra.py#L231-L256" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>And here’s an example of getting the ct value at the centroid of tetrahedra to define Young’s modulus:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/pieper/SlicerSOFA/blob/69f85ffbf8ea55ae5e8f400636d33cfe670f11ce/Experiments/vertebra.py#L112-L144">
  <header class="source">

      <a href="https://github.com/pieper/SlicerSOFA/blob/69f85ffbf8ea55ae5e8f400636d33cfe670f11ce/Experiments/vertebra.py#L112-L144" target="_blank" rel="noopener">github.com/pieper/SlicerSOFA</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/pieper/SlicerSOFA/blob/69f85ffbf8ea55ae5e8f400636d33cfe670f11ce/Experiments/vertebra.py#L112-L144" target="_blank" rel="noopener">Experiments/vertebra.py</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/pieper/SlicerSOFA/blob/69f85ffbf8ea55ae5e8f400636d33cfe670f11ce/Experiments/vertebra.py#L112-L144" rel="noopener"><code>69f85ffbf</code></a>
</div>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="112" style="counter-reset: li-counter 111 ;">
          <li>ctArray = slicer.util.arrayFromVolume(ctVolume)</li>
          <li></li>
          <li>rasToIJK = vtk.vtkMatrix4x4()</li>
          <li>ctVolume.GetRASToIJKMatrix(rasToIJK)</li>
          <li></li>
          <li>centroidsIJK = []</li>
          <li>for centroid in centroidsArray:</li>
          <li>    centroidH = [*centroid, 1.]</li>
          <li>    centroidIJK = [0.]*4</li>
          <li>    rasToIJK.MultiplyPoint(centroidH, centroidIJK)</li>
          <li>    centroidIJK = list(map(math.floor, centroidIJK))[:3]</li>
          <li>    centroidsIJK.append(centroidIJK)</li>
          <li></li>
          <li>ctMax = ctArray.max()</li>
          <li>ctMean = ctArray.mean()</li>
          <li></li>
          <li>youngModulusBase = 1.5</li>
          <li>youngModulusArray = numpy.ones(centroidsArray.shape[0]) * youngModulusBase</li>
          <li></li>
          <li>for elementIndex in range(len(youngModulusArray)):</li>
      </ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/pieper/SlicerSOFA/blob/69f85ffbf8ea55ae5e8f400636d33cfe670f11ce/Experiments/vertebra.py#L112-L144" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Here’s how you create cell scalars array:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/pieper/SlicerSOFA/blob/69f85ffbf8ea55ae5e8f400636d33cfe670f11ce/Experiments/vertebra.py#L146-L151">
  <header class="source">

      <a href="https://github.com/pieper/SlicerSOFA/blob/69f85ffbf8ea55ae5e8f400636d33cfe670f11ce/Experiments/vertebra.py#L146-L151" target="_blank" rel="noopener">github.com/pieper/SlicerSOFA</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/pieper/SlicerSOFA/blob/69f85ffbf8ea55ae5e8f400636d33cfe670f11ce/Experiments/vertebra.py#L146-L151" target="_blank" rel="noopener">Experiments/vertebra.py</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/pieper/SlicerSOFA/blob/69f85ffbf8ea55ae5e8f400636d33cfe670f11ce/Experiments/vertebra.py#L146-L151" rel="noopener"><code>69f85ffbf</code></a>
</div>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="146" style="counter-reset: li-counter 145 ;">
          <li># create a stress array</li>
          <li></li>
          <li>stressVTKArray = vtk.vtkFloatArray()</li>
          <li>stressVTKArray.SetNumberOfValues(grid.GetNumberOfCells())</li>
          <li>stressVTKArray.SetName("VonMisesStress")</li>
          <li>modelNode.GetUnstructuredGrid().GetCellData().AddArray(stressVTKArray)</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>So you would need to mix these together so you would get a labelmap of the cell IDs at each pixel and then you could map that info into your Young’s modulus map.</p>
<p>Let us know how it goes for you.  These scripts are just experiments so far, but at somepoint we’ll want to have some useful high-level functionality for this kind of thing.</p>

---

## Post #7 by @William_Kuo (2025-03-17 22:18 UTC)

<p>This is my current script. It’s able to take coordinates of nodes from a numpy array and get the voxel value at any coord point I input. This includes centroids and other integration points.</p>
<pre><code class="lang-auto"># import slicer
import slicer
import numpy as np
import csv
import time
nodes_coords = np.load(r"\node_Array.npy")

# Get your bone mask segment
volumeNode = slicer.util.getNode('Bone_Scan')  

for row in nodes_coords:
	# Get point coordinate in RAS
	x = row[0] * -1
	y = row[1] * -1
	z = row[2]
	point_Ras = [x,y,z]

	# If volume node is transformed, apply that transform to get volume's RAS coordinates
	transformRasToVolumeRas = vtk.vtkGeneralTransform()
	slicer.vtkMRMLTransformNode.GetTransformBetweenNodes(None, volumeNode.GetParentTransformNode(), transformRasToVolumeRas)
	point_VolumeRas = transformRasToVolumeRas.TransformPoint(point_Ras)

	# Get voxel coordinates from physical coordinates
	volumeRasToIjk = vtk.vtkMatrix4x4()
	volumeNode.GetRASToIJKMatrix(volumeRasToIjk)
	point_Ijk = [0, 0, 0, 1]
	volumeRasToIjk.MultiplyPoint(np.append(point_VolumeRas,1.0), point_Ijk)
	point_Ijk = [ int(round(c)) for c in point_Ijk[0:3] ]

	voxelValue = voxels[point_Ijk[2], point_Ijk[1], point_Ijk[0]]  # note that numpy array index order is kji (not ijk)
	
	# print(row)
	# print(point_Ras)
	# print(point_Ijk)
	# print(voxelValue)
</code></pre>
<p>I want to extract the voxel values within 4 points of a tetrahedral. Is there a method to apply a label map, segmentation, or ROI within the tetrahedral for me to extract the values?</p>

---

## Post #8 by @pieper (2025-03-17 22:51 UTC)

<aside class="quote no-group" data-username="William_Kuo" data-post="7" data-topic="42181">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/william_kuo/48/65525_2.png" class="avatar"> William_Kuo:</div>
<blockquote>
<p>Is there a method to apply a label map, segmentation, or ROI within the tetrahedral for me to extract the values?</p>
</blockquote>
</aside>
<p>Yes, you can use the method I described above.</p>

---

## Post #9 by @William_Kuo (2025-03-17 23:11 UTC)

<p>I get this error when I try to run your first example.</p>
<pre><code class="lang-auto">    typ = vtk_array.GetDataType()
AttributeError: 'NoneType' object has no attribute 'GetDataType'
[VTK] Input port 1 of algorithm vtkProbeFilter (000001F4B8128160) has 0 connections but is not optional.
</code></pre>
<p>This is my code:</p>
<pre><code class="lang-auto">import slicer
import numpy as np
import csv
import time
import math

# Get your bone mask segment
ctVolume = slicer.util.getNode('Bone_Scan')    
modelNode = slicer.util.getNode('Result')  

probeGrid = vtk.vtkImageData()
probeDimension = 10
probeGrid.SetDimensions(probeDimension, probeDimension, probeDimension)
probeGrid.AllocateScalars(vtk.VTK_DOUBLE, 1)
meshBounds = [0]*6
modelNode.GetRASBounds(meshBounds)
probeGrid.SetOrigin(meshBounds[0], meshBounds[2], meshBounds[4])
probeSize = (meshBounds[1] - meshBounds[0], meshBounds[3] - meshBounds[2], meshBounds[5] - meshBounds[4])
probeGrid.SetSpacing(probeSize[0]/probeDimension, probeSize[1]/probeDimension, probeSize[2]/probeDimension)
probeFilter = vtk.vtkProbeFilter()
probeFilter.SetInputData(probeGrid)
probeFilter.SetSourceData(modelNode.GetUnstructuredGrid())
probeFilter.SetPassPointArrays(True)
probeFilter.Update()
probeImage = probeFilter.GetOutputDataObject(0)
probeArray = vtk.util.numpy_support.vtk_to_numpy(probeImage.GetPointData().GetArray("Displacement"))
</code></pre>
<p>I’m thinking maybe it’s because we are using different scan regions so it’s not picking up the grid.</p>

---

## Post #10 by @pieper (2025-03-18 00:22 UTC)

<p>Yes, you’ll need to debug it.  I don’t have a script that does exactly what you are asking for.</p>

---
