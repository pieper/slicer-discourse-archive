# Slicer quit unexpectedly on MacBook with M1 chip

**Topic ID**: 25989
**Date**: 2022-10-31
**URL**: https://discourse.slicer.org/t/slicer-quit-unexpectedly-on-macbook-with-m1-chip/25989

---

## Post #1 by @Young_Wang (2022-10-31 19:31 UTC)

<p>I’m not sure if this is an isolated case but ever since I switched to a new laptop(MacBook with M1 chip), I noticed more and more crash whenever I use Slicer.</p>
<p>I attached the full report here if anyone is experiencing the same issue.</p>
<details>
<summary>
Translated Report (Full Report Below)</summary>
<pre><code class="lang-auto">Process:               Slicer [15879]
Path:                  /Applications/Slicer.app/Contents/MacOS/Slicer
Identifier:            org.slicer.slicer
Version:               5.0.3 (5.0.3)
Code Type:             X86-64 (Translated)
Parent Process:        launchd [1]
User ID:               501

Date/Time:             2022-10-31 16:23:40.7377 -0300
OS Version:            macOS 13.0 (22A380)
Report Version:        12
Anonymous UUID:        B624F4FD-D95A-5096-DE94-F54B8E365129

Sleep/Wake UUID:       1A8035CC-83AB-424F-9D69-7161DE5801E1

Time Awake Since Boot: 65000 seconds
Time Since Wake:       8859 seconds

System Integrity Protection: enabled

Notes:
dyld_process_snapshot_create_for_process failed with 5

Crashed Thread:        0  Dispatch queue: com.apple.main-thread

Exception Type:        EXC_BAD_ACCESS (SIGSEGV)
Exception Codes:       KERN_INVALID_ADDRESS at 0x0070006d00690040 -&gt; 0x0000006d00690040 (possible pointer authentication failure)
Exception Codes:       0x0000000000000001, 0x0070006d00690040

Termination Reason:    Namespace SIGNAL, Code 11 Segmentation fault: 11
Terminating Process:   exc handler [15879]

VM Region Info: 0x6d00690040 is in 0x1000000000-0x7000000000;  bytes after start: 399438839872  bytes before end: 12878020543
      REGION TYPE                    START - END         [ VSIZE] PRT/MAX SHRMOD  REGION DETAIL
      commpage (reserved)         fc0000000-1000000000   [  1.0G] ---/--- SM=NUL  ...(unallocated)
---&gt;  GPU Carveout (reserved)    1000000000-7000000000   [384.0G] ---/--- SM=NUL  ...(unallocated)
      GAP OF 0x5f9000000000 BYTES
      MALLOC_NANO              600000000000-600008000000 [128.0M] rw-/rwx SM=PRV  

Error Formulating Crash Report:
dyld_process_snapshot_create_for_process failed with 5

Thread 0 Crashed::  Dispatch queue: com.apple.main-thread
0   libvtkIGSIOCodecs.dylib       	       0x182498b75 vpx_codec_destroy + 37
1   libvtkIGSIOCodecs.dylib       	       0x18249569d vtkVP9VolumeCodec::vtkInternal::~vtkInternal() + 29
2   libvtkIGSIOCodecs.dylib       	       0x18249578e vtkVP9VolumeCodec::vtkInternal::~vtkInternal() + 14
3   libvtkIGSIOCodecs.dylib       	       0x182491b05 vtkVP9VolumeCodec::~vtkVP9VolumeCodec() + 37
4   libvtkCommon-9.1.1.dylib      	       0x1412e775e vtkSmartPointerBase::~vtkSmartPointerBase() + 30
5   libvtkAddon.dylib             	       0x11101fff8 vtkStreamingVolumeCodecFactory::~vtkStreamingVolumeCodecFactory() + 72
6   libvtkAddon.dylib             	       0x11101fb4b vtkStreamingVolumeCodecFactoryInitialize::~vtkStreamingVolumeCodecFactoryInitialize() + 27
7   libsystem_c.dylib             	    0x7ff81c91dccf __cxa_finalize_ranges + 409
8   libsystem_c.dylib             	    0x7ff81c91dae9 exit + 35
9   libdyld.dylib                 	    0x7ff81ca3e1d3 dyld4::LibSystemHelpers::exit(int) const + 11
10  dyld                          	       0x20119f33a start + 2474

Thread 1:: com.apple.rosetta.exceptionserver
0   runtime                       	    0x7ff7ffdb1750 0x7ff7ffdad000 + 18256
1   runtime                       	    0x7ff7ffdbd66c 0x7ff7ffdad000 + 67180
2   runtime                       	    0x7ff7ffdbf06c 0x7ff7ffdad000 + 73836

Thread 2:: com.apple.NSEventThread
0   ???                           	    0x7ff8abcae9a8 ???
1   libsystem_kernel.dylib        	    0x7ff81c9e86a2 mach_msg2_trap + 10
2   libsystem_kernel.dylib        	    0x7ff81c9f667d mach_msg2_internal + 82
3   libsystem_kernel.dylib        	    0x7ff81c9ef71a mach_msg_overwrite + 723
4   libsystem_kernel.dylib        	    0x7ff81c9e8989 mach_msg + 19
5   CoreFoundation                	    0x7ff81cb0202b __CFRunLoopServiceMachPort + 145
6   CoreFoundation                	    0x7ff81cb00a84 __CFRunLoopRun + 1387
7   CoreFoundation                	    0x7ff81caffe9f CFRunLoopRunSpecific + 560
8   AppKit                        	    0x7ff81fcbd696 _NSEventThread + 132
9   libsystem_pthread.dylib       	    0x7ff81ca27259 _pthread_start + 125
10  libsystem_pthread.dylib       	    0x7ff81ca22c7b thread_start + 15

