# How to change color of 3d-cube inside 3D-View?

**Topic ID**: 769
**Date**: 2017-07-26
**URL**: https://discourse.slicer.org/t/how-to-change-color-of-3d-cube-inside-3d-view/769

---

## Post #1 by @AJ_ZHU (2017-07-26 12:26 UTC)

<p>I am new to Slicer. I got a question:<br>
How to change color of 3D-cube inside 3D-view through python-interactor?<br>
Thanks a lot!<br>
Aijun</p>

---

## Post #2 by @Fernando (2017-07-26 16:17 UTC)

<p>I don’t think you can do that. But you can hide it and create your own:</p>
<pre><code class="lang-python"># Choose your color
RGB_COLOR = 0.2, 0.4, 0.8

# Hide the cube
v = slicer.util.getNode('View1')
v.SetBoxVisible(False)

# Create yours
cube = vtk.vtkCubeSource()
cube.SetXLength(200)
cube.SetYLength(200)
cube.SetZLength(200)
cube.Update()
cubePolyData = cube.GetOutput()

# Create a model with the cube and add it to scene
modelNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLModelNode')
modelNode.SetAndObservePolyData(cubePolyData)
modelNode.CreateDefaultDisplayNodes()
modelNode.SetName('My cube')

# Edit display properties
displayNode = modelNode.GetDisplayNode()
displayNode.SetLighting(False)
displayNode.SetColor(RGB_COLOR)
WIREFRAME = 1
displayNode.SetRepresentation(WIREFRAME)
displayNode.SetBackfaceCulling(False)
</code></pre>

---

## Post #3 by @AJ_ZHU (2017-07-27 18:03 UTC)

<p>Thanks you so much, Fernando!<br>
I do appreciate your help very well!</p>
<p>It worked well after I did a little bit change:<br>
<span class="hashtag">#modelNode</span> = slicer.mrmlScene.AddNewNodeByClass(‘vtkMRMLModelNode’)<br>
–&gt; modelNode = slicer.mrmlScene.AddNode(slicer.vtkMRMLModelNode())<br>
I am not sure of why AddNewNodeByClass was not there.</p>
<p>Thank you again! Great job!</p>
<p>regards,<br>
Aijun</p>

---

## Post #4 by @Fernando (2017-07-27 19:49 UTC)

<p>You can mark my answer so that it helps next person who gets in the thread for help.</p>
<aside class="quote no-group" data-username="AJ_ZHU" data-post="3" data-topic="769">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/db5fbb/48.png" class="avatar"> AJ_ZHU:</div>
<blockquote>
<p>I am not sure of why AddNewNodeByClass was not there.</p>
</blockquote>
</aside>
<p>You probably have an old version of Slicer. I think the <a href="https://github.com/Slicer/Slicer/commit/f6df62e88ea90092c2080f012364cead65d41fef" rel="noopener nofollow ugc">commit</a> that introduced that function is from May.</p>

---

## Post #5 by @AJ_ZHU (2017-07-27 19:51 UTC)

<p>Thanks a lot.<br>
I guess you are right, I am using an old one.</p>
<p>By the way, I am facing the new issue of the center. I got an model there, is there way to get the center of the model object so that I may get my cube-center matched?</p>
<p>Thanks in advance!<br>
Aijun</p>

---

## Post #6 by @Fernando (2017-07-27 19:56 UTC)

<p>Try <code>modelNode.GetPolyData().GetCenter()</code>.</p>

---

## Post #7 by @AJ_ZHU (2017-07-30 23:44 UTC)

<p>hi Fernando,<br>
Thanks a lot, But I am still stuck with how to get the modelNode.GetPolyData().GetCenter() working (I guess just because I am new). I am still not sure of the classes structures/config for the slicer view.</p>
<p>Best,<br>
Aijun</p>

---

## Post #8 by @Fernando (2017-07-31 00:03 UTC)

<aside class="quote no-group" data-username="AJ_ZHU" data-post="7" data-topic="769">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/db5fbb/48.png" class="avatar"> AJ_ZHU:</div>
<blockquote>
<p>I am still not sure of the classes structures/config for the slicer view.</p>
</blockquote>
</aside>
<p>I’m not sure I understand the problem. Can you please rephrase? What are you doing? What do you expect? What do you get?</p>

---

## Post #9 by @AJ_ZHU (2017-08-07 01:27 UTC)

<p>Hi Fernando,<br>
sorry for a long time to get back here to check with your expertise on the slicer.<br>
Here is a snapshot:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e1b6efdabb2c3896289bf0ae773e8042135cdad.png" alt="image" data-base62-sha1="b8Y1alUiUws2NNCYW50XsmJE5hH" width="435" height="386"><br>
you see here, I get your idea of making a new cube scene but I have to no idea how to get my object and the cube sharing the same center.</p>
<p>Thanks a lot,<br>
Aijun</p>

---

## Post #10 by @Fernando (2017-11-18 15:24 UTC)

<p>I just saw your answer. Were you able to solve the problem?</p>

---

## Post #11 by @lassoan (2021-06-07 00:13 UTC)

<p>A post was split to a new topic: <a href="/t/how-to-change-the-size-of-the-cube-in-3d-views/17983">How to change the size of the cube in 3D views</a></p>

---
