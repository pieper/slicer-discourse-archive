---
topic_id: 34675
title: "Markups Plane Placement Process Is Confusing"
date: 2024-03-03
url: https://discourse.slicer.org/t/34675
---

# Markups plane: placement process is confusing

**Topic ID**: 34675
**Date**: 2024-03-03
**URL**: https://discourse.slicer.org/t/markups-plane-placement-process-is-confusing/34675

---

## Post #1 by @chir.set (2024-03-03 18:42 UTC)

<p>I’m using 5.7.0-2024-02-29 r32739 / c7fe865 from your repository on Linux. When placing a markups plane, the mouse cursor remains in placement mode. Clicking in a slice view creates a second plane and releases the mouse cursor. Deleting the second node (P_1) in the Markups module crashes Slicer. It is seen in self-built too.</p>
<p>It happens in my previous build also: 5.7.0-2024-02-16 r32720 / 9c49644.</p>
<p>It happens in 5.6.1 with a slight difference: removing P_1 does not crash Slicer.</p>
<p>All these in new empty scenes just after startup.</p>
<p>We can reasonably expect that P_1 never gets created once P is on screen, there’s only one single point.</p>
<p>FYI.</p>
<p>Regards.</p>

---

## Post #2 by @chir.set (2024-03-03 19:50 UTC)

<p>It could be related to <a href="https://projectweek.na-mic.org/PW39_2023_Montreal/Projects/UndoRedo/" rel="noopener nofollow ugc">Undo/Redo</a> in .slicerrc.py.</p>
<p>After excluding vtkMRMLMarkupsPlaneNode for Undo/Redo, placing a new plane node behaves as expected.</p>
<p>Here is a backtrace of the crash.</p>
<pre><code class="lang-auto">Process 7260 stopped
* thread #1, name = 'SlicerApp-real', stop reason = signal SIGSEGV: invalid address (fault address: 0x0)
    frame #0: 0x00007fff8d5e726e libvtkSlicerMarkupsModuleVTKWidgets.so`vtkSlicerMarkupsInteractionWidgetRepresentation::UpdateHandleToWorldTransform(this=0x000055555f01cf20, handleToWorldTransform=0x000055555f123d30) at vtkSlicerMarkupsInteractionWidgetRepresentation.cxx:562:63
   559  void vtkSlicerMarkupsInteractionWidgetRepresentation::UpdateHandleToWorldTransform(vtkTransform* handleToWorldTransform)
   560  {
   561    handleToWorldTransform-&gt;Identity();
-&gt; 562    handleToWorldTransform-&gt;Concatenate(this-&gt;GetMarkupsNode()-&gt;GetInteractionHandleToWorldMatrix());
   563  }
   564 
   565  //----------------------------------------------------------------------