Thread 3:: caulk.messenger.shared:17
0   ???                           	    0x7ff8abcae9a8 ???
1   libsystem_kernel.dylib        	    0x7ff81c9e861e semaphore_wait_trap + 10
2   caulk                         	    0x7ff8266748f8 caulk::mach::semaphore::wait_or_error() + 16
3   caulk                         	    0x7ff82665a664 caulk::concurrent::details::worker_thread::run() + 36
4   caulk                         	    0x7ff82665a328 void* caulk::thread_proxy&lt;std::__1::tuple&lt;caulk::thread::attributes, void (caulk::concurrent::details::worker_thread::*)(), std::__1::tuple&lt;caulk::concurrent::details::worker_thread*&gt; &gt; &gt;(void*) + 41
5   libsystem_pthread.dylib       	    0x7ff81ca27259 _pthread_start + 125
6   libsystem_pthread.dylib       	    0x7ff81ca22c7b thread_start + 15

Thread 4:: QFileInfoGatherer
0   ???                           	    0x7ff8abcae9a8 ???
1   libsystem_kernel.dylib        	    0x7ff81c9eb1fe __psynch_cvwait + 10
2   libsystem_pthread.dylib       	    0x7ff81ca277e1 _pthread_cond_wait + 1243
3   QtCore                        	       0x10ded06ab 0x10dea6000 + 173739
4   QtCore                        	       0x10ded05ed QWaitCondition::wait(QMutex*, QDeadlineTimer) + 93
5   QtWidgets                     	       0x10b7fbc88 0x10b5bb000 + 2362504
6   QtCore                        	       0x10dec8569 0x10dea6000 + 140649
7   libsystem_pthread.dylib       	    0x7ff81ca27259 _pthread_start + 125
8   libsystem_pthread.dylib       	    0x7ff81ca22c7b thread_start + 15

Thread 5:: QFileInfoGatherer
0   ???                           	    0x7ff8abcae9a8 ???
1   libsystem_kernel.dylib        	    0x7ff81c9eb1fe __psynch_cvwait + 10
2   libsystem_pthread.dylib       	    0x7ff81ca277e1 _pthread_cond_wait + 1243
3   QtCore                        	       0x10ded06ab 0x10dea6000 + 173739
4   QtCore                        	       0x10ded05ed QWaitCondition::wait(QMutex*, QDeadlineTimer) + 93
5   QtWidgets                     	       0x10b7fbc88 0x10b5bb000 + 2362504
6   QtCore                        	       0x10dec8569 0x10dea6000 + 140649
7   libsystem_pthread.dylib       	    0x7ff81ca27259 _pthread_start + 125
8   libsystem_pthread.dylib       	    0x7ff81ca22c7b thread_start + 15

Thread 6:
0   runtime                       	    0x7ff7ffdcf87c 0x7ff7ffdad000 + 141436

Thread 7:
0   runtime                       	    0x7ff7ffdcf87c 0x7ff7ffdad000 + 141436

Thread 8:
0   runtime                       	    0x7ff7ffdcf87c 0x7ff7ffdad000 + 141436

Thread 9:
0   runtime                       	    0x7ff7ffdcf87c 0x7ff7ffdad000 + 141436

Thread 10:
0   runtime                       	    0x7ff7ffdcf87c 0x7ff7ffdad000 + 141436

Thread 11:
0   runtime                       	    0x7ff7ffdcf87c 0x7ff7ffdad000 + 141436

Thread 12:
0   runtime                       	    0x7ff7ffdcf87c 0x7ff7ffdad000 + 141436

Thread 13:
0   runtime                       	    0x7ff7ffdcf87c 0x7ff7ffdad000 + 141436

Thread 14:
0   runtime                       	    0x7ff7ffdcf87c 0x7ff7ffdad000 + 141436

Thread 15:
0   runtime                       	    0x7ff7ffdcf87c 0x7ff7ffdad000 + 141436

Thread 16:
0   runtime                       	    0x7ff7ffdcf87c 0x7ff7ffdad000 + 141436

Thread 17:
0   runtime                       	    0x7ff7ffdcf87c 0x7ff7ffdad000 + 141436

Thread 18:
0   runtime                       	    0x7ff7ffdcf87c 0x7ff7ffdad000 + 141436

Thread 19:
0   runtime                       	    0x7ff7ffdcf87c 0x7ff7ffdad000 + 141436

Thread 20:
0   runtime                       	    0x7ff7ffdcf87c 0x7ff7ffdad000 + 141436

Thread 21:
0   runtime                       	    0x7ff7ffdcf87c 0x7ff7ffdad000 + 141436

Thread 22:
0   runtime                       	    0x7ff7ffdcf87c 0x7ff7ffdad000 + 141436


Thread 0 crashed with X86 Thread State (64-bit):
  rax: 0x0000000000000001  rbx: 0x00007fa7c3646720  rcx: 0x0070006d00690020  rdx: 0x0000000000000000
  rdi: 0x0046007300650073  rsi: 0x0000000000000000  rbp: 0x000000030618a770  rsp: 0x000000030618a760
   r8: 0x00007fa808066400   r9: 0x0000000000000006  r10: 0x00007ff86006c4a0  r11: 0x0000600000fb2834
  r12: 0xfffffffffffffff0  r13: 0x00000000000000c0  r14: 0x0000600002eb1ef0  r15: 0x0000600000f09b30
  rip: &lt;unavailable&gt;       rfl: 0x0000000000000202
 tmp0: 0x0000000182634010 tmp1: 0x0000000182491b05 tmp2: 0x000000018249569d


