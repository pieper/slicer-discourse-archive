---
topic_id: 21389
title: "Volume Rendering Displaying Roi Leads To A Crash On Self Bui"
date: 2022-01-10
url: https://discourse.slicer.org/t/21389
---

# Volume Rendering : displaying ROI leads to a crash on self built Slicer

**Topic ID**: 21389
**Date**: 2022-01-10
**URL**: https://discourse.slicer.org/t/volume-rendering-displaying-roi-leads-to-a-crash-on-self-built-slicer/21389

---

## Post #1 by @chir.set (2022-01-10 16:42 UTC)

<p>My weekly Slicer build at 4f1e6145ca8 on Arch Linux crashes when showing the ROI in Volume rendering. Factory build Slicer at 4f1e6145ca8 (r30526) does not crash with the same steps. A clean build does not resolve the issue.</p>
<p>Building with GCC 11.1 or clang 13.0 gives the same results. Using cmake 3.22.1.</p>
<p>Volume Rendering now uses a markups ROI node instead of an annotation ROI. It’s OK in factory build, so there should be some problem here, and I don’t have any clue.</p>
<p>I wish someone could give me some hints for a solution.</p>
<p>Thanks.</p>
<hr>
<p>This backtrace could be obtained :</p>
<pre><code class="lang-auto">"Volume" Reader has successfully read the file "/home/user/tmp/Slicer/CTA-cardio.nrrd" "[0.70s]"
Switch to module:  "VolumeRendering"
void qSlicerVolumeRenderingModuleWidget::onEffectiveRangeModified() : Invalid volume property node
error: libgcc_s.so.1 {0x00011591}: DIE has DW_AT_ranges(DW_FORM_sec_offset 0x1ecb) attribute, but range extraction failed (invalid range list offset 0x1ecb), please file a bug and attach the file at the start of this error message
error: libgcc_s.so.1 {0x000117df}: DIE has DW_AT_ranges(DW_FORM_sec_offset 0x1ea5) attribute, but range extraction failed (invalid range list offset 0x1ea5), please file a bug and attach the file at the start of this error message
error: libgcc_s.so.1 {0x00011a02}: DIE has DW_AT_ranges(DW_FORM_sec_offset 0x1e5f) attribute, but range extraction failed (invalid range list offset 0x1e5f), please file a bug and attach the file at the start of this error message
error: libgcc_s.so.1 {0x00011dec}: DIE has DW_AT_ranges(DW_FORM_sec_offset 0x1c9d) attribute, but range extraction failed (invalid range list offset 0x1c9d), please file a bug and attach the file at the start of this error message
error: libgcc_s.so.1 {0x000120c4}: DIE has DW_AT_ranges(DW_FORM_sec_offset 0x1d24) attribute, but range extraction failed (invalid range list offset 0x1d24), please file a bug and attach the file at the start of this error message
error: libgcc_s.so.1 {0x0001247b}: DIE has DW_AT_ranges(DW_FORM_sec_offset 0x1c42) attribute, but range extraction failed (invalid range list offset 0x1c42), please file a bug and attach the file at the start of this error message
error: libgcc_s.so.1 {0x00012736}: DIE has DW_AT_ranges(DW_FORM_sec_offset 0x171d) attribute, but range extraction failed (invalid range list offset 0x171d), please file a bug and attach the file at the start of this error message
error: libgcc_s.so.1 {0x00012aca}: DIE has DW_AT_ranges(DW_FORM_sec_offset 0x1bdb) attribute, but range extraction failed (invalid range list offset 0x1bdb), please file a bug and attach the file at the start of this error message
error: libgcc_s.so.1 {0x00012d9c}: DIE has DW_AT_ranges(DW_FORM_sec_offset 0x1ace) attribute, but range extraction failed (invalid range list offset 0x1ace), please file a bug and attach the file at the start of this error message
error: libgcc_s.so.1 {0x00013746}: DIE has DW_AT_ranges(DW_FORM_sec_offset 0x1913) attribute, but range extraction failed (invalid range list offset 0x1913), please file a bug and attach the file at the start of this error message
error: libgcc_s.so.1 {0x00013ce3}: DIE has DW_AT_ranges(DW_FORM_sec_offset 0x1827) attribute, but range extraction failed (invalid range list offset 0x1827), please file a bug and attach the file at the start of this error message
error: libgcc_s.so.1 {0x00014968}: DIE has DW_AT_ranges(DW_FORM_sec_offset 0x1a18) attribute, but range extraction failed (invalid range list offset 0x1a18), please file a bug and attach the file at the start of this error message
error: libgcc_s.so.1 {0x00015764}: DIE has DW_AT_ranges(DW_FORM_sec_offset 0x17b2) attribute, but range extraction failed (invalid range list offset 0x17b2), please file a bug and attach the file at the start of this error message
error: libgcc_s.so.1 {0x00015b63}: DIE has DW_AT_ranges(DW_FORM_sec_offset 0x17c7) attribute, but range extraction failed (invalid range list offset 0x17c7), please file a bug and attach the file at the start of this error message
error: libgcc_s.so.1 {0x00015f9b}: DIE has DW_AT_ranges(DW_FORM_sec_offset 0x179d) attribute, but range extraction failed (invalid range list offset 0x179d), please file a bug and attach the file at the start of this error message
error: libstdc++.so.6 {0x00181389}: DIE has DW_AT_ranges(DW_FORM_sec_offset 0x119c8) attribute, but range extraction failed (invalid range list offset 0x119c8), please file a bug and attach the file at the start of this error message
Process 589921 stopped
* thread #1, name = 'SlicerApp-real', stop reason = signal SIGSEGV: invalid address (fault address: 0x0)
    frame #0: 0x00007fffe1b63933 libgcc_s.so.1`_Unwind_Resume at unwind.inc:240:6
