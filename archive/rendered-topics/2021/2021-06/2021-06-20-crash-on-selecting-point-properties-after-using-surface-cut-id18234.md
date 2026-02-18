# Crash on selecting point properties after using Surface Cut

**Topic ID**: 18234
**Date**: 2021-06-20
**URL**: https://discourse.slicer.org/t/crash-on-selecting-point-properties-after-using-surface-cut/18234

---

## Post #1 by @chir.set (2021-06-20 10:45 UTC)

<p>Slicer built at 2946f735c6 with VTK8 on Arch Linux, with lldb version 12.0.0. gcc 11.1.0 is installed.</p>
<p>These patches are applied, else it won’t build with this gcc version:</p>
<pre><code class="lang-auto">diff --git a/Modules/Loadable/Segmentations/Logic/vtkImageGrowCutSegment.cxx b/Modules/Loadable/Segmentations/Logic/vtkImageGrowCutSegment.cxx
index b64a450bd..6996a3a58 100644
--- a/Modules/Loadable/Segmentations/Logic/vtkImageGrowCutSegment.cxx
+++ b/Modules/Loadable/Segmentations/Logic/vtkImageGrowCutSegment.cxx
@@ -13,6 +13,7 @@
 #include &lt;vtkTimerLog.h&gt;
 
 #include "FibHeap.h"
+#include &lt;limits&gt;
 
 vtkStandardNewMacro(vtkImageGrowCutSegment);
 
 
diff --git a/Modules/ThirdParty/GDCM/src/gdcm/Source/MediaStorageAndFileFormat/gdcmImageChangePhotometricInterpretation.h b/Modules/ThirdParty/GDCM/src/gdcm/Source/MediaStorageAndFileFormat/gdcmImageChangePhotometricInterpretation.h
index d55a5ee473..798d3dfa6a 100644
--- a/Modules/ThirdParty/GDCM/src/gdcm/Source/MediaStorageAndFileFormat/gdcmImageChangePhotometricInterpretation.h
+++ b/Modules/ThirdParty/GDCM/src/gdcm/Source/MediaStorageAndFileFormat/gdcmImageChangePhotometricInterpretation.h
@@ -16,6 +16,7 @@
 
 #include "gdcmImageToImageFilter.h"
 #include "gdcmPhotometricInterpretation.h"