Binary Images:
       0x182478000 -        0x1825f1fff libvtkIGSIOCodecs.dylib (*) &lt;47a44e65-3b50-3dc7-b5c7-e62d0e563e81&gt; /Applications/Slicer.app/Contents/Extensions-30893/SlicerIGSIO/lib/Slicer-5.0/libvtkIGSIOCodecs.dylib
       0x140977000 -        0x141513fff libvtkCommon-9.1.1.dylib (*) &lt;6cf01138-25fc-3fbd-afcc-adc41b0bc36a&gt; /Applications/Slicer.app/Contents/lib/Slicer-5.0/libvtkCommon-9.1.1.dylib
       0x110fb8000 -        0x11102bfff libvtkAddon.dylib (*) &lt;6ecdb57e-c541-3a2e-9663-ab84db139b38&gt; /Applications/Slicer.app/Contents/lib/Slicer-5.0/libvtkAddon.dylib
    0x7ff81c8ef000 -     0x7ff81c977fff libsystem_c.dylib (*) &lt;5efaf10b-2ec1-32ed-b077-80125e552c8d&gt; /usr/lib/system/libsystem_c.dylib
    0x7ff81ca2d000 -     0x7ff81ca4dfff libdyld.dylib (*) &lt;6c8b449a-78f4-3127-bc23-910719de96ab&gt; /usr/lib/system/libdyld.dylib
       0x201199000 -        0x201230fff dyld (*) &lt;0f050705-2258-3d40-b7bc-f3b35a44bbea&gt; /usr/lib/dyld
    0x7ff7ffdad000 -     0x7ff7ffddcfff runtime (*) &lt;6f797d84-b330-3656-9a0d-7b3dbd3f8a07&gt; /usr/libexec/rosetta/runtime
               0x0 - 0xffffffffffffffff ??? (*) &lt;00000000-0000-0000-0000-000000000000&gt; ???
    0x7ff81c9e7000 -     0x7ff81ca20ff7 libsystem_kernel.dylib (*) &lt;0c2fd2c9-777c-3355-b70f-7b1b6e9d1b0b&gt; /usr/lib/system/libsystem_kernel.dylib
    0x7ff81ca83000 -     0x7ff81cf1afff com.apple.CoreFoundation (6.9) &lt;bca7763f-086a-3837-b278-2f8046e4e885&gt; /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
    0x7ff81fb1f000 -     0x7ff820b23ff6 com.apple.AppKit (6.9) &lt;817d572e-eb8c-3999-b7a0-68e1c4b47266&gt; /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
    0x7ff81ca21000 -     0x7ff81ca2cff7 libsystem_pthread.dylib (*) &lt;13b5e252-77d1-31e1-888d-1c5f4426ea87&gt; /usr/lib/system/libsystem_pthread.dylib
    0x7ff826658000 -     0x7ff82667dfff com.apple.audio.caulk (1.0) &lt;43ed8c13-59df-3c8d-b4d2-aee44e4939b9&gt; /System/Library/PrivateFrameworks/caulk.framework/Versions/A/caulk
       0x10dea6000 -        0x10e416fff org.qt-project.QtCore (5.15) &lt;eda847f8-ebac-3db5-80d9-95a0b5e3a870&gt; /Applications/Slicer.app/Contents/Frameworks/QtCore.framework/Versions/5/QtCore
       0x10b5bb000 -        0x10ba01fff org.qt-project.QtWidgets (5.15) &lt;6a0c4de6-8a12-31d0-90cb-63e5c78b6c35&gt; /Applications/Slicer.app/Contents/Frameworks/QtWidgets.framework/Versions/5/QtWidgets

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


-----------
Full Report
-----------

