---
topic_id: 26586
title: "Mac Stable 5 2 1 Reports A Crash Everytime It Is Closed"
date: 2022-12-05
url: https://discourse.slicer.org/t/26586
---

# Mac Stable (5.2.1.) reports a crash everytime it is closed

**Topic ID**: 26586
**Date**: 2022-12-05
**URL**: https://discourse.slicer.org/t/mac-stable-5-2-1-reports-a-crash-everytime-it-is-closed/26586

---

## Post #1 by @muratmaga (2022-12-05 22:36 UTC)

<p>Not sure what to make of this but, even if I simply close Slicer window (with no data loaded into it), I get this crash report from Mac.</p>
<p>Otherwise application appears to be working correctly.</p>
<pre><code class="lang-auto">-------------------------------------
Translated Report (Full Report Below)
-------------------------------------

Process:               Slicer [50196]
Path:                  /Applications/Slicer.app/Contents/MacOS/Slicer
Identifier:            org.slicer.slicer
Version:               5.2.1 (5.2.1)
Code Type:             X86-64 (Native)
Parent Process:        launchd [1]
User ID:               1950572333

Date/Time:             2022-12-05 14:33:53.4615 -0800
OS Version:            macOS 12.6.1 (21G217)
Report Version:        12
Bridge OS Version:     7.0 (20P411)
Anonymous UUID:        061333B8-0FD5-DBE2-ED53-7B373F48D0CE


Time Awake Since Boot: 1100000 seconds

System Integrity Protection: enabled

Crashed Thread:        0  Dispatch queue: com.apple.main-thread

Exception Type:        EXC_BAD_ACCESS (SIGSEGV)
Exception Codes:       UNKNOWN_0xD at 0x0000000000000000
Exception Codes:       0x000000000000000d, 0x0000000000000000
Exception Note:        EXC_CORPSE_NOTIFY

Termination Reason:    Namespace SIGNAL, Code 11 Segmentation fault: 11
Terminating Process:   exc handler [50196]

VM Region Info: 0 is not in any region.  Bytes before following region: 4306030592
      REGION TYPE                    START - END         [ VSIZE] PRT/MAX SHRMOD  REGION DETAIL
      UNUSED SPACE AT START
---&gt;  
      __TEXT                      100a8d000-100acf000    [  264K] r-x/rwx SM=COW  .../MacOS/Slicer

Thread 0 Crashed::  Dispatch queue: com.apple.main-thread
0   libvtkIGSIOCodecs.dylib       	       0x1522fab75 vpx_codec_destroy + 37
1   libvtkIGSIOCodecs.dylib       	       0x1522f769d vtkVP9VolumeCodec::vtkInternal::~vtkInternal() + 29
2   libvtkIGSIOCodecs.dylib       	       0x1522f778e vtkVP9VolumeCodec::vtkInternal::~vtkInternal() + 14
3   libvtkIGSIOCodecs.dylib       	       0x1522f3b05 vtkVP9VolumeCodec::~vtkVP9VolumeCodec() + 37
4   libvtkCommon-9.1.1.dylib      	       0x11c95f6ee vtkSmartPointerBase::~vtkSmartPointerBase() + 30
5   libvtkAddon.dylib             	       0x10384dff8 vtkStreamingVolumeCodecFactory::~vtkStreamingVolumeCodecFactory() + 72
6   libvtkAddon.dylib             	       0x10384db4b vtkStreamingVolumeCodecFactoryInitialize::~vtkStreamingVolumeCodecFactoryInitialize() + 27
7   libsystem_c.dylib             	    0x7ff812224de4 __cxa_finalize_ranges + 409
8   libsystem_c.dylib             	    0x7ff812224bfe exit + 35
9   libdyld.dylib                 	    0x7ff812338375 dyld4::LibSystemHelpers::exit(int) const + 11
10  dyld                          	       0x104b30558 start + 504

Thread 1:
0   libsystem_pthread.dylib       	    0x7ff812327f48 start_wqthread + 0

Thread 2:: QNetworkAccessManager thread
0   libsystem_kernel.dylib        	    0x7ff8122f60aa poll + 10
1   QtCore                        	       0x103cfe1c0 qt_safe_poll(pollfd*, unsigned int, timespec const*) + 608
2   QtCore                        	       0x103cff9c1 QEventDispatcherUNIX::processEvents(QFlags&lt;QEventLoop::ProcessEventsFlag&gt;) + 849
3   QtCore                        	       0x103c97a6f QEventLoop::exec(QFlags&lt;QEventLoop::ProcessEventsFlag&gt;) + 431
4   QtCore                        	       0x103ac4553 QThread::exec() + 131
5   QtCore                        	       0x103ac5569 0x103aa3000 + 140649
6   libsystem_pthread.dylib       	    0x7ff81232c4e1 _pthread_start + 125
7   libsystem_pthread.dylib       	    0x7ff812327f6b thread_start + 15

Thread 3:: com.apple.NSEventThread
0   libsystem_kernel.dylib        	    0x7ff8122ef97a mach_msg_trap + 10
1   libsystem_kernel.dylib        	    0x7ff8122efce8 mach_msg + 56
2   CoreFoundation                	    0x7ff8123f336d __CFRunLoopServiceMachPort + 319
3   CoreFoundation                	    0x7ff8123f19f8 __CFRunLoopRun + 1276
4   CoreFoundation                	    0x7ff8123f0e3c CFRunLoopRunSpecific + 562
5   AppKit                        	    0x7ff814f989ce _NSEventThread + 132
6   libsystem_pthread.dylib       	    0x7ff81232c4e1 _pthread_start + 125
7   libsystem_pthread.dylib       	    0x7ff812327f6b thread_start + 15

Thread 4:: AMCP Logging Spool
0   libsystem_kernel.dylib        	    0x7ff8122ef9b6 semaphore_wait_trap + 10
1   caulk                         	    0x7ff81ae2c2e6 caulk::mach::semaphore::wait_or_error() + 16
2   caulk                         	    0x7ff81ae14148 caulk::concurrent::details::worker_thread::run() + 36
3   caulk                         	    0x7ff81ae13e0c void* caulk::thread_proxy&lt;std::__1::tuple&lt;caulk::thread::attributes, void (caulk::concurrent::details::worker_thread::*)(), std::__1::tuple&lt;caulk::concurrent::details::worker_thread*&gt; &gt; &gt;(void*) + 41
4   libsystem_pthread.dylib       	    0x7ff81232c4e1 _pthread_start + 125
5   libsystem_pthread.dylib       	    0x7ff812327f6b thread_start + 15

Thread 5:: QFileInfoGatherer
0   libsystem_kernel.dylib        	    0x7ff8122f23ea __psynch_cvwait + 10
1   libsystem_pthread.dylib       	    0x7ff81232ca6f _pthread_cond_wait + 1249
2   QtCore                        	       0x103acd6ab 0x103aa3000 + 173739
3   QtCore                        	       0x103acd5ed QWaitCondition::wait(QMutex*, QDeadlineTimer) + 93
4   QtWidgets                     	       0x1024bdc88 0x10227d000 + 2362504
5   QtCore                        	       0x103ac5569 0x103aa3000 + 140649
6   libsystem_pthread.dylib       	    0x7ff81232c4e1 _pthread_start + 125
7   libsystem_pthread.dylib       	    0x7ff812327f6b thread_start + 15

Thread 6:: QFileInfoGatherer
0   libsystem_kernel.dylib        	    0x7ff8122f23ea __psynch_cvwait + 10
1   libsystem_pthread.dylib       	    0x7ff81232ca6f _pthread_cond_wait + 1249
2   QtCore                        	       0x103acd6ab 0x103aa3000 + 173739
3   QtCore                        	       0x103acd5ed QWaitCondition::wait(QMutex*, QDeadlineTimer) + 93
4   QtWidgets                     	       0x1024bdc88 0x10227d000 + 2362504
5   QtCore                        	       0x103ac5569 0x103aa3000 + 140649
6   libsystem_pthread.dylib       	    0x7ff81232c4e1 _pthread_start + 125
7   libsystem_pthread.dylib       	    0x7ff812327f6b thread_start + 15

Thread 7:
0   libsystem_pthread.dylib       	    0x7ff812327f48 start_wqthread + 0

Thread 8:
0   libsystem_pthread.dylib       	    0x7ff812327f48 start_wqthread + 0

Thread 9:
0   libsystem_pthread.dylib       	    0x7ff812327f48 start_wqthread + 0

Thread 10:
0   libsystem_pthread.dylib       	    0x7ff812327f48 start_wqthread + 0

Thread 11:
0   libsystem_pthread.dylib       	    0x7ff812327f48 start_wqthread + 0


Thread 0 crashed with X86 Thread State (64-bit):
  rax: 0x0000000000000001  rbx: 0x00007fad0691a1a0  rcx: 0x0070006d00690020  rdx: 0x0000000000000000
  rdi: 0x0046007300650073  rsi: 0x0000000000000000  rbp: 0x00007ff7bf4728d0  rsp: 0x00007ff7bf4728c0
   r8: 0x00007facf9829000   r9: 0x0000000000000016  r10: 0x00007ff853a7fee0  r11: 0x00000000000001ff
  r12: 0xfffffffffffffff0  r13: 0x00000000000002c0  r14: 0x00006000033b8690  r15: 0x0000600001207270
  rip: 0x00000001522fab75  rfl: 0x0000000000010202  cr2: 0x000000010afbbbe0
  
Logical CPU:     0
Error Code:      0x00000000 
Trap Number:     13

Thread 0 instruction stream:
  66 66 2e 0f 1f 84 00 00-00 00 00 55 48 89 e5 48  ff.........UH..H
  85 ff 74 1a 83 7f 10 00-74 18 48 8b 47 30 48 83  ..t.....t.H.G0H.
  c7 18 48 85 c0 48 0f 45-f8 48 8b 07 5d c3 31 c0  ..H..H.E.H..].1.
  5d c3 31 c0 5d c3 0f 1f-44 00 00 55 48 89 e5 53  ].1.]...D..UH..S
  50 48 89 fb 48 85 db 74-3d 48 8b 4b 08 b8 01 00  PH..H..t=H.K....
  00 00 48 85 c9 74 25 48-8b 7b 30 48 85 ff 74 1c  ..H..t%H.{0H..t.
 [ff]51 20 48 c7 43 30 00-00 00 00 48 c7 43 08 00  .Q H.C0....H.C..	&lt;==
  00 00 00 48 c7 03 00 00-00 00 31 c0 89 43 10 48  ...H......1..C.H
  83 c4 08 5b 5d c3 b8 08-00 00 00 48 83 c4 08 5b  ...[]......H...[
  5d c3 66 0f 1f 84 00 00-00 00 00 55 48 89 e5 48  ].f........UH..H
  85 ff 74 06 48 8b 47 10-5d c3 31 c0 5d c3 66 66  ..t.H.G.].1.].ff
  66 66 2e 0f 1f 84 00 00-00 00 00 55 48 89 e5 53  ff.........UH..S

Binary Images:
       0x1522da000 -        0x152453fff libvtkIGSIOCodecs.dylib (*) &lt;f10d6339-7e21-351c-98b7-8346870c1d5a&gt; /Applications/Slicer.app/Contents/Extensions-31317/SlicerIGSIO/lib/Slicer-5.2/libvtkIGSIOCodecs.dylib
       0x11bff5000 -        0x11cb7efff libvtkCommon-9.1.1.dylib (*) &lt;f57d8297-7b4b-3854-88a7-38769ea8ef31&gt; /Applications/Slicer.app/Contents/lib/Slicer-5.2/libvtkCommon-9.1.1.dylib
       0x1037e6000 -        0x103859fff libvtkAddon.dylib (*) &lt;c6ecbb9b-430f-3ec6-93a6-7661578ce1e9&gt; /Applications/Slicer.app/Contents/lib/Slicer-5.2/libvtkAddon.dylib
    0x7ff8121f6000 -     0x7ff81227efff libsystem_c.dylib (*) &lt;e42e9d7a-03b4-340b-b61e-dcd45fd4acc0&gt; /usr/lib/system/libsystem_c.dylib
    0x7ff812332000 -     0x7ff81233dfff libdyld.dylib (*) &lt;64c284b3-231b-391d-845c-a285dfa305cd&gt; /usr/lib/system/libdyld.dylib
       0x104b2b000 -        0x104b96fff dyld (*) &lt;7b87a986-a153-33c4-8470-d56410b7f9d5&gt; /usr/lib/dyld
    0x7ff812326000 -     0x7ff812331fff libsystem_pthread.dylib (*) &lt;b5454e27-e8c7-3fdb-b77f-714f1e82e70b&gt; /usr/lib/system/libsystem_pthread.dylib
    0x7ff8122ee000 -     0x7ff812325fff libsystem_kernel.dylib (*) &lt;0ea0d8ac-c27b-3a71-a59b-ec3a6f116acf&gt; /usr/lib/system/libsystem_kernel.dylib
       0x103aa3000 -        0x104013fff org.qt-project.QtCore (5.15) &lt;eda847f8-ebac-3db5-80d9-95a0b5e3a870&gt; /Applications/Slicer.app/Contents/Frameworks/QtCore.framework/Versions/5/QtCore
    0x7ff812373000 -     0x7ff812875fff com.apple.CoreFoundation (6.9) &lt;93c48919-68af-367e-9a67-db4159bc962c&gt; /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
    0x7ff814dec000 -     0x7ff815c7bfff com.apple.AppKit (6.9) &lt;d2726161-3c3f-3b59-bd8d-4a088d4545ef&gt; /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
    0x7ff81ae12000 -     0x7ff81ae33fff com.apple.audio.caulk (1.0) &lt;8e7b3d95-1d47-3f17-9512-c5fcc30792c2&gt; /System/Library/PrivateFrameworks/caulk.framework/Versions/A/caulk
       0x10227d000 -        0x1026c3fff org.qt-project.QtWidgets (5.15) &lt;6a0c4de6-8a12-31d0-90cb-63e5c78b6c35&gt; /Applications/Slicer.app/Contents/Frameworks/QtWidgets.framework/Versions/5/QtWidgets

External Modification Summary:
  Calls made by other processes targeting this process:
    task_for_pid: 0
    thread_create: 0
    thread_set_state: 0
  Calls made by this process:
    task_for_pid: 0
    thread_create: 0
    thread_set_state: 0
  Calls made by all processes on this machine:
    task_for_pid: 0
    thread_create: 0
    thread_set_state: 0

VM Region Summary:
ReadOnly portion of Libraries: Total=2.1G resident=0K(0%) swapped_out_or_unallocated=2.1G(100%)
Writable regions: Total=2.8G written=0K(0%) resident=0K(0%) swapped_out=0K(0%) unallocated=2.8G(100%)

                                  VIRTUAL   REGION 
REGION TYPE                          SIZE    COUNT (non-coalesced) 
===========                       =======  ======= 
Accelerate framework                 384K        3 
Activity Tracing                     256K        1 
CG backing stores                   3840K        4 
CG image                             160K       13 
ColorSync                            224K       26 
CoreAnimation                        136K        9 
CoreGraphics                          12K        2 
CoreUI image data                   1592K       13 
Foundation                            16K        1 
JS JIT generated code              128.0M        1 
JS JIT generated code (reserved)     1.9G        1         reserved VM address space (unallocated)
Kernel Alloc Once                      8K        1 
MALLOC                             325.8M      116 
MALLOC guard page                     32K        8 
MALLOC_LARGE (reserved)              128K        1         reserved VM address space (unallocated)
MALLOC_NANO (reserved)             384.0M        1         reserved VM address space (unallocated)
ObjC additional data                  15K        1 
OpenGL GLSL                          256K        3 
STACK GUARD                         56.0M       12 
Stack                               13.6M       12 
VM_ALLOCATE                         57.6M      255 
VM_ALLOCATE (reserved)                44K        2         reserved VM address space (unallocated)
WebKit Malloc                       1184K        6 
__CTF                                 756        1 
__DATA                              92.5M     1460 
__DATA_CONST                        32.3M      337 
__DATA_DIRTY                        1641K      212 
__FONT_DATA                            4K        1 
__GLSLBUILTINS                      5176K        1 
__LINKEDIT                         812.6M      844 
__TEXT                               1.3G     1365 
__UNICODE                            592K        1 
dyld private memory                 6144K        3 
mapped file                        384.8M       74 
shared memory                        776K       18 
===========                       =======  ======= 
TOTAL                                5.4G     4809 
TOTAL, minus reserved VM space       3.2G     4809 



-----------
Full Report
-----------

