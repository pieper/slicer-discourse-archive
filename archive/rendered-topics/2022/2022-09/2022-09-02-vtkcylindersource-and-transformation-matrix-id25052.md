---
topic_id: 25052
title: "Vtkcylindersource And Transformation Matrix"
date: 2022-09-02
url: https://discourse.slicer.org/t/25052
---

# vtkCylinderSource() and transformation matrix

**Topic ID**: 25052
**Date**: 2022-09-02
**URL**: https://discourse.slicer.org/t/vtkcylindersource-and-transformation-matrix/25052

---

## Post #1 by @mosenco (2022-09-02 12:05 UTC)

<p>I had a problem, back then, with the rotation. I had a cylinder, C1, in space, with its rotation and another one C2, placed at the origin (0,0,0). I wanted to move and rotate C2 like C1, so C2 overlaps C1. I did it with euler angles using the transformation matrix 4x4.</p>
<p>Now i have another problem. I have a model of a brain and many models of cylinders that represent electrodes to capture brain activities and i wanted to detect if a specific cylinder is outside or inside the brain and color it accordingly. I tried with <code>vtkCollisionDetectionFilter()</code> and had my problems and i already made a post about it here, but then i found another class <code>vtkSelectEnclosedPoints()</code> that works better for my case, because giving an input data, a surface data, then i just use the function <code>IsInside()</code> to check if the input data is inside the surface data. But weird enough, the result was all wrong.</p>
<p>Turns out, the transformation matrix is the one that was giving the errors.<br>
I rewrote the code without the transformation matrix, so both brain and cylinder have the same cartesian system, and the <code>vtkSelectEnclosedPoints()</code> works fine. Turns out, that if i rotate with the euler angles, so using the transformation matrix, the brain and the cylinder have different cartesiam system. So for example, the position in space (0,0,0) for the brain is different for the cylinder, because they are refering to different cartesian system.</p>
<p>What can i do?</p>
<pre><code class="lang-auto">### Create a vtk cylinder
cylinderSource = vtk.vtkCylinderSource()
cylinderSource.SetCenter(0,0,0)
cylinderSource.SetHeight(list(models.values())[0][1])
cylinderSource.SetRadius(list(models.values())[0][2])
cylinderSource.SetResolution(100)
cylinderSource.Update()
### Create a model of the cylinder to add to the scene
cylindermodel = slicer.vtkMRMLModelNode()
cylindermodel.SetName(name + "_direction")
cylindermodel.SetAndObservePolyData(cylinderSource.GetOutput())

#Create a Transform node for the model to copy the rotation
cylinderTS = slicer.vtkMRMLTransformNode()

##compute the rotation
#Given the vector (p1,p3) i move it to the origin
vorigin = np.subtract(p1,p3)
#compute rotation matrix
R = self.rotMat(vorigin)
#from 3x3 matrix i transformit in a 4x4 matrix
matrix4 = self.mat3To4(R, float(points[p]), float(points[p + 1]), float(points[p + 2]))
#from 4x4 matrix, generate vtkmatrix4x4 object
rMatrix = self.mat4x4Gen(matrix4)
#add the rotation to the model
cylinderTS.SetAndObserveMatrixTransformToParent(rMatrix)

cylindermodelDisplay = slicer.vtkMRMLModelDisplayNode()
cylindermodelDisplay.SetSliceIntersectionVisibility(True)  # Hide in slice view
cylindermodelDisplay.SetVisibility(True)  # Show in 3D view
cylindermodelDisplay.SetColor(1, 0, 0)
cylindermodelDisplay.SetLineWidth(2)
cylindermodelDisplay.SetOpacity(0.5)

slicer.mrmlScene.AddNode(cylindermodelDisplay)
cylindermodel.SetAndObserveDisplayNodeID(cylindermodelDisplay.GetID())

slicer.mrmlScene.AddNode(cylinderTS)
cylindermodel.SetAndObserveTransformNodeID(cylinderTS.GetID())

slicer.mrmlScene.AddNode(cylindermodel)

# Check if electrodes are inside or outside the brain
for j in range(0, len(listBrain)):
    select = vtk.vtkSelectEnclosedPoints()
    select.SetInputData(cylindermodel.GetPolyData())
    select.SetSurfaceData(listBrain[j])
    select.SetTolerance(.00001)
    select.Update()
    if select.IsInsideSurface([float(points[p]), float(points[p + 1]), float(points[p + 2])]):
        cylindermodelDisplay.SetColor(1, 1, 1)
        fidNode.SetNthFiducialLabel(a, name + str((p / 3) + 1)+"#")
    del select
</code></pre>
<pre><code class="lang-auto">def mat4x4Gen(self, m):
    rMatrix = vtk.vtkMatrix4x4()
    for x in range(4):
        for y in range(4):
            rMatrix.SetElement(x, y, m[x][y])
    return rMatrix

def mat3To4(self, m,x,y,z):
    b = np.array([[0, 0, 0]])
    c = np.concatenate((m, b), axis=0)
    d = np.array([[x, y, z, 1]])
    return np.concatenate((c, d.T), axis=1)

  