{"app_name":"Slicer","timestamp":"2022-10-31 16:23:50.00 -0300","app_version":"5.0.3","slice_uuid":"c18d93c3-415c-33bd-976c-0644209bc8c7","build_version":"5.0.3","platform":1,"bundleID":"org.slicer.slicer","share_with_app_devs":1,"is_first_party":0,"bug_type":"309","os_version":"macOS 13.0 (22A380)","roots_installed":0,"name":"Slicer","incident_id":"CD82087D-9617-4E61-9C3D-A0A8EB5CF665"}
{
  "uptime" : 65000,
  "procRole" : "Background",
  "version" : 2,
  "userID" : 501,
  "deployVersion" : 210,
  "modelCode" : "MacBookPro18,3",
  "coalitionID" : 4181,
  "osVersion" : {
    "train" : "macOS 13.0",
    "build" : "22A380",
    "releaseType" : "User"
  },
  "captureTime" : "2022-10-31 16:23:40.7377 -0300",
  "incident" : "CD82087D-9617-4E61-9C3D-A0A8EB5CF665",
  "pid" : 15879,
  "translated" : true,
  "cpuType" : "X86-64",
  "roots_installed" : 0,
  "bug_type" : "309",
  "procLaunch" : "2022-10-31 10:16:33.3749 -0300",
  "procStartAbsTime" : 1134204452461,
  "procExitAbsTime" : 1569154049128,
  "procName" : "Slicer",
  "procPath" : "\/Applications\/Slicer.app\/Contents\/MacOS\/Slicer",
  "bundleInfo" : {"CFBundleShortVersionString":"5.0.3","CFBundleVersion":"5.0.3","CFBundleIdentifier":"org.slicer.slicer"},
  "storeInfo" : {"deviceIdentifierForVendor":"5250FA91-9D78-5FB1-A93D-FA7CFF5B36A5","thirdParty":true},
  "parentProc" : "launchd",
  "parentPid" : 1,
  "coalitionName" : "org.slicer.slicer",
  "crashReporterKey" : "B624F4FD-D95A-5096-DE94-F54B8E365129",
  "wakeTime" : 8859,
  "sleepWakeUUID" : "1A8035CC-83AB-424F-9D69-7161DE5801E1",
  "sip" : "enabled",
  "vmRegionInfo" : "0x6d00690040 is in 0x1000000000-0x7000000000;  bytes after start: 399438839872  bytes before end: 12878020543\n      REGION TYPE                    START - END         [ VSIZE] PRT\/MAX SHRMOD  REGION DETAIL\n      commpage (reserved)         fc0000000-1000000000   [  1.0G] ---\/--- SM=NUL  ...(unallocated)\n---&gt;  GPU Carveout (reserved)    1000000000-7000000000   [384.0G] ---\/--- SM=NUL  ...(unallocated)\n      GAP OF 0x5f9000000000 BYTES\n      MALLOC_NANO              600000000000-600008000000 [128.0M] rw-\/rwx SM=PRV  ",
  "exception" : {"codes":"0x0000000000000001, 0x0070006d00690040","rawCodes":[1,31525665549910080],"type":"EXC_BAD_ACCESS","signal":"SIGSEGV","subtype":"KERN_INVALID_ADDRESS at 0x0070006d00690040 -&gt; 0x0000006d00690040 (possible pointer authentication failure)"},
  "termination" : {"flags":0,"code":11,"namespace":"SIGNAL","indicator":"Segmentation fault: 11","byProc":"exc handler","byPid":15879},
  "vmregioninfo" : "0x6d00690040 is in 0x1000000000-0x7000000000;  bytes after start: 399438839872  bytes before end: 12878020543\n      REGION TYPE                    START - END         [ VSIZE] PRT\/MAX SHRMOD  REGION DETAIL\n      commpage (reserved)         fc0000000-1000000000   [  1.0G] ---\/--- SM=NUL  ...(unallocated)\n---&gt;  GPU Carveout (reserved)    1000000000-7000000000   [384.0G] ---\/--- SM=NUL  ...(unallocated)\n      GAP OF 0x5f9000000000 BYTES\n      MALLOC_NANO              600000000000-600008000000 [128.0M] rw-\/rwx SM=PRV  ",
  "extMods" : {"caller":{"thread_create":0,"thread_set_state":0,"task_for_pid":0},"system":{"thread_create":0,"thread_set_state":0,"task_for_pid":0},"targeted":{"thread_create":0,"thread_set_state":0,"task_for_pid":0},"warnings":0},
  "faultingThread" : 0,
  "threads" : [{"triggered":true,"id":836486,"threadState":{"flavor":"x86_THREAD_STATE","rbp":{"value":12987180912},"r12":{"value":18446744073709551600},"rosetta":{"tmp2":{"value":6480811677},"tmp1":{"value":6480796421},"tmp0":{"value":6482509840}},"rbx":{"value":140358514403104},"r8":{"value":140359665869824},"r15":{"value":105553132034864},"r10":{"value":140704739673248,"symbolLocation":24,"symbol":"atexit_mutex"},"rdx":{"value":0},"rdi":{"value":19703742297604211},"r9":{"value":6},"r13":{"value":192},"rflags":{"value":514},"rax":{"value":1},"rsp":{"value":12987180896},"r11":{"value":105553132726324},"rcx":{"value":31525665549910048},"r14":{"value":105553165229808},"rsi":{"value":0}},"queue":"com.apple.main-thread","frames":[{"imageOffset":134005,"symbol":"vpx_codec_destroy","symbolLocation":37,"imageIndex":0},{"imageOffset":120477,"symbol":"vtkVP9VolumeCodec::vtkInternal::~vtkInternal()","symbolLocation":29,"imageIndex":0},{"imageOffset":120718,"symbol":"vtkVP9VolumeCodec::vtkInternal::~vtkInternal()","symbolLocation":14,"imageIndex":0},{"imageOffset":105221,"symbol":"vtkVP9VolumeCodec::~vtkVP9VolumeCodec()","symbolLocation":37,"imageIndex":0},{"imageOffset":9897822,"symbol":"vtkSmartPointerBase::~vtkSmartPointerBase()","symbolLocation":30,"imageIndex":1},{"imageOffset":425976,"symbol":"vtkStreamingVolumeCodecFactory::~vtkStreamingVolumeCodecFactory()","symbolLocation":72,"imageIndex":2},{"imageOffset":424779,"symbol":"vtkStreamingVolumeCodecFactoryInitialize::~vtkStreamingVolumeCodecFactoryInitialize()","symbolLocation":27,"imageIndex":2},{"imageOffset":191695,"symbol":"__cxa_finalize_ranges","symbolLocation":409,"imageIndex":3},{"imageOffset":191209,"symbol":"exit","symbolLocation":35,"imageIndex":3},{"imageOffset":70099,"symbol":"dyld4::LibSystemHelpers::exit(int) const","symbolLocation":11,"imageIndex":4},{"imageOffset":25402,"symbol":"start","symbolLocation":2474,"imageIndex":5}]},{"id":836493,"name":"com.apple.rosetta.exceptionserver","frames":[{"imageOffset":18256,"imageIndex":6},{"imageOffset":67180,"imageIndex":6},{"imageOffset":73836,"imageIndex":6}]},{"id":836603,"name":"com.apple.NSEventThread","frames":[{"imageOffset":140706010818984,"imageIndex":7},{"imageOffset":5794,"symbol":"mach_msg2_trap","symbolLocation":10,"imageIndex":8},{"imageOffset":63101,"symbol":"mach_msg2_internal","symbolLocation":82,"imageIndex":8},{"imageOffset":34586,"symbol":"mach_msg_overwrite","symbolLocation":723,"imageIndex":8},{"imageOffset":6537,"symbol":"mach_msg","symbolLocation":19,"imageIndex":8},{"imageOffset":520235,"symbol":"__CFRunLoopServiceMachPort","symbolLocation":145,"imageIndex":9},{"imageOffset":514692,"symbol":"__CFRunLoopRun","symbolLocation":1387,"imageIndex":9},{"imageOffset":511647,"symbol":"CFRunLoopRunSpecific","symbolLocation":560,"imageIndex":9},{"imageOffset":1697430,"symbol":"_NSEventThread","symbolLocation":132,"imageIndex":10},{"imageOffset":25177,"symbol":"_pthread_start","symbolLocation":125,"imageIndex":11},{"imageOffset":7291,"symbol":"thread_start","symbolLocation":15,"imageIndex":11}]},{"id":836645,"name":"caulk.messenger.shared:17","frames":[{"imageOffset":140706010818984,"imageIndex":7},{"imageOffset":5662,"symbol":"semaphore_wait_trap","symbolLocation":10,"imageIndex":8},{"imageOffset":116984,"symbol":"caulk::mach::semaphore::wait_or_error()","symbolLocation":16,"imageIndex":12},{"imageOffset":9828,"symbol":"caulk::concurrent::details::worker_thread::run()","symbolLocation":36,"imageIndex":12},{"imageOffset":9000,"symbol":"void* caulk::thread_proxy&lt;std::__1::tuple&lt;caulk::thread::attributes, void (caulk::concurrent::details::worker_thread::*)(), std::__1::tuple&lt;caulk::concurrent::details::worker_thread*&gt; &gt; &gt;(void*)","symbolLocation":41,"imageIndex":12},{"imageOffset":25177,"symbol":"_pthread_start","symbolLocation":125,"imageIndex":11},{"imageOffset":7291,"symbol":"thread_start","symbolLocation":15,"imageIndex":11}]},{"id":836673,"name":"QFileInfoGatherer","frames":[{"imageOffset":140706010818984,"imageIndex":7},{"imageOffset":16894,"symbol":"__psynch_cvwait","symbolLocation":10,"imageIndex":8},{"imageOffset":26593,"symbol":"_pthread_cond_wait","symbolLocation":1243,"imageIndex":11},{"imageOffset":173739,"imageIndex":13},{"imageOffset":173549,"symbol":"QWaitCondition::wait(QMutex*, QDeadlineTimer)","symbolLocation":93,"imageIndex":13},{"imageOffset":2362504,"imageIndex":14},{"imageOffset":140649,"imageIndex":13},{"imageOffset":25177,"symbol":"_pthread_start","symbolLocation":125,"imageIndex":11},{"imageOffset":7291,"symbol":"thread_start","symbolLocation":15,"imageIndex":11}]},{"id":836674,"name":"QFileInfoGatherer","frames":[{"imageOffset":140706010818984,"imageIndex":7},{"imageOffset":16894,"symbol":"__psynch_cvwait","symbolLocation":10,"imageIndex":8},{"imageOffset":26593,"symbol":"_pthread_cond_wait","symbolLocation":1243,"imageIndex":11},{"imageOffset":173739,"imageIndex":13},{"imageOffset":173549,"symbol":"QWaitCondition::wait(QMutex*, QDeadlineTimer)","symbolLocation":93,"imageIndex":13},{"imageOffset":2362504,"imageIndex":14},{"imageOffset":140649,"imageIndex":13},{"imageOffset":25177,"symbol":"_pthread_start","symbolLocation":125,"imageIndex":11},{"imageOffset":7291,"symbol":"thread_start","symbolLocation":15,"imageIndex":11}]},{"id":1255443,"frames":[{"imageOffset":141436,"imageIndex":6}]},{"id":1255872,"frames":[{"imageOffset":141436,"imageIndex":6}]},{"id":1258490,"frames":[{"imageOffset":141436,"imageIndex":6}]},{"id":1258838,"frames":[{"imageOffset":141436,"imageIndex":6}]},{"id":1259200,"frames":[{"imageOffset":141436,"imageIndex":6}]},{"id":1259201,"frames":[{"imageOffset":141436,"imageIndex":6}]},{"id":1259202,"frames":[{"imageOffset":141436,"imageIndex":6}]},{"id":1259546,"frames":[{"imageOffset":141436,"imageIndex":6}]},{"id":1259547,"frames":[{"imageOffset":141436,"imageIndex":6}]},{"id":1259580,"frames":[{"imageOffset":141436,"imageIndex":6}]},{"id":1259581,"frames":[{"imageOffset":141436,"imageIndex":6}]},{"id":1259582,"frames":[{"imageOffset":141436,"imageIndex":6}]},{"id":1259583,"frames":[{"imageOffset":141436,"imageIndex":6}]},{"id":1259616,"frames":[{"imageOffset":141436,"imageIndex":6}]},{"id":1259617,"frames":[{"imageOffset":141436,"imageIndex":6}]},{"id":1259618,"frames":[{"imageOffset":141436,"imageIndex":6}]},{"id":1259638,"frames":[{"imageOffset":141436,"imageIndex":6}]}],
  "usedImages" : [
  {
    "source" : "P",
    "arch" : "x86_64",
    "base" : 6480691200,
    "size" : 1548288,
    "uuid" : "47a44e65-3b50-3dc7-b5c7-e62d0e563e81",
    "path" : "\/Applications\/Slicer.app\/Contents\/Extensions-30893\/SlicerIGSIO\/lib\/Slicer-5.0\/libvtkIGSIOCodecs.dylib",
    "name" : "libvtkIGSIOCodecs.dylib"
  },
  {
    "source" : "P",
    "arch" : "x86_64",
    "base" : 5378633728,
    "size" : 12177408,
    "uuid" : "6cf01138-25fc-3fbd-afcc-adc41b0bc36a",
    "path" : "\/Applications\/Slicer.app\/Contents\/lib\/Slicer-5.0\/libvtkCommon-9.1.1.dylib",
    "name" : "libvtkCommon-9.1.1.dylib"
  },
  {
    "source" : "P",
    "arch" : "x86_64",
    "base" : 4579885056,
    "size" : 475136,
    "uuid" : "6ecdb57e-c541-3a2e-9663-ab84db139b38",
    "path" : "\/Applications\/Slicer.app\/Contents\/lib\/Slicer-5.0\/libvtkAddon.dylib",
    "name" : "libvtkAddon.dylib"
  },
  {
    "source" : "P",
    "arch" : "x86_64",
    "base" : 140703607746560,
    "size" : 561152,
    "uuid" : "5efaf10b-2ec1-32ed-b077-80125e552c8d",
    "path" : "\/usr\/lib\/system\/libsystem_c.dylib",
    "name" : "libsystem_c.dylib"
  },
  {
    "source" : "P",
    "arch" : "x86_64",
    "base" : 140703609049088,
    "size" : 135168,
    "uuid" : "6c8b449a-78f4-3127-bc23-910719de96ab",
    "path" : "\/usr\/lib\/system\/libdyld.dylib",
    "name" : "libdyld.dylib"
  },
  {
    "source" : "P",
    "arch" : "x86_64",
    "base" : 8608387072,
    "size" : 622592,
    "uuid" : "0f050705-2258-3d40-b7bc-f3b35a44bbea",
    "path" : "\/usr\/lib\/dyld",
    "name" : "dyld"
  },
  {
    "source" : "P",
    "arch" : "arm64",
    "base" : 140703126179840,
    "size" : 196608,
    "uuid" : "6f797d84-b330-3656-9a0d-7b3dbd3f8a07",
    "path" : "\/usr\/libexec\/rosetta\/runtime",
    "name" : "runtime"
  },
  {
    "size" : 0,
    "source" : "A",
    "base" : 0,
    "uuid" : "00000000-0000-0000-0000-000000000000"
  },
  {
    "source" : "P",
    "arch" : "x86_64",
    "base" : 140703608762368,
    "size" : 237560,
    "uuid" : "0c2fd2c9-777c-3355-b70f-7b1b6e9d1b0b",
    "path" : "\/usr\/lib\/system\/libsystem_kernel.dylib",
    "name" : "libsystem_kernel.dylib"
  },
  {
    "source" : "P",
    "arch" : "x86_64",
    "base" : 140703609401344,
    "CFBundleShortVersionString" : "6.9",
    "CFBundleIdentifier" : "com.apple.CoreFoundation",
    "size" : 4816896,
    "uuid" : "bca7763f-086a-3837-b278-2f8046e4e885",
    "path" : "\/System\/Library\/Frameworks\/CoreFoundation.framework\/Versions\/A\/CoreFoundation",
    "name" : "CoreFoundation",
    "CFBundleVersion" : "1953.1"
  },
  {
    "source" : "P",
    "arch" : "x86_64",
    "base" : 140703660371968,
    "CFBundleShortVersionString" : "6.9",
    "CFBundleIdentifier" : "com.apple.AppKit",
    "size" : 16797687,
    "uuid" : "817d572e-eb8c-3999-b7a0-68e1c4b47266",
    "path" : "\/System\/Library\/Frameworks\/AppKit.framework\/Versions\/C\/AppKit",
    "name" : "AppKit",
    "CFBundleVersion" : "2299"
  },
  {
    "source" : "P",
    "arch" : "x86_64",
    "base" : 140703608999936,
    "size" : 49144,
    "uuid" : "13b5e252-77d1-31e1-888d-1c5f4426ea87",
    "path" : "\/usr\/lib\/system\/libsystem_pthread.dylib",
    "name" : "libsystem_pthread.dylib"
  },
  {
    "source" : "P",
    "arch" : "x86_64",
    "base" : 140703772803072,
    "CFBundleShortVersionString" : "1.0",
    "CFBundleIdentifier" : "com.apple.audio.caulk",
    "size" : 155648,
    "uuid" : "43ed8c13-59df-3c8d-b4d2-aee44e4939b9",
    "path" : "\/System\/Library\/PrivateFrameworks\/caulk.framework\/Versions\/A\/caulk",
    "name" : "caulk"
  },
  {
    "source" : "P",
    "arch" : "x86_64",
    "base" : 4528431104,
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
    "arch" : "x86_64",
    "base" : 4485525504,
    "CFBundleShortVersionString" : "5.15",
    "CFBundleIdentifier" : "org.qt-project.QtWidgets",
    "size" : 4485120,
    "uuid" : "6a0c4de6-8a12-31d0-90cb-63e5c78b6c35",
    "path" : "\/Applications\/Slicer.app\/Contents\/Frameworks\/QtWidgets.framework\/Versions\/5\/QtWidgets",
    "name" : "QtWidgets",
    "CFBundleVersion" : "5.15.2"
  }
],
  "legacyInfo" : {
  "threadTriggered" : {
    "queue" : "com.apple.main-thread"
  }
},
  "trialInfo" : {
  "rollouts" : [
    {
      "rolloutId" : "63582c5f8a53461413999550",
      "factorPackIds" : {
        "PROACTIVE_MAIL_INTELLIGENCE_SALIENCY" : "63582cdd892de80b72cc9bde"
      },
      "deploymentId" : 240000001
    },
    {
      "rolloutId" : "610d52e1fc54bc3389840408",
      "factorPackIds" : {
        "SIRI_UNDERSTANDING_ASR_ASSISTANT" : "633387bf700e8d49302bbf98",
        "SIRI_UNDERSTANDING_MORPHUN" : "62ec7220c682040ba94e6a20"
      },
      "deploymentId" : 240000468
    }
  ],
  "experiments" : [

  ]
},
  "reportNotes" : [
  "dyld_process_snapshot_create_for_process failed with 5"
]
}

