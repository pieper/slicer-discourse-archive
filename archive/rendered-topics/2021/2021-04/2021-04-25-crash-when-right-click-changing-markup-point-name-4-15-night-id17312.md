# Crash when right-click changing markup point name - 4/15 nightly

**Topic ID**: 17312
**Date**: 2021-04-25
**URL**: https://discourse.slicer.org/t/crash-when-right-click-changing-markup-point-name-4-15-nightly/17312

---

## Post #1 by @hherhold (2021-04-25 17:59 UTC)

<p>MacOS 10.15.7.</p>
<p>This is an annoyingly intermittent crash. Sometimes when I right-click on a markup point to change the name, after modifying the name and hitting OK, Slicer seg faults.</p>
<p>I’m guessing the best course of action is to build a debug version and see if I can replicate it with that?</p>
<p>-Hollister</p>
<p>Stack trace:</p>
<pre><code>Crashed Thread:        0  Dispatch queue: com.apple.main-thread

Exception Type:        EXC_BAD_ACCESS (SIGSEGV)
Exception Codes:       KERN_INVALID_ADDRESS at 0x000007fc148e8fb8
Exception Note:        EXC_CORPSE_NOTIFY

Termination Signal:    Segmentation fault: 11
Termination Reason:    Namespace SIGNAL, Code 0xb
Terminating Process:   exc handler [36313]

VM Regions Near 0x7fc148e8fb8:
    VM_ALLOCATE            00000001b0563000-00000001bd1fb000 [204.6M] rw-/rwx SM=PRV  
--&gt; 
    JS JIT generated code  000059d9c0c00000-000059d9c8c00000 [128.0M] rwx/rwx SM=COW  

