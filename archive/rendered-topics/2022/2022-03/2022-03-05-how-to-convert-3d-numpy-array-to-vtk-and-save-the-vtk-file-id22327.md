---
topic_id: 22327
title: "How To Convert 3D Numpy Array To Vtk And Save The Vtk File"
date: 2022-03-05
url: https://discourse.slicer.org/t/22327
---

# How to convert 3D numpy array to vtk and save the .vtk file?

**Topic ID**: 22327
**Date**: 2022-03-05
**URL**: https://discourse.slicer.org/t/how-to-convert-3d-numpy-array-to-vtk-and-save-the-vtk-file/22327

---

## Post #1 by @user4 (2022-03-05 18:23 UTC)

<p>Hi,all.Sorry for my little knowledge about VTK.<br>
Here is the thing I want to do:<br>
I have a scalar volume (3D numpy array)<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dc35aee498196792389e5fb04bbc356857db4e3d.png" alt="1646504309(1)" data-base62-sha1="vq43FsloQsHjQY1Y0vDDJM0bApT" width="333" height="90"><br>
I want to add some information describing the image and then save it as a .vtk file as follows:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/daac4e154ebb304b01eaf0cb2db1d7139d57b973.png" alt="image" data-base62-sha1="vctfwkcezoIK8cPjBT7Ywy5zTQ7" width="117" height="117"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6a99a1737008e06fab116e13c41a7484e8986501.png" data-download-href="/uploads/short-url/fd1Ln1IIc8XNlBjYGsQC99PvQIN.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6a99a1737008e06fab116e13c41a7484e8986501.png" alt="image" data-base62-sha1="fd1Ln1IIc8XNlBjYGsQC99PvQIN" width="690" height="163" data-dominant-color="3F4750"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">969×229 22.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
What should I do to achieve this conversion?<br>
Thank you in advance for your attention and help!</p>

---

## Post #2 by @ebrahim (2022-03-07 14:00 UTC)

<p>I don’t know about adding information to a vtk file, but for converting a numpy array to a vtk array format there is <code>vtk.util.numpy_support.numpy_to_vtk</code>; see <a href="https://github.com/Kitware/VTK/blob/0e3d0202115be28c521b3116e664250a8c8368c1/Wrapping/Python/vtkmodules/util/numpy_support.py#L104-L127" rel="noopener nofollow ugc">here</a></p>

---

## Post #3 by @user4 (2022-03-08 09:06 UTC)

<p>yes you are right.</p>
<pre><code class="lang-auto">import vtk.util.numpy_support as numpy_support

def numpyToVTK(data):
    data_type = vtk.VTK_FLOAT
    shape = data.shape

    flat_data_array = data.flatten()
    vtk_data = numpy_support.numpy_to_vtk(num_array=flat_data_array, deep=True, array_type=data_type)
    
    img = vtk.vtkImageData()
    img.GetPointData().SetScalars(vtk_data)
    img.SetDimensions(shape[0], shape[1], shape[2])
    return img
</code></pre>
<p>with the above function I did a quick test below:</p>
<pre><code class="lang-auto">test_arr = np.arange(36).reshape(3,4,3)
test_arr

--&gt; array([[
        [ 0,  1,  2],
        [ 3,  4,  5],
        [ 6,  7,  8],
        [ 9, 10, 11]],

       [[12, 13, 14],
        [15, 16, 17],
        [18, 19, 20],
        [21, 22, 23]],

       [[24, 25, 26],
        [27, 28, 29],
        [30, 31, 32],
        [33, 34, 35]]])
</code></pre>
<p>img = numpyToVTK(data)</p>
<p><strong>Then verify the vtkImageData is right or not</strong></p>
<pre><code class="lang-auto">test = vtk.util.numpy_support.vtk_to_numpy(img.GetPointData().GetScalars())
test = test.reshape(3,4,3)
(test == test_arr).all()

--&gt;True
</code></pre>
<p>However,I’m like you and don’t know how to save the vtk file to the hard drive</p>

---

## Post #4 by @ebrahim (2022-03-08 13:40 UTC)

<p>If you have the array associated to a storable mrml node then you can write it to file <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#save-a-node-to-file" rel="noopener nofollow ugc">as shown here</a>.</p>
<p>To create a volume node out of your numpy array,</p>
<ol>
<li>Add a volume node: <code>volume_node = slicer.mrmlScene.AddNewNodeByClass("vktMRMLScalarVolumeNode")</code>
</li>
<li>Set the values of <code>volume_node</code>'s underlying vtkImageData using <code>slicer.util.updateVolumeFromArray</code> <a href="https://github.com/Slicer/Slicer/blob/41e1adf2a86a18bef376c3220a8125cd034b971e/Base/Python/slicer/util.py#L1958-L1967" rel="noopener nofollow ugc">described here</a>.</li>
</ol>

---

## Post #5 by @user4 (2022-03-10 06:11 UTC)

<p>Thanks, Ebrahim.<br>
Thank you for telling me the way to create the volume node.<br>
However,if I want to save the numpy array as .vtk file,actually it’s quite simple as follows:</p>
<pre><code class="lang-auto">f = open('test.vtk','w') # change your vtk file name
f.write('# vtk DataFile Version 2.0\n')
f.write('test\n')
f.write('ASCII\n')
f.write('DATASET STRUCTURED_POINTS\n')
f.write('DIMENSIONS 3 3 4\n') # change your dimension
f.write('SPACING 0.100000 0.100000 0.100000\n')
f.write('ORIGIN 0 0 0\n')
f.write('POINT_DATA 36\n') # change the number of point data
f.write('SCALARS volume_scalars float 1\n')
f.write('LOOKUP_TABLE default\n')
f.write(numpy_array) # change your numpy array here but need some processing
f.close()
</code></pre>

