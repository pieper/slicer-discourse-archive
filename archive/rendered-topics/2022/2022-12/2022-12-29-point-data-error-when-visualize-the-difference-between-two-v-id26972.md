---
topic_id: 26972
title: "Point Data Error When Visualize The Difference Between Two V"
date: 2022-12-29
url: https://discourse.slicer.org/t/26972
---

# Point data error when visualize the difference between two volumetric meshes

**Topic ID**: 26972
**Date**: 2022-12-29
**URL**: https://discourse.slicer.org/t/point-data-error-when-visualize-the-difference-between-two-volumetric-meshes/26972

---

## Post #1 by @suranga (2022-12-29 10:24 UTC)

<p>Hi,</p>
<p>I have two volumetric liver meshes in vtk unstructured grid format (ground-truth and predicted versions) and I’d like to plot the error, i.e., the difference between the ground-truth and predicted liver meshes, on the predicted mesh / mesh coordinates with a different colour (colour code based on displacement magnitudes). The N-th point in the ground-truth mesh correspond to the N-th point in the predicted mesh.</p>
<p>I have attempted to do this by following script however I got an error message as attached below.</p>
<p>Code:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; gtMesh = getNode('gtMesh')
&gt;&gt;&gt; predMesh = getNode('predMesh')
&gt;&gt;&gt; diff_arr = gtMesh - predMesh
&gt;&gt;&gt; gtMesh_np_arr = slicer.util.arrayFromModelPoints(gtMesh)
&gt;&gt;&gt; predMesh_np_arr = slicer.util.arrayFromModelPoints(predMesh)
&gt;&gt;&gt; diff_arr = gtMesh_np_arr - predMesh_np_arr
&gt;&gt;&gt; slicer.util.arrayFromModelPointData(gtMesh, diff_arr)
</code></pre>
<p>Error Message:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/3491e83da211511804915bffce7dc17bd8f5b773.png" data-download-href="/uploads/short-url/7v3qR8fk5JLdEg6gSdtggiKBKtZ.png?dl=1" title="error_msg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/3491e83da211511804915bffce7dc17bd8f5b773.png" alt="error_msg" data-base62-sha1="7v3qR8fk5JLdEg6gSdtggiKBKtZ" width="690" height="83" data-dominant-color="FDF1F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">error_msg</span><span class="informations">1110×135 7.17 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2022-12-31 04:38 UTC)

<p>You need to create a vtk.vtkDoubleArray, fill it with zeros, set its name, and add it as a point data array to the polydata. You can then modify it using <code>slicer.util.arrayFromModelPointData</code> as you did it above.</p>

---

## Post #3 by @suranga (2023-01-04 17:18 UTC)

<p>Meshes are volumetric and have an unstructured grid vtk format. In that case, how can I assign a poly data object to these meshes, given that they are not surface meshes?</p>
<p>I just created poly data object as below with a vtk.vtkDoubleArray, fill it with zeros. However, I cannot add that to the volumetric mesh. Should I extract surface mesh from the volumetric mesh first ?</p>
<pre><code class="lang-auto">gtMesh = getNode('gtMesh')
predMesh = getNode('predMesh')
diff_arr = gtMesh - predMesh
gtMesh_np_arr = slicer.util.arrayFromModelPoints(gtMesh)
predMesh_np_arr = slicer.util.arrayFromModelPoints(predMesh)
diff_arr = gtMesh_np_arr - predMesh_np_arr

shape = np.shape(gtMesh_np_arr)
zeros_np_arr = np.zeros(shape)
vtkdubarr.SetArray(zeros_np_arr, 0, 1)

gtMeshPolyData = gtMesh.GetPolyData()
gtMeshPolyData.GetPointData().AddArray(vtkdubarr)

gtMeshPolyData = vtk.vtkPolyData()
gtMeshPolyData.GetPointData().AddArray(vtkdubarr)
gtMeshPolyData.GetPointData().SetActiveScalars("vtkdubarr")
</code></pre>

---

## Post #4 by @lassoan (2023-01-05 13:50 UTC)

<aside class="quote no-group" data-username="suranga" data-post="3" data-topic="26972">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/8491ac/48.png" class="avatar"> suranga:</div>
<blockquote>
<p><code>gtMesh.GetPolyData()</code></p>
</blockquote>
</aside>
<p>If you work with unstructured grid then you can use the more generic <code>gtMesh.GetMesh()</code> method.</p>

---

## Post #5 by @suranga (2023-01-05 14:30 UTC)

<p>I got poly data from the GetMesh() function, but when I tried slicer.util.arrayFromModelPointData by passing the mesh and the displacement field array, I got ‘only integer scalar arrays can be converted to a scalar index’.</p>
<p>slicer.util.arrayFromModelPointData does not accept the numpy arrays as an arguement?</p>
<p>Code:</p>
<pre><code class="lang-auto">gtMesh = getNode('gtMesh')
predMesh = getNode('predMesh')
diff_arr = gtMesh - predMesh
gtMesh_np_arr = slicer.util.arrayFromModelPoints(gtMesh)
predMesh_np_arr = slicer.util.arrayFromModelPoints(predMesh)
diff_arr = gtMesh_np_arr - predMesh_np_arr

shape = np.shape(gtMesh_np_arr)
zeros_np_arr = np.zeros(shape)
vtkdubarr.SetArray(zeros_np_arr, 0, 1)

gtMesh.GetMesh().GetPointData().AddArray(vtkdubarr)
gtMesh.GetMesh().GetPointData().SetActiveScalars("vtkdubarr")

slicer.util.arrayFromModelPointData(gtMesh, diff_arr)
</code></pre>
<p>Error Message:</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
  File "C:\Users\mnwoki\AppData\Local\NA-MIC\Slicer 5.1.0-2022-07-08\bin\Python\slicer\util.py", line 1722, in arrayFromModelPointData
    arrayVtk = _vtkArrayFromModelData(modelNode, arrayName, 'point')
  File "C:\Users\mnwoki\AppData\Local\NA-MIC\Slicer 5.1.0-2022-07-08\bin\Python\slicer\util.py", line 1706, in _vtkArrayFromModelData
    arrayVtk = modelData.GetArray(arrayName)
TypeError: GetArray argument 1: only integer scalar arrays can be converted to a scalar index
</code></pre>

---

## Post #6 by @lassoan (2023-01-05 14:33 UTC)

<p>Please upload a sample “gtMesh” and “predMesh” files somewhere and post the download link here so that I can test your code snippet.</p>

---

## Post #8 by @suranga (2023-01-06 13:53 UTC)

<p>Can I ask a posibble solution for this please ? Aything missing with the shared files ?</p>

---

## Post #9 by @suranga (2023-01-10 09:28 UTC)

<p>Hi Lassoan,</p>
<p>Could you please provide an update on this matter? Is there anything I’m doing wrong in the code?</p>

---

## Post #10 by @suranga (2023-01-13 15:11 UTC)

<p>I’m still having this problem and am unable to resolve it. Any suggestions, please?</p>

---
