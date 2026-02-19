---
topic_id: 24880
title: "Orienting A Cylinder Model Using Vtk"
date: 2022-08-23
url: https://discourse.slicer.org/t/24880
---

# Orienting a cylinder model using vtk

**Topic ID**: 24880
**Date**: 2022-08-23
**URL**: https://discourse.slicer.org/t/orienting-a-cylinder-model-using-vtk/24880

---

## Post #1 by @SegmentedYannig (2022-08-23 10:01 UTC)

<p>Hello, I’ve been having issues with orienting a cylinder with vtk. After applying a transformation (with vtkTransformPolyDataFilter), the model wouldn’t display anymore (the non oriented cylinder can be displayed). At first, I noticed I forgot to “update” the transformation so the output was empty but after correcting my code and printing the content of the polydata, it does seem to have data, but still wouldn’t display like it did before the transformation.</p>
<p>I’ve read <a href="https://discourse.slicer.org/t/set-orientation-at-vtkcylindersource/8663">this topic</a> as well as <a href="https://kitware.github.io/vtk-examples/site/Cxx/GeometricObjects/OrientedCylinder/" rel="noopener nofollow ugc">this vtk example</a> but I’m now stuck.</p>
<p>Here is my code :</p>
<pre><code class="lang-python">def placeRetractor(retractorNode):
  # Extremities coordinates
  pointsCoordinates = np.zeros((3,2))
  for i in range(2):
    retractorNode.GetNthControlPointPosition(i,pointsCoordinates[:,i])
  
  # Center coordinates
  center = np.zeros((3,1))
  center[0] = (pointsCoordinates[0,0] + pointsCoordinates[0,1]) / 2
  center[1] = (pointsCoordinates[1,0] + pointsCoordinates[1,1]) / 2
  center[2] = (pointsCoordinates[2,0] + pointsCoordinates[2,1]) / 2
  
  # Length
  length = np.linalg.norm(pointsCoordinates[:,1] - pointsCoordinates[:,0])
  
  # Radius
  radius = 8 #from thickness of the retractor's arm in mm, easily modifiable here
  
  # Cylinder
  source = vtk.vtkCylinderSource()
  source.SetResolution(32)
  source.SetCenter(center)
  source.SetHeight(length)
  source.SetRadius(radius)
  source.CappingOn()
  source.Update()
  polyData = source.GetOutput()
  print("debug polydata pre-transform :\n",polyData)
  
  # Cylinder rotation
  #basis
  #X axis is port-&gt;target
  X_axis = np.zeros((3,1))
  X_axis[0] = (pointsCoordinates[0,0] + pointsCoordinates[0,1])
  X_axis[1] = (pointsCoordinates[1,0] + pointsCoordinates[1,1])
  X_axis[2] = (pointsCoordinates[2,0] + pointsCoordinates[2,1])
  X_axis = X_axis / np.linalg.norm(X_axis)
  #Z axis is any vector cross X
  anyVector = np.ones((3,1))
  Z_axis = np.cross(anyVector,X_axis,axis=0)
  Z_axis = Z_axis / np.linalg.norm(Z_axis)
  #Y axis is X cross Z
  Y_axis = np.cross(X_axis,Z_axis,axis=0)
  Y_axis = Y_axis / np.linalg.norm(Y_axis)
  #transform matrix
  transformer = vtk.vtkMatrix4x4()
  transformer.Identity()
  for i in range(3):
    transformer.SetElement(i,0,X_axis[i])
    transformer.SetElement(i,1,Y_axis[i])
    transformer.SetElement(i,2,Z_axis[i])
  #transform
  transform = vtk.vtkTransform()
  transform.Concatenate(transformer)
  transform.RotateZ(-90.0)
  #transformation
  transformation = vtk.vtkTransformPolyDataFilter()
  transformation.SetTransform(transform)
  transformation.SetInputData(polyData)
  transformation.Update()
  polyData2 = transformation.GetOutput()
  print("debug polydata post-transform :\n",polyData2)
  
  modelNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLModelNode','retractor')
  modelNode.SetAndObservePolyData(polyData2)
  
  # display
  modelNode.CreateDefaultDisplayNodes()
  modelNode.GetDisplayNode().SetOpacity(0.25)
  modelNode.GetDisplayNode().SetColor(0, 1, 0)
  
  return modelNode