{"app_name":"Slicer","timestamp":"2022-12-05 14:33:54.00 -0800","app_version":"5.2.1","slice_uuid":"0d378013-ad07-308c-a7b7-b5418f961ffa","build_version":"5.2.1","platform":1,"bundleID":"org.slicer.slicer","share_with_app_devs":1,"is_first_party":0,"bug_type":"309","os_version":"macOS 12.6.1 (21G217)","incident_id":"307EBFB2-9528-4131-B36E-D20CB4F0C9C2","name":"Slicer"}
{
  "uptime" : 1100000,
  "procLaunch" : "2022-12-05 14:25:30.7761 -0800",
  "procRole" : "Foreground",
  "version" : 2,
  "userID" : 1950572333,
  "deployVersion" : 210,
  "modelCode" : "MacBookPro15,1",
  "procStartAbsTime" : 1134075343416785,
  "coalitionID" : 64051,
  "osVersion" : {
    "train" : "macOS 12.6.1",
    "build" : "21G217",
    "releaseType" : "User"
  },
  "captureTime" : "2022-12-05 14:33:53.4615 -0800",
  "incident" : "307EBFB2-9528-4131-B36E-D20CB4F0C9C2",
  "bug_type" : "309",
  "pid" : 50196,
  "procExitAbsTime" : 1134578012199028,
  "cpuType" : "X86-64",
  "procName" : "Slicer",
  "procPath" : "\/Applications\/Slicer.app\/Contents\/MacOS\/Slicer",
  "bundleInfo" : {"CFBundleShortVersionString":"5.2.1","CFBundleVersion":"5.2.1","CFBundleIdentifier":"org.slicer.slicer"},
  "storeInfo" : {"deviceIdentifierForVendor":"5711C463-2F32-5E5D-8265-6A5BDD3872BC","thirdParty":true},
  "parentProc" : "launchd",
  "parentPid" : 1,
  "coalitionName" : "org.slicer.slicer",
  "crashReporterKey" : "061333B8-0FD5-DBE2-ED53-7B373F48D0CE",
  "bridgeVersion" : {"build":"20P411","train":"7.0"},
  "sip" : "enabled",
  "vmRegionInfo" : "0 is not in any region.  Bytes before following region: 4306030592\n      REGION TYPE                    START - END         [ VSIZE] PRT\/MAX SHRMOD  REGION DETAIL\n      UNUSED SPACE AT START\n---&gt;  \n      __TEXT                      100a8d000-100acf000    [  264K] r-x\/rwx SM=COW  ...\/MacOS\/Slicer",
  "isCorpse" : 1,
  "exception" : {"codes":"0x000000000000000d, 0x0000000000000000","rawCodes":[13,0],"type":"EXC_BAD_ACCESS","signal":"SIGSEGV","subtype":"UNKNOWN_0xD at 0x0000000000000000"},
  "termination" : {"flags":0,"code":11,"namespace":"SIGNAL","indicator":"Segmentation fault: 11","byProc":"exc handler","byPid":50196},
  "vmregioninfo" : "0 is not in any region.  Bytes before following region: 4306030592\n      REGION TYPE                    START - END         [ VSIZE] PRT\/MAX SHRMOD  REGION DETAIL\n      UNUSED SPACE AT START\n---&gt;  \n      __TEXT                      100a8d000-100acf000    [  264K] r-x\/rwx SM=COW  ...\/MacOS\/Slicer",
  "extMods" : {"caller":{"thread_create":0,"thread_set_state":0,"task_for_pid":0},"system":{"thread_create":0,"thread_set_state":0,"task_for_pid":0},"targeted":{"thread_create":0,"thread_set_state":0,"task_for_pid":0},"warnings":0},
  "faultingThread" : 0,
  "threads" : [{"triggered":true,"id":8263000,"instructionState":{"instructionStream":{"bytes":[102,102,46,15,31,132,0,0,0,0,0,85,72,137,229,72,133,255,116,26,131,127,16,0,116,24,72,139,71,48,72,131,199,24,72,133,192,72,15,69,248,72,139,7,93,195,49,192,93,195,49,192,93,195,15,31,68,0,0,85,72,137,229,83,80,72,137,251,72,133,219,116,61,72,139,75,8,184,1,0,0,0,72,133,201,116,37,72,139,123,48,72,133,255,116,28,255,81,32,72,199,67,48,0,0,0,0,72,199,67,8,0,0,0,0,72,199,3,0,0,0,0,49,192,137,67,16,72,131,196,8,91,93,195,184,8,0,0,0,72,131,196,8,91,93,195,102,15,31,132,0,0,0,0,0,85,72,137,229,72,133,255,116,6,72,139,71,16,93,195,49,192,93,195,102,102,102,102,46,15,31,132,0,0,0,0,0,85,72,137,229,83],"offset":96}},"threadState":{"r13":{"value":704},"rax":{"value":1},"rflags":{"value":66050},"cpu":{"value":0},"r14":{"value":105553170499216},"rsi":{"value":0},"r8":{"value":140380897185792},"cr2":{"value":4479237088},"rdx":{"value":0},"r10":{"value":140704532135648,"symbolLocation":24,"symbol":"atexit_mutex"},"r9":{"value":22},"r15":{"value":105553135170160},"rbx":{"value":140381116277152},"trap":{"value":13},"err":{"value":0},"r11":{"value":511},"rip":{"value":5673823093,"matchesCrashFrame":1},"rbp":{"value":140702042761424},"rsp":{"value":140702042761408},"r12":{"value":18446744073709551600},"rcx":{"value":31525665549910048},"flavor":"x86_THREAD_STATE","rdi":{"value":19703742297604211}},"queue":"com.apple.main-thread","frames":[{"imageOffset":134005,"symbol":"vpx_codec_destroy","symbolLocation":37,"imageIndex":0},{"imageOffset":120477,"symbol":"vtkVP9VolumeCodec::vtkInternal::~vtkInternal()","symbolLocation":29,"imageIndex":0},{"imageOffset":120718,"symbol":"vtkVP9VolumeCodec::vtkInternal::~vtkInternal()","symbolLocation":14,"imageIndex":0},{"imageOffset":105221,"symbol":"vtkVP9VolumeCodec::~vtkVP9VolumeCodec()","symbolLocation":37,"imageIndex":0},{"imageOffset":9873134,"symbol":"vtkSmartPointerBase::~vtkSmartPointerBase()","symbolLocation":30,"imageIndex":1},{"imageOffset":425976,"symbol":"vtkStreamingVolumeCodecFactory::~vtkStreamingVolumeCodecFactory()","symbolLocation":72,"imageIndex":2},{"imageOffset":424779,"symbol":"vtkStreamingVolumeCodecFactoryInitialize::~vtkStreamingVolumeCodecFactoryInitialize()","symbolLocation":27,"imageIndex":2},{"imageOffset":191972,"symbol":"__cxa_finalize_ranges","symbolLocation":409,"imageIndex":3},{"imageOffset":191486,"symbol":"exit","symbolLocation":35,"imageIndex":3},{"imageOffset":25461,"symbol":"dyld4::LibSystemHelpers::exit(int) const","symbolLocation":11,"imageIndex":4},{"imageOffset":21848,"symbol":"start","symbolLocation":504,"imageIndex":5}]},{"id":8263041,"frames":[{"imageOffset":8008,"symbol":"start_wqthread","symbolLocation":0,"imageIndex":6}]},{"id":8263134,"name":"QNetworkAccessManager thread","frames":[{"imageOffset":32938,"symbol":"poll","symbolLocation":10,"imageIndex":7},{"imageOffset":2470336,"symbol":"qt_safe_poll(pollfd*, unsigned int, timespec const*)","symbolLocation":608,"imageIndex":8},{"imageOffset":2476481,"symbol":"QEventDispatcherUNIX::processEvents(QFlags&lt;QEventLoop::ProcessEventsFlag&gt;)","symbolLocation":849,"imageIndex":8},{"imageOffset":2050671,"symbol":"QEventLoop::exec(QFlags&lt;QEventLoop::ProcessEventsFlag&gt;)","symbolLocation":431,"imageIndex":8},{"imageOffset":136531,"symbol":"QThread::exec()","symbolLocation":131,"imageIndex":8},{"imageOffset":140649,"imageIndex":8},{"imageOffset":25825,"symbol":"_pthread_start","symbolLocation":125,"imageIndex":6},{"imageOffset":8043,"symbol":"thread_start","symbolLocation":15,"imageIndex":6}]},{"id":8263168,"name":"com.apple.NSEventThread","frames":[{"imageOffset":6522,"symbol":"mach_msg_trap","symbolLocation":10,"imageIndex":7},{"imageOffset":7400,"symbol":"mach_msg","symbolLocation":56,"imageIndex":7},{"imageOffset":525165,"symbol":"__CFRunLoopServiceMachPort","symbolLocation":319,"imageIndex":9},{"imageOffset":518648,"symbol":"__CFRunLoopRun","symbolLocation":1276,"imageIndex":9},{"imageOffset":515644,"symbol":"CFRunLoopRunSpecific","symbolLocation":562,"imageIndex":9},{"imageOffset":1755598,"symbol":"_NSEventThread","symbolLocation":132,"imageIndex":10},{"imageOffset":25825,"symbol":"_pthread_start","symbolLocation":125,"imageIndex":6},{"imageOffset":8043,"symbol":"thread_start","symbolLocation":15,"imageIndex":6}]},{"id":8263331,"name":"AMCP Logging Spool","frames":[{"imageOffset":6582,"symbol":"semaphore_wait_trap","symbolLocation":10,"imageIndex":7},{"imageOffset":107238,"symbol":"caulk::mach::semaphore::wait_or_error()","symbolLocation":16,"imageIndex":11},{"imageOffset":8520,"symbol":"caulk::concurrent::details::worker_thread::run()","symbolLocation":36,"imageIndex":11},{"imageOffset":7692,"symbol":"void* caulk::thread_proxy&lt;std::__1::tuple&lt;caulk::thread::attributes, void (caulk::concurrent::details::worker_thread::*)(), std::__1::tuple&lt;caulk::concurrent::details::worker_thread*&gt; &gt; &gt;(void*)","symbolLocation":41,"imageIndex":11},{"imageOffset":25825,"symbol":"_pthread_start","symbolLocation":125,"imageIndex":6},{"imageOffset":8043,"symbol":"thread_start","symbolLocation":15,"imageIndex":6}]},{"id":8263367,"name":"QFileInfoGatherer","frames":[{"imageOffset":17386,"symbol":"__psynch_cvwait","symbolLocation":10,"imageIndex":7},{"imageOffset":27247,"symbol":"_pthread_cond_wait","symbolLocation":1249,"imageIndex":6},{"imageOffset":173739,"imageIndex":8},{"imageOffset":173549,"symbol":"QWaitCondition::wait(QMutex*, QDeadlineTimer)","symbolLocation":93,"imageIndex":8},{"imageOffset":2362504,"imageIndex":12},{"imageOffset":140649,"imageIndex":8},{"imageOffset":25825,"symbol":"_pthread_start","symbolLocation":125,"imageIndex":6},{"imageOffset":8043,"symbol":"thread_start","symbolLocation":15,"imageIndex":6}]},{"id":8263368,"name":"QFileInfoGatherer","frames":[{"imageOffset":17386,"symbol":"__psynch_cvwait","symbolLocation":10,"imageIndex":7},{"imageOffset":27247,"symbol":"_pthread_cond_wait","symbolLocation":1249,"imageIndex":6},{"imageOffset":173739,"imageIndex":8},{"imageOffset":173549,"symbol":"QWaitCondition::wait(QMutex*, QDeadlineTimer)","symbolLocation":93,"imageIndex":8},{"imageOffset":2362504,"imageIndex":12},{"imageOffset":140649,"imageIndex":8},{"imageOffset":25825,"symbol":"_pthread_start","symbolLocation":125,"imageIndex":6},{"imageOffset":8043,"symbol":"thread_start","symbolLocation":15,"imageIndex":6}]},{"id":8265910,"frames":[{"imageOffset":8008,"symbol":"start_wqthread","symbolLocation":0,"imageIndex":6}]},{"id":8266383,"frames":[{"imageOffset":8008,"symbol":"start_wqthread","symbolLocation":0,"imageIndex":6}]},{"id":8266396,"frames":[{"imageOffset":8008,"symbol":"start_wqthread","symbolLocation":0,"imageIndex":6}]},{"id":8266405,"frames":[{"imageOffset":8008,"symbol":"start_wqthread","symbolLocation":0,"imageIndex":6}]},{"id":8266406,"frames":[{"imageOffset":8008,"symbol":"start_wqthread","symbolLocation":0,"imageIndex":6}]}],
  "usedImages" : [
  {
    "source" : "P",
    "arch" : "x86_64",
    "base" : 5673689088,
    "size" : 1548288,
    "uuid" : "f10d6339-7e21-351c-98b7-8346870c1d5a",
    "path" : "\/Applications\/Slicer.app\/Contents\/Extensions-31317\/SlicerIGSIO\/lib\/Slicer-5.2\/libvtkIGSIOCodecs.dylib",
    "name" : "libvtkIGSIOCodecs.dylib"
  },
  {
    "source" : "P",
    "arch" : "x86_64",
    "base" : 4764684288,
    "size" : 12099584,
    "uuid" : "f57d8297-7b4b-3854-88a7-38769ea8ef31",
    "path" : "\/Applications\/Slicer.app\/Contents\/lib\/Slicer-5.2\/libvtkCommon-9.1.1.dylib",
    "name" : "libvtkCommon-9.1.1.dylib"
  },
  {
    "source" : "P",
    "arch" : "x86_64",
    "base" : 4353581056,
    "size" : 475136,
    "uuid" : "c6ecbb9b-430f-3ec6-93a6-7661578ce1e9",
    "path" : "\/Applications\/Slicer.app\/Contents\/lib\/Slicer-5.2\/libvtkAddon.dylib",
    "name" : "libvtkAddon.dylib"
  },
  {
    "source" : "P",
    "arch" : "x86_64",
    "base" : 140703432663040,
    "size" : 561152,
    "uuid" : "e42e9d7a-03b4-340b-b61e-dcd45fd4acc0",
    "path" : "\/usr\/lib\/system\/libsystem_c.dylib",
    "name" : "libsystem_c.dylib"
  },
  {
    "source" : "P",
    "arch" : "x86_64",
    "base" : 140703433957376,
    "size" : 49152,
    "uuid" : "64c284b3-231b-391d-845c-a285dfa305cd",
    "path" : "\/usr\/lib\/system\/libdyld.dylib",
    "name" : "libdyld.dylib"
  },
  {
    "source" : "P",
    "arch" : "x86_64",
    "base" : 4373786624,
    "size" : 442368,
    "uuid" : "7b87a986-a153-33c4-8470-d56410b7f9d5",
    "path" : "\/usr\/lib\/dyld",
    "name" : "dyld"
  },
  {
    "source" : "P",
    "arch" : "x86_64",
    "base" : 140703433908224,
    "size" : 49152,
    "uuid" : "b5454e27-e8c7-3fdb-b77f-714f1e82e70b",
    "path" : "\/usr\/lib\/system\/libsystem_pthread.dylib",
    "name" : "libsystem_pthread.dylib"
  },
  {
    "source" : "P",
    "arch" : "x86_64",
    "base" : 140703433678848,
    "size" : 229376,
    "uuid" : "0ea0d8ac-c27b-3a71-a59b-ec3a6f116acf",
    "path" : "\/usr\/lib\/system\/libsystem_kernel.dylib",
    "name" : "libsystem_kernel.dylib"
  },
  {
    "source" : "P",
    "arch" : "x86_64",
    "base" : 4356452352,
    "CFBundleShortVersionString" : "5.15",
    "CFBundleIdentifier" : "org.qt-project.QtCore",
    "size" : 5705728,
    "uuid" : "eda847f8-ebac-3db5-80d9-95a0b5e3a870",
    "path" : "\/Applications\/Slicer.app\/Contents\/Frameworks\/QtCore.framework\/Versions\/5\/QtCore",
    "name" : "QtCore",
    "CFBundleVersion" : "5.15.2"
  },
  {
    "source" : "P",
    "arch" : "x86_64h",
    "base" : 140703434223616,
    "CFBundleShortVersionString" : "6.9",
    "CFBundleIdentifier" : "com.apple.CoreFoundation",
    "size" : 5255168,
    "uuid" : "93c48919-68af-367e-9a67-db4159bc962c",
    "path" : "\/System\/Library\/Frameworks\/CoreFoundation.framework\/Versions\/A\/CoreFoundation",
    "name" : "CoreFoundation",
    "CFBundleVersion" : "1866"
  },
  {
    "source" : "P",
    "arch" : "x86_64",
    "base" : 140703478759424,
    "CFBundleShortVersionString" : "6.9",
    "CFBundleIdentifier" : "com.apple.AppKit",
    "size" : 15269888,
    "uuid" : "d2726161-3c3f-3b59-bd8d-4a088d4545ef",
    "path" : "\/System\/Library\/Frameworks\/AppKit.framework\/Versions\/C\/AppKit",
    "name" : "AppKit",
    "CFBundleVersion" : "2113.60.148"
  },
  {
    "source" : "P",
    "arch" : "x86_64",
    "base" : 140703579578368,
    "CFBundleShortVersionString" : "1.0",
    "CFBundleIdentifier" : "com.apple.audio.caulk",
    "size" : 139264,
    "uuid" : "8e7b3d95-1d47-3f17-9512-c5fcc30792c2",
    "path" : "\/System\/Library\/PrivateFrameworks\/caulk.framework\/Versions\/A\/caulk",
    "name" : "caulk"
  },
  {
    "source" : "P",
    "arch" : "x86_64",
    "base" : 4331130880,
    "CFBundleShortVersionString" : "5.15",
    "CFBundleIdentifier" : "org.qt-project.QtWidgets",
    "size" : 4485120,
    "uuid" : "6a0c4de6-8a12-31d0-90cb-63e5c78b6c35",
    "path" : "\/Applications\/Slicer.app\/Contents\/Frameworks\/QtWidgets.framework\/Versions\/5\/QtWidgets",
    "name" : "QtWidgets",
    "CFBundleVersion" : "5.15.2"
  }
],
  "sharedCache" : {
  "base" : 140703430651904,
  "size" : 19331678208,
  "uuid" : "57de9b7b-39b3-3557-8aed-37ac450fa1f3"
},
  "vmSummary" : "ReadOnly portion of Libraries: Total=2.1G resident=0K(0%) swapped_out_or_unallocated=2.1G(100%)\nWritable regions: Total=2.8G written=0K(0%) resident=0K(0%) swapped_out=0K(0%) unallocated=2.8G(100%)\n\n                                  VIRTUAL   REGION \nREGION TYPE                          SIZE    COUNT (non-coalesced) \n===========                       =======  ======= \nAccelerate framework                 384K        3 \nActivity Tracing                     256K        1 \nCG backing stores                   3840K        4 \nCG image                             160K       13 \nColorSync                            224K       26 \nCoreAnimation                        136K        9 \nCoreGraphics                          12K        2 \nCoreUI image data                   1592K       13 \nFoundation                            16K        1 \nJS JIT generated code              128.0M        1 \nJS JIT generated code (reserved)     1.9G        1         reserved VM address space (unallocated)\nKernel Alloc Once                      8K        1 \nMALLOC                             325.8M      116 \nMALLOC guard page                     32K        8 \nMALLOC_LARGE (reserved)              128K        1         reserved VM address space (unallocated)\nMALLOC_NANO (reserved)             384.0M        1         reserved VM address space (unallocated)\nObjC additional data                  15K        1 \nOpenGL GLSL                          256K        3 \nSTACK GUARD                         56.0M       12 \nStack                               13.6M       12 \nVM_ALLOCATE                         57.6M      255 \nVM_ALLOCATE (reserved)                44K        2         reserved VM address space (unallocated)\nWebKit Malloc                       1184K        6 \n__CTF                                 756        1 \n__DATA                              92.5M     1460 \n__DATA_CONST                        32.3M      337 \n__DATA_DIRTY                        1641K      212 \n__FONT_DATA                            4K        1 \n__GLSLBUILTINS                      5176K        1 \n__LINKEDIT                         812.6M      844 \n__TEXT                               1.3G     1365 \n__UNICODE                            592K        1 \ndyld private memory                 6144K        3 \nmapped file                        384.8M       74 \nshared memory                        776K       18 \n===========                       =======  ======= \nTOTAL                                5.4G     4809 \nTOTAL, minus reserved VM space       3.2G     4809 \n",
  "legacyInfo" : {
  "threadTriggered" : {
    "queue" : "com.apple.main-thread"
  }
},
  "trialInfo" : {
  "rollouts" : [
    {
      "rolloutId" : "61301e3a61217b3110231469",
      "factorPackIds" : {
        "SIRI_FIND_MY_CONFIGURATION_FILES" : "6348493aa52bb16adc4e4d06"
      },
      "deploymentId" : 240000023
    },
    {
      "rolloutId" : "60356660bbe37970735c5624",
      "factorPackIds" : {

      },
      "deploymentId" : 240000027
    }
  ],
  "experiments" : [

  ]
}
}