(lldb) bt
* thread #1, name = 'SlicerApp-real', stop reason = signal SIGSEGV: invalid address (fault address: 0x0)
  * frame #0: 0x00007fffe1b63933 libgcc_s.so.1`_Unwind_Resume at unwind.inc:240:6
    frame #1: 0x00007ffe68de8b4e libvtkSlicerVolumeRenderingModuleLogic.so`vtkSlicerVolumeRenderingLogic::CreateROINode(this=0xd7c86d1111dc2c00, displayNode=0x000055555ca7e370) at new_allocator.h:0:2
    frame #2: 0x00007ffe68e2f017 libqSlicerVolumeRenderingModuleWidgets.so`qSlicerVolumeRenderingModuleWidget::onROICropDisplayCheckBoxToggled(this=&lt;unavailable&gt;, toggle=true) at qSlicerVolumeRenderingModuleWidget.cxx:842:14
    frame #3: 0x00007ffff64e0c4f libQt5Core.so.5`___lldb_unnamed_symbol10834 + 1391
    frame #4: 0x00007ffff7007bc7 libQt5Widgets.so.5`QAbstractButton::toggled(bool) + 71
    frame #5: 0x00007ffff700d6c7 libQt5Widgets.so.5`QAbstractButton::setChecked(bool) + 247
    frame #6: 0x00007ffff701df2e libQt5Widgets.so.5`QCheckBox::nextCheckState() + 78
    frame #7: 0x00007ffff700d15d libQt5Widgets.so.5`___lldb_unnamed_symbol12645 + 77
    frame #8: 0x00007ffff700d388 libQt5Widgets.so.5`QAbstractButton::mouseReleaseEvent(QMouseEvent*) + 184
    frame #9: 0x00007ffff6f59646 libQt5Widgets.so.5`QWidget::event(QEvent*) + 2198
    frame #10: 0x00007ffff6f231a6 libQt5Widgets.so.5`QApplicationPrivate::notify_helper(QObject*, QEvent*) + 134
    frame #11: 0x00007ffff6f27fd7 libQt5Widgets.so.5`QApplication::notify(QObject*, QEvent*) + 2919
    frame #12: 0x00007ffff7c9ac82 libqSlicerBaseQTGUI.so`qSlicerApplication::notify(this=&lt;unavailable&gt;, receiver=&lt;unavailable&gt;, event=&lt;unavailable&gt;) at qSlicerApplication.cxx:412:26
    frame #13: 0x00007ffff64b008a libQt5Core.so.5`QCoreApplication::notifyInternal2(QObject*, QEvent*) + 314
    frame #14: 0x00007ffff6f2699f libQt5Widgets.so.5`QApplicationPrivate::sendMouseEvent(QWidget*, QMouseEvent*, QWidget*, QWidget*, QWidget**, QPointer&lt;QWidget&gt;&amp;, bool, bool) + 447
    frame #15: 0x00007ffff6f77837 libQt5Widgets.so.5`___lldb_unnamed_symbol12244 + 743
    frame #16: 0x00007ffff6f793dc libQt5Widgets.so.5`___lldb_unnamed_symbol12248 + 572
    frame #17: 0x00007ffff6f231a6 libQt5Widgets.so.5`QApplicationPrivate::notify_helper(QObject*, QEvent*) + 134
    frame #18: 0x00007ffff7c9ac82 libqSlicerBaseQTGUI.so`qSlicerApplication::notify(this=&lt;unavailable&gt;, receiver=&lt;unavailable&gt;, event=&lt;unavailable&gt;) at qSlicerApplication.cxx:412:26
    frame #19: 0x00007ffff64b008a libQt5Core.so.5`QCoreApplication::notifyInternal2(QObject*, QEvent*) + 314
    frame #20: 0x00007ffff687ff90 libQt5Gui.so.5`QGuiApplicationPrivate::processMouseEvent(QWindowSystemInterfacePrivate::MouseEvent*) + 1392
    frame #21: 0x00007ffff686b5e5 libQt5Gui.so.5`QWindowSystemInterface::sendWindowSystemEvents(QFlags&lt;QEventLoop::ProcessEventsFlag&gt;) + 181
    frame #22: 0x00007fffce7e2d70 libQt5XcbQpa.so.5`___lldb_unnamed_symbol2220 + 32
    frame #23: 0x00007fffe0fde52c libglib-2.0.so.0`g_main_context_dispatch + 620
    frame #24: 0x00007fffe10327b9 libglib-2.0.so.0`___lldb_unnamed_symbol2483 + 521
    frame #25: 0x00007fffe0fdbc11 libglib-2.0.so.0`g_main_context_iteration + 49
    frame #26: 0x00007ffff64fb2ba libQt5Core.so.5`QEventDispatcherGlib::processEvents(QFlags&lt;QEventLoop::ProcessEventsFlag&gt;) + 106
    frame #27: 0x00007ffff64a836b libQt5Core.so.5`QEventLoop::exec(QFlags&lt;QEventLoop::ProcessEventsFlag&gt;) + 299
    frame #28: 0x00007ffff64b3ab7 libQt5Core.so.5`QCoreApplication::exec() + 151
    frame #29: 0x00007ffff754f516 libqSlicerBaseQTCore.so`qSlicerCoreApplication::exec() at qSlicerCoreApplication.cxx:876:19
    frame #30: 0x000055555555998c SlicerApp-real`main [inlined] (anonymous namespace)::SlicerAppMain(argc=1, argv=0x00007fffffffc1e8) at Main.cxx:62:10
    frame #31: 0x00005555555597a1 SlicerApp-real`main(argc=&lt;unavailable&gt;, argv=0x00007fffffffc1e8) at qSlicerApplicationMainWrapper.cxx:56:10
    frame #32: 0x00007fffe19adb25 libc.so.6`__libc_start_main + 213
    frame #33: 0x00005555555596ae SlicerApp-real`_start + 46
