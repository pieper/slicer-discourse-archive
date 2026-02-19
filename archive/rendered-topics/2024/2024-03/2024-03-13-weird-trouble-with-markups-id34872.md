---
topic_id: 34872
title: "Weird Trouble With Markups"
date: 2024-03-13
url: https://discourse.slicer.org/t/34872
---

# Weird trouble with markups

**Topic ID**: 34872
**Date**: 2024-03-13
**URL**: https://discourse.slicer.org/t/weird-trouble-with-markups/34872

---

## Post #1 by @chir.set (2024-03-13 17:32 UTC)

<p>Hello,</p>
<p>This repeatable crash is puzzling. It is seen with any markups node.</p>
<p>Go to Markups module<br>
Pick any node<br>
Place one point in a slice view<br>
Go out of place mode<br>
Move the point in the slice view<br>
Close the scene → crash.</p>
<p>It is seen in 5.6.1 stable and latest preview. All on Linux.</p>
<p>Here is a backtrace from a self-built Slicer:</p>
<pre><code class="lang-auto">Process 97542 stopped
* thread #1, name = 'SlicerApp-real', stop reason = signal SIGSEGV: address not mapped to object (fault address: 0x1b0)
    frame #0: 0x00007fffeb9690e4 libMRMLCore.so`vtkMRMLSubjectHierarchyNode::GetItemByDataNode(this=0x0000000000000000, dataNode=0x000055555d62b520) at vtkMRMLSubjectHierarchyNode.cxx:3089:41
   3086   vtkSubjectHierarchyItem* item = this-&gt;Internal-&gt;FindItemByID(itemID);
   3087   if (!item)
   3088   {
-&gt; 3089     vtkErrorMacro("GetDataNodesInBranch: Failed to find subject hierarchy item by ID " &lt;&lt; itemID);
   3090     return;
   3091   }
   3092