Model: MacBookPro15,1, BootROM 1916.40.8.0.0 (iBridge: 20.16.411.0.0,0), 8 processors, 8-Core Intel Core i9, 2.3 GHz, 16 GB, SMC 
Graphics: Intel UHD Graphics 630, Intel UHD Graphics 630, Built-In
Graphics: Radeon Pro 560X, Radeon Pro 560X, PCIe, 4 GB
Display: DELL U2718Q, 5120 x 2880 (5K/UHD+ - Ultra High Definition Plus), Main, MirrorOff, Online
Memory Module: BANK 0/ChannelA-DIMM0, 8 GB, DDR4, 2400 MHz, SK Hynix, HMA81GS6AFR8N-UH
Memory Module: BANK 2/ChannelB-DIMM0, 8 GB, DDR4, 2400 MHz, SK Hynix, HMA81GS6AFR8N-UH
AirPort: spairport_wireless_card_type_wifi (0x14E4, 0x7BF), wl0: Jul 12 2021 19:26:30 version 9.30.464.0.32.5.76 FWID 01-45ccefcd
Bluetooth: Version (null), 0 services, 0 devices, 0 incoming serial ports
Network Service: AX88179A, Ethernet, en6
Network Service: Wi-Fi, AirPort, en0
USB Device: USB3.0 Hub
USB Device: AX88179A
USB Device: USB31Bus
USB Device: USB2.0 Hub
USB Device: Cable Matters USB-C Video Cable
USB Device: T2Bus
USB Device: Touch Bar Backlight
USB Device: Touch Bar Display
USB Device: Apple Internal Keyboard / Trackpad
USB Device: Headset
USB Device: Ambient Light Sensor
USB Device: FaceTime HD Camera (Built-in)
USB Device: Apple T2 Controller
Thunderbolt Bus: MacBook Pro, Apple Inc., 47.5
Thunderbolt Bus: MacBook Pro, Apple Inc., 47.5
</code></pre>

---

## Post #2 by @pieper (2022-12-05 23:58 UTC)

<p>Looks like the same crash as this one: <a href="https://discourse.slicer.org/t/slicer-quit-unexpectedly-on-macbook-with-m1-chip/25989/3" class="inline-onebox">Slicer quit unexpectedly on MacBook with M1 chip - #3 by Young_Wang</a> (in <code>vpx_codec_destroy</code>).</p>
<p>Do you have the <a href="https://github.com/IGSIO/SlicerIGSIO">IGSIO extension</a> installed?  It provides <code>libvtkIGSIOCodecs</code></p>

---

## Post #3 by @muratmaga (2022-12-06 00:36 UTC)

<p>I have installed the SlicerIGT, which I think automatically installs IGSIO.</p>

---

## Post #4 by @pieper (2022-12-06 00:37 UTC)

<p>yes, that’s probably it.</p>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a>, any suggestions?</p>

---

## Post #5 by @Sunderlandkyl (2022-12-06 00:49 UTC)

<p>Disposing of the VP9 codec seems to be causing the crash, I’ll look into it.</p>
<p>Is this an issue that just started on Mac, or has IGSIO been causing a crash on close for a while?</p>

---