+#include &lt;limits&gt;
 
 namespace gdcm
 {
</code></pre>
<p>Steps to reproduce :</p>
<p>Load CTA-cardio<br>
Switch to Segment Editor<br>
Select Surface Cut<br>
Place a few points in the three usual slice views<br>
Right click once to end point placement<br>
Right click a second time at the same location to dismiss the slice view’s context menu<br>
Move a few fiducial points<br>
Right click on a fiducial point<br>
Select Properties → crash</p>
<pre><code class="lang-auto">error: libstdc++.so.6 {0x00181389}: DIE has DW_AT_ranges(0x119c8) attribute, but range extraction failed (missing or invalid range list table), please file a bug and attach the file at the start of this error message
Process 286812 stopped
* thread #1, name = 'SlicerApp-real', stop reason = signal SIGSEGV: invalid address (fault address: 0x0)
    frame #0: 0x00007fffe10eebff libvtkCommon-8.2.so.1`vtkSubjectHelper::InvokeEvent(this=0x000055555db699e0, event=16100, callData=0x000055555e53d390, self=0x000055555c7c4900) at vtkObject.cxx:602:18
(lldb) bt
* thread #1, name = 'SlicerApp-real', stop reason = signal SIGSEGV: invalid address (fault address: 0x0)
  * frame #0: 0x00007fffe10eebff libvtkCommon-8.2.so.1`vtkSubjectHelper::InvokeEvent(this=0x000055555db699e0, event=16100, callData=0x000055555e53d390, self=0x000055555c7c4900) at vtkObject.cxx:602:18
    frame #1: 0x00007fff79ee0862 libvtkSlicerMarkupsModuleVTKWidgets.so`vtkSlicerMarkupsWidget::ProcessWidgetMenu(this=0x000055555e271f70, eventData=0x000055555e45d2e0) at vtkSlicerMarkupsWidget.cxx:659:23
    frame #2: 0x00007fff79f3d179 libvtkSlicerMarkupsModuleMRMLDisplayableManager.so`vtkMRMLMarkupsDisplayableManager::ProcessInteractionEvent(this=&lt;unavailable&gt;, eventData=0x000055555e45d2e0) at vtkMRMLMarkupsDisplayableManager.cxx:755:24
    frame #3: 0x00007fffed2b2489 libMRMLDisplayableManager.so`vtkMRMLViewInteractorStyle::DelegateInteractionEventDataToDisplayableManagers(this=0x00005555583a5e10, eventData=0x000055555e45d2e0) at vtkMRMLViewInteractorStyle.cxx:408:53
    frame #4: 0x00007fffed2b3213 libMRMLDisplayableManager.so`vtkMRMLSliceViewInteractorStyle::DelegateInteractionEventToDisplayableManagers(this=0x00005555583a5e10, inputEventData=0x000055555e735160) at vtkMRMLSliceViewInteractorStyle.cxx:148:23
    frame #5: 0x00007fffed2b20bc libMRMLDisplayableManager.so`vtkMRMLViewInteractorStyle::DelegateInteractionEventToDisplayableManagers(this=0x00005555583a5e10, event=&lt;unavailable&gt;) at vtkMRMLViewInteractorStyle.cxx:300:16
    frame #6: 0x00007fffe0f8f26c libvtkCommon-8.2.so.1`vtkCallbackCommand::Execute(this=0x00005555583a6820, caller=&lt;unavailable&gt;, event=&lt;unavailable&gt;, callData=&lt;unavailable&gt;) at vtkCallbackCommand.cxx:42:5
    frame #7: 0x00007fffe10eee3b libvtkCommon-8.2.so.1`vtkSubjectHelper::InvokeEvent(this=0x00005555583af750, event=19, callData=0x00007fffffffb9e0, self=0x00005555581c5b30) at vtkObject.cxx:616:26
    frame #8: 0x00007fffe4c0e9e1 libvtkGUISupportQt-8.2.so.1`QVTKInteractorAdapter::ProcessEvent(this=&lt;unavailable&gt;, e=&lt;unavailable&gt;, iren=&lt;unavailable&gt;) at QVTKInteractorAdapter.cxx:0
    frame #9: 0x00007ffff6e2f0be libQt5Widgets.so.5`QWidget::event(QEvent*) + 526
    frame #10: 0x00007ffff6debd62 libQt5Widgets.so.5`QApplicationPrivate::notify_helper(QObject*, QEvent*) + 130
    frame #11: 0x00007ffff6df3ac9 libQt5Widgets.so.5`QApplication::notify(QObject*, QEvent*) + 2729
    frame #12: 0x00007ffff7c8fdfe libqSlicerBaseQTGUI.so`qSlicerApplication::notify(this=&lt;unavailable&gt;, receiver=&lt;unavailable&gt;, event=&lt;unavailable&gt;) at qSlicerApplication.cxx:411:26
    frame #13: 0x00007ffff631600a libQt5Core.so.5`QCoreApplication::notifyInternal2(QObject*, QEvent*) + 314
    frame #14: 0x00007ffff6df257b libQt5Widgets.so.5`QApplicationPrivate::sendMouseEvent(QWidget*, QMouseEvent*, QWidget*, QWidget*, QWidget**, QPointer&lt;QWidget&gt;&amp;, bool, bool) + 443
    frame #15: 0x00007ffff6e48a84 libQt5Widgets.so.5`___lldb_unnamed_symbol921$$libQt5Widgets.so.5 + 740
    frame #16: 0x00007ffff6e4bdb5 libQt5Widgets.so.5`___lldb_unnamed_symbol932$$libQt5Widgets.so.5 + 517
    frame #17: 0x00007ffff6debd62 libQt5Widgets.so.5`QApplicationPrivate::notify_helper(QObject*, QEvent*) + 130
    frame #18: 0x00007ffff7c8fdfe libqSlicerBaseQTGUI.so`qSlicerApplication::notify(this=&lt;unavailable&gt;, receiver=&lt;unavailable&gt;, event=&lt;unavailable&gt;) at qSlicerApplication.cxx:411:26
    frame #19: 0x00007ffff631600a libQt5Core.so.5`QCoreApplication::notifyInternal2(QObject*, QEvent*) + 314
    frame #20: 0x00007ffff66ee210 libQt5Gui.so.5`QGuiApplicationPrivate::processMouseEvent(QWindowSystemInterfacePrivate::MouseEvent*) + 1712
    frame #21: 0x00007ffff66c37e5 libQt5Gui.so.5`QWindowSystemInterface::sendWindowSystemEvents(QFlags&lt;QEventLoop::ProcessEventsFlag&gt;) + 181
    frame #22: 0x00007fffce39efbc libQt5XcbQpa.so.5`___lldb_unnamed_symbol407$$libQt5XcbQpa.so.5 + 28
    frame #23: 0x00007fffdeed010c libglib-2.0.so.0`g_main_context_dispatch + 620
    frame #24: 0x00007fffdef23b99 libglib-2.0.so.0`___lldb_unnamed_symbol449$$libglib-2.0.so.0 + 521
    frame #25: 0x00007fffdeecd871 libglib-2.0.so.0`g_main_context_iteration + 49
    frame #26: 0x00007ffff636ec36 libQt5Core.so.5`QEventDispatcherGlib::processEvents(QFlags&lt;QEventLoop::ProcessEventsFlag&gt;) + 102
    frame #27: 0x00007ffff631497c libQt5Core.so.5`QEventLoop::exec(QFlags&lt;QEventLoop::ProcessEventsFlag&gt;) + 300
    frame #28: 0x00007ffff631cee4 libQt5Core.so.5`QCoreApplication::exec() + 148
    frame #29: 0x00007ffff74e4226 libqSlicerBaseQTCore.so`qSlicerCoreApplication::exec() at qSlicerCoreApplication.cxx:861:19
    frame #30: 0x000055555555996c SlicerApp-real`main [inlined] (anonymous namespace)::SlicerAppMain(argc=1, argv=0x00007fffffffc238) at Main.cxx:62:10
    frame #31: 0x0000555555559781 SlicerApp-real`main(argc=&lt;unavailable&gt;, argv=0x00007fffffffc238) at qSlicerApplicationMainWrapper.cxx:56
    frame #32: 0x00007fffdf707b25 libc.so.6`__libc_start_main + 213
    frame #33: 0x000055555555968e SlicerApp-real`_start + 46
(lldb)
</code></pre>
<p>I hope it may help for a fix.</p>
<p>Regards.</p>

---

## Post #2 by @lassoan (2021-06-20 13:26 UTC)

<p>Thanks for reporting this, I’ll fix it tomorrow.</p>

---

## Post #3 by @lassoan (2021-06-21 18:42 UTC)

<p>A fix is implemented and under review. You can follow the progress here:</p>
<aside class="onebox githubpullrequest">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/5704" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/pull/5704" target="_blank" rel="noopener">Fix markups edit properties</a>
    </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>lassoan:fix-markups-edit-properties</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-06-21" data-time="18:36:21" data-timezone="UTC">06:36PM - 21 Jun 21 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>

      <div class="lines" title="2 commits changed 11 files with 130 additions and 73 deletions">
        <a href="https://github.com/Slicer/Slicer/pull/5704/files" target="_blank" rel="noopener">
          <span class="added">+130</span>
          <span class="removed">-73</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Fixes https://discourse.slicer.org/t/crash-on-selecting-point-properties-after-u<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/5704" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">sing-surface-cut/18234/2</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @chir.set (2021-06-25 09:43 UTC)

<p>Thanks for the fix. However, a reproducible crash persists with Surface Cut :</p>
<p>Place some points<br>
Apply<br>
Edit<br>
Right click on a point<br>
Edit properties → crash</p>
<p>(The backtrace is posted as a screen capture because my console app has gone nuts, can’t copy)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cdf4be96cd47a5232e7bd385038b2c0171bb01a1.png" data-download-href="/uploads/short-url/tnYf8hAtyFSZ5HlUN1l6LnN8CKR.png?dl=1" title="Screenshot_20210625_113842" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cdf4be96cd47a5232e7bd385038b2c0171bb01a1_2_631x500.png" alt="Screenshot_20210625_113842" data-base62-sha1="tnYf8hAtyFSZ5HlUN1l6LnN8CKR" width="631" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cdf4be96cd47a5232e7bd385038b2c0171bb01a1_2_631x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cdf4be96cd47a5232e7bd385038b2c0171bb01a1_2_946x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cdf4be96cd47a5232e7bd385038b2c0171bb01a1_2_1262x1000.png 2x" data-dominant-color="081508"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_20210625_113842</span><span class="informations">1542×1220 337 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The right click management is OK now, no double action.</p>

---

## Post #5 by @lassoan (2021-06-25 12:39 UTC)

<p>“Edit properties” option would indeed crash the application (because the effect deletes the temporary markup node while processing the event callbacks from that markup node), but the option is no longer visible on the context menu. What Slicer version do you use?</p>

---

## Post #6 by @chir.set (2021-06-25 13:12 UTC)

<p>4.13.0-2021-06-24 r30000 / 2c3bbb7ddbd</p>
<p>which includes f9f11666e8.</p>
<p>Sometimes it shows the Markups module with an empty list, sometimes it crashes. But the menu item is always present.</p>

---

## Post #7 by @lassoan (2021-06-25 20:00 UTC)

<p>I’ve forgot to push the corresponding change in SegmentEditorExtraEffects extension. It’ll work well in tomorrow’s Slicer Preview Release.</p>

---

## Post #8 by @chir.set (2021-06-28 09:45 UTC)

<p>It’s OK now, the Edit Properties menu item no longer appears. Thanks.</p>

---