</code></pre>
<p>And what the console displays about the PolyDatas :</p>
<pre data-code-wrap="txt"><code class="lang-nohighlight">debug polydata pre-transform :
 vtkPolyData (0000022C15C76BB0)
  Debug: Off
  Modified Time: 574542
  Reference Count: 2
  Registered Events: (none)
  Information: 0000022C0F1E6E40
  Data Released: False
  Global Release Data: Off
  UpdateTime: 574543
  Field Data:
    Debug: Off
    Modified Time: 574500
    Reference Count: 1
    Registered Events: (none)
    Number Of Arrays: 0
    Number Of Components: 0
    Number Of Tuples: 0
  Number Of Points: 128
  Number Of Cells: 34
  Cell Data:
    Debug: Off
    Modified Time: 574508
    Reference Count: 1
    Registered Events: 
      Registered Observers:
        vtkObserver (0000022C0D90B0C0)
          Event: 33
          EventName: ModifiedEvent
          Command: 0000022C0F1E7660
          Priority: 0
          Tag: 1
    Number Of Arrays: 0
    Number Of Components: 0
    Number Of Tuples: 0
    Copy Tuple Flags: ( 1 1 1 1 1 0 1 1 1 1 1 )
    Interpolate Flags: ( 1 1 1 1 1 0 0 1 1 1 1 )
    Pass Through Flags: ( 1 1 1 1 1 1 1 1 1 1 1 )
    Scalars: (none)
    Vectors: (none)
    Normals: (none)
    TCoords: (none)
    Tensors: (none)
    GlobalIds: (none)
    PedigreeIds: (none)
    EdgeFlag: (none)
    Tangents: (none)
    RationalWeights: (none)
    HigherOrderDegrees: (none)
  Point Data:
    Debug: Off
    Modified Time: 574541
    Reference Count: 1
    Registered Events: 
      Registered Observers:
        vtkObserver (0000022C0D90B090)
          Event: 33
          EventName: ModifiedEvent
          Command: 0000022C0F1E7660
          Priority: 0
          Tag: 1
    Number Of Arrays: 2
    Array 0 name = Normals
    Array 1 name = TCoords
    Number Of Components: 5
    Number Of Tuples: 128
    Copy Tuple Flags: ( 1 1 1 1 1 0 1 1 1 1 1 )
    Interpolate Flags: ( 1 1 1 1 1 0 0 1 1 1 1 )
    Pass Through Flags: ( 1 1 1 1 1 1 1 1 1 1 1 )
    Scalars: (none)
    Vectors: (none)
    Normals: 
      Debug: Off
      Modified Time: 574522
      Reference Count: 1
      Registered Events: (none)
      Name: Normals
      Data type: float
      Size: 645
      MaxId: 383
      NumberOfComponents: 3
      Information: 0000000000000000
      Name: Normals
      Number Of Components: 3
      Number Of Tuples: 128
      Size: 645
      MaxId: 383
      LookupTable: (none)
    TCoords: 
      Debug: Off
      Modified Time: 574526
      Reference Count: 1
      Registered Events: (none)
      Name: TCoords
      Data type: float
      Size: 258
      MaxId: 255
      NumberOfComponents: 2
      Information: 0000000000000000
      Name: TCoords
      Number Of Components: 2
      Number Of Tuples: 128
      Size: 258
      MaxId: 255
      LookupTable: (none)
    Tensors: (none)
    GlobalIds: (none)
    PedigreeIds: (none)
    EdgeFlag: (none)
    Tangents: (none)
    RationalWeights: (none)
    HigherOrderDegrees: (none)
  Bounds: 
    Xmin,Xmax: (17.1243, 22.1243)
    Ymin,Ymax: (-63.2904, 103.709)
    Zmin,Zmax: (-162.708, -157.708)
  Compute Time: 574555
  Editable: false
  Number Of Points: 128
  Point Coordinates: 0000022C160ED360
  PointLocator: 0000000000000000
  CellLocator: 0000000000000000
  Number Of Vertices: 0
  Number Of Lines: 0
  Number Of Polygons: 34
  Number Of Triangle Strips: 0
  Number Of Pieces: 1
  Piece: 0
  Ghost Level: 0
  CellsBounds: 
    Xmin,Xmax: (17.1243, 22.1243)
    Ymin,Ymax: (-63.2904, 103.709)
    Zmin,Zmax: (-162.708, -157.708)
  CellsBounds Time: 574556

