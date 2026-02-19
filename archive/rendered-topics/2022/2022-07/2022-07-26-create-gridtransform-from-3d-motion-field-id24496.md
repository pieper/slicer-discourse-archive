---
topic_id: 24496
title: "Create Gridtransform From 3D Motion Field"
date: 2022-07-26
url: https://discourse.slicer.org/t/24496
---

# Create GridTransform from 3d motion field

**Topic ID**: 24496
**Date**: 2022-07-26
**URL**: https://discourse.slicer.org/t/create-gridtransform-from-3d-motion-field/24496

---

## Post #1 by @llafitte007 (2022-07-26 11:26 UTC)

<p>Hi,</p>
<p>I am developing a motion estimation module based on an existing library ; the result of the estimate is 3d vector field of type numpy array (shape = (width, height, depth, 3)) plus other fields (origin, spacing, …).</p>
<p>If I save the motion result from my program (nifti format) and open it as Transformation from slicer it works great: the visualization and the registration of motion are great!</p>
<p>My problem comes in the automatic conversion, in the module, of the estimated motion into a GridTransform. Several utils approach the solution (<em>slicer.util.addVolumeFromArray, slicer.util.loadTransform</em>) but nothing that I can’t use for my case. Would there be an equivalent to <em>slicer.util.addVolumeFromArray</em> for GridTransforms (like <em>slicer.util.addGridTransformFromArray</em>) ?</p>
<p>I tried to manually convert motion field and create GridTransform without success:</p>
<pre><code class="lang-auto"># found here https://discourse.slicer.org/t/how-to-convert-3d-numpy-array-to-vtk-and-save-the-vtk-file/22327/3
def numpyToVTK(data):
    data_type = vtk.VTK_FLOAT
    shape = data.shape
    flat_data_array = data.flatten()
    vtk_data = vtk.util.numpy_support.numpy_to_vtk(num_array=flat_data_array, deep=True, array_type=data_type)
    img = vtk.vtkImageData()
    img.GetPointData().SetScalars(vtk_data)
    img.SetDimensions(shape[0], shape[1], shape[2])
    print(img)
    return img

motionNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLGridTransformNode")
motionVtk = numpyToVTK(motionData)
motionNode.GetTransformFromParent().SetDisplacementGridData(motionVtk)
motionNode.GetTransformFromParent().GetDisplacementGrid().SetOrigin(motionOrigin)
motionNode.GetTransformFromParent().GetDisplacementGrid().SetSpacing(motionSpacing)
</code></pre>
<p>Can anyone help me ? Thanks</p>

---

## Post #2 by @pieper (2022-07-26 13:11 UTC)

<p>Here are a couple examples of creating grid transforms in python.  Yes, a utility function could be helpful so if you want to try abstracting this code a PR would be great.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/3328b81211cb2e9ae16a0b49097744171c8c71c0/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L621-L648">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/3328b81211cb2e9ae16a0b49097744171c8c71c0/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L621-L648" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/3328b81211cb2e9ae16a0b49097744171c8c71c0/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L621-L648" target="_blank" rel="noopener">Slicer/Slicer/blob/3328b81211cb2e9ae16a0b49097744171c8c71c0/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L621-L648</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="621" style="counter-reset: li-counter 620 ;">
          <li># create the grid transform node</li>
          <li>gridTransform = slicer.vtkMRMLGridTransformNode()</li>
          <li>gridTransform.SetName('Acquisition Transform')</li>
          <li>slicer.mrmlScene.AddNode(gridTransform)</li>
          <li>
          </li>
<li># create a grid transform with one vector at the corner of each slice</li>
          <li># the transform is in the same space and orientation as the volume node</li>
          <li>gridImage = vtk.vtkImageData()</li>
          <li>gridImage.SetOrigin(*volumeNode.GetOrigin())</li>
          <li>gridImage.SetDimensions(2, 2, slices)</li>
          <li>sourceSpacing = volumeNode.GetSpacing()</li>
          <li>gridImage.SetSpacing(sourceSpacing[0] * columns, sourceSpacing[1] * rows, sourceSpacing[2])</li>
          <li>gridImage.AllocateScalars(vtk.VTK_DOUBLE, 3)</li>
          <li>transform = slicer.vtkOrientedGridTransform()</li>
          <li>directionMatrix = vtk.vtkMatrix4x4()</li>
          <li>volumeNode.GetIJKToRASDirectionMatrix(directionMatrix)</li>
          <li>transform.SetGridDirectionMatrix(directionMatrix)</li>
          <li>transform.SetDisplacementGridData(gridImage)</li>
          <li>gridTransform.SetAndObserveTransformToParent(transform)</li>
          <li>volumeNode.SetAndObserveTransformNodeID(gridTransform.GetID())</li>
      </ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/3328b81211cb2e9ae16a0b49097744171c8c71c0/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L621-L648" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/LandmarkRegistration/blob/master/RegistrationLib/ThinPlatePlugin.py#L83-L118">
  <header class="source">

      <a href="https://github.com/Slicer/LandmarkRegistration/blob/master/RegistrationLib/ThinPlatePlugin.py#L83-L118" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/LandmarkRegistration/blob/master/RegistrationLib/ThinPlatePlugin.py#L83-L118" target="_blank" rel="noopener">Slicer/LandmarkRegistration/blob/master/RegistrationLib/ThinPlatePlugin.py#L83-L118</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="83" style="counter-reset: li-counter 82 ;">
          <li>def onExportGrid(self):</li>
          <li>  """Converts the current thin plate transform to a grid"""</li>
          <li>  state = self.registrationState()</li>
          <li>
          </li>
<li>  # since the transform is ras-to-ras, we find the extreme points</li>
          <li>  # in ras space of the fixed (target) volume and fix the unoriented</li>
          <li>  # box around it.  Sample the grid transform at the resolution of</li>
          <li>  # the fixed volume, which may be a bit overkill but it should aways</li>
          <li>  # work without too much loss.</li>
          <li>  rasBounds = [0,]*6</li>
          <li>  state.fixed.GetRASBounds(rasBounds)</li>
          <li>  from math import floor, ceil</li>
          <li>  origin = list(map(int,map(floor,rasBounds[::2])))</li>
          <li>  maxes = list(map(int,map(ceil,rasBounds[1::2])))</li>
          <li>  boundSize = [m - o for m,o in zip(maxes,origin) ]</li>
          <li>  spacing = state.fixed.GetSpacing()</li>
          <li>  spacing = [max(spacing)*5]*3</li>
          <li>  samples = [ceil(int(b / s)) for b,s in zip(boundSize,spacing)]</li>
          <li>  extent = [0,]*6</li>
          <li>  extent[::2] = [0,]*3</li>
      </ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/Slicer/LandmarkRegistration/blob/master/RegistrationLib/ThinPlatePlugin.py#L83-L118" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