(lldb)
</code></pre>

---

## Post #2 by @pieper (2022-01-10 20:15 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="1" data-topic="21389">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<pre><code class="lang-auto">void qSlicerVolumeRenderingModuleWidget::onEffectiveRangeModified() : Invalid volume property node
</code></pre>
</blockquote>
</aside>
<p>I also get this message on my local ubuntu 20.04 build but I don’t get the other messages or a crash.</p>
<aside class="quote no-group" data-username="chir.set" data-post="1" data-topic="21389">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<pre><code class="lang-auto">error: libgcc_s.so.1 {0x00011591}: DIE has DW_AT_ranges(DW_FORM_sec_offset 0x1ecb) attribute, but range extraction failed (invalid range list offset 0x1ecb), please file a bug and attach the file at the start of this error message
</code></pre>
</blockquote>
</aside>
<p>These messages make it look like a compiler or libgcc issue.  Not sure why it would show up in builds with two different compilers.  Perhaps it’s a system lib issue on that OS?</p>

---

## Post #3 by @chir.set (2022-01-11 11:25 UTC)

<p>This patch solves the problem :</p>
<pre><code class="lang-auto">diff --git a/Modules/Loadable/VolumeRendering/Logic/vtkSlicerVolumeRenderingLogic.cxx b/Modules/Loadable/VolumeRendering/Logic/vtkSlicerVolumeRenderingLogic.cxx
index 7ef9e92aa..2cb518512 100644
--- a/Modules/Loadable/VolumeRendering/Logic/vtkSlicerVolumeRenderingLogic.cxx
+++ b/Modules/Loadable/VolumeRendering/Logic/vtkSlicerVolumeRenderingLogic.cxx
@@ -1151,6 +1151,9 @@ vtkMRMLDisplayableNode* vtkSlicerVolumeRenderingLogic::CreateROINode(vtkMRMLVolu
     }
   displayNode-&gt;SetAndObserveROINodeID(roiNode-&gt;GetID());
   this-&gt;FitROIToVolume(displayNode);
