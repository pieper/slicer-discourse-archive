---
topic_id: 7562
title: "Display Fibers As Tube With Non Uniform Radius"
date: 2019-07-13
url: https://discourse.slicer.org/t/7562
---

# Display fibers as tube with non-uniform radius

**Topic ID**: 7562
**Date**: 2019-07-13
**URL**: https://discourse.slicer.org/t/display-fibers-as-tube-with-non-uniform-radius/7562

---

## Post #1 by @fpsiddiqui91 (2019-07-13 15:20 UTC)

<p>Hello Developers,<br>
I am trying to implement something similar to center line module. I want a non unifrom tube (something like vessel) around my fibers.</p>
<p>Can you guide how can I get something like this? How can I use center line module in my own application?</p>
<p>Thank you</p>

---

## Post #2 by @lassoan (2019-07-13 23:57 UTC)

<p>If your input is vtkPolyData with points and point scalars for radius then you can use vtkTubeFilter to generate tube with the desired radius at each point.</p>

---

## Post #3 by @fpsiddiqui91 (2019-07-14 11:10 UTC)

<p>Thank you for your response. I am generating the tube around my points like this</p>
<pre><code>  def createTube(self,cord):
print ("tube mai")

modelNode = slicer.vtkMRMLModelNode()#slicer.util.getNode('SphereModel')
sizeLine = np.shape(cord)
numPoints=sizeLine[0]
lineCellArray = vtk.vtkCellArray()
lineCellArray.InsertNextCell(numPoints)
points = vtk.vtkPoints()

for i in xrange(numPoints):
  points.InsertPoint(i,cord[i])

for i in xrange(numPoints):
  lineCellArray.InsertCellPoint(i)

linePolyData = vtk.vtkPolyData()
linePolyData.SetPoints(points)
linePolyData.SetLines(lineCellArray)

tubeSegmentFilter = vtk.vtkTubeFilter()
tubeSegmentFilter.SetInputData(linePolyData)
tubeSegmentFilter.SetRadius(5)  # INSERT VALUE
tubeSegmentFilter.SetNumberOfSides(10)  # INSERT VALUE
tubeSegmentFilter.CappingOn()
tubeSegmentFilter.Update()
display=modelNode.GetDisplayNode()
display.SetOpacity(0.5)
modelNode.SetAndObservePolyData(tubeSegmentFilter.GetOutput())
</code></pre>
<p>The problem is I cannot give Radius array as tubeSegmentFilter.SetRadius(Array).   It requires float as an input.</p>
<p>Thank you so much for your help.</p>

---

## Post #4 by @ljod (2019-07-14 11:58 UTC)

<p>Check out the vtk doc on this filter:<br>
<a href="https://vtk.org/doc/nightly/html/classvtkTubeFilter.html" class="onebox" target="_blank" rel="nofollow noopener">https://vtk.org/doc/nightly/html/classvtkTubeFilter.html</a></p>
<p>Look at the methods related to VaryRadius. Not sure how you specify which scalar to use, but probably setting the active scalar on your polydata will work.</p>

---

## Post #5 by @fpsiddiqui91 (2019-07-14 12:31 UTC)

<p>Thank you so much for you help Andras and Lauren. I have managed to fix the problem. I am attaching the code for others.</p>
<pre><code>  def createTube(self,cord):


modelNode = slicer.vtkMRMLModelNode()#slicer.util.getNode('SphereModel')
sizeLine = np.shape(cord)
numPoints=sizeLine[0]
lineCellArray = vtk.vtkCellArray()
lineCellArray.InsertNextCell(numPoints)
points = vtk.vtkPoints()

for i in xrange(numPoints):
  points.InsertPoint(i,cord[i])

for i in xrange(numPoints):
  lineCellArray.InsertCellPoint(i)

#Add radius
tubeRadius=vtk.vtkDoubleArray()
tubeRadius.SetNumberOfTuples(numPoints)
tubeRadius.SetName("TubeRadius")

for i in range(numPoints):
  radius=0.5*i   #variable radius
  tubeRadius.SetTuple1(i, radius)


