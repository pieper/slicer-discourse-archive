---
topic_id: 18528
title: "Baffle Planner May Crash Slicer"
date: 2021-07-06
url: https://discourse.slicer.org/t/18528
---

# Baffle planner may crash Slicer

**Topic ID**: 18528
**Date**: 2021-07-06
**URL**: https://discourse.slicer.org/t/baffle-planner-may-crash-slicer/18528

---

## Post #1 by @chir.set (2021-07-06 10:53 UTC)

<p>Seen on Linux, factory and home built. The crash happens <em>almost</em> always in this sequence :</p>
<ul>
<li>Load a volume</li>
<li>Go to Baffle planner</li>
<li>Create new closed curve from combobox</li>
<li>Place points in a single slice view</li>
<li>Create model with the combobox</li>
<li>Rotate a little in 3D view</li>
<li>Move a few points in 3D view</li>
<li>Close scene</li>
<li>Do not change module</li>
<li>Repeat above</li>
</ul>
<p>Slicer crashes almost always at step ‘Create model with the combobox’.</p>
<p>The following backtrace could be obtained :</p>
<pre><code class="lang-auto">error: libstdc++.so.6 {0x00181389}: DIE has DW_AT_ranges(0x119c8) attribute, but range extraction failed (missing or invalid range list table), please file a bug and attach the file at the start of this error message
Process 467994 stopped
* thread #1, name = 'SlicerApp-real', stop reason = signal SIGSEGV: invalid address (fault address: 0x41)
    frame #0: 0x00007fffe0bfa97b libvtkCommon-8.2.so.1`___lldb_unnamed_symbol3451$$libvtkCommon-8.2.so.1 + 43
