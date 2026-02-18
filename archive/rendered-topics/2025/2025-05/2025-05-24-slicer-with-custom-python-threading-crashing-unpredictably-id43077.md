# Slicer with custom Python threading crashing unpredictably

**Topic ID**: 43077
**Date**: 2025-05-24
**URL**: https://discourse.slicer.org/t/slicer-with-custom-python-threading-crashing-unpredictably/43077

---

## Post #1 by @pedr0sorio (2025-05-24 14:28 UTC)

<p>Dear Slicer Community,</p>
<p>I have been building a custom slicer extension that allows me to do localised modifications in a CT scan using some AI models running in a Flask server that I access with <code>requests</code>.</p>
<p>The extension I implemented follows a structure similar to this <a href="https://github.com/bowang-lab/MedSAMSlicer/tree/MedSAM2" rel="noopener nofollow ugc">MedSAM extension here</a>.</p>
<p>My extension works well most of the time, but, at times, for reasons I have not been yet able to determine, I am encountering that Slicer suddenly crashes.</p>
<p>Things I have checked:</p>
<ul>
<li>CPU and RAM usage before crash is not larger than usual.</li>
<li>Following this <a href="https://discourse.slicer.org/t/full-slicer-cache-leads-to-performance-problems-with-monailabel/23305/2">other issue documented in this community</a> I have increased the cache size to 10000MBs. This seemed to decrease the frequency of the crashes but they still happen occasionally.</li>
<li>Crashes can happen right before/during I write some DICOM data to <code>qt.QTemporaryDir()</code> for later sending it to my server via <code>requests</code>. Although, they can also happen right after incorporating the predictions of the model into the scene.</li>
<li>Checking the logs after the crash in a new Slicer session are not informative. There aren’t any specific errors, just simply blank after my last debugging print.</li>
</ul>
<p>The crashes don’t happen always but I need to understand how to avoid them completely. Do you have any ideas?</p>
<p>Thanks in advance!<br>
Best,<br>
Pedro</p>

---

## Post #2 by @lassoan (2025-05-24 14:36 UTC)

<p>The easiest would be to get a stack trace to see where exactly the crash occurs. It is even better if you run the code step by step in a debugger, then you can see exactly what leads to the issue. Also, make sure you use the matest main version of the source code, as we keep improving the code.</p>
<p>If you are interested in interactive AI segmentation then I would recommend to try NNInteractive extension. Based on my experience, it is way better than any SAM variants: it is natively 3D, fast, and accurate, and you can use it to edit or refine existing 3D segmentations. I would say NNInteractive is the first practically useful interactive medical AI segmentation tool.</p>

---

## Post #3 by @pedr0sorio (2025-05-30 09:28 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="43077">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>a stack trace to see where exactly the crash occurs. It is even better if you run the code step by step in a debugger, then you can see exactly what leads to the issue. Also, make sure you use the matest main version of the source code, as we keep improving the code.</p>
</blockquote>
</aside>
<p>Thanks for the fast response! I have been investigating possible causes and I wonder if my sporadic crashes are due to the fact that I am using the <code>threading</code> python lib in my extension’s logic module.</p>
<p>Considering I am running a python function in my ScriptedLoadableModuleLogic class which performs multiple different API calls to a server. For one of these requests due it taking beyond a minute to complete I am using <code>threading</code> lib to run it in a different thread and still be able to update a progress bar (slicer.util.createProgressDialog) based on the processing time that has passed.</p>
<p>I have since realised from the <a href="https://github.com/KitwareMedical/SlicerNNUnet" rel="noopener nofollow ugc">SlicerNNUnet</a> extension one can use <code>qt.QProcess()</code> to run a CLI program in a different process. Do you think running all my API calls in a different process could help minimise the crashes? Finally, is there any added benefit to using <code>qt.QProcess()</code> for that rather than python’s <code>multiprocessing</code>?</p>
<p>Thanks for the help so far!</p>
<p>Best,<br>
Pedro</p>

---

## Post #4 by @lassoan (2025-05-30 12:47 UTC)

