# Performance issues on Mac M1?

**Topic ID**: 22564
**Date**: 2022-03-17
**URL**: https://discourse.slicer.org/t/performance-issues-on-mac-m1/22564

---

## Post #1 by @bpjohannessen (2022-03-17 15:30 UTC)

<p>Hello everybody.</p>
<p>I’m using 3D Slicer 4.11.20210226 (latest at time of writing) on my Windows PC without any performance issues, and I can segment CT scans (thorax, abdomen, wrists, etc) without any performance issues. Unfortunately I’m experiencing severe performance issues with the same version, and also 4.13.0-2022-03-15, on my MacBook Pro M1 (2020, 16 GB, macOS Monterey 12.3). I’m getting either a ever-lasting spinning beach ball or it crashes. I’ve tried it without any plugins.</p>
<p>To other Mac/M1 users, are you experiencing any of these issues, or is there some fix for it? I know Slicer is using 3rd party applications that (yet) is not ported to Apple Silicon, and if there are no known fixes I’ll continue working on a Windows PC.</p>
<p>In advance, thank you!<br>
Bjørn-Petter Johannessen MD/resident radiologist.</p>

---

## Post #2 by @jamesobutler (2022-03-17 15:31 UTC)

<aside class="quote no-group" data-username="bpjohannessen" data-post="1" data-topic="22564">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/9dc877/48.png" class="avatar"> bpjohannessen:</div>
<blockquote>
<p>I’m getting either a ever-lasting spinning beach ball or it crashes.</p>
</blockquote>
</aside>
<p>When does this happen? On startup? After doing certain actions in Slicer?</p>

---

## Post #3 by @bpjohannessen (2022-03-17 20:56 UTC)

<p>Thank you for your reply. I’m sorry I didn’t mention the important details…</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="2" data-topic="22564">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>When does this happen? On startup?</p>
</blockquote>
</aside>
<p>I haven’t encountered any problems on startup, loading DICOM files, thresholding, drawing, erasing, etc.</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="2" data-topic="22564">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>After doing certain actions in Slicer?</p>
</blockquote>
</aside>
<p>I’m encountering the issues when I’m scissoring while the 3D view is enabled. It doesn’t matter if I’m scissoring in the 3D view or in one of the 2D views (ax/cor/sag). Scissoring a smaller CT (e.g., wrist) is quicker than an abdominal CT, but the application hangs regardless. 100% CPU usage and ~3-4-5 GB of RAM. I still have free RAM, and I don’t think the hardware itself is problematic (except M1?).</p>
<p>I hope this helps. Please let me know if you need any other details. Thresholding, some basic drawing/erasing and scissoring is what I need.</p>

---

## Post #4 by @lassoan (2022-03-18 14:29 UTC)

<p>Does the slowdown occur when you release the mouse button after finishing drawing the curve?</p>
<p>How long do you have to wait after renewing the mouse button due the application to become responsive again?</p>
<p>Does the slowdown occur if you disable surface smoothing (in the dropdown menu of the “Show 3D” button)?</p>
<p>Note that after thresholding you can have tens of thousands of small speckles in the segmentation, which can drastically slow down 3D display and some processing. After thresholding it usually makes sense to use Smoothing effect with default parameters to reduce the amount of speckles and make the extracted surfaces smoother.</p>

---

## Post #5 by @sannpeterson (2022-08-04 01:26 UTC)

<p>I also posted about this same issue. Performance on my brand new Macbook Pro M1 is very unreliable. I’ve tried working with smaller areas but it doesn’t seem to matter much. Sometimes it runs smoothly but most of the time it’s painfully slow. I switched back over to windows just to use Slicer.</p>

---

## Post #6 by @lassoan (2022-08-04 05:57 UTC)

<p>I’ve submitted an issue to keep track of this:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/6490">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/6490" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/6490" target="_blank" rel="noopener">Slowdowns or hangs when running on ARM (M1) systems</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-08-04" data-time="05:47:24" data-timezone="UTC">05:47AM - 04 Aug 22 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          type:bug
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Summary

Two users reported slowdowns when using M1 mac systems:

&gt; I’m u<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">sing 3D Slicer 4.11.20210226 (latest at time of writing) on my Windows PC without any performance issues, and I can segment CT scans (thorax, abdomen, wrists, etc) without any performance issues. Unfortunately I’m experiencing severe performance issues with the same version, and also 4.13.0-2022-03-15, on my MacBook Pro M1 (2020, 16 GB, macOS Monterey 12.3). I’m getting either a ever-lasting spinning beach ball or it crashes. I’ve tried it without any plugins. 

https://discourse.slicer.org/t/performance-issues-on-mac-m1/22564

https://discourse.slicer.org/t/issues-running-slicer-on-macbook-m1-max/23974/3

## Environment

