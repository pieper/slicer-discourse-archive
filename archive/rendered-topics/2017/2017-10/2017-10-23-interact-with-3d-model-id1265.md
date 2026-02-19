---
topic_id: 1265
title: "Interact With 3D Model"
date: 2017-10-23
url: https://discourse.slicer.org/t/1265
---

# Interact with 3D model

**Topic ID**: 1265
**Date**: 2017-10-23
**URL**: https://discourse.slicer.org/t/interact-with-3d-model/1265

---

## Post #1 by @Frederic (2017-10-23 15:36 UTC)

<p>Hi all,<br>
I have an actor/mapper misunderstood with 3d slicer.<br>
I want to interact in python, with my 3d model, but I don’t know how to access to the “GetOutput” of my loading model.</p>
<p>Pragmatically, how to find (in bold) that:</p>
<blockquote>
<p>reader = vtk.vtkSTLReader()<br>
reader.SetFileName(“human-head.stl”)<br>
X=vtk.X()<br>
X.SetInputConnection(<strong>reader.GetOutputPort()</strong>)`</p>
</blockquote>
<p>with that:</p>
<blockquote>
<p>model = slicer.util.loadModel(“/netapp/vol1_homeunix/briend/human-head.stl”, returnNode=True)[1]</p>
</blockquote>
<p>Thanks in advance,<br>
Frederic</p>

---

## Post #2 by @lassoan (2017-10-23 17:30 UTC)

<p>In general, you display surface meshes using a model node. You can create a model node directly from a file using this utility function:</p>
<pre><code>slicer.util.loadModel('something.stl')
</code></pre>
<p>If you already have a vtkPolyData object, then you can create a model using:</p>
<pre><code>slicer.modules.models.logic().AddModel(myPolyData)</code></pre>

---

## Post #3 by @Frederic (2017-10-24 09:59 UTC)

<p>Thanks Andrea,<br>
But in fact, I want to connect the output port of one algorithm (my model loaded by ‘slicer.util.loadModel(‘model.stl’)’  to the input port of another algorithm (here called X).</p>
<blockquote>
<p><strong>model</strong>=slicer.util.loadModel(‘model.stl’)<br>
X=vtk.X()<br>
X.SetInputConnection(<strong>model</strong>.GetOutputPort())`</p>
</blockquote>
<p>How to process to that?</p>

---

## Post #4 by @lassoan (2017-10-24 13:00 UTC)

<p>You can get/set polydata connection using <code>GetPolyDataConnection</code> and <code>SetPolyDataConnection</code>. For example:</p>
<pre><code>[success, model]=slicer.util.loadModel("model.stl", returnNode=True)
smoother = vtk.vtkSmoothPolyDataFilter()
smoother.SetNumberOfIterations(300)
smoother.SetInputConnection(model.GetPolyDataConnection())
model.SetPolyDataConnection(smoother.GetOutputPort())</code></pre>

---

## Post #5 by @Frederic (2017-10-24 13:59 UTC)

<p>Thanks Andrea,</p>
<p>But I always miss the reader.GetOutputPort().<br>
I am sorry but I do not understand how slicer use VTK (always this actor/mapper question), thus in Slicer, I am lost how to access to the:</p>
<blockquote>
<p>.GetProperty().SetColor(1,0,0) or SetPointSize(20)</p>
</blockquote>
<p>Typically, without actor/mapper, how to do that with 3d slicer:</p>
<pre><code>reader = vtk.vtkSTLReader()
reader.SetFileName(‘model.stl’)

p0=[0]*3
pd = reader.GetOutput()
pd.GetNumberOfPoints()
loc = vtk.vtkPointLocator()
loc.SetDataSet(pd)
loc.BuildLocator()
closestPointId = loc.FindClosestPoint(p0)
</code></pre>

---

## Post #6 by @lassoan (2017-10-24 23:25 UTC)

<p>Those properties can be set through the display node.</p>
<pre><code>myModelNode.GetDisplayNode().Set...
</code></pre>
<p>See <a href="http://apidocs.slicer.org/master/classvtkMRMLDisplayNode.html">http://apidocs.slicer.org/master/classvtkMRMLDisplayNode.html</a> and <a href="http://apidocs.slicer.org/master/classvtkMRMLModelDisplayNode.html">http://apidocs.slicer.org/master/classvtkMRMLModelDisplayNode.html</a> for details.</p>

---

## Post #7 by @Frederic (2017-10-25 13:25 UTC)

<p>Perfect,<br>
Thanks one again <a class="mention" href="/u/lassoan">@lassoan</a>, and sorry for my newby question.<br>
Best.</p>
<p>Ps: I completed my script to calculate distance along the surface in slicer. I will probably value it in implementing my python lines in an extension in a couple of days.</p>

---