linePolyData = vtk.vtkPolyData()
linePolyData.SetPoints(points)
linePolyData.SetLines(lineCellArray)
linePolyData.GetPointData().AddArray(tubeRadius)
linePolyData.GetPointData().SetActiveScalars("TubeRadius")




tubeSegmentFilter = vtk.vtkTubeFilter()
tubeSegmentFilter.SetInputData(linePolyData)

tubeSegmentFilter.SetNumberOfSides(10)  # INSERT VALUE
tubeSegmentFilter.CappingOn()
tubeSegmentFilter.SetVaryRadiusToVaryRadiusByAbsoluteScalar()
tubeSegmentFilter.Update()

modelNode.SetAndObservePolyData(tubeSegmentFilter.GetOutput())
modelDisplay = slicer.vtkMRMLModelDisplayNode()
modelDisplay.SetOpacity(0.5)
slicer.mrmlScene.AddNode(modelDisplay)
modelNode.SetAndObserveDisplayNodeID(modelDisplay.GetID())
modelDisplay.SetInputPolyDataConnection(modelNode.GetPolyDataConnection())
slicer.mrmlScene.AddNode(modelNode)</code></pre>

---

## Post #6 by @Roni (2019-07-18 09:36 UTC)

<p><a class="mention" href="/u/fpsiddiqui91">@fpsiddiqui91</a></p>
<p>Grt that you found the solution. I am sort of stuck on a more implementation of my question. I already have a centerline computed, which had points and radius. But i just don’t know how i can use them?</p>
<p>Andras had answered and i went through the vtk examples. However, i am an ameture in python coding and i also do not know the child functions of each module. So your explanation would help someone beginner like me. My question is</p>
<ol>
<li>Could you may be help me understand the logic/steps you are taking by just typing comments next to the steps? (e.g. i want to know if you are generating the points and radius or using it from some model?)</li>
<li>what would be your advice if i already have the points and radius for each center point? (which part of code should i ignore? and if you know which child function to use to port the data.</li>
</ol>
<p>e.g.<br>
<code>1 c = getNode('ComputationModel')</code><br>
computation model is computed based on vmtk centerlinemodel</p>
<p><code>2 lineMapper = vtk.vtkPolyDataMapper()</code><br>
<code>3 lineMapper.SetInputConnection(c.GetOutputPort())</code><br>
–&gt; I want to directly feed the points and radius from my model in this step<br>
<code>get error at this step.. object has no attribute 'GetOutputPort'</code></p>
<p>if i change line 3 to<br>
<code>3 lineMapper.SetInputConnection(c.GetOutputPolyData())</code><br>
<code>get error at this step.. object has no attribute 'GetOutputPolyData'</code></p>
<p>Your insight would be really helpful.</p>

---

## Post #7 by @fpsiddiqui91 (2019-07-18 11:45 UTC)

<p>Hey,</p>
<p>I am actually getting my points and Radius from my own functions (They are just numpy arrays). I am just feeding them in visualization pipeline. You can find in the code how it has been converted to vtk points.</p>
<p>Moreover, computational model does not have Getoutput fuction in it. you need to extract the points, make a line out of it and then you can use the tube filter .</p>
<p>See the code:</p>
<pre><code class="lang-python">def createTube(self,cord,Radius,Opacity,Color):   ##input arguments are the points, Radius , Opacity of the tube and Color
    print ("tube mai")

    modelNode = slicer.vtkMRMLModelNode()
    sizeLine = np.shape(cord)
    numPoints=sizeLine[0]
    lineCellArray = vtk.vtkCellArray()
    lineCellArray.InsertNextCell(numPoints)
    points = vtk.vtkPoints()

    for i in xrange(numPoints):
      points.InsertPoint(i,cord[i])             #These points are calculated in my own function

    for i in xrange(numPoints):
      lineCellArray.InsertCellPoint(i)

    #Add radius
    tubeRadius=vtk.vtkDoubleArray()
    tubeRadius.SetNumberOfTuples(numPoints)
    tubeRadius.SetName("TubeRadius")

    for i in range(numPoints):

      tubeRadius.SetTuple1(i, Radius[i])       #Radius is feeded in from another function


    linePolyData = vtk.vtkPolyData()
    linePolyData.SetPoints(points)
    linePolyData.SetLines(lineCellArray)
    linePolyData.GetPointData().AddArray(tubeRadius)
    linePolyData.GetPointData().SetActiveScalars("TubeRadius")


    modelNode1 = slicer.vtkMRMLModelNode()
    modelNode1.SetAndObservePolyData(linePolyData)
    modelDisplay1 = slicer.vtkMRMLModelDisplayNode()
    modelDisplay1.SetVisibility(True)
    modelDisplay1.SetColor(0.7, 0.1, 0.1)
    modelDisplay1.BackfaceCullingOff()
    modelDisplay1.SetLineWidth(3.5)


    slicer.mrmlScene.AddNode(modelDisplay1)
    modelNode1.SetAndObserveDisplayNodeID(modelDisplay1.GetID())
    modelDisplay1.SetInputPolyDataConnection(modelNode1.GetPolyDataConnection())
    slicer.mrmlScene.AddNode(modelNode1)



    tubeSegmentFilter = vtk.vtkTubeFilter()
    tubeSegmentFilter.SetInputData(linePolyData)

    tubeSegmentFilter.SetNumberOfSides(10)  # INSERT VALUE
    tubeSegmentFilter.CappingOn()
    tubeSegmentFilter.SetVaryRadiusToVaryRadiusByAbsoluteScalar()
    tubeSegmentFilter.Update()

    modelNode.SetAndObservePolyData(tubeSegmentFilter.GetOutput())
    modelDisplay = slicer.vtkMRMLModelDisplayNode()
    modelDisplay.SetOpacity(Opacity)
    modelDisplay.SetColor(Color)
    slicer.mrmlScene.AddNode(modelDisplay)
    modelNode.SetAndObserveDisplayNodeID(modelDisplay.GetID())
    modelDisplay.SetInputPolyDataConnection(modelNode.GetPolyDataConnection())
    slicer.mrmlScene.AddNode(modelNode)
</code></pre>

---

## Post #8 by @Roni (2019-07-18 13:08 UTC)

<p>Hi <a class="mention" href="/u/fpsiddiqui91">@fpsiddiqui91</a> , Thanks for the quick reply and information.</p>
<p>Not sure if i understood completely your code, so just request you to breakit down for me.</p>
<pre><code class="lang-auto">modelNode = slicer.vtkMRMLModelNode()   #does it create the node or it get's a node?
sizeLine = np.shape(cord)   #what is np here ? and what becomes SizeLine ?
numPoints=sizeLine[0]    #this gives you single number say 200/15 depending on value in [0] point?
lineCellArray = vtk.vtkCellArray()  
lineCellArray.InsertNextCell(numPoints) #Don't get this statement at all.
points = vtk.vtkPoints()  

for i in xrange(numPoints):  #what is xrange? how do you define it?
  points.InsertPoint(i,cord[i])             

for i in xrange(numPoints): #Same what is xrange?
  lineCellArray.InsertCellPoint(i)

#Add radius
tubeRadius=vtk.vtkDoubleArray()
tubeRadius.SetNumberOfTuples(numPoints)
tubeRadius.SetName("TubeRadius")

for i in range(numPoints):   #What is range here? where is it defined?

  tubeRadius.SetTuple1(i, Radius[i])       


linePolyData = vtk.vtkPolyData()
linePolyData.SetPoints(points)
linePolyData.SetLines(lineCellArray)
linePolyData.GetPointData().AddArray(tubeRadius)
linePolyData.GetPointData().SetActiveScalars("TubeRadius")
</code></pre>
<p>Could you clarify the comments/questions asked after # in your code above? I know i sound really newbie, but if you could do that, it will be a great help.<br>
Thanks</p>

---

## Post #9 by @lassoan (2019-07-18 13:18 UTC)

<p>To speed up your progress, I would recommend to do a Python introduction tutorial, read the VTK textbook, play a bit with VTK examples, and complete Slicer programming tutorials. See links in <a href="https://discourse.slicer.org/t/a-free-biomedical-image-analysis-and-visualization-2-day-course/2584/10">this post</a>.</p>

---

## Post #10 by @Roni (2019-07-22 07:43 UTC)

<p>Thanks Andras for the information about resources. That’s very helpful.</p>

---
