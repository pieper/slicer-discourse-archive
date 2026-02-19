---
topic_id: 25380
title: "How To Edit Line Width Thickness From Line Generated From Vt"
date: 2022-09-21
url: https://discourse.slicer.org/t/25380
---

# How to Edit line width/thickness from line generated from vtk polydata?

**Topic ID**: 25380
**Date**: 2022-09-21
**URL**: https://discourse.slicer.org/t/how-to-edit-line-width-thickness-from-line-generated-from-vtk-polydata/25380

---

## Post #1 by @Jack_Zhang (2022-09-21 20:37 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 5.0.3</p>
<p>I’m trying to code a python extension that plots a line using points read from a csv file. After creating the script to add the required values to a vtkPoints and vtkPolyLine objects, I was able to render the line using the following:</p>
<pre><code class="lang-auto"># Create a polydata to store everything in
polyData = vtk.vtkPolyData()

# Add the points to the dataset
polyData.SetPoints(points)

# Add the lines to the dataset
polyData.SetLines(cells)

slicer.modules.models.logic().AddModel(polyData)
</code></pre>
<p>Output:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7bd810f6bd6efe1ea8fb3873e7603cf91d46abb5.png" alt="image" data-base62-sha1="hFzEdC4uBjx5tZEPaILwd01VVyd" width="676" height="413"></p>
<p>I now want to edit the line thickness.</p>
<p>When I use vtk outside of slicer, I would just use the following:</p>
<pre><code class="lang-auto"># Setup actor and mapper
mapper = vtkPolyDataMapper()
mapper.SetInputData(polyData)

actor = vtkActor()
actor.SetMapper(mapper)
actor.GetProperty().SetLineWidth(5)

# Setup render window, renderer, and interactor
renderer = vtkRenderer()
renderWindow = vtkRenderWindow()
renderWindow.SetWindowName('PolyLine')
renderWindow.AddRenderer(renderer)
renderWindowInteractor = vtkRenderWindowInteractor()
renderWindowInteractor.SetRenderWindow(renderWindow)
renderer.AddActor(actor)
renderWindow.Render()
renderWindowInteractor.Start()
</code></pre>
<p>However, I’m not sure how to use actor and renderer with Slicer. Is there a way of using actors in a Slicer scene?</p>
<p>I know the <em>Models</em> module’s UI has a line width slider, so I’m probably just missing something. I’ve tried looking in the logic file for the <em>Models</em> module, but haven’t found anything I can use. Any help at all would be appreciated.</p>

---

## Post #2 by @pieper (2022-09-21 20:49 UTC)

<p>Slicer uses. concept called a “displayable manager”.  You can search the code and this forum for <code>MRMLDM</code> and find discussions.  This is the part of the code that manages mapping from the MRML scene to the mappers/actors at the vtk rendering system level.</p>

---

## Post #3 by @Jack_Zhang (2022-09-21 20:49 UTC)

<p>Thanks I’ll give that a try.</p>

---

## Post #4 by @Jack_Zhang (2022-09-22 15:19 UTC)

<p>I found the solution. I used the following code to get the actor being used by the 3D renderer and then modify its line width property.</p>
<pre><code class="lang-auto"># Get renderer actor
actor = slicer.app.layoutManager().activeThreeDRenderer().GetActors().GetLastActor()

# Adjust line width property
actorProperty = actor.GetProperty()
actorProperty.SetLineWidth(3)
</code></pre>

---
