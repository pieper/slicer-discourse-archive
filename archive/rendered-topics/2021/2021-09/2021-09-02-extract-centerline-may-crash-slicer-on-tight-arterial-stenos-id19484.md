# Extract centerline may crash slicer on tight arterial stenosis

**Topic ID**: 19484
**Date**: 2021-09-02
**URL**: https://discourse.slicer.org/t/extract-centerline-may-crash-slicer-on-tight-arterial-stenosis/19484

---

## Post #1 by @chir.set (2021-09-02 14:40 UTC)

<p>First, this is reported for its technical aspects.</p>
<p>Centerline extraction may not always produce a good one with default parameters and only two endpoints. I noticed that by decreasing ‘Decimation aggressiveness’, centerline extraction ends up with good results very often.</p>
<p>My last extraction on a femoral segment with a long stenosis, very tight st some points, succeeded with default parameters, but crashed Slicer when ‘Decimation aggressiveness’ is decreased to 1.0 k (as an experiment). This is reproducible. The scene MRB file is linked <a href="https://disk.yandex.com/d/_Lcrfsfe_iiScA" rel="noopener nofollow ugc">here</a>. And the backtrace follows :</p>
<pre><code class="lang-auto">Switch to module:  "ExtractCenterline"
Found CommandLine Module, target is  /data_ssd/programs/Slicer-4.13.0-2021-08-28-linux-amd64/bin/../lib/Slicer-4.13/cli-modules/Decimation
ModuleType: CommandLineModule
Decimation command line: 

/data_ssd/programs/Slicer-4.13.0-2021-08-28-linux-amd64/bin/../lib/Slicer-4.13/cli-modules/Decimation --reductionFactor 0.692497 --method FastQuadric --deleteBoundary --aggressiveness 1 /tmp/Slicer/GBCFIJ_vtkMRMLModelNodeF.obj /tmp/Slicer/GBCFIJ_vtkMRMLModelNodeG.obj 

Process 612589 stopped and restarted: thread 1 received signal: SIGCHLD
Decimation standard output:

Input: 16260 vertices,32520 triangles (target 10000)

Decimation standard error:

Unable to reduce mesh.



Decimation completed with errors



Input port 0 of algorithm vtkCleanPolyData(0x55555c430ab0) has 0 connections but is not optional.


No points to subdivide


&lt;&lt;Cannot triangulate; no input points


error: libstdc++.so.6 {0x00181389}: DIE has DW_AT_ranges(0x119c8) attribute, but range extraction failed (missing or invalid range list table), please file a bug and attach the file at the start of this error message
Process 612589 stopped
* thread #1, name = 'SlicerApp-real', stop reason = signal SIGSEGV: invalid address (fault address: 0x0)
    frame #0: 0x00007ffeff6da9a7 libvtkvmtkComputationalGeometry.so`vtkvmtkPolyDataCenterlines::RequestData(vtkInformation*, vtkInformationVector**, vtkInformationVector*) + 535
