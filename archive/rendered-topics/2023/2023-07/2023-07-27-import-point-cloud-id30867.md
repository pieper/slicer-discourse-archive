# Import point cloud

**Topic ID**: 30867
**Date**: 2023-07-27
**URL**: https://discourse.slicer.org/t/import-point-cloud/30867

---

## Post #1 by @jessdtate (2023-07-27 16:44 UTC)

<p>I’m having trouble generalizing this solution to unstructured point clouds.  I have an example text file with x, y, z values <a href="https://github.com/SCIInstitute/ShapeWorks/blob/master/Testing/data/ellipsoid_particles/seg.ellipsoid_0.isores.pad.com.aligned.cropped.tpSmoothDT_world.particles" rel="noopener nofollow ugc">here</a>.  I can read them as an numpy array easily enough, and I noticed that there is a new PointSet vtk data type.  Is that the way to do this now?</p>

---

## Post #2 by @lassoan (2023-07-29 15:19 UTC)

<p>You can import and visualize point clouds in Slicer by creating a model node and loading the points into its <code>vtkPolyData</code> object:</p>
<ul>
<li>Create a vkPolyData object and set its points coordinates from numpy array</li>
<li>Add a vertex cell at each point (or use vtkGlyph3D filter to add a small sphere or other object at each point position) to make something visible at those point positions</li>
<li>Create a model node from the polydata object</li>
</ul>
<p>Since VTK is widely used, has a logical and consistent API, documentation, and examples, you can usually generate fully functional Python code for it using bing chat or ChatGPT.</p>
<p>For example, bing chat <code>generate python code that creates a vtk point cloud from numpy array and generates a polydata from it by adding a small sphere at each point</code>:</p>
<pre><code class="lang-python">import vtk
import numpy as np

# Create a random point cloud.
points = np.random.rand(1000, 3) * 100

# Create the vtkPoints object.
vtk_points = vtk.vtkPoints()
vtk_points.SetData(vtk.util.numpy_support.numpy_to_vtk(points))

# Create the vtkPolyData object.
polydata = vtk.vtkPolyData()
polydata.SetPoints(vtk_points)

# Create the vtkSphereSource object.
sphere = vtk.vtkSphereSource()
sphere.SetRadius(2.0)

# Create the vtkGlyph3D object.
glyph = vtk.vtkGlyph3D()
glyph.SetInputData(polydata)
glyph.SetSourceConnection(sphere.GetOutputPort())
</code></pre>
<p>To display this point cloud in Slicer, you can do this:</p>
<pre><code class="lang-python">pointCloudModelNode = slicer.modules.models.logic().AddModel(glyph.GetOutputPort())
</code></pre>

---
