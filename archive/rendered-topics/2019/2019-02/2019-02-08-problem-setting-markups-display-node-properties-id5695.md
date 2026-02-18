# Problem setting markups display node properties

**Topic ID**: 5695
**Date**: 2019-02-08
**URL**: https://discourse.slicer.org/t/problem-setting-markups-display-node-properties/5695

---

## Post #1 by @smrolfe (2019-02-08 16:48 UTC)

<p>Hello,<br>
Slicer is crashing when I try to modify markups display node properties from a python module. I can modify these properties using the python interactor without a problem. When I try any modification of the markups display node from my module, Slicer crashes with the error report:</p>
<p>Exception Type:        EXC_BAD_ACCESS (SIGSEGV)<br>
Exception Codes:       KERN_INVALID_ADDRESS at 0x0000000000000068<br>
Exception Note:        EXC_CORPSE_NOTIFY</p>
<p>I generated a simplified module and scene with landmarks to replicate this error. With the sample data loaded, the combo box is used to select a markups node. The select button should get the display node and set the option to project landmarks on the slice views. I’ve tried this on the nightly and stable versions of Slicer. Any insight would be very helpful.</p>
<p>Sample data:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerMorph/SampleData/blob/master/gorilla_reference.mrb">
  <header class="source">

      <a href="https://github.com/SlicerMorph/SampleData/blob/master/gorilla_reference.mrb" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerMorph/SampleData/blob/master/gorilla_reference.mrb" target="_blank" rel="noopener nofollow ugc">SlicerMorph/SampleData/blob/master/gorilla_reference.mrb</a></h4>


  This file is binary. <a href="https://github.com/SlicerMorph/SampleData/blob/master/gorilla_reference.mrb" target="_blank" rel="noopener nofollow ugc">show original</a>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Module:<br>
<a href="https://github.com/smrolfe/TestSlicer/tree/master/TestLMDisplay" class="onebox" target="_blank" rel="noopener nofollow ugc">https://github.com/smrolfe/TestSlicer/tree/master/TestLMDisplay</a></p>

---

## Post #2 by @pieper (2019-02-08 20:21 UTC)

