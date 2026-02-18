# Rendering Text in VR mode

**Topic ID**: 16343
**Date**: 2021-03-03
**URL**: https://discourse.slicer.org/t/rendering-text-in-vr-mode/16343

---

## Post #1 by @Raj_Kumar_Ranabhat (2021-03-03 20:21 UTC)

<p>Is it possible to render a  scripted text or message in Virtual Reality Environment in addition with Rendered label map Model ?</p>

---

## Post #2 by @lassoan (2021-03-04 01:44 UTC)

<p>Markups would be the most convenient way of displaying labels, but they use 2D text actors, which I think are rendered with ghosting. However, there are many 3D text actors that you can add to the scene, for example:</p>
<pre><code class="lang-python">viewIndex = 0
label = vtk.vtkFlagpoleLabel()
label.SetInput("My label")
renderWindow = slicer.app.layoutManager().threeDWidget(viewIndex).threeDView().renderWindow()
renderer = renderWindow.GetRenderers().GetFirstRenderer()
renderer.AddActor(label)
renderer.Render()
</code></pre>
<p>You need to replace <code>viewIndex</code> with the index of the virtual reality view.</p>

---

## Post #3 by @Raj_Kumar_Ranabhat (2021-03-05 18:30 UTC)

<p>thank you Andras, I am getting this error while trying to use  vtk.FlagpoleLabel(). Do I need to import any other library beside vtk to work it out ?</p>
<p>vtk.vtkFlagpoleLabel()</p>
<p>Traceback (most recent call last):</p>
<p>File “”, line 1, in </p>
<p>AttributeError: module ‘vtkmodules.all’ has no attribute ‘vtkFlagpoleLabel’</p>
<p>Using slicer 4.11.0</p>
<p>Thank you !!</p>

---

## Post #4 by @lassoan (2021-03-05 18:33 UTC)

<p>vtkFlagpoleLabel has been added to VTK recently, so it is only available in Slicer Preview Releases (VTK9), but there are other similar 3D text actors in VTK8 that you can use in Slicer-4.11.</p>

---
