---
topic_id: 42745
title: "Need Help On Implementing Slice Visibility Of A 3D Model"
date: 2025-04-30
url: https://discourse.slicer.org/t/42745
---

# Need help on implementing slice visibility of a 3d model

**Topic ID**: 42745
**Date**: 2025-04-30
**URL**: https://discourse.slicer.org/t/need-help-on-implementing-slice-visibility-of-a-3d-model/42745

---

## Post #1 by @alientex (2025-04-30 10:06 UTC)

<p>Hello everyone,</p>
<p>I am new to Slicer, and I have gone through some tutorial PDFs provided in the developer section of the official site. I have created a scripted module using the Extension Wizard. For my module, I am implementing functionality that allows visualization of the slice visibility of a 3D model, specifically the slice intersection.</p>
<p>I found that the class <code>vtkMRMLModelSliceDisplayableManager</code> is responsible for slice visibility when it is enabled in the Models module. Based on this, I created a rendering pipeline. However, the actor is not visible. Previously, it was visible but not correctly positioned in the slice views—it appeared in the bottom-left corner of the Axial view.</p>
<p>Here is my code:</p>
<pre><code class="lang-auto">class SliceVisibilityPipeline(VTKObservationMixin):
    def __init__(self, modelNode, sliceViewName='Red'):
        VTKObservationMixin.__init__(self)

        self.modelNode = modelNode
        self.modelDisplayNode = self.modelNode.GetDisplayNode()
        self.sliceViewName = sliceViewName
        
        # Get slice node and renderer
        layoutManager = slicer.app.layoutManager()
        self.sliceWidget = layoutManager.sliceWidget(self.sliceViewName)
        self.sliceView = self.sliceWidget.sliceView()
        self.renderWindow = self.sliceView.renderWindow()
        self.renderer = self.renderWindow.GetRenderers().GetFirstRenderer()

        self.sliceLogic = self.sliceWidget.sliceLogic()
        self.sliceNode = self.sliceLogic.GetSliceNode()
        
        # Create pipeline
        self.plane = vtk.vtkPlane()
        self.nodeToWorld = vtk.vtkGeneralTransform()
        
        # Model warper
        self.modelWarper = vtk.vtkTransformFilter()
        self.modelWarper.SetTransform(self.nodeToWorld)

        # Plane cutter
        self.cutter = vtk.vtkPlaneCutter()
        self.cutter.SetPlane(self.plane)
        self.cutter.SetInputConnection(self.modelWarper.GetOutputPort())

        # Transform to slice space
        self.transformToSlice = vtk.vtkTransform()
        self.transformer = vtk.vtkTransformPolyDataFilter()
        self.transformer.SetTransform(self.transformToSlice)
        self.transformer.SetInputConnection(self.cutter.GetOutputPort())

        # Set up mapper and actor for display
        self.mapper = vtk.vtkPolyDataMapper2D()
        self.mapper.SetInputConnection(self.transformer.GetOutputPort())
        self.mapper.ScalarVisibilityOff()

        self.actor = vtk.vtkActor2D()
        self.actor.SetMapper(self.mapper)
        self.actor.SetVisibility(0)

        # Add actor to renderer
        self.renderer.AddActor2D(self.actor)

        # Set up initial pipeline
        self.updatePipeline()

        # Observe slice node changes
        self.addObserver(self.sliceNode, vtk.vtkCommand.ModifiedEvent, self.onSliceModified)

    def updatePipeline(self):
        self.cleanup()

        if not self.modelNode or not self.modelDisplayNode:
            print("No model or display node found.")
            self.actor.SetVisibility(False)
            return
        
        # Get the mesh data
        polyData = self.modelNode.GetPolyData()
        if not polyData or polyData.GetNumberOfPoints() == 0:
            print("No points are found in model")
            self.actor.SetVisibility(False)
            return
        
        # Update the model warper input
        self.modelWarper.SetInputData(polyData)

        # Get transform from model to world
        if self.modelNode.GetParentTransformNode():
            self.modelNode.GetParentTransformNode().GetTransformToWorld(self.nodeToWorld)
        else:
            self.nodeToWorld.Identity()

        # Update the slice plane based on current slice position
        sliceXYToRAS = vtk.vtkMatrix4x4()
        sliceXYToRAS.DeepCopy(self.sliceNode.GetXYToRAS())
        self.updateSlicePlane(sliceXYToRAS, self.plane)

        # Update the transform from RAS to slice XY
        rasToSliceXY = vtk.vtkMatrix4x4()
        vtk.vtkMatrix4x4.Invert(sliceXYToRAS, rasToSliceXY)
        self.transformToSlice.SetMatrix(rasToSliceXY)

        # Force update of the pipeline to check if there are any points
        self.cutter.Update()
        if self.cutter.GetOutput().GetNumberOfPoints() &lt; 1:
            print("No intersection points found")
            self.actor.SetVisibility(False)
            return
        
        # Update actor properties
        actorProperty = self.actor.GetProperty()
        actorProperty.SetColor(self.modelDisplayNode.GetColor())
        actorProperty.SetLineWidth(self.modelDisplayNode.GetSliceIntersectionThickness())
        actorProperty.SetPointSize(self.modelDisplayNode.GetSliceIntersectionThickness())
        actorProperty.SetOpacity(self.modelDisplayNode.GetSliceIntersectionOpacity())

        # Make actor visible
        self.actor.SetVisibility(True)

        # Force render update
        self.renderWindow.Render()
        
        # Observe slice movements to update plane and cutter
        self.sliceNodeObserverTag = self.sliceNode.AddObserver(vtk.vtkCommand.ModifiedEvent, self.onSliceModified)

    def updateSlicePlane(self, sliceMatrix, plane):
        normal = [0, 0, 0]
        origin = [0, 0, 0]

        for i in range(3):
            normal[i] = sliceMatrix.GetElement(i, 2)
            origin[i] = sliceMatrix.GetElement(i, 3)
        
        vtk.vtkMath.Normalize(normal)
        plane.SetNormal(normal)
        plane.SetOrigin(origin)

    def onSliceModified(self, caller, event):
        # Update the slice plane when the slice changes
        self.updatePipeline()

    def cleanup(self):
        if hasattr(self, 'sliceNode') and hasattr(self, 'sliceNodeObserverTag'):
            self.sliceNode.RemoveObserver(self.sliceNodeObserverTag)
        if hasattr(self, 'renderer') and hasattr(self, 'actor'):
            self.renderer.RemoveActor2D(self.actor)
            self.renderWindow.Render()
