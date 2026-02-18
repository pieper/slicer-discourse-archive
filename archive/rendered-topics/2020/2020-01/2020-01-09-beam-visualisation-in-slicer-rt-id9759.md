# Beam Visualisation in Slicer RT

**Topic ID**: 9759
**Date**: 2020-01-09
**URL**: https://discourse.slicer.org/t/beam-visualisation-in-slicer-rt/9759

---

## Post #1 by @electus (2020-01-09 15:19 UTC)

<p>Hi guys,</p>
<p>I am develeping a tool for slicer that needs a very similar functionality compared to Slicer RT.</p>
<p>I want to display beam in the slicer scene just like it is done in Slcier RT. But i am not very far with that.<br>
I was trying to get into that and managed to draw lines. I found out about vtkMRMLModel(Display)Node and so on.</p>
<p>But could someone please give me a more or less detailed explenation how this task was carried out in Slicer RT, maybe even with a little bit of code.</p>
<p>I’d be very thankful.<br>
Cheers</p>

---

## Post #2 by @Sam_Horvath (2020-01-09 15:40 UTC)

<p>So, the code for how SlicerRT generates the beam model is here:<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/SlicerRt/SlicerRT/blob/f78335ba182b5f76eea5fcf8be9b3cfe17a4872f/Beams/MRML/vtkMRMLRTBeamNode.cxx#L495" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerRt/SlicerRT/blob/f78335ba182b5f76eea5fcf8be9b3cfe17a4872f/Beams/MRML/vtkMRMLRTBeamNode.cxx#L495" target="_blank" rel="nofollow noopener">SlicerRt/SlicerRT/blob/f78335ba182b5f76eea5fcf8be9b3cfe17a4872f/Beams/MRML/vtkMRMLRTBeamNode.cxx#L495</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="485" style="counter-reset: li-counter 484 ;">
<li>void vtkMRMLRTBeamNode::UpdateGeometry()
</li>
<li>{
</li>
<li>  // Make sure display node exists
</li>
<li>  this-&gt;CreateDefaultDisplayNodes();
</li>
<li>
</li>
<li>  // Update beam poly data based on jaws and MLC
</li>
<li>  this-&gt;CreateBeamPolyData();
</li>
<li>}
</li>
<li>
</li>
<li>//---------------------------------------------------------------------------
</li>
<li class="selected">void vtkMRMLRTBeamNode::CreateBeamPolyData(vtkPolyData* beamModelPolyData/*=nullptr*/)
</li>
<li>{
</li>
<li>  if (!beamModelPolyData)
</li>
<li>  {
</li>
<li>    beamModelPolyData = this-&gt;GetPolyData();
</li>
<li>  }
</li>
<li>  if (!beamModelPolyData)
</li>
<li>  {
</li>
<li>    vtkErrorMacro("CreateBeamPolyData: Invalid beam node");
</li>
<li>    return;
</li>
<li>  }
</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>But it is not the most informative.  In general, what you are going to want to do is</p>
<ol>
<li>Create a vtkPolyData containing the model</li>
<li>Attach the polydata to a vtkMRMLModelNode (SetAndObservePolyData)</li>
<li>Use the Model Node’s associated display node properties to set color, opacity, etc</li>
</ol>
<p>To create the polydata in (1), there a a number of quick ways to create a simple cylinder model:</p>
<ol>
<li><a href="https://vtk.org/Wiki/VTK/Examples/Cxx/GeometricObjects/Cylinder" rel="nofollow noopener">vtkCylinderSource</a></li>
<li><a href="https://vtk.org/Wiki/VTK/Examples/Cxx/PolyData/TubeFilter" rel="nofollow noopener">vtkTubeFilter</a></li>
</ol>

---

## Post #3 by @electus (2020-01-09 15:55 UTC)

<p>Thanks a lot for the reply.</p>
<p>Could you please give me a quick example of lets say connecting 3 points with straight lines and displaying them on slicer.<br>
I think I would be able to work from there on.</p>
<p>Please note I am working in Python.</p>

---

## Post #4 by @Sam_Horvath (2020-01-09 16:22 UTC)

<p>Here is a small example</p>
<pre><code class="lang-python">import slicer
import vtk

#Create node for model
lineNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLModelNode')
lineNode.SetName('Lines')
lineNode.CreateDefaultDisplayNodes()

#Create Polydata, 
points = vtk.vtkPoints()
points.SetNumberOfPoints(3)

points.SetPoint(0, 0.0, 0.0, 0.0)
points.SetPoint(1,   0.0, 20.0, 0.0)
points.SetPoint(2,   0.0,  0.0, 20.0)

line = vtk.vtkLineSource()
line.SetPoints(points)
line.Update()

#attach polydata to model node
lineNode.SetAndObservePolyData(line.GetOutput())

#Visibility
disp = lineNode.GetModelDisplayNode()
disp.SetVisibility(True)
disp.SetLineWidth(10.0)
</code></pre>
<p>The <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository" rel="nofollow noopener">python script repository</a> is a good resource for slicer python code snippets</p>

---

## Post #5 by @lassoan (2020-01-09 16:36 UTC)

<p>You can make things even simpler by using Models module logic’s <code>AddModel</code> method (it creates model and display nodes and add them to the scene):</p>
<pre><code class="lang-python">points = vtk.vtkPoints()
points.SetNumberOfPoints(3)
points.SetPoint(0, 0.0, 0.0, 0.0)
points.SetPoint(1,   0.0, 20.0, 0.0)
points.SetPoint(2,   0.0,  0.0, 20.0)
line = vtk.vtkLineSource()
line.SetPoints(points)
lineNode = slicer.modules.models.logic().AddModel(line.GetOutputPort())
</code></pre>

---

## Post #6 by @electus (2020-01-10 14:07 UTC)

<p>Hi thanks a lot.<br>
This worked well and i could play around with it and using many line sources would serve my task.<br>
I was wondering if a source already exists that combines the line sources and models a rectangular divergent beam.</p>
<p>I was trying to figure out how Slicer RT did it</p>
<pre><code>points = vtk.vtkPoints()
points.SetNumberOfPoints(5)
cellArray = vtk.vtkCellArray()

x1 = -100.0
x2 = 100
y1 = -100
y2 = 100

points.SetPoint(0, 0.0, 0.0, -212.0)
points.SetPoint(1, x1, y1, -212.0)
points.SetPoint(2, x1, y2, -212.0)
points.SetPoint(3, x2, y2, -212.0)
points.SetPoint(3, x2, y1, -212.0)

cellArray.InsertNextCell(3)
cellArray.InsertCellPoint(0)
cellArray.InsertCellPoint(1)
cellArray.InsertCellPoint(2)

cellArray.InsertNextCell(3)
cellArray.InsertCellPoint(0)
cellArray.InsertCellPoint(2)
cellArray.InsertCellPoint(3)

cellArray.InsertNextCell(3)
cellArray.InsertCellPoint(0)
cellArray.InsertCellPoint(3)
cellArray.InsertCellPoint(4)

cellArray.InsertNextCell(3)
cellArray.InsertCellPoint(0)
cellArray.InsertCellPoint(4)
cellArray.InsertCellPoint(1)


cellArray.InsertNextCell(4)
cellArray.InsertCellPoint(1)
cellArray.InsertCellPoint(2)
cellArray.InsertCellPoint(3)
cellArray.InsertCellPoint(4)


line = vtk.vtkLineSource()
line.SetPoints(points)
line.SetPolys(cellArray)

lineNode = slicer.modules.models.logic().AddModel(line.GetOutputPort())
</code></pre>
<p>And I am not quite sure which type of vtkSource was used here.<br>
And what is the reason, that the lines, that I already got with your help, are only visible in 3D part, but not in the other scenes (R, Y, G).</p>
<p>Thanks a lot again and have a  nice weekend!</p>

---

## Post #7 by @lassoan (2020-01-10 14:18 UTC)

<p>What would you like to achieve? Why don’t you use/customize/enhance SlicerRT instead of renplementing selected features of it?</p>

---

## Post #8 by @electus (2020-01-10 18:58 UTC)

<p>I am trying to create treatment planning modalities. And I have thought about extending RT. But I need to do quite some things differently then performed in Slicer RT.<br>
For example the source itself is different already, so I need to create an own model therefore anyways.<br>
That’s why I was trying to break it down, how this task was carried out in Slicer RT.<br>
But I’m struggling a little, that’s why I asked for help <img src="https://emoji.discourse-cdn.com/twitter/blush.png?v=9" title=":blush:" class="emoji" alt=":blush:"></p>

---

## Post #9 by @cpinter (2020-01-11 09:22 UTC)

<p>SlicerRT is created to be modular and extensible. External Beam Planning supports adding any kind of dose computation engine and model. I have a hard time imagining how things could get easier for you starting from scratch and reimplementing 90% of the same features to add your own 10%. Also, working in an established open-source project ensures always high quality code and outsources some of the maintenance burden, so I strongly suggest taking some time to look at the SlicerRT code instead of starting from hello-world type code as you do here. We are here to help, so if you have any question about how things are done in SlicerRT and why, we are happy to answer!</p>

---

## Post #10 by @electus (2020-01-12 12:36 UTC)

<p>Thanks for your reply.</p>

---

## Post #11 by @electus (2020-01-12 12:51 UTC)

<p>Can I please ask how lines created like shown above, can also be made visible in the red, yellow and green scenes. For now they are only visible in the 3d represetation of the cube.</p>
<p>Thanks</p>

---
