---
topic_id: 19325
title: "Crash When Using Vtkqwidgetwidget With Slicer Built Against"
date: 2021-08-23
url: https://discourse.slicer.org/t/19325
---

# Crash when using vtkQWidgetWidget with Slicer built against VTK9

**Topic ID**: 19325
**Date**: 2021-08-23
**URL**: https://discourse.slicer.org/t/crash-when-using-vtkqwidgetwidget-with-slicer-built-against-vtk9/19325

---

## Post #1 by @cpinter (2021-08-23 16:43 UTC)

<p>Hi all,</p>
<p>Despite the expectations about all the fixes done in VTK since the version Slicer used to be stuck on, unfortunately it seems that vtkQWidgetWidget cannot be used with Slicer built against VTK9.</p>
<p>First I tried the code that worked “more or less” (i.e. the Qt widget appeared in the VTK renderer, although there were rendering issues and it crashed when the widget was created on the heap instead of the stack) - it can be found in <a href="https://github.com/cpinter/SlicerVirtualReality/blob/virtual-widget-2/VirtualReality/Widgets/qMRMLVirtualRealityView.cxx#L873-L917">this SlicerVR branch</a>.</p>
<p>Then I wanted to get rid of the complications to see what was going on and created <a href="https://github.com/cpinter/VtkQWidgetTest">this minimal Slicer extension</a> that has one module exposing one button which is reproducing <a href="https://gitlab.kitware.com/vtk/vtk/-/blob/master/GUISupport/Qt/Testing/Cxx/TestQWidgetWidget.cxx">the VTK test</a>.</p>
<p>It crashes when enabling the QWidgetWidget, in the nvoglv64.dll module. In the main thread the call stack varies, but it is sometimes at the destruction of the widget (i.e. it reaches the end of the <code>addHelloWorldClicked</code> function), but many times in <code>vtkOpenGLFramebufferObject::Blit</code>, within <code>process_events_and_wait</code>.</p>
<p>This widget seems to work in VTK and in Paraview. Am I doing something wrong with how I use it? Any suggestions about what to try to get it working? Thank you very much!</p>

---

## Post #2 by @pieper (2021-08-23 18:53 UTC)

<p><a href="https://github.com/cpinter/VtkQWidgetTest/blob/52b7f80d263f7cfb19cae76eea07ce38fd8bffd0/VtkQWidgetTest/qSlicerVtkQWidgetTestModuleWidget.cxx#L179-L195">This call <code>process_events_and_wait</code></a> looks like a red flag to me, since processing events could trigger a render or other changes to the qt or opengl state.  Is that being used in ParaView?  Maybe it’s okay in the vtk testing code since there are no other events going on, but usual Qt style would be have everything be event driven.</p>

---

## Post #3 by @lassoan (2021-08-23 20:14 UTC)

<p>I agree that we should not pump the event loop by calling <code>process_events_and_wait</code>, but it should be done by the application as usual.</p>
<p>I would add that as far as I remember, ParaView’s implementation did not allow simultaneous virtual reality+desktop experience (at least this was the first implementation that I tried several years ago), but if you start virtual reality mode then the desktop application GUI is blocked. So, Slicer might encounter some issues that ParaView does not.</p>
<p>I had a look at the vtkQWidgetWidget implementation and it uses the same messy state and event design as other VTK core widgets, so we will need to have our own modified clone of the widget and representation in Slicer. As a first step, you could test just porting the representation and place it in the renderer (it is just an actor) and see if it works. If it does then we know that the crash is most likely due to the message handling.</p>

---

## Post #4 by @cpinter (2021-08-24 09:17 UTC)

<p>Thanks for the answers!</p>
<p>Process events: Of course I tried first without this (see the SlicerVR branch linked in the post above), and the application crashes if I just add the widget without any force update. I only used the VTK testing code to demonstrate that the same thing that they use in VTK to test the widget with crases in Slicer environment.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> By porting the representation do you mean migrating the widget from VTK to the widget-representation mechanism used lately in Slicer?</p>

---

## Post #5 by @lassoan (2021-08-24 12:45 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="4" data-topic="19325">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>By porting the representation do you mean migrating the widget from VTK to the widget-representation mechanism used lately in Slicer?</p>
</blockquote>
</aside>
<p>Yes, at least change the base class to vtkMRMLAbstractWidgetRepresentation and implement basic functions, such as update from MRML (e.g., control show/hide by observing the corresponding node).</p>

---

## Post #6 by @cpinter (2021-08-31 15:43 UTC)

<p>I started porting to the Slicer VTK widget infrastructure. I made some commits in the <a href="https://github.com/cpinter/VtkQWidgetTest">minimum working example extension</a> with my intermediate results. The second button in the module UI (in Examples category) adds the widget to the 3D view as a quick test.</p>
<p>The example does not work currently with the texture applied. After commenting out <a href="https://github.com/cpinter/VtkQWidgetTest/blob/master/VtkQWidgetTest/VTKWidgets/vtkSlicerQWidgetRepresentation.cxx#L61">this line</a> the widget shows up as a white plane, but uncommenting the line causes the widget to not appear, or show fully transparent, not sure. <a class="mention" href="/u/lassoan">@lassoan</a> do you have any ide why the texture does not work? I can continue working on this early next week. Thank you!</p>

---