- MacBook Pro M1 (2020, 16 GB, macOS Monterey 12.3)
- MacBook M1 max</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Probably will have to buy a few M1 macs so that we can test this. But for that we would need to know which ones are problematic.</p>
<p><a class="mention" href="/u/sannpeterson">@sannpeterson</a> can you give more information about your system (model name and year, CPU, RAM, operating system)?</p>

---

## Post #7 by @sannpeterson (2022-08-07 00:52 UTC)

<p>Macbook Pro M1 Max (2021) w/ 10 core CPU and 32 core GPU<br>
32 GB memory<br>
1 TB SSD<br>
macOS Monterey 12.5</p>

---

## Post #8 by @bpjohannessen (2022-08-14 14:31 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="22564" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Does the slowdown occur when you release the mouse button after finishing drawing the curve?</p>
</blockquote>
</aside>
<p>Yes, when I release the mouse button.</p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="22564" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>How long do you have to wait after renewing the mouse button due the application to become responsive again?</p>
</blockquote>
</aside>
<p>Depends, sometimes it’s just “laggy” and a couple-10 seconds. Right now I’ve been waiting for 10 minutes after scissoring out parts of a kidney.</p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="22564" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Does the slowdown occur if you disable surface smoothing (in the dropdown menu of the “Show 3D” button)?</p>
</blockquote>
</aside>
<p>I haven’t been using a stopwatch, but it doesn’t seem to make a difference.</p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="22564" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Note that after thresholding you can have tens of thousands of small speckles in the segmentation, which can drastically slow down 3D display and some processing. After thresholding it usually makes sense to use Smoothing effect with default parameters to reduce the amount of speckles and make the extracted surfaces smoother.</p>
</blockquote>
</aside>
<p>I’ve tried with and without smoothing, but I can’t notice any significant difference.</p>
<p>Right now I’m segmenting a CT arteriography of aorta from a axial 3 mm scan with 241 slices, so it’s not a lot of data…</p>
<p>MacBook Pro 13 M1, 2020<br>
16 GB memory.<br>
Fresh install of macOS 12.4. I’ve been using Slicer 3D version 4.x and now 5.0.3 and I can’t tell any difference in the performance.<br>
Still works great on Windows.</p>
<p>(Sorry for the late reply - I thought I had replied to this)</p>

---

## Post #9 by @Iris_M (2022-09-18 09:59 UTC)

<p>Hi, I am also experiencing issues with Slicer (v. 5.0.3.) when working in the Segmentation editor. It crashes constantly when using the scissor to cut off segmentation results.</p>
<p>MacBook Pro (13-inch, M2, 2022)<br>
Monterey v 12.5.1</p>

---

## Post #10 by @semredogan (2022-11-09 12:34 UTC)

<p>I have multiple problems regarding segmentation on CT images (Maxillofacial ones don’t differ much from others but anyways). Especially when I’m trying to use “Scissors”, “Watershed” tools.<br>
The process usually goes like this:<br>
-I import the CT data<br>
-I add new segmentations to segment the cortical part of the mandible and the teeth. I used the method mentioned in this forum<br>
-I use “grow from seeds” tool which typically results in mixed segmentations since the tissues do not differ from each other so much in terms of calcification<br>
-I use “scissors” or “paintbrush” tool to fix the flooded/extra/unnecessary parts, then BOOM.<br>
The app crashes, and all my efforts are gone</p>

---

## Post #11 by @pieper (2022-11-09 13:31 UTC)

<p>Thanks for reporting.  There does seem to be some instability on macs with Apple chips.  I have run some simple tests and things run fine, but we have seen <a href="https://github.com/pieper/SlicerParallelProcessing/commit/2cf7d7d61e7b17cc949cb8fd31acefe9e4de25a1">previous issues</a> indicating that the on-the-fly run time code conversion is not the same as running on native hardware.  So until Apple fixes their emulation layer or Slicer is ported to the new architecture there are likely to be edge cases that fail.</p>
<p>I tested the basic flow described by <a class="mention" href="/u/semredogan">@semredogan</a> and got the crash report below basically instantly when using the scissors on my first try.  Later attempts to do the same thing did not crash.  I’ve never seen this on non-Apple CPUs.</p>
<p>For now I’d say the best option is to save often or use a different computer for intensive work.</p>
<pre><code class="lang-auto">
Crashed Thread:        0  CrBrowserMain  Dispatch queue: com.apple.main-thread

Exception Type:        EXC_BAD_ACCESS (SIGSEGV)
Exception Codes:       KERN_INVALID_ADDRESS at 0x0000000000000030
Exception Codes:       0x0000000000000001, 0x0000000000000030

Termination Reason:    Namespace SIGNAL, Code 11 Segmentation fault: 11
Terminating Process:   exc handler [6040]