<aside class="quote no-group" data-username="pedr0sorio" data-post="3" data-topic="43077">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/pedr0sorio/48/80267_2.png" class="avatar"> pedr0sorio:</div>
<blockquote>
<p>I wonder if my sporadic crashes are due to the fact that I am using the <code>threading</code> python lib in my extension’s logic module.</p>
</blockquote>
</aside>
<p>Yes, absolutely. Threading is complex and it is easy to cause crashes. For example, if you make any modifications to any nodes in a worker thread then the application will crash. You can make modifications to a copy of the data on a worker thread then signal to the main thread that new data is available, for example using a Python <a href="https://docs.python.org/3/library/queue.html">queue</a>. The main thread can regularly check the queue using a QTimer and if it finds that there is updated data, it can update nodes in the scene.</p>
<p>Using a subprocess for running tasks in parallel is a good way to isolate the background operations from the main thread, so crashes cannot occur. This is good for any tasks that take longer than a couple of seconds (because then the overhead of starting a new process is negligible). This is also good if the processing is resource-intensive (e.g., uses lots of memory) or the implementation is not robust (it may crash) because in case of a crash, the main application does not crash. You can also terminate the subprocess anytime (while you can just nicely ask a thread to terminate, but it may or may not actually stop).</p>
<p>You can find examples for both running a background process and using background threads to not block the GUI in <a href="https://github.com/lassoan/SlicerMONAIAuto3DSeg/blob/main/MONAIAuto3DSeg/MONAIAuto3DSegLib/process.py">MONAIAuto3DSeg extension</a>.</p>

---

## Post #5 by @pedr0sorio (2025-06-17 09:50 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="43077">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>he main thread can regularly check the queue using a QTimer and if it finds that there is updated data, it can update nodes in the scene.</p>
<p>Using a subprocess for running tasks in parallel is a good way to isolate the background operations from the main thread, so crashes cannot occur. This is good for any tasks that take longer than a couple of seconds (because then the overhead of starting a new process is negligible). This is also good if the processing is resource-intensive (e.g., uses lots of memory) or the impleme</p>
</blockquote>
</aside>
<p>Thank <a class="mention" href="/u/lassoan">@lassoan</a> for the insight.</p>
<p>Following the advice I have restructured my extension to use qt.Process to run the longest API request (few minutes) in a subprocess to not clog Slicer and hopefully avoid the crashes I am having entirely.</p>
<p>After doing so I still get these crashes. My Mac’s problem report for slicer shows the following massive log which is not much different than what I got before running the long API call in the subprocess:</p>
<pre><code class="lang-auto">-------------------------------------
Translated Report (Full Report Below)
-------------------------------------

Process:               Slicer [81080]
Path:                  /Applications/Slicer 5.8.1.app/Contents/MacOS/Slicer
Identifier:            org.slicer.slicer
Version:               5.8.1 (5.8.1)
Code Type:             X86-64 (Translated)
Parent Process:        launchd [1]
User ID:               503

Date/Time:             2025-06-17 11:42:25.5227 +0200
OS Version:            macOS 15.5 (24F74)
Report Version:        12
Anonymous UUID:        C1A7B4D7-410D-E9E1-224F-B59CB3F6C79E

Sleep/Wake UUID:       E3B5FAD0-0324-40EB-9A2F-1409830AFBCC

Time Awake Since Boot: 95000 seconds
Time Since Wake:       11997 seconds

System Integrity Protection: enabled

Notes:
RIP register does not match crashing frame (0xEE000000014CDD94 vs 0x100EE0A38)

Crashed Thread:        30  Dispatch queue: com.Metal.CompletionQueueDispatch

Exception Type:        EXC_BAD_ACCESS (SIGSEGV)
Exception Codes:       KERN_INVALID_ADDRESS at 0xee000000014cdd94 -&gt; 0x00000000014cdd94 (possible pointer authentication failure)
Exception Codes:       0x0000000000000001, 0xee000000014cdd94

Termination Reason:    Namespace SIGNAL, Code 11 Segmentation fault: 11
Terminating Process:   exc handler [81080]

VM Region Info: 0x14cdd94 is not in any region.  Bytes before following region: 4282413676
      REGION TYPE                    START - END         [ VSIZE] PRT/MAX SHRMOD  REGION DETAIL
      UNUSED SPACE AT START
---&gt;  
      __TEXT                      1008d5000-10091d000    [  288K] r-x/r-x SM=COW  /Applications/Slicer 5.8.1.app/Contents/MacOS/Slicer