(lldb) bt
* thread #1, name = 'SlicerApp-real', stop reason = signal SIGSEGV: address not mapped to object (fault address: 0x1b0)
  * frame #0: 0x00007fffeb9690e4 libMRMLCore.so`vtkMRMLSubjectHierarchyNode::GetItemByDataNode(this=0x0000000000000000, dataNode=0x000055555d62b520) at vtkMRMLSubjectHierarchyNode.cxx:3089:41
    frame #1: 0x00007fff8d3e3447 libqSlicerMarkupsModule.so`qSlicerMarkupsModuleWidget::updateWidgetFromMRML(this=0x000055555ddd8770) at qSlicerMarkupsModuleWidget.cxx:972:73
    frame #2: 0x00007ffff5ec8fe3 libQt5Core.so.5`___lldb_unnamed_symbol10861 + 2435
    frame #3: 0x00007ffff61f458a libCTKVisualizationVTKCore.so.0.1`ctkVTKConnection::emitExecute(this=&lt;unavailable&gt;, _t1=0x000055555d62b520, _t2=0x0000000000000000, _t3=33, _t4=0x000055555e465170) at moc_ctkVTKConnection.cpp:167:5
    frame #4: 0x00007ffff61ec3ab libCTKVisualizationVTKCore.so.0.1`ctkVTKConnectionPrivate::execute(this=0x000055555e465170, vtk_obj=0x000055555d62b520, vtk_event=33, client_data=0x000055555e465170, call_data=0x0000000000000000) at ctkVTKConnection.cpp:414:17
    frame #5: 0x00007fffdd8acbad libvtkCommon-9.2.so.1`vtkCallbackCommand::Execute(this=0x000055555e4253a0, caller=&lt;unavailable&gt;, event=&lt;unavailable&gt;, callData=&lt;unavailable&gt;) at vtkCallbackCommand.cxx:42:5
    frame #6: 0x00007fffeb7c43f0 libMRMLCore.so`vtkEventBroker::InvokeObservation(this=0x0000555555b09fb0, observation=0x000055555e436970, eid=33, callData=0x0000000000000000) at vtkEventBroker.cxx:841:40
    frame #7: 0x00007fffeb7c3e6a libMRMLCore.so`vtkEventBroker::ProcessEvent(this=0x0000555555b09fb0, observation=0x000055555e436970, caller=0x000055555d62b520, eid=33, callData=0x0000000000000000) at vtkEventBroker.cxx:693:13
    frame #8: 0x00007fffdd8acbad libvtkCommon-9.2.so.1`vtkCallbackCommand::Execute(this=0x000055555e45fbe0, caller=&lt;unavailable&gt;, event=&lt;unavailable&gt;, callData=&lt;unavailable&gt;) at vtkCallbackCommand.cxx:42:5
    frame #9: 0x00007fffdda2442e libvtkCommon-9.2.so.1`vtkSubjectHelper::InvokeEvent(this=0x000055555e01b550, event=33, callData=0x0000000000000000, self=0x000055555d62b520) at vtkObject.cxx:650:26
    frame #10: 0x00007ffff5b26e2e libMRMLCLI.so`vtkMRMLNode::InvokePendingModifiedEvent(this=0x000055555d62b520) at vtkMRMLNode.h:551:19
    frame #11: 0x00007fff8f70388a libvtkSlicerMarkupsModuleMRML.so`vtkMRMLMarkupsNode::EndModify(int) [inlined] vtkMRMLNode::EndModify(this=0x000055555d62b520, previousDisableModifiedEventState=&lt;unavailable&gt;) at vtkMRMLNode.h:326:20
    frame #12: 0x00007fff8f703874 libvtkSlicerMarkupsModuleMRML.so`vtkMRMLMarkupsNode::EndModify(this=0x000055555d62b520, previousDisableModifiedEventState=&lt;unavailable&gt;) at vtkMRMLMarkupsNode.cxx:305:33
    frame #13: 0x00007fffeb955121 libMRMLCore.so`vtkSubjectHierarchyItem::RemoveAllChildren() [inlined] MRMLNodeModifyBlocker::~MRMLNodeModifyBlocker(this=0x00007fffffff9800) at vtkMRMLNode.h:1079:19
    frame #14: 0x00007fffeb95510a libMRMLCore.so`vtkSubjectHierarchyItem::RemoveAllChildren(this=0x000055555e0d4800) at vtkMRMLSubjectHierarchyNode.cxx:1287:1
    frame #15: 0x00007fffeb954ddb libMRMLCore.so`vtkSubjectHierarchyItem::~vtkSubjectHierarchyItem(this=&lt;unavailable&gt;) at vtkMRMLSubjectHierarchyNode.cxx:286:9
    frame #16: 0x00007fffeb9551b9 libMRMLCore.so`vtkSubjectHierarchyItem::~vtkSubjectHierarchyItem(this=&lt;unavailable&gt;) at vtkMRMLSubjectHierarchyNode.cxx:285:1
    frame #17: 0x00007fffdda969ab libvtkCommon-9.2.so.1`vtkSmartPointerBase::~vtkSmartPointerBase(this=&lt;unavailable&gt;) at vtkSmartPointerBase.cxx:61:13
    frame #18: 0x00007fffeb95cd9f libMRMLCore.so`vtkSubjectHierarchyItem::RemoveChild(this=0x00005555594d7150, itemID=&lt;unavailable&gt;) at vtkMRMLSubjectHierarchyNode.cxx:1216:1
    frame #19: 0x00007fffeb95506c libMRMLCore.so`vtkSubjectHierarchyItem::RemoveAllChildren(this=0x00005555594d7150) at vtkMRMLSubjectHierarchyNode.cxx:1280:30
    frame #20: 0x00007fffeb954ddb libMRMLCore.so`vtkSubjectHierarchyItem::~vtkSubjectHierarchyItem(this=&lt;unavailable&gt;) at vtkMRMLSubjectHierarchyNode.cxx:286:9
    frame #21: 0x00007fffeb9551b9 libMRMLCore.so`vtkSubjectHierarchyItem::~vtkSubjectHierarchyItem(this=&lt;unavailable&gt;) at vtkMRMLSubjectHierarchyNode.cxx:285:1
    frame #22: 0x00007fffeb95e7f2 libMRMLCore.so`vtkMRMLSubjectHierarchyNode::vtkInternal::~vtkInternal(this=0x00005555594d6a60) at vtkMRMLSubjectHierarchyNode.cxx:1556:22
    frame #23: 0x00007fffeb960b23 libMRMLCore.so`vtkMRMLSubjectHierarchyNode::~vtkMRMLSubjectHierarchyNode(this=0x00005555585cba20) at vtkMRMLSubjectHierarchyNode.cxx:1843:3
    frame #24: 0x00007fffeb960b69 libMRMLCore.so`vtkMRMLSubjectHierarchyNode::~vtkMRMLSubjectHierarchyNode(this=&lt;unavailable&gt;) at vtkMRMLSubjectHierarchyNode.cxx:1839:1
    frame #25: 0x00007fffeb8b050b libMRMLCore.so`vtkMRMLScene::RemoveNode(this=0x0000555555d0efd0, n=0x00005555585cba20) at vtkMRMLScene.cxx:1561:6
    frame #26: 0x00007fffeb8af884 libMRMLCore.so`vtkMRMLScene::RemoveAllNodes(this=0x0000555555d0efd0, removeSingletons=&lt;unavailable&gt;) at vtkMRMLScene.cxx:376:13
    frame #27: 0x00007fffeb8af158 libMRMLCore.so`vtkMRMLScene::Clear(this=0x0000555555d0efd0, removeSingletons=0) at vtkMRMLScene.cxx:320:9
    frame #28: 0x00007ffff7ef50f3 libqSlicerBaseQTApp.so`qSlicerMainWindow::on_FileCloseSceneAction_triggered(this=&lt;unavailable&gt;) at qSlicerMainWindow.cxx:1043:57
    frame #29: 0x00007ffff7f05ef7 libqSlicerBaseQTApp.so`qSlicerMainWindow::qt_metacall(this=0x00005555586dd4c0, _c=InvokeMetaMethod, _id=15, _a=0x00007fffffff9da0) at moc_qSlicerMainWindow.cpp:454:13
    frame #30: 0x00007ffff7f29444 libqSlicerApp.so`qSlicerAppMainWindow::qt_metacall(this=&lt;unavailable&gt;, _c=&lt;unavailable&gt;, _id=&lt;unavailable&gt;, _a=&lt;unavailable&gt;) at moc_qSlicerAppMainWindow.cpp:175:30
    frame #31: 0x00007ffff5ec8a5f libQt5Core.so.5`___lldb_unnamed_symbol10861 + 1023
    frame #32: 0x00007ffff6b4abb7 libQt5Widgets.so.5`QAction::triggered(bool) + 71