Thread 0 Crashed:: Dispatch queue: com.apple.main-thread
0   libvtkCommon-9.0.1.dylib      	0x0000000117a5d910 vtkSubjectHelper::InvokeEvent(unsigned long, void*, vtkObject*) + 816
1   libvtkSlicerMarkupsModuleVTKWidgets.dylib	0x00000001398b1cdf vtkSlicerMarkupsWidget::ProcessWidgetMenu(vtkMRMLInteractionEventData*) + 399
2   libvtkSlicerMarkupsModuleMRMLDisplayableManager.dylib	0x00000001397fb685 vtkMRMLMarkupsDisplayableManager::ProcessInteractionEvent(vtkMRMLInteractionEventData*) + 501
3   libMRMLDisplayableManager.dylib	0x000000010c4227dc vtkMRMLViewInteractorStyle::DelegateInteractionEventDataToDisplayableManagers(vtkMRMLInteractionEventData*) + 540
4   libMRMLDisplayableManager.dylib	0x000000010c42408b vtkMRMLThreeDViewInteractorStyle::DelegateInteractionEventToDisplayableManagers(vtkEventData*) + 379
5   libMRMLDisplayableManager.dylib	0x000000010c422392 vtkMRMLViewInteractorStyle::DelegateInteractionEventToDisplayableManagers(unsigned long) + 50
6   libMRMLDisplayableManager.dylib	0x000000010c421e60 vtkMRMLViewInteractorStyle::CustomProcessEvents(vtkObject*, unsigned long, void*, void*) + 176
7   libvtkCommon-9.0.1.dylib      	0x000000011791c2a1 vtkCallbackCommand::Execute(vtkObject*, unsigned long, void*) + 33
8   libvtkCommon-9.0.1.dylib      	0x0000000117a5d9bf vtkSubjectHelper::InvokeEvent(unsigned long, void*, vtkObject*) + 991
9   libvtkGUISupportQt-9.0.1.dylib	0x000000011370984b QVTKInteractorAdapter::ProcessEvent(QEvent*, vtkRenderWindowInteractor*) + 2171
10  libvtkGUISupportQt-9.0.1.dylib	0x000000011370bc3e QVTKOpenGLNativeWidget::event(QEvent*) + 30
11  org.qt-project.QtWidgets      	0x0000000102245fea QApplicationPrivate::notify_helper(QObject*, QEvent*) + 266
12  org.qt-project.QtWidgets      	0x0000000102248d55 QApplication::notify(QObject*, QEvent*) + 6965
13  libqSlicerBaseQTGUI.dylib     	0x0000000101704e95 qSlicerApplication::notify(QObject*, QEvent*) + 21
14  org.qt-project.QtCore         	0x0000000102fe17f4 QCoreApplication::notifyInternal2(QObject*, QEvent*) + 212
15  org.qt-project.QtWidgets      	0x0000000102246910 QApplicationPrivate::sendMouseEvent(QWidget*, QMouseEvent*, QWidget*, QWidget*, QWidget**, QPointer&lt;QWidget&gt;&amp;, bool, bool) + 896
16  org.qt-project.QtWidgets      	0x000000010229f622 0x102235000 + 435746
17  org.qt-project.QtWidgets      	0x000000010229dce9 0x102235000 + 429289
18  org.qt-project.QtWidgets      	0x0000000102245fea QApplicationPrivate::notify_helper(QObject*, QEvent*) + 266
19  org.qt-project.QtWidgets      	0x0000000102247411 QApplication::notify(QObject*, QEvent*) + 497
20  libqSlicerBaseQTGUI.dylib     	0x0000000101704e95 qSlicerApplication::notify(QObject*, QEvent*) + 21
21  org.qt-project.QtCore         	0x0000000102fe17f4 QCoreApplication::notifyInternal2(QObject*, QEvent*) + 212
22  org.qt-project.QtGui          	0x000000010281dac3 QGuiApplicationPrivate::processMouseEvent(QWindowSystemInterfacePrivate::MouseEvent*) + 3411
23  org.qt-project.QtGui          	0x0000000102802a6b QWindowSystemInterface::sendWindowSystemEvents(QFlags&lt;QEventLoop::ProcessEventsFlag&gt;) + 219
24  libqcocoa.dylib               	0x000000011c986290 0x11c94c000 + 238224
25  libqcocoa.dylib               	0x000000011c9869f8 0x11c94c000 + 240120
26  com.apple.CoreFoundation      	0x00007fff360b2d52 __CFRUNLOOP_IS_CALLING_OUT_TO_A_SOURCE0_PERFORM_FUNCTION__ + 17
27  com.apple.CoreFoundation      	0x00007fff360b2cf1 __CFRunLoopDoSource0 + 103
28  com.apple.CoreFoundation      	0x00007fff360b2b0b __CFRunLoopDoSources0 + 209
29  com.apple.CoreFoundation      	0x00007fff360b183a __CFRunLoopRun + 927
30  com.apple.CoreFoundation      	0x00007fff360b0e3e CFRunLoopRunSpecific + 462
31  com.apple.HIToolbox           	0x00007fff34cddabd RunCurrentEventLoopInMode + 292
32  com.apple.HIToolbox           	0x00007fff34cdd6f4 ReceiveNextEventCommon + 359
33  com.apple.HIToolbox           	0x00007fff34cdd579 _BlockUntilNextEventMatchingListInModeWithFilter + 64
34  com.apple.AppKit              	0x00007fff33323039 _DPSNextEvent + 883
35  com.apple.AppKit              	0x00007fff33321880 -[NSApplication(NSEvent) _nextEventMatchingEventMask:untilDate:inMode:dequeue:] + 1352
36  com.apple.AppKit              	0x00007fff3331358e -[NSApplication run] + 658
37  libqcocoa.dylib               	0x000000011c98565f 0x11c94c000 + 235103
38  org.qt-project.QtCore         	0x0000000102fdd88f QEventLoop::exec(QFlags&lt;QEventLoop::ProcessEventsFlag&gt;) + 431
39  org.qt-project.QtCore         	0x0000000102fe1e02 QCoreApplication::exec() + 130
40  libqSlicerBaseQTCore.dylib    	0x000000010200bc89 qSlicerCoreApplication::exec() + 9
41  org.slicer.slicer             	0x0000000101448423 main + 483
42  libdyld.dylib                 	0x00007fff70169cc9 start + 1</code></pre>

---

## Post #2 by @lassoan (2021-04-25 18:24 UTC)

<p>Have you installed any extensions?</p>

---

## Post #3 by @hherhold (2021-04-25 18:35 UTC)

<p>Yes - several, but nothing specific to markups, or that I need to test this out. Anything in particular I would look for? I do not have any extensions active when renaming the markup point (though they’ve all been loaded at startup).</p>

---

## Post #4 by @lassoan (2021-04-25 18:40 UTC)

<p>It would be useful if we could narrow down the potential root causes of the issue. If you can only reproduce the problem if a certain extension is installed then we know where to look for the problem. If you can come up with a series of steps that always reproduce the issue then that can help a lot, too.</p>
<p>Alternatively, if you can build Slicer in debug mode and reproduce the problem then we may be able to see what is going on exactly.</p>

---

## Post #5 by @hherhold (2021-04-25 18:43 UTC)

<p>I’m doing a debug build right now. I’ll use this for a while with no extensions loaded and see if I can replicate. I’ll go for days without it crashing, and then it will happen.</p>

---