debug polydata post-transform :
 vtkPolyData (0000022C15C76D90)
  Debug: Off
  Modified Time: 574804
  Reference Count: 2
  Registered Events: (none)
  Information: 0000022C0F1EFE50
  Data Released: False
  Global Release Data: Off
  UpdateTime: 574805
  Field Data:
    Debug: Off
    Modified Time: 574765
    Reference Count: 1
    Registered Events: (none)
    Number Of Arrays: 0
    Number Of Components: 0
    Number Of Tuples: 0
  Number Of Points: 128
  Number Of Cells: 34
  Cell Data:
    Debug: Off
    Modified Time: 574773
    Reference Count: 1
    Registered Events: 
      Registered Observers:
        vtkObserver (0000022C0D874320)
          Event: 33
          EventName: ModifiedEvent
          Command: 0000022C0F1F0210
          Priority: 0
          Tag: 1
    Number Of Arrays: 0
    Number Of Components: 0
    Number Of Tuples: 0
    Copy Tuple Flags: ( 1 1 1 1 1 0 1 1 1 1 1 )
    Interpolate Flags: ( 1 1 1 1 1 0 0 1 1 1 1 )
    Pass Through Flags: ( 1 1 1 1 1 1 1 1 1 1 1 )
    Scalars: (none)
    Vectors: (none)
    Normals: (none)
    TCoords: (none)
    Tensors: (none)
    GlobalIds: (none)
    PedigreeIds: (none)
    EdgeFlag: (none)
    Tangents: (none)
    RationalWeights: (none)
    HigherOrderDegrees: (none)
  Point Data:
    Debug: Off
    Modified Time: 574804
    Reference Count: 1
    Registered Events: 
      Registered Observers:
        vtkObserver (0000022C0D873E40)
          Event: 33
          EventName: ModifiedEvent
          Command: 0000022C0F1F0210
          Priority: 0
          Tag: 1
    Number Of Arrays: 2
    Array 0 name = Normals
    Array 1 name = TCoords
    Number Of Components: 5
    Number Of Tuples: 128
    Copy Tuple Flags: ( 1 1 0 1 1 0 1 1 1 1 1 )
    Interpolate Flags: ( 1 1 0 1 1 0 0 1 1 1 1 )
    Pass Through Flags: ( 1 1 0 1 1 1 1 1 1 1 1 )
    Scalars: (none)
    Vectors: (none)
    Normals: 
      Debug: Off
      Modified Time: 574789
      Reference Count: 1
      Registered Events: (none)
      Name: Normals
      Data type: float
      Size: 384
      MaxId: 383
      NumberOfComponents: 3
      Information: 0000000000000000
      Name: Normals
      Number Of Components: 3
      Number Of Tuples: 128
      Size: 384
      MaxId: 383
      LookupTable: (none)
    TCoords: 
      Debug: Off
      Modified Time: 574526
      Reference Count: 2
      Registered Events: (none)
      Name: TCoords
      Data type: float
      Size: 258
      MaxId: 255
      NumberOfComponents: 2
      Information: 0000000000000000
      Name: TCoords
      Number Of Components: 2
      Number Of Tuples: 128
      Size: 258
      MaxId: 255
      LookupTable: (none)
    Tensors: (none)
    GlobalIds: (none)
    PedigreeIds: (none)
    EdgeFlag: (none)
    Tangents: (none)
    RationalWeights: (none)
    HigherOrderDegrees: (none)
  Bounds: 
    Xmin,Xmax: (89.7003, 114.811)
    Ymin,Ymax: (-137.127, -111.418)
    Zmin,Zmax: (-106.341, 59.0011)
  Compute Time: 574817
  Editable: false
  Number Of Points: 128
  Point Coordinates: 0000022C160F8D60
  PointLocator: 0000000000000000
  CellLocator: 0000000000000000
  Number Of Vertices: 0
  Number Of Lines: 0
  Number Of Polygons: 34
  Number Of Triangle Strips: 0
  Number Of Pieces: 1
  Piece: 0
  Ghost Level: 0
  CellsBounds: 
    Xmin,Xmax: (89.7003, 114.811)
    Ymin,Ymax: (-137.127, -111.418)
    Zmin,Zmax: (-106.341, 59.0011)
  CellsBounds Time: 574818
