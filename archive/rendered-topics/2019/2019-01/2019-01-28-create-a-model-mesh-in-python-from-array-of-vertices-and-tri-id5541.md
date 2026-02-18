# Create a model/mesh in python from array of vertices and triangles?

**Topic ID**: 5541
**Date**: 2019-01-28
**URL**: https://discourse.slicer.org/t/create-a-model-mesh-in-python-from-array-of-vertices-and-triangles/5541

---

## Post #1 by @stephan (2019-01-28 14:50 UTC)

<p>Hi,<br>
I am trying to create a model in python. The model data, i.e. the raw vertices, vertex normals and triangles, will come from reading a non-standard file format in this extension. (Background: The extension will eventually be able to read data exported from an electroanatomic mapping system such as <a href="http://www.bostonscientific.com/en-US/products/capital-equipment--mapping-and-navigation/rhythmia-mapping-system.html" rel="nofollow noopener">this one</a>.)<br>
I’ve found some guidance <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Accessing_Model_data_as_numpy_array" rel="nofollow noopener">here</a> and <a href="https://vtk.org/doc/nightly/html/classvtkPolyData.html#a34a0f2c07e4464a32cfb30e946a78be2" rel="nofollow noopener">here</a>, but I am stuck.</p>
<p>I’ve tried:</p>
<pre><code>cubeVerts = [[1.0, 1.0, 1.0],
             [1.0, -1.0, 1.0],
             [-1.0, -1.0, 1.0],
             [-1.0, 1.0, 1.0],
             [1.0, 1.0, -1.0],
             [1.0, -1.0, -1.0],
             [-1.0, -1.0, -1.0],
             [-1.0, 1.0, -1.0]]

cubeTris = [[0,1,2],
            [0,2,3],
            [0,1,5],
            [0,5,4],
            [0,4,7],
            [0,7,3],
            [3,2,6],
            [3,6,7],
            [1,5,7],
            [1,6,2],
            [4,5,6],
            [4,6,7]] 

modelNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLModelNode')
modelPolyData = modelNode.GetPolyData()
modelPolyData.SetVerts(cube)
</code></pre>
<p>But since the model created does not contain any points initially, <code>modelPolyData = modelNode.GetPolyData()</code> return nothing and <code>modelPolyData.SetVerts</code> fails with <code>AttributeError: 'NoneType' object has no attribute 'SetVerts'</code>.</p>
<p>I considered using the approach in <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Accessing_Model_data_as_numpy_array" rel="nofollow noopener">this example</a> in the script repository and create a dummy sphere first which is then overwritten by the actual data, but here I ran into another problem: <code>vtkPolyData::SetVerts</code> needs a vtkCellArray and I could not find any member function of this type that simply takes an array of point coordinates together with another array of connectivity information.</p>
<p>I even thought about simply writing out a .vtk file line by line from the python script and re-load it into Slicer, but I am sure there is a more elegant solution…</p>
<p>Any help would be appreciated.</p>
<p>Thanks<br>
Stephan</p>

---

## Post #2 by @stephan (2019-01-28 19:19 UTC)

<p>In the meantime I have found some very valuable additional resources <a href="https://vtk.org/Wiki/VTK/Examples/Python/DataManipulation/Cube.py" rel="nofollow noopener">here</a>, <a href="https://public.kitware.com/pipermail/vtkusers/2004-August/026366.html" rel="nofollow noopener">here</a>, and <a href="http://vtk.1045678.n5.nabble.com/Set-vertex-normals-td5734525.html" rel="nofollow noopener">here</a> and have been able to solve the issue.</p>
<p>If someone has the same question in the future: this was my solution (based on the references above).</p>
<pre><code>def mkVtkIdList(it):
  vil = vtk.vtkIdList()
  for i in it:
    vil.InsertNextId(int(i))
  return vil

def CreateMesh(modeNode, arrayVertices, arrayVertexNormals, arrayTriangles, labelsScalars, arrayScalars):
  # modelNode : a vtkMRMLModelNode in the Slicer scene which will hold the mesh
  # arrayVertices : list of triples [[x1,y1,z2], [x2,y2,z2], ... ,[xn,yn,zn]] of vertex coordinates
  # arrayVertexNormals : list of triples [[nx1,ny1,nz2], [nx2,ny2,nz2], ... ] of vertex normals
  # arrayTriangles : list of triples of 0-based indices defining triangles
  # labelsScalars : list of strings such as ["bipolar", "unipolar"] to label the individual scalars data sets
  # arrayScalars : an array of n rows for n vertices and m colums for m inidividual scalar sets

  # create the building blocks of polydata including data attributes.
  mesh    = vtk.vtkPolyData()
  points  = vtk.vtkPoints()
  normals = vtk.vtkFloatArray()
  polys   = vtk.vtkCellArray()
  
  # load the array data into the respective VTK data structures
  for i in range(len(arrayVertices)):
    points.InsertPoint(i, arrayVertices[i])
  
  for i in range(len(arrayTriangles)):
    polys.InsertNextCell(mkVtkIdList(arrayTriangles[i]))
  
  for i in range(len(arrayVertexNormals)):
    normals.InsertTuple3(i, arrayVertexNormals[i][0], arrayVertexNormals[i][1], arrayVertexNormals[i][2])
  
  # put together the mesh object
  mesh.SetPoints(points)
  mesh.SetPolys(polys)
  if(len(arrayVertexNormals) == len(arrayVertices)):
    mesh.GetPointData().SetNormals(normals)
  
  # Add scalars
  scalars = []
  for j in range(len(labelsScalars)):
    scalars.append(vtk.vtkFloatArray())
    
    for i in range(len(arrayVertices)):
      scalars[j].InsertTuple1(i,arrayScalars[i][j])
    
    scalars[j].SetName(labelsScalars[j])
    mesh.GetPointData().AddArray(scalars[j])
  
  modelNode.SetAndObservePolyData(mesh)</code></pre>

---

## Post #3 by @hyncik (2023-09-08 03:43 UTC)

<p>Thank you for the solution, it saved me a lot of time. Ludek</p>

---
