---
topic_id: 46974
title: "Volume rendering broken in latest Linux previews?"
date: 2026-05-08
url: https://discourse.slicer.org/t/46974
last_bumped: 2026-05-27T13:28:43.234Z
---

# Volume rendering broken in latest Linux previews?

**Topic ID**: 46974
**Date**: 2026-05-08
**URL**: https://discourse.slicer.org/t/volume-rendering-broken-in-latest-linux-previews/46974

---

## Post #1 by @muratmaga (2026-05-08 18:49 UTC)

<p>I am using the preview build from May 5th on Ubuntu, and I can’t get the MRHead (or any of the baked data) to render. When I drag and drop volume object to the 3D viewer, application fails catastrophically, without any error on the console or in the command line.</p>
<p>Same if I were to use the Volume Rendering module. Here is all the log from the failed session:</p>
<pre><code class="lang-auto">[DEBUG][Qt] 08.05.2026 11:39:58 [] (unknown:0) - Session start time .......: 20260508_113958
[DEBUG][Qt] 08.05.2026 11:39:58 [] (unknown:0) - Slicer version ...........: 5.11.0-2026-05-05 (revision 34535 / c59af2b) linux-amd64 - installed release
[DEBUG][Qt] 08.05.2026 11:39:58 [] (unknown:0) - Operating system .........: Linux / 6.8.0-106-generic / #106-Ubuntu SMP PREEMPT_DYNAMIC Fri Mar  6 07:58:08 UTC 2026 / UTF-8 - 64-bit
[DEBUG][Qt] 08.05.2026 11:39:58 [] (unknown:0) - Memory ...................: 515582 MB physical, 2047 MB virtual
[DEBUG][Qt] 08.05.2026 11:39:58 [] (unknown:0) - CPU ......................: AuthenticAMD AMD Ryzen Threadripper PRO 3995WX 64-Cores, 64 cores, 128 logical processors
[DEBUG][Qt] 08.05.2026 11:39:58 [] (unknown:0) - VTK configuration ........: OpenGL2 rendering, TBB threading
[DEBUG][Qt] 08.05.2026 11:39:58 [] (unknown:0) - Qt configuration .........: version 5.15.2, with SSL, requested OpenGL 3.2 (core profile)
[DEBUG][Qt] 08.05.2026 11:39:58 [] (unknown:0) - DCMTK configuration ......: version 3.7.0, no SSL
[DEBUG][Qt] 08.05.2026 11:39:58 [] (unknown:0) - Internationalization .....: disabled, language=
[DEBUG][Qt] 08.05.2026 11:39:58 [] (unknown:0) - Developer mode ...........: enabled
[DEBUG][Qt] 08.05.2026 11:39:58 [] (unknown:0) - Application path .........: /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin
[DEBUG][Qt] 08.05.2026 11:39:58 [] (unknown:0) - Additional module paths ..: (none)
[WARNING][VTK] 08.05.2026 11:39:58 [vtkCacheManager (0x2b9d5930)] (vtkCacheManager.cxx:1068) - Cache pruning is disabled as no sentinel file is found in the cache directory.
[INFO][Stream] 08.05.2026 11:39:58 [] (unknown:0) -
[WARNING][Python] 08.05.2026 11:40:02 [Python] (/home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/lib/Python/lib/python3.12/site-packages/pydicom/misc.py:82) - get_frame_offsets is deprecated and will be removed in v4.0
[DEBUG][Python] 08.05.2026 11:40:03 [Python] (/home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/lib/Slicer-5.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:40) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 08.05.2026 11:40:03 [Python] (/home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/lib/Slicer-5.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:40) - Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Qt] 08.05.2026 11:40:03 [] (unknown:0) - Switch to module:  "Data"
[WARNING][VTK] 08.05.2026 11:40:41 [vtkCacheManager (0x3b1c7a60)] (vtkCacheManager.cxx:407) - Cache directory does not contain sentinel file .slicer-cache. Destructive cache operations are disabled until the sentinel is created.
[DEBUG][Qt] 08.05.2026 11:40:41 [] (unknown:0) - "Volume" Reader has successfully read the file "/home/maga/.cache/slicer.org/Slicer/SlicerIO/MR-head.nrrd" "[0.14s]"
[DEBUG][Qt] 08.05.2026 11:40:50 [] (unknown:0) - Switch to module:  "VolumeRendering"

</code></pre>

---

## Post #2 by @pieper (2026-05-08 19:02 UTC)

<p>With today’s linux nightly I couldn’t even download any sample data.  When I loaded local data the volume rendering did work.</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "/home/exouser/Downloads/Slicer-5.11.0-2026-05-07-linux-amd64/bin/../lib/Slicer-5.11/qt-scripted-modules/SampleData.py", line 457, in &lt;lambda&gt;
    b.connect("clicked()", lambda s=source: logic.downloadFromSource(s))
                                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/exouser/Downloads/Slicer-5.11.0-2026-05-07-linux-amd64/bin/../lib/Slicer-5.11/qt-scripted-modules/SampleData.py", line 912, in downloadFromSource
    filePath = self.downloadFileIntoCache(uri, fileName, checksum, forceDownload=forceDownload)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/exouser/Downloads/Slicer-5.11.0-2026-05-07-linux-amd64/bin/../lib/Slicer-5.11/qt-scripted-modules/SampleData.py", line 836, in downloadFileIntoCache
    return self.downloadFile(uri, destFolderPath, name, checksum, forceDownload=forceDownload)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/exouser/Downloads/Slicer-5.11.0-2026-05-07-linux-amd64/bin/../lib/Slicer-5.11/qt-scripted-modules/SampleData.py", line 1168, in downloadFile
    self.logMessage(_("Verifying checksum"))
  File "/home/exouser/Downloads/Slicer-5.11.0-2026-05-07-linux-amd64/bin/../lib/Slicer-5.11/qt-scripted-modules/SampleData.py", line 473, in logMessage
    self.log.insertHtml(message)
    ^^^^^^^^
AttributeError: 'SampleDataWidget' object has no attribute 'log'
</code></pre>

---

## Post #3 by @chir.set (2026-05-08 19:13 UTC)

<p>With <code>5.11.0-2026-05-07 r34537 / 785744e</code> on Arch, MRHead is downloaded but volume rendering does crash the application.</p>

---

## Post #4 by @lassoan (2026-05-11 05:33 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="46974">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>With today’s linux nightly I couldn’t even download any sample data.</p>
</blockquote>
</aside>
<p>Sorry, that’s my mistake (it was a recent quick fix to allow translation of Sample Data category names). Here is a PR with the fix: <a href="https://github.com/Slicer/Slicer/pull/9150" class="inline-onebox">BUG: Fix SampleData module by lassoan · Pull Request #9150 · Slicer/Slicer · GitHub</a></p>
<p>I’ve installed <code>Slicer 5.11.0-2026-05-07 r34537 / 785744e</code> on Ubuntu 24.04 on GPU-accelerated container and volume rendering worked well when I drag-and-dropped <code>CTChest</code> sample data set to the 3D view or switched to Volume Rendering module and clicked the eye button. Both with CPU and GPU volume rendering. Both with factory-built Slicer and custom-built debug-mode Slicer.</p>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> <a class="mention" href="/u/chir.set">@chir.set</a> can you give more information on the issue? It could be nice to get a stack trace. Or information on when the problem started to occur (by installing a couple of Slicer releases from previous weeks or months).</p>

---

## Post #5 by @chir.set (2026-05-11 08:38 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="46974">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>can you give more information on the issue?</p>
</blockquote>
</aside>
<p>The crash does not occur if this environment variable is set:</p>
<p><code>export QT_QPA_PLATFORM=xcb</code></p>
<p>Else, there’s no backtrace in <code>lldb</code>, only the following:</p>
<pre><code class="lang-auto">Switch to module:  "VolumeRendering"
X Error of failed request:  BadAccess (attempt to access private resource denied)
  Major opcode of failed request:  150 (GLX)
  Minor opcode of failed request:  5 (X_GLXMakeCurrent)
  Serial number of failed request:  34
  Current serial number in output stream:  34
vtkDebugLeaks has detected LEAKS!
Class "vtkXOpenGLRenderWindow has 1 instance still around.
Class "vtkInteractorStyleTrackballCamera has 1 instance still around.
Class "vtkShader has 138 instances still around.
Class "vtkMRMLMultiVolumeRenderingDisplayNode has 1 instance still around.
...
...
</code></pre>
<p>It seems to  be a Wayland oddity, one more. It’s the default display server on my machines.</p>

---

## Post #6 by @pieper (2026-05-11 15:10 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="5" data-topic="46974">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>It seems to be a Wayland oddity,</p>
</blockquote>
</aside>
<p>That makes sense - my machines use X.</p>

---

## Post #7 by @muratmaga (2026-05-11 15:42 UTC)

<p>That didn’t make any difference for me, still crashes with that setting. I am not using Wayland, regular X (as far as I can tell).</p>
<p>It also crashes on the MorphoCloud instances.</p>

---

## Post #8 by @pieper (2026-05-11 15:44 UTC)