Error Formulating Crash Report:
RIP register does not match crashing frame (0xEE000000014CDD94 vs 0x100EE0A38)

Thread 0::  Dispatch queue: com.apple.main-thread
0   libpython3.9.dylib            	       0x13a3f6386 _PyDict_GetItem_KnownHash + 54
1   libpython3.9.dylib            	       0x13a43e0d8 find_name_in_mro + 152
2   libpython3.9.dylib            	       0x13a43df9f _PyType_Lookup + 111
3   libpython3.9.dylib            	       0x13a42b5cb _PyObject_GenericGetAttrWithDict + 123
4   libpython3.9.dylib            	       0x13a4d9f2e _PyEval_EvalFrameDefault + 19758
5   libpython3.9.dylib            	       0x13a4df968 _PyEval_EvalCode + 2360
6   libpython3.9.dylib            	       0x13a3daf89 _PyFunction_Vectorcall + 265
7   libpython3.9.dylib            	       0x13a4dec7d call_function + 413
8   libpython3.9.dylib            	       0x13a4db5e4 _PyEval_EvalFrameDefault + 25572
9   libpython3.9.dylib            	       0x13a4df968 _PyEval_EvalCode + 2360
10  libpython3.9.dylib            	       0x13a3daf89 _PyFunction_Vectorcall + 265
11  libpython3.9.dylib            	       0x13a3dac7b PyVectorcall_Call + 155
12  libpython3.9.dylib            	       0x13a4dba18 _PyEval_EvalFrameDefault + 26648
13  libpython3.9.dylib            	       0x13a4df968 _PyEval_EvalCode + 2360
14  libpython3.9.dylib            	       0x13a3daf89 _PyFunction_Vectorcall + 265
15  libpython3.9.dylib            	       0x13a4dec7d call_function + 413
16  libpython3.9.dylib            	       0x13a4db5e4 _PyEval_EvalFrameDefault + 25572
17  libpython3.9.dylib            	       0x13a3db093 function_code_fastcall + 163
18  libpython3.9.dylib            	       0x13a3ed4ba method_vectorcall + 202
19  libpython3.9.dylib            	       0x13a4dec7d call_function + 413
20  libpython3.9.dylib            	       0x13a4db5e4 _PyEval_EvalFrameDefault + 25572
21  libpython3.9.dylib            	       0x13a4df968 _PyEval_EvalCode + 2360
22  libpython3.9.dylib            	       0x13a3daf89 _PyFunction_Vectorcall + 265
23  libpython3.9.dylib            	       0x13a3ed5ec method_vectorcall + 508
24  libpython3.9.dylib            	       0x13a4dba18 _PyEval_EvalFrameDefault + 26648
25  libpython3.9.dylib            	       0x13a4df968 _PyEval_EvalCode + 2360
26  libpython3.9.dylib            	       0x13a3daf89 _PyFunction_Vectorcall + 265
27  libpython3.9.dylib            	       0x13a3ed5ec method_vectorcall + 508
28  libpython3.9.dylib            	       0x13a4dba18 _PyEval_EvalFrameDefault + 26648
29  libpython3.9.dylib            	       0x13a4df968 _PyEval_EvalCode + 2360
30  libpython3.9.dylib            	       0x13a3daf89 _PyFunction_Vectorcall + 265
31  libpython3.9.dylib            	       0x13a3da6d4 _PyObject_FastCallDictTstate + 260
32  libpython3.9.dylib            	       0x13a3db36b _PyObject_Call_Prepend + 139
33  libpython3.9.dylib            	       0x13a4454c7 slot_tp_call + 87
34  libpython3.9.dylib            	       0x13a3dadcd _PyObject_Call + 141
35  libpython3.9.dylib            	       0x13a4dba18 _PyEval_EvalFrameDefault + 26648
36  libpython3.9.dylib            	       0x13a4df968 _PyEval_EvalCode + 2360
37  libpython3.9.dylib            	       0x13a3daf89 _PyFunction_Vectorcall + 265
38  libpython3.9.dylib            	       0x13a3ed5ec method_vectorcall + 508
39  libpython3.9.dylib            	       0x13a4dba18 _PyEval_EvalFrameDefault + 26648
40  libpython3.9.dylib            	       0x13a4df968 _PyEval_EvalCode + 2360
41  libpython3.9.dylib            	       0x13a3daf89 _PyFunction_Vectorcall + 265
42  libpython3.9.dylib            	       0x13a3da6d4 _PyObject_FastCallDictTstate + 260
43  libpython3.9.dylib            	       0x13a3db36b _PyObject_Call_Prepend + 139
44  libpython3.9.dylib            	       0x13a4454c7 slot_tp_call + 87
45  libpython3.9.dylib            	       0x13a3dadcd _PyObject_Call + 141
46  libPythonQt.dylib             	       0x111c4a05a PythonQtSignalTarget::call(_object*, PythonQtMethodInfo const*, void**, bool) + 330
47  libPythonQt.dylib             	       0x111c49e7c PythonQtSignalTarget::call(void**) const + 44
48  libPythonQt.dylib             	       0x111c4abff PythonQtSignalReceiver::qt_metacall(QMetaObject::Call, int, void**) + 95
49  QtCore                        	       0x10dbe706f 0x10d9cc000 + 2207855
50  QtCore                        	       0x10db3da04 0x10d9cc000 + 1513988
51  QtCore                        	       0x10db40a1e 0x10d9cc000 + 1526302
52  QtCore                        	       0x10dbe71bc 0x10d9cc000 + 2208188
53  QtCore                        	       0x10dbef7cb QSocketNotifier::event(QEvent*) + 491
54  QtWidgets                     	       0x10b08e526 QApplicationPrivate::notify_helper(QObject*, QEvent*) + 262
55  QtWidgets                     	       0x10b08f8ad QApplication::notify(QObject*, QEvent*) + 477
56  libqSlicerBaseQTGUI.dylib     	       0x109670414 qSlicerApplication::notify(QObject*, QEvent*) + 20
57  QtCore                        	       0x10dbb5b17 QCoreApplication::notifyInternal2(QObject*, QEvent*) + 167
58  QtCore                        	       0x10dc08d9e 0x10d9cc000 + 2346398
59  CoreFoundation                	    0x7ff817b89744 __CFSocketPerformV0 + 951
60  CoreFoundation                	    0x7ff817b6360e __CFRUNLOOP_IS_CALLING_OUT_TO_A_SOURCE0_PERFORM_FUNCTION__ + 17
61  CoreFoundation                	    0x7ff817b635b0 __CFRunLoopDoSource0 + 157
62  CoreFoundation                	    0x7ff817b6336f __CFRunLoopDoSources0 + 203
63  CoreFoundation                	    0x7ff817b61fe4 __CFRunLoopRun + 973
64  CoreFoundation                	    0x7ff817b615d0 CFRunLoopRunSpecific + 536
65  HIToolbox                     	    0x7ff823a580d4 RunCurrentEventLoopInMode + 281
66  HIToolbox                     	    0x7ff823a5af97 ReceiveNextEventCommon + 499
67  HIToolbox                     	    0x7ff823be419a _BlockUntilNextEventMatchingListInModeWithFilter + 63
68  AppKit                        	    0x7ff81b532e2d _DPSNextEvent + 912
69  AppKit                        	    0x7ff81bfc0d27 -[NSApplication(NSEventRouting) _nextEventMatchingEventMask:untilDate:inMode:dequeue:] + 1263
70  AppKit                        	    0x7ff81b523f19 -[NSApplication run] + 610
71  libqcocoa.dylib               	       0x142c7d4d3 0x142c44000 + 234707
72  QtCore                        	       0x10dbb20e6 QEventLoop::exec(QFlags&lt;QEventLoop::ProcessEventsFlag&gt;) + 502
73  QtCore                        	       0x10dbb60b2 QCoreApplication::exec() + 130
74  libqSlicerBaseQTCore.dylib    	       0x10a8929e9 qSlicerCoreApplication::exec() + 9
75  Slicer                        	       0x1009193f9 main + 505
76  dyld                          	       0x200cda530 start + 3056