---

## Post #6 by @koeglfryderyk (2022-04-22 01:38 UTC)

<p>do you maybe have an idea how to do this for a 2D numpy array?</p>

---

## Post #7 by @koeglfryderyk (2022-04-22 01:42 UTC)

<p>Just found out:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://discourse.vtk.org/t/matlab-martix-to-vtkmatrix4x4/1419/3">
  <header class="source">
      <img src="https://discourse.vtk.org/uploads/default/optimized/1X/6c8eb860cf266ca35755a0f95e95251fbe63514d_2_32x32.png" class="site-icon" width="32" height="32">

      <a href="https://discourse.vtk.org/t/matlab-martix-to-vtkmatrix4x4/1419/3" target="_blank" rel="noopener nofollow ugc" title="05:24PM - 25 July 2019">VTK – 25 Jul 19</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/369;"><img src="https://discourse.vtk.org/uploads/default/original/1X/b7d45ff6520965c4fbd148f8d0b1f7720956fa24.png" class="thumbnail" width="690" height="369"></div>

<h3><a href="https://discourse.vtk.org/t/matlab-martix-to-vtkmatrix4x4/1419/3" target="_blank" rel="noopener nofollow ugc">matlab martix to vtkMatrix4x4</a></h3>

  <p>Conversion is possible with the DeepCopy() methods that were originally written to be used with C arrays.  The ndarray.ravel() method returns a flattened view of the numpy array that can be used with DeepCopy:  import numpy as np import vtk  m =...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #8 by @user4 (2022-06-16 02:36 UTC)

<p>Thanks Ebrahim,<br>
In the begining,I just use python open() to write the numpy data,but later I found it is not efficient,taking too long to save large volume.<br>
Your way is better so I have changed the Solution.I have followed your steps to save vtk file on disk but there’s some modification.</p>
<ol>
<li>Create a 3D scalar image just as an example</li>
</ol>
<pre><code class="lang-auto">import numpy as np

numpy_arr = np.arange(1,61)
numpy_arr = numpy_arr.reshape(5,4,3)
numpy_arr.shape
--&gt; (5, 4, 3)
</code></pre>
<ol start="2">
<li>Create a new empty volume</li>
</ol>
<pre><code class="lang-auto">nodeName = "MyNewVolume"
imageSize = [5, 4, 3]
voxelType=vtk.VTK_UNSIGNED_CHAR
imageOrigin = [0.0, 0.0, 0.0]
imageSpacing = [0.1, 0.1, 0.1]
imageDirections = [[1,0,0], [0,1,0], [0,0,1]]
fillVoxelValue = 0

# Create an empty image volume, filled with fillVoxelValue
imageData = vtk.vtkImageData()
imageData.SetDimensions(imageSize)
imageData.AllocateScalars(voxelType, 1)
imageData.GetPointData().GetScalars().Fill(fillVoxelValue)

# Create volume node
volumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode", nodeName)
volumeNode.SetOrigin(imageOrigin)
volumeNode.SetSpacing(imageSpacing)
volumeNode.SetIJKToRASDirections(imageDirections)
volumeNode.SetAndObserveImageData(imageData)
volumeNode.CreateDefaultDisplayNodes()
</code></pre>
<ol start="3">
<li>Update voxels of my volume node from a numpy array</li>
</ol>
<pre><code class="lang-auto">slicer.util.updateVolumeFromArray(volumeNode,numpy_arr)
</code></pre>
<ol start="4">
<li>Save volumeNode to file</li>
</ol>
<pre><code class="lang-auto">myStorageNode = volumeNode.CreateDefaultStorageNode()
myStorageNode.SetFileName("test_data.vtk")
myStorageNode.WriteData(volumeNode)
</code></pre>
<p>It is pretty okay when I open this test_data.vtk to check.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/6161cb7ea218c22ca34595395c182c6c6df6c174.png" data-download-href="/uploads/short-url/dTtQ231K83CO6zsoexGoTOG0Gji.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/6161cb7ea218c22ca34595395c182c6c6df6c174.png" alt="image" data-base62-sha1="dTtQ231K83CO6zsoexGoTOG0Gji" width="690" height="208" data-dominant-color="434B54"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">790×239 8.25 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Also,I have loaded this file in Slicer as follows,<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a3c0465b1dc93dce34978b8bfc0ac4ed76d27c96.png" data-download-href="/uploads/short-url/nmBM1zkpUcnuZWelrhKJyQnJM5o.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a3c0465b1dc93dce34978b8bfc0ac4ed76d27c96_2_304x250.png" alt="image" data-base62-sha1="nmBM1zkpUcnuZWelrhKJyQnJM5o" width="304" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a3c0465b1dc93dce34978b8bfc0ac4ed76d27c96_2_304x250.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a3c0465b1dc93dce34978b8bfc0ac4ed76d27c96_2_456x375.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a3c0465b1dc93dce34978b8bfc0ac4ed76d27c96_2_608x500.png 2x" data-dominant-color="9598CB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">999×819 25.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Then,I get the array back from this volume in order to double check,</p>
<pre><code class="lang-auto">volumeNode = getNode('MyNewVolume')
# volumeNode
a = arrayFromVolume(volumeNode)
a.shape
--&gt; (5, 4, 3)

(a==numpy_arr).all()
--&gt; True
</code></pre>
<p>So, I am pretty sure the data is saved correctly as vtk file.<br>
Thank you very much for your help again,Ebrahim.</p>

---