<p>My test was on a jetstream2 VM without a GPU, so maybe it’s a driver thing.</p>

---

## Post #9 by @pieper (2026-05-11 15:48 UTC)

<p>I just tried the latest preview build from <a href="http://download.slicer.org">download.slicer.org</a> on a vast.ai machine with a 3070 running X (ubuntu 24.04) and both the sample data and volume rendering work.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c6583b64b11b6a4f847f4b7cf473072f6f39657.jpeg" data-download-href="/uploads/short-url/fsV3L20wKjSYHZ0RJbaXK1G91xt.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c6583b64b11b6a4f847f4b7cf473072f6f39657_2_690x329.jpeg" alt="image" data-base62-sha1="fsV3L20wKjSYHZ0RJbaXK1G91xt" width="690" height="329" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c6583b64b11b6a4f847f4b7cf473072f6f39657_2_690x329.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c6583b64b11b6a4f847f4b7cf473072f6f39657_2_1035x493.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c6583b64b11b6a4f847f4b7cf473072f6f39657_2_1380x658.jpeg 2x" data-dominant-color="888587"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×917 198 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @muratmaga (2026-05-11 15:57 UTC)

<pre><code class="lang-auto">"Volume" Reader has successfully read the file "/home/maga/.cache/slicer.org/Slicer/SlicerIO/MR-head.nrrd" "\[0.14s\]"

Thread 1 "SlicerApp-real" received signal SIGSEGV, Segmentation fault.
0x00007fffec3e4c71 in std::\__detail::\_Scanner::\_M_scan_normal() ()
from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libQt5WebEngineCore.so.5
(gdb) thread apply all bt

Thread 390 (Thread 0x7ffb65ff76c0 (LWP 1108542) "QFileInfoGather"):
#0  0x00007fffd0298d71 in \__futex_abstimed_wait_common64 (private=32767, cancel=true, abstime=0x0, op=393, expected=0, futex_word=0x7db6fd0) at ./nptl/futex-internal.c:57
#1  \__futex_abstimed_wait_common (cancel=true, private=32767, abstime=0x0, clockid=0, expected=0, futex_word=0x7db6fd0) at ./nptl/futex-internal.c:87
#2  \__GI___futex_abstimed_wait_cancelable64 (futex_word=futex_word@entry=0x7db6fd0, expected=expected@entry=0, clockid=clockid@entry=0, abstime=abstime@entry=0x0, private=private@entry=0) at ./nptl/futex-internal.c:139
#3  0x00007fffd029b7ed in \__pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x7db6f80, cond=0x7db6fa8) at ./nptl/pthread_cond_wait.c:503
#4  \___pthread_cond_wait (cond=0x7db6fa8, mutex=0x7db6f80) at ./nptl/pthread_cond_wait.c:627
#5  0x00007ffff56ba613 in QWaitCondition::wait(QMutex\*, QDeadlineTimer) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libQt5Core.so.5
#6  0x00007ffff6b73690 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libQt5Widgets.so.5
#7  0x00007ffff56b3b35 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libQt5Core.so.5
#8  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#9  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 389 (Thread 0x7ffb683f06c0 (LWP 1108535) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 388 (Thread 0x7ffb673fc6c0 (LWP 1108537) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 387 (Thread 0x7ffb66bfa6c0 (LWP 1108539) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78
--Type  for more, q to quit, c to continue without paging--c