</code></pre>
<p>I suspect the issue might lie in the transformation, though I am not sure. Could anyone please help me identify where I might be making a mistake?</p>
<p>Thanks.</p>

---

## Post #2 by @cpinter (2025-04-30 10:12 UTC)

<p>My obvious question is why you are implementing this? This is a feature already existing in Slicer. You just need to use these functions of the display node of your model node:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/3b2948fb04b431468f5ef809f8e02d621eaa6397/Libs/MRML/Core/vtkMRMLDisplayNode.h#L272-L283">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/3b2948fb04b431468f5ef809f8e02d621eaa6397/Libs/MRML/Core/vtkMRMLDisplayNode.h#L272-L283" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/3b2948fb04b431468f5ef809f8e02d621eaa6397/Libs/MRML/Core/vtkMRMLDisplayNode.h#L272-L283" target="_blank" rel="noopener">Libs/MRML/Core/vtkMRMLDisplayNode.h</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/Slicer/Slicer/blob/3b2948fb04b431468f5ef809f8e02d621eaa6397/Libs/MRML/Core/vtkMRMLDisplayNode.h#L272-L283" rel="noopener"><code>3b2948fb0</code></a>
</div>



    <pre class="onebox"><code class="lang-h">
      <ol class="start lines" start="272" style="counter-reset: li-counter 271 ;">
          <li>/// Set the 2D visibility of the display node.</li>
          <li>/// \sa Visibility2D, GetVisibility2D(),</li>
          <li>/// Visibility2DOn(), Visibility2DOff()</li>
          <li>vtkSetMacro(Visibility2D, int);</li>
          <li>/// Get the 2D visibility of the display node.</li>
          <li>/// \sa Visibility2D, SetVisibility2D(),</li>
          <li>/// Visibility2DOn(), Visibility2DOff()</li>
          <li>vtkGetMacro(Visibility2D, int);</li>
          <li>/// Set the 2D visibility of the display node.</li>
          <li>/// \sa Visibility2D, SetVisibility2D(),</li>
          <li>/// GetVisibility2D(),</li>
          <li>vtkBooleanMacro(Visibility2D, int);</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Slicer has been created with probably millions of hours of more than a hundred programmers, have been thoroughly tested and proven, and a multitude of special cases and complicated geometry issues have been addressed in the past years. I really suggest not reinventing the wheel, just using what is available.</p>

---

## Post #3 by @alientex (2025-04-30 10:21 UTC)

<p>Thank you for your response — I completely agree and appreciate the immense work that has gone into Slicer over the years.</p>
<p>I’m aware that slice intersection visibility is already built-in via the display node, and I fully intend to use those in actual projects. However, I’m reimplementing a basic version purely for learning purposes — to better understand how the rendering pipeline, transforms, and VTK/MRML components work together.</p>
<p>I’m not aiming to replicate full functionality, just exploring the basics to deepen my understanding. I really appreciate your guidance and insights.</p>
<p>Thanks again!</p>

---