VM Region Info: 0x30 is not in any region.  Bytes before following region: 140722657165264
      REGION TYPE                    START - END         [ VSIZE] PRT/MAX SHRMOD  REGION DETAIL
      UNUSED SPACE AT START
---&gt;  
      mapped file              7ffc8bfe0000-7ffc92e98000 [110.7M] r-x/r-x SM=COW  ...t_id=cbf25fb1

Error Formulating Crash Report:
dyld_process_snapshot_create_for_process failed with 5

Kernel Triage:
VM - pmap_enter retried due to resource shortage
VM - pmap_enter retried due to resource shortage


Thread 0 Crashed:: CrBrowserMain Dispatch queue: com.apple.main-thread
0   &lt;translation info unavailable&gt;	       0x10493f43c ???
1   &lt;translation info unavailable&gt;	       0x10493ea4c ???
2   libvtkCommon-9.1.1.dylib      	       0x143fb9cc0 vtkPolyData::BuildLinks(int) + 160
3   libvtkFilters-9.1.1.dylib     	       0x1407a356e vtkPolyDataNormals::RequestData(vtkInformation*, vtkInformationVector**, vtkInformationVector*) + 1614
4   libvtkCommon-9.1.1.dylib      	       0x143d9ab15 vtkExecutive::CallAlgorithm(vtkInformation*, int, vtkInformationVector**, vtkInformationVector*) + 69
5   libvtkCommon-9.1.1.dylib      	       0x143d9585d vtkDemandDrivenPipeline::ExecuteData(vtkInformation*, vtkInformationVector**, vtkInformationVector*) + 61
6   libvtkCommon-9.1.1.dylib      	       0x143d8fc98 vtkCompositeDataPipeline::ExecuteData(vtkInformation*, vtkInformationVector**, vtkInformationVector*) + 104
7   libvtkCommon-9.1.1.dylib      	       0x143d9501d vtkDemandDrivenPipeline::ProcessRequest(vtkInformation*, vtkInformationVector**, vtkInformationVector*) + 1437
8   libvtkCommon-9.1.1.dylib      	       0x143dd9930 vtkStreamingDemandDrivenPipeline::ProcessRequest(vtkInformation*, vtkInformationVector**, vtkInformationVector*) + 848
9   libvtkCommon-9.1.1.dylib      	       0x143d90f39 vtkCompositeDataPipeline::ForwardUpstream(vtkInformation*) + 297
10  libvtkCommon-9.1.1.dylib      	       0x143d94e3d vtkDemandDrivenPipeline::ProcessRequest(vtkInformation*, vtkInformationVector**, vtkInformationVector*) + 957
11  libvtkCommon-9.1.1.dylib      	       0x143dd9930 vtkStreamingDemandDrivenPipeline::ProcessRequest(vtkInformation*, vtkInformationVector**, vtkInformationVector*) + 848
12  libvtkCommon-9.1.1.dylib      	       0x143dd9f2b vtkStreamingDemandDrivenPipeline::Update(int, vtkInformationVector*) + 283
13  libqSlicerSegmentationsEditorEffects.dylib	       0x18289cc5b qSlicerSegmentEditorScissorsEffectPrivate::updateBrushStencil(qMRMLWidget*) + 203
14  libqSlicerSegmentationsEditorEffects.dylib	       0x18289cfb9 qSlicerSegmentEditorScissorsEffectPrivate::paintApply(qMRMLWidget*) + 137
15  libqSlicerSegmentationsEditorEffects.dylib	       0x1828a0d30 qSlicerSegmentEditorScissorsEffect::processInteractionEvents(vtkRenderWindowInteractor*, unsigned long, qMRMLWidget*) + 448
16  libqSlicerSegmentationsModuleWidgets.dylib	       0x18271302b qMRMLSegmentEditorWidget::processEvents(vtkObject*, unsigned long, void*, void*) + 619
17  libvtkCommon-9.1.1.dylib      	       0x14457b351 vtkCallbackCommand::Execute(vtkObject*, unsigned long, void*) + 33
18  libvtkCommon-9.1.1.dylib      	       0x14468f330 vtkSubjectHelper::InvokeEvent(unsigned long, void*, vtkObject*) + 1200
19  libvtkGUISupportQt-9.1.1.dylib	       0x1360218cb QVTKInteractorAdapter::ProcessEvent(QEvent*, vtkRenderWindowInteractor*) + 2171
20  libvtkGUISupportQt-9.1.1.dylib	       0x136023cae QVTKOpenGLNativeWidget::event(QEvent*) + 30
21  QtWidgets                     	       0x10e9c0a1a QApplicationPrivate::notify_helper(QObject*, QEvent*) + 266
22  QtWidgets                     	       0x10e9c3785 QApplication::notify(QObject*, QEvent*) + 6965
23  libqSlicerBaseQTGUI.dylib     	       0x10d0aaf20 qSlicerApplication::notify(QObject*, QEvent*) + 16
24  QtCore                        	       0x1114939d4 QCoreApplication::notifyInternal2(QObject*, QEvent*) + 212
25  QtWidgets                     	       0x10e9c1340 QApplicationPrivate::sendMouseEvent(QWidget*, QMouseEvent*, QWidget*, QWidget*, QWidget**, QPointer&lt;QWidget&gt;&amp;, bool, bool) + 896
26  QtWidgets                     	       0x10ea1a052 0x10e9b0000 + 434258
27  QtWidgets                     	       0x10ea18719 0x10e9b0000 + 427801
28  QtWidgets                     	       0x10e9c0a1a QApplicationPrivate::notify_helper(QObject*, QEvent*) + 266
29  QtWidgets                     	       0x10e9c1e41 QApplication::notify(QObject*, QEvent*) + 497
30  libqSlicerBaseQTGUI.dylib     	       0x10d0aaf20 qSlicerApplication::notify(QObject*, QEvent*) + 16
31  QtCore                        	       0x1114939d4 QCoreApplication::notifyInternal2(QObject*, QEvent*) + 212
32  QtGui                         	       0x10fdc11de QGuiApplicationPrivate::processMouseEvent(QWindowSystemInterfacePrivate::MouseEvent*) + 3534
33  QtGui                         	       0x10fda612b QWindowSystemInterface::sendWindowSystemEvents(QFlags&lt;QEventLoop::ProcessEventsFlag&gt;) + 219
34  libqcocoa.dylib               	       0x143123260 0x1430e9000 + 238176
35  libqcocoa.dylib               	       0x1431239c8 0x1430e9000 + 240072
36  CoreFoundation                	    0x7ff80289def1 __CFRUNLOOP_IS_CALLING_OUT_TO_A_SOURCE0_PERFORM_FUNCTION__ + 17
37  CoreFoundation                	    0x7ff80289dea0 __CFRunLoopDoSource0 + 157
38  CoreFoundation                	    0x7ff80289dc6e __CFRunLoopDoSources0 + 212
39  CoreFoundation                	    0x7ff80289c8c8 __CFRunLoopRun + 943
40  CoreFoundation                	    0x7ff80289be9f CFRunLoopRunSpecific + 560
41  HIToolbox                     	    0x7ff80c6c3bd6 RunCurrentEventLoopInMode + 292
42  HIToolbox                     	    0x7ff80c6c3806 ReceiveNextEventCommon + 199
43  HIToolbox                     	    0x7ff80c6c3723 _BlockUntilNextEventMatchingListInModeWithFilter + 70
44  AppKit                        	    0x7ff8058f9b37 _DPSNextEvent + 909
45  AppKit                        	    0x7ff8058f89b8 -[NSApplication(NSEvent) _nextEventMatchingEventMask:untilDate:inMode:dequeue:] + 1219
46  AppKit                        	    0x7ff8058eaff3 -[NSApplication run] + 586
47  libqcocoa.dylib               	       0x14312262f 0x1430e9000 + 235055
48  QtCore                        	       0x11148fa6f QEventLoop::exec(QFlags&lt;QEventLoop::ProcessEventsFlag&gt;) + 431
49  QtCore                        	       0x111493fe2 QCoreApplication::exec() + 130
50  libqSlicerBaseQTCore.dylib    	       0x10e1cc1a9 qSlicerCoreApplication::exec() + 9
51  Slicer                        	       0x10432cae3 main + 483
52  dyld                          	       0x20460b310 start + 2432
</code></pre>

---

## Post #12 by @BoudAnt1 (2023-02-06 17:16 UTC)

<p>This is follow-up question that may not be perfect for a sub-thread, but here goes:<br>
• Has anyone had any difficulties with the new Mac M2 chip?<br>
• Is there a fix planned for the scissor issue raised in this thread?<br>
• More generally, is the Slicer group adapting their Mac OS build for the new chips, or is this +/- irrelevant?</p>
<p>Thank you.</p>

---

## Post #13 by @pieper (2023-02-06 17:23 UTC)

<p>I have done some testing and mostly running the intel binaries on the M2 mac air seems to work well.  I haven’t extensively tested the scissors though.</p>
<p>I also did a <a href="https://github.com/Slicer/Slicer/issues/5944#issuecomment-1328179343">preliminary build with some features disabled</a> and it works well.</p>
<p>Eventually yes, we do plan to support Apple silicon natively.  If anyone who wants to help sort out the remaining build issues it would be much appreciated.</p>

---

## Post #14 by @lassoan (2023-02-06 18:54 UTC)

<p>The scissors issue is fixed in recent Slicer Preview Releases. If you can still reproduce the problem then let me know (you can activate some debugging options that will help me figuring out the final fix).</p>

---
