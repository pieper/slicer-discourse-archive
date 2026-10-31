---
topic_id: 48607
title: "Apple Silicon (arm64 macOS) application and extensions now available"
date: 2026-10-26
url: https://discourse.slicer.org/t/48607
last_bumped: 2026-10-30T11:52:45.950Z
---

# Apple Silicon (arm64 macOS) application and extensions now available

**Topic ID**: 48607
**Date**: 2026-10-26
**URL**: https://discourse.slicer.org/t/apple-silicon-arm64-macos-application-and-extensions-now-available/48607

---

## Post #1 by @Sam_Horvath (2026-10-26 16:25 UTC)

<p>The Apple Silicon installer for 3D Slicer is now available for preview builds on <a href="https://download.slicer.org/">https://download.slicer.org/</a>. A stable arm64 package will be available in the next release.</p>
<p>Please give it a try and report any issues!</p>

---

## Post #2 by @Philipp_G (2026-10-27 20:34 UTC)

<p>I installed it on m1 mac mini macos 27.2, Rosetta installed. I as far as allowing the app to run through privacy settings, entering password, but after that the app crashes. launching again shows the splash screen, a couple of things load, then again crash. I useful I can post the crash report.</p>

---

## Post #3 by @Sam_Horvath (2026-10-27 20:57 UTC)

<p>Yes, please post the crash report.</p>

---

## Post #4 by @russellmiller49 (2026-10-28 02:48 UTC)

<p>I’m experiencing what appears to be the same issue with the new native Apple Silicon preview build.</p>
<p><strong>System:</strong></p>
<ul>
<li>
<p>3D Slicer: 5.13.0 (2026-10-26), ARM64 native</p>
</li>
<li>
<p>macOS: 27.2 (build 26B118)</p>
</li>
<li>
<p>Mac hardware identifier: Mac17,6</p>
</li>
<li>
<p>Bundled Qt version: 6.11.1</p>
</li>
</ul>
<p>Slicer displays its splash screen and begins loading, but crashes consistently before the main window appears.</p>
<p><strong>Crash report:</strong></p>
<ul>
<li>
<p>Exception: <code>EXC_BREAKPOINT (SIGTRAP)</code></p>
</li>
<li>
<p>Crashed thread: 0 (main thread)</p>
</li>
<li>
<p>Error: <code>pointer authentication trap DA</code></p>
</li>
</ul>
<p>Relevant stack trace:</p>
<pre><code class="lang-auto">CoreFoundation  __CF_IS_OBJC
CoreFoundation  CFGetTypeID
CoreGraphics   CGColorSpaceGetType
CoreGraphics   valid_image_colorspace
CoreGraphics   verify_image_parameters
CoreGraphics   CGImageCreate
QtGui          QImage::toCGImage()
QtGui          imageFromQIcon
libqcocoa      QCocoaMenuItem::sync()
QtWidgets      QMenu::actionEvent()
Slicer         qSlicerMainWindowPrivate::setupUi()
</code></pre>
<p>I investigated the crash and found that it closely matches <strong>QTBUG-147602</strong>, a use-after-free bug in Qt 6.11.1 affecting <code>QImage::toCGImage()</code> on macOS. The same failure has been reported in other Qt applications, including OBS Studio, on macOS 27.2.</p>
<p>The upstream Qt issue was reportedly fixed in Qt 6.11.2 and 6.12.0.</p>
<p>Since this Slicer preview bundles Qt 6.11.1, I suspect the same issue is responsible for the crash. Would it be possible to incorporate the upstream Qt fix or update the bundled Qt version in the next ARM64 preview?</p>
<p>I’ve attached my complete macOS crash report for reference as Gist here: <a href="https://gist.github.com/russellmiller49/f4c0d0871139561384afbc61828a5d0f#file-slicer-arm64-crash-2026-10-27" class="inline-onebox" rel="noopener nofollow ugc">slicer-arm64-crash-2026-10-27 · GitHub</a></p>
<p>Thanks for making the native Apple Silicon build available!</p>

---

## Post #5 by @Sam_Horvath (2026-10-28 12:32 UTC)

<p>Thanks for the detailed report! I will look into getting this sorted today.</p>

---

## Post #6 by @jamesobutler (2026-10-28 20:28 UTC)

<p>The Slicer arm64 build with Qt 6.11.1 did not have any issues for me when running macOS 27.0.1, but the same application version did crash during startup after I updated to macOS 27.2.</p>