libvtkCommon-8.2.so.1`___lldb_unnamed_symbol3451$$libvtkCommon-8.2.so.1:
-&gt;  0x7fffe0bfa97b &lt;+43&gt;: movl   (%rdi), %eax
    0x7fffe0bfa97d &lt;+45&gt;: movl   %eax, 0x1c(%rsp)
    0x7fffe0bfa981 &lt;+49&gt;: movl   $0x0, (%rdi)
    0x7fffe0bfa987 &lt;+55&gt;: xorps  %xmm0, %xmm0
(lldb) bt
* thread #1, name = 'SlicerApp-real', stop reason = signal SIGSEGV: invalid address (fault address: 0x41)
  * frame #0: 0x00007fffe0bfa97b libvtkCommon-8.2.so.1`___lldb_unnamed_symbol3451$$libvtkCommon-8.2.so.1 + 43
    frame #1: 0x00007fffe0bfad5b libvtkCommon-8.2.so.1`___lldb_unnamed_symbol3451$$libvtkCommon-8.2.so.1 + 1035
    frame #2: 0x00007fffe0d6b4e9 libvtkCommon-8.2.so.1`vtkDataSet::Initialize() + 9
    frame #3: 0x00007fffe0ed5b79 libvtkCommon-8.2.so.1`vtkPointSet::Initialize() + 9
    frame #4: 0x00007fffe0edca7c libvtkCommon-8.2.so.1`vtkPolyData::Initialize() + 12
    frame #5: 0x00007fffe0fc030e libvtkCommon-8.2.so.1`vtkDemandDrivenPipeline::ExecuteDataStart(vtkInformation*, vtkInformationVector**, vtkInformationVector*) + 206
    frame #6: 0x00007fffe0fe3a8c libvtkCommon-8.2.so.1`vtkStreamingDemandDrivenPipeline::ExecuteDataStart(vtkInformation*, vtkInformationVector**, vtkInformationVector*) + 108
    frame #7: 0x00007fffe0fc01fd libvtkCommon-8.2.so.1`vtkDemandDrivenPipeline::ExecuteData(vtkInformation*, vtkInformationVector**, vtkInformationVector*) + 29
    frame #8: 0x00007fffe0fbb084 libvtkCommon-8.2.so.1`vtkCompositeDataPipeline::ExecuteData(vtkInformation*, vtkInformationVector**, vtkInformationVector*) + 116
    frame #9: 0x00007fffe0fbfa12 libvtkCommon-8.2.so.1`vtkDemandDrivenPipeline::ProcessRequest(vtkInformation*, vtkInformationVector**, vtkInformationVector*) + 1234
    frame #10: 0x00007fffe0fe185f libvtkCommon-8.2.so.1`vtkStreamingDemandDrivenPipeline::ProcessRequest(vtkInformation*, vtkInformationVector**, vtkInformationVector*) + 703
    frame #11: 0x00007fffe0fbff85 libvtkCommon-8.2.so.1`vtkDemandDrivenPipeline::UpdateData(int) + 245
    frame #12: 0x00007fffe0fe1d71 libvtkCommon-8.2.so.1`vtkStreamingDemandDrivenPipeline::Update(int, vtkInformationVector*) + 241
    frame #13: 0x00007fff38c009ed libvtkCommonKitPython36D-8.2.so.1`___lldb_unnamed_symbol11178$$libvtkCommonKitPython36D-8.2.so.1 + 461
    frame #14: 0x00007fffe531a9fc libpython3.6m.so`_PyCFunction_FastCallDict + 172
    frame #15: 0x00007fffe538f1bb libpython3.6m.so`___lldb_unnamed_symbol1574$$libpython3.6m.so + 475
    frame #16: 0x00007fffe538c43e libpython3.6m.so`_PyEval_EvalFrameDefault + 25230
    frame #17: 0x00007fffe5390492 libpython3.6m.so`___lldb_unnamed_symbol1576$$libpython3.6m.so + 450
    frame #18: 0x00007fffe538f194 libpython3.6m.so`___lldb_unnamed_symbol1574$$libpython3.6m.so + 436
    frame #19: 0x00007fffe538c43e libpython3.6m.so`_PyEval_EvalFrameDefault + 25230
    frame #20: 0x00007fffe538fd56 libpython3.6m.so`___lldb_unnamed_symbol1575$$libpython3.6m.so + 2774
    frame #21: 0x00007fffe539041c libpython3.6m.so`___lldb_unnamed_symbol1576$$libpython3.6m.so + 332
    frame #22: 0x00007fffe538f194 libpython3.6m.so`___lldb_unnamed_symbol1574$$libpython3.6m.so + 436
    frame #23: 0x00007fffe538c43e libpython3.6m.so`_PyEval_EvalFrameDefault + 25230
    frame #24: 0x00007fffe5390492 libpython3.6m.so`___lldb_unnamed_symbol1576$$libpython3.6m.so + 450
    frame #25: 0x00007fffe538f194 libpython3.6m.so`___lldb_unnamed_symbol1574$$libpython3.6m.so + 436
    frame #26: 0x00007fffe538c43e libpython3.6m.so`_PyEval_EvalFrameDefault + 25230
    frame #27: 0x00007fffe5390492 libpython3.6m.so`___lldb_unnamed_symbol1576$$libpython3.6m.so + 450
    frame #28: 0x00007fffe538f194 libpython3.6m.so`___lldb_unnamed_symbol1574$$libpython3.6m.so + 436
    frame #29: 0x00007fffe538c43e libpython3.6m.so`_PyEval_EvalFrameDefault + 25230
    frame #30: 0x00007fffe538fd56 libpython3.6m.so`___lldb_unnamed_symbol1575$$libpython3.6m.so + 2774
    frame #31: 0x00007fffe5390761 libpython3.6m.so`_PyFunction_FastCallDict + 529
    frame #32: 0x00007fffe52d8612 libpython3.6m.so`_PyObject_FastCallDict + 162
    frame #33: 0x00007fffe52d87b1 libpython3.6m.so`_PyObject_Call_Prepend + 129
    frame #34: 0x00007fffe52d8483 libpython3.6m.so`PyObject_Call + 99
    frame #35: 0x00007fffe52185b1 libvtkWrappingPython36Core-8.2.so.1`vtkPythonCommand::Execute(vtkObject*, unsigned long, void*) + 305
    frame #36: 0x00007fffe0bfad5b libvtkCommon-8.2.so.1`___lldb_unnamed_symbol3451$$libvtkCommon-8.2.so.1 + 1035
    frame #37: 0x00007fffeb431e59 libMRMLCore.so`vtkMRMLNode::SetAndObserveNthNodeReferenceID(char const*, int, char const*, vtkIntArray*) + 2777
    frame #38: 0x00007fff2b4277da libMRMLCorePythonD.so`___lldb_unnamed_symbol1374$$libMRMLCorePythonD.so + 298
    frame #39: 0x00007fffe531a9fc libpython3.6m.so`_PyCFunction_FastCallDict + 172
    frame #40: 0x00007fffe538f1bb libpython3.6m.so`___lldb_unnamed_symbol1574$$libpython3.6m.so + 475
    frame #41: 0x00007fffe538c43e libpython3.6m.so`_PyEval_EvalFrameDefault + 25230
    frame #42: 0x00007fffe5390492 libpython3.6m.so`___lldb_unnamed_symbol1576$$libpython3.6m.so + 450
    frame #43: 0x00007fffe538f194 libpython3.6m.so`___lldb_unnamed_symbol1574$$libpython3.6m.so + 436
    frame #44: 0x00007fffe538c43e libpython3.6m.so`_PyEval_EvalFrameDefault + 25230
    frame #45: 0x00007fffe538fd56 libpython3.6m.so`___lldb_unnamed_symbol1575$$libpython3.6m.so + 2774
    frame #46: 0x00007fffe5386164 libpython3.6m.so`PyEval_EvalCodeEx + 84
    frame #47: 0x00007fffe52ffba3 libpython3.6m.so`___lldb_unnamed_symbol707$$libpython3.6m.so + 355
    frame #48: 0x00007fffe52d8483 libpython3.6m.so`PyObject_Call + 99
    frame #49: 0x00007fffebe0eb5b libPythonQt.so`PythonQtSignalTarget::call(_object*, PythonQtMethodInfo const*, void**, bool) + 299
    frame #50: 0x00007fffebe0f5a1 libPythonQt.so`PythonQtSignalReceiver::qt_metacall(QMetaObject::Call, int, void**) + 209
    frame #51: 0x00007ffff63374a7 libQt5Core.so.5`___lldb_unnamed_symbol4768$$libQt5Core.so.5 + 631
    frame #52: 0x00007ffff7aed35d libqMRMLWidgets.so`qMRMLNodeComboBox::currentNodeChanged(vtkMRMLNode*) + 61
    frame #53: 0x00007ffff7a5c7f3 libqMRMLWidgets.so`qMRMLNodeComboBox::emitCurrentNodeChanged() + 115
    frame #54: 0x00007ffff7aecfe7 libqMRMLWidgets.so`___lldb_unnamed_symbol188$$libqMRMLWidgets.so + 2343
    frame #55: 0x00007ffff6337790 libQt5Core.so.5`___lldb_unnamed_symbol4768$$libQt5Core.so.5 + 1376
    frame #56: 0x00007ffff6ee0556 libQt5Widgets.so.5`QComboBox::currentIndexChanged(QString const&amp;) + 54
    frame #57: 0x00007ffff6ee2e9f libQt5Widgets.so.5`___lldb_unnamed_symbol1621$$libQt5Widgets.so.5 + 79
    frame #58: 0x00007ffff6ee59ef libQt5Widgets.so.5`___lldb_unnamed_symbol1633$$libQt5Widgets.so.5 + 463
    frame #59: 0x00007ffff6ee5c1a libQt5Widgets.so.5`___lldb_unnamed_symbol1635$$libQt5Widgets.so.5 + 74
    frame #60: 0x00007ffff6337790 libQt5Core.so.5`___lldb_unnamed_symbol4768$$libQt5Core.so.5 + 1376
    frame #61: 0x00007ffff6ee0853 libQt5Widgets.so.5`QComboBoxPrivateContainer::itemSelected(QModelIndex const&amp;) + 51
    frame #62: 0x00007ffff6ee0df8 libQt5Widgets.so.5`QComboBoxPrivateContainer::eventFilter(QObject*, QEvent*) + 344
    frame #63: 0x00007ffff6300102 libQt5Core.so.5`QCoreApplicationPrivate::sendThroughObjectEventFilters(QObject*, QEvent*) + 162
    frame #64: 0x00007ffff6dd6d51 libQt5Widgets.so.5`QApplicationPrivate::notify_helper(QObject*, QEvent*) + 113
    frame #65: 0x00007ffff6ddec07 libQt5Widgets.so.5`QApplication::notify(QObject*, QEvent*) + 3047
    frame #66: 0x00007ffff7c8ce0e libqSlicerBaseQTGUI.so`qSlicerApplication::notify(QObject*, QEvent*) + 30
    frame #67: 0x00007ffff63003aa libQt5Core.so.5`QCoreApplication::notifyInternal2(QObject*, QEvent*) + 314
    frame #68: 0x00007ffff7a5d1c4 libqMRMLWidgets.so`qMRMLNodeComboBox::setCurrentNodeID(QString const&amp;) + 500
    frame #69: 0x00007ffff7a5bc26 libqMRMLWidgets.so`qMRMLNodeComboBox::setCurrentNode(vtkMRMLNode*) + 198
    frame #70: 0x00007ffff7a5b8c1 libqMRMLWidgets.so`qMRMLNodeComboBox::addNode(QString) + 273
    frame #71: 0x00007ffff7a5a0fe libqMRMLWidgets.so`qMRMLNodeComboBox::activateExtraItem(QModelIndex const&amp;) + 1150
    frame #72: 0x00007ffff7aecfda libqMRMLWidgets.so`___lldb_unnamed_symbol188$$libqMRMLWidgets.so + 2330
    frame #73: 0x00007ffff6337790 libQt5Core.so.5`___lldb_unnamed_symbol4768$$libQt5Core.so.5 + 1376
    frame #74: 0x00007ffff7050db6 libQt5Widgets.so.5`QAbstractItemView::clicked(QModelIndex const&amp;) + 54
    frame #75: 0x00007ffff7054fad libQt5Widgets.so.5`QAbstractItemView::mouseReleaseEvent(QMouseEvent*) + 1261
    frame #76: 0x00007ffff709da10 libQt5Widgets.so.5`QListView::mouseReleaseEvent(QMouseEvent*) + 32
    frame #77: 0x00007ffff6e1a0be libQt5Widgets.so.5`QWidget::event(QEvent*) + 526
    frame #78: 0x00007ffff6ec984f libQt5Widgets.so.5`QFrame::event(QEvent*) + 31
    frame #79: 0x00007ffff6300102 libQt5Core.so.5`QCoreApplicationPrivate::sendThroughObjectEventFilters(QObject*, QEvent*) + 162
    frame #80: 0x00007ffff6dd6d51 libQt5Widgets.so.5`QApplicationPrivate::notify_helper(QObject*, QEvent*) + 113
    frame #81: 0x00007ffff6ddeac9 libQt5Widgets.so.5`QApplication::notify(QObject*, QEvent*) + 2729
    frame #82: 0x00007ffff7c8ce0e libqSlicerBaseQTGUI.so`qSlicerApplication::notify(QObject*, QEvent*) + 30
    frame #83: 0x00007ffff63003aa libQt5Core.so.5`QCoreApplication::notifyInternal2(QObject*, QEvent*) + 314
    frame #84: 0x00007ffff6ddd57b libQt5Widgets.so.5`QApplicationPrivate::sendMouseEvent(QWidget*, QMouseEvent*, QWidget*, QWidget*, QWidget**, QPointer&lt;QWidget&gt;&amp;, bool, bool) + 443
    frame #85: 0x00007ffff6e34593 libQt5Widgets.so.5`___lldb_unnamed_symbol921$$libQt5Widgets.so.5 + 3571
    frame #86: 0x00007ffff6e36db5 libQt5Widgets.so.5`___lldb_unnamed_symbol932$$libQt5Widgets.so.5 + 517
    frame #87: 0x00007ffff6dd6d62 libQt5Widgets.so.5`QApplicationPrivate::notify_helper(QObject*, QEvent*) + 130
    frame #88: 0x00007ffff7c8ce0e libqSlicerBaseQTGUI.so`qSlicerApplication::notify(QObject*, QEvent*) + 30
    frame #89: 0x00007ffff63003aa libQt5Core.so.5`QCoreApplication::notifyInternal2(QObject*, QEvent*) + 314
    frame #90: 0x00007ffff66d9210 libQt5Gui.so.5`QGuiApplicationPrivate::processMouseEvent(QWindowSystemInterfacePrivate::MouseEvent*) + 1712
    frame #91: 0x00007ffff66ae7e5 libQt5Gui.so.5`QWindowSystemInterface::sendWindowSystemEvents(QFlags&lt;QEventLoop::ProcessEventsFlag&gt;) + 181
    frame #92: 0x00007fffcdd8bfac libQt5XcbQpa.so.5`___lldb_unnamed_symbol407$$libQt5XcbQpa.so.5 + 28
    frame #93: 0x00007fffde8bd10c libglib-2.0.so.0`g_main_context_dispatch + 620
    frame #94: 0x00007fffde910b99 libglib-2.0.so.0`___lldb_unnamed_symbol449$$libglib-2.0.so.0 + 521
    frame #95: 0x00007fffde8ba871 libglib-2.0.so.0`g_main_context_iteration + 49
    frame #96: 0x00007ffff6358fd6 libQt5Core.so.5`QEventDispatcherGlib::processEvents(QFlags&lt;QEventLoop::ProcessEventsFlag&gt;) + 102
    frame #97: 0x00007ffff62fed1c libQt5Core.so.5`QEventLoop::exec(QFlags&lt;QEventLoop::ProcessEventsFlag&gt;) + 300
    frame #98: 0x00007ffff6307284 libQt5Core.so.5`QCoreApplication::exec() + 148
    frame #99: 0x00007ffff74d0916 libqSlicerBaseQTCore.so`qSlicerCoreApplication::exec() + 6
    frame #100: 0x000055555555996c SlicerApp-real`main + 524
    frame #101: 0x00007fffdf0f6b25 libc.so.6`__libc_start_main + 213
    frame #102: 0x000055555555968e SlicerApp-real`___lldb_unnamed_symbol3$$SlicerApp-real + 46
(lldb)
</code></pre>
<p>Hoping it helps for a fix.</p>
<p>Regards.</p>

---

## Post #2 by @lassoan (2021-07-07 23:46 UTC)

<p>Thanks for reporting. It seems that this problem was fixed in VTK. I could not reproduce it with a recent Slicer Preview Release.</p>

---