libvtkvmtkComputationalGeometry.so`vtkvmtkPolyDataCenterlines::RequestData:
-&gt;  0x7ffeff6da9a7 &lt;+535&gt;: movq   (%rax), %rcx
    0x7ffeff6da9aa &lt;+538&gt;: movq   %rax, %rdi
    0x7ffeff6da9ad &lt;+541&gt;: callq  *0x190(%rcx)
    0x7ffeff6da9b3 &lt;+547&gt;: movq   (%rbp), %rcx
(lldb) bt
* thread #1, name = 'SlicerApp-real', stop reason = signal SIGSEGV: invalid address (fault address: 0x0)
  * frame #0: 0x00007ffeff6da9a7 libvtkvmtkComputationalGeometry.so`vtkvmtkPolyDataCenterlines::RequestData(vtkInformation*, vtkInformationVector**, vtkInformationVector*) + 535
    frame #1: 0x00007fffe1911fdf libvtkCommon-9.0.so.1`vtkExecutive::CallAlgorithm(this=0x000055555f466ec0, request=0x000055555f463ce0, direction=&lt;unavailable&gt;, inInfo=0x000055555de7b750, outInfo=0x000055555da22cf0) at vtkExecutive.cxx:746:33
    frame #2: 0x00007fffe190d867 libvtkCommon-9.0.so.1`vtkDemandDrivenPipeline::ExecuteData(this=0x000055555f466ec0, request=0x000055555f463ce0, inInfo=0x000055555de7b750, outInfo=0x000055555da22cf0) at vtkDemandDrivenPipeline.cxx:462:22
    frame #3: 0x00007fffe1908a17 libvtkCommon-9.0.so.1`vtkCompositeDataPipeline::ExecuteData(this=0x000055555f466ec0, request=0x000055555f463ce0, inInfoVec=0x000055555de7b750, outInfoVec=0x000055555da22cf0) at vtkCompositeDataPipeline.cxx:161:32
    frame #4: 0x00007fffe190d083 libvtkCommon-9.0.so.1`vtkDemandDrivenPipeline::ProcessRequest(this=0x000055555f466ec0, request=0x000055555f463ce0, inInfoVec=0x000055555de7b750, outInfoVec=&lt;unavailable&gt;) at vtkDemandDrivenPipeline.cxx:261:22
    frame #5: 0x00007fffe1937b1a libvtkCommon-9.0.so.1`vtkStreamingDemandDrivenPipeline::ProcessRequest(this=0x000055555f466ec0, request=0x000055555f463ce0, inInfoVec=&lt;unavailable&gt;, outInfoVec=0x000055555da22cf0) at vtkStreamingDemandDrivenPipeline.cxx:0
    frame #6: 0x00007fffe190d635 libvtkCommon-9.0.so.1`vtkDemandDrivenPipeline::UpdateData(this=0x000055555f466ec0, outputPort=&lt;unavailable&gt;) at vtkDemandDrivenPipeline.cxx:419:16
    frame #7: 0x00007fffe19380d1 libvtkCommon-9.0.so.1`vtkStreamingDemandDrivenPipeline::Update(this=0x000055555f466ec0, port=0, requests=&lt;unavailable&gt;) at vtkStreamingDemandDrivenPipeline.cxx:417:34
    frame #8: 0x00007fff8c2d2b92 vtkCommonExecutionModel.cpython-36m-x86_64-linux-gnu.so`PyvtkAlgorithm_Update(_object*, _object*) [inlined] PyvtkAlgorithm_Update_s2(self=&lt;unavailable&gt;, args=&lt;unavailable&gt;) at vtkAlgorithmPython.cxx:2338:11
    frame #9: 0x00007fff8c2d2b29 vtkCommonExecutionModel.cpython-36m-x86_64-linux-gnu.so`PyvtkAlgorithm_Update(self=&lt;unavailable&gt;, args=&lt;unavailable&gt;) at vtkAlgorithmPython.cxx:2425
    frame #10: 0x00007fffe51b89fc libpython3.6m.so`_PyCFunction_FastCallDict(func_obj=0x00007ffef6f41ca8, args=0x000055555f1e0f98, nargs=&lt;unavailable&gt;, kwargs=0x0000000000000000) at methodobject.c:234:22
    frame #11: 0x00007fffe522d1bb libpython3.6m.so`call_function(pp_stack=0x00007fffffffae08, oparg=&lt;unavailable&gt;, kwnames=&lt;unavailable&gt;) at ceval.c:4837:9
    frame #12: 0x00007fffe522a43e libpython3.6m.so`_PyEval_EvalFrameDefault(f=0x000055555f1e0d68, throwflag=&lt;unavailable&gt;) at ceval.c:3335:19
    frame #13: 0x00007fffe522dd56 libpython3.6m.so`_PyEval_EvalCodeWithName [inlined] PyEval_EvalFrameEx(f=0x000055555f1e0d68, throwflag=0) at ceval.c:754:12
    frame #14: 0x00007fffe522dd40 libpython3.6m.so`_PyEval_EvalCodeWithName(_co=&lt;unavailable&gt;, globals=&lt;unavailable&gt;, locals=&lt;unavailable&gt;, args=0x000055555e182d68, argcount=&lt;unavailable&gt;, kwnames=0x0000000000000000, kwargs=0x000055555e182d88, kwcount=0, kwstep=1, defs=0x00007fff105f86f0, defcount=1, kwdefs=0x0000000000000000, closure=0x0000000000000000, name=0x00007fff105ff5d0, qualname=0x00007fff105812d0) at ceval.c:4166
    frame #15: 0x00007fffe522e41c libpython3.6m.so`fast_function(func=&lt;unavailable&gt;, stack=0x000055555e182d68, nargs=&lt;unavailable&gt;, kwnames=&lt;unavailable&gt;) at ceval.c:4978:12
    frame #16: 0x00007fffe522d194 libpython3.6m.so`call_function(pp_stack=0x00007fffffffb0a8, oparg=&lt;unavailable&gt;, kwnames=&lt;unavailable&gt;) at ceval.c:4858:17
    frame #17: 0x00007fffe522a43e libpython3.6m.so`_PyEval_EvalFrameDefault(f=0x000055555e182b38, throwflag=&lt;unavailable&gt;) at ceval.c:3335:19
    frame #18: 0x00007fffe522e887 libpython3.6m.so`_PyFunction_FastCallDict(func=&lt;unavailable&gt;, args=&lt;unavailable&gt;, nargs=&lt;unavailable&gt;, kwargs=&lt;unavailable&gt;) at ceval.c:0
    frame #19: 0x00007fffe5176612 libpython3.6m.so`_PyObject_FastCallDict(func=0x00007fff1058a158, args=0x00007fffffffb210, nargs=1, kwargs=0x0000000000000000) at abstract.c:2310:18
    frame #20: 0x00007fffe51767b1 libpython3.6m.so`_PyObject_Call_Prepend(func=0x00007fff1058a158, obj=0x00007ffe1412eb70, args=&lt;unavailable&gt;, kwargs=0x0000000000000000) at abstract.c:2373:14
    frame #21: 0x00007fffe51766b4 libpython3.6m.so`_PyObject_FastCallDict(func=0x00007ffe14152248, args=0x0000000000000000, nargs=0, kwargs=0x0000000000000000) at abstract.c:2331:18
    frame #22: 0x00007fffec2b7ecb libPythonQt.so`PythonQtSignalTarget::call(callable=0x00007ffe14152248, methodInfos=0x000055555c080110, arguments=0x00007fffffffb450, skipFirstArgumentOfMethodInfo=&lt;unavailable&gt;) at PythonQtSignalReceiver.cpp:130:14
    frame #23: 0x00007fffec2b8901 libPythonQt.so`PythonQtSignalReceiver::qt_metacall(QMetaObject::Call, int, void**) [inlined] PythonQtSignalTarget::call(this=0x000055555d4c51e0, arguments=0x00007fffffffb450) const at PythonQtSignalReceiver.cpp:56:22
    frame #24: 0x00007fffec2b88e9 libPythonQt.so`PythonQtSignalReceiver::qt_metacall(this=0x000055555bed1e00, c=&lt;unavailable&gt;, id=5, arguments=&lt;unavailable&gt;) at PythonQtSignalReceiver.cpp:273
    frame #25: 0x00007ffff62f14a7 libQt5Core.so.5`___lldb_unnamed_symbol4768$$libQt5Core.so.5 + 631
    frame #26: 0x00007ffff6e864e3 libQt5Widgets.so.5`QAbstractButton::clicked(bool) + 67
    frame #27: 0x00007ffff6e8676c libQt5Widgets.so.5`___lldb_unnamed_symbol1438$$libQt5Widgets.so.5 + 60
    frame #28: 0x00007ffff6e88374 libQt5Widgets.so.5`___lldb_unnamed_symbol1444$$libQt5Widgets.so.5 + 196
    frame #29: 0x00007ffff6e88595 libQt5Widgets.so.5`QAbstractButton::mouseReleaseEvent(QMouseEvent*) + 245
    frame #30: 0x00007ffff6dd20be libQt5Widgets.so.5`QWidget::event(QEvent*) + 526
    frame #31: 0x00007ffff6d8ed62 libQt5Widgets.so.5`QApplicationPrivate::notify_helper(QObject*, QEvent*) + 130
    frame #32: 0x00007ffff6d96ac9 libQt5Widgets.so.5`QApplication::notify(QObject*, QEvent*) + 2729
    frame #33: 0x00007ffff7c8cd1e libqSlicerBaseQTGUI.so`qSlicerApplication::notify(this=&lt;unavailable&gt;, receiver=&lt;unavailable&gt;, event=&lt;unavailable&gt;) at qSlicerApplication.cxx:412:26
    frame #34: 0x00007ffff62ba3aa libQt5Core.so.5`QCoreApplication::notifyInternal2(QObject*, QEvent*) + 314
    frame #35: 0x00007ffff6d9557b libQt5Widgets.so.5`QApplicationPrivate::sendMouseEvent(QWidget*, QMouseEvent*, QWidget*, QWidget*, QWidget**, QPointer&lt;QWidget&gt;&amp;, bool, bool) + 443
    frame #36: 0x00007ffff6deba84 libQt5Widgets.so.5`___lldb_unnamed_symbol921$$libQt5Widgets.so.5 + 740
    frame #37: 0x00007ffff6deedb5 libQt5Widgets.so.5`___lldb_unnamed_symbol932$$libQt5Widgets.so.5 + 517
    frame #38: 0x00007ffff6d8ed62 libQt5Widgets.so.5`QApplicationPrivate::notify_helper(QObject*, QEvent*) + 130
    frame #39: 0x00007ffff7c8cd1e libqSlicerBaseQTGUI.so`qSlicerApplication::notify(this=&lt;unavailable&gt;, receiver=&lt;unavailable&gt;, event=&lt;unavailable&gt;) at qSlicerApplication.cxx:412:26
    frame #40: 0x00007ffff62ba3aa libQt5Core.so.5`QCoreApplication::notifyInternal2(QObject*, QEvent*) + 314
    frame #41: 0x00007ffff6693210 libQt5Gui.so.5`QGuiApplicationPrivate::processMouseEvent(QWindowSystemInterfacePrivate::MouseEvent*) + 1712
    frame #42: 0x00007ffff66687e5 libQt5Gui.so.5`QWindowSystemInterface::sendWindowSystemEvents(QFlags&lt;QEventLoop::ProcessEventsFlag&gt;) + 181
    frame #43: 0x00007fffce0d1fcc libQt5XcbQpa.so.5`___lldb_unnamed_symbol407$$libQt5XcbQpa.so.5 + 28
    frame #44: 0x00007fffe071b10c libglib-2.0.so.0`g_main_context_dispatch + 620
    frame #45: 0x00007fffe076eba9 libglib-2.0.so.0`___lldb_unnamed_symbol449$$libglib-2.0.so.0 + 521
    frame #46: 0x00007fffe0718871 libglib-2.0.so.0`g_main_context_iteration + 49
    frame #47: 0x00007ffff6312fd6 libQt5Core.so.5`QEventDispatcherGlib::processEvents(QFlags&lt;QEventLoop::ProcessEventsFlag&gt;) + 102
    frame #48: 0x00007ffff62b8d1c libQt5Core.so.5`QEventLoop::exec(QFlags&lt;QEventLoop::ProcessEventsFlag&gt;) + 300
    frame #49: 0x00007ffff62c1284 libQt5Core.so.5`QCoreApplication::exec() + 148
    frame #50: 0x00007ffff74e4436 libqSlicerBaseQTCore.so`qSlicerCoreApplication::exec() at qSlicerCoreApplication.cxx:876:19
    frame #51: 0x000055555555996c SlicerApp-real`main [inlined] (anonymous namespace)::SlicerAppMain(argc=1, argv=0x00007fffffffc2a8) at Main.cxx:62:10
    frame #52: 0x0000555555559781 SlicerApp-real`main(argc=&lt;unavailable&gt;, argv=0x00007fffffffc2a8) at qSlicerApplicationMainWrapper.cxx:56
    frame #53: 0x00007fffe1150b25 libc.so.6`__libc_start_main + 213
    frame #54: 0x000055555555968e SlicerApp-real`_start + 46
