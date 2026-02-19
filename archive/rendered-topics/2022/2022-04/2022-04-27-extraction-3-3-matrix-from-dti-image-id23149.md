---
topic_id: 23149
title: "Extraction 3 3 Matrix From Dti Image"
date: 2022-04-27
url: https://discourse.slicer.org/t/23149
---

# Extraction 3*3 Matrix from DTI Image

**Topic ID**: 23149
**Date**: 2022-04-27
**URL**: https://discourse.slicer.org/t/extraction-3-3-matrix-from-dti-image/23149

---

## Post #1 by @Haytham (2022-04-27 14:00 UTC)

<p>Hi all,</p>
<p>I have a set of patients’ dti images. How do I extract the 3x3 diffusion tensor matrices per each voxel in C++ using VTK?</p>
<p>thank you</p>

---

## Post #2 by @pieper (2022-04-27 14:30 UTC)

<p>You can look at the <a href="https://github.com/Slicer/Slicer/blob/40087afee09fa4779e1b809423d927add1904cb7/Libs/vtkTeem/vtkDiffusionTensorMathematics.cxx"><code>vtkDiffusionTensorMathematics</code></a> source code for examples.</p>

---

## Post #3 by @Haytham (2022-04-29 07:51 UTC)

<p>Hello,<br>
thank you for the responce.<br>
I have a vtkMRMLDiffusionTensorVolumeDisplayNode object, and i need to extract the 3*3 tensor matrix per each voxel.</p>
<p>after that, i can use the vtkDiffusionTensorMathematics to calculate the eigenvalues.<br>
how do I extract for each voxel, the diffusion tensor matrix from a vtkMRMLDiffusionTensorVolumeDisplayNode object?</p>
<p>thank you</p>

---

## Post #4 by @pieper (2022-04-29 12:15 UTC)

<p>You’ll want the <code>vtkMRMLDiffusionTensorVolumeNode</code>, instance (with the image data) not the display node (which stores display parameters).</p>
<p>Once you have that, the <code>vtkImageData</code> has the actual array of tensor values and you can access like in the <code>vtkDiffusionTensorMathematics</code> or like this (in python, but could be converted to C++).</p><aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/util.py#L1610">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/util.py#L1610" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/util.py#L1610" target="_blank" rel="noopener">Slicer/Slicer/blob/master/Base/Python/slicer/util.py#L1610</a></h4>



    <pre class="onebox">      <code class="lang-py">
        <ol class="start lines" start="1600" style="counter-reset: li-counter 1599 ;">
            <li>  import vtk.util.numpy_support</li>
            <li>  narray = None</li>
            <li>  if volumeNode.GetClassName() in scalarTypes:</li>
            <li>    narray = vtk.util.numpy_support.vtk_to_numpy(vimage.GetPointData().GetScalars()).reshape(nshape)</li>
            <li>  elif volumeNode.GetClassName() in vectorTypes:</li>
            <li>    components = vimage.GetNumberOfScalarComponents()</li>
            <li>    if components &gt; 1:</li>
            <li>      nshape = nshape + (components,)</li>
            <li>    narray = vtk.util.numpy_support.vtk_to_numpy(vimage.GetPointData().GetScalars()).reshape(nshape)</li>
            <li>  elif volumeNode.GetClassName() in tensorTypes:</li>
            <li class="selected">    narray = vtk.util.numpy_support.vtk_to_numpy(vimage.GetPointData().GetTensors()).reshape(nshape+(3,3))</li>
            <li>  else:</li>
            <li>    raise RuntimeError("Unsupported volume type: "+volumeNode.GetClassName())</li>
            <li>  return narray</li>
            <li>
            </li>
<li>
            </li>
<li>def arrayFromVolumeModified(volumeNode):</li>
            <li>  """Indicate that modification of a numpy array returned by :py:meth:`arrayFromVolume` has been completed."""</li>
            <li>  imageData = volumeNode.GetImageData()</li>
            <li>  pointData = imageData.GetPointData() if imageData else None</li>
            <li>  if pointData:</li>
        </ol>
      </code>
    </pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