Thread 386 (Thread 0x7ffb677fd6c0 (LWP 1108536) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 385 (Thread 0x7ffb66ffb6c0 (LWP 1108538) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 384 (Thread 0x7ffb667f96c0 (LWP 1108540) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 383 (Thread 0x7ffb663f86c0 (LWP 1108541) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 382 (Thread 0x7ffb6abfa6c0 (LWP 1108525) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 381 (Thread 0x7ffb787f16c0 (LWP 1108505) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 380 (Thread 0x7ffb73bfe6c0 (LWP 1108511) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 379 (Thread 0x7ffb707f16c0 (LWP 1108520) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 378 (Thread 0x7ffb70ff36c0 (LWP 1108518) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 377 (Thread 0x7ffb733fc6c0 (LWP 1108508) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 376 (Thread 0x7ffb793f46c0 (LWP 1108502) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 375 (Thread 0x7ffb71ff76c0 (LWP 1108514) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 374 (Thread 0x7ffb72bfa6c0 (LWP 1108512) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 373 (Thread 0x7ffb697f56c0 (LWP 1108530) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 372 (Thread 0x7ffb713f46c0 (LWP 1108517) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 371 (Thread 0x7ffb68bf26c0 (LWP 1108533) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 370 (Thread 0x7ffb73fff6c0 (LWP 1108506) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 369 (Thread 0x7ffb69bf66c0 (LWP 1108529) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 368 (Thread 0x7ffb71bf66c0 (LWP 1108515) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 367 (Thread 0x7ffb693f46c0 (LWP 1108531) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 366 (Thread 0x7ffb727f96c0 (LWP 1108510) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 365 (Thread 0x7ffb737fd6c0 (LWP 1108507) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 364 (Thread 0x7ffb717f56c0 (LWP 1108516) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 363 (Thread 0x7ffb6bbfe6c0 (LWP 1108521) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 362 (Thread 0x7ffb68ff36c0 (LWP 1108532) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 361 (Thread 0x7ffb70bf26c0 (LWP 1108519) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 360 (Thread 0x7ffb6b3fc6c0 (LWP 1108523) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 359 (Thread 0x7ffb6a3f86c0 (LWP 1108527) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 358 (Thread 0x7ffb6b7fd6c0 (LWP 1108522) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 357 (Thread 0x7ffb78bf26c0 (LWP 1108504) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 356 (Thread 0x7ffb78ff36c0 (LWP 1108503) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 355 (Thread 0x7ffb6affb6c0 (LWP 1108524) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 354 (Thread 0x7ffb69ff76c0 (LWP 1108528) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 353 (Thread 0x7ffb687f16c0 (LWP 1108534) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 352 (Thread 0x7ffb72ffb6c0 (LWP 1108509) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 351 (Thread 0x7ffb6a7f96c0 (LWP 1108526) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 350 (Thread 0x7ffb723f86c0 (LWP 1108513) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 349 (Thread 0x7ffb7a3f86c0 (LWP 1108498) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 348 (Thread 0x7ffb93fff6c0 (LWP 1108482) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 347 (Thread 0x7ffb7bbfe6c0 (LWP 1108491) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 346 (Thread 0x7ffb91bf66c0 (LWP 1108477) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 345 (Thread 0x7ffb917f56c0 (LWP 1108478) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 344 (Thread 0x7ffb937fd6c0 (LWP 1108484) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 343 (Thread 0x7ffb79ff76c0 (LWP 1108499) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 342 (Thread 0x7ffb633fc6c0 (LWP 1108489) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 341 (Thread 0x7ffb907f16c0 (LWP 1108483) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 340 (Thread 0x7ffb90ff36c0 (LWP 1108480) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 339 (Thread 0x7ffb923f86c0 (LWP 1108474) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 338 (Thread 0x7ffb7b7fd6c0 (LWP 1108487) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 337 (Thread 0x7ffb79bf66c0 (LWP 1108500) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 336 (Thread 0x7ffb5affb6c0 (LWP 1108492) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 335 (Thread 0x7ffb7bfff6c0 (LWP 1108486) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 334 (Thread 0x7ffb7affb6c0 (LWP 1108497) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 333 (Thread 0x7ffb933fc6c0 (LWP 1108485) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 332 (Thread 0x7ffb91ff76c0 (LWP 1108476) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 331 (Thread 0x7ffb7b3fc6c0 (LWP 1108488) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 330 (Thread 0x7ffb92ffb6c0 (LWP 1108496) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 329 (Thread 0x7ffb7abfa6c0 (LWP 1108495) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 328 (Thread 0x7ffb90bf26c0 (LWP 1108481) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 327 (Thread 0x7ffb797f56c0 (LWP 1108501) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 326 (Thread 0x7ffb67bfe6c0 (LWP 1108475) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 325 (Thread 0x7ffb93bfe6c0 (LWP 1108490) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 324 (Thread 0x7ffb7a7f96c0 (LWP 1108494) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 323 (Thread 0x7ffb913f46c0 (LWP 1108479) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 322 (Thread 0x7ffb637fd6c0 (LWP 1108493) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 321 (Thread 0x7ffb927f96c0 (LWP 1108472) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 320 (Thread 0x7ffb92bfa6c0 (LWP 1108471) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 319 (Thread 0x7ffb6bfff6c0 (LWP 1108473) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 318 (Thread 0x7ffba87f16c0 (LWP 1108470) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 317 (Thread 0x7ffba93f46c0 (LWP 1108467) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 316 (Thread 0x7ffbaa7f96c0 (LWP 1108462) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 315 (Thread 0x7ffba97f56c0 (LWP 1108466) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 314 (Thread 0x7ffba8bf26c0 (LWP 1108469) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 313 (Thread 0x7ffbab3fc6c0 (LWP 1108459) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 312 (Thread 0x7ffbaa3f86c0 (LWP 1108463) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 311 (Thread 0x7ffba9bf66c0 (LWP 1108465) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 310 (Thread 0x7ffbaabfa6c0 (LWP 1108461) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 309 (Thread 0x7ffbaaffb6c0 (LWP 1108460) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 308 (Thread 0x7ffbab7fd6c0 (LWP 1108458) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 307 (Thread 0x7ffba9ff76c0 (LWP 1108464) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 306 (Thread 0x7ffba8ff36c0 (LWP 1108468) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 305 (Thread 0x7ffbeabfa6c0 (LWP 1108446) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 304 (Thread 0x7ffbe87f16c0 (LWP 1108455) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 303 (Thread 0x7ffbe9ff76c0 (LWP 1108449) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 302 (Thread 0x7ffbebbfe6c0 (LWP 1108442) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 301 (Thread 0x7ffbe9bf66c0 (LWP 1108450) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 300 (Thread 0x7ffbeb7fd6c0 (LWP 1108443) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 299 (Thread 0x7ffbe97f56c0 (LWP 1108451) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 298 (Thread 0x7ffbea3f86c0 (LWP 1108448) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 297 (Thread 0x7ffbe93f46c0 (LWP 1108452) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 296 (Thread 0x7ffbe8ff36c0 (LWP 1108453) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 295 (Thread 0x7ffbfc7f16c0 (LWP 1108440) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 294 (Thread 0x7ffbabbfe6c0 (LWP 1108456) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 293 (Thread 0x7ffbeb3fc6c0 (LWP 1108444) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 292 (Thread 0x7ffbeaffb6c0 (LWP 1108445) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 291 (Thread 0x7ffbabfff6c0 (LWP 1108457) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 290 (Thread 0x7ffbea7f96c0 (LWP 1108447) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 289 (Thread 0x7ffbebfff6c0 (LWP 1108441) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 288 (Thread 0x7ffbe8bf26c0 (LWP 1108454) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 287 (Thread 0x7ffbff3fc6c0 (LWP 1108433) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 286 (Thread 0x7ffbfdff76c0 (LWP 1108434) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 285 (Thread 0x7ffbfe7f96c0 (LWP 1108432) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 284 (Thread 0x7ffbfcbf26c0 (LWP 1108439) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 283 (Thread 0x7ffbfdbf66c0 (LWP 1108435) "SlicerApp-real"):
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007fffd81afcfb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#2  0x00007fffd81c96f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libtbb.so.12
#3  0x00007fffd029caa4 in start_thread (arg=) at ./nptl/pthread_create.c:447
#4  0x00007fffd0329c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 282 (Thread 0x7ffbfd3f46c0 (LWP 1108437) "SlicerApp-real"): 
</code></pre>

---

## Post #11 by @muratmaga (2026-05-11 16:09 UTC)

<p>For me this version works: Slicer-5.11.0-2026-02-10-linux-amd64/Slicer</p>
<p>Anything after that I can see on the downloads page, crashed the same way.</p>

---

## Post #12 by @mhalle (2026-05-11 16:37 UTC)

<p>Claude suggests this might be related to a VTK 9.6.0 → 9.6.1 change where VTK 9.6.x replaced GLEW with GLAD as the OpenGL function loader and, more importantly, added <strong>runtime detection of GLX / EGL / OSMesa</strong> (Kitware MR !11367). It wouldn’t be triggered in some configurations like Steve’s.</p>
<p>Claude suggests:<br>
export<code>VTK_DEFAULT_OPENGL_WINDOW=vtkEGLRenderWindow</code></p>
<p><code>or possibly vtkOSOpenGLRenderWindow</code></p>
<p>as a test.</p>

---

## Post #13 by @muratmaga (2026-05-11 16:43 UTC)

<aside class="quote no-group" data-username="mhalle" data-post="12" data-topic="46974">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/50afbb/48.png" class="avatar"> mhalle:</div>
<blockquote>
<p>vtkOSOpenGLRenderWindow</p>
</blockquote>
</aside>
<p>Neither have any effect, still crashes.</p>

---

## Post #14 by @muratmaga (2026-05-11 16:53 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/jamesobutler">@jamesobutler</a> I think it is this for me:</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/Slicer/Slicer/commit/1b21266bf47f126ece58d12b87160e38f55ad258">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/commit/1b21266bf47f126ece58d12b87160e38f55ad258" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/commit/1b21266bf47f126ece58d12b87160e38f55ad258" target="_blank" rel="noopener nofollow ugc">ENH: Add support for building against VTK version 9.6.0</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2026-03-11" data-time="22:06:50" data-timezone="UTC">10:06PM - 11 Mar 26 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/jamesobutler" target="_blank" rel="noopener nofollow ugc">
          <img alt="" src="https://avatars.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
          jamesobutler
        </a>
      </div>

      <div class="lines" title="changed 2 files with 8 additions and 5 deletions">
        <a href="https://github.com/Slicer/Slicer/commit/1b21266bf47f126ece58d12b87160e38f55ad258" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+8</span>
          <span class="removed">-5</span>
        </a>
      </div>
    </div>
  </div>
</div>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Slicer from 3/04 works, 3/12 crashes.</p>

---

## Post #15 by @lassoan (2026-05-11 18:12 UTC)

<p>The error location (in the Qt web browser) is very interesting. Could you copy here the stack trace for Thread 1? (what you copied contained Thread 390 to 282)</p>

---

## Post #16 by @muratmaga (2026-05-11 19:03 UTC)

<p><code>thread apply all bt</code></p>
<pre><code class="lang-auto">Thread 1 (Thread 0x7fffcc6c6900 (LWP 1127013) "SlicerApp-real"):
#0  0x00007fffec3e4c71 in std::\__detail::\_Scanner::\_M_scan_normal() () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libQt5WebEngineCore.so.5
#1  0x00007fffdbfc079f in std::\__detail::\_Compiler&lt;std::\__cxx11::regex_traits &gt;::\_M_try_char() () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/libvtkInfovisCore-9.6.so.1
#2  0x00007fffdbfcb5e4 in std::\__detail::\_Compiler&lt;std::\__cxx11::regex_traits &gt;::\_M_atom() () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/libvtkInfovisCore-9.6.so.1
#3  0x00007fffdbfcbc28 in std::\__detail::\_Compiler&lt;std::\__cxx11::regex_traits &gt;::\_M_alternative() () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/libvtkInfovisCore-9.6.so.1
#4  0x00007fffdbfcbeb9 in std::\__detail::\_Compiler&lt;std::\__cxx11::regex_traits &gt;::\_M_disjunction() () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/libvtkInfovisCore-9.6.so.1
#5  0x00007fffdbfcb92b in std::\__detail::\_Compiler&lt;std::\__cxx11::regex_traits &gt;::\_M_atom() () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/libvtkInfovisCore-9.6.so.1
#6  0x00007fffdbfcbc28 in std::\__detail::\_Compiler&lt;std::\__cxx11::regex_traits &gt;::\_M_alternative() () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/libvtkInfovisCore-9.6.so.1
#7  0x00007fffdbfcbeb9 in std::\__detail::\_Compiler&lt;std::\__cxx11::regex_traits &gt;::\_M_disjunction() () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/libvtkInfovisCore-9.6.so.1
#8  0x00007fffd1e0084f in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/libvtkCommon-9.6.so.1
#9  0x00007fffd1e0102d in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/libvtkCommon-9.6.so.1
#10 0x00007fffd1ded2c9 in vtk::is_printf_format(std::\__cxx11::basic_string&lt;char, std::char_traits, std::allocator &gt; const&amp;) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/libvtkCommon-9.6.so.1
#11 0x00007fffd1def5d4 in vtk::to_std_format(std::\__cxx11::basic_string&lt;char, std::char_traits, std::allocator &gt; const&amp;) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/libvtkCommon-9.6.so.1
#12 0x00007fffda4ec400 in vtkImageReader2::ComputeInternalFileName(int) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/libvtkIO-9.6.so.1
#13 0x00007fffda4f7a48 in vtkJPEGReader::ExecuteInformation() () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/libvtkIO-9.6.so.1
#14 0x00007fffda4ebc95 in vtkImageReader2::RequestInformation(vtkInformation\*, vtkInformationVector\*\*, vtkInformationVector\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/libvtkIO-9.6.so.1
#15 0x00007fffd15b2831 in vtkExecutive::CallAlgorithm(vtkInformation\*, int, vtkInformationVector\*\*, vtkInformationVector\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/libvtkCommon-9.6.so.1
#16 0x00007fffd162de57 in vtkStreamingDemandDrivenPipeline::ExecuteInformation(vtkInformation\*, vtkInformationVector\*\*, vtkInformationVector\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/libvtkCommon-9.6.so.1
#17 0x00007fffd15ac44c in vtkDemandDrivenPipeline::ProcessRequest(vtkInformation\*, vtkInformationVector\*\*, vtkInformationVector\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/libvtkCommon-9.6.so.1
#18 0x00007fffd162ee10 in vtkStreamingDemandDrivenPipeline::Update(int, vtkInformationVector\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/libvtkCommon-9.6.so.1
#19 0x00007fffdbccc2fc in vtkOpenGLRenderWindow::GetNoiseTextureUnit() () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/libvtkOpenGL-9.6.so.1
#20 0x00007fffdbb3545c in vtkOpenGLGPUVolumeRayCastMapper::vtkInternal::SetMapperShaderParameters(vtkShaderProgram\*, vtkRenderer\*, int, int) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/libvtkOpenGL-9.6.so.1
#21 0x00007fffdbb41827 in vtkOpenGLGPUVolumeRayCastMapper::vtkInternal::RenderSingleInput(vtkRenderer\*, vtkOpenGLCamera\*, vtkShaderProgram\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/libvtkOpenGL-9.6.so.1
#22 0x00007fffdbb4cb14 in vtkOpenGLGPUVolumeRayCastMapper::GPURender(vtkRenderer\*, vtkVolume\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/libvtkOpenGL-9.6.so.1
#23 0x00007fffd8d79b15 in vtkGPUVolumeRayCastMapper::Render(vtkRenderer\*, vtkVolume\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/libvtkRendering-9.6.so.1
#24 0x00007fffd9061939 in vtkVolume::RenderVolumetricGeometry(vtkViewport\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/libvtkRendering-9.6.so.1
#25 0x00007fffdbcd27f7 in vtkOpenGLRenderer::UpdateGeometry(vtkFrameBufferObjectBase\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/libvtkOpenGL-9.6.so.1
#26 0x00007fffdbcd6d83 in vtkOpenGLRenderer::DeviceRender() () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/libvtkOpenGL-9.6.so.1
#27 0x00007fffd9038305 in vtkRenderer::Render() () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/libvtkRendering-9.6.so.1
#28 0x00007fffd903e5ba in vtkRendererCollection::Render() () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/libvtkRendering-9.6.so.1
#29 0x00007fffd902968d in vtkRenderWindow::DoStereoRender() () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/libvtkRendering-9.6.so.1
#30 0x00007fffd902a0b8 in vtkRenderWindow::Render() () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/libvtkRendering-9.6.so.1
#31 0x00007fffdbcd13ce in vtkOpenGLRenderWindow::Render() () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/libvtkOpenGL-9.6.so.1
#32 0x00007fffdbba557a in vtkGenericOpenGLRenderWindow::Render() () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/libvtkOpenGL-9.6.so.1
#33 0x00007ffff7dca269 in ctkVTKAbstractView::forceRender() () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libCTKVisualizationVTKWidgets.so.0.1
#34 0x00007ffff58d5ddf in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libQt5Core.so.5
#35 0x00007ffff715565b in ctkVTKConnection::emitExecute(vtkObject\*, void\*, unsigned long, void\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libCTKVisualizationVTKCore.so.0.1
#36 0x00007ffff7160b59 in ctkVTKConnectionPrivate::execute(vtkObject\*, unsigned long, void\*, void\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libCTKVisualizationVTKCore.so.0.1
#37 0x00007fffd45d92c9 in vtkCallbackCommand::Execute(vtkObject\*, unsigned long, void\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/libvtkCommon-9.6.so.1
#38 0x00007fffe6ca586c in vtkEventBroker::InvokeObservation(vtkObservation\*, unsigned long, void\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libMRMLCore.so
#39 0x00007fffe6ca8781 in vtkEventBroker::ProcessEvent(vtkObservation\*, vtkObject\*, unsigned long, void\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libMRMLCore.so
#40 0x00007fffd45d92c9 in vtkCallbackCommand::Execute(vtkObject\*, unsigned long, void\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/libvtkCommon-9.6.so.1
#41 0x00007fffd465e2f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/libvtkCommon-9.6.so.1
#42 0x00007ffd3390c686 in vtkMRMLVolumeRenderingDisplayableManager::ProcessMRMLNodesEvents(vtkObject\*, unsigned long, void\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/qt-loadable-modules/libvtkSlicerVolumeRenderingModuleMRMLDisplayableManager.so
#43 0x00007ffff4a74d26 in vtkMRMLAbstractLogic::MRMLNodesCallback(vtkObject\*, unsigned long, void\*, void\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libMRMLLogic.so
#44 0x00007fffd45d92c9 in vtkCallbackCommand::Execute(vtkObject\*, unsigned long, void\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/libvtkCommon-9.6.so.1
#45 0x00007fffe6ca586c in vtkEventBroker::InvokeObservation(vtkObservation\*, unsigned long, void\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libMRMLCore.so
#46 0x00007fffe6ca8781 in vtkEventBroker::ProcessEvent(vtkObservation\*, vtkObject\*, unsigned long, void\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libMRMLCore.so
#47 0x00007fffd45d92c9 in vtkCallbackCommand::Execute(vtkObject\*, unsigned long, void\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/libvtkCommon-9.6.so.1
#48 0x00007fffd465e2f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/libvtkCommon-9.6.so.1
#49 0x00007fffe6d3ad57 in vtkMRMLDisplayableNode::ProcessMRMLEvents(vtkObject\*, unsigned long, void\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libMRMLCore.so
#50 0x00007fffe712eea8 in vtkMRMLVolumeNode::ProcessMRMLEvents(vtkObject\*, unsigned long, void\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libMRMLCore.so
#51 0x00007fffe6e791fa in vtkMRMLNode::MRMLCallback(vtkObject\*, unsigned long, void\*, void\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libMRMLCore.so
#52 0x00007fffd45d92c9 in vtkCallbackCommand::Execute(vtkObject\*, unsigned long, void\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/libvtkCommon-9.6.so.1
#53 0x00007fffe6ca586c in vtkEventBroker::InvokeObservation(vtkObservation\*, unsigned long, void\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libMRMLCore.so
#54 0x00007fffe6ca8781 in vtkEventBroker::ProcessEvent(vtkObservation\*, vtkObject\*, unsigned long, void\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libMRMLCore.so
#55 0x00007fffd45d92c9 in vtkCallbackCommand::Execute(vtkObject\*, unsigned long, void\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/libvtkCommon-9.6.so.1
#56 0x00007fffd465e2f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/libvtkCommon-9.6.so.1
#57 0x00007ffd33862ec9 in vtkMRMLVolumeRenderingDisplayNode::ProcessMRMLEvents(vtkObject\*, unsigned long, void\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/qt-loadable-modules/libvtkSlicerVolumeRenderingModuleMRML.so
#58 0x00007fffe6e791fa in vtkMRMLNode::MRMLCallback(vtkObject\*, unsigned long, void\*, void\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libMRMLCore.so
#59 0x00007fffd45d92c9 in vtkCallbackCommand::Execute(vtkObject\*, unsigned long, void\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/libvtkCommon-9.6.so.1
#60 0x00007fffe6ca586c in vtkEventBroker::InvokeObservation(vtkObservation\*, unsigned long, void\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libMRMLCore.so
#61 0x00007fffe6ca8781 in vtkEventBroker::ProcessEvent(vtkObservation\*, vtkObject\*, unsigned long, void\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libMRMLCore.so
#62 0x00007fffd45d92c9 in vtkCallbackCommand::Execute(vtkObject\*, unsigned long, void\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/libvtkCommon-9.6.so.1
#63 0x00007fffd465e2f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/libvtkCommon-9.6.so.1
#64 0x00007ffff775d30d in qMRMLSceneModel::updateNodeFromItem(vtkMRMLNode\*, QStandardItem\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libqMRMLWidgets.so
#65 0x00007ffff7757e0f in qMRMLSceneModel::updateNodeItems(vtkMRMLNode\*, QString const&amp;) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libqMRMLWidgets.so
#66 0x00007ffff7758527 in qMRMLSceneModel::onMRMLNodeModified(vtkObject\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libqMRMLWidgets.so
#67 0x00007ffff58d5ddf in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libQt5Core.so.5
#68 0x00007ffff715565b in ctkVTKConnection::emitExecute(vtkObject\*, void\*, unsigned long, void\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libCTKVisualizationVTKCore.so.0.1
#69 0x00007ffff7160b59 in ctkVTKConnectionPrivate::execute(vtkObject\*, unsigned long, void\*, void\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libCTKVisualizationVTKCore.so.0.1
#70 0x00007fffd45d92c9 in vtkCallbackCommand::Execute(vtkObject\*, unsigned long, void\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/libvtkCommon-9.6.so.1
#71 0x00007fffe6ca586c in vtkEventBroker::InvokeObservation(vtkObservation\*, unsigned long, void\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libMRMLCore.so
#72 0x00007fffe6ca8781 in vtkEventBroker::ProcessEvent(vtkObservation\*, vtkObject\*, unsigned long, void\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libMRMLCore.so
#73 0x00007fffd45d92c9 in vtkCallbackCommand::Execute(vtkObject\*, unsigned long, void\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/libvtkCommon-9.6.so.1
#74 0x00007fffd465e2f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/libvtkCommon-9.6.so.1
#75 0x00007ffff7e82fea in vtkMRMLNode::InvokePendingModifiedEvent() () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libqSlicerBaseQTCLI.so
#76 0x00007fffe6e84076 in vtkMRMLNode::Copy(vtkMRMLNode\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libMRMLCore.so
#77 0x00007fffe6f90db5 in vtkMRMLStorableNode::Copy(vtkMRMLNode\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libMRMLCore.so
#78 0x00007ffd33889fd0 in vtkSlicerVolumeRenderingLogic::SetRecommendedVolumeRenderingProperties(vtkMRMLVolumeRenderingDisplayNode\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/qt-loadable-modules/libvtkSlicerVolumeRenderingModuleLogic.so
#79 0x00007ffd3388ea05 in vtkSlicerVolumeRenderingLogic::CreateDefaultVolumeRenderingNodes(vtkMRMLVolumeNode\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/qt-loadable-modules/libvtkSlicerVolumeRenderingModuleLogic.so
#80 0x00007ffd338a4f35 in qSlicerSubjectHierarchyVolumeRenderingPlugin::showVolumeRendering(bool, long long, vtkMRMLViewNode\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/qt-loadable-modules/libqSlicerVolumeRenderingSubjectHierarchyPlugins.so
#81 0x00007ffd41195ea1 in qSlicerSubjectHierarchyPluginHandler::showItemsInView(vtkIdList\*, vtkMRMLAbstractViewNode\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/qt-loadable-modules/libqSlicerSubjectHierarchyModuleWidgets.so
#82 0x00007fffd45d92c9 in vtkCallbackCommand::Execute(vtkObject\*, unsigned long, void\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/libvtkCommon-9.6.so.1
#83 0x00007fffd465e2f6 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/libvtkCommon-9.6.so.1
#84 0x00007fffe6facf3a in vtkMRMLSubjectHierarchyNode::ShowItemsInView(vtkIdList\*, vtkMRMLAbstractViewNode\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libMRMLCore.so
#85 0x00007ffff77a4fca in qMRMLThreeDView::dropEvent(QDropEvent\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libqMRMLWidgets.so
#86 0x00007ffff69a1740 in QWidget::event(QEvent\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libQt5Widgets.so.5
#87 0x00007ffff696343c in QApplicationPrivate::notify_helper(QObject\*, QEvent\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libQt5Widgets.so.5
#88 0x00007ffff696a866 in QApplication::notify(QObject\*, QEvent\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libQt5Widgets.so.5
#89 0x00007ffff7ab4bd7 in qSlicerApplication::notify(QObject\*, QEvent\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libqSlicerBaseQTGUI.so
#90 0x00007ffff589d808 in QCoreApplication::notifyInternal2(QObject\*, QEvent\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libQt5Core.so.5
#91 0x00007ffff69bcfd8 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libQt5Widgets.so.5
#92 0x00007ffff69bdcdb in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libQt5Widgets.so.5
#93 0x00007ffff696343c in QApplicationPrivate::notify_helper(QObject\*, QEvent\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libQt5Widgets.so.5
#94 0x00007ffff6969f20 in QApplication::notify(QObject\*, QEvent\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libQt5Widgets.so.5
#95 0x00007ffff7ab4bd7 in qSlicerApplication::notify(QObject\*, QEvent\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libqSlicerBaseQTGUI.so
#96 0x00007ffff589d808 in QCoreApplication::notifyInternal2(QObject\*, QEvent\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libQt5Core.so.5
#97 0x00007ffff5f70f36 in QGuiApplicationPrivate::processDrop(QWindow\*, QMimeData const\*, QPoint const&amp;, QFlags&lt;Qt::DropAction&gt;, QFlags&lt;Qt::MouseButton&gt;, QFlags&lt;Qt::KeyboardModifier&gt;) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libQt5Gui.so.5
#98 0x00007ffff5f4c1f0 in QWindowSystemInterface::handleDrop(QWindow\*, QMimeData const\*, QPoint const&amp;, QFlags&lt;Qt::DropAction&gt;, QFlags&lt;Qt::MouseButton&gt;, QFlags&lt;Qt::KeyboardModifier&gt;) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libQt5Gui.so.5
#99 0x00007fffcb476df0 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libQt5XcbQpa.so.5
#100 0x00007fffcb47aa44 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libQt5XcbQpa.so.5
#101 0x00007ffff5fad93e in QBasicDrag::eventFilter(QObject\*, QEvent\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libQt5Gui.so.5
#102 0x00007ffff589d478 in QCoreApplicationPrivate::sendThroughApplicationEventFilters(QObject\*, QEvent\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libQt5Core.so.5
#103 0x00007ffff6963478 in QApplicationPrivate::notify_helper(QObject\*, QEvent\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libQt5Widgets.so.5
#104 0x00007ffff6969f20 in QApplication::notify(QObject\*, QEvent\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libQt5Widgets.so.5
#105 0x00007ffff7ab4bd7 in qSlicerApplication::notify(QObject\*, QEvent\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libqSlicerBaseQTGUI.so
#106 0x00007ffff589d808 in QCoreApplication::notifyInternal2(QObject\*, QEvent\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libQt5Core.so.5
#107 0x00007ffff5f6f56d in QGuiApplicationPrivate::processMouseEvent(QWindowSystemInterfacePrivate::MouseEvent\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libQt5Gui.so.5
#108 0x00007ffff5f70955 in QGuiApplicationPrivate::processWindowSystemEvent(QWindowSystemInterfacePrivate::WindowSystemEvent\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libQt5Gui.so.5
#109 0x00007ffff5f4c8ab in QWindowSystemInterface::sendWindowSystemEvents(QFlags&lt;QEventLoop::ProcessEventsFlag&gt;) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libQt5Gui.so.5
#110 0x00007fffcb46569a in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libQt5XcbQpa.so.5
#111 0x00007fffd0514585 in ?? () from /lib/x86_64-linux-gnu/libglib-2.0.so.0
#112 0x00007fffd0573977 in ?? () from /lib/x86_64-linux-gnu/libglib-2.0.so.0
#113 0x00007fffd0513a23 in g_main_context_iteration () from /lib/x86_64-linux-gnu/libglib-2.0.so.0
#114 0x00007ffff58f91cc in QEventDispatcherGlib::processEvents(QFlags&lt;QEventLoop::ProcessEventsFlag&gt;) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libQt5Core.so.5
#115 0x00007ffff589c21a in QEventLoop::exec(QFlags&lt;QEventLoop::ProcessEventsFlag&gt;) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libQt5Core.so.5
#116 0x00007ffff5fad4a3 in QBasicDrag::drag(QDrag\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libQt5Gui.so.5
#117 0x00007ffff5fab286 in QDragManager::drag(QDrag\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libQt5Gui.so.5
#118 0x00007ffff5fab530 in QDrag::exec(QFlags&lt;Qt::DropAction&gt;, Qt::DropAction) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libQt5Gui.so.5
#119 0x00007ffff6baecd4 in QAbstractItemView::startDrag(QFlags&lt;Qt::DropAction&gt;) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libQt5Widgets.so.5
#120 0x00007ffff6bad7f6 in QAbstractItemView::mouseMoveEvent(QMouseEvent\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libQt5Widgets.so.5
#121 0x00007ffff6c15cf3 in QTreeView::mouseMoveEvent(QMouseEvent\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libQt5Widgets.so.5
#122 0x00007ffff69a1740 in QWidget::event(QEvent\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libQt5Widgets.so.5
#123 0x00007ffff6a4a21e in QFrame::event(QEvent\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libQt5Widgets.so.5
#124 0x00007ffff6bae2bc in QAbstractItemView::viewportEvent(QEvent\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libQt5Widgets.so.5
#125 0x00007ffff6c1564c in QTreeView::viewportEvent(QEvent\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libQt5Widgets.so.5
#126 0x00007ffff589d5a0 in QCoreApplicationPrivate::sendThroughObjectEventFilters(QObject\*, QEvent\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libQt5Core.so.5
#127 0x00007ffff6963412 in QApplicationPrivate::notify_helper(QObject\*, QEvent\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libQt5Widgets.so.5
#128 0x00007ffff696a1f8 in QApplication::notify(QObject\*, QEvent\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libQt5Widgets.so.5
#129 0x00007ffff7ab4bd7 in qSlicerApplication::notify(QObject\*, QEvent\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libqSlicerBaseQTGUI.so
#130 0x00007ffff589d808 in QCoreApplication::notifyInternal2(QObject\*, QEvent\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libQt5Core.so.5
#131 0x00007ffff696953a in QApplicationPrivate::sendMouseEvent(QWidget\*, QMouseEvent\*, QWidget\*, QWidget\*, QWidget\*\*, QPointer&amp;, bool, bool) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libQt5Widgets.so.5
#132 0x00007ffff69bafe8 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libQt5Widgets.so.5
#133 0x00007ffff69bdcf3 in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libQt5Widgets.so.5
#134 0x00007ffff696343c in QApplicationPrivate::notify_helper(QObject\*, QEvent\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libQt5Widgets.so.5
#135 0x00007ffff6969f20 in QApplication::notify(QObject\*, QEvent\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libQt5Widgets.so.5
#136 0x00007ffff7ab4bd7 in qSlicerApplication::notify(QObject\*, QEvent\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libqSlicerBaseQTGUI.so
#137 0x00007ffff589d808 in QCoreApplication::notifyInternal2(QObject\*, QEvent\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libQt5Core.so.5
#138 0x00007ffff5f6f56d in QGuiApplicationPrivate::processMouseEvent(QWindowSystemInterfacePrivate::MouseEvent\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libQt5Gui.so.5
#139 0x00007ffff5f70955 in QGuiApplicationPrivate::processWindowSystemEvent(QWindowSystemInterfacePrivate::WindowSystemEvent\*) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libQt5Gui.so.5
#140 0x00007ffff5f4c8ab in QWindowSystemInterface::sendWindowSystemEvents(QFlags&lt;QEventLoop::ProcessEventsFlag&gt;) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libQt5Gui.so.5
#141 0x00007fffcb46569a in ?? () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libQt5XcbQpa.so.5
#142 0x00007fffd0514585 in ?? () from /lib/x86_64-linux-gnu/libglib-2.0.so.0
#143 0x00007fffd0573977 in ?? () from /lib/x86_64-linux-gnu/libglib-2.0.so.0
#144 0x00007fffd0513a23 in g_main_context_iteration () from /lib/x86_64-linux-gnu/libglib-2.0.so.0
#145 0x00007ffff58f91cc in QEventDispatcherGlib::processEvents(QFlags&lt;QEventLoop::ProcessEventsFlag&gt;) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libQt5Core.so.5
#146 0x00007ffff589c21a in QEventLoop::exec(QFlags&lt;QEventLoop::ProcessEventsFlag&gt;) () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libQt5Core.so.5
#147 0x00007ffff58a51d3 in QCoreApplication::exec() () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libQt5Core.so.5
#148 0x00007ffff794653a in qSlicerCoreApplication::exec() () from /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin/../lib/Slicer-5.11/libqSlicerBaseQTCore.so
#149 0x00000000004059dc in ?? ()
#150 0x00007fffd022a1ca in \__libc_start_call_main (main=main@entry=0x405830, argc=argc@entry=1, argv=argv@entry=0x7fffffffba08) at ../sysdeps/nptl/libc_start_call_main.h:58
#151 0x00007fffd022a28b in \__libc_start_main_impl (main=0x405830, argc=1, argv=0x7fffffffba08, init=, fini=, rtld_fini=, stack_end=0x7fffffffb9f8) at ../csu/libc-start.c:360
#152 0x0000000000405a9e in ?? ()
</code></pre>

---

## Post #17 by @muratmaga (2026-05-11 23:02 UTC)

<p>This is what Claude Code interpretted this as:</p>
<pre><code class="lang-auto">Yes — this trace shows a fairly diagnosable failure, and the most interesting clue is in frame 0.

What it crashed doing
You drag-dropped a volume onto the 3D view:

frame 85: qMRMLThreeDView::dropEvent
frame 80: showVolumeRendering (the SH plugin's "show in view" path)
frame 79–78: CreateDefaultVolumeRenderingNodes → SetRecommendedVolumeRenderingProperties
That triggered a render, and the GPU ray-cast mapper tried to set up its noise texture:

frame 19: vtkOpenGLRenderWindow::GetNoiseTextureUnit
frames 18→12: it ran a pipeline update on a vtkJPEGReader (the noise pattern is being loaded from a JPEG)
frame 12: vtkImageReader2::ComputeInternalFileName
frames 11–10: vtk::to_std_format / vtk::is_printf_format — VTK 9.6 uses std::regex here to translate filename patterns like %03d into {:03d} form
frames 7→0: deep inside std::regex compilation, dying in _Scanner::_M_scan_normal
The smoking gun
Look at where frame 0 resolves:


#0 std::__detail::_Scanner::_M_scan_normal() ()
   from .../libQt5WebEngineCore.so.5
That's a libstdc++ template symbol — but the dynamic linker is binding it inside QtWebEngineCore. QtWebEngine ships its own Chromium-internal copies of various C++ template instantiations and exports them, and on Ubuntu 24.04 with its newer glibc/libstdc++ those exported copies are getting picked over the system libstdc++. Frame 1 has a sibling weirdness — a _Compiler symbol resolved into libvtkInfovisCore. So the regex machinery is being stitched together from three different libraries' copies, which is exactly the kind of ABI Frankenstein that segfaults in _M_scan_normal.

This is a symbol interposition / ODR violation between QtWebEngine's bundled Chromium libstdc++ symbols and the system one — not a problem with your data or your GPU.
</code></pre>

---

## Post #18 by @pieper (2026-05-11 23:07 UTC)

<p>ha ha, well I do think Claude nailed this one (or even it it’s not exactly right it’s certainly plausible and well described!).</p>
<aside class="quote no-group" data-username="Claude" data-post="17" data-topic="46974">
<div class="title">
<div class="quote-controls"></div>
 Claude:</div>
<blockquote>
<p><code>exactly the kind of ABI Frankenstein that segfaults</code></p>
</blockquote>
</aside>

---

## Post #19 by @muratmaga (2026-05-12 05:56 UTC)

<p>So is a fix likely? because we can’t use Slicer properly on MorphoCloud (with builds after March 6th).</p>

---

## Post #20 by @chir.set (2026-05-12 11:25 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="5" data-topic="46974">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>export QT_QPA_PLATFORM=xcb</p>
</blockquote>
</aside>
<p>The above is true for self-built Slicer, but not for the factory Slicer package.</p>

---

## Post #21 by @pieper (2026-05-12 12:57 UTC)

<p>My Claude found this which seems relevant: <a href="https://discourse.slicer.org/t/cannot-import-gmsh-python-package/29344" class="inline-onebox">Cannot import gmsh Python package</a></p>
<p>It also came up with all these suggestions.</p>
<blockquote>
<p><img src="https://emoji.discourse-cdn.com/twitter/robot.png?v=15" title=":robot:" class="emoji" alt=":robot:" loading="lazy" width="20" height="20"> The rest of this post is AI-generated content.</p>
</blockquote>
<h2><a name="p-133731-concrete-debugging-plan-what-id-ask-murat-to-run-1" class="anchor" href="#p-133731-concrete-debugging-plan-what-id-ask-murat-to-run-1" aria-label="Heading link"></a>Concrete debugging plan (what I’d ask Murat to run)</h2>
<ol>
<li><strong>Capture a real backtrace, not just frame 0:</strong></li>
</ol>
<pre><code class="lang-auto">ulimit -c unlimited
./Slicer            # reproduce crash
coredumpctl gdb     # or: gdb ./bin/SlicerApp-real core
(gdb) bt full
(gdb) info sharedlibrary
(gdb) info proc mappings
</code></pre>
<p>Frame 0 alone tells us nothing about the caller; <code>bt full</code> will show which Slicer/VTK code fed garbage into the regex.<br>
2. <strong>Identify which libstdc++ is actually loaded at the crash site:</strong></p>
<pre><code class="lang-auto">cd Slicer-5.11.0-2026-05-05-linux-amd64
LD_DEBUG=libs ./Slicer 2&gt;&amp;1 | grep -E 'libstdc\+\+|libgcc_s' | head
ldd bin/SlicerApp-real | grep -E 'stdc\+\+|gcc_s'
strings -a $(ldd bin/SlicerApp-real | awk '/libstdc\+\+/{print $3}') \
  | grep -E '^GLIBCXX_[0-9]' | sort -V | tail
strings -a /usr/lib/x86_64-linux-gnu/libstdc++.so.6 \
  | grep -E '^GLIBCXX_[0-9]' | sort -V | tail
</code></pre>
<p>If those two GLIBCXX max versions differ, that’s the smoking gun.<br>
3. <strong>Run with a clean environment to rule out conda contamination:</strong></p>
<pre><code class="lang-auto">env -i HOME=$HOME PATH=/usr/bin:/bin DISPLAY=$DISPLAY \
    LANG=C.UTF-8 LC_ALL=C.UTF-8 \
    ./Slicer
</code></pre>
<p>If that fixes it, walk <code>printenv | grep -E 'LD_|PYTHON|CONDA'</code> to find the offending var.<br>
4. <strong>Check the locale path</strong> (cheap and worth ruling out):</p>
<pre><code class="lang-auto">locale ; locale -a | grep -i utf
</code></pre>
<ol start="5">
<li><strong>Bisect the factory builds.</strong> <a href="http://download.slicer.org">download.slicer.org</a> keeps weekly Linux previews; install three or four (e.g. 2026-04-01, 2026-04-15, 2026-04-28, 2026-05-05) and find the first that crashes on Murat’s box. Then <code>git log --oneline &lt;good_rev&gt;..&lt;bad_rev&gt;</code> on Slicer + look at Superbuild revisions of VTK/Qt for that span. (The thread does <em>not</em> yet identify a regressing commit, despite what the WebFetch summary claimed.)</li>
<li><strong>If frame 0’s <code>bt full</code> shows the regex string is empty / null / garbage</strong>, the bug is most likely on the <em>Slicer</em> side (a recent change that passes an uninitialized <code>std::string</code> to <code>std::regex</code>), not glibc. Same fix shape as the 2022 <code>vtkSlicerVolumeRenderingLogic::CreateROINode</code> regression in <a>2022-01-10</a>.</li>
</ol>
<h2><a name="p-133731-fix-paths-2" class="anchor" href="#p-133731-fix-paths-2" aria-label="Heading link"></a>Fix paths</h2>
<ul>
<li><strong>If libstdc++ mismatch is confirmed</strong> (step 2): ship a vendored <code>libstdc++.so.6</code> in <code>Slicer-5.11/lib/</code> and add it to the launcher’s <code>LD_LIBRARY_PATH</code> ahead of system. Slicer used to do this; if it was dropped, that’s the regression. Cheapest verification: <code>cp /usr/lib/.../libstdc++.so.6 lib/Slicer-5.11/</code> on the build machine, re‑run, see if the crash goes away.</li>
<li><strong>If it’s a conda/Anaconda env pollution:</strong> add a launcher guard that scrubs <code>LD_LIBRARY_PATH</code> entries containing <code>anaconda</code>/<code>miniconda</code>/<code>conda</code> before exec, and document it.</li>
<li><strong>If it’s a real null‑string fed into <code>std::regex</code>:</strong> fix the call site (<code>bt full</code> will name it). No glibc involvement.</li>
<li><strong>For chir.set’s Wayland/GLX issue</strong> (separate): have Slicer’s launcher detect <code>XDG_SESSION_TYPE=wayland</code> + Qt5 and default <code>QT_QPA_PLATFORM=xcb</code>, since Slicer’s Qt5 has no working Wayland path with the VTK GL contexts.</li>
</ul>
<p>Want me to draft the launcher patch for the Wayland default, or to scaffold a <code>slicer-debug-libs.sh</code> script that runs steps 1–4 in one go?</p>

---

## Post #22 by @muratmaga (2026-05-12 15:00 UTC)

<p>I don’t really know what to do with this.</p>
<ol>
<li>It is already clear in my case that the breaking change is around vtk9.5.1-&gt;9.6.0 commit in March. After that, slicer crashes. (this specifically: <a href="https://github.com/Slicer/Slicer/commit/1b21266bf47f126ece58d12b87160e38f55ad258" class="inline-onebox" rel="noopener nofollow ugc">ENH: Add support for building against VTK version 9.6.0 · Slicer/Slicer@1b21266 · GitHub</a>)</li>
<li>I do not use conda or inject LD_LIBRARY_PATH.</li>
</ol>
<p>The rest I have no clue.</p>

---

## Post #23 by @pieper (2026-05-12 17:26 UTC)

<p>Okay, after our discussion at the developer meeting <a class="mention" href="/u/lassoan">@lassoan</a> suggested that a workaround would be to disable surface smoothing in the volume renderer:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd8ef966205927ad1342234893b8a4368afec9f2.png" alt="image" data-base62-sha1="tkscxzX1jWiU3iMG7ROiPvEJUBA" width="330" height="96"></p>
<p>I tested and I can get the crash with the current preview build if it turn on this feature, so it does seem to be the thing that triggers the bad code path.  <a class="mention" href="/u/muratmaga">@muratmaga</a> can you confirm?</p>
<p>We also realized that the builds with the crash are actually using the new VTK version, so this is probably what triggered the underlying issue.  I’ll try some of the things Claude suggested and see if I can get any more info on any underlying glibc issues.</p>

---

## Post #24 by @pieper (2026-05-12 21:02 UTC)

<blockquote>
<p><img src="https://emoji.discourse-cdn.com/twitter/robot.png?v=15" title=":robot:" class="emoji" alt=":robot:" loading="lazy" width="20" height="20"> This post was written with AI assistance.</p>
</blockquote>
<p>So after some testing it looks like there’s a C++ issue that I won’t try to explain that happens on linux and has to do with the way VTK compiles by default.</p>
<p>Probably we can patch it with these flags when building VTK:</p>
<pre><code class="lang-auto">  ...
  CMAKE_CACHE_ARGS
    ...
    -DCMAKE_CXX_VISIBILITY_PRESET:STRING=hidden
    -DCMAKE_VISIBILITY_INLINES_HIDDEN:BOOL=ON
    -DCMAKE_SHARED_LINKER_FLAGS:STRING=-Wl,-Bsymbolic-functions
)
</code></pre>
<p>It would be better for VTK to be built like this by default, but we can do this as a workaround if we want.</p>
<p>For the very short run, just turning off the surface smoothing in volume rendering is a patch.</p>
<p>The underlying issue is illustrated by just running this script.  Maybe we can refine this here and then file an issue in the VTK gitlab with the suggested fix.</p>
<pre><code class="lang-auto">exouser@sdp-test-volume-render:~/Downloads$ cat ~/repo.sh 
#!/usr/bin/env bash
# Reproducer: VTK 9.6 std::regex ODR exposure on Linux/ELF.
# Paste into any Linux box with g++, python3-venv, and an older g++ available.
set -euo pipefail

OLDGCC=${OLDGCC:-g++-9}            # override if g++-9 missing; try g++-11 or g++-13
if ! command -v "$OLDGCC" &gt;/dev/null; then
  cat &gt;&amp;2 &lt;&lt;EOF
need $OLDGCC in PATH.
  Ubuntu/Debian: sudo apt-get update &amp;&amp; sudo apt-get install -y $OLDGCC
                 (older series may need 'universe' enabled, or try OLDGCC=g++-11)
  Fedora/RHEL:   sudo dnf install -y gcc-toolset-11-gcc-c++
                 then: scl enable gcc-toolset-11 -- bash  (and re-run this script)
  Arch:          sudo pacman -S gcc11   (then OLDGCC=g++-11 $0)
override the version on the command line, e.g.:  OLDGCC=g++-11 $0
EOF
  exit 1
fi

W=$(mktemp -d); cd "$W"
echo "workdir: $W"
echo "old g++:     $($OLDGCC --version | head -1)"
echo "default g++: $(g++ --version  | head -1)"

cat &gt; companion.cxx &lt;&lt;'CXX'
#include &lt;regex&gt;
extern "C" void companion_touch() {
  static std::regex r("(a)|(b)|(c)"); (void)r;
}
CXX

"$OLDGCC" -shared -fPIC -O2 companion.cxx -o libcompanion.so

python3 -m venv .venv &amp;&amp; . .venv/bin/activate
pip install --quiet 'vtk&gt;=9.6'

PYCALL='import vtk; r=vtk.vtkImageReader2(); r.ComputeInternalFileName(0); print("VTK",vtk.VTK_VERSION,"ok:",repr(r.GetInternalFileName()))'

echo; echo "=== 1. bare run ==="
python -c "$PYCALL"


echo; echo "=== 2. companion preloaded (LD_PRELOAD) ==="
err=$(mktemp)
set +e
LD_PRELOAD=$PWD/libcompanion.so python -c "$PYCALL" 2&gt; &gt;(tee "$err" &gt;&amp;2)
rc=$?
set -e
echo
if [ $rc -eq 0 ]; then
  echo "&gt;&gt;&gt; RESULT: did NOT reproduce (clean exit)."
  echo "&gt;&gt;&gt;         Try a wider GCC gap: OLDGCC=g++-9 (or g++-7) $0"
elif [ $rc -ge 128 ]; then
  sig=$((rc - 128)); name=$(kill -l "$sig" 2&gt;/dev/null || echo "?")
  case "$name" in
    SEGV|ABRT|BUS|ILL|FPE)
      echo "&gt;&gt;&gt; RESULT: BUG REPRODUCED."
      echo "&gt;&gt;&gt;         Process killed by SIG$name (signal $sig, exit $rc)."
      if grep -q 'bad_alloc\|terminate called' "$err"; then
        echo "&gt;&gt;&gt;         libstdc++ aborted from an uncaught exception (e.g. std::bad_alloc)."
        echo "&gt;&gt;&gt;         This is the same ODR-drift class as the SIGSEGV seen in the field."
        echo "&gt;&gt;&gt;         _Compiler is built with one layout, walked with another;"
        echo "&gt;&gt;&gt;         the corrupted state can deref a bad pointer (SIGSEGV) OR request"
        echo "&gt;&gt;&gt;         an absurd allocation (bad_alloc -&gt; terminate -&gt; SIGABRT)."
      else
        echo "&gt;&gt;&gt;         Same crash class as Murat's field SIGSEGV in vtkStringFormatter."
      fi
      ;;
    *)
      echo "&gt;&gt;&gt; RESULT: killed by SIG$name (signal $sig); inconclusive."
      ;;
  esac
else
  echo "&gt;&gt;&gt; RESULT: exited $rc (non-zero but not a signal). Not a crash; probably a Python-level error."
fi
rm -f "$err"



echo; echo "=== 3. which library wins the _Compiler template symbol ==="
for env in "" "LD_PRELOAD=$PWD/libcompanion.so"; do
  echo "-- env: ${env:-none}"
  env $env gdb --batch -q \
    -ex 'set breakpoint pending on' \
    -ex 'b vtkImageReader2::ComputeInternalFileName' \
    -ex 'run' \
    -ex "info sym 'std::__detail::_Compiler&lt;std::__cxx11::regex_traits&lt;char&gt; &gt;::_M_alternative()'" \
    --args python -c "$PYCALL" 2&gt;/dev/null | grep -E '^\$|in section|libcompanion|libvtk|libstdc' || true
done
</code></pre>

---

## Post #25 by @muratmaga (2026-05-12 21:06 UTC)

<aside class="quote no-group" data-username="pieper" data-post="23" data-topic="46974">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> can you confirm?</p>
</blockquote>
</aside>
<p>Yep, disabling surface smoothing makes rendering possible.</p>

---

## Post #26 by @pieper (2026-05-13 14:44 UTC)

<p>I filed an issue on the vtk tracker here: <a href="https://gitlab.kitware.com/vtk/vtk/-/work_items/20047">https://gitlab.kitware.com/vtk/vtk/-/work_items/20047</a></p>

---

## Post #27 by @jamesobutler (2026-05-13 19:23 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> Can you try uninstalling the VTK Python package that Slicer builds and instead pip install the VTK whl from PyPI? I would suspect there are some differences in how we configure and build the whl versus VTK.</p>

---

## Post #28 by @pieper (2026-05-13 19:39 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a> it should be the same either way.  The script I sent uses the VTK pip package and a python that is independent to Slicer.</p>

---

## Post #29 by @jamesobutler (2026-05-14 01:01 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> I asked because I was thinking about</p>
<p><code>_GLIBCXX_USE_CXX11_ABI=0</code></p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://gitlab.kitware.com/vtk/vtk/-/work_items/1991">
  <header class="source">

      <a href="https://gitlab.kitware.com/vtk/vtk/-/work_items/1991" target="_blank" rel="noopener nofollow ugc">gitlab.kitware.com</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://gitlab.kitware.com/vtk/vtk/-/work_items/1991" target="_blank" rel="noopener nofollow ugc">Verifying connection...</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Does the issue happen in Slicer core with no extensions installed with its self-built VTK whl or does a Slicer extension install a specific VTK whl that pulls from PyPI that is using a different <code>_GLIBCXX_USE_CXX11_ABI</code>?</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/8168">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/8168" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/8168" target="_blank" rel="noopener nofollow ugc">BUG: Add support for configuring `_manylinux` module (#8168)</a>
      </h4>

    <div class="branches">
      <code>main</code> ← <code>jcfr:ensure-manylinux-abi-compat</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2025-01-24" data-time="00:52:56" data-timezone="UTC">12:52AM - 24 Jan 25 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/jcfr" target="_blank" rel="noopener nofollow ugc">
            <img alt="" src="https://avatars.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
            jcfr
          </a>
        </div>

        <div class="lines" title="1 commits changed 2 files with 187 additions and 0 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/8168/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+187</span>
            <span class="removed">-0</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This commit introduces the ability to configure a `_manylinux` module in the Sli<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/8168" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">cer build system to enhance compatibility when installing binary Python wheels.

This update resolves potential issues with installing Python wheels built for newer GLIBC versions or ABIs, which could cause crashes in environments with older configurations.

Specifically, installing `manylinux_2_28_x86_64` ITK wheels compiled with `_GLIBCXX_USE_CXX11_ABI=1` was causing segmentation faults in the _Stable_ Slicer version, which is compiled with `_GLIBCXX_USE_CXX11_ABI=0`. The `_manylinux` module ensures that `manylinux_2_17_x86_64` ITK wheels are always installed, even when Slicer and its associated Python interpreter are executed on newer operating systems.

The `_manylinux.py` module is dynamically generated during the build process and ensures that Python packages installed via `pip` are compatible with the GLIBC version used in the Slicer build environment.

### Summary of Changes

**`External_python.cmake`**:
- Added logic to configure `_manylinux.py` for Linux-based build environments.
- By default, `_manylinux.py` is generated. If disabled using the CMake option `PYTHON_CONFIGURE_MANYLINUX_MODULE`, any existing `_manylinux.py` module is removed to prevent inadvertent impacts on Python package installations.
- Introduced a CMake option `PYTHON_REMOVE_MANYLINUX_MODULE_IF_EXISTS` to allow users to disable the removal of an existing `_manylinux.py` module.

**`python_configure_manylinux_module.cmake`**:
- New CMake script to detect the system's GLIBC version using `ldd`.
- Dynamically generates the `_manylinux.py` module, which includes:
  - A `manylinux_compatible` function to override the default behavior of `pip` for checking compatibility of manylinux tags.
  - Embedded documentation and compatibility checks to prevent crashes caused by mismatched ABI or GLIBC versions.

By restricting installed packages to compatible manylinux tags, this update ensures stability and reliability for Python packages in the Slicer ecosystem.

### References

- [PEP 600: Manylinux Platform Tag](https://peps.python.org/pep-0600/)
- [GCC Dual ABI Documentation](https://gcc.gnu.org/onlinedocs/libstdc++/manual/using_dual_abi.html)</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="quote quote-modified" data-post="1" data-topic="43802">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/slicer-build-environment-upgraded-to-qt5-almalinux8-gcc14/43802">Slicer Build Environment Upgraded to `qt5-almalinux8-gcc14`</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #000000;" data-drop-close="true" class="badge-category --style-square " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
    </div>
  </div>
  <blockquote>
    The build environment used for generating Slicer Preview and its extensions has been upgraded from qt5-centos7-gcc7 to qt5-almalinux8-gcc14. 
This update brings improved C++ standards support, better compatibility with modern systems, and eliminates complications related to the Dual ABI issue previously discussed <a href="https://discourse.slicer.org/t/temporary-disabling-of-stable-extension-builds-in-preparation-for-slicer-5-8-release-visual-studio-update/41207/7">here</a>. 
<a name="p-126953-comparison-of-build-environments-1" class="anchor" href="#p-126953-comparison-of-build-environments-1" aria-label="Heading link"></a>Comparison of Build Environments




Build Environment
Minimum Required glibc
Manylinux Policy
GCC Version
Compatible Systems




qt5-centos7-gcc7
2.17
manylinux2014, manylinux_2…
  </blockquote>
</aside>

<p>Latest VTK on PyPI only provide x86_64 whls that are manylinux_2_17 as they provide manylinux_2_28 whl for ARM64 Linux only. <a href="https://pypi.org/project/vtk/9.6.1/#files" class="inline-onebox" rel="noopener nofollow ugc">vtk · PyPI</a></p>

---

## Post #30 by @lassoan (2026-05-14 06:21 UTC)

<p>I’ve checked and libQt<em>WebEngineCore.so.</em> contains incorrectly exported std symbols until Qt-6.6, but the problem got fixed in Qt-6.7. So, the simplest fix the crash in Slicer would be to upgrade to Qt-6.7 or higher.</p>
<p>It is nice if we also fix this in VTK, because that way we avoid crashes in the future when any other software component incorrectly exports symbols. The flags that were proposed above (CMAKE_CXX_VISIBILITY_PRESET, CMAKE_VISIBILITY_INLINES_HIDDEN, etc.) were already set, but Claude suggested a <a href="https://github.com/Kitware/VTK/commit/cd15bea2b99bf3feaf51ff332fc5ae7d7199a4ef">small, localized change that made the global std:: symbols disappear</a>. –  <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> or <a class="mention" href="/u/ebrahim">@ebrahim</a> could you patch VTK on factory with this commit and create a nightly linux build with it to confirm the fix and test that there are no regressions?</p>

---

## Post #31 by @pieper (2026-05-14 13:00 UTC)

<p>If making a custom build today is not feasible, we could just apply this patch to Slicer/VTK and check the build tomorrow.</p>

---

## Post #32 by @jamesobutler (2026-05-14 13:45 UTC)

<p>Here’s the correct gitlab link that I was trying to post regarding a:</p>
<blockquote>
<p>Mixing old and new ABIs in the same application causes crashes in <code>std::regex</code> due to a known libstdc++ bug:</p>
</blockquote>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://gitlab.kitware.com/vtk/vtk/-/work_items/19919">
  <header class="source">

      <a href="https://gitlab.kitware.com/vtk/vtk/-/work_items/19919" target="_blank" rel="noopener nofollow ugc">gitlab.kitware.com</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://gitlab.kitware.com/vtk/vtk/-/work_items/19919" target="_blank" rel="noopener nofollow ugc">Verifying connection...</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #33 by @pieper (2026-05-27 13:28 UTC)

<p>Issue is being tracked here:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/9181">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/9181" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/9181" target="_blank" rel="noopener">`std::regex` crash</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2026-05-26" data-time="15:12:23" data-timezone="UTC">03:12PM - 26 May 26 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/sjh26" target="_blank" rel="noopener">
          <img alt="" src="https://avatars.githubusercontent.com/u/25040869?v=4" class="onebox-avatar-inline" width="20" height="20">
          sjh26
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">@lassoan</p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