(lldb) bt
* thread #1, name = 'SlicerApp-real', stop reason = signal SIGSEGV: invalid address (fault address: 0x0)
  * frame #0: 0x00007fff8d5e726e libvtkSlicerMarkupsModuleVTKWidgets.so`vtkSlicerMarkupsInteractionWidgetRepresentation::UpdateHandleToWorldTransform(this=0x000055555f01cf20, handleToWorldTransform=0x000055555f123d30) at vtkSlicerMarkupsInteractionWidgetRepresentation.cxx:562:63
    frame #1: 0x00007ffff5bb3cf2 libMRMLDisplayableManager.so`vtkMRMLInteractionWidgetRepresentation::UpdateHandleToWorldTransform(this=0x000055555f01cf20) at vtkMRMLInteractionWidgetRepresentation.cxx:469:9
    frame #2: 0x00007ffff5bb5565 libMRMLDisplayableManager.so`vtkMRMLInteractionWidgetRepresentation::RenderOpaqueGeometry(this=0x000055555f01cf20, viewport=0x0000555557f2d4b0) at vtkMRMLInteractionWidgetRepresentation.cxx:731:11
    frame #3: 0x00007fffe0f90d87 libvtkRendering-9.2.so.1`vtkRenderer::UpdateOpaquePolygonalGeometry(this=0x0000555557f2d4b0) at vtkRenderer.cxx:744:35
    frame #4: 0x00007fffe37c19c3 libvtkOpenGL-9.2.so.1`vtkOpenGLRenderer::UpdateGeometry(this=0x0000555557f2d4b0, fbo=0x0000000000000000) at vtkOpenGLRenderer.cxx:394:11
    frame #5: 0x00007fffe37c12c5 libvtkOpenGL-9.2.so.1`vtkOpenGLRenderer::DeviceRender(this=0x0000555557f2d4b0) at vtkOpenGLRenderer.cxx:299:11
    frame #6: 0x00007fffe0f8fb4b libvtkRendering-9.2.so.1`vtkRenderer::Render(this=0x0000555557f2d4b0) at vtkRenderer.cxx:385:9
    frame #7: 0x00007fffe0f97840 libvtkRendering-9.2.so.1`vtkRendererCollection::Render(this=0x00005555599a6e70) at vtkRendererCollection.cxx:52:14
    frame #8: 0x00007fffe0f8736e libvtkRendering-9.2.so.1`vtkRenderWindow::DoStereoRender(this=0x00005555599a6470) at vtkRenderWindow.cxx:356:22
    frame #9: 0x00007fffe0f87208 libvtkRendering-9.2.so.1`vtkRenderWindow::Render(this=0x00005555599a6470) at vtkRenderWindow.cxx:316:9
    frame #10: 0x00007fffe37c00a1 libvtkOpenGL-9.2.so.1`vtkOpenGLRenderWindow::Render(this=0x00005555599a6470) at vtkOpenGLRenderWindow.cxx:2781:21
    frame #11: 0x00007fffe3746ed8 libvtkOpenGL-9.2.so.1`vtkGenericOpenGLRenderWindow::Render(this=0x00005555599a6470) at vtkGenericOpenGLRenderWindow.cxx:220:25
    frame #12: 0x00007ffff5ec8fe3 libQt5Core.so.5`___lldb_unnamed_symbol10861 + 2435
    frame #13: 0x00007ffff61f457a libCTKVisualizationVTKCore.so.0.1`ctkVTKConnection::emitExecute(this=&lt;unavailable&gt;, _t1=&lt;unavailable&gt;, _t2=&lt;unavailable&gt;, _t3=&lt;unavailable&gt;, _t4=&lt;unavailable&gt;) at moc_ctkVTKConnection.cpp:167:5
    frame #14: 0x00007ffff61ec39b libCTKVisualizationVTKCore.so.0.1`ctkVTKConnectionPrivate::execute(this=0x0000555559bce9b0, vtk_obj=0x0000555559b68000, vtk_event=74, client_data=0x0000555559bce9b0, call_data=0x0000000000000000) at ctkVTKConnection.cpp:414:17
    frame #15: 0x00007fffddaa7bfd libvtkCommon-9.2.so.1`vtkCallbackCommand::Execute(this=0x0000555559bd2010, caller=&lt;unavailable&gt;, event=&lt;unavailable&gt;, callData=&lt;unavailable&gt;) at vtkCallbackCommand.cxx:42:5
    frame #16: 0x00007fffeb7c4280 libMRMLCore.so`vtkEventBroker::InvokeObservation(this=0x0000555555b09fb0, observation=0x0000555559bd36d0, eid=74, callData=0x0000000000000000) at vtkEventBroker.cxx:841:40
    frame #17: 0x00007fffeb7c3cfa libMRMLCore.so`vtkEventBroker::ProcessEvent(this=0x0000555555b09fb0, observation=0x0000555559bd36d0, caller=0x0000555559b68000, eid=74, callData=0x0000000000000000) at vtkEventBroker.cxx:693:13
    frame #18: 0x00007fffddaa7bfd libvtkCommon-9.2.so.1`vtkCallbackCommand::Execute(this=0x0000555559bcf300, caller=&lt;unavailable&gt;, event=&lt;unavailable&gt;, callData=&lt;unavailable&gt;) at vtkCallbackCommand.cxx:42:5
    frame #19: 0x00007fffddc1eb50 libvtkCommon-9.2.so.1`vtkSubjectHelper::InvokeEvent(this=0x0000555559bd1fc0, event=74, callData=0x0000000000000000, self=0x0000555559b68000) at vtkObject.cxx:650:26
    frame #20: 0x00007fffed4c1c0c libMRMLLogic.so`vtkMRMLAbstractLogic::MRMLSceneCallback(caller=0x0000555555fc83b0, eid=8195, clientData=0x0000555559b509a0, callData=0x000055555d93c9a0) at vtkMRMLAbstractLogic.cxx:172:9
    frame #21: 0x00007fffddaa7bfd libvtkCommon-9.2.so.1`vtkCallbackCommand::Execute(this=0x0000555559a73ad0, caller=&lt;unavailable&gt;, event=&lt;unavailable&gt;, callData=&lt;unavailable&gt;) at vtkCallbackCommand.cxx:42:5
    frame #22: 0x00007fffeb7c4280 libMRMLCore.so`vtkEventBroker::InvokeObservation(this=0x0000555555b09fb0, observation=0x0000555559bff820, eid=8195, callData=0x000055555d93c9a0) at vtkEventBroker.cxx:841:40
    frame #23: 0x00007fffeb7c3cfa libMRMLCore.so`vtkEventBroker::ProcessEvent(this=0x0000555555b09fb0, observation=0x0000555559bff820, caller=0x0000555555fc83b0, eid=8195, callData=0x000055555d93c9a0) at vtkEventBroker.cxx:693:13
    frame #24: 0x00007fffddaa7bfd libvtkCommon-9.2.so.1`vtkCallbackCommand::Execute(this=0x0000555559bffba0, caller=&lt;unavailable&gt;, event=&lt;unavailable&gt;, callData=&lt;unavailable&gt;) at vtkCallbackCommand.cxx:42:5
    frame #25: 0x00007fffddc1eb50 libvtkCommon-9.2.so.1`vtkSubjectHelper::InvokeEvent(this=0x00005555560b6310, event=8195, callData=0x000055555d93c9a0, self=0x0000555555fc83b0) at vtkObject.cxx:650:26
    frame #26: 0x00007fffeb8b02a7 libMRMLCore.so`vtkMRMLScene::RemoveNode(this=0x0000555555fc83b0, n=0x000055555d93c9a0) at vtkMRMLScene.cxx:1523:9
    frame #27: 0x00007fffeb9684e2 libMRMLCore.so`vtkMRMLSubjectHierarchyNode::RemoveItem(this=0x000055555887b5e0, itemID=16, removeDataNode=true, recursive=&lt;unavailable&gt;) at vtkMRMLSubjectHierarchyNode.cxx:2713:18
    frame #28: 0x00007fff98193af8 libqSlicerSubjectHierarchyModuleWidgets.so`qMRMLSubjectHierarchyTreeView::deleteSelectedItems(this=&lt;unavailable&gt;) at qMRMLSubjectHierarchyTreeView.cxx:2064:35
    frame #29: 0x00007ffff5ec8fe3 libQt5Core.so.5`___lldb_unnamed_symbol10861 + 2435
    frame #30: 0x00007ffff6b4abb7 libQt5Widgets.so.5`QAction::triggered(bool) + 71
    frame #31: 0x00007ffff6b5060b libQt5Widgets.so.5`QAction::activate(QAction::ActionEvent) + 187
...
...
</code></pre>

---
