# Slicer Crashes when projecting fiducials in 4.10

**Topic ID**: 5698
**Date**: 2019-02-08
**URL**: https://discourse.slicer.org/t/slicer-crashes-when-projecting-fiducials-in-4-10/5698

---

## Post #1 by @muratmaga (2019-02-08 17:55 UTC)

<p>I can reproduce this with this data:<br>
<a href="https://github.com/SlicerMorph/SampleData/blob/master/gorilla_reference.mrb?raw=true" class="onebox" target="_blank" rel="nofollow noopener">https://github.com/SlicerMorph/SampleData/blob/master/gorilla_reference.mrb?raw=true</a></p>
<p>Navigate to the Markups module, and enable Fiducial projection. Slicer stalls and crashes. I can’t see what the error is. The last entry in the log file is “Switching to Markups Module”</p>
<ul>
<li>“MarkupsFiducials” Reader has successfully read the file “C:/Users/Murat/Documents/Gorilla_template_LM1.fcsv” “[0.10s]”<br>
[DEBUG][Qt] 08.02.2019 09:51:37 [] (unknown:0) - Switch to module:  “Markups”</li>
</ul>

---

## Post #2 by @pieper (2019-05-14 16:16 UTC)

<p>Thanks for reporting this - I am able to replicate it on the mac with 4.10.1 and I get the stack trace below.</p>
<p>I also tested on the current master (with the all new markups) and things work as expected with no crash.</p>
<p>So I’m sure it’s possible to dig in and debug to avoid the crash but it would be a workaround at best since we won’t be maintaining the old Markups infrastructure.  Is using the current nightly an option?</p>
<pre>
Thread 0 Crashed:: Dispatch queue: com.apple.main-thread
0   libvtkFilters-8.2.1.dylib     	0x00000001200e7882 vtkGlyph2D::RequestData(vtkInformation*, vtkInformationVector**, vtkInformationVector*) + 2994
1   libvtkCommon-8.2.1.dylib      	0x00000001215ec2c5 vtkExecutive::CallAlgorithm(vtkInformation*, int, vtkInformationVector**, vtkInformationVector*) + 69
2   libvtkCommon-8.2.1.dylib      	0x00000001215e6e9d vtkDemandDrivenPipeline::ExecuteData(vtkInformation*, vtkInformationVector**, vtkInformationVector*) + 61
3   libvtkCommon-8.2.1.dylib      	0x00000001215e185b vtkCompositeDataPipeline::ExecuteData(vtkInformation*, vtkInformationVector**, vtkInformationVector*) + 107
4   libvtkCommon-8.2.1.dylib      	0x00000001215e661c vtkDemandDrivenPipeline::ProcessRequest(vtkInformation*, vtkInformationVector**, vtkInformationVector*) + 1228
5   libvtkCommon-8.2.1.dylib      	0x000000012160c9a0 vtkStreamingDemandDrivenPipeline::ProcessRequest(vtkInformation*, vtkInformationVector**, vtkInformationVector*) + 1120
6   libvtkCommon-8.2.1.dylib      	0x000000012160cd8e vtkStreamingDemandDrivenPipeline::Update(int, vtkInformationVector*) + 254
7   libvtkOpenGL-8.2.1.dylib      	0x000000011ddc96f3 vtkOpenGLPolyDataMapper2D::RenderOverlay(vtkViewport*, vtkActor2D*) + 67
8   libvtkRendering-8.2.1.dylib   	0x000000011e79a04e vtkActor2D::RenderOverlay(vtkViewport*) + 286
9   libvtkOpenGL-8.2.1.dylib      	0x000000011ddda06a vtkOpenGLRenderer::UpdateGeometry() + 2666
10  libvtkOpenGL-8.2.1.dylib      	0x000000011ddd95d5 vtkOpenGLRenderer::DeviceRender() + 181
11  libvtkRendering-8.2.1.dylib   	0x000000011e832173 vtkRenderer::Render() + 1443
12  libvtkRendering-8.2.1.dylib   	0x000000011e830edb vtkRendererCollection::Render() + 139
13  libvtkRendering-8.2.1.dylib   	0x000000011e83bb3c vtkRenderWindow::DoStereoRender() + 140
14  libvtkRendering-8.2.1.dylib   	0x000000011e83b9fc vtkRenderWindow::Render() + 332
15  libvtkOpenGL-8.2.1.dylib      	0x000000011ddd85fe vtkOpenGLRenderWindow::Render() + 14
16  libvtkOpenGL-8.2.1.dylib      	0x000000011dd71dd2 vtkGenericOpenGLRenderWindow::Render() + 34
17  org.qt-project.QtCore         	0x000000011d9be139 QMetaObject::activate(QObject*, int, int, void**) + 3113
18  libCTKVisualizationVTKCore.0.1.dylib	0x000000010f911d04 ctkVTKConnection::emitExecute(vtkObject*, void*, unsigned long, void*) + 100
19  libCTKVisualizationVTKCore.0.1.dylib	0x000000010f90a3b2 ctkVTKConnectionPrivate::execute(vtkObject*, unsigned long, void*, void*) + 610
20  libvtkCommon-8.2.1.dylib      	0x00000001210b7231 vtkCallbackCommand::Execute(vtkObject*, unsigned long, void*) + 33
21  libMRMLCore.dylib             	0x0000000118bfc868 vtkEventBroker::InvokeObservation(vtkObservation*, unsigned long, void*) + 168
22  libMRMLCore.dylib             	0x0000000118bfc399 vtkEventBroker::ProcessEvent(vtkObservation*, vtkObject*, unsigned long, void*) + 137
23  libvtkCommon-8.2.1.dylib      	0x00000001210b7231 vtkCallbackCommand::Execute(vtkObject*, unsigned long, void*) + 33
24  libvtkCommon-8.2.1.dylib      	0x000000012122efc5 vtkSubjectHelper::InvokeEvent(unsigned long, void*, vtkObject*) + 1045
25  libvtkSlicerMarkupsModuleMRMLDisplayableManager.dylib	0x000000012c589eec vtkMRMLMarkupsFiducialDisplayableManager2D::SetNthSeed(int, vtkMRMLMarkupsFiducialNode*, vtkSeedWidget*) + 4444
26  libvtkSlicerMarkupsModuleMRMLDisplayableManager.dylib	0x000000012c58ae90 vtkMRMLMarkupsFiducialDisplayableManager2D::PropagateMRMLToWidget(vtkMRMLMarkupsNode*, vtkAbstractWidget*) + 2032
27  libvtkSlicerMarkupsModuleMRMLDisplayableManager.dylib	0x000000012c5813af vtkMRMLMarkupsDisplayableManager2D::OnMRMLMarkupsDisplayNodeModifiedEvent(vtkMRMLNode*) + 111
28  libMRMLLogic.dylib            	0x000000010f4a9e18 vtkMRMLAbstractLogic::MRMLNodesCallback(vtkObject*, unsigned long, void*, void*) + 72
29  libvtkCommon-8.2.1.dylib      	0x00000001210b7231 vtkCallbackCommand::Execute(vtkObject*, unsigned long, void*) + 33
30  libMRMLCore.dylib             	0x0000000118bfc868 vtkEventBroker::InvokeObservation(vtkObservation*, unsigned long, void*) + 168
31  libMRMLCore.dylib             	0x0000000118bfc399 vtkEventBroker::ProcessEvent(vtkObservation*, vtkObject*, unsigned long, void*) + 137
32  libvtkCommon-8.2.1.dylib      	0x00000001210b7231 vtkCallbackCommand::Execute(vtkObject*, unsigned long, void*) + 33
33  libvtkCommon-8.2.1.dylib      	0x000000012122efc5 vtkSubjectHelper::InvokeEvent(unsigned long, void*, vtkObject*) + 1045
34  libMRMLCore.dylib             	0x0000000118c4786a vtkMRMLDisplayableNode::ProcessMRMLEvents(vtkObject*, unsigned long, void*) + 202
35  libMRMLCore.dylib             	0x0000000118ccabc8 vtkMRMLNode::MRMLCallback(vtkObject*, unsigned long, void*, void*) + 72
36  libvtkCommon-8.2.1.dylib      	0x00000001210b7231 vtkCallbackCommand::Execute(vtkObject*, unsigned long, void*) + 33
37  libMRMLCore.dylib             	0x0000000118bfc868 vtkEventBroker::InvokeObservation(vtkObservation*, unsigned long, void*) + 168
38  libMRMLCore.dylib             	0x0000000118bfc399 vtkEventBroker::ProcessEvent(vtkObservation*, vtkObject*, unsigned long, void*) + 137
39  libvtkCommon-8.2.1.dylib      	0x00000001210b7231 vtkCallbackCommand::Execute(vtkObject*, unsigned long, void*) + 33
40  libvtkCommon-8.2.1.dylib      	0x000000012122efc5 vtkSubjectHelper::InvokeEvent(unsigned long, void*, vtkObject*) + 1045
41  org.qt-project.QtCore         	0x000000011d9be139 QMetaObject::activate(QObject*, int, int, void**) + 3113
42  org.qt-project.QtWidgets      	0x000000011cdbcb88 0x11ccaa000 + 1125256
43  org.qt-project.QtWidgets      	0x000000011cdbbf59 QAbstractButton::setChecked(bool) + 297
44  org.qt-project.QtWidgets      	0x000000011cdcc367 QCheckBox::nextCheckState() + 55
45  org.qt-project.QtWidgets      	0x000000011cdbc769 0x11ccaa000 + 1124201
46  org.qt-project.QtWidgets      	0x000000011cdbd82f QAbstractButton::mouseReleaseEvent(QMouseEvent*) + 271
47  org.qt-project.QtWidgets      	0x000000011ccf2afb QWidget::event(QEvent*) + 603
48  org.qt-project.QtWidgets      	0x000000011cdbd590 QAbstractButton::event(QEvent*) + 160
49  org.qt-project.QtWidgets      	0x000000011ccba8cd QApplicationPrivate::notify_helper(QObject*, QEvent*) + 301
50  org.qt-project.QtWidgets      	0x000000011ccbd8af QApplication::notify(QObject*, QEvent*) + 7663
51  libqSlicerBaseQTGUI.dylib     	0x000000010da365b1 qSlicerApplication::notify(QObject*, QEvent*) + 17
52  org.qt-project.QtCore         	0x000000011d98bc84 QCoreApplication::notifyInternal2(QObject*, QEvent*) + 164
53  org.qt-project.QtWidgets      	0x000000011ccbb1fa QApplicationPrivate::sendMouseEvent(QWidget*, QMouseEvent*, QWidget*, QWidget*, QWidget**, QPointer&amp;, bool) + 874
54  org.qt-project.QtWidgets      	0x000000011cd13bf0 0x11ccaa000 + 433136
55  org.qt-project.QtWidgets      	0x000000011cd12aaa 0x11ccaa000 + 428714
56  org.qt-project.QtWidgets      	0x000000011ccba8cd QApplicationPrivate::notify_helper(QObject*, QEvent*) + 301
57  org.qt-project.QtWidgets      	0x000000011ccbbc47 QApplication::notify(QObject*, QEvent*) + 391
58  libqSlicerBaseQTGUI.dylib     	0x000000010da365b1 qSlicerApplication::notify(QObject*, QEvent*) + 17
59  org.qt-project.QtCore         	0x000000011d98bc84 QCoreApplication::notifyInternal2(QObject*, QEvent*) + 164
60  org.qt-project.QtGui          	0x000000011d296796 QGuiApplicationPrivate::processMouseEvent(QWindowSystemInterfacePrivate::MouseEvent*) + 3062
61  org.qt-project.QtGui          	0x000000011d27d95b QWindowSystemInterface::sendWindowSystemEvents(QFlags) + 155
62  libqcocoa.dylib               	0x0000000123b620a1 0x123b37000 + 176289
63  com.apple.CoreFoundation      	0x00007fff361ca31b __CFRUNLOOP_IS_CALLING_OUT_TO_A_SOURCE0_PERFORM_FUNCTION__ + 17
64  com.apple.CoreFoundation      	0x00007fff361ca2c1 __CFRunLoopDoSource0 + 108
65  com.apple.CoreFoundation      	0x00007fff361ae1bb __CFRunLoopDoSources0 + 195
66  com.apple.CoreFoundation      	0x00007fff361ad783 __CFRunLoopRun + 1196
67  com.apple.CoreFoundation      	0x00007fff361ad085 CFRunLoopRunSpecific + 459
68  com.apple.HIToolbox           	0x00007fff3548b9db RunCurrentEventLoopInMode + 292
69  com.apple.HIToolbox           	0x00007fff3548b61d ReceiveNextEventCommon + 355
70  com.apple.HIToolbox           	0x00007fff3548b4a6 _BlockUntilNextEventMatchingListInModeWithFilter + 64
71  com.apple.AppKit              	0x00007fff33825ffb _DPSNextEvent + 965
72  com.apple.AppKit              	0x00007fff33824d93 -[NSApplication(NSEvent) _nextEventMatchingEventMask:untilDate:inMode:dequeue:] + 1361
73  com.apple.AppKit              	0x00007fff3381eeb0 -[NSApplication run] + 699
74  libqcocoa.dylib               	0x0000000123b60e0d 0x123b37000 + 171533
75  org.qt-project.QtCore         	0x000000011d987641 QEventLoop::exec(QFlags) + 417
76  org.qt-project.QtCore         	0x000000011d98c358 QCoreApplication::exec() + 392
77                                	0x000000010d6a5782 main + 530
78  libdyld.dylib                 	0x00007fff626c03d5 start + 1
</pre>