</code></pre>

---

## Post #2 by @SegmentedYannig (2022-08-30 08:43 UTC)

<p><strong>Update on the situation, before anyone tries to solve the issue, I fixed it.</strong></p>
<p>Firstly, the X axis was poorly defined, with a <strong>+</strong> instead of a <strong>-</strong> in the calculation of the coordinates.<br>
Then, we found out by accident that the cylinder was actually there, although not in the right place and in black, on a black background… I think I’ll stick with the light blue background now…<br>
Also, I noticed the transform had problems if we set the center of the cylinder beforehand. Setting said center by a translation in the transformation before applying the new base solves the problem.<br>
Finally, the cylinder was not entirely black, but actually colored, only on the inside. Some tests confirmed my suspicions, it was inside out. By setting the diameter and length during the transformation, instead of the source, it is possible to set the length to a negative value, which fixes the issue. <em>Now that I think about it, maybe it was possible to set a negative length from the source, I didn’t try</em></p>
<p>So yes, tl;dr : it works now. And for anyone curious, here is the corrected code :</p>
<pre><code class="lang-python">def placeRetractor(retractorNode):
  # Extremities coordinates
  pointsCoordinates = np.zeros((3,2))
  for i in range(2):
    retractorNode.GetNthControlPointPosition(i,pointsCoordinates[:,i])
  
  # Center coordinates
  center = np.zeros((3,1))
  center[0] = (pointsCoordinates[0,0] + pointsCoordinates[0,1]) / 2
  center[1] = (pointsCoordinates[1,0] + pointsCoordinates[1,1]) / 2
  center[2] = (pointsCoordinates[2,0] + pointsCoordinates[2,1]) / 2
  
  # Length
  length = np.linalg.norm(pointsCoordinates[:,1] - pointsCoordinates[:,0])
  
  # Diameter
  diameter = 8 #from thickness of the retractor's arm in mm, easily modifiable here
  
  # Cylinder
  source = vtk.vtkCylinderSource()
  source.SetResolution(32)
  source.CappingOn()
  source.Update()
  polyData = source.GetOutput()
  
  # Cylinder rotation
  #basis
  #X axis is port-&gt;target
  X_axis = np.zeros((3,1))
  X_axis[0] = (pointsCoordinates[0,1] - pointsCoordinates[0,0])
  X_axis[1] = (pointsCoordinates[1,1] - pointsCoordinates[1,0])
  X_axis[2] = (pointsCoordinates[2,1] - pointsCoordinates[2,0])
  X_axis = X_axis / np.linalg.norm(X_axis)
  #Z axis is any vector cross X
  anyVector = np.ones((3,1))
  Z_axis = np.cross(anyVector,X_axis,axis=0)
  Z_axis = Z_axis / np.linalg.norm(Z_axis)
  #Y axis is X cross Z
  Y_axis = np.cross(X_axis,Z_axis,axis=0)
  Y_axis = Y_axis / np.linalg.norm(Y_axis)
  #transform matrix
  transformer = vtk.vtkMatrix4x4()
  transformer.Identity()
  for i in range(3):
    transformer.SetElement(i,0,X_axis[i])
    transformer.SetElement(i,1,Y_axis[i])
    transformer.SetElement(i,2,Z_axis[i])
  #transform
  transform = vtk.vtkTransform()
  transform.Translate(center) #setting the center
  transform.Concatenate(transformer) #applying the new base
  transform.RotateZ(-90.0) #alignment
  transform.Scale(diameter, -length, diameter) #setting of the dimensions
  #transformation
  transformation = vtk.vtkTransformPolyDataFilter()
  transformation.SetTransform(transform)
  transformation.SetInputData(polyData)
  transformation.Update()
  polyData = transformation.GetOutput()
  
  modelNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLModelNode','retractor')
  modelNode.SetAndObservePolyData(polyData)
  
  # display
  modelNode.CreateDefaultDisplayNodes()
  modelNode.GetDisplayNode().SetOpacity(0.25)
  modelNode.GetDisplayNode().SetColor(0, 1, 0)
  
  return modelNode