## Post #6 by @jamesobutler (2022-12-06 00:53 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="26586">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>vpx_codec_destroy</p>
</blockquote>
</aside>
<aside class="onebox githubblob" data-onebox-src="https://github.com/IGSIO/SlicerIGSIO/blob/b57a4200125e91a3e484f9471ec472ba7febad54/SuperBuild/External_VP9.cmake#L57-L64">
  <header class="source">

      <a href="https://github.com/IGSIO/SlicerIGSIO/blob/b57a4200125e91a3e484f9471ec472ba7febad54/SuperBuild/External_VP9.cmake#L57-L64" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/IGSIO/SlicerIGSIO/blob/b57a4200125e91a3e484f9471ec472ba7febad54/SuperBuild/External_VP9.cmake#L57-L64" target="_blank" rel="noopener nofollow ugc">IGSIO/SlicerIGSIO/blob/b57a4200125e91a3e484f9471ec472ba7febad54/SuperBuild/External_VP9.cmake#L57-L64</a></h4>



    <pre class="onebox"><code class="lang-cmake">
      <ol class="start lines" start="57" style="counter-reset: li-counter 56 ;">
          <li>  "${EP_GIT_PROTOCOL}://github.com/webmproject/libvpx.git"</li>
          <li>  QUIET</li>
          <li>  )</li>
          <li></li>
          <li>ExternalProject_SetIfNotDefined(</li>
          <li>  ${CMAKE_PROJECT_NAME}_${proj}_GIT_TAG</li>
          <li>  "v1.8.2"</li>
          <li>  QUIET</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I would assume an old VP9 is contributing. SlicerIGSIO is using 1.8.2, but version 1.10 is when Darwin 20, aka macOS 11, support was added. macOS 11 corresponded when the first Apple Silicon (M1) chips were released. Therefore I would assume this has been an issue with latest SlicerIGSIO for awhile on macOS and not necessarily due to the Slicer 5.2.1 release directly.</p>
<blockquote>
<p>2021-03-09 v1.10.0 “Ruddy Duck”<br>
This maintenance release adds support for darwin20 and new codec controls, as<br>
well as numerous bug fixes.</p>
</blockquote>
<p><a href="https://chromium.googlesource.com/webm/libvpx/+/master/CHANGELOG" class="onebox" target="_blank" rel="noopener nofollow ugc">https://chromium.googlesource.com/webm/libvpx/+/master/CHANGELOG</a></p>

---

## Post #7 by @lassoan (2022-12-06 01:30 UTC)

<p>Is this an M1 mac?<br>
Do you have Rosetta 2?</p>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> it would be great if you could update VP9 to the latest version - hopefully the error goes away.</p>

---

## Post #8 by @jamesobutler (2022-12-06 01:45 UTC)

<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> There appears to be an external VP9 project for SlicerIGSIO and also IGSIO. Probably want to update in both repositories.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/IGSIO/IGSIO/blob/master/SuperBuild/External_VP9.cmake">
  <header class="source">

      <a href="https://github.com/IGSIO/IGSIO/blob/master/SuperBuild/External_VP9.cmake" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/IGSIO/IGSIO/blob/master/SuperBuild/External_VP9.cmake" target="_blank" rel="noopener nofollow ugc">IGSIO/IGSIO/blob/master/SuperBuild/External_VP9.cmake</a></h4>


      <pre><code class="lang-cmake">set(proj "VP9")

SET(${proj}_DEPENDENCIES)

IF(VP9_DIR)
  FIND_PACKAGE(VP9 REQUIRED)
  SET(IGSIO_VP9_DIR ${VP9_DIR})
ELSE()

  SET(IGSIO_VP9_DIR "${CMAKE_BINARY_DIR}/VP9")

  # VP9 has not been built yet, so download and build it as an external project
  if(NOT CMAKE_SYSTEM_NAME STREQUAL "Windows")
    INCLUDE(${IGSIO_SOURCE_DIR}/SuperBuild/External_YASM.cmake)
    IF(NOT YASM_FOUND)
      LIST(APPEND ${proj}_DEPENDENCIES YASM)
    ENDIF()

    SET (VP9_INCLUDE_DIR "${CMAKE_BINARY_DIR}/VP9/vpx" CACHE PATH "VP9 source directory" FORCE)
    SET (VP9_LIBRARY_DIR "${CMAKE_BINARY_DIR}/VP9" CACHE PATH "VP9 library directory" FORCE)
</code></pre>



  This file has been truncated. <a href="https://github.com/IGSIO/IGSIO/blob/master/SuperBuild/External_VP9.cmake" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #9 by @muratmaga (2022-12-06 04:51 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="26586">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Is this an M1 mac?</p>
</blockquote>
</aside>
<p>If this is for me, this is an Intel Macbook pro from 2019</p>

---

## Post #10 by @Young_Wang (2022-12-07 13:19 UTC)

<aside class="quote" data-post="12" data-topic="25989">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/young_wang/48/13926_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/slicer-quit-unexpectedly-on-macbook-with-m1-chip/25989/12">Slicer quit unexpectedly on MacBook with M1 chip</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    <a class="mention" href="/u/pieper">@pieper</a> thanks. It seems to fix this issue.
  </blockquote>
</aside>
<p>
I deleted the setting file, and it fixed the crash during the launch for me. Hopefully it helps.</p>

---

## Post #11 by @jamesobutler (2022-12-07 15:01 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> and <a class="mention" href="/u/young_wang">@Young_Wang</a> Using Slicer 5.2.1, can you try reinstalling SlicerIGSIO (or the other extensions that pull in SlicerIGSIO such as Slicer IGT) on your macOS machines and see if there is a crash on close? You could attempt checking for extension updates as well. Please report back here your results.</p>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> pushed updates yesterday to use the latest versions of VP9 which supposedly have better support for macOS 11+.</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/IGSIO/SlicerIGSIO/commit/24ee86eb19cceedd1c2dae1dda5e999c324fd5b3">
  <header class="source">

      <a href="https://github.com/IGSIO/SlicerIGSIO/commit/24ee86eb19cceedd1c2dae1dda5e999c324fd5b3" target="_blank" rel="noopener nofollow ugc">github.com/IGSIO/SlicerIGSIO</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/IGSIO/SlicerIGSIO/commit/24ee86eb19cceedd1c2dae1dda5e999c324fd5b3" target="_blank" rel="noopener nofollow ugc">ENH: Update VP9 to 1.12.0</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2022-12-06" data-time="23:55:55" data-timezone="UTC">11:55PM - 06 Dec 22 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/Sunderlandkyl" target="_blank" rel="noopener nofollow ugc">
          <img alt="Sunderlandkyl" src="https://avatars.githubusercontent.com/u/9222709?v=4" class="onebox-avatar-inline" width="20" height="20">
          Sunderlandkyl
        </a>
      </div>

      <div class="lines" title="changed 1 files with 3 additions and 3 deletions">
        <a href="https://github.com/IGSIO/SlicerIGSIO/commit/24ee86eb19cceedd1c2dae1dda5e999c324fd5b3" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+3</span>
          <span class="removed">-3</span>
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
<aside class="onebox githubcommit" data-onebox-src="https://github.com/IGSIO/IGSIO/commit/730a632c779b72618f6a4718cb43b0fb62a7d3e2">
  <header class="source">

      <a href="https://github.com/IGSIO/IGSIO/commit/730a632c779b72618f6a4718cb43b0fb62a7d3e2" target="_blank" rel="noopener nofollow ugc">github.com/IGSIO/IGSIO</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/IGSIO/IGSIO/commit/730a632c779b72618f6a4718cb43b0fb62a7d3e2" target="_blank" rel="noopener nofollow ugc">ENH: Update VP9 to 1.12.0</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2022-12-06" data-time="23:59:35" data-timezone="UTC">11:59PM - 06 Dec 22 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/Sunderlandkyl" target="_blank" rel="noopener nofollow ugc">
          <img alt="Sunderlandkyl" src="https://avatars.githubusercontent.com/u/9222709?v=4" class="onebox-avatar-inline" width="20" height="20">
          Sunderlandkyl
        </a>
      </div>

      <div class="lines" title="changed 1 files with 6 additions and 3 deletions">
        <a href="https://github.com/IGSIO/IGSIO/commit/730a632c779b72618f6a4718cb43b0fb62a7d3e2" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+6</span>
          <span class="removed">-3</span>
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


---

## Post #12 by @muratmaga (2022-12-09 17:22 UTC)

<p>I tried the official update, and now Slicer doesn’t start, Crash log appears immediately:</p>
<hr>
<h2><a name="p-87373-translated-report-full-report-below-1" class="anchor" href="#p-87373-translated-report-full-report-below-1" aria-label="Heading link"></a>Translated Report (Full Report Below)</h2>
<p>Process:               Slicer [96880]<br>
Path:                  /Applications/Slicer.app/Contents/MacOS/Slicer<br>
Identifier:            org.slicer.slicer<br>
Version:               5.2.1 (5.2.1)<br>
Code Type:             X86-64 (Native)<br>
Parent Process:        launchd [1]<br>
User ID:               1950572333</p>
<p>Date/Time:             2022-12-09 09:20:28.5235 -0800<br>
OS Version:            macOS 12.6.1 (21G217)<br>
Report Version:        12<br>
Bridge OS Version:     7.0 (20P411)<br>
Anonymous UUID:        061333B8-0FD5-DBE2-ED53-7B373F48D0CE</p>
<p>Time Awake Since Boot: 1400000 seconds</p>
<p>System Integrity Protection: enabled</p>
<p>Crashed Thread:        0  Dispatch queue: com.apple.main-thread</p>
<p>Exception Type:        EXC_CRASH (SIGABRT)<br>
Exception Codes:       0x0000000000000000, 0x0000000000000000<br>
Exception Note:        EXC_CORPSE_NOTIFY</p>
<p>Application Specific Information:<br>
abort() called</p>
<p>Thread 0 Crashed::  Dispatch queue: com.apple.main-thread<br>
0   libsystem_kernel.dylib        	    0x7ff8122f600e __pthread_kill + 10<br>
1   libsystem_pthread.dylib       	    0x7ff81232c1ff pthread_kill + 263<br>
2   libsystem_c.dylib             	    0x7ff812277d24 abort + 123<br>
3   libsystem_malloc.dylib        	    0x7ff812155357 malloc_vreport + 551<br>
4   libsystem_malloc.dylib        	    0x7ff812169308 malloc_zone_error + 178<br>
5   libsystem_malloc.dylib        	    0x7ff81214a50c tiny_malloc_from_free_list + 1820<br>
6   libsystem_malloc.dylib        	    0x7ff8121498ad tiny_malloc_should_clear + 255<br>
7   libsystem_malloc.dylib        	    0x7ff8121487d2 szone_malloc_should_clear + 66<br>
8   libsystem_malloc.dylib        	    0x7ff812163abb _malloc_zone_malloc + 125<br>
9   libpython3.9.dylib            	       0x10ddf2682 _PyObject_Malloc + 50<br>
10  libpython3.9.dylib            	       0x10dd849e8 _PyObject_GC_Alloc + 104<br>
11  libpython3.9.dylib            	       0x10ddff957 PyType_GenericAlloc + 215<br>
12  libPythonQt.dylib             	       0x1071956a3 PythonQtClassWrapper_alloc(_typeobject*, long) + 19<br>
13  libpython3.9.dylib            	       0x10de03b60 type_new + 1024<br>
14  libpython3.9.dylib            	       0x10de02eac type_call + 76<br>
15  libpython3.9.dylib            	       0x10dd9a5dd _PyObject_Call + 141<br>
16  libPythonQt.dylib             	       0x1071f0b1c PythonQtPrivate::createNewPythonQtClassWrapper(PythonQtClassInfo*, _object*, QByteArray const&amp;) + 172<br>
17  libPythonQt.dylib             	       0x1071f0878 PythonQtPrivate::createPythonQtClassWrapper(PythonQtClassInfo*, char const*, _object*) + 216<br>
18  libPythonQt.dylib             	       0x1071f04f3 PythonQtPrivate::registerClass(QMetaObject const*, char const*, QObject* (<em>)(), void (</em>)(void*, PythonQtInstanceWrapperStruct*), _object*, int) + 387<br>
19  libPythonQt.dylib             	       0x1071f14d9 PythonQtPrivate::wrapPtr(void*, QByteArray const&amp;, bool) + 1097<br>
20  libPythonQt.dylib             	       0x107257cc9 PythonQtCallSlot(PythonQtClassInfo*, QObject*, _object*, bool, PythonQtSlotInfo*, void*, _object**, void**, PythonQtPassThisOwnershipType*) + 1641<br>
21  libPythonQt.dylib             	       0x107259768 PythonQtSlotFunction_CallImpl(PythonQtClassInfo*, QObject*, PythonQtSlotInfo*, _object*, _object*, void*, void**, PythonQtPassThisOwnershipType*) + 1928<br>
22  libPythonQt.dylib             	       0x1072583f8 PythonQtMemberFunction_Call(PythonQtSlotInfo*, _object*, _object*, _object*) + 216<br>
23  libpython3.9.dylib            	       0x10dd9a067 _PyObject_MakeTpCall + 375<br>
24  libpython3.9.dylib            	       0x10deb2d90 call_function + 768<br>
25  libpython3.9.dylib            	       0x10deaf728 _PyEval_EvalFrameDefault + 26520<br>
26  libpython3.9.dylib            	       0x10dd9a885 function_code_fastcall + 229<br>
27  libpython3.9.dylib            	       0x10ddae1a2 method_vectorcall + 450<br>
28  libPythonQt.dylib             	       0x107256586 PythonQtSignalTarget::call(_object*, PythonQtMethodInfo const*, void**, bool) + 326<br>
29  libPythonQt.dylib             	       0x107257241 PythonQtSignalReceiver::qt_metacall(QMetaObject::Call, int, void**) + 193<br>
30  QtCore                        	       0x104f1af0e 0x104cef000 + 2277134<br>
31  libqSlicerBaseQTCore.dylib    	       0x102e69873 qSlicerModuleManager::qt_static_metacall(QObject*, QMetaObject::Call, int, void**) + 275<br>
32  QtCore                        	       0x104f1b075 0x104cef000 + 2277493<br>
33  libqSlicerBaseQTCore.dylib    	       0x102e69497 qSlicerModuleFactoryManager::moduleLoaded(QString const&amp;) + 55<br>
34  libqSlicerBaseQTCore.dylib    	       0x102e24866 qSlicerModuleFactoryManager::loadModule(QString const&amp;, QString const&amp;) + 1926<br>
35  libqSlicerBaseQTCore.dylib    	       0x102e238cf qSlicerModuleFactoryManager::loadModule(QString const&amp;) + 31<br>
36  Slicer                        	       0x101d183d3 int qSlicerApplicationHelper::postInitializeApplication(qSlicerApplication&amp;, QScopedPointer&lt;QSplashScreen, QScopedPointerDeleter &gt;&amp;, QScopedPointer&lt;qSlicerAppMainWindow, QScopedPointerDeleter &gt;&amp;) + 5971<br>
37  Slicer                        	       0x101d16990 main + 144<br>
38  dyld                          	       0x11032c52e start + 462</p>
<p>Thread 1:<br>
0   libsystem_pthread.dylib       	    0x7ff812327f48 start_wqthread + 0</p>
<p>Thread 2:<br>
0   libsystem_pthread.dylib       	    0x7ff812327f48 start_wqthread + 0</p>
<p>Thread 3:<br>
0   libsystem_kernel.dylib        	    0x7ff8122f22be __semwait_signal + 10<br>
1   libsystem_c.dylib             	    0x7ff812206863 nanosleep + 196<br>
2   libsystem_c.dylib             	    0x7ff812206799 usleep + 53<br>
3   libSlicerBaseLogic.dylib      	       0x10341bbcc vtkSlicerApplicationLogic::ProcessProcessingTasks() + 364<br>
4   libSlicerBaseLogic.dylib      	       0x10341b816 vtkSlicerApplicationLogic::ProcessingThreaderCallback(void*) + 38<br>
5   libsystem_pthread.dylib       	    0x7ff81232c4e1 _pthread_start + 125<br>
6   libsystem_pthread.dylib       	    0x7ff812327f6b thread_start + 15</p>
<p>Thread 4:<br>
0   libsystem_kernel.dylib        	    0x7ff8122f22be __semwait_signal + 10<br>
1   libsystem_c.dylib             	    0x7ff812206863 nanosleep + 196<br>
2   libsystem_c.dylib             	    0x7ff812206799 usleep + 53<br>
3   libSlicerBaseLogic.dylib      	       0x10341bd8c vtkSlicerApplicationLogic::ProcessNetworkingTasks() + 364<br>
4   libSlicerBaseLogic.dylib      	       0x10341b8c6 vtkSlicerApplicationLogic::NetworkingThreaderCallback(void*) + 38<br>
5   libsystem_pthread.dylib       	    0x7ff81232c4e1 _pthread_start + 125<br>
6   libsystem_pthread.dylib       	    0x7ff812327f6b thread_start + 15</p>
<p>Thread 5:: Qt bearer thread<br>
0   libsystem_kernel.dylib        	    0x7ff8122f60aa poll + 10<br>
1   QtCore                        	       0x104f4a1c0 qt_safe_poll(pollfd*, unsigned int, timespec const*) + 608<br>
2   QtCore                        	       0x104f4b9c1 QEventDispatcherUNIX::processEvents(QFlags<a>QEventLoop::ProcessEventsFlag</a>) + 849<br>
3   QtCore                        	       0x104ee3a6f QEventLoop::exec(QFlags<a>QEventLoop::ProcessEventsFlag</a>) + 431<br>
4   QtCore                        	       0x104d10553 QThread::exec() + 131<br>
5   QtCore                        	       0x104d11569 0x104cef000 + 140649<br>
6   libsystem_pthread.dylib       	    0x7ff81232c4e1 _pthread_start + 125<br>
7   libsystem_pthread.dylib       	    0x7ff812327f6b thread_start + 15</p>
<p>Thread 6:: ctkFDHandler<br>
0   libsystem_kernel.dylib        	    0x7ff8122f03ba read + 10<br>
1   libCTKCore.0.1.dylib          	       0x103391a11 ctkFDHandler::run() + 113<br>
2   QtCore                        	       0x104d11569 0x104cef000 + 140649<br>
3   libsystem_pthread.dylib       	    0x7ff81232c4e1 _pthread_start + 125<br>
4   libsystem_pthread.dylib       	    0x7ff812327f6b thread_start + 15</p>
<p>Thread 7:: ctkFDHandler<br>
0   libsystem_kernel.dylib        	    0x7ff8122f03ba read + 10<br>
1   libCTKCore.0.1.dylib          	       0x103391a11 ctkFDHandler::run() + 113<br>
2   QtCore                        	       0x104d11569 0x104cef000 + 140649<br>
3   libsystem_pthread.dylib       	    0x7ff81232c4e1 _pthread_start + 125<br>
4   libsystem_pthread.dylib       	    0x7ff812327f6b thread_start + 15</p>
<p>Thread 8:<br>
0   libsystem_pthread.dylib       	    0x7ff812327f48 start_wqthread + 0</p>
<p>Thread 9:: com.apple.NSEventThread<br>
0   libsystem_kernel.dylib        	    0x7ff8122ef97a mach_msg_trap + 10<br>
1   libsystem_kernel.dylib        	    0x7ff8122efce8 mach_msg + 56<br>
2   CoreFoundation                	    0x7ff8123f336d __CFRunLoopServiceMachPort + 319<br>
3   CoreFoundation                	    0x7ff8123f19f8 __CFRunLoopRun + 1276<br>
4   CoreFoundation                	    0x7ff8123f0e3c CFRunLoopRunSpecific + 562<br>
5   AppKit                        	    0x7ff814f989ce _NSEventThread + 132<br>
6   libsystem_pthread.dylib       	    0x7ff81232c4e1 _pthread_start + 125<br>
7   libsystem_pthread.dylib       	    0x7ff812327f6b thread_start + 15</p>
<p>Thread 10:: Thread (pooled)<br>
0   libsystem_kernel.dylib        	    0x7ff8122f23ea __psynch_cvwait + 10<br>
1   libsystem_pthread.dylib       	    0x7ff81232ca6f _pthread_cond_wait + 1249<br>
2   QtCore                        	       0x104d199ff 0x104cef000 + 174591<br>
3   QtCore                        	       0x104d196ce 0x104cef000 + 173774<br>
4   QtCore                        	       0x104d195ed QWaitCondition::wait(QMutex*, QDeadlineTimer) + 93<br>
5   QtCore                        	       0x104d15c1d 0x104cef000 + 158749<br>
6   QtCore                        	       0x104d11569 0x104cef000 + 140649<br>
7   libsystem_pthread.dylib       	    0x7ff81232c4e1 _pthread_start + 125<br>
8   libsystem_pthread.dylib       	    0x7ff812327f6b thread_start + 15</p>
<p>Thread 11:: Thread (pooled)<br>
0   libsystem_kernel.dylib        	    0x7ff8122f23ea __psynch_cvwait + 10<br>
1   libsystem_pthread.dylib       	    0x7ff81232ca6f _pthread_cond_wait + 1249<br>
2   QtCore                        	       0x104d199ff 0x104cef000 + 174591<br>
3   QtCore                        	       0x104d196ce 0x104cef000 + 173774<br>
4   QtCore                        	       0x104d195ed QWaitCondition::wait(QMutex*, QDeadlineTimer) + 93<br>
5   QtCore                        	       0x104d15c1d 0x104cef000 + 158749<br>
6   QtCore                        	       0x104d11569 0x104cef000 + 140649<br>
7   libsystem_pthread.dylib       	    0x7ff81232c4e1 _pthread_start + 125<br>
8   libsystem_pthread.dylib       	    0x7ff812327f6b thread_start + 15</p>
<p>Thread 12:: Thread (pooled)<br>
0   libsystem_kernel.dylib        	    0x7ff8122f23ea __psynch_cvwait + 10<br>
1   libsystem_pthread.dylib       	    0x7ff81232ca6f _pthread_cond_wait + 1249<br>
2   QtCore                        	       0x104d199ff 0x104cef000 + 174591<br>
3   QtCore                        	       0x104d196ce 0x104cef000 + 173774<br>
4   QtCore                        	       0x104d195ed QWaitCondition::wait(QMutex*, QDeadlineTimer) + 93<br>
5   QtCore                        	       0x104d15c1d 0x104cef000 + 158749<br>
6   QtCore                        	       0x104d11569 0x104cef000 + 140649<br>
7   libsystem_pthread.dylib       	    0x7ff81232c4e1 _pthread_start + 125<br>
8   libsystem_pthread.dylib       	    0x7ff812327f6b thread_start + 15</p>
<p>Thread 13:: Thread (pooled)<br>
0   libsystem_kernel.dylib        	    0x7ff8122f23ea __psynch_cvwait + 10<br>
1   libsystem_pthread.dylib       	    0x7ff81232ca6f _pthread_cond_wait + 1249<br>
2   QtCore                        	       0x104d199ff 0x104cef000 + 174591<br>
3   QtCore                        	       0x104d196ce 0x104cef000 + 173774<br>
4   QtCore                        	       0x104d195ed QWaitCondition::wait(QMutex*, QDeadlineTimer) + 93<br>
5   QtCore                        	       0x104d15c1d 0x104cef000 + 158749<br>
6   QtCore                        	       0x104d11569 0x104cef000 + 140649<br>
7   libsystem_pthread.dylib       	    0x7ff81232c4e1 _pthread_start + 125<br>
8   libsystem_pthread.dylib       	    0x7ff812327f6b thread_start + 15</p>
<p>Thread 14:: Thread (pooled)<br>
0   libsystem_kernel.dylib        	    0x7ff8122f23ea __psynch_cvwait + 10<br>
1   libsystem_pthread.dylib       	    0x7ff81232ca6f _pthread_cond_wait + 1249<br>
2   QtCore                        	       0x104d199ff 0x104cef000 + 174591<br>
3   QtCore                        	       0x104d196ce 0x104cef000 + 173774<br>
4   QtCore                        	       0x104d195ed QWaitCondition::wait(QMutex*, QDeadlineTimer) + 93<br>
5   QtCore                        	       0x104d15c1d 0x104cef000 + 158749<br>
6   QtCore                        	       0x104d11569 0x104cef000 + 140649<br>
7   libsystem_pthread.dylib       	    0x7ff81232c4e1 _pthread_start + 125<br>
8   libsystem_pthread.dylib       	    0x7ff812327f6b thread_start + 15</p>
<p>Thread 15:: Thread (pooled)<br>
0   libsystem_kernel.dylib        	    0x7ff8122f23ea __psynch_cvwait + 10<br>
1   libsystem_pthread.dylib       	    0x7ff81232ca6f _pthread_cond_wait + 1249<br>
2   QtCore                        	       0x104d199ff 0x104cef000 + 174591<br>
3   QtCore                        	       0x104d196ce 0x104cef000 + 173774<br>
4   QtCore                        	       0x104d195ed QWaitCondition::wait(QMutex*, QDeadlineTimer) + 93<br>
5   QtCore                        	       0x104d15c1d 0x104cef000 + 158749<br>
6   QtCore                        	       0x104d11569 0x104cef000 + 140649<br>
7   libsystem_pthread.dylib       	    0x7ff81232c4e1 _pthread_start + 125<br>
8   libsystem_pthread.dylib       	    0x7ff812327f6b thread_start + 15</p>
<p>Thread 16:: Thread (pooled)<br>
0   libsystem_kernel.dylib        	    0x7ff8122f23ea __psynch_cvwait + 10<br>
1   libsystem_pthread.dylib       	    0x7ff81232ca6f _pthread_cond_wait + 1249<br>
2   QtCore                        	       0x104d199ff 0x104cef000 + 174591<br>
3   QtCore                        	       0x104d196ce 0x104cef000 + 173774<br>
4   QtCore                        	       0x104d195ed QWaitCondition::wait(QMutex*, QDeadlineTimer) + 93<br>
5   QtCore                        	       0x104d15c1d 0x104cef000 + 158749<br>
6   QtCore                        	       0x104d11569 0x104cef000 + 140649<br>
7   libsystem_pthread.dylib       	    0x7ff81232c4e1 _pthread_start + 125<br>
8   libsystem_pthread.dylib       	    0x7ff812327f6b thread_start + 15</p>
<p>Thread 17:: Thread (pooled)<br>
0   libsystem_kernel.dylib        	    0x7ff8122f23ea __psynch_cvwait + 10<br>
1   libsystem_pthread.dylib       	    0x7ff81232ca6f _pthread_cond_wait + 1249<br>
2   QtCore                        	       0x104d199ff 0x104cef000 + 174591<br>
3   QtCore                        	       0x104d196ce 0x104cef000 + 173774<br>
4   QtCore                        	       0x104d195ed QWaitCondition::wait(QMutex*, QDeadlineTimer) + 93<br>
5   QtCore                        	       0x104d15c1d 0x104cef000 + 158749<br>
6   QtCore                        	       0x104d11569 0x104cef000 + 140649<br>
7   libsystem_pthread.dylib       	    0x7ff81232c4e1 _pthread_start + 125<br>
8   libsystem_pthread.dylib       	    0x7ff812327f6b thread_start + 15</p>
<p>Thread 18:: Thread (pooled)<br>
0   libsystem_kernel.dylib        	    0x7ff8122f23ea __psynch_cvwait + 10<br>
1   libsystem_pthread.dylib       	    0x7ff81232ca6f _pthread_cond_wait + 1249<br>
2   QtCore                        	       0x104d199ff 0x104cef000 + 174591<br>
3   QtCore                        	       0x104d196ce 0x104cef000 + 173774<br>
4   QtCore                        	       0x104d195ed QWaitCondition::wait(QMutex*, QDeadlineTimer) + 93<br>
5   QtCore                        	       0x104d15c1d 0x104cef000 + 158749<br>
6   QtCore                        	       0x104d11569 0x104cef000 + 140649<br>
7   libsystem_pthread.dylib       	    0x7ff81232c4e1 _pthread_start + 125<br>
8   libsystem_pthread.dylib       	    0x7ff812327f6b thread_start + 15</p>
<p>Thread 19:<br>
0   libsystem_kernel.dylib        	    0x7ff8122f23ea __psynch_cvwait + 10<br>
1   libsystem_pthread.dylib       	    0x7ff81232ca6f _pthread_cond_wait + 1249<br>
2   libopenblas.0.dylib           	       0x15897370f blas_thread_server + 207<br>
3   libsystem_pthread.dylib       	    0x7ff81232c4e1 _pthread_start + 125<br>
4   libsystem_pthread.dylib       	    0x7ff812327f6b thread_start + 15</p>
<p>Thread 20:<br>
0   libsystem_kernel.dylib        	    0x7ff8122f23ea __psynch_cvwait + 10<br>
1   libsystem_pthread.dylib       	    0x7ff81232ca6f _pthread_cond_wait + 1249<br>
2   libopenblas.0.dylib           	       0x15897370f blas_thread_server + 207<br>
3   libsystem_pthread.dylib       	    0x7ff81232c4e1 _pthread_start + 125<br>
4   libsystem_pthread.dylib       	    0x7ff812327f6b thread_start + 15</p>
<p>Thread 21:<br>
0   libsystem_kernel.dylib        	    0x7ff8122f23ea __psynch_cvwait + 10<br>
1   libsystem_pthread.dylib       	    0x7ff81232ca6f _pthread_cond_wait + 1249<br>
2   libopenblas.0.dylib           	       0x15897370f blas_thread_server + 207<br>
3   libsystem_pthread.dylib       	    0x7ff81232c4e1 _pthread_start + 125<br>
4   libsystem_pthread.dylib       	    0x7ff812327f6b thread_start + 15</p>
<p>Thread 22:<br>
0   libsystem_kernel.dylib        	    0x7ff8122f23ea __psynch_cvwait + 10<br>
1   libsystem_pthread.dylib       	    0x7ff81232ca6f _pthread_cond_wait + 1249<br>
2   libopenblas.0.dylib           	       0x15897370f blas_thread_server + 207<br>
3   libsystem_pthread.dylib       	    0x7ff81232c4e1 _pthread_start + 125<br>
4   libsystem_pthread.dylib       	    0x7ff812327f6b thread_start + 15</p>
<p>Thread 23:<br>
0   libsystem_kernel.dylib        	    0x7ff8122f23ea __psynch_cvwait + 10<br>
1   libsystem_pthread.dylib       	    0x7ff81232ca6f _pthread_cond_wait + 1249<br>
2   libopenblas.0.dylib           	       0x15897370f blas_thread_server + 207<br>
3   libsystem_pthread.dylib       	    0x7ff81232c4e1 _pthread_start + 125<br>
4   libsystem_pthread.dylib       	    0x7ff812327f6b thread_start + 15</p>
<p>Thread 24:<br>
0   libsystem_kernel.dylib        	    0x7ff8122f23ea __psynch_cvwait + 10<br>
1   libsystem_pthread.dylib       	    0x7ff81232ca6f _pthread_cond_wait + 1249<br>
2   libopenblas.0.dylib           	       0x15897370f blas_thread_server + 207<br>
3   libsystem_pthread.dylib       	    0x7ff81232c4e1 _pthread_start + 125<br>
4   libsystem_pthread.dylib       	    0x7ff812327f6b thread_start + 15</p>
<p>Thread 25:<br>
0   libsystem_kernel.dylib        	    0x7ff8122f23ea __psynch_cvwait + 10<br>
1   libsystem_pthread.dylib       	    0x7ff81232ca6f _pthread_cond_wait + 1249<br>
2   libopenblas.0.dylib           	       0x15897370f blas_thread_server + 207<br>
3   libsystem_pthread.dylib       	    0x7ff81232c4e1 _pthread_start + 125<br>
4   libsystem_pthread.dylib       	    0x7ff812327f6b thread_start + 15</p>
<p>Thread 26:: Thread (pooled)<br>
0   libsystem_kernel.dylib        	    0x7ff8122f23ea __psynch_cvwait + 10<br>
1   libsystem_pthread.dylib       	    0x7ff81232ca6f _pthread_cond_wait + 1249<br>
2   QtCore                        	       0x104d199ff 0x104cef000 + 174591<br>
3   QtCore                        	       0x104d196ce 0x104cef000 + 173774<br>
4   QtCore                        	       0x104d195ed QWaitCondition::wait(QMutex*, QDeadlineTimer) + 93<br>
5   QtCore                        	       0x104d15c1d 0x104cef000 + 158749<br>
6   QtCore                        	       0x104d11569 0x104cef000 + 140649<br>
7   libsystem_pthread.dylib       	    0x7ff81232c4e1 _pthread_start + 125<br>
8   libsystem_pthread.dylib       	    0x7ff812327f6b thread_start + 15</p>
<p>Thread 27:: Thread (pooled)<br>
0   libsystem_kernel.dylib        	    0x7ff8122f23ea __psynch_cvwait + 10<br>
1   libsystem_pthread.dylib       	    0x7ff81232ca6f _pthread_cond_wait + 1249<br>
2   QtCore                        	       0x104d199ff 0x104cef000 + 174591<br>
3   QtCore                        	       0x104d196ce 0x104cef000 + 173774<br>
4   QtCore                        	       0x104d195ed QWaitCondition::wait(QMutex*, QDeadlineTimer) + 93<br>
5   QtCore                        	       0x104d15c1d 0x104cef000 + 158749<br>
6   QtCore                        	       0x104d11569 0x104cef000 + 140649<br>
7   libsystem_pthread.dylib       	    0x7ff81232c4e1 _pthread_start + 125<br>
8   libsystem_pthread.dylib       	    0x7ff812327f6b thread_start + 15</p>
<p>Thread 28:: Thread (pooled)<br>
0   libsystem_kernel.dylib        	    0x7ff8122f23ea __psynch_cvwait + 10<br>
1   libsystem_pthread.dylib       	    0x7ff81232ca6f _pthread_cond_wait + 1249<br>
2   QtCore                        	       0x104d199ff 0x104cef000 + 174591<br>
3   QtCore                        	       0x104d196ce 0x104cef000 + 173774<br>
4   QtCore                        	       0x104d195ed QWaitCondition::wait(QMutex*, QDeadlineTimer) + 93<br>
5   QtCore                        	       0x104d15c1d 0x104cef000 + 158749<br>
6   QtCore                        	       0x104d11569 0x104cef000 + 140649<br>
7   libsystem_pthread.dylib       	    0x7ff81232c4e1 _pthread_start + 125<br>
8   libsystem_pthread.dylib       	    0x7ff812327f6b thread_start + 15</p>
<p>Thread 29:<br>
0   libsystem_pthread.dylib       	    0x7ff812327f48 start_wqthread + 0</p>
<p>Thread 30:: AMCP Logging Spool<br>
0   libsystem_kernel.dylib        	    0x7ff8122ef9b6 semaphore_wait_trap + 10<br>
1   caulk                         	    0x7ff81ae2c2e6 caulk::mach::semaphore::wait_or_error() + 16<br>
2   caulk                         	    0x7ff81ae14148 caulk::concurrent::details::worker_thread::run() + 36<br>
3   caulk                         	    0x7ff81ae13e0c void* caulk::thread_proxy&lt;std::__1::tuple&lt;caulk:<img src="https://emoji.discourse-cdn.com/twitter/thread.png?v=15" title=":thread:" class="emoji" alt=":thread:" loading="lazy" width="20" height="20">:attributes, void (caulk::concurrent::details::worker_thread::<em>)(), std::__1::tuple<a>caulk::concurrent::details::worker_thread*</a> &gt; &gt;(void</em>) + 41<br>
4   libsystem_pthread.dylib       	    0x7ff81232c4e1 _pthread_start + 125<br>
5   libsystem_pthread.dylib       	    0x7ff812327f6b thread_start + 15</p>
<p>Thread 31:: QFileInfoGatherer<br>
0   libsystem_kernel.dylib        	    0x7ff8122f23ea __psynch_cvwait + 10<br>
1   libsystem_pthread.dylib       	    0x7ff81232ca6f _pthread_cond_wait + 1249<br>
2   QtCore                        	       0x104d196ab 0x104cef000 + 173739<br>
3   QtCore                        	       0x104d195ed QWaitCondition::wait(QMutex*, QDeadlineTimer) + 93<br>
4   QtWidgets                     	       0x103709c88 0x1034c9000 + 2362504<br>
5   QtCore                        	       0x104d11569 0x104cef000 + 140649<br>
6   libsystem_pthread.dylib       	    0x7ff81232c4e1 _pthread_start + 125<br>
7   libsystem_pthread.dylib       	    0x7ff812327f6b thread_start + 15</p>
<p>Thread 32:: QFileInfoGatherer<br>
0   libsystem_kernel.dylib        	    0x7ff8122f23ea __psynch_cvwait + 10<br>
1   libsystem_pthread.dylib       	    0x7ff81232ca6f _pthread_cond_wait + 1249<br>
2   QtCore                        	       0x104d196ab 0x104cef000 + 173739<br>
3   QtCore                        	       0x104d195ed QWaitCondition::wait(QMutex*, QDeadlineTimer) + 93<br>
4   QtWidgets                     	       0x103709c88 0x1034c9000 + 2362504<br>
5   QtCore                        	       0x104d11569 0x104cef000 + 140649<br>
6   libsystem_pthread.dylib       	    0x7ff81232c4e1 _pthread_start + 125<br>
7   libsystem_pthread.dylib       	    0x7ff812327f6b thread_start + 15</p>
<p>Thread 0 crashed with X86 Thread State (64-bit):<br>
rax: 0x0000000000000000  rbx: 0x00000001103a7600  rcx: 0x00007ff7be2257e8  rdx: 0x0000000000000000<br>
rdi: 0x0000000000000103  rsi: 0x0000000000000006  rbp: 0x00007ff7be225810  rsp: 0x00007ff7be2257e8<br>
r8: 0x0000000000000001   r9: 0x0000000000000000  r10: 0x0000000000000000  r11: 0x0000000000000246<br>
r12: 0x0000000000000103  r13: 0x0000000000000043  r14: 0x0000000000000006  r15: 0x0000000000000016<br>
rip: 0x00007ff8122f600e  rfl: 0x0000000000000246  cr2: 0x00007ff853a9b008</p>
<p>Logical CPU:     0<br>
Error Code:      0x02000148<br>
Trap Number:     133</p>
<p>Binary Images:<br>
0x7ff8122ee000 -     0x7ff812325fff libsystem_kernel.dylib (<em>) &lt;0ea0d8ac-c27b-3a71-a59b-ec3a6f116acf&gt; /usr/lib/system/libsystem_kernel.dylib<br>
0x7ff812326000 -     0x7ff812331fff libsystem_pthread.dylib (</em>)  /usr/lib/system/libsystem_pthread.dylib<br>
0x7ff8121f6000 -     0x7ff81227efff libsystem_c.dylib (<em>)  /usr/lib/system/libsystem_c.dylib<br>
0x7ff812146000 -     0x7ff812171fff libsystem_malloc.dylib (</em>) &lt;47042acd-a337-322a-8db7-ecd59cc60d92&gt; /usr/lib/system/libsystem_malloc.dylib<br>
0x10dd82000 -        0x10e029fff libpython3.9.dylib (<em>) &lt;9049176e-b3d9-3325-84d9-f6121239ab76&gt; /Applications/Slicer.app/Contents/lib/Python/lib/libpython3.9.dylib<br>
0x107185000 -        0x107aecfff libPythonQt.dylib (</em>) &lt;60b5ff11-32b7-39bc-9dee-e1196ec1e752&gt; /Applications/Slicer.app/Contents/lib/Slicer-5.2/libPythonQt.dylib<br>
0x104cef000 -        0x10525ffff org.qt-project.QtCore (5.15)  /Applications/Slicer.app/Contents/Frameworks/QtCore.framework/Versions/5/QtCore<br>
0x102dad000 -        0x102eb1fff libqSlicerBaseQTCore.dylib (<em>)  /Applications/Slicer.app/Contents/lib/Slicer-5.2/libqSlicerBaseQTCore.dylib<br>
0x101cd9000 -        0x101d1afff org.slicer.slicer (5.2.1) &lt;0d378013-ad07-308c-a7b7-b5418f961ffa&gt; /Applications/Slicer.app/Contents/MacOS/Slicer<br>
0x110327000 -        0x110392fff dyld (</em>) &lt;7b87a986-a153-33c4-8470-d56410b7f9d5&gt; /usr/lib/dyld<br>
0x1033f0000 -        0x103454fff libSlicerBaseLogic.dylib (<em>) &lt;1173d1b8-e8b1-364f-82cb-e3171c0d5fa8&gt; /Applications/Slicer.app/Contents/lib/Slicer-5.2/libSlicerBaseLogic.dylib<br>
0x103377000 -        0x1033bafff libCTKCore.0.1.dylib (</em>)  /Applications/Slicer.app/Contents/lib/Slicer-5.2/libCTKCore.0.1.dylib<br>
0x7ff812373000 -     0x7ff812875fff com.apple.CoreFoundation (6.9) &lt;93c48919-68af-367e-9a67-db4159bc962c&gt; /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation<br>
0x7ff814dec000 -     0x7ff815c7bfff com.apple.AppKit (6.9)  /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit<br>
0x15863a000 -        0x15c2a9fff libopenblas.0.dylib (*)  /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages/scipy/.dylibs/libopenblas.0.dylib<br>
0x7ff81ae12000 -     0x7ff81ae33fff com.apple.audio.caulk (1.0) &lt;8e7b3d95-1d47-3f17-9512-c5fcc30792c2&gt; /System/Library/PrivateFrameworks/caulk.framework/Versions/A/caulk<br>
0x1034c9000 -        0x10390ffff org.qt-project.QtWidgets (5.15) &lt;6a0c4de6-8a12-31d0-90cb-63e5c78b6c35&gt; /Applications/Slicer.app/Contents/Frameworks/QtWidgets.framework/Versions/5/QtWidgets</p>
<p>External Modification Summary:<br>
Calls made by other processes targeting this process:<br>
task_for_pid: 0<br>
thread_create: 0<br>
thread_set_state: 0<br>
Calls made by this process:<br>
task_for_pid: 0<br>
thread_create: 0<br>
thread_set_state: 0<br>
Calls made by all processes on this machine:<br>
task_for_pid: 0<br>
thread_create: 0<br>
thread_set_state: 0</p>
<p>VM Region Summary:<br>
ReadOnly portion of Libraries: Total=2.1G resident=0K(0%) swapped_out_or_unallocated=2.1G(100%)<br>
Writable regions: Total=1.3G written=0K(0%) resident=0K(0%) swapped_out=0K(0%) unallocated=1.3G(100%)</p>
<pre><code>                            VIRTUAL   REGION 
</code></pre>
<p>REGION TYPE                        SIZE    COUNT (non-coalesced)<br>
===========                     =======  =======<br>
Accelerate framework               256K        2<br>
Activity Tracing                   256K        1<br>
CG backing stores                 3840K        4<br>
CG image                            24K        1<br>
ColorSync                          224K       26<br>
CoreAnimation                       68K        6<br>
CoreGraphics                        12K        2<br>
CoreUI image data                  708K        5<br>
Foundation                          16K        1<br>
Kernel Alloc Once                    8K        1<br>
MALLOC                           361.2M      208<br>
MALLOC guard page                   32K        8<br>
MALLOC_LARGE (reserved)            384K        1         reserved VM address space (unallocated)<br>
MALLOC_NANO (reserved)           384.0M        1         reserved VM address space (unallocated)<br>
ObjC additional data                15K        1<br>
STACK GUARD                       56.1M       33<br>
Stack                             24.2M       33<br>
VM_ALLOCATE                      152.4M      242<br>
VM_ALLOCATE (reserved)           384.0M        4         reserved VM address space (unallocated)<br>
__CTF                               756        1<br>
__DATA                            92.4M     1449<br>
__DATA_CONST                      32.2M      335<br>
__DATA_DIRTY                      1637K      211<br>
__FONT_DATA                          4K        1<br>
__GLSLBUILTINS                    5176K        1<br>
__LINKEDIT                       811.3M      834<br>
__TEXT                             1.3G     1353<br>
__UNICODE                          592K        1<br>
dyld private memory               6144K        3<br>
mapped file                      373.2M       28<br>
shared memory                      792K       21<br>
===========                     =======  =======<br>
TOTAL                              3.9G     4818<br>
TOTAL, minus reserved VM space     3.1G     4818</p>
<hr>
<h2><a name="p-87373-full-report-2" class="anchor" href="#p-87373-full-report-2" aria-label="Heading link"></a>Full Report</h2>
<p>{“app_name”:“Slicer”,“timestamp”:“2022-12-09 09:20:29.00 -0800”,“app_version”:“5.2.1”,“slice_uuid”:“0d378013-ad07-308c-a7b7-b5418f961ffa”,“build_version”:“5.2.1”,“platform”:1,“bundleID”:“org.slicer.slicer”,“share_with_app_devs”:1,“is_first_party”:0,“bug_type”:“309”,“os_version”:“macOS 12.6.1 (21G217)”,“incident_id”:“10EFF45C-BDA4-4832-AEF4-AA1CF661354D”,“name”:“Slicer”}<br>
{<br>
“uptime” : 1400000,<br>
“procLaunch” : “2022-12-09 09:20:13.0786 -0800”,<br>
“procRole” : “Background”,<br>
“version” : 2,<br>
“userID” : 1950572333,<br>
“deployVersion” : 210,<br>
“modelCode” : “MacBookPro15,1”,<br>
“procStartAbsTime” : 1461357054716847,<br>
“coalitionID” : 64051,<br>
“osVersion” : {<br>
“train” : “macOS 12.6.1”,<br>
“build” : “21G217”,<br>
“releaseType” : “User”<br>
},<br>
“captureTime” : “2022-12-09 09:20:28.5235 -0800”,<br>
“incident” : “10EFF45C-BDA4-4832-AEF4-AA1CF661354D”,<br>
“bug_type” : “309”,<br>
“pid” : 96880,<br>
“procExitAbsTime” : 1461372498076149,<br>
“cpuType” : “X86-64”,<br>
“procName” : “Slicer”,<br>
“procPath” : “/Applications/Slicer.app/Contents/MacOS/Slicer”,<br>
“bundleInfo” : {“CFBundleShortVersionString”:“5.2.1”,“CFBundleVersion”:“5.2.1”,“CFBundleIdentifier”:“org.slicer.slicer”},<br>
“storeInfo” : {“deviceIdentifierForVendor”:“5711C463-2F32-5E5D-8265-6A5BDD3872BC”,“thirdParty”:true},<br>
“parentProc” : “launchd”,<br>
“parentPid” : 1,<br>
“coalitionName” : “org.slicer.slicer”,<br>
“crashReporterKey” : “061333B8-0FD5-DBE2-ED53-7B373F48D0CE”,<br>
“bridgeVersion” : {“build”:“20P411”,“train”:“7.0”},<br>
“sip” : “enabled”,<br>
“isCorpse” : 1,<br>
“exception” : {“codes”:“0x0000000000000000, 0x0000000000000000”,“rawCodes”:[0,0],“type”:“EXC_CRASH”,“signal”:“SIGABRT”},<br>
“asi” : {“libsystem_c.dylib”:[“abort() called”]},<br>
“extMods” : {“caller”:{“thread_create”:0,“thread_set_state”:0,“task_for_pid”:0},“system”:{“thread_create”:0,“thread_set_state”:0,“task_for_pid”:0},“targeted”:{“thread_create”:0,“thread_set_state”:0,“task_for_pid”:0},“warnings”:0},<br>
“faultingThread” : 0,<br>
“threads” : [{“triggered”:true,“id”:10187276,“threadState”:{“r13”:{“value”:67},“rax”:{“value”:0},“rflags”:{“value”:582},“cpu”:{“value”:0},“r14”:{“value”:6},“rsi”:{“value”:6},“r8”:{“value”:1},“cr2”:{“value”:140704532246536},“rdx”:{“value”:0},“r10”:{“value”:0},“r9”:{“value”:0},“r15”:{“value”:22},“rbx”:{“value”:4567234048,“symbolLocation”:0,“symbol”:“_main_thread”},“trap”:{“value”:133},“err”:{“value”:33554760},“r11”:{“value”:582},“rip”:{“value”:140703433711630,“matchesCrashFrame”:1},“rbp”:{“value”:140702023571472},“rsp”:{“value”:140702023571432},“r12”:{“value”:259},“rcx”:{“value”:140702023571432},“flavor”:“x86_THREAD_STATE”,“rdi”:{“value”:259}},“queue”:“com.apple.main-thread”,“frames”:[{“imageOffset”:32782,“symbol”:“__pthread_kill”,“symbolLocation”:10,“imageIndex”:0},{“imageOffset”:25087,“symbol”:“pthread_kill”,“symbolLocation”:263,“imageIndex”:1},{“imageOffset”:531748,“symbol”:“abort”,“symbolLocation”:123,“imageIndex”:2},{“imageOffset”:62295,“symbol”:“malloc_vreport”,“symbolLocation”:551,“imageIndex”:3},{“imageOffset”:144136,“symbol”:“malloc_zone_error”,“symbolLocation”:178,“imageIndex”:3},{“imageOffset”:17676,“symbol”:“tiny_malloc_from_free_list”,“symbolLocation”:1820,“imageIndex”:3},{“imageOffset”:14509,“symbol”:“tiny_malloc_should_clear”,“symbolLocation”:255,“imageIndex”:3},{“imageOffset”:10194,“symbol”:“szone_malloc_should_clear”,“symbolLocation”:66,“imageIndex”:3},{“imageOffset”:121531,“symbol”:“_malloc_zone_malloc”,“symbolLocation”:125,“imageIndex”:3},{“imageOffset”:460418,“symbol”:“_PyObject_Malloc”,“symbolLocation”:50,“imageIndex”:4},{“imageOffset”:10728,“symbol”:“_PyObject_GC_Alloc”,“symbolLocation”:104,“imageIndex”:4},{“imageOffset”:514391,“symbol”:“PyType_GenericAlloc”,“symbolLocation”:215,“imageIndex”:4},{“imageOffset”:67235,“symbol”:“PythonQtClassWrapper_alloc(_typeobject*, long)”,“symbolLocation”:19,“imageIndex”:5},{“imageOffset”:531296,“symbol”:“type_new”,“symbolLocation”:1024,“imageIndex”:4},{“imageOffset”:528044,“symbol”:“type_call”,“symbolLocation”:76,“imageIndex”:4},{“imageOffset”:99805,“symbol”:“_PyObject_Call”,“symbolLocation”:141,“imageIndex”:4},{“imageOffset”:441116,“symbol”:“PythonQtPrivate::createNewPythonQtClassWrapper(PythonQtClassInfo*, _object*, QByteArray const&amp;)”,“symbolLocation”:172,“imageIndex”:5},{“imageOffset”:440440,“symbol”:“PythonQtPrivate::createPythonQtClassWrapper(PythonQtClassInfo*, char const*, _object*)”,“symbolLocation”:216,“imageIndex”:5},{“imageOffset”:439539,“symbol”:“PythonQtPrivate::registerClass(QMetaObject const*, char const*, QObject* (<em>)(), void (</em>)(void*, PythonQtInstanceWrapperStruct*), _object*, int)”,“symbolLocation”:387,“imageIndex”:5},{“imageOffset”:443609,“symbol”:“PythonQtPrivate::wrapPtr(void*, QByteArray const&amp;, bool)”,“symbolLocation”:1097,“imageIndex”:5},{“imageOffset”:863433,“symbol”:“PythonQtCallSlot(PythonQtClassInfo*, QObject*, _object*, bool, PythonQtSlotInfo*, void*, _object**, void**, PythonQtPassThisOwnershipType*)”,“symbolLocation”:1641,“imageIndex”:5},{“imageOffset”:870248,“symbol”:“PythonQtSlotFunction_CallImpl(PythonQtClassInfo*, QObject*, PythonQtSlotInfo*, _object*, _object*, void*, void**, PythonQtPassThisOwnershipType*)”,“symbolLocation”:1928,“imageIndex”:5},{“imageOffset”:865272,“symbol”:“PythonQtMemberFunction_Call(PythonQtSlotInfo*, _object*, _object*, _object*)”,“symbolLocation”:216,“imageIndex”:5},{“imageOffset”:98407,“symbol”:“_PyObject_MakeTpCall”,“symbolLocation”:375,“imageIndex”:4},{“imageOffset”:1248656,“symbol”:“call_function”,“symbolLocation”:768,“imageIndex”:4},{“imageOffset”:1234728,“symbol”:“_PyEval_EvalFrameDefault”,“symbolLocation”:26520,“imageIndex”:4},{“imageOffset”:100485,“symbol”:“function_code_fastcall”,“symbolLocation”:229,“imageIndex”:4},{“imageOffset”:180642,“symbol”:“method_vectorcall”,“symbolLocation”:450,“imageIndex”:4},{“imageOffset”:857478,“symbol”:“PythonQtSignalTarget::call(_object*, PythonQtMethodInfo const*, void**, bool)”,“symbolLocation”:326,“imageIndex”:5},{“imageOffset”:860737,“symbol”:“PythonQtSignalReceiver::qt_metacall(QMetaObject::Call, int, void**)”,“symbolLocation”:193,“imageIndex”:5},{“imageOffset”:2277134,“imageIndex”:6},{“imageOffset”:772211,“symbol”:“qSlicerModuleManager::qt_static_metacall(QObject*, QMetaObject::Call, int, void**)”,“symbolLocation”:275,“imageIndex”:7},{“imageOffset”:2277493,“imageIndex”:6},{“imageOffset”:771223,“symbol”:“qSlicerModuleFactoryManager::moduleLoaded(QString const&amp;)”,“symbolLocation”:55,“imageIndex”:7},{“imageOffset”:489574,“symbol”:“qSlicerModuleFactoryManager::loadModule(QString const&amp;, QString const&amp;)”,“symbolLocation”:1926,“imageIndex”:7},{“imageOffset”:485583,“symbol”:“qSlicerModuleFactoryManager::loadModule(QString const&amp;)”,“symbolLocation”:31,“imageIndex”:7},{“imageOffset”:259027,“symbol”:“int qSlicerApplicationHelper::postInitializeApplication(qSlicerApplication&amp;, QScopedPointer&lt;QSplashScreen, QScopedPointerDeleter &gt;&amp;, QScopedPointer&lt;qSlicerAppMainWindow, QScopedPointerDeleter &gt;&amp;)”,“symbolLocation”:5971,“imageIndex”:8},{“imageOffset”:252304,“symbol”:“main”,“symbolLocation”:144,“imageIndex”:8},{“imageOffset”:21806,“symbol”:“start”,“symbolLocation”:462,“imageIndex”:9}]},{“id”:10187298,“frames”:[{“imageOffset”:8008,“symbol”:“start_wqthread”,“symbolLocation”:0,“imageIndex”:1}]},{“id”:10187307,“frames”:[{“imageOffset”:8008,“symbol”:“start_wqthread”,“symbolLocation”:0,“imageIndex”:1}]},{“id”:10187332,“frames”:[{“imageOffset”:17086,“symbol”:“__semwait_signal”,“symbolLocation”:10,“imageIndex”:0},{“imageOffset”:67683,“symbol”:“nanosleep”,“symbolLocation”:196,“imageIndex”:2},{“imageOffset”:67481,“symbol”:“usleep”,“symbolLocation”:53,“imageIndex”:2},{“imageOffset”:179148,“symbol”:“vtkSlicerApplicationLogic::ProcessProcessingTasks()”,“symbolLocation”:364,“imageIndex”:10},{“imageOffset”:178198,“symbol”:“vtkSlicerApplicationLogic::ProcessingThreaderCallback(void*)”,“symbolLocation”:38,“imageIndex”:10},{“imageOffset”:25825,“symbol”:“_pthread_start”,“symbolLocation”:125,“imageIndex”:1},{“imageOffset”:8043,“symbol”:“thread_start”,“symbolLocation”:15,“imageIndex”:1}]},{“id”:10187333,“frames”:[{“imageOffset”:17086,“symbol”:“__semwait_signal”,“symbolLocation”:10,“imageIndex”:0},{“imageOffset”:67683,“symbol”:“nanosleep”,“symbolLocation”:196,“imageIndex”:2},{“imageOffset”:67481,“symbol”:“usleep”,“symbolLocation”:53,“imageIndex”:2},{“imageOffset”:179596,“symbol”:“vtkSlicerApplicationLogic::ProcessNetworkingTasks()”,“symbolLocation”:364,“imageIndex”:10},{“imageOffset”:178374,“symbol”:“vtkSlicerApplicationLogic::NetworkingThreaderCallback(void*)”,“symbolLocation”:38,“imageIndex”:10},{“imageOffset”:25825,“symbol”:“_pthread_start”,“symbolLocation”:125,“imageIndex”:1},{“imageOffset”:8043,“symbol”:“thread_start”,“symbolLocation”:15,“imageIndex”:1}]},{“id”:10187341,“name”:“Qt bearer thread”,“frames”:[{“imageOffset”:32938,“symbol”:“poll”,“symbolLocation”:10,“imageIndex”:0},{“imageOffset”:2470336,“symbol”:“qt_safe_poll(pollfd*, unsigned int, timespec const*)”,“symbolLocation”:608,“imageIndex”:6},{“imageOffset”:2476481,“symbol”:“QEventDispatcherUNIX::processEvents(QFlags<a>QEventLoop::ProcessEventsFlag</a>)”,“symbolLocation”:849,“imageIndex”:6},{“imageOffset”:2050671,“symbol”:“QEventLoop::exec(QFlags<a>QEventLoop::ProcessEventsFlag</a>)”,“symbolLocation”:431,“imageIndex”:6},{“imageOffset”:136531,“symbol”:“QThread::exec()”,“symbolLocation”:131,“imageIndex”:6},{“imageOffset”:140649,“imageIndex”:6},{“imageOffset”:25825,“symbol”:“_pthread_start”,“symbolLocation”:125,“imageIndex”:1},{“imageOffset”:8043,“symbol”:“thread_start”,“symbolLocation”:15,“imageIndex”:1}]},{“id”:10187343,“name”:“ctkFDHandler”,“frames”:[{“imageOffset”:9146,“symbol”:“read”,“symbolLocation”:10,“imageIndex”:0},{“imageOffset”:109073,“symbol”:“ctkFDHandler::run()”,“symbolLocation”:113,“imageIndex”:11},{“imageOffset”:140649,“imageIndex”:6},{“imageOffset”:25825,“symbol”:“_pthread_start”,“symbolLocation”:125,“imageIndex”:1},{“imageOffset”:8043,“symbol”:“thread_start”,“symbolLocation”:15,“imageIndex”:1}]},{“id”:10187344,“name”:“ctkFDHandler”,“frames”:[{“imageOffset”:9146,“symbol”:“read”,“symbolLocation”:10,“imageIndex”:0},{“imageOffset”:109073,“symbol”:“ctkFDHandler::run()”,“symbolLocation”:113,“imageIndex”:11},{“imageOffset”:140649,“imageIndex”:6},{“imageOffset”:25825,“symbol”:“_pthread_start”,“symbolLocation”:125,“imageIndex”:1},{“imageOffset”:8043,“symbol”:“thread_start”,“symbolLocation”:15,“imageIndex”:1}]},{“id”:10187369,“frames”:[{“imageOffset”:8008,“symbol”:“start_wqthread”,“symbolLocation”:0,“imageIndex”:1}]},{“id”:10187373,“name”:“com.apple.NSEventThread”,“frames”:[{“imageOffset”:6522,“symbol”:“mach_msg_trap”,“symbolLocation”:10,“imageIndex”:0},{“imageOffset”:7400,“symbol”:“mach_msg”,“symbolLocation”:56,“imageIndex”:0},{“imageOffset”:525165,“symbol”:“__CFRunLoopServiceMachPort”,“symbolLocation”:319,“imageIndex”:12},{“imageOffset”:518648,“symbol”:“__CFRunLoopRun”,“symbolLocation”:1276,“imageIndex”:12},{“imageOffset”:515644,“symbol”:“CFRunLoopRunSpecific”,“symbolLocation”:562,“imageIndex”:12},{“imageOffset”:1755598,“symbol”:“_NSEventThread”,“symbolLocation”:132,“imageIndex”:13},{“imageOffset”:25825,“symbol”:“_pthread_start”,“symbolLocation”:125,“imageIndex”:1},{“imageOffset”:8043,“symbol”:“thread_start”,“symbolLocation”:15,“imageIndex”:1}]},{“id”:10187376,“name”:“Thread (pooled)”,“frames”:[{“imageOffset”:17386,“symbol”:“__psynch_cvwait”,“symbolLocation”:10,“imageIndex”:0},{“imageOffset”:27247,“symbol”:“_pthread_cond_wait”,“symbolLocation”:1249,“imageIndex”:1},{“imageOffset”:174591,“imageIndex”:6},{“imageOffset”:173774,“imageIndex”:6},{“imageOffset”:173549,“symbol”:“QWaitCondition::wait(QMutex*, QDeadlineTimer)”,“symbolLocation”:93,“imageIndex”:6},{“imageOffset”:158749,“imageIndex”:6},{“imageOffset”:140649,“imageIndex”:6},{“imageOffset”:25825,“symbol”:“_pthread_start”,“symbolLocation”:125,“imageIndex”:1},{“imageOffset”:8043,“symbol”:“thread_start”,“symbolLocation”:15,“imageIndex”:1}]},{“id”:10187377,“name”:“Thread (pooled)”,“frames”:[{“imageOffset”:17386,“symbol”:“__psynch_cvwait”,“symbolLocation”:10,“imageIndex”:0},{“imageOffset”:27247,“symbol”:“_pthread_cond_wait”,“symbolLocation”:1249,“imageIndex”:1},{“imageOffset”:174591,“imageIndex”:6},{“imageOffset”:173774,“imageIndex”:6},{“imageOffset”:173549,“symbol”:“QWaitCondition::wait(QMutex*, QDeadlineTimer)”,“symbolLocation”:93,“imageIndex”:6},{“imageOffset”:158749,“imageIndex”:6},{“imageOffset”:140649,“imageIndex”:6},{“imageOffset”:25825,“symbol”:“_pthread_start”,“symbolLocation”:125,“imageIndex”:1},{“imageOffset”:8043,“symbol”:“thread_start”,“symbolLocation”:15,“imageIndex”:1}]},{“id”:10187378,“name”:“Thread (pooled)”,“frames”:[{“imageOffset”:17386,“symbol”:“__psynch_cvwait”,“symbolLocation”:10,“imageIndex”:0},{“imageOffset”:27247,“symbol”:“_pthread_cond_wait”,“symbolLocation”:1249,“imageIndex”:1},{“imageOffset”:174591,“imageIndex”:6},{“imageOffset”:173774,“imageIndex”:6},{“imageOffset”:173549,“symbol”:“QWaitCondition::wait(QMutex*, QDeadlineTimer)”,“symbolLocation”:93,“imageIndex”:6},{“imageOffset”:158749,“imageIndex”:6},{“imageOffset”:140649,“imageIndex”:6},{“imageOffset”:25825,“symbol”:“_pthread_start”,“symbolLocation”:125,“imageIndex”:1},{“imageOffset”:8043,“symbol”:“thread_start”,“symbolLocation”:15,“imageIndex”:1}]},{“id”:10187379,“name”:“Thread (pooled)”,“frames”:[{“imageOffset”:17386,“symbol”:“__psynch_cvwait”,“symbolLocation”:10,“imageIndex”:0},{“imageOffset”:27247,“symbol”:“_pthread_cond_wait”,“symbolLocation”:1249,“imageIndex”:1},{“imageOffset”:174591,“imageIndex”:6},{“imageOffset”:173774,“imageIndex”:6},{“imageOffset”:173549,“symbol”:“QWaitCondition::wait(QMutex*, QDeadlineTimer)”,“symbolLocation”:93,“imageIndex”:6},{“imageOffset”:158749,“imageIndex”:6},{“imageOffset”:140649,“imageIndex”:6},{“imageOffset”:25825,“symbol”:“_pthread_start”,“symbolLocation”:125,“imageIndex”:1},{“imageOffset”:8043,“symbol”:“thread_start”,“symbolLocation”:15,“imageIndex”:1}]},{“id”:10187380,“name”:“Thread (pooled)”,“frames”:[{“imageOffset”:17386,“symbol”:“__psynch_cvwait”,“symbolLocation”:10,“imageIndex”:0},{“imageOffset”:27247,“symbol”:“_pthread_cond_wait”,“symbolLocation”:1249,“imageIndex”:1},{“imageOffset”:174591,“imageIndex”:6},{“imageOffset”:173774,“imageIndex”:6},{“imageOffset”:173549,“symbol”:“QWaitCondition::wait(QMutex*, QDeadlineTimer)”,“symbolLocation”:93,“imageIndex”:6},{“imageOffset”:158749,“imageIndex”:6},{“imageOffset”:140649,“imageIndex”:6},{“imageOffset”:25825,“symbol”:“_pthread_start”,“symbolLocation”:125,“imageIndex”:1},{“imageOffset”:8043,“symbol”:“thread_start”,“symbolLocation”:15,“imageIndex”:1}]},{“id”:10187381,“name”:“Thread (pooled)”,“frames”:[{“imageOffset”:17386,“symbol”:“__psynch_cvwait”,“symbolLocation”:10,“imageIndex”:0},{“imageOffset”:27247,“symbol”:“_pthread_cond_wait”,“symbolLocation”:1249,“imageIndex”:1},{“imageOffset”:174591,“imageIndex”:6},{“imageOffset”:173774,“imageIndex”:6},{“imageOffset”:173549,“symbol”:“QWaitCondition::wait(QMutex*, QDeadlineTimer)”,“symbolLocation”:93,“imageIndex”:6},{“imageOffset”:158749,“imageIndex”:6},{“imageOffset”:140649,“imageIndex”:6},{“imageOffset”:25825,“symbol”:“_pthread_start”,“symbolLocation”:125,“imageIndex”:1},{“imageOffset”:8043,“symbol”:“thread_start”,“symbolLocation”:15,“imageIndex”:1}]},{“id”:10187382,“name”:“Thread (pooled)”,“frames”:[{“imageOffset”:17386,“symbol”:“__psynch_cvwait”,“symbolLocation”:10,“imageIndex”:0},{“imageOffset”:27247,“symbol”:“_pthread_cond_wait”,“symbolLocation”:1249,“imageIndex”:1},{“imageOffset”:174591,“imageIndex”:6},{“imageOffset”:173774,“imageIndex”:6},{“imageOffset”:173549,“symbol”:“QWaitCondition::wait(QMutex*, QDeadlineTimer)”,“symbolLocation”:93,“imageIndex”:6},{“imageOffset”:158749,“imageIndex”:6},{“imageOffset”:140649,“imageIndex”:6},{“imageOffset”:25825,“symbol”:“_pthread_start”,“symbolLocation”:125,“imageIndex”:1},{“imageOffset”:8043,“symbol”:“thread_start”,“symbolLocation”:15,“imageIndex”:1}]},{“id”:10187383,“name”:“Thread (pooled)”,“frames”:[{“imageOffset”:17386,“symbol”:“__psynch_cvwait”,“symbolLocation”:10,“imageIndex”:0},{“imageOffset”:27247,“symbol”:“_pthread_cond_wait”,“symbolLocation”:1249,“imageIndex”:1},{“imageOffset”:174591,“imageIndex”:6},{“imageOffset”:173774,“imageIndex”:6},{“imageOffset”:173549,“symbol”:“QWaitCondition::wait(QMutex*, QDeadlineTimer)”,“symbolLocation”:93,“imageIndex”:6},{“imageOffset”:158749,“imageIndex”:6},{“imageOffset”:140649,“imageIndex”:6},{“imageOffset”:25825,“symbol”:“_pthread_start”,“symbolLocation”:125,“imageIndex”:1},{“imageOffset”:8043,“symbol”:“thread_start”,“symbolLocation”:15,“imageIndex”:1}]},{“id”:10187384,“name”:“Thread (pooled)”,“frames”:[{“imageOffset”:17386,“symbol”:“__psynch_cvwait”,“symbolLocation”:10,“imageIndex”:0},{“imageOffset”:27247,“symbol”:“_pthread_cond_wait”,“symbolLocation”:1249,“imageIndex”:1},{“imageOffset”:174591,“imageIndex”:6},{“imageOffset”:173774,“imageIndex”:6},{“imageOffset”:173549,“symbol”:“QWaitCondition::wait(QMutex*, QDeadlineTimer)”,“symbolLocation”:93,“imageIndex”:6},{“imageOffset”:158749,“imageIndex”:6},{“imageOffset”:140649,“imageIndex”:6},{“imageOffset”:25825,“symbol”:“_pthread_start”,“symbolLocation”:125,“imageIndex”:1},{“imageOffset”:8043,“symbol”:“thread_start”,“symbolLocation”:15,“imageIndex”:1}]},{“id”:10187387,“frames”:[{“imageOffset”:17386,“symbol”:“__psynch_cvwait”,“symbolLocation”:10,“imageIndex”:0},{“imageOffset”:27247,“symbol”:“_pthread_cond_wait”,“symbolLocation”:1249,“imageIndex”:1},{“imageOffset”:3381007,“symbol”:“blas_thread_server”,“symbolLocation”:207,“imageIndex”:14},{“imageOffset”:25825,“symbol”:“_pthread_start”,“symbolLocation”:125,“imageIndex”:1},{“imageOffset”:8043,“symbol”:“thread_start”,“symbolLocation”:15,“imageIndex”:1}]},{“id”:10187388,“frames”:[{“imageOffset”:17386,“symbol”:“__psynch_cvwait”,“symbolLocation”:10,“imageIndex”:0},{“imageOffset”:27247,“symbol”:“_pthread_cond_wait”,“symbolLocation”:1249,“imageIndex”:1},{“imageOffset”:3381007,“symbol”:“blas_thread_server”,“symbolLocation”:207,“imageIndex”:14},{“imageOffset”:25825,“symbol”:“_pthread_start”,“symbolLocation”:125,“imageIndex”:1},{“imageOffset”:8043,“symbol”:“thread_start”,“symbolLocation”:15,“imageIndex”:1}]},{“id”:10187389,“frames”:[{“imageOffset”:17386,“symbol”:“__psynch_cvwait”,“symbolLocation”:10,“imageIndex”:0},{“imageOffset”:27247,“symbol”:“_pthread_cond_wait”,“symbolLocation”:1249,“imageIndex”:1},{“imageOffset”:3381007,“symbol”:“blas_thread_server”,“symbolLocation”:207,“imageIndex”:14},{“imageOffset”:25825,“symbol”:“_pthread_start”,“symbolLocation”:125,“imageIndex”:1},{“imageOffset”:8043,“symbol”:“thread_start”,“symbolLocation”:15,“imageIndex”:1}]},{“id”:10187390,“frames”:[{“imageOffset”:17386,“symbol”:“__psynch_cvwait”,“symbolLocation”:10,“imageIndex”:0},{“imageOffset”:27247,“symbol”:“_pthread_cond_wait”,“symbolLocation”:1249,“imageIndex”:1},{“imageOffset”:3381007,“symbol”:“blas_thread_server”,“symbolLocation”:207,“imageIndex”:14},{“imageOffset”:25825,“symbol”:“_pthread_start”,“symbolLocation”:125,“imageIndex”:1},{“imageOffset”:8043,“symbol”:“thread_start”,“symbolLocation”:15,“imageIndex”:1}]},{“id”:10187391,“frames”:[{“imageOffset”:17386,“symbol”:“__psynch_cvwait”,“symbolLocation”:10,“imageIndex”:0},{“imageOffset”:27247,“symbol”:“_pthread_cond_wait”,“symbolLocation”:1249,“imageIndex”:1},{“imageOffset”:3381007,“symbol”:“blas_thread_server”,“symbolLocation”:207,“imageIndex”:14},{“imageOffset”:25825,“symbol”:“_pthread_start”,“symbolLocation”:125,“imageIndex”:1},{“imageOffset”:8043,“symbol”:“thread_start”,“symbolLocation”:15,“imageIndex”:1}]},{“id”:10187392,“frames”:[{“imageOffset”:17386,“symbol”:“__psynch_cvwait”,“symbolLocation”:10,“imageIndex”:0},{“imageOffset”:27247,“symbol”:“_pthread_cond_wait”,“symbolLocation”:1249,“imageIndex”:1},{“imageOffset”:3381007,“symbol”:“blas_thread_server”,“symbolLocation”:207,“imageIndex”:14},{“imageOffset”:25825,“symbol”:“_pthread_start”,“symbolLocation”:125,“imageIndex”:1},{“imageOffset”:8043,“symbol”:“thread_start”,“symbolLocation”:15,“imageIndex”:1}]},{“id”:10187393,“frames”:[{“imageOffset”:17386,“symbol”:“__psynch_cvwait”,“symbolLocation”:10,“imageIndex”:0},{“imageOffset”:27247,“symbol”:“_pthread_cond_wait”,“symbolLocation”:1249,“imageIndex”:1},{“imageOffset”:3381007,“symbol”:“blas_thread_server”,“symbolLocation”:207,“imageIndex”:14},{“imageOffset”:25825,“symbol”:“_pthread_start”,“symbolLocation”:125,“imageIndex”:1},{“imageOffset”:8043,“symbol”:“thread_start”,“symbolLocation”:15,“imageIndex”:1}]},{“id”:10187429,“name”:“Thread (pooled)”,“frames”:[{“imageOffset”:17386,“symbol”:“__psynch_cvwait”,“symbolLocation”:10,“imageIndex”:0},{“imageOffset”:27247,“symbol”:“_pthread_cond_wait”,“symbolLocation”:1249,“imageIndex”:1},{“imageOffset”:174591,“imageIndex”:6},{“imageOffset”:173774,“imageIndex”:6},{“imageOffset”:173549,“symbol”:“QWaitCondition::wait(QMutex*, QDeadlineTimer)”,“symbolLocation”:93,“imageIndex”:6},{“imageOffset”:158749,“imageIndex”:6},{“imageOffset”:140649,“imageIndex”:6},{“imageOffset”:25825,“symbol”:“_pthread_start”,“symbolLocation”:125,“imageIndex”:1},{“imageOffset”:8043,“symbol”:“thread_start”,“symbolLocation”:15,“imageIndex”:1}]},{“id”:10187430,“name”:“Thread (pooled)”,“frames”:[{“imageOffset”:17386,“symbol”:“__psynch_cvwait”,“symbolLocation”:10,“imageIndex”:0},{“imageOffset”:27247,“symbol”:“_pthread_cond_wait”,“symbolLocation”:1249,“imageIndex”:1},{“imageOffset”:174591,“imageIndex”:6},{“imageOffset”:173774,“imageIndex”:6},{“imageOffset”:173549,“symbol”:“QWaitCondition::wait(QMutex*, QDeadlineTimer)”,“symbolLocation”:93,“imageIndex”:6},{“imageOffset”:158749,“imageIndex”:6},{“imageOffset”:140649,“imageIndex”:6},{“imageOffset”:25825,“symbol”:“_pthread_start”,“symbolLocation”:125,“imageIndex”:1},{“imageOffset”:8043,“symbol”:“thread_start”,“symbolLocation”:15,“imageIndex”:1}]},{“id”:10187431,“name”:“Thread (pooled)”,“frames”:[{“imageOffset”:17386,“symbol”:“__psynch_cvwait”,“symbolLocation”:10,“imageIndex”:0},{“imageOffset”:27247,“symbol”:“_pthread_cond_wait”,“symbolLocation”:1249,“imageIndex”:1},{“imageOffset”:174591,“imageIndex”:6},{“imageOffset”:173774,“imageIndex”:6},{“imageOffset”:173549,“symbol”:“QWaitCondition::wait(QMutex*, QDeadlineTimer)”,“symbolLocation”:93,“imageIndex”:6},{“imageOffset”:158749,“imageIndex”:6},{“imageOffset”:140649,“imageIndex”:6},{“imageOffset”:25825,“symbol”:“_pthread_start”,“symbolLocation”:125,“imageIndex”:1},{“imageOffset”:8043,“symbol”:“thread_start”,“symbolLocation”:15,“imageIndex”:1}]},{“id”:10187432,“frames”:[{“imageOffset”:8008,“symbol”:“start_wqthread”,“symbolLocation”:0,“imageIndex”:1}]},{“id”:10187435,“name”:“AMCP Logging Spool”,“frames”:[{“imageOffset”:6582,“symbol”:“semaphore_wait_trap”,“symbolLocation”:10,“imageIndex”:0},{“imageOffset”:107238,“symbol”:“caulk::mach::semaphore::wait_or_error()”,“symbolLocation”:16,“imageIndex”:15},{“imageOffset”:8520,“symbol”:“caulk::concurrent::details::worker_thread::run()”,“symbolLocation”:36,“imageIndex”:15},{“imageOffset”:7692,“symbol”:“void* caulk::thread_proxy&lt;std::__1::tuple&lt;caulk:<img src="https://emoji.discourse-cdn.com/twitter/thread.png?v=15" title=":thread:" class="emoji" alt=":thread:" loading="lazy" width="20" height="20">:attributes, void (caulk::concurrent::details::worker_thread::<em>)(), std::__1::tuple<a>caulk::concurrent::details::worker_thread*</a> &gt; &gt;(void</em>)”,“symbolLocation”:41,“imageIndex”:15},{“imageOffset”:25825,“symbol”:“_pthread_start”,“symbolLocation”:125,“imageIndex”:1},{“imageOffset”:8043,“symbol”:“thread_start”,“symbolLocation”:15,“imageIndex”:1}]},{“id”:10187469,“name”:“QFileInfoGatherer”,“frames”:[{“imageOffset”:17386,“symbol”:“__psynch_cvwait”,“symbolLocation”:10,“imageIndex”:0},{“imageOffset”:27247,“symbol”:“_pthread_cond_wait”,“symbolLocation”:1249,“imageIndex”:1},{“imageOffset”:173739,“imageIndex”:6},{“imageOffset”:173549,“symbol”:“QWaitCondition::wait(QMutex*, QDeadlineTimer)”,“symbolLocation”:93,“imageIndex”:6},{“imageOffset”:2362504,“imageIndex”:16},{“imageOffset”:140649,“imageIndex”:6},{“imageOffset”:25825,“symbol”:“_pthread_start”,“symbolLocation”:125,“imageIndex”:1},{“imageOffset”:8043,“symbol”:“thread_start”,“symbolLocation”:15,“imageIndex”:1}]},{“id”:10187470,“name”:“QFileInfoGatherer”,“frames”:[{“imageOffset”:17386,“symbol”:“__psynch_cvwait”,“symbolLocation”:10,“imageIndex”:0},{“imageOffset”:27247,“symbol”:“_pthread_cond_wait”,“symbolLocation”:1249,“imageIndex”:1},{“imageOffset”:173739,“imageIndex”:6},{“imageOffset”:173549,“symbol”:“QWaitCondition::wait(QMutex*, QDeadlineTimer)”,“symbolLocation”:93,“imageIndex”:6},{“imageOffset”:2362504,“imageIndex”:16},{“imageOffset”:140649,“imageIndex”:6},{“imageOffset”:25825,“symbol”:“_pthread_start”,“symbolLocation”:125,“imageIndex”:1},{“imageOffset”:8043,“symbol”:“thread_start”,“symbolLocation”:15,“imageIndex”:1}]}],<br>
“usedImages” : [<br>
{<br>
“source” : “P”,<br>
“arch” : “x86_64”,<br>
“base” : 140703433678848,<br>
“size” : 229376,<br>
“uuid” : “0ea0d8ac-c27b-3a71-a59b-ec3a6f116acf”,<br>
“path” : “/usr/lib/system/libsystem_kernel.dylib”,<br>
“name” : “libsystem_kernel.dylib”<br>
},<br>
{<br>
“source” : “P”,<br>
“arch” : “x86_64”,<br>
“base” : 140703433908224,<br>
“size” : 49152,<br>
“uuid” : “b5454e27-e8c7-3fdb-b77f-714f1e82e70b”,<br>
“path” : “/usr/lib/system/libsystem_pthread.dylib”,<br>
“name” : “libsystem_pthread.dylib”<br>
},<br>
{<br>
“source” : “P”,<br>
“arch” : “x86_64”,<br>
“base” : 140703432663040,<br>
“size” : 561152,<br>
“uuid” : “e42e9d7a-03b4-340b-b61e-dcd45fd4acc0”,<br>
“path” : “/usr/lib/system/libsystem_c.dylib”,<br>
“name” : “libsystem_c.dylib”<br>
},<br>
{<br>
“source” : “P”,<br>
“arch” : “x86_64”,<br>
“base” : 140703431942144,<br>
“size” : 180224,<br>
“uuid” : “47042acd-a337-322a-8db7-ecd59cc60d92”,<br>
“path” : “/usr/lib/system/libsystem_malloc.dylib”,<br>
“name” : “libsystem_malloc.dylib”<br>
},<br>
{<br>
“source” : “P”,<br>
“arch” : “x86_64”,<br>
“base” : 4527235072,<br>
“size” : 2785280,<br>
“uuid” : “9049176e-b3d9-3325-84d9-f6121239ab76”,<br>
“path” : “/Applications/Slicer.app/Contents/lib/Python/lib/libpython3.9.dylib”,<br>
“name” : “libpython3.9.dylib”<br>
},<br>
{<br>
“source” : “P”,<br>
“arch” : “x86_64”,<br>
“base” : 4414001152,<br>
“size” : 9863168,<br>
“uuid” : “60b5ff11-32b7-39bc-9dee-e1196ec1e752”,<br>
“path” : “/Applications/Slicer.app/Contents/lib/Slicer-5.2/libPythonQt.dylib”,<br>
“name” : “libPythonQt.dylib”<br>
},<br>
{<br>
“source” : “P”,<br>
“arch” : “x86_64”,<br>
“base” : 4375638016,<br>
“CFBundleShortVersionString” : “5.15”,<br>
“CFBundleIdentifier” : “org.qt-project.QtCore”,<br>
“size” : 5705728,<br>
“uuid” : “eda847f8-ebac-3db5-80d9-95a0b5e3a870”,<br>
“path” : “/Applications/Slicer.app/Contents/Frameworks/QtCore.framework/Versions/5/QtCore”,<br>
“name” : “QtCore”,<br>
“CFBundleVersion” : “5.15.2”<br>
},<br>
{<br>
“source” : “P”,<br>
“arch” : “x86_64”,<br>
“base” : 4342861824,<br>
“size” : 1069056,<br>
“uuid” : “fcac4dca-409b-3492-b034-f4d291f6a747”,<br>
“path” : “/Applications/Slicer.app/Contents/lib/Slicer-5.2/libqSlicerBaseQTCore.dylib”,<br>
“name” : “libqSlicerBaseQTCore.dylib”<br>
},<br>
{<br>
“source” : “P”,<br>
“arch” : “x86_64”,<br>
“base” : 4325216256,<br>
“CFBundleShortVersionString” : “5.2.1”,<br>
“CFBundleIdentifier” : “org.slicer.slicer”,<br>
“size” : 270336,<br>
“uuid” : “0d378013-ad07-308c-a7b7-b5418f961ffa”,<br>
“path” : “/Applications/Slicer.app/Contents/MacOS/Slicer”,<br>
“name” : “Slicer”,<br>
“CFBundleVersion” : “5.2.1”<br>
},<br>
{<br>
“source” : “P”,<br>
“arch” : “x86_64”,<br>
“base” : 4566708224,<br>
“size” : 442368,<br>
“uuid” : “7b87a986-a153-33c4-8470-d56410b7f9d5”,<br>
“path” : “/usr/lib/dyld”,<br>
“name” : “dyld”<br>
},<br>
{<br>
“source” : “P”,<br>
“arch” : “x86_64”,<br>
“base” : 4349427712,<br>
“size” : 413696,<br>
“uuid” : “1173d1b8-e8b1-364f-82cb-e3171c0d5fa8”,<br>
“path” : “/Applications/Slicer.app/Contents/lib/Slicer-5.2/libSlicerBaseLogic.dylib”,<br>
“name” : “libSlicerBaseLogic.dylib”<br>
},<br>
{<br>
“source” : “P”,<br>
“arch” : “x86_64”,<br>
“base” : 4348932096,<br>
“size” : 278528,<br>
“uuid” : “b2a36c43-b6d7-3a82-b9a1-893deb6b4885”,<br>
“path” : “/Applications/Slicer.app/Contents/lib/Slicer-5.2/libCTKCore.0.1.dylib”,<br>
“name” : “libCTKCore.0.1.dylib”<br>
},<br>
{<br>
“source” : “P”,<br>
“arch” : “x86_64h”,<br>
“base” : 140703434223616,<br>
“CFBundleShortVersionString” : “6.9”,<br>
“CFBundleIdentifier” : “com.apple.CoreFoundation”,<br>
“size” : 5255168,<br>
“uuid” : “93c48919-68af-367e-9a67-db4159bc962c”,<br>
“path” : “/System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation”,<br>
“name” : “CoreFoundation”,<br>
“CFBundleVersion” : “1866”<br>
},<br>
{<br>
“source” : “P”,<br>
“arch” : “x86_64”,<br>
“base” : 140703478759424,<br>
“CFBundleShortVersionString” : “6.9”,<br>
“CFBundleIdentifier” : “com.apple.AppKit”,<br>
“size” : 15269888,<br>
“uuid” : “d2726161-3c3f-3b59-bd8d-4a088d4545ef”,<br>
“path” : “/System/Library/Frameworks/AppKit.framework/Versions/C/AppKit”,<br>
“name” : “AppKit”,<br>
“CFBundleVersion” : “2113.60.148”<br>
},<br>
{<br>
“source” : “P”,<br>
“arch” : “x86_64”,<br>
“base” : 5777891328,<br>
“size” : 63373312,<br>
“uuid” : “ccf8b470-9ccf-3558-9748-04374e88d1ea”,<br>
“path” : “/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages/scipy/.dylibs/libopenblas.0.dylib”,<br>
“name” : “libopenblas.0.dylib”<br>
},<br>
{<br>
“source” : “P”,<br>
“arch” : “x86_64”,<br>
“base” : 140703579578368,<br>
“CFBundleShortVersionString” : “1.0”,<br>
“CFBundleIdentifier” : “com.apple.audio.caulk”,<br>
“size” : 139264,<br>
“uuid” : “8e7b3d95-1d47-3f17-9512-c5fcc30792c2”,<br>
“path” : “/System/Library/PrivateFrameworks/caulk.framework/Versions/A/caulk”,<br>
“name” : “caulk”<br>
},<br>
{<br>
“source” : “P”,<br>
“arch” : “x86_64”,<br>
“base” : 4350316544,<br>
“CFBundleShortVersionString” : “5.15”,<br>
“CFBundleIdentifier” : “org.qt-project.QtWidgets”,<br>
“size” : 4485120,<br>
“uuid” : “6a0c4de6-8a12-31d0-90cb-63e5c78b6c35”,<br>
“path” : “/Applications/Slicer.app/Contents/Frameworks/QtWidgets.framework/Versions/5/QtWidgets”,<br>
“name” : “QtWidgets”,<br>
“CFBundleVersion” : “5.15.2”<br>
}<br>
],<br>
“sharedCache” : {<br>
“base” : 140703430651904,<br>
“size” : 19331678208,<br>
“uuid” : “57de9b7b-39b3-3557-8aed-37ac450fa1f3”<br>
},<br>
“vmSummary” : “ReadOnly portion of Libraries: Total=2.1G resident=0K(0%) swapped_out_or_unallocated=2.1G(100%)\nWritable regions: Total=1.3G written=0K(0%) resident=0K(0%) swapped_out=0K(0%) unallocated=1.3G(100%)\n\n                                VIRTUAL   REGION \nREGION TYPE                        SIZE    COUNT (non-coalesced) \n===========                     =======  ======= \nAccelerate framework               256K        2 \nActivity Tracing                   256K        1 \nCG backing stores                 3840K        4 \nCG image                            24K        1 \nColorSync                          224K       26 \nCoreAnimation                       68K        6 \nCoreGraphics                        12K        2 \nCoreUI image data                  708K        5 \nFoundation                          16K        1 \nKernel Alloc Once                    8K        1 \nMALLOC                           361.2M      208 \nMALLOC guard page                   32K        8 \nMALLOC_LARGE (reserved)            384K        1         reserved VM address space (unallocated)\nMALLOC_NANO (reserved)           384.0M        1         reserved VM address space (unallocated)\nObjC additional data                15K        1 \nSTACK GUARD                       56.1M       33 \nStack                             24.2M       33 \nVM_ALLOCATE                      152.4M      242 \nVM_ALLOCATE (reserved)           384.0M        4         reserved VM address space (unallocated)\n__CTF                               756        1 \n__DATA                            92.4M     1449 \n__DATA_CONST                      32.2M      335 \n__DATA_DIRTY                      1637K      211 \n__FONT_DATA                          4K        1 \n__GLSLBUILTINS                    5176K        1 \n__LINKEDIT                       811.3M      834 \n__TEXT                             1.3G     1353 \n__UNICODE                          592K        1 \ndyld private memory               6144K        3 \nmapped file                      373.2M       28 \nshared memory                      792K       21 \n===========                     =======  ======= \nTOTAL                              3.9G     4818 \nTOTAL, minus reserved VM space     3.1G     4818 \n”,<br>
“legacyInfo” : {<br>
“threadTriggered” : {<br>
“queue” : “com.apple.main-thread”<br>
}<br>
},<br>
“trialInfo” : {<br>
“rollouts” : [<br>
{<br>
“rolloutId” : “61301e3a61217b3110231469”,<br>
“factorPackIds” : {<br>
“SIRI_FIND_MY_CONFIGURATION_FILES” : “6348493aa52bb16adc4e4d06”<br>
},<br>
“deploymentId” : 240000023<br>
},<br>
{<br>
“rolloutId” : “60356660bbe37970735c5624”,<br>
“factorPackIds” : {</p>
<pre><code>  },
  "deploymentId" : 240000027
}
</code></pre>
<p>],<br>
“experiments” : [</p>
<p>]<br>
}<br>
}</p>
<p>Model: MacBookPro15,1, BootROM 1916.40.8.0.0 (iBridge: 20.16.411.0.0,0), 8 processors, 8-Core Intel Core i9, 2.3 GHz, 16 GB, SMC<br>
Graphics: Intel UHD Graphics 630, Intel UHD Graphics 630, Built-In<br>
Graphics: Radeon Pro 560X, Radeon Pro 560X, PCIe, 4 GB<br>
Display: DELL U2718Q, 5120 x 2880 (5K/UHD+ - Ultra High Definition Plus), Main, MirrorOff, Online<br>
Memory Module: BANK 0/ChannelA-DIMM0, 8 GB, DDR4, 2400 MHz, SK Hynix, HMA81GS6AFR8N-UH<br>
Memory Module: BANK 2/ChannelB-DIMM0, 8 GB, DDR4, 2400 MHz, SK Hynix, HMA81GS6AFR8N-UH<br>
AirPort: spairport_wireless_card_type_wifi (0x14E4, 0x7BF), wl0: Jul 12 2021 19:26:30 version 9.30.464.0.32.5.76 FWID 01-45ccefcd<br>
Bluetooth: Version (null), 0 services, 0 devices, 0 incoming serial ports<br>
Network Service: AX88179A, Ethernet, en6<br>
Network Service: Wi-Fi, AirPort, en0<br>
USB Device: USB3.0 Hub<br>
USB Device: AX88179A<br>
USB Device: USB31Bus<br>
USB Device: USB2.0 Hub<br>
USB Device: Cable Matters USB-C Video Cable<br>
USB Device: T2Bus<br>
USB Device: Touch Bar Backlight<br>
USB Device: Touch Bar Display<br>
USB Device: Apple Internal Keyboard / Trackpad<br>
USB Device: Headset<br>
USB Device: Ambient Light Sensor<br>
USB Device: FaceTime HD Camera (Built-in)<br>
USB Device: Apple T2 Controller<br>
Thunderbolt Bus: MacBook Pro, Apple Inc., 47.5<br>
Thunderbolt Bus: MacBook Pro, Apple Inc., 47.5</p>

---

## Post #13 by @lassoan (2022-12-09 19:05 UTC)

<p>Have you installed any extensions?</p>
<p>If yes, try to reinstall Slicer from scratch, then try adding extensions one by one and see which causes the crash.</p>
<p>If it’s just Slicer then see if it is specific to one computer or you can reproduce it on your other mac systems.</p>

---

## Post #14 by @muratmaga (2022-12-09 19:49 UTC)

<p>IGSIO is causing the crash (or rather its update). Before the update, it simply reported a crash after Slicer windows is closed. Now slicer doesn’t start. Removing the IGSIO folder fixes the non-starting problem.</p>

---

## Post #15 by @Sunderlandkyl (2022-12-09 22:04 UTC)

<p>I can reproduce the crash on the Mac in the lab. I’m building a debug version of Slicer now.</p>

---

## Post #16 by @lassoan (2022-12-10 15:29 UTC)

<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> this is a blocking issue for SlicerHeart, too. We should fix it as soon as possible. We may disable VP9 support on macOS until a proper fix can be developed (if the problem indeed comes from VP9).</p>

---

## Post #17 by @Sunderlandkyl (2022-12-10 19:55 UTC)

<p>The crash is not present in my local build. I’ve disabled VP9 in SlicerIGSIO on MacOS by default until we can find a solution.</p>

---
