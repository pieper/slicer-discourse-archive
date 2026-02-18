# Method Requires VTK Object Error

**Topic ID**: 18386
**Date**: 2021-06-29
**URL**: https://discourse.slicer.org/t/method-requires-vtk-object-error/18386

---

## Post #1 by @Bastien_Saunois (2021-06-29 08:08 UTC)

<p>I am implementing the extract Network algorithm, but I get an issue with this line :</p>
<pre><code class="lang-auto">networkExtraction.SetInputData(surfacePolyData)
</code></pre>
<p>I get this error :</p>
<pre><code class="lang-auto">method requires a VTK object
</code></pre>
<p>I saw on some forums that it could come from a conflict between 2 versions of vtk, is there something else that could raise this error ?</p>
<p>Here is the code I am writing :</p>
<pre><code>def extractNetwork(self,surfacePolyData):

    cleaner = vtk.vtkCleanPolyData()

    cleaner.SetInputData(surfacePolyData)
    triangleFilter = vtk.vtkTriangleFilter()
    triangleFilter.SetInputConnection(cleaner.GetOutputPort())
    triangleFilter.Update()
    simplifiedPolyData = triangleFilter.GetOutput()

    bounds = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    surfacePolyData.GetBounds(bounds)
    startPosition = [bounds[0], bounds[2], bounds[4]]

    self.openSurfaceAtPoint(surfacePolyData,startPosition)

    # Extract network
    networkExtraction = vtkvmtkMisc.vtkvmtkPolyDataNetworkExtraction()
    networkExtraction.SetInputData(simplifiedPolyData)
    networkExtraction.SetAdvancementRatio(1.05)
    networkExtraction.SetRadiusArrayName(self.radiusArrayName)
    networkExtraction.SetTopologyArrayName(self.topologyArrayName)
    networkExtraction.SetMarksArrayName(self.marksArrayName)
    networkExtraction.Update()

    return networkExtraction.GetOutput()
</code></pre>
<p>Bastien</p>

---

## Post #2 by @lassoan (2021-06-30 02:48 UTC)

<p>Are you sure that <code>surfacePolyData</code> is a valid VTK object? How did you generate it? What do you see if you call <code>print(surfacePolyData)</code>?</p>

---

## Post #3 by @Bastien_Saunois (2021-06-30 08:42 UTC)

<p>Thanks for the quick reply <a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>I created the mesh that way and I directly used it as input for my extraction of the network :</p>
<pre><code class="lang-auto">def Addmesh( self, Matrixvertices :float, Matrixtriangle: float)-&gt;vars:
        """
        Input :
        Matrixvertices = [[x0,y0,z0],...,[xn,yn,zn]]
        --&gt; Contains the points (n points)
        Matrixshape = [xid0,yid0,zid0,...,xidp,yidp,zidp]
        --&gt; Contains the triplet of ids giving a triangle (p triangles)
        Ouput : 
        actor --&gt; Actor which contains the mesh of our object
        """       
        # Define points, triangles and colors
        points = vtk.vtkPoints()
        triangles = vtk.vtkCellArray()
        #Add the different points to the mesh
        for i in range(len(Matrixvertices)):
            points.InsertNextPoint(Matrixvertices[i][0], Matrixvertices[i][1], Matrixvertices[i][2])
        
        #Add the Ids of the point to create the triangle cells.
        cmpt=0
        for i in range(int(len(Matrixtriangle)/3)): 

            triangle = vtk.vtkTriangle()
            triangle.GetPointIds().SetId(0, Matrixtriangle.astype(int)[cmpt])
            triangle.GetPointIds().SetId(1, Matrixtriangle.astype(int)[1+cmpt])
            triangle.GetPointIds().SetId(2, Matrixtriangle.astype(int)[2+cmpt])
            triangles.InsertNextCell(triangle)
            cmpt+=3

        #Creation of polydata object
        trianglePolyData = vtk.vtkPolyData()
        filler = vtk.vtkFillHolesFilter()

        # Add the geometry and topology to the polydata
        trianglePolyData.SetPoints(points)
        trianglePolyData.SetPolys(triangles)
</code></pre>
<p>(I notice there could be an error because I am defining an open surface as mesh, but I also tried with a closed surface the same way as the examples of Slicer, and I still had the error)</p>
<p>And if I use <code>print(surfacePolyData)</code>  I get this :</p>
<pre><code class="lang-auto">vtkPolyData (000002827B4CCA80) 
  Debug: Off
  Modified Time: 9882
  Reference Count: 3
  Registered Events: (none)
  Information: 000002827B61F6F0
  Data Released: False
  Global Release Data: Off
  UpdateTime: 10991
  Field Data:
    Debug: Off
    Modified Time: 9864
    Reference Count: 1
    Registered Events: (none)
    Number Of Arrays: 0
    Number Of Components: 0
    Number Of Tuples: 0
  Number Of Points: 192
  Number Of Cells: 95
  Cell Data:
    Debug: Off
    Modified Time: 9867
    Reference Count: 1
    Registered Events:
      Registered Observers:
        vtkObserver (000002827B591EA0)
          Event: 33
          EventName: ModifiedEvent
          Command: 000002827B61ECF0
          Priority: 0
          Tag: 1
    Number Of Arrays: 0
    Number Of Components: 0
    Number Of Tuples: 0
    Copy Tuple Flags: ( 1 1 1 1 1 0 1 1 )
    Interpolate Flags: ( 1 1 1 1 1 0 0 1 )
    Pass Through Flags: ( 1 1 1 1 1 1 1 1 )
    Scalars: (none)
    Vectors: (none)
    Normals: (none)
    TCoords: (none)
    Tensors: (none)
    GlobalIds: (none)
    PedigreeIds: (none)
    EdgeFlag: (none)
  Point Data:
    Debug: Off
    Modified Time: 9866
    Reference Count: 1
    Registered Events:
      Registered Observers:
        vtkObserver (000002827B592530)
          Event: 33
          EventName: ModifiedEvent
          Command: 000002827B61ECF0
          Priority: 0
          Tag: 1
    Number Of Arrays: 0
    Number Of Components: 0
    Number Of Tuples: 0
    Copy Tuple Flags: ( 1 1 1 1 1 0 1 1 )
    Interpolate Flags: ( 1 1 1 1 1 0 0 1 )
    Pass Through Flags: ( 1 1 1 1 1 1 1 1 )
    Scalars: (none)
    Vectors: (none)
    Normals: (none)
    TCoords: (none)
    Tensors: (none)
    GlobalIds: (none)
    PedigreeIds: (none)
    EdgeFlag: (none)
  Bounds:
    Xmin,Xmax: (-0.91, -0.69)
    Ymin,Ymax: (-0.11, 0.11)
    Zmin,Zmax: (-0.7, -0.6)
  Compute Time: 11035
  Number Of Points: 192
  Point Coordinates: 000002827B619890
  Locator: 0000000000000000
  Number Of Vertices: 0
  Number Of Lines: 0
  Number Of Polygons: 95
  Number Of Triangle Strips: 0
  Number Of Pieces: 1
  Piece: 0
  Ghost Level: 0
</code></pre>

---

## Post #4 by @Bastien_Saunois (2021-07-08 10:18 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> I’m sorry to follow up, but I couldn’t find an answer to this error so I’m still stuck.</p>

---
