# Need help making a 3D mesh given co-ordinates of the vertices and vertex indices of each face for 3D Slicer - trimesh/vtkwrite/etc

**Topic ID**: 24536
**Date**: 2022-07-28
**URL**: https://discourse.slicer.org/t/need-help-making-a-3d-mesh-given-co-ordinates-of-the-vertices-and-vertex-indices-of-each-face-for-3d-slicer-trimesh-vtkwrite-etc/24536

---

## Post #1 by @jsalas424 (2022-07-28 04:27 UTC)

<p>Hi all,</p>
<p>Given the following data:</p>
<ol>
<li>The Cartesian co-ordinates of the vertices in the surface mesh: n vertices x 3</li>
<li>The vertex indices of each face in the surface mesh: n faces x 3</li>
</ol>
<p>I’m trying to make some 3D file that I can readily import to <a href="https://www.slicer.org/" rel="noopener nofollow ugc">3D Slicer</a> for registration against a 2nd VTK file.</p>
<p>Faces: <a href="https://pastebin.com/qWq7aiEs" class="inline-onebox" rel="noopener nofollow ugc">339,263,314340,315,263340,293,315368,314,313368,339,314369,263,33936 - Pastebin.com</a><br>
Vertices: <a href="https://pastebin.com/VxsxsdcM" class="inline-onebox" rel="noopener nofollow ugc">16.215,13.236,126.06516.149,14.237,125.70816.843,13.707,125.85115.178,14.2 - Pastebin.com</a></p>
<p>I have been trying various packages/libraries etc.</p>
<p>I’ve tried  <a href="https://pythonawesome.com/python-library-for-loading-and-using-triangular-meshes/" rel="noopener nofollow ugc">Trimesh in Python</a> and am running into issues probably due to my poor Python ability. I’m opening a <a href="https://stackoverflow.com/questions/73147271/need-help-making-a-3d-mesh-given-co-ordinates-of-the-vertices-and-vertex-indices" rel="noopener nofollow ugc">Stackoverflow question about that separately</a>. I’ve used <a href="https://www.mathworks.com/matlabcentral/fileexchange/47814-vtkwrite-exports-various-2d-3d-data-to-paraview-in-vtk-file-format" rel="noopener nofollow ugc">vtkwrite</a> but the “Precision” option is broken in the package and it’s doing some odd-rounding that is changing the original data too much.</p>
<p>From the <a href="https://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html#supported-data-formats" rel="noopener nofollow ugc">supporting data formats</a> page, it seems like I want something other than VTK that will preserve orientation.</p>
<p>How are ya’ll overcoming this?</p>

---

## Post #2 by @connorh (2022-07-28 14:01 UTC)

<p>I’m no expert but I’ve seen this done with vtkPolydata - if anyone else weighs in I’d defer to them! You can see an example of it here:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/stephan1312/SlicerEAMapReader/blob/2798100fe2aebf482a83b347c1cef18135f2df87/EAMapReader-Slicer-4.11/lib/Slicer-4.11/qt-scripted-modules/EAMapReader.py#L218-L290">
  <header class="source">

      <a href="https://github.com/stephan1312/SlicerEAMapReader/blob/2798100fe2aebf482a83b347c1cef18135f2df87/EAMapReader-Slicer-4.11/lib/Slicer-4.11/qt-scripted-modules/EAMapReader.py#L218-L290" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/stephan1312/SlicerEAMapReader/blob/2798100fe2aebf482a83b347c1cef18135f2df87/EAMapReader-Slicer-4.11/lib/Slicer-4.11/qt-scripted-modules/EAMapReader.py#L218-L290" target="_blank" rel="noopener nofollow ugc">stephan1312/SlicerEAMapReader/blob/2798100fe2aebf482a83b347c1cef18135f2df87/EAMapReader-Slicer-4.11/lib/Slicer-4.11/qt-scripted-modules/EAMapReader.py#L218-L290</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="218" style="counter-reset: li-counter 217 ;">
          <li>def CreateMesh(self, modelNode, arrayVertices, arrayVertexNormals, arrayTriangles, labelsScalars, arrayScalars):
</li>
          <li>  # based on https://vtk.org/Wiki/VTK/Examples/Python/DataManipulation/Cube.py
</li>
          <li>  # modelNode : a vtkMRMLModelNode in the Slicer scene which will hold the mesh
</li>
          <li>  # arrayVertices : list of triples [[x1,y1,z2], [x2,y2,z2], ... ,[xn,yn,zn]] of vertex coordinates
</li>
          <li>  # arrayVertexNormals : list of triples [[nx1,ny1,nz2], [nx2,ny2,nz2], ... ] of vertex normals
</li>
          <li>  # arrayTriangles : list of triples of 0-based indices defining triangles
</li>
          <li>  # labelsScalars : list of strings such as ["bipolar", "unipolar"] to label the individual scalars data sets
</li>
          <li>  # arrayScalars : list of n m-tuples for n vertices and m individual scalar sets
</li>
          <li>  
</li>
          <li>  # create the building blocks of polydata including data attributes.
</li>
          <li>  mesh    = vtk.vtkPolyData()
</li>
          <li>  points  = vtk.vtkPoints()
</li>
          <li>  normals = vtk.vtkFloatArray()
</li>
          <li>  polys   = vtk.vtkCellArray()
</li>
          <li>  
</li>
          <li>  # load the array data into the respective VTK data structures
</li>
          <li>  #self.addLog("  Initializing vertices.")
</li>
          <li>  for i in range(len(arrayVertices)):
</li>
          <li>    points.InsertPoint(i, arrayVertices[i])
</li>
          <li>  
</li>
      </ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/stephan1312/SlicerEAMapReader/blob/2798100fe2aebf482a83b347c1cef18135f2df87/EAMapReader-Slicer-4.11/lib/Slicer-4.11/qt-scripted-modules/EAMapReader.py#L218-L290" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>In this example, a scalar value is assigned to each vertex but I don’t think that’s required for polydata. I’m not sure if you’ll face the same rounding issues you’re having with Trimesh.</p>

---

## Post #3 by @jsalas424 (2022-07-28 15:19 UTC)

<p>Ah back to SlicerEAMapReader, I have a ticket open on that Git due to some issues with the latest version (4.13) and Slicer 5.0.3. Nontheless, the script is helpful, thanks! Looking forward to more input.</p>

---
