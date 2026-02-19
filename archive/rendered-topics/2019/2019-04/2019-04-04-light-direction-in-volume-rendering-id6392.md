---
topic_id: 6392
title: "Light Direction In Volume Rendering"
date: 2019-04-04
url: https://discourse.slicer.org/t/6392
---

# Light direction in volume rendering

**Topic ID**: 6392
**Date**: 2019-04-04
**URL**: https://discourse.slicer.org/t/light-direction-in-volume-rendering/6392

---

## Post #1 by @Melodicpinpon (2019-04-04 11:03 UTC)

<p>Hello,</p>
<p>Is there a way to change the direction of the light source within 3D slicer. I found the material properties options, but in order to create illustration with the same lightning, it may me helpfull for me to be able to define the direction of the light.</p>

---

## Post #2 by @pieper (2019-04-04 12:16 UTC)

<p>Yes, you can access the renderer and set up the lights however you want via the python interface as shown below.</p>
<p><a href="https://vtk.org/doc/nightly/html/classvtkLight.html" class="onebox" target="_blank" rel="nofollow noopener">https://vtk.org/doc/nightly/html/classvtkLight.html</a></p>
<pre><code class="lang-auto">&gt;&gt;&gt; v = slicer.app.layoutManager().threeDWidget(0).threeDView()
&gt;&gt;&gt; v.renderWindow()
(vtkRenderingOpenGL2Python.vtkGenericOpenGLRenderWindow)0x12ea318d8
&gt;&gt;&gt; v.renderWindow().GetRenderers().GetItemAsObject(0)
(vtkRenderingOpenGL2Python.vtkOpenGLRenderer)0x12ea358d8
&gt;&gt;&gt; v.renderWindow().GetRenderers().GetItemAsObject(0)
(vtkRenderingOpenGL2Python.vtkOpenGLRenderer)0x12ea358d8
&gt;&gt;&gt; v.renderWindow().GetRenderers().GetItemAsObject(0).GetLights()
(vtkRenderingCorePython.vtkLightCollection)0x12ea359a8
&gt;&gt;&gt; v.renderWindow().GetRenderers().GetItemAsObject(0).GetLights().GetItemAsObject(0).SetColor([1,0,0])
</code></pre>

---

## Post #3 by @Melodicpinpon (2019-10-10 11:54 UTC)

<p>Thank you for your answer.<br>
As a non coder; I wont invest the time to use it.<br>
But thank you.</p>

---

## Post #4 by @lassoan (2019-10-16 20:25 UTC)

<p>I’ve added a module that you can use to customize lighting without Python scripting. See details here: <a href="https://discourse.slicer.org/t/new-module-to-customize-lighting-in-3d-view/8804" class="inline-onebox">New module to customize lighting in 3D view</a></p>

---

## Post #5 by @Melodicpinpon (2019-10-16 23:35 UTC)

<p>Good evening Mr Lasso;</p>
<p>Thank you for your answer anf for this new development.</p>
<p>This is simply great. I did not think that I would ever see this in 3D slicer.<br>
You make me want to learn more about the program every time.</p>
<p>Kind regards,</p>
<p>Gauthier</p>
<p>Le mer. 16 oct. 2019 à 22:35, Andras Lasso via 3D Slicer Community <a href="mailto:slicer@discoursemail.com">slicer@discoursemail.com</a> a écrit :</p>

---