<p>Thanks for reporting this <a class="mention" href="/u/smrolfe">@smrolfe</a>, and for providing the method to reproduce <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=6" title=":+1:" class="emoji" alt=":+1:"></p>
<p>I took a look at this in the debugger and there is some corruption of the projected seed widget’s polydata that causes a null pointer during rendering (stack trace below).  Oddly, it happens on the seed 21 out of 41.  If I edit your fcsv file to make it shorter the crash doesn’t happen.  The behavior seems to be the same either using your test module or the ‘eye’ icon in the Markups module, which makes sense because the are calling the same set method.</p>
<p>I’m tempted to keep digging, but I’m also thinking anything we do to fix this will be obsolete shortly when the <a href="https://github.com/Slicer/Slicer/pull/1079#issuecomment-459694142" rel="nofollow noopener">new fiducial infrastructure</a> is merged.  What do you and <a class="mention" href="/u/muratmaga">@muratmaga</a> think?</p>
<p>-Steve</p>
<pre><code class="lang-auto">
Thread 0 Crashed:: Dispatch queue: com.apple.main-thread
0   libvtkFilters-8.2.1.dylib     	0x000000011cd9c493 vtkGlyph2D::RequestData(vtkInformation*, vtkInformationVector**, vtkInformationVector*) + 2979 (vtkPoints.h:126)
1   libvtkCommon-8.2.1.dylib      	0x000000011e355515 vtkExecutive::CallAlgorithm(vtkInformation*, int, vtkInformationVector**, vtkInformationVector*) + 69 (vtkExecutive.cxx:773)
2   libvtkCommon-8.2.1.dylib      	0x000000011e35031d vtkDemandDrivenPipeline::ExecuteData(vtkInformation*, vtkInformationVector**, vtkInformationVector*) + 61 (vtkDemandDrivenPipeline.cxx:490)
3   libvtkCommon-8.2.1.dylib      	0x000000011e34af7b vtkCompositeDataPipeline::ExecuteData(vtkInformation*, vtkInformationVector**, vtkInformationVector*) + 107
4   libvtkCommon-8.2.1.dylib      	0x000000011e34fab7 vtkDemandDrivenPipeline::ProcessRequest(vtkInformation*, vtkInformationVector**, vtkInformationVector*) + 1175 (vtkDemandDrivenPipeline.cxx:273)
5   libvtkCommon-8.2.1.dylib      	0x000000011e374572 vtkStreamingDemandDrivenPipeline::ProcessRequest(vtkInformation*, vtkInformationVector**, vtkInformationVector*) + 706 (vtkStreamingDemandDrivenPipeline.cxx:351)
6   libvtkCommon-8.2.1.dylib      	0x000000011e374acb vtkStreamingDemandDrivenPipeline::Update(int, vtkInformationVector*) + 283 (vtkStreamingDemandDrivenPipeline.cxx:429)
7   libvtkOpenGL-8.2.1.dylib      	0x000000011a623d3f vtkOpenGLPolyDataMapper2D::RenderOverlay(vtkViewport*, vtkActor2D*) + 63 (vtkOpenGLPolyDataMapper2D.cxx:755)
8   libvtkRendering-8.2.1.dylib   	0x000000011b1d3695 vtkActor2D::RenderOverlay(vtkViewport*) + 229 (vtkActor2D.cxx:123)
9   libvtkOpenGL-8.2.1.dylib      	0x000000011a634f97 vtkOpenGLRenderer::UpdateGeometry() + 1911 (vtkOpenGLRenderer.cxx:379)
10  libvtkOpenGL-8.2.1.dylib      	0x000000011a6347f2 vtkOpenGLRenderer::DeviceRender() + 178 (vtkOpenGLRenderer.cxx:239)
11  libvtkRendering-8.2.1.dylib   	0x000000011b25b504 vtkRenderer::Render() + 1236
12  libvtkRendering-8.2.1.dylib   	0x000000011b25a4db vtkRendererCollection::Render() + 139 (vtkCollection.h:193)
13  libvtkRendering-8.2.1.dylib   	0x000000011b264dfc vtkRenderWindow::DoStereoRender() + 140 (vtkRenderWindow.cxx:333)
14  libvtkRendering-8.2.1.dylib   	0x000000011b264cb9 vtkRenderWindow::Render() + 377 (vtkRenderWindow.cxx:292)
15  libvtkOpenGL-8.2.1.dylib      	0x000000011a63397e vtkOpenGLRenderWindow::Render() + 14 (vtkOpenGLRenderWindow.cxx:2564)
16  libvtkOpenGL-8.2.1.dylib      	0x000000011a5cf942 vtkGenericOpenGLRenderWindow::Render() + 34 (vtkGenericOpenGLRenderWindow.cxx:245)
17  org.qt-project.QtCore         	0x000000011a1d810c QMetaObject::activate(QObject*, int, int, void**) + 3132
18  libCTKVisualizationVTKCore.0.1.dylib	0x0000000110b968d3 ctkVTKConnection::emitExecute(vtkObject*, void*, unsigned long, void*) + 99
19  libCTKVisualizationVTKCore.0.1.dylib	0x0000000110b8fa03 ctkVTKConnectionPrivate::execute(vtkObject*, unsigned long, void*, void*) + 611
20  libvtkCommon-8.2.1.dylib      	0x000000011de75051 vtkCallbackCommand::Execute(vtkObject*, unsigned long, void*) + 33 (vtkCallbackCommand.cxx:43)
21  libMRMLCore.dylib             	0x0000000114bffe18 vtkEventBroker::InvokeObservation(vtkObservation*, unsigned long, void*) + 168 (vtkEventBroker.cxx:841)
22  libMRMLCore.dylib             	0x0000000114bff910 vtkEventBroker::ProcessEvent(vtkObservation*, vtkObject*, unsigned long, void*) + 144 (vtkEventBroker.cxx:706)
23  libvtkCommon-8.2.1.dylib      	0x000000011de75051 vtkCallbackCommand::Execute(vtkObject*, unsigned long, void*) + 33 (vtkCallbackCommand.cxx:43)
24  libvtkCommon-8.2.1.dylib      	0x000000011dfcf0ec vtkSubjectHelper::InvokeEvent(unsigned long, void*, vtkObject*) + 988 (vtkObject.cxx:619)
25  libvtkSlicerMarkupsModuleMRMLDisplayableManager.dylib	0x000000012c5f0619 vtkMRMLMarkupsFiducialDisplayableManager2D::SetNthSeed(int, vtkMRMLMarkupsFiducialNode*, vtkSeedWidget*) + 4313 (vtkMRMLMarkupsFiducialDisplayableManager2D.cxx:825)
26  libvtkSlicerMarkupsModuleMRMLDisplayableManager.dylib	0x000000012c5f1560 vtkMRMLMarkupsFiducialDisplayableManager2D::PropagateMRMLToWidget(vtkMRMLMarkupsNode*, vtkAbstractWidget*) + 1968 (vtkMRMLMarkupsFiducialDisplayableManager2D.cxx:1113)
27  libvtkSlicerMarkupsModuleMRMLDisplayableManager.dylib	0x000000012c5e7dbf vtkMRMLMarkupsDisplayableManager2D::OnMRMLMarkupsDisplayNodeModifiedEvent(vtkMRMLNode*) + 111 (vtkMRMLMarkupsDisplayableManager2D.cxx:596)
28  libMRMLLogic.dylib            	0x0000000110707e58 vtkMRMLAbstractLogic::MRMLNodesCallback(vtkObject*, unsigned long, void*, void*) + 72 (vtkMRMLAbstractLogic.cxx:403)
29  libvtkCommon-8.2.1.dylib      	0x000000011de75051 vtkCallbackCommand::Execute(vtkObject*, unsigned long, void*) + 33 (vtkCallbackCommand.cxx:43)
30  libMRMLCore.dylib             	0x0000000114bffe18 vtkEventBroker::InvokeObservation(vtkObservation*, unsigned long, void*) + 168 (vtkEventBroker.cxx:841)
31  libMRMLCore.dylib             	0x0000000114bff910 vtkEventBroker::ProcessEvent(vtkObservation*, vtkObject*, unsigned long, void*) + 144 (vtkEventBroker.cxx:706)
32  libvtkCommon-8.2.1.dylib      	0x000000011de75051 vtkCallbackCommand::Execute(vtkObject*, unsigned long, void*) + 33 (vtkCallbackCommand.cxx:43)
33  libvtkCommon-8.2.1.dylib      	0x000000011dfcf0ec vtkSubjectHelper::InvokeEvent(unsigned long, void*, vtkObject*) + 988 (vtkObject.cxx:619)
34  libMRMLCore.dylib             	0x0000000114c47b12 vtkMRMLDisplayableNode::ProcessMRMLEvents(vtkObject*, unsigned long, void*) + 210 (vtkMRMLDisplayableNode.cxx:221)
35  libMRMLCore.dylib             	0x0000000114cc4328 vtkMRMLNode::MRMLCallback(vtkObject*, unsigned long, void*, void*) + 72 (vtkMRMLNode.h:332)
36  libvtkCommon-8.2.1.dylib      	0x000000011de75051 vtkCallbackCommand::Execute(vtkObject*, unsigned long, void*) + 33 (vtkCallbackCommand.cxx:43)
37  libMRMLCore.dylib             	0x0000000114bffe18 vtkEventBroker::InvokeObservation(vtkObservation*, unsigned long, void*) + 168 (vtkEventBroker.cxx:841)
38  libMRMLCore.dylib             	0x0000000114bff910 vtkEventBroker::ProcessEvent(vtkObservation*, vtkObject*, unsigned long, void*) + 144 (vtkEventBroker.cxx:706)
39  libvtkCommon-8.2.1.dylib      	0x000000011de75051 vtkCallbackCommand::Execute(vtkObject*, unsigned long, void*) + 33 (vtkCallbackCommand.cxx:43)
40  libvtkCommon-8.2.1.dylib      	0x000000011dfcf0ec vtkSubjectHelper::InvokeEvent(unsigned long, void*, vtkObject*) + 988 (vtkObject.cxx:619)
41  org.qt-project.QtCore         	0x000000011a1d810c QMetaObject::activate(QObject*, int, int, void**) + 3132
42  org.qt-project.QtWidgets      	0x00000001195d8d1a 0x1194df000 + 1023258
43  org.qt-project.QtWidgets      	0x00000001195d8132 QAbstractButton::setChecked(bool) + 242
44  org.qt-project.QtWidgets      	0x00000001195e7da5 QCheckBox::nextCheckState() + 53
45  org.qt-project.QtWidgets      	0x00000001195d8913 0x1194df000 + 1022227
46  org.qt-project.QtWidgets      	0x00000001195d9a9f QAbstractButton::mouseReleaseEvent(QMouseEvent*) + 271
47  org.qt-project.QtWidgets      	0x000000011952a9ed QWidget::event(QEvent*) + 445
48  org.qt-project.QtWidgets      	0x00000001194eef7d QApplicationPrivate::notify_helper(QObject*, QEvent*) + 269
49  org.qt-project.QtWidgets      	0x00000001194f1dd8 QApplication::notify(QObject*, QEvent*) + 7336
50  libqSlicerBaseQTGUI.dylib     	0x0000000107f4175e qSlicerApplication::notify(QObject*, QEvent*) + 14 (qSlicerApplication.cxx:412)
51  org.qt-project.QtCore         	0x000000011a1a6fb4 QCoreApplication::notifyInternal2(QObject*, QEvent*) + 212
52  org.qt-project.QtWidgets      	0x00000001194ef8a0 QApplicationPrivate::sendMouseEvent(QWidget*, QMouseEvent*, QWidget*, QWidget*, QWidget**, QPointer&lt;QWidget&gt;&amp;, bool, bool) + 896
53  org.qt-project.QtWidgets      	0x000000011954a35e 0x1194df000 + 439134
54  org.qt-project.QtWidgets      	0x0000000119548cb5 0x1194df000 + 433333
55  org.qt-project.QtWidgets      	0x00000001194eef7d QApplicationPrivate::notify_helper(QObject*, QEvent*) + 269
56  org.qt-project.QtWidgets      	0x00000001194f0382 QApplication::notify(QObject*, QEvent*) + 594
57  libqSlicerBaseQTGUI.dylib     	0x0000000107f4175e qSlicerApplication::notify(QObject*, QEvent*) + 14 (qSlicerApplication.cxx:412)
58  org.qt-project.QtCore         	0x000000011a1a6fb4 QCoreApplication::notifyInternal2(QObject*, QEvent*) + 212
59  org.qt-project.QtGui          	0x0000000119ab1c7c QGuiApplicationPrivate::processMouseEvent(QWindowSystemInterfacePrivate::MouseEvent*) + 3404
60  org.qt-project.QtGui          	0x0000000119a98f9b QWindowSystemInterface::sendWindowSystemEvents(QFlags&lt;QEventLoop::ProcessEventsFlag&gt;) + 219
61  libqcocoa.dylib               	0x0000000123c10b90 0x123be3000 + 187280
62  libqcocoa.dylib               	0x0000000123c11400 0x123be3000 + 189440
63  com.apple.CoreFoundation      	0x00007fff4c3281d9 __CFRUNLOOP_IS_CALLING_OUT_TO_A_SOURCE0_PERFORM_FUNCTION__ + 17
64  com.apple.CoreFoundation      	0x00007fff4c32817f __CFRunLoopDoSource0 + 108
65  com.apple.CoreFoundation      	0x00007fff4c30c02c __CFRunLoopDoSources0 + 195
66  com.apple.CoreFoundation      	0x00007fff4c30b5d3 __CFRunLoopRun + 1226
67  com.apple.CoreFoundation      	0x00007fff4c30aeb6 CFRunLoopRunSpecific + 467
68  com.apple.HIToolbox           	0x00007fff4b594ab5 RunCurrentEventLoopInMode + 293
69  com.apple.HIToolbox           	0x00007fff4b5946f4 ReceiveNextEventCommon + 371
70  com.apple.HIToolbox           	0x00007fff4b594568 _BlockUntilNextEventMatchingListInModeWithFilter + 64
71  com.apple.AppKit              	0x00007fff4984f363 _DPSNextEvent + 997
72  com.apple.AppKit              	0x00007fff4984e102 -[NSApplication(NSEvent) _nextEventMatchingEventMask:untilDate:inMode:dequeue:] + 1362
73  com.apple.AppKit              	0x00007fff49848165 -[NSApplication run] + 699
74  libqcocoa.dylib               	0x0000000123c1025b 0x123be3000 + 184923
75  org.qt-project.QtCore         	0x000000011a1a261f QEventLoop::exec(QFlags&lt;QEventLoop::ProcessEventsFlag&gt;) + 431
76  org.qt-project.QtCore         	0x000000011a1a75c2 QCoreApplication::exec() + 130
77                                	0x0000000107bd6f53 main + 483 (Main.cxx:62)
78  libdyld.dylib                 	0x00007fff795e5ed9 start + 1

</code></pre>

---

## Post #3 by @muratmaga (2019-02-08 20:31 UTC)

<p>I would be also hesitant to fix something that’s going to be replaced soon. Any idea when the new infrastructure will be in place?</p>

---

## Post #4 by @pieper (2019-02-08 20:45 UTC)

<p>I believe it’s very close.  <a class="mention" href="/u/davide_punzo">@Davide_Punzo</a> or <a class="mention" href="/u/lassoan">@lassoan</a> and estimate on the remaining work?</p>

---

## Post #5 by @lassoan (2019-02-08 23:19 UTC)

<p>Probably a few more days. See status <a href="https://github.com/Slicer/Slicer/pull/1079#issuecomment-457002667" rel="nofollow noopener">here</a>.</p>

---

## Post #6 by @muratmaga (2019-02-09 01:21 UTC)

<p>Ok. Sounds like we can definitely wait for the updated infrastructure.</p>

---

## Post #7 by @smrolfe (2019-02-09 01:35 UTC)

<p>Sounds like a good plan!</p>

---