Thread 1:: com.apple.rosetta.exceptionserver
0   runtime                       	    0x7ff7ffd450e4 0x7ff7ffd41000 + 16612

Thread 2:
0   ???                           	    0x7ff8a4faaae0 ???
1   libsystem_kernel.dylib        	    0x7ff817a3b5c2 __semwait_signal + 10
2   libsystem_c.dylib             	    0x7ff81792826d nanosleep + 199
3   libsystem_c.dylib             	    0x7ff8179281a0 usleep + 53
4   libSlicerBaseLogic.dylib      	       0x10d7691d3 vtkSlicerApplicationLogic::ProcessProcessingTasks() + 83
5   libSlicerBaseLogic.dylib      	       0x10d768d48 vtkSlicerApplicationLogic::ProcessingThreaderCallback(void*) + 40
6   libsystem_pthread.dylib       	    0x7ff817a7adf1 _pthread_start + 99
7   libsystem_pthread.dylib       	    0x7ff817a76857 thread_start + 15

Thread 3:
0   ???                           	    0x7ff8a4faaae0 ???
1   libsystem_kernel.dylib        	    0x7ff817a3b5c2 __semwait_signal + 10
2   libsystem_c.dylib             	    0x7ff81792826d nanosleep + 199
3   libsystem_c.dylib             	    0x7ff8179281a0 usleep + 53
4   libSlicerBaseLogic.dylib      	       0x10d7693a3 vtkSlicerApplicationLogic::ProcessNetworkingTasks() + 83
5   libSlicerBaseLogic.dylib      	       0x10d768ea8 vtkSlicerApplicationLogic::NetworkingThreaderCallback(void*) + 40
6   libsystem_pthread.dylib       	    0x7ff817a7adf1 _pthread_start + 99
7   libsystem_pthread.dylib       	    0x7ff817a76857 thread_start + 15

