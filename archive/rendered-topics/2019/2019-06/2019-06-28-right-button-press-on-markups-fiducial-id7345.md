---
topic_id: 7345
title: "Right Button Press On Markups Fiducial"
date: 2019-06-28
url: https://discourse.slicer.org/t/7345
---

# Right Button Press on Markups Fiducial

**Topic ID**: 7345
**Date**: 2019-06-28
**URL**: https://discourse.slicer.org/t/right-button-press-on-markups-fiducial/7345

---

## Post #1 by @zacbaum (2019-06-28 02:39 UTC)

<p>Hello,</p>
<p>I am looking to implement a context menu similar to <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Show_a_context_menu_when_a_markup_point_is_clicked_in_a_slice_or_3D_view" rel="nofollow noopener">this</a> one from the script repository - however, I’d like to be able to use a right click instead of a left click with the mouse.</p>
<p>I know that I can do something like the below to create a menu when I right click, but this allows the menu to pop up even if a markup fiducial is not clicked, and doesn’t allow me to pass the fiducial ID through the callData to update the menu accordingly.</p>
<pre><code>layoutManager = slicer.app.layoutManager()
redRenderWindow = layoutManager.sliceWidget('Red').sliceView().renderWindow()
style = vtk.vtkInteractorStyleUser()
redRenderWindow.GetInteractor().SetInteractorStyle(style)
style.AddObserver(vtk.vtkCallbackCommand.RightButtonPressEvent, self.analysisWidget.markupCallback)</code></pre>

---

## Post #2 by @lassoan (2019-06-28 23:15 UTC)

<p>Markups are completely reworked in recent 4.11 versions. In these versions you can easily change/add mapping of right-click to an arbitrary markup node event (that you can observe from your module). This is not exposed on any external API though, so you need to <a href="https://github.com/Slicer/Slicer/blob/52a4c6c97b7b4589f4c2c79e306786bdf5bfbb21/Modules/Loadable/Markups/VTKWidgets/vtkSlicerMarkupsWidget.cxx#L56" rel="nofollow noopener">change the source code</a> of Slicer and rebuild.</p>

---