Model: MacBookPro18,3, BootROM 8419.41.10, proc 8:6:2 processors, 16 GB, SMC 
Graphics: Apple M1 Pro, Apple M1 Pro, Built-In
Display: Color LCD, 3024 x 1964 Retina, Main, MirrorOff, Online
Display: R240HY, 1920 x 1080 (1080p FHD - Full High Definition), MirrorOff, Online
Display: ASUS MG28U, 3840 x 2160 (2160p/4K UHD 1 - Ultra High Definition), MirrorOff, Online
Memory Module: LPDDR5, Samsung
AirPort: spairport_wireless_card_type_wifi (0x14E4, 0x4387), wl0: Sep  3 2022 02:35:52 version 20.10.965.9.8.7.129 FWID 01-b0e84a9b
Bluetooth: Version (null), 0 services, 0 devices, 0 incoming serial ports
Network Service: Wi-Fi, AirPort, en0
USB Device: USB31Bus
USB Device: USB3.0 Hub
USB Device: AX88179A
USB Device: USB3.0-CRW
USB Device: USB2.0 Hub
USB Device: PD3.0 USB-C Device
USB Device: USB31Bus
USB Device: USB31Bus
Thunderbolt Bus: Laptop, Apple Inc.
Thunderbolt Bus: Laptop, Apple Inc.
Thunderbolt Bus: Laptop, Apple Inc.
</code></pre>
</details>