Thread 4:: Qt bearer thread
0   ???                           	    0x7ff8a4faaae0 ???
1   libsystem_kernel.dylib        	    0x7ff817a3f8f2 poll + 10
2   QtCore                        	       0x10dc13e1e qt_safe_poll(pollfd*, unsigned int, timespec const*) + 94
3   QtCore                        	       0x10dc1568b QEventDispatcherUNIX::processEvents(QFlags&lt;QEventLoop::ProcessEventsFlag&gt;) + 795
4   QtCore                        	       0x10dbb20e6 QEventLoop::exec(QFlags&lt;QEventLoop::ProcessEventsFlag&gt;) + 502
5   QtCore                        	       0x10d9ece2c QThread::exec() + 140
6   QtCore                        	       0x10d9edd20 0x10d9cc000 + 138528
7   libsystem_pthread.dylib       	    0x7ff817a7adf1 _pthread_start + 99
8   libsystem_pthread.dylib       	    0x7ff817a76857 thread_start + 15

Thread 5:: ctkFDHandler
0   ???                           	    0x7ff8a4faaae0 ???
1   libsystem_kernel.dylib        	    0x7ff817a395b2 read + 10
2   libCTKCore.0.1.dylib          	       0x10d62daf2 ctkFDHandler::run() + 114
3   QtCore                        	       0x10d9edd20 0x10d9cc000 + 138528
4   libsystem_pthread.dylib       	    0x7ff817a7adf1 _pthread_start + 99
5   libsystem_pthread.dylib       	    0x7ff817a76857 thread_start + 15

Thread 6:: ctkFDHandler
0   ???                           	    0x7ff8a4faaae0 ???
1   libsystem_kernel.dylib        	    0x7ff817a395b2 read + 10
2   libCTKCore.0.1.dylib          	       0x10d62daf2 ctkFDHandler::run() + 114
3   QtCore                        	       0x10d9edd20 0x10d9cc000 + 138528
4   libsystem_pthread.dylib       	    0x7ff817a7adf1 _pthread_start + 99
5   libsystem_pthread.dylib       	    0x7ff817a76857 thread_start + 15

Thread 7:: QFileInfoGatherer
0   ???                           	    0x7ff8a4faaae0 ???
1   libsystem_kernel.dylib        	    0x7ff817a3b6f6 __psynch_cvwait + 10
2   libsystem_pthread.dylib       	    0x7ff817a7b27a _pthread_cond_wait + 988
3   QtCore                        	       0x10d9f5a8b 0x10d9cc000 + 170635
4   QtCore                        	       0x10d9f5a04 QWaitCondition::wait(QMutex*, QDeadlineTimer) + 84
5   QtWidgets                     	       0x10b2c57ba 0x10b07e000 + 2389946
6   QtCore                        	       0x10d9edd20 0x10d9cc000 + 138528
7   libsystem_pthread.dylib       	    0x7ff817a7adf1 _pthread_start + 99
8   libsystem_pthread.dylib       	    0x7ff817a76857 thread_start + 15

