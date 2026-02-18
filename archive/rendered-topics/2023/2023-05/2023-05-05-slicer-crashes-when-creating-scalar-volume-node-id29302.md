# Slicer crashes when creating scalar volume node

**Topic ID**: 29302
**Date**: 2023-05-05
**URL**: https://discourse.slicer.org/t/slicer-crashes-when-creating-scalar-volume-node/29302

---

## Post #1 by @nnzzll (2023-05-05 09:06 UTC)

<p>I try to create a <code>vtkMRMLScalarVolumeNode</code> by calling <code>slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode")</code>, but slicer crashed after calling this method.</p>
<p>Messages below are output of terminal:</p>
<pre><code class="lang-auto">Input port 0 of algorithm vtkImageThreshold(0x562d37c530a0) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageMapToWindowLevelColors(0x562d37c696f0) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageMapToWindowLevelColors(0x562d37c696f0) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageThreshold(0x562d37c530a0) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageMapToWindowLevelColors(0x562d37c696f0) has 0 connections but is not optional.


Segmentation fault (core dumped)
</code></pre>
<p>I used gdb to debug the program and found that Slicer crashed at <code>build/VTK/Rendering/OpenGL2/vtkOpenGLImageMapper.cxx:616</code></p>
<pre><code class="lang-auto">  switch (data-&gt;GetPointData()-&gt;GetScalars()-&gt;GetDataType())
</code></pre>
<p><code>data-&gt;GetPointData()-&gt;GetScalars()</code> returns a nullptr which triggered the segmentation fault.</p>
<p>How can I fix this problem? It works fine on Windows but crashes everytime on my ubuntu desktop.</p>
<p>OS: ubuntu 18.04<br>
Slicer Version:5.0.3 (7ea0f439e837fca8c92a315fb0b2a9b0ff28e1e4)</p>

---

## Post #2 by @pearsonm (2023-05-05 23:25 UTC)

<p>Can you show more of the code? That call works as expected on my ubuntu 22.04 machine.</p>

---

## Post #3 by @nnzzll (2023-05-06 01:26 UTC)

<p>There is no more code.<br>
Just start a Slicer program and type <code>slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode")</code> in the python interactor, then Slicer crashes.</p>

---

## Post #4 by @lassoan (2023-05-06 17:09 UTC)

<p>We have <a href="https://github.com/Slicer/Slicer/issues/6381">fixed this crash some time ago</a>. Please use current version of Slicer.</p>
<p>That said, while we try to add safety checks everywhere in the code, if you use the API in unexpected ways (in this case, create a volume node and not set image data in it) then problems may occur. Feel free to keep reporting these, as we can make the API more robust based on these feedbacks.</p>

---