---

## Post #3 by @muratmaga (2019-05-14 16:28 UTC)

<p>Well, we are releasing a new extension that relies on this feature. Of course forcing nightly is an option, but given the state of changes happening in the nightly, and the fact of the potential users of this extension will be all new to Slicer, I am a little hesitant.</p>

---

## Post #4 by @lassoan (2019-05-14 16:34 UTC)

<p>I would suggest to test the nightly and fix any errors we find there.</p>

---

## Post #5 by @muratmaga (2019-05-14 16:40 UTC)

<p>I doesn’t happen with nightly.</p>
<p>My primary concern is reliability of the nightlies due to code refactoring. Over the course of summer we are going to introduce to Slicer about 60 biologists and basic scientists who never used it before and may not be ready for the idiosyncrasies of working with a constantly developing software. In other words, not making a good initial impression is my concern…</p>

---

## Post #6 by @lassoan (2019-05-14 16:45 UTC)

<p>I think the big changes have been completed. We are in the process of cleaning up.</p>
<p>We are still making changes to Markups, but there will be less and less API changes.</p>
<p>When is the first event?</p>

---

## Post #7 by @muratmaga (2019-05-14 16:48 UTC)

<p>First big workshop is June 17, then the second big group is starting August 25th. We have smaller demos between now and then, but those are not a big concern.</p>

---

## Post #8 by @lassoan (2019-05-14 17:20 UTC)

<p>By June 17, but Slicer should be stable and features that worked in 4.10 should work in the nightlies as well. If you find any issues then let us know. By August we should have all the new Markup features working well, too.</p>

---