Thread 8:: com.apple.NSEventThread
0   ???                           	    0x7ff8a4faaae0 ???
1   libsystem_kernel.dylib        	    0x7ff817a38b4a mach_msg2_trap + 10
2   libsystem_kernel.dylib        	    0x7ff817a47704 mach_msg2_internal + 83
3   libsystem_kernel.dylib        	    0x7ff817a3fbc3 mach_msg_overwrite + 574
4   libsystem_kernel.dylib        	    0x7ff817a38e3b mach_msg + 19
5   CoreFoundation                	    0x7ff817b63744 __CFRunLoopServiceMachPort + 145
6   CoreFoundation                	    0x7ff817b621ad __CFRunLoopRun + 1430
7   CoreFoundation                	    0x7ff817b615d0 CFRunLoopRunSpecific + 536
8   AppKit                        	    0x7ff81b687a2f _NSEventThread + 127
9   libsystem_pthread.dylib       	    0x7ff817a7adf1 _pthread_start + 99
10  libsystem_pthread.dylib       	    0x7ff817a76857 thread_start + 15

Thread 9:
0   ???                           	    0x7ff8a4faaae0 ???
1   libsystem_kernel.dylib        	    0x7ff817a38ac6 semaphore_wait_trap + 10
2   libtbb.12.dylib               	       0x13efb45f9 tbb::detail::r1::rml::private_worker::run() + 697
3   libtbb.12.dylib               	       0x13efb45f9 tbb::detail::r1::rml::private_worker::run() + 697
4   libtbb.12.dylib               	       0x13efb4339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
5   libtbb.12.dylib               	       0x13efb4339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
6   libtbb.12.dylib               	       0x13efb4339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
7   libtbb.12.dylib               	       0x13efb4339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
8   libtbb.12.dylib               	       0x13efb4339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
9   libtbb.12.dylib               	       0x13efb4339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
10  libtbb.12.dylib               	       0x13efb4339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
11  libtbb.12.dylib               	       0x13efb4339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
12  libtbb.12.dylib               	       0x13efb4339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
13  libtbb.12.dylib               	       0x13efb4339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
14  libtbb.12.dylib               	       0x13efb4339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
15  libtbb.12.dylib               	       0x13efb4339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
16  libtbb.12.dylib               	       0x13efb4339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
17  libtbb.12.dylib               	       0x13efb4339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
18  libtbb.12.dylib               	       0x13efb4339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
19  libtbb.12.dylib               	       0x13efb4339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
20  libtbb.12.dylib               	       0x13efb4339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
21  libtbb.12.dylib               	       0x13efb4339 tbb::detail::r1::rml::p
# ...
# this line here continues repeating for hundreds of times ...
</code></pre>
<p>I am not really sure what to make of this. I do still have some API calls running in the main process, however they take only a few seconds (&lt; 5 sec) to run to completion. Do you think running a subprocess for these calls might help or is my problem likely elsewhere?</p>
<p>Thanks for all the help so far!</p>
<p>Best,<br>
Pedro</p>

---

## Post #6 by @pedr0sorio (2025-06-17 12:02 UTC)

<p>I am thinking it might be due to something else considering Slicer at times also crashes upon loading regular DICOM data into the scene and while no functionality from my extension has been used. Could it be due to some issue while initialising my extension? Perhaps something to do with the python libraries it depends on? I am open to ideas.</p>
<p>Thanks again!</p>

---

## Post #7 by @jcfr (2025-06-18 03:11 UTC)

<aside class="quote no-group" data-username="pedr0sorio" data-post="5" data-topic="43077">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/pedr0sorio/48/80267_2.png" class="avatar"> pedr0sorio:</div>
<blockquote>
<p><code>Crashed Thread:        30  Dispatch queue: com.Metal.CompletionQueueDispatch</code></p>
</blockquote>
</aside>
<p>Can you confirm that the crash is always related to <code>com.Metal.CompletionQueueDispatch</code> ?</p>
<p>Do you have observe the issue running the latest Slicer Preview ?</p>

---