def rotMat(self, vec2):
    """ Find the rotation matrix that aligns vec1 to vec2
    :param vec1: A 3d "source" vector
    :param vec2: A 3d "destination" vector
    :return mat: A transform matrix (3x3) which when applied to vec1, aligns it with vec2.
    """
    vec1 = [0,1,0]
    a, b = (vec1 / np.linalg.norm(vec1)).reshape(3), (vec2 / np.linalg.norm(vec2)).reshape(3)
    v = np.cross(a, b)
    c = np.dot(a, b)
    s = np.linalg.norm(v)
    kmat = np.array([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])
    rotation_matrix = np.eye(3) + kmat + kmat.dot(kmat) * ((1 - c) / (s ** 2))
    return rotation_matrix
</code></pre>

---

## Post #2 by @lassoan (2022-09-03 14:21 UTC)

<p>If you apply a transform to a model node (using <code>SetAndObserveTransformNodeID()</code>) then the polydata in the model node is not changed.</p>
<p>If you want to get a polydata in world coordinate system (what you see on screen) then you can either:</p>
<ul>
<li>harden a transform (persistently transform all points of a model, using <code>HardenTransform()</code>)</li>
<li>get the polydata, make a copy, and apply use <code>vtkTransformPolyDataFilter</code> to transform the polydata (using the transform provided by <code>transformNode.GetMatrixTransformToWorld()</code>).</li>
</ul>
<p>However, I would to determine what parts of an electrode intersect the brain (or segmented regions of the brain) using “Probe volume with model” module. This modules assigns to each labelpoint the value of the image at that position. It takes care of all transforms (you get what you see in the 3D view). You can get the values as a numpy array by calling <code>pd = slicer.util.arrayFromModelPointData()</code> and if you want to know if any points are inside the volume then you can simply check if <code>pd.max() &gt; 0</code>.</p>

---

## Post #3 by @mosenco (2022-09-13 18:30 UTC)

<p>I tried to use</p>
<pre><code class="lang-auto">pointAt = [0,0,0]
for indexMesh in range(0, cylindermodel.GetPolyData().GetNumberOfPoints()):
    cylindermodel.GetPolyData().GetPoint(indexMesh, pointAt)
</code></pre>
<p>so at each cycle, pointAt will return a continuous flow of points regarding my single <code>cylindermodel</code>. And for each point i create a new <code>AddControlPoint(pointAt)</code> so i can see where that point is.</p>
<p>To my surprise they all are at (0,0,0), because as you see in previous code when i declare <code>cylinderSource</code> i set the center at (0,0,0). So when i called <code>cylindermodel.SetAndObservePolyData(cylinderSource.GetOutput())</code>, my model was just mirroring the <code>cylinderSource</code> but the model doesnt have any mesh or poly or anything.</p>
<p>With <code>cylinderTS = slicer.vtkMRMLTransformNode()</code> i managed to make a transformation so with <code>cylindermodel.SetAndObserveDisplayNodeID(cylindermodelDisplay.GetID())</code> i just rotate and move my model.</p>
<p>The problem is that when i call <code>cylindermodel.GetPolyData()</code> it returns me the poly data of <code>cylinderSource</code> not the one i see in the 3Dslicer.</p>
<p>I tried to  search on the forum but didn’t find anything. Is there any guide to create, for example, a cube using vtk and then put it in the scene? Is there any other way from what i did?</p>

---

## Post #4 by @mosenco (2022-09-13 21:07 UTC)

<p>i tried to follow this guide to how use hardentransform <a href="https://python.hotexamples.com/examples/slicer/-/vtkSlicerTransformLogic/python-vtkslicertransformlogic-function-examples.html" rel="noopener nofollow ugc">https://python.hotexamples.com/examples/slicer/-/vtkSlicerTransformLogic/python-vtkslicertransformlogic-function-examples.html</a> but i dunno, my cylinder vtk stays at position (0,0,0) even  if i hardentransformed. I tried also <code>cylindermodel.HardenTransform()</code> but nothing happens.</p>
<p>I used <code>cylindermodel.GetPolyData().GetPoint(0, pos)</code> before and after hardentransform  and the value of pos doesnt change</p>

---

## Post #5 by @lassoan (2022-09-13 21:47 UTC)

<p>Most likely the issue is something trivial, like you haven’t called <code>Update()</code> on cylinder source. Please provide a code snippet that I can copy-paste into the Python console that reproduces the unexpected behavior.</p>

---

## Post #6 by @mosenco (2022-09-14 13:07 UTC)

<p>Meanwhile i was writing a test to share it with you, i found out the problem. <code>cylindermodel.HardenTransform()</code> must be used after  <code>slicer.mrmlScene.AddNode(cylindermodel)</code>.</p>
<p>Btw, i didn’t know about the <code>hardentransform()</code>, that solved it!</p>

---

## Post #7 by @lassoan (2022-09-14 15:20 UTC)

<p>That’s correct. Node references (such as the model node refers to a transform node) only work between nodes that are added to the scene.</p>

---