---

## Post #2 by @pieper (2022-10-31 19:36 UTC)

<p>I haven’t tried extensive work with the Apple M series cpus but they seem to work generally fine but then have some odd corner cases where they don’t work quite the same (e.g. <a href="https://github.com/pieper/SlicerParallelProcessing/commit/2cf7d7d61e7b17cc949cb8fd31acefe9e4de25a1">this one</a>.  I suspect Apple may be fixing these behind the scenes.  Eventually we’ll compile Slicer natively and it should work better.</p>
<p>If you have a reproducible way to trigger a crash let us know.</p>

---

## Post #3 by @Young_Wang (2022-11-30 17:25 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a>, thanks for looking into this for me and for the detailed explanation.</p>

---

## Post #4 by @Young_Wang (2022-12-01 13:42 UTC)

<p>hi <a class="mention" href="/u/pieper">@pieper</a>, following our last conversation. I upgraded the slicer to 5.2.1, and I found it after loading a dicom set. Slicer quit unexpectedly during the next launch. I’m happy to contribute to the testing effort if it helps.<br>
And please see the attached file for the error message<br>
<a href="https://dalu-my.sharepoint.com/:w:/g/personal/jn511893_dal_ca/EVMI9Eo1MG9BudaBRY_O4xwBfwwxs3lzbnAGp6PIZKBkeg?e=S2HVWe" rel="noopener nofollow ugc">slicer error message.rtf</a></p>

---

## Post #5 by @pieper (2022-12-02 17:41 UTC)

<p>Thanks for reporting.  It looks like the crash is in this class, which I believe comes from <a href="https://vtkIGSIOCodecs">this extension</a>.  Maybe you can try with that disabled?  Also if there’s a way to replicate the crash with public data that would be helpful for testing.</p>
<p>I hope we’ll have <a href="https://github.com/Slicer/Slicer/issues/6490#issuecomment-1333221178">native packages soon</a>.  If you can live with some limitations it’s also <a href="https://github.com/Slicer/Slicer/issues/5944#issuecomment-1328179343">possible to build from source</a>.</p>
<pre><code class="lang-auto">Thread 0 Crashed:: Dispatch queue: com.apple.main-thread

0 libvtkIGSIOCodecs.dylib 0x1837d3b75 vpx_codec_destroy + 37

1 libvtkIGSIOCodecs.dylib 0x1837d069d vtkVP9VolumeCodec::vtkInternal::~vtkInternal() + 29
</code></pre>

---

## Post #6 by @Young_Wang (2022-12-02 18:31 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> thank you for taking a look at it for me. Somehow this extension link is broken. Could you repost it? And also thanks for putting time into this!</p>
<p>I just used the zeta dataset from the OpenEar library, you can find this dataset <a href="https://zenodo.org/record/1473724#.Y4pC5-zMJBZ" rel="noopener nofollow ugc">here</a>.</p>

---

## Post #7 by @pieper (2022-12-02 18:42 UTC)

<p>Well, 5.2.1 opens for me on my M2 mac.  I started to download the OpenEar data but it says it will take 4 hours.  Is that the only data that crashes?  Maybe you are just running out of memory.</p>
<p>Sorry I mis-pasted.  The repo is <a href="https://github.com/IGSIO/SlicerIGSIO" class="inline-onebox">GitHub - IGSIO/SlicerIGSIO: Utility extension for 3D Slicer, containing tools and algorithms for building image guided surgery applications</a>. Did you try running with this uninstalled?</p>

---

## Post #8 by @Young_Wang (2022-12-02 19:09 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> thanks! I just uninstalled this module but it still crashes. Please see the full report <a href="https://dalu-my.sharepoint.com/:w:/g/personal/jn511893_dal_ca/ESt7tdR1du5NkvvjxueEppgBtKC87Ri3NeY-qpdYgKY0DQ?e=LrPF5h" rel="noopener nofollow ugc">here</a><br>
Also, you can use <a href="https://github.com/MedicalImageAnalysisTutorials/VisSimData/blob/master/P100003_DV_R_a.nrrd" rel="noopener nofollow ugc">dataset</a></p>

---

## Post #9 by @pieper (2022-12-03 15:56 UTC)

<p>The OpenEar data is not downloading for me.  Do you have another way to replicate the issue?</p>

---

## Post #10 by @Young_Wang (2022-12-05 02:35 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> the crash actually happens with loading into any dataset. It crashes during the startup</p>

---

## Post #11 by @pieper (2022-12-05 20:50 UTC)

<p>Hmm, that’s not happening for me on the M2 mac.  Maybe try deleting your Settings file:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/settings.html#settings-file-location" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/settings.html#settings-file-location</a></p>
<p>If you are still having trouble maybe others with similar hardware/software can comment.</p>

---

## Post #12 by @Young_Wang (2022-12-07 13:17 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> thanks. It seems to fix this issue.</p>

---

## Post #13 by @MR_MUHAMMAD_SIDDIQUI (2023-06-16 16:16 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d8813e2dc526a580493c5e8aca363379d05fb15f.png" data-download-href="/uploads/short-url/uTi2boCttMV09RLpEGaecv8VLfF.png?dl=1" title="Screen Shot 2023-06-16 at 9.10.47 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d8813e2dc526a580493c5e8aca363379d05fb15f_2_412x500.png" alt="Screen Shot 2023-06-16 at 9.10.47 PM" data-base62-sha1="uTi2boCttMV09RLpEGaecv8VLfF" width="412" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d8813e2dc526a580493c5e8aca363379d05fb15f_2_412x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d8813e2dc526a580493c5e8aca363379d05fb15f.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d8813e2dc526a580493c5e8aca363379d05fb15f.png 2x" data-dominant-color="3D4046"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2023-06-16 at 9.10.47 PM</span><span class="informations">541×656 62.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
I just installed 3d slicer today and i cant see to open it. im just getting this message every time i try to open it. I have a macbook pro M1 pro chip running on mac os monterey. Would really appreciate soe assistance.</p>

---

## Post #14 by @MR_MUHAMMAD_SIDDIQUI (2023-06-16 18:16 UTC)

<p>I just installed 3d slicer today and i cant seem to open it. im just getting this message every time i try to open it. I have a macbook pro M1 pro chip running on mac os monterey. Would really appreciate soe assistance.</p>
<p>Operating system:<br>
Slicer version:<br>
Expected behavior:<br>
Actual behavior:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d8813e2dc526a580493c5e8aca363379d05fb15f.png" data-download-href="/uploads/short-url/uTi2boCttMV09RLpEGaecv8VLfF.png?dl=1" title="Screen Shot 2023-06-16 at 9.10.47 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d8813e2dc526a580493c5e8aca363379d05fb15f_2_412x500.png" alt="Screen Shot 2023-06-16 at 9.10.47 PM" data-base62-sha1="uTi2boCttMV09RLpEGaecv8VLfF" width="412" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d8813e2dc526a580493c5e8aca363379d05fb15f_2_412x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d8813e2dc526a580493c5e8aca363379d05fb15f.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d8813e2dc526a580493c5e8aca363379d05fb15f.png 2x" data-dominant-color="3D4046"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2023-06-16 at 9.10.47 PM</span><span class="informations">541×656 62.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #15 by @lassoan (2023-06-16 19:01 UTC)

<p>What Slicer version are you using?</p>
<p>Have you installed any extensions?</p>
<p>Do you use Rosetta or Rosetta2? (see <a href="https://discourse.slicer.org/t/mac-stable-5-2-1-reports-a-crash-everytime-it-is-closed/26586" class="inline-onebox">Mac Stable (5.2.1.) reports a crash everytime it is closed</a>)</p>

---

## Post #16 by @pieper (2023-06-17 16:24 UTC)

<p>For me, Slicer 5.2.2 runs fine on Mac OS 13.1 Ventura on an M2 mac book air.  Perhaps you need to upgrade your OS.</p>

---