... ...
</code></pre>
<p>Can this be confirmed? The whole observation is very odd.</p>
<p>Thank you.</p>

---

## Post #2 by @Sunderlandkyl (2024-03-13 17:44 UTC)

<p>I can confirm that this also happens on Windows.</p>
<p>Looks like it’s caused by this line, which doesn’t check to see if the subject hierarchy node exists before accessing it: <a href="https://github.com/Slicer/Slicer/blob/024b340baaa191968b6fc954b9f0e548adb40d6d/Modules/Loadable/Markups/qSlicerMarkupsModuleWidget.cxx#L972" class="inline-onebox" rel="noopener nofollow ugc">Slicer/Modules/Loadable/Markups/qSlicerMarkupsModuleWidget.cxx at 024b340baaa191968b6fc954b9f0e548adb40d6d · Slicer/Slicer · GitHub</a>.</p>
<p>I’ll submit a fix.</p>

---

## Post #3 by @Sunderlandkyl (2024-03-13 17:51 UTC)

<p>PR created here: <a href="https://github.com/Slicer/Slicer/pull/7628" class="inline-onebox" rel="noopener nofollow ugc">BUG: Fix crash in Markups widget when closing scene by Sunderlandkyl · Pull Request #7628 · Slicer/Slicer · GitHub</a>.</p>

---

## Post #4 by @Sunderlandkyl (2024-03-14 17:08 UTC)

<p>Fix was integrated in <a href="https://github.com/Slicer/Slicer/commit/7a31ad9b0586784d5682a8703250067d0eb56865" class="inline-onebox" rel="noopener nofollow ugc">BUG: Fix crash in Markups widget when closing scene · Slicer/Slicer@7a31ad9 · GitHub</a>.</p>

---

## Post #5 by @chir.set (2024-03-14 17:15 UTC)

<p>Great, thanks. Quite a fast fix.</p>

---
