---
topic_id: 19583
title: "Cant Display Vtkcubeaxesactor2D In Slice View"
date: 2021-09-08
url: https://discourse.slicer.org/t/19583
---

# Can't display `vtkCubeAxesActor2D` in slice view

**Topic ID**: 19583
**Date**: 2021-09-08
**URL**: https://discourse.slicer.org/t/cant-display-vtkcubeaxesactor2d-in-slice-view/19583

---

## Post #1 by @keri (2021-09-08 19:27 UTC)

<p>Hi,</p>
<p>In an attempt to display <code>vtkCubeAxesActor2D</code> I use the code:</p>
<pre><code class="lang-python"># Get renderer and camera
layoutManager = slicer.app.layoutManager()
view = layoutManager.sliceWidget('Red').sliceView()
renderWindow = view.renderWindow()
renderers = renderWindow.GetRenderers()
renderer = renderers.GetItemAsObject(0)
camera = renderer.GetActiveCamera()

# Customize vtkCubeAxesActor2D
cubeAxesActor = vtk.vtkCubeAxesActor2D()
cubeAxesActor.SetBounds(-50, 50, -50, 50, -50, 50)    # some boundary points
cubeAxesActor.SetCamera(camera)
cubeAxesActor.SetXAxisVisibility(1)
cubeAxesActor.SetYAxisVisibility(1)
cubeAxesActor.SetZAxisVisibility(1)
cubeAxesActor.SetVisibility(1)
renderer.AddActor(cubeAxesActor)

# Update views
slicer.util.forceRenderAllViews()
</code></pre>
<p>this snippet of code doesn’t show anything.</p>
<p>I look to the <code>vtkMRMLRulerDisplayableManager</code> source code and I feel that I pretty understand how <code>vtkMRMLRulerDisplayableManager</code> works but it uses <code>vtkAxisActor2D</code> instead.</p>
<p>There is a thing that I can’t understand: what is <code>layers</code> in slice view? Is slice view is represented by somehow overlapping square planes and there is foreground layer and background?</p>

---

## Post #2 by @keri (2021-09-08 21:53 UTC)

<p>I just figured out that I should have used boundary in range from 0 to 1:</p>
<pre><code class="lang-python">cubeAxesActor.SetBounds(0.1, 0.9, 0.1, 0.9, 0.1, 0.9)
</code></pre>
<p>The question about slice’s layers is still actual…</p>

---

## Post #3 by @jamesobutler (2021-09-08 22:14 UTC)

<p>Yes a slice view has layers including background volume, foreground volume and labelmap volume. This is why you can’t overlay say 4 volumes at once and see them all at the same time in the same slice viewer. See</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html?highlight=background%20layer#slice-view" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html?highlight=background%20layer#slice-view</a></p>

---

## Post #4 by @keri (2021-09-09 13:02 UTC)

<p>Thank you for the hint. Probably I need some time to understand</p>

---