---

## Post #7 by @Sam_Horvath (2026-10-28 20:44 UTC)

<p>So, the arm64 factory has been updated to 6.11.2.  Tomorrow’s installer should have the updated version</p>

---

## Post #8 by @jamesobutler (2026-10-29 14:02 UTC)

<p>The updated arm64 version with Qt 6.11.2 runs successfully on macOS 27.2 now.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/dee7ead808c74c5684a66523314aa64f66e9a7f4.png" data-download-href="/uploads/short-url/vNUSvdFa5Oad8XOarhMdFWwGtuc.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/dee7ead808c74c5684a66523314aa64f66e9a7f4_2_690x141.png" alt="image" data-base62-sha1="vNUSvdFa5Oad8XOarhMdFWwGtuc" width="690" height="141" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/dee7ead808c74c5684a66523314aa64f66e9a7f4_2_690x141.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/dee7ead808c74c5684a66523314aa64f66e9a7f4_2_1035x211.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/dee7ead808c74c5684a66523314aa64f66e9a7f4.png 2x" data-dominant-color="E1DFDF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1092×224 14.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @Philipp_G (2026-10-30 11:07 UTC)

<p>Hey Sam - sorry for the delay. unfortunately I can not send the full report due to character limit. I’ll send the first rows:</p>
<hr>
<h2><a name="p-136582-translated-report-full-report-below-1" class="anchor" href="#p-136582-translated-report-full-report-below-1" aria-label="Heading link"></a>Translated Report (Full Report Below)</h2>
<p>Process:             SlicerApp-real [7270]<br>
Path:                /Applications/3D Slicer ARM 5.13.0 2026-10-26.app/Contents/MacOS/SlicerApp-real<br>
Identifier:          SlicerApp-real<br>
Version:             ???<br>
Code Type:           ARM-64 (Native)<br>
Role:                Foreground<br>
Parent Process:      launchd [1]<br>
Coalition:           org.slicer.slicer [3167]<br>
User ID:             501</p>
<p>Date/Time:           2026-10-30 12:02:42.7233 +0100<br>
Launch Time:         2026-10-30 12:02:28.3114 +0100<br>
Hardware Model:      Macmini9,1<br>
OS Version:          macOS 27.2 (26B123)<br>
Release Type:        User</p>
<p>Crash Reporter Key:  42881F9D-E4C0-4874-D77B-71A85945A7F7<br>
Incident Identifier: 3C457067-C8FE-4177-A36C-E8C903A0C45F</p>
<p>Sleep/Wake UUID:       036AA30B-5CCF-4026-88C6-FF0C3BD5B942</p>
<p>Time Awake Since Boot: 91000 seconds<br>
Time Since Wake:       40 seconds</p>
<p>System Integrity Protection: enabled</p>
<p>Triggered by Thread: 0, Dispatch Queue: com.apple.main-thread</p>
<p>Exception Type:    EXC_BREAKPOINT (SIGTRAP)<br>
Exception Codes:   0x0000000000000001, 0x0000000194070294</p>
<p>Termination Reason:  Namespace SIGNAL, Code 5, Trace/BPT trap: 5<br>
Terminating Process: exc handler [7270]</p>
<p>Thread 0 Crashed::  Dispatch queue: com.apple.main-thread<br>
0   CoreFoundation                	       0x194070294 __CF_IS_OBJC + 52<br>
1   CoreFoundation                	       0x193f34dc8 CFGetTypeID + 180<br>
2   CoreGraphics                  	       0x191721950 CGColorSpaceGetType + 28<br>
3   CoreGraphics                  	       0x19174eb74 valid_image_colorspace + 32<br>
4   CoreGraphics                  	       0x1918be220 verify_image_parameters + 520<br>
5   CoreGraphics                  	       0x19174e8bc CGImageCreate + 136<br>
6   QtGui                         	       0x10f452758 QImage::toCGImage() const + 264<br>
7   QtGui                         	       0x10f453884 +[NSImage(QtExtras) imageFromQIcon:withSize:withMode:withState:] + 376<br>
8   libqcocoa.dylib               	       0x126d532dc QCocoaMenuItem::sync() + 2020<br>
9   libqcocoa.dylib               	       0x126d4c908 QCocoaMenu::insertMenuItem(QPlatformMenuItem*, QPlatformMenuItem*) + 72<br>
10  QtWidgets                     	       0x10e1828b8 QMenuPrivate::insertActionInPlatformMenu(QAction const*, QPlatformMenuItem*) + 352<br>
11  QtWidgets                     	       0x10e18fa34 QMenu::actionEvent(QActionEvent*) + 1204<br>
12  QtWidgets                     	       0x10e02eb9c QWidget::event(QEvent*) + 216<br>
13  QtWidgets                     	       0x10e18d75c QMenu::event(QEvent*) + 1172<br>
14  QtWidgets                     	       0x10dfe0acc QApplicationPrivate::notify_helper(QObject*, QEvent*) + 336<br>
15  QtWidgets                     	       0x10dfe1b4c QApplication::notify(QObject*, QEvent*) + 468<br>
16  libqSlicerBaseQTGUI.dylib     	       0x101457494 qSlicerApplication::notify(QObject*, QEvent*) + 24<br>
17  QtCore                        	       0x10faed2c8 QCoreApplication::sendEvent(QObject*, QEvent*) + 168<br>
18  QtWidgets                     	       0x10e021a38 QWidget::insertAction(QAction*, QAction*) + 352<br>
19  libqSlicerBaseQTApp.dylib     	       0x100f34a24 qSlicerMainWindowPrivate::setupUi(QMainWindow*) + 5140<br>
20  libqSlicerApp.dylib           	       0x100d338b8 qSlicerAppMainWindowPrivate::setupUi(QMainWindow*) + 2504<br>
21  libqSlicerBaseQTApp.dylib     	       0x100f33570 qSlicerMainWindowPrivate::init() + 40<br>
22  libqSlicerApp.dylib           	       0x100d34604 qSlicerAppMainWindow::qSlicerAppMainWindow(QWidget*) + 124<br>
23  SlicerApp-real                	       0x100bdc354 int qSlicerApplicationHelper::postInitializeApplication(qSlicerApplication&amp;, QScopedPointer&lt;QSplashScreen, QScopedPointerDeleter&gt;&amp;, QScopedPointer&lt;qSlicerAppMainWindow, QScopedPointerDeleter&gt;&amp;) + 4708<br>
24  SlicerApp-real                	       0x100bdae40 main + 152<br>
25  dyld                          	       0x18fcfcd7c start + 6652</p>
<p>Thread 1:</p>
<p>Thread 2:</p>
<p>Thread 3:</p>
<p>Thread 4:</p>
<p>Thread 5:</p>
<p>Thread 6:: com.apple.NSEventThread<br>
0   libsystem_kernel.dylib        	       0x18fd8bc20 mach_msg2_trap + 8<br>
1   libsystem_kernel.dylib        	       0x18fd9e8e0 mach_msg2_internal + 76<br>
2   libsystem_kernel.dylib        	       0x18fd94a28 mach_msg_overwrite + 480<br>
3   libsystem_kernel.dylib        	       0x18fd8bfac mach_msg + 24<br>
4   CoreFoundation                	       0x193f95ac8 __CFRunLoopServiceMachPort + 160<br>
5   CoreFoundation                	       0x193f94310 __CFRunLoopRun + 1172<br>
6   CoreFoundation                	       0x19406ec10 _CFRunLoopRunSpecificWithOptions + 536<br>
7   AppKit                        	       0x199d63554 _NSEventThread + 152<br>
8   libsystem_pthread.dylib       	       0x18fdd0ce4 _pthread_start + 136<br>
9   libsystem_pthread.dylib       	       0x18fdcbcd0 thread_start + 8</p>
<p>Thread 7:<br>
0   libsystem_kernel.dylib        	       0x18fd8f308 __semwait_signal + 8<br>
1   libsystem_c.dylib             	       0x18fdf7054 nanosleep + 220<br>
2   libsystem_c.dylib             	       0x18fdf6f6c usleep + 68<br>
3   libSlicerBaseLogic.dylib      	       0x102c64b50 vtkSlicerApplicationLogic::ProcessProcessingTasks() + 72<br>
4   libSlicerBaseLogic.dylib      	       0x102c6d308 void* std::__1::__thread_proxy[abi:ne200100]&lt;std::__1::tuple&lt;std::__1::unique_ptr&lt;std::__1::__thread_struct, std::__1::default_deletestd::__1::__thread_struct&gt;, void (<em>)(vtkSlicerApplicationLogic</em>), vtkSlicerApplicationLogic*&gt;&gt;(void*) + 52<br>
5   libsystem_pthread.dylib       	       0x18fdd0ce4 _pthread_start + 136<br>
6   libsystem_pthread.dylib       	       0x18fdcbcd0 thread_start + 8</p>
<p>Thread 8:<br>
0   libsystem_kernel.dylib        	       0x18fd8f308 __semwait_signal + 8<br>
1   libsystem_c.dylib             	       0x18fdf7054 nanosleep + 220<br>
2   libsystem_c.dylib             	       0x18fdf6f6c usleep + 68<br>
3   libSlicerBaseLogic.dylib      	       0x102c64d3c vtkSlicerApplicationLogic::ProcessNetworkingTasks() + 72<br>
4   libSlicerBaseLogic.dylib      	       0x102c6d308 void* std::__1::__thread_proxy[abi:ne200100]&lt;std::__1::tuple&lt;std::__1::unique_ptr&lt;std::__1::__thread_struct, std::__1::default_deletestd::__1::__thread_struct&gt;, void (<em>)(vtkSlicerApplicationLogic</em>), vtkSlicerApplicationLogic*&gt;&gt;(void*) + 52<br>
5   libsystem_pthread.dylib       	       0x18fdd0ce4 _pthread_start + 136<br>
6   libsystem_pthread.dylib       	       0x18fdcbcd0 thread_start + 8</p>
<p>Thread 9:: QNetworkAccessManager thread<br>
0   libsystem_kernel.dylib        	       0x18fd94760 poll + 8<br>
1   QtCore                        	       0x10fc98528 qt_safe_poll(pollfd*, unsigned int, QDeadlineTimer) + 76<br>
2   QtCore                        	       0x10fc9c5b8 QEventDispatcherUNIX::processEvents(QFlagsQEventLoop::ProcessEventsFlag) + 880<br>
3   QtCore                        	       0x10faf6588 QEventLoop::exec(QFlagsQEventLoop::ProcessEventsFlag) + 588<br>
4   QtCore                        	       0x10fbe9bb8 QThread::exec() + 348<br>
5   QtCore                        	       0x10fc99f84 QThreadPrivate::start(void*) + 392<br>
6   libsystem_pthread.dylib       	       0x18fdd0ce4 _pthread_start + 136<br>
7   libsystem_pthread.dylib       	       0x18fdcbcd0 thread_start + 8</p>
<p>Thread 10:: Thread (pooled)<br>
0   libsystem_kernel.dylib        	       0x18fd8f50c __psynch_cvwait + 8<br>
1   libsystem_pthread.dylib       	       0x18fdd11b4 _pthread_cond_wait + 980<br>
2   QtCore                        	       0x10fca2cd8 QWaitConditionPrivate::wait(QDeadlineTimer) + 236<br>
3   QtCore                        	       0x10fca2b84 QWaitCondition::wait(QMutex*, QDeadlineTimer) + 108<br>
4   QtCore                        	       0x10fbebe2c QThreadPoolThread::run() + 932<br>
5   QtCore                        	       0x10fc99f84 QThreadPrivate::start(void*) + 392<br>
6   libsystem_pthread.dylib       	       0x18fdd0ce4 _pthread_start + 136<br>
7   libsystem_pthread.dylib       	       0x18fdcbcd0 thread_start + 8</p>
<p>Thread 11:: QNetworkAccessManager thread<br>
0   libsystem_kernel.dylib        	       0x18fd94760 poll + 8<br>
1   QtCore                        	       0x10fc98594 qt_safe_poll(pollfd*, unsigned int, QDeadlineTimer) + 184<br>
2   QtCore                        	       0x10fc9c5b8 QEventDispatcherUNIX::processEvents(QFlagsQEventLoop::ProcessEventsFlag) + 880<br>
3   QtCore                        	       0x10faf6588 QEventLoop::exec(QFlagsQEventLoop::ProcessEventsFlag) + 588<br>
4   QtCore                        	       0x10fbe9bb8 QThread::exec() + 348<br>
5   QtCore                        	       0x10fc99f84 QThreadPrivate::start(void*) + 392<br>
6   libsystem_pthread.dylib       	       0x18fdd0ce4 _pthread_start + 136<br>
7   libsystem_pthread.dylib       	       0x18fdcbcd0 thread_start + 8</p>
<p>Thread 12:: Thread (pooled)<br>
0   libsystem_kernel.dylib        	       0x18fd8f50c __psynch_cvwait + 8<br>
1   libsystem_pthread.dylib       	       0x18fdd11b4 _pthread_cond_wait + 980<br>
2   QtCore                        	       0x10fca2cd8 QWaitConditionPrivate::wait(QDeadlineTimer) + 236<br>
3   QtCore                        	       0x10fca2b84 QWaitCondition::wait(QMutex*, QDeadlineTimer) + 108<br>
4   QtCore                        	       0x10fbebe2c QThreadPoolThread::run() + 932<br>
5   QtCore                        	       0x10fc99f84 QThreadPrivate::start(void*) + 392<br>
6   libsystem_pthread.dylib       	       0x18fdd0ce4 _pthread_start + 136<br>
7   libsystem_pthread.dylib       	       0x18fdcbcd0 thread_start + 8</p>
<p>Thread 13:: ctkFDHandler<br>
0   libsystem_kernel.dylib        	       0x18fd8c910 read + 8<br>
1   libCTKCore.0.1.dylib          	       0x102690798 ctkFDHandler::run() + 96<br>
2   QtCore                        	       0x10fc99f84 QThreadPrivate::start(void*) + 392<br>
3   libsystem_pthread.dylib       	       0x18fdd0ce4 _pthread_start + 136<br>
4   libsystem_pthread.dylib       	       0x18fdcbcd0 thread_start + 8</p>
<p>Thread 14:: ctkFDHandler<br>
0   libsystem_kernel.dylib        	       0x18fd8c910 read + 8<br>
1   libCTKCore.0.1.dylib          	       0x102690798 ctkFDHandler::run() + 96<br>
2   QtCore                        	       0x10fc99f84 QThreadPrivate::start(void*) + 392<br>
3   libsystem_pthread.dylib       	       0x18fdd0ce4 _pthread_start + 136<br>
4   libsystem_pthread.dylib       	       0x18fdcbcd0 thread_start + 8</p>
<p>Thread 15:: QFileInfoGatherer<br>
0   libsystem_kernel.dylib        	       0x18fd8f50c __psynch_cvwait + 8<br>
1   libsystem_pthread.dylib       	       0x18fdd11b4 _pthread_cond_wait + 980<br>
2   QtCore                        	       0x10fca2c34 QWaitConditionPrivate::wait(QDeadlineTimer) + 72<br>
3   QtCore                        	       0x10fca2b84 QWaitCondition::wait(QMutex*, QDeadlineTimer) + 108<br>
4   QtGui                         	       0x10f5012e0 QFileInfoGatherer::run() + 140<br>
5   QtCore                        	       0x10fc99f84 QThreadPrivate::start(void*) + 392<br>
6   libsystem_pthread.dylib       	       0x18fdd0ce4 _pthread_start + 136<br>
7   libsystem_pthread.dylib       	       0x18fdcbcd0 thread_start + 8</p>
<p>Thread 16:: Thread (pooled)<br>
0   libsystem_kernel.dylib        	       0x18fd8f50c __psynch_cvwait + 8<br>
1   libsystem_pthread.dylib       	       0x18fdd11b4 _pthread_cond_wait + 980<br>
2   QtCore                        	       0x10fca2cd8 QWaitConditionPrivate::wait(QDeadlineTimer) + 236<br>
3   QtCore                        	       0x10fca2b84 QWaitCondition::wait(QMutex*, QDeadlineTimer) + 108<br>
4   QtCore                        	       0x10fbebe2c QThreadPoolThread::run() + 932<br>
5   QtCore                        	       0x10fc99f84 QThreadPrivate::start(void*) + 392<br>
6   libsystem_pthread.dylib       	       0x18fdd0ce4 _pthread_start + 136<br>
7   libsystem_pthread.dylib       	       0x18fdcbcd0 thread_start + 8</p>
<p>Thread 17:: Thread (pooled)<br>
0   libsystem_kernel.dylib        	       0x18fd8f50c __psynch_cvwait + 8<br>
1   libsystem_pthread.dylib       	       0x18fdd11b4 _pthread_cond_wait + 980<br>
2   QtCore                        	       0x10fca2cd8 QWaitConditionPrivate::wait(QDeadlineTimer) + 236<br>
3   QtCore                        	       0x10fca2b84 QWaitCondition::wait(QMutex*, QDeadlineTimer) + 108<br>
4   QtCore                        	       0x10fbebe2c QThreadPoolThread::run() + 932<br>
5   QtCore                        	       0x10fc99f84 QThreadPrivate::start(void*) + 392<br>
6   libsystem_pthread.dylib       	       0x18fdd0ce4 _pthread_start + 136<br>
7   libsystem_pthread.dylib       	       0x18fdcbcd0 thread_start + 8</p>
<p>Thread 18:: Thread (pooled)<br>
0   libsystem_kernel.dylib        	       0x18fd8f50c __psynch_cvwait + 8<br>
1   libsystem_pthread.dylib       	       0x18fdd11b4 _pthread_cond_wait + 980<br>
2   QtCore                        	       0x10fca2cd8 QWaitConditionPrivate::wait(QDeadlineTimer) + 236<br>
3   QtCore                        	       0x10fca2b84 QWaitCondition::wait(QMutex*, QDeadlineTimer) + 108<br>
4   QtCore                        	       0x10fbebe2c QThreadPoolThread::run() + 932<br>
5   QtCore                        	       0x10fc99f84 QThreadPrivate::start(void*) + 392<br>
6   libsystem_pthread.dylib       	       0x18fdd0ce4 _pthread_start + 136<br>
7   libsystem_pthread.dylib       	       0x18fdcbcd0 thread_start + 8</p>
<p>Thread 19:: Thread (pooled)<br>
0   libsystem_kernel.dylib        	       0x18fd8f50c __psynch_cvwait + 8<br>
1   libsystem_pthread.dylib       	       0x18fdd11b4 _pthread_cond_wait + 980<br>
2   QtCore                        	       0x10fca2cd8 QWaitConditionPrivate::wait(QDeadlineTimer) + 236<br>
3   QtCore                        	       0x10fca2b84 QWaitCondition::wait(QMutex*, QDeadlineTimer) + 108<br>
4   QtCore                        	       0x10fbebe2c QThreadPoolThread::run() + 932<br>
5   QtCore                        	       0x10fc99f84 QThreadPrivate::start(void*) + 392<br>
6   libsystem_pthread.dylib       	       0x18fdd0ce4 _pthread_start + 136<br>
7   libsystem_pthread.dylib       	       0x18fdcbcd0 thread_start + 8</p>
<p>Thread 20:<br>
0   libsystem_kernel.dylib        	       0x18fd8bb9c semaphore_wait_trap + 8<br>
1   libdispatch.dylib             	       0x194d5249c _dispatch_sema4_wait + 28<br>
2   libdispatch.dylib             	       0x194d52b28 _dispatch_semaphore_wait_slow + 132<br>
3   libtbb.12.dylib               	       0x110a4c57c tbb::detail::r1::rml::private_worker::thread_routine(void*) + 348<br>
4   libsystem_pthread.dylib       	       0x18fdd0ce4 _pthread_start + 136<br>
5   libsystem_pthread.dylib       	       0x18fdcbcd0 thread_start + 8</p>
<p>Thread 21:<br>
0   libsystem_kernel.dylib        	       0x18fd8bb9c semaphore_wait_trap + 8<br>
1   libdispatch.dylib             	       0x194d5249c _dispatch_sema4_wait + 28<br>
2   libdispatch.dylib             	       0x194d52b28 _dispatch_semaphore_wait_slow + 132<br>
3   libtbb.12.dylib               	       0x110a4c57c tbb::detail::r1::rml::private_worker::thread_routine(void*) + 348<br>
4   libsystem_pthread.dylib       	       0x18fdd0ce4 _pthread_start + 136<br>
5   libsystem_pthread.dylib       	       0x18fdcbcd0 thread_start + 8</p>
<p>Thread 22:<br>
0   libsystem_kernel.dylib        	       0x18fd8bb9c semaphore_wait_trap + 8<br>
1   libdispatch.dylib             	       0x194d5249c _dispatch_sema4_wait + 28<br>
2   libdispatch.dylib             	       0x194d52b28 _dispatch_semaphore_wait_slow + 132<br>
3   libtbb.12.dylib               	       0x110a4c57c tbb::detail::r1::rml::private_worker::thread_routine(void*) + 348<br>
4   libsystem_pthread.dylib       	       0x18fdd0ce4 _pthread_start + 136<br>
5   libsystem_pthread.dylib       	       0x18fdcbcd0 thread_start + 8</p>
<p>Thread 23:<br>
0   libsystem_kernel.dylib        	       0x18fd8bb9c semaphore_wait_trap + 8<br>
1   libdispatch.dylib             	       0x194d5249c _dispatch_sema4_wait + 28<br>
2   libdispatch.dylib             	       0x194d52b28 _dispatch_semaphore_wait_slow + 132<br>
3   libtbb.12.dylib               	       0x110a4c57c tbb::detail::r1::rml::private_worker::thread_routine(void*) + 348<br>
4   libsystem_pthread.dylib       	       0x18fdd0ce4 _pthread_start + 136<br>
5   libsystem_pthread.dylib       	       0x18fdcbcd0 thread_start + 8</p>
<p>Thread 24:<br>
0   libsystem_kernel.dylib        	       0x18fd8bb9c semaphore_wait_trap + 8<br>
1   libdispatch.dylib             	       0x194d5249c _dispatch_sema4_wait + 28<br>
2   libdispatch.dylib             	       0x194d52b28 _dispatch_semaphore_wait_slow + 132<br>
3   libtbb.12.dylib               	       0x110a4c57c tbb::detail::r1::rml::private_worker::thread_routine(void*) + 348<br>
4   libsystem_pthread.dylib       	       0x18fdd0ce4 _pthread_start + 136<br>
5   libsystem_pthread.dylib       	       0x18fdcbcd0 thread_start + 8</p>
<p>Thread 25:<br>
0   libsystem_kernel.dylib        	       0x18fd8bb9c semaphore_wait_trap + 8<br>
1   libdispatch.dylib             	       0x194d5249c _dispatch_sema4_wait + 28<br>
2   libdispatch.dylib             	       0x194d52b28 _dispatch_semaphore_wait_slow + 132<br>
3   libtbb.12.dylib               	       0x110a4c57c tbb::detail::r1::rml::private_worker::thread_routine(void*) + 348<br>
4   libsystem_pthread.dylib       	       0x18fdd0ce4 _pthread_start + 136<br>
5   libsystem_pthread.dylib       	       0x18fdcbcd0 thread_start + 8</p>
<p>Thread 26:<br>
0   libsystem_kernel.dylib        	       0x18fd8bb9c semaphore_wait_trap + 8<br>
1   libdispatch.dylib             	       0x194d5249c _dispatch_sema4_wait + 28<br>
2   libdispatch.dylib             	       0x194d52b28 _dispatch_semaphore_wait_slow + 132<br>
3   libtbb.12.dylib               	       0x110a4c57c tbb::detail::r1::rml::private_worker::thread_routine(void*) + 348<br>
4   libsystem_pthread.dylib       	       0x18fdd0ce4 _pthread_start + 136<br>
5   libsystem_pthread.dylib       	       0x18fdcbcd0 thread_start + 8</p>
<p>Thread 0 crashed with ARM Thread State (64-bit):<br>
x0: 0x0000000000000000   x1: 0x0000007811b20310   x2: 0x0000000000000020   x3: 0x0000000000000008<br>
x4: 0x0000000000000020   x5: 0x0000000000000080   x6: 0x0000000000000000   x7: 0x000000016f266360<br>
x8: 0x6c80000000000005   x9: 0x6c94d2b5057bb26d  x10: 0x007ffffffffffff8  x11: 0x000000780c8a1d90<br>
x12: 0x000000780c8a1d90  x13: 0x00000000000001b8  x14: 0x6c94d2b51843adbd  x15: 0x6c94d2b51843adbd<br>
x16: 0x0014d2b5057bb268  x17: 0x000052b5057bb268  x18: 0x0000000000000000  x19: 0x0000007811b20310<br>
x20: 0x0000007811b20318  x21: 0x000000780c8a1cc0  x22: 0x0000000000000020  x23: 0x0000000000000008<br>
x24: 0x000000016f26636c  x25: 0x0000000000000000  x26: 0x0000007811b20310  x27: 0x0000000000002000<br>
x28: 0x000000016f266360   fp: 0x000000016f266240   lr: 0x0000000193f34dc8<br>
sp: 0x000000016f266230   pc: 0x0000000194070294 cpsr: 0x20001000<br>
far: 0x0000000000000000  esr: 0xf200c472 (Breakpoint) pointer authentication trap DA</p>

---

## Post #10 by @Philipp_G (2026-10-30 11:52 UTC)

<p>new 29th release works!</p>

---
