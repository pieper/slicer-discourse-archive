---
topic_id: 24689
title: "Updating Of The Sphere"
date: 2022-08-09
url: https://discourse.slicer.org/t/24689
---

# Updating of the sphere

**Topic ID**: 24689
**Date**: 2022-08-09
**URL**: https://discourse.slicer.org/t/updating-of-the-sphere/24689

---

## Post #1 by @AMK (2022-08-09 10:45 UTC)

<p>Hi,</p>
<p>I have been trying to develop a model of a cup. For this I followed the following steps:</p>
<ol>
<li>
<p>Selected two fiducial points.</p>
</li>
<li>
<p>Based on the fiducial points a sphere is created.</p>
</li>
<li>
<p>A plane passes through these two fiducial points.</p>
</li>
<li>
<p>Using the dynamic modeler module, a shell is created. This gives a hollow sphere.</p>
</li>
<li>
<p>Using the dynamic modeler, the above generated plane cuts the sphere into half. This gives a cup as desired.</p>
</li>
<li>
<p>Now I have also added the capability to rotate the cup as desired. The remaining sphere and the plane rotates together. This is the desired effect.</p>
</li>
</ol>
<p>The issue I am facing is that now I am unable to update the radius of the sphere dynamically. I have also added an observor to detect any change in the position of the sphere and update it accordingly.<br>
I have attached the code.</p>
<p>Thanks</p>
<p>def CreateSphere(self):<br>
def UpdateSphere(param1, param2):<br>
“”“Update the sphere from the control points<br>
“””<br>
import math<br>
pointListNode = slicer.util.getNode(“F”)<br>
centerPointCoord = [0.0, 0.0, 0.0]<br>
pointListNode.GetNthControlPointPosition(0,centerPointCoord)<br>
circumferencePointCoord = [0.0, 0.0, 0.0]<br>
pointListNode.GetNthControlPointPosition(1,circumferencePointCoord)</p>
<pre><code>        sphere.SetCenter(centerPointCoord)
        radius=math.sqrt((centerPointCoord[0]-circumferencePointCoord[0])**2+(centerPointCoord[1]-circumferencePointCoord[1])**2+(centerPointCoord[2]-circumferencePointCoord[2])**2)
        sphere.SetRadius(radius)
        sphere.SetPhiResolution(30)
        sphere.SetThetaResolution(30)
        sphere.Update()
        # Get point list node from scene
    pointListNode = slicer.util.getNode("F")
    #print(pointListNode)
    sphere = vtk.vtkSphereSource()
    UpdateSphere(0,0)

    # Create model node and add to scene
    modelsLogic = slicer.modules.models.logic()
    model = modelsLogic.AddModel(sphere.GetOutput())
    model.GetDisplayNode().SetSliceIntersectionVisibility(True)
    model.GetDisplayNode().SetSliceIntersectionThickness(3)
    model.GetDisplayNode().SetColor(1,1,0)

    # Call UpdateSphere whenever the control points are changed
    pointListNode.AddObserver(slicer.vtkMRMLMarkupsNode.PointModifiedEvent, UpdateSphere, 2)

    # Compute best fit plane
   # translatedLineStartPoint = np.zeros(3)
    #center = pointListNode.GetNthControlPointPosition(0,translatedLineStartPoint)

   # translatedLineStopPoint = np.zeros(3)
   # circumference = pointListNode.GetNthControlPointPosition(0,translatedLineStopPoint)

    #normal = np.cross(center, circumference)
    #print(normal)


    #print(pointListNode.GetNthControlPointPosition(0,translatedLineStartPoint))

    center = [10.0, 0.0, 0.0]
    normal = [0.0, 0.0, 1.0]
    
    vtk.vtkPlane.ComputeBestFittingPlane(model.GetPolyData().GetPoints(), center, normal)

    # Display best fit plane as a markups plane
    planeNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsPlaneNode')
    planeNode.SetCenter(center)
    planeNode.SetNormal(normal)
    planeNode.SetName("MarkupsPlane")
    
    
    hollowModeler = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLDynamicModelerNode")
    hollowModeler.SetToolName("Hollow")
    hollowModeler.SetNodeReferenceID("Hollow.InputModel", model.GetID())
    #hollowedModelNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLModelNode")  # this node will store the hollow model
    hollowModeler.SetNodeReferenceID("Hollow.OutputModel", model.GetID())
    hollowModeler.SetAttribute("ShellThickness", "2.5")  # grow outside
    hollowModeler.SetContinuousUpdate(True)  # auto-update output model if input parameters are changed

    #hollowModeler.SetNodeReferenceID("PlaneCut.OutputPositiveModel", PlaneCuttedModelNode.GetID())
    slicer.modules.dynamicmodeler.logic().RunDynamicModelerTool(hollowModeler)

    # Set up Plane Cut tool
    PlaneModeler = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLDynamicModelerNode")
    PlaneModeler.SetToolName("Plane cut")
    PlaneModeler.SetNodeReferenceID("PlaneCut.InputModel", model.GetID())
    PlaneModeler.SetNodeReferenceID("PlaneCut.InputPlane", planeNode.GetID())
    PlaneCuttedModelNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLModelNode")  # this node will store the hollow model
    PlaneModeler.SetNodeReferenceID("PlaneCut.OutputModel", model.GetID())
    PlaneModeler.SetAttribute("OperationType", "Union")  # grow outside
    PlaneModeler.SetContinuousUpdate(True)  # auto-update output model if input parameters are changed

    PlaneModeler.SetNodeReferenceID("PlaneCut.OutputPositiveModel", model.GetID())
    slicer.modules.dynamicmodeler.logic().RunDynamicModelerTool(PlaneModeler)



    PlaneNode = slicer.util.getNode('MarkupsPlane')
    PlaneNode.SetPlaneType(PlaneNode.PlaneType3Points)


    displayNode = PlaneNode.GetDisplayNode()
    displayNode.SetGlyphScale(2.5)
    displayNode.HandlesInteractiveOn()

    displayNode.SetRotationHandleVisibility(True)
    displayNode.SetTranslationHandleVisibility(True)


    planeToWorldTransformNode = slicer.vtkMRMLLinearTransformNode()
    planeToWorldTransformNode.SetName(slicer.mrmlScene.GetUniqueNameByString("planeToWorld"))
    slicer.mrmlScene.AddNode(planeToWorldTransformNode)

    # Save the inverse of the initial transform of the plane
    worldToInitialModelTransformNode = slicer.vtkMRMLLinearTransformNode()
    worldToInitialModelTransformNode.SetName(slicer.mrmlScene.GetUniqueNameByString("worldToInitialModel"))
    slicer.mrmlScene.AddNode(worldToInitialModelTransformNode)

    model.SetAndObserveTransformNodeID(worldToInitialModelTransformNode.GetID())
    worldToInitialModelTransformNode.SetAndObserveTransformNodeID(planeToWorldTransformNode.GetID())

    # function to update the model's position/orientation interactively
    def onPlaneModified(sourceNode,event=None):
        planeToWorldMatrix = vtk.vtkMatrix4x4()
        try:
            sourceNode.GetObjectToWorldMatrix(planeToWorldMatrix)
        except:
            sourceNode.GetPlaneToWorldMatrix(planeToWorldMatrix)
        # 
        planeNodeToWorldTransformNode = model.GetParentTransformNode().GetParentTransformNode()
        planeNodeToWorldTransformNode.SetMatrixTransformToParent(planeToWorldMatrix)

    onPlaneModified(planeNode)
    planeToWorldMatrix = vtk.vtkMatrix4x4()
    # This call is done to give the transformNode time to update its matrixToParent
    planeNodeToWorldTransformNode = model.GetParentTransformNode().GetParentTransformNode()
    planeNodeToWorldTransformNode.GetMatrixTransformToParent(planeToWorldMatrix)

    worldToInitialModelMatrix = vtk.vtkMatrix4x4()
    worldToInitialModelMatrix.DeepCopy(planeToWorldMatrix)
    worldToInitialModelMatrix.Invert()
    worldToInitialModelTransformNode.SetMatrixTransformToParent(worldToInitialModelMatrix)

    observer  = planeNode.AddObserver(slicer.vtkMRMLMarkupsNode.PointModifiedEvent,onPlaneModified)
</code></pre>

---

## Post #2 by @mau_igna_06 (2022-08-09 11:30 UTC)

<p>I think you should define the <code>UpdateSphere</code> function after you define the sphere source.</p>
<p>Please let me know if that helps</p>
<p>Mauro</p>

---

## Post #3 by @AMK (2022-08-09 14:33 UTC)

<p>Hi,</p>
<p>It didn’t worked that way. So, I just created two different function and now it works as desired.</p>

---