</code></pre>

---

## Post #3 by @jumbojing (2024-06-01 23:37 UTC)

<aside class="quote no-group" data-username="SegmentedYannig" data-post="2" data-topic="24880">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/segmentedyannig/48/16010_2.png" class="avatar"> SegmentedYannig:</div>
<blockquote>
<p><code>setting of the dimensions</code></p>
</blockquote>
</aside>
<p>I modified <code>Z-axis</code>(<code>*-1</code>) and got the correct display. I don’t know why?</p>
<aside class="quote no-group quote-modified" data-username="SegmentedYannig" data-post="2" data-topic="24880">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/segmentedyannig/48/16010_2.png" class="avatar"> SegmentedYannig:</div>
<blockquote>
<pre><code class="lang-auto">  for i in range(3):
    transformer.SetElement(i,0,X_axis[i])
    transformer.SetElement(i,1,Y_axis[i])
    transformer.SetElement(i,2,Z_axis[i]*-1)
</code></pre>
</blockquote>
</aside>
<pre><code class="lang-auto"># @staticmethod
def oriMat(norX):
  norY = [0] * 3  # y坐标
  norZ = [0] * 3  # z坐标
  # 用正则化函数归一化x坐标
  vtk.vtkMath.Normalize(norX)
  # 计算z坐标，用x和任意向量的叉乘
  vtk.vtkMath.Cross(norX, ndA([1,1,1]), norZ)
  # 用正则化函数归一化z坐标
  vtk.vtkMath.Normalize(norZ)
  # 计算y坐标，用z和x的叉乘
  vtk.vtkMath.Cross(norZ, norX, norY)
  # 创建一个阵列用于构造方向余弦阵
  mat = vtk.vtkMatrix4x4()
  # 创建方向余弦阵
  mat.Identity()
  for i in range(0, 3):
    mat.SetElement(i, 0, norX[i])
    mat.SetElement(i, 1, norY[i])
    mat.SetElement(i, 2, norZ[i])
  # mArr = ut.arrayFromVTKMatrix(mat)
  # print(f'{mArr=}')
  # 返回方向余弦阵
  return mat
</code></pre>
<p>Using ‘vtkMath’ can actually obtain the correct directional cosine matrix and display correctly.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/4980a3e2781ae55b2cd79cda86f3cbecc3ac47bb.jpeg" data-download-href="/uploads/short-url/auesRWjIZsppPSOZfC9gHaQSaev.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/4980a3e2781ae55b2cd79cda86f3cbecc3ac47bb_2_650x500.jpeg" alt="image" data-base62-sha1="auesRWjIZsppPSOZfC9gHaQSaev" width="650" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/4980a3e2781ae55b2cd79cda86f3cbecc3ac47bb_2_650x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/4980a3e2781ae55b2cd79cda86f3cbecc3ac47bb.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/4980a3e2781ae55b2cd79cda86f3cbecc3ac47bb.jpeg 2x" data-dominant-color="9F9FB6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">970×746 55.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