+  return (markupsROINode
+        ? vtkMRMLDisplayableNode::SafeDownCast(markupsROINode)
+        : vtkMRMLDisplayableNode::SafeDownCast(annotationROINode));
 }
 
 //----------------------------------------------------------------------------
</code></pre>
<p>A non void function missed a return statement.</p>

---

## Post #4 by @chir.set (2022-01-12 09:51 UTC)

<p>This patch works too, and is simpler :</p>
<pre><code class="lang-auto">diff --git a/Modules/Loadable/VolumeRendering/Logic/vtkSlicerVolumeRenderingLogic.cxx b/Modules/Loadable/VolumeRendering/Logic/vtkSlicerVolumeRenderingLogic.cxx
index 7ef9e92aa..c96693e1a 100644
--- a/Modules/Loadable/VolumeRendering/Logic/vtkSlicerVolumeRenderingLogic.cxx
+++ b/Modules/Loadable/VolumeRendering/Logic/vtkSlicerVolumeRenderingLogic.cxx
@@ -1151,6 +1151,7 @@ vtkMRMLDisplayableNode* vtkSlicerVolumeRenderingLogic::CreateROINode(vtkMRMLVolu
     }
   displayNode-&gt;SetAndObserveROINodeID(roiNode-&gt;GetID());
   this-&gt;FitROIToVolume(displayNode);
+  return (displayNode-&gt;GetROINode());
 }
 
 //----------------------------------------------------------------------------
</code></pre>

---

## Post #5 by @pieper (2022-01-12 13:40 UTC)

<p>Nice - can you do a PR?</p>

---

## Post #6 by @chir.set (2022-01-12 14:37 UTC)

<aside class="quote no-group" data-username="pieper" data-post="5" data-topic="21389">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>can you do a PR?</p>
</blockquote>
</aside>
<p><a href="https://github.com/Slicer/Slicer/pull/6109" rel="noopener nofollow ugc">Here</a> it is.</p>
<p>Just for the sake of discussion, it’s hard to understand why Slicer does not crash in factory builds. Any ideas ?</p>

---

## Post #7 by @pieper (2022-01-12 15:09 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="6" data-topic="21389">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>Just for the sake of discussion, it’s hard to understand why Slicer does not crash in factory builds. Any ideas ?</p>
</blockquote>
</aside>
<p>Sounds like a boundary condition in a compiler optimization path.  There should have been a compiler warning about the missing return statement but maybe there wasn’t or the developer didn’t notice it.  Good example of why we need to pay attention to the warnings.</p>

---

## Post #8 by @chir.set (2022-01-12 15:32 UTC)

<aside class="quote no-group" data-username="pieper" data-post="7" data-topic="21389">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>There should have been a compiler warning about the missing return statement</p>
</blockquote>
</aside>
<p>In fact, it’s the compiler warning that prompted me to this. I initially got rid of all annotation ROI nodes in this file, then built Modules/Loadable section only, and that warning appeared. Reverted everything and fixed.</p>
<p>Anyway, good it’s over.</p>

---
