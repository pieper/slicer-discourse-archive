# How to Create a zero thickness plane in 3D slicer?

**Topic ID**: 20743
**Date**: 2021-11-23
**URL**: https://discourse.slicer.org/t/how-to-create-a-zero-thickness-plane-in-3d-slicer/20743

---

## Post #1 by @Sliceeeeee (2021-11-23 08:12 UTC)

<p>Hello</p>
<p>I have made 3d model of nasal cavity ,now I want to add another segment in which I will create a plane surface with zero thickness , how can I do that?</p>

---

## Post #2 by @mau_igna_06 (2021-11-23 12:52 UTC)

<p>If you want a model. You can add a modelNode to the scene and set its polydata from <code>vtk.vtkPlaneSource()</code></p>
<p>I’m sure you’ll find vtk examples on how to use that filter and you can use this from the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#define-edit-a-circular-region-of-interest-in-a-slice-viewer">scriptRepository</a>:</p>
<pre><code class="lang-auto"># Create model node and add to scene
modelsLogic = slicer.modules.models.logic()
model = modelsLogic.AddModel(sphere.GetOutput())
</code></pre>
<p>Instead of sphere it should be your plane.</p>

---

## Post #4 by @Sliceeeeee (2021-11-23 07:12 UTC)

<p>Hello Sir</p>
<p>How can I make a plane of zero thickness in 3D slicer ?</p>

---

## Post #5 by @lassoan (2021-11-23 15:29 UTC)

<p>Markups plane node is a plane of zero thickness.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3b46f6ac860bbe42adfa5919de59125d9214802a.png" data-download-href="/uploads/short-url/8socZkFTF8yTjh42wbQ0HBbxdG2.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3b46f6ac860bbe42adfa5919de59125d9214802a_2_690x390.png" alt="image" data-base62-sha1="8socZkFTF8yTjh42wbQ0HBbxdG2" width="690" height="390" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3b46f6ac860bbe42adfa5919de59125d9214802a_2_690x390.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3b46f6ac860bbe42adfa5919de59125d9214802a_2_1035x585.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3b46f6ac860bbe42adfa5919de59125d9214802a_2_1380x780.png 2x" data-dominant-color="CCCDE2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1672×946 87.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @Sliceeeeee (2021-11-23 15:42 UTC)

<p>But can I export this plane as a STL geometry , how can I do that please help</p>

---

## Post #7 by @lassoan (2021-11-23 16:05 UTC)

<p>You can save the plane as a json file, which contains the plane position and normal, size, etc. You can also create a model node from the markup node using this code snippet that can be saved as STL, PLY, etc. file format:</p>
<pre><code class="lang-python">planeNode = getNode('P')

# Get plane geometry
import numpy as np
origin = np.array(planeNode.GetOriginWorld())
axisX = np.zeros(3)
axisY = np.zeros(3)
axisZ = np.zeros(3)
planeNode.GetAxesWorld(axisX, axisY, axisZ)
corner = origin - 0.5 * size[0]*axisX - 0.5 * size[1]*axisY
size = planeNode.GetSize()

# Create polygonal mesh model that can be saved as ply, obj, stl,... file
planeSource = vtk.vtkPlaneSource()
planeSource.SetOrigin(corner)
planeSource.SetPoint1(corner+size[0]*axisX)
planeSource.SetPoint2(corner+size[1]*axisY)
planeModel = slicer.modules.models.logic().AddModel(planeSource.GetOutputPort())
</code></pre>
<p>Why do you need this plane as an STL file?</p>

---

## Post #8 by @Sliceeeeee (2021-11-23 18:55 UTC)

<p>Where should I write the code? I am not getting any option</p>

---

## Post #9 by @Sliceeeeee (2021-11-24 05:30 UTC)

<p>I need this plane because i will use this plane to select patches in my geometry for giving boundary conditions</p>

---

## Post #10 by @lassoan (2021-11-24 13:43 UTC)

<p>Your can open the Python console from the View menu.</p>

---

## Post #11 by @mau_igna_06 (2022-12-22 22:33 UTC)

<p>This code works for any <a href="https://apidocs.slicer.org/master/classvtkMRMLMarkupsPlaneNode.html" rel="noopener nofollow ugc">vtkMRMLMarkupsPlaneNode</a> <em>(any sizeMode, any planeType)</em>:</p>
<pre><code class="lang-auto">planeNode = getNode('P')

cornerPoints = vtk.vtkPoints()
planeNode.GetPlaneCornerPoints(cornerPoints)

from vtk.util.numpy_support import vtk_to_numpy
cornerPoints_np = vtk_to_numpy(cornerPoints.GetData())

import numpy as np
def sort_points(pts):
    """Sort 4 points in a winding order"""
    pts = np.array(pts)
    centroid = np.sum(pts, axis=0) / pts.shape[0]
    vector_from_centroid = pts - centroid
    vector_angle = np.arctan2(
        vector_from_centroid[:, 1], vector_from_centroid[:, 0])
    # Find the indices that give a sorted vector_angle array
    sort_order = np.argsort(-vector_angle)
    # Apply sort_order to original pts array.
    return list(sort_order)

order = sort_points(cornerPoints_np)

# Create polygonal mesh model that can be saved as ply, obj, stl,... file
planeSource = vtk.vtkPlaneSource()
planeSource.SetOrigin(cornerPoints_np[order[0]])
planeSource.SetPoint1(cornerPoints_np[order[1]])
planeSource.SetPoint2(cornerPoints_np[order[-1]])
planeModel = slicer.modules.models.logic().AddModel(planeSource.GetOutputPort())
</code></pre>
<p>Hope it helps</p>

---

## Post #12 by @VincentYu (2023-07-12 02:40 UTC)

<pre><code class="lang-auto">corner = origin - 0.5 * size[0]*axisX - 0.5 * size[1]*axisY
size = planeNode.GetSize()
</code></pre>
<p>These two lines seems have to be swapped since the variable “size” is used before defined?<br>
Thank you, prof. Lasso, this code is helpful !</p>

---