(lldb)
</code></pre>
<p>I further tried with a ‘Decimation aggressiveness’ value of 0.1 k in another segment of an aortic aneurysm (big tube, in contrast to a tight stenosis). It succeeded.</p>
<p>That is not a clinical issue as treatment options are quite clear in that case.</p>
<p>I just wish to report it so that a decimation failure could be managed, so as to avoid application crash. I can’t know if it’s up to ‘Extract centerline’ to handle this, or to the VMTK libs themselves.</p>
<p>Regards.</p>

---

## Post #2 by @lassoan (2021-09-02 18:11 UTC)

<p>Thanks for reporting this. Since it is not a nominal use case and there is a workaround, we will not immediately address this. Also, the issue is most likely due to some missing null-pointer check in VTK and will be resolved in future VTK versions. But it is good to know about and track this issue, so it would be great if you could submit this as an issue to <a href="https://github.com/vmtk/SlicerExtension-VMTK/">SlicerVMTK</a> bugtracker.</p>

---

## Post #3 by @chir.set (2021-09-02 19:11 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="19484">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>we will not immediately address this</p>
</blockquote>
</aside>
<p>Of course this can wait.<br>
Submitted <a href="https://github.com/vmtk/SlicerExtension-VMTK/issues/41" rel="noopener nofollow ugc">here</a>.</p>

---

## Post #4 by @lassoan (2023-03-18 04:17 UTC)

<p>Probably this fix solved this problem:</p>
<aside class="quote" data-post="7" data-topic="26576">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/extract-centeline-auto-detect-tree-mode/26576/7">Extract centeline Auto-detect tree mode</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    The crash was due to a bug in VTK that I’ve fixed a couple of months ago, but that fix was not yet backported into Slicer’s VTK. I’ve now <a href="https://github.com/Slicer/Slicer/commit/396c8e5d0ac6bcacf413103c3cb358211a9d5d8c">backported it</a>, so centerline extraction will work robustly in Slicer Preview Release that you download on 2023-03-19 or later.
  </blockquote>
</aside>


---

## Post #5 by @chir.set (2023-03-18 08:21 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="19484">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Probably this fix solved this problem:</p>
</blockquote>
</aside>
<p>Yes, Slicer does not crash when redoing the steps described above (‘Target point count’ and ‘Decimation aggressiveness’ were being confused in the original post <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20">).</p>

---
