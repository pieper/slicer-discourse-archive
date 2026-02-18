# Crash reporting

**Topic ID**: 28269
**Date**: 2023-03-10
**URL**: https://discourse.slicer.org/t/crash-reporting/28269

---

## Post #1 by @zyy (2023-03-10 02:23 UTC)

<pre><code class="lang-auto">-------------------------------------
Translated Report (Full Report Below)
-------------------------------------

Process:               Slicer [32381]
Path:                  /Applications/Slicer.app/Contents/MacOS/Slicer
Identifier:            org.slicer.slicer
Version:               5.2.2 (5.2.2)
Code Type:             X86-64 (Native)
Parent Process:        launchd [1]
User ID:               501

Date/Time:             2023-03-10 10:20:14.8226 +0800
OS Version:            macOS 13.2.1 (22D68)
Report Version:        12
Anonymous UUID:        24035B9F-6F92-A8A7-F37B-FF7BB60EC79B

Sleep/Wake UUID:       BA78C671-E910-41E0-B5FF-21916A6A5FE9

Time Awake Since Boot: 120000 seconds
Time Since Wake:       3161 seconds

System Integrity Protection: disabled

Crashed Thread:        0  Dispatch queue: com.apple.main-thread

Exception Type:        EXC_BAD_ACCESS (SIGSEGV)
Exception Codes:       KERN_INVALID_ADDRESS at 0x000000090bfc9000
Exception Codes:       0x0000000000000001, 0x000000090bfc9000

Termination Reason:    Namespace SIGNAL, Code 11 Segmentation fault: 11
Terminating Process:   exc handler [32381]

VM Region Info: 0x90bfc9000 is not in any region.  Bytes after previous region: 32539185153  Bytes before following region: 105514260459520
      REGION TYPE                    START - END         [ VSIZE] PRT/MAX SHRMOD  REGION DETAIL
      mapped file                 1787d9000-178800000    [  156K] r--/r-- SM=ALI  ...t_id=a84f6d3d
---&gt;  GAP OF 0x5ffe87800000 BYTES
      MALLOC_NANO              600000000000-600008000000 [128.0M] rw-/rwx SM=PRV  

Thread 0 Crashed::  Dispatch queue: com.apple.main-thread
0   dyld                          	    0x7ff80b893ce4 lsl::AllocationMetadata::freeObject() + 88
1   dyld                          	    0x7ff80b8a42cb lsl::UniquePtr&lt;dyld4::Atlas::Image&gt;::~UniquePtr() + 59
2   dyld                          	    0x7ff80b87b807 lsl::BTree&lt;lsl::UniquePtr&lt;dyld4::Atlas::Image&gt;, std::__1::less&lt;lsl::UniquePtr&lt;dyld4::Atlas::Image&gt; &gt;, false&gt;::NodeCore&lt;31u, 15u&gt;::deallocateChildren() + 101
3   dyld                          	    0x7ff80b87b7d3 lsl::BTree&lt;lsl::UniquePtr&lt;dyld4::Atlas::Image&gt;, std::__1::less&lt;lsl::UniquePtr&lt;dyld4::Atlas::Image&gt; &gt;, false&gt;::NodeCore&lt;31u, 15u&gt;::deallocateChildren() + 49
4   dyld                          	    0x7ff80b87b7d3 lsl::BTree&lt;lsl::UniquePtr&lt;dyld4::Atlas::Image&gt;, std::__1::less&lt;lsl::UniquePtr&lt;dyld4::Atlas::Image&gt; &gt;, false&gt;::NodeCore&lt;31u, 15u&gt;::deallocateChildren() + 49
5   dyld                          	    0x7ff80b87b764 lsl::BTree&lt;lsl::UniquePtr&lt;dyld4::Atlas::Image&gt;, std::__1::less&lt;lsl::UniquePtr&lt;dyld4::Atlas::Image&gt; &gt;, false&gt;::clear() + 22
6   dyld                          	    0x7ff80b87b28d dyld4::RuntimeState::freeProcessSnapshot() + 61
7   dyld                          	    0x7ff80b876c76 dyld4::RuntimeState::decDlRefCount(dyld4::Loader const*) + 254
8   dyld                          	    0x7ff80b89ea90 dyld4::APIs::dlclose(void*) + 208
9   QtCore                        	       0x10cda9cc5 0x10cbb7000 + 2043077
10  QtCore                        	       0x10cda4540 0x10cbb7000 + 2020672
11  QtCore                        	       0x10cda722f 0x10cbb7000 + 2032175
12  QtCore                        	       0x10cda3a09 0x10cbb7000 + 2017801
13  libsystem_c.dylib             	    0x7ff80ba96c1f __cxa_finalize_ranges + 409
14  libsystem_c.dylib             	    0x7ff80ba96a39 exit + 35
15  libdyld.dylib                 	    0x7ff80bbb71d3 dyld4::LibSystemHelpers::exit(int) const + 11
16  dyld                          	    0x7ff80b86d33a start + 2474

Thread 1:: com.apple.NSEventThread
0   libsystem_kernel.dylib        	    0x7ff80bb615c2 mach_msg2_trap + 10
1   libsystem_kernel.dylib        	    0x7ff80bb6f604 mach_msg2_internal + 82
2   libsystem_kernel.dylib        	    0x7ff80bb68635 mach_msg_overwrite + 723
3   libsystem_kernel.dylib        	    0x7ff80bb618a8 mach_msg + 19
4   CoreFoundation                	    0x7ff80bc7bcbe __CFRunLoopServiceMachPort + 145
5   CoreFoundation                	    0x7ff80bc7a72a __CFRunLoopRun + 1360
6   CoreFoundation                	    0x7ff80bc79b60 CFRunLoopRunSpecific + 560
7   AppKit                        	    0x7ff80ef2b179 _NSEventThread + 132
8   libsystem_pthread.dylib       	    0x7ff80bba0259 _pthread_start + 125
9   libsystem_pthread.dylib       	    0x7ff80bb9bc7b thread_start + 15

Thread 2:: QFileInfoGatherer
0   libsystem_kernel.dylib        	    0x7ff80bb6411a __psynch_cvwait + 10
1   libsystem_pthread.dylib       	    0x7ff80bba07e1 _pthread_cond_wait + 1243
2   QtCore                        	       0x10cbe16ab 0x10cbb7000 + 173739
3   QtCore                        	       0x10cbe15ed QWaitCondition::wait(QMutex*, QDeadlineTimer) + 93
4   QtWidgets                     	       0x10b5d1c88 0x10b391000 + 2362504
5   QtCore                        	       0x10cbd9569 0x10cbb7000 + 140649
6   libsystem_pthread.dylib       	    0x7ff80bba0259 _pthread_start + 125
7   libsystem_pthread.dylib       	    0x7ff80bb9bc7b thread_start + 15

Thread 3:: QFileInfoGatherer
0   libsystem_kernel.dylib        	    0x7ff80bb6411a __psynch_cvwait + 10
1   libsystem_pthread.dylib       	    0x7ff80bba07e1 _pthread_cond_wait + 1243
2   QtCore                        	       0x10cbe16ab 0x10cbb7000 + 173739
3   QtCore                        	       0x10cbe15ed QWaitCondition::wait(QMutex*, QDeadlineTimer) + 93
4   QtWidgets                     	       0x10b5d1c88 0x10b391000 + 2362504
5   QtCore                        	       0x10cbd9569 0x10cbb7000 + 140649
6   libsystem_pthread.dylib       	    0x7ff80bba0259 _pthread_start + 125
7   libsystem_pthread.dylib       	    0x7ff80bb9bc7b thread_start + 15

Thread 4:
0   libsystem_pthread.dylib       	    0x7ff80bb9bc58 start_wqthread + 0

Thread 5:
0   libsystem_pthread.dylib       	    0x7ff80bb9bc58 start_wqthread + 0

Thread 6:
0   libsystem_pthread.dylib       	    0x7ff80bb9bc58 start_wqthread + 0

Thread 7:
0   libsystem_pthread.dylib       	    0x7ff80bb9bc58 start_wqthread + 0


Thread 0 crashed with X86 Thread State (64-bit):
  rax: 0x0000000000000010  rbx: 0x000000012284cdc8  rcx: 0x00007ff80b8ea104  rdx: 0x0000000000000010
  rdi: 0x000000090bfc9000  rsi: 0x0000000173aa0e00  rbp: 0x00007ff7b62ee510  rsp: 0x00007ff7b62ee510
   r8: 0x0000000000000002   r9: 0x0000000000000000  r10: 0x00000001773ae800  r11: 0x0000000173aa0502
  r12: 0x0000000109c7afb0  r13: 0x00007ff90241dfb0  r14: 0x000000012284cdb0  r15: 0x0000000000000007
  rip: 0x00007ff80b893ce4  rfl: 0x0000000000010202  cr2: 0x000000090bfc9000
  
Logical CPU:     4
Error Code:      0x00000004 (no mapping for user data read)
Trap Number:     14

Thread 0 instruction stream:
  89 e5 48 8d 47 f0 5d c3-55 48 89 e5 48 89 fe 48  ..H.G.].UH..H..H
  8b 17 48 8d 0c d5 00 00-00 00 48 bf f8 ff ff ff  ..H.......H.....
  ff ff 0f 00 48 21 cf 48-89 d0 48 c1 e8 31 25 ff  ....H!.H..H..1%.
  07 00 00 48 c1 ea 3c 83-e2 03 48 8d 0d ab 64 05  ...H..&lt;...H...d.
  00 8a 0c 0a 48 d3 e0 48-83 c0 10 48 83 f8 11 ba  ....H..H...H....
  10 00 00 00 48 0f 43 d0-48 83 c2 0f 48 83 e2 f0  ....H.C.H...H...
 [48]8b 07 48 8b 40 40 5d-ff e0 48 85 f6 74 64 55  H..H.@@]..H..tdU	&lt;==
  48 89 e5 48 8b 56 f0 48-83 c6 f0 48 8d 0c d5 00  H..H.V.H...H....
  00 00 00 48 bf f8 ff ff-ff ff ff 0f 00 48 21 cf  ...H.........H!.
  48 89 d0 48 c1 e8 31 25-ff 07 00 00 48 c1 ea 3c  H..H..1%....H..&lt;
  83 e2 03 48 8d 0d 42 64-05 00 8a 0c 0a 48 d3 e0  ...H..Bd.....H..
  48 83 c0 10 48 83 f8 11-ba 10 00 00 00 48 0f 43  H...H........H.C

Binary Images:
    0x7ff80b867000 -     0x7ff80b8fbcaf dyld (*) &lt;bba77709-6cad-3592-ab03-09d0f7b8610e&gt; /usr/lib/dyld
       0x10cbb7000 -        0x10d127fff org.qt-project.QtCore (5.15) &lt;eda847f8-ebac-3db5-80d9-95a0b5e3a870&gt; /Applications/Slicer.app/Contents/Frameworks/QtCore.framework/Versions/5/QtCore
    0x7ff80ba68000 -     0x7ff80baf0fff libsystem_c.dylib (*) &lt;1aec5d1a-6e43-30f9-a9f2-11eb85d3e70c&gt; /usr/lib/system/libsystem_c.dylib
    0x7ff80bba6000 -     0x7ff80bbc6fff libdyld.dylib (*) &lt;45277dd5-20a4-3c50-b361-a6f18c327027&gt; /usr/lib/system/libdyld.dylib
    0x7ff80bb60000 -     0x7ff80bb99ff7 libsystem_kernel.dylib (*) &lt;87ff381c-4d30-3087-bab7-a5a53d232c00&gt; /usr/lib/system/libsystem_kernel.dylib
    0x7ff80bbfc000 -     0x7ff80c095fef com.apple.CoreFoundation (6.9) &lt;c2615780-0140-315c-a455-7e03bb22d3d6&gt; /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
    0x7ff80ed8c000 -     0x7ff80fd94ff2 com.apple.AppKit (6.9) &lt;540cedfd-5a35-3f35-8953-dcb7c4834eb5&gt; /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
    0x7ff80bb9a000 -     0x7ff80bba5ff7 libsystem_pthread.dylib (*) &lt;3bd433d4-15bd-3add-a612-95e4d3b20719&gt; /usr/lib/system/libsystem_pthread.dylib
       0x10b391000 -        0x10b7d7fff org.qt-project.QtWidgets (5.15) &lt;6a0c4de6-8a12-31d0-90cb-63e5c78b6c35&gt; /Applications/Slicer.app/Contents/Frameworks/QtWidgets.framework/Versions/5/QtWidgets
               0x0 - 0xffffffffffffffff ??? (*) &lt;00000000-0000-0000-0000-000000000000&gt; ???

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
ReadOnly portion of Libraries: Total=1.4G resident=0K(0%) swapped_out_or_unallocated=1.4G(100%)
Writable regions: Total=6.0G written=0K(0%) resident=0K(0%) swapped_out=0K(0%) unallocated=6.0G(100%)

                                VIRTUAL   REGION 
REGION TYPE                        SIZE    COUNT (non-coalesced) 
===========                     =======  ======= 
Accelerate framework               128K        1 
Activity Tracing                   256K        1 
CG backing stores                 1920K        8 
CG image                            92K       16 
ColorSync                          240K       27 
CoreAnimation                     1152K       20 
CoreGraphics                        24K        4 
CoreUI image data                  796K       13 
Foundation                          16K        1 
Kernel Alloc Once                    8K        1 
MALLOC                             3.8G      190 
MALLOC guard page                   48K       12 
MALLOC_MEDIUM (reserved)           2.2G       20         reserved VM address space (unallocated)
OpenGL GLSL                        256K        3 
STACK GUARD                       56.0M        8 
Stack                             11.6M        8 
VM_ALLOCATE                       35.5M      188 
VM_ALLOCATE (reserved)              44K        2         reserved VM address space (unallocated)
__CTF                               756        1 
__DATA                            61.3M     1328 
__DATA_CONST                      51.3M      374 
__DATA_DIRTY                      1813K      222 
__FONT_DATA                        2352        1 
__GLSLBUILTINS                    5174K        1 
__LINKEDIT                       302.2M      658 
__OBJC_RO                         65.5M        1 
__OBJC_RW                         1989K        2 
__TEXT                             1.1G     1251 
dyld private memory               3328K       10 
mapped file                      400.5M      188 
shared memory                      816K       27 
===========                     =======  ======= 
TOTAL                              8.0G     4587 
TOTAL, minus reserved VM space     5.9G     4587 



-----------
Full Report
-----------

{"app_name":"Slicer","timestamp":"2023-03-10 10:20:15.00 +0800","app_version":"5.2.2","slice_uuid":"4f9a6c91-055c-32b6-a20f-fb9ecd5649bc","build_version":"5.2.2","platform":1,"bundleID":"org.slicer.slicer","share_with_app_devs":0,"is_first_party":0,"bug_type":"309","os_version":"macOS 13.2.1 (22D68)","roots_installed":0,"name":"Slicer","incident_id":"D3F3CA34-A97E-404C-91B1-5C2EE4AD08AB"}
{
  "uptime" : 120000,
  "procRole" : "Foreground",
  "version" : 2,
  "userID" : 501,
  "deployVersion" : 210,
  "modelCode" : "MacPro7,1",
  "coalitionID" : 7661,
  "osVersion" : {
    "train" : "macOS 13.2.1",
    "build" : "22D68",
    "releaseType" : "User"
  },
  "captureTime" : "2023-03-10 10:20:14.8226 +0800",
  "incident" : "D3F3CA34-A97E-404C-91B1-5C2EE4AD08AB",
  "pid" : 32381,
  "cpuType" : "X86-64",
  "roots_installed" : 0,
  "bug_type" : "309",
  "procLaunch" : "2023-03-09 15:29:21.0248 +0800",
  "procStartAbsTime" : 109526906736346,
  "procExitAbsTime" : 125467921211226,
  "procName" : "Slicer",
  "procPath" : "\/Applications\/Slicer.app\/Contents\/MacOS\/Slicer",
  "bundleInfo" : {"CFBundleShortVersionString":"5.2.2","CFBundleVersion":"5.2.2","CFBundleIdentifier":"org.slicer.slicer"},
  "storeInfo" : {"deviceIdentifierForVendor":"EA735995-B421-51AC-ABC5-18FDAD738113","thirdParty":true},
  "parentProc" : "launchd",
  "parentPid" : 1,
  "coalitionName" : "org.slicer.slicer",
  "crashReporterKey" : "24035B9F-6F92-A8A7-F37B-FF7BB60EC79B",
  "throttleTimeout" : 2147483647,
  "wakeTime" : 3161,
  "sleepWakeUUID" : "BA78C671-E910-41E0-B5FF-21916A6A5FE9",
  "sip" : "disabled",
  "vmRegionInfo" : "0x90bfc9000 is not in any region.  Bytes after previous region: 32539185153  Bytes before following region: 105514260459520\n      REGION TYPE                    START - END         [ VSIZE] PRT\/MAX SHRMOD  REGION DETAIL\n      mapped file                 1787d9000-178800000    [  156K] r--\/r-- SM=ALI  ...t_id=a84f6d3d\n---&gt;  GAP OF 0x5ffe87800000 BYTES\n      MALLOC_NANO              600000000000-600008000000 [128.0M] rw-\/rwx SM=PRV  ",
  "exception" : {"codes":"0x0000000000000001, 0x000000090bfc9000","rawCodes":[1,38855806976],"type":"EXC_BAD_ACCESS","signal":"SIGSEGV","subtype":"KERN_INVALID_ADDRESS at 0x000000090bfc9000"},
  "termination" : {"flags":0,"code":11,"namespace":"SIGNAL","indicator":"Segmentation fault: 11","byProc":"exc handler","byPid":32381},
  "vmregioninfo" : "0x90bfc9000 is not in any region.  Bytes after previous region: 32539185153  Bytes before following region: 105514260459520\n      REGION TYPE                    START - END         [ VSIZE] PRT\/MAX SHRMOD  REGION DETAIL\n      mapped file                 1787d9000-178800000    [  156K] r--\/r-- SM=ALI  ...t_id=a84f6d3d\n---&gt;  GAP OF 0x5ffe87800000 BYTES\n      MALLOC_NANO              600000000000-600008000000 [128.0M] rw-\/rwx SM=PRV  ",
  "extMods" : {"caller":{"thread_create":0,"thread_set_state":0,"task_for_pid":0},"system":{"thread_create":0,"thread_set_state":0,"task_for_pid":0},"targeted":{"thread_create":0,"thread_set_state":0,"task_for_pid":0},"warnings":0},
  "faultingThread" : 0,
  "threads" : [{"triggered":true,"id":2431784,"instructionState":{"instructionStream":{"bytes":[137,229,72,141,71,240,93,195,85,72,137,229,72,137,254,72,139,23,72,141,12,213,0,0,0,0,72,191,248,255,255,255,255,255,15,0,72,33,207,72,137,208,72,193,232,49,37,255,7,0,0,72,193,234,60,131,226,3,72,141,13,171,100,5,0,138,12,10,72,211,224,72,131,192,16,72,131,248,17,186,16,0,0,0,72,15,67,208,72,131,194,15,72,131,226,240,72,139,7,72,139,64,64,93,255,224,72,133,246,116,100,85,72,137,229,72,139,86,240,72,131,198,240,72,141,12,213,0,0,0,0,72,191,248,255,255,255,255,255,15,0,72,33,207,72,137,208,72,193,232,49,37,255,7,0,0,72,193,234,60,131,226,3,72,141,13,66,100,5,0,138,12,10,72,211,224,72,131,192,16,72,131,248,17,186,16,0,0,0,72,15,67],"offset":96}},"threadState":{"r13":{"value":140707461455792},"rax":{"value":16},"rflags":{"value":66050},"cpu":{"value":4},"r14":{"value":4874096048},"rsi":{"value":6235491840},"r8":{"value":2},"cr2":{"value":38855806976},"rdx":{"value":16},"r10":{"value":6295316480},"r9":{"value":0},"r15":{"value":7},"rbx":{"value":4874096072},"trap":{"value":14,"description":"(no mapping for user data read)"},"err":{"value":4},"r11":{"value":6235489538},"rip":{"value":140703322160356,"matchesCrashFrame":1},"rbp":{"value":140701890176272},"rsp":{"value":140701890176272},"r12":{"value":4459048880},"rcx":{"value":140703322513668,"symbolLocation":884,"symbol":"dyld3::sVersionMap"},"flavor":"x86_THREAD_STATE","rdi":{"value":38855806976}},"queue":"com.apple.main-thread","frames":[{"imageOffset":183524,"symbol":"lsl::AllocationMetadata::freeObject()","symbolLocation":88,"imageIndex":0},{"imageOffset":250571,"symbol":"lsl::UniquePtr&lt;dyld4::Atlas::Image&gt;::~UniquePtr()","symbolLocation":59,"imageIndex":0},{"imageOffset":83975,"symbol":"lsl::BTree&lt;lsl::UniquePtr&lt;dyld4::Atlas::Image&gt;, std::__1::less&lt;lsl::UniquePtr&lt;dyld4::Atlas::Image&gt; &gt;, false&gt;::NodeCore&lt;31u, 15u&gt;::deallocateChildren()","symbolLocation":101,"imageIndex":0},{"imageOffset":83923,"symbol":"lsl::BTree&lt;lsl::UniquePtr&lt;dyld4::Atlas::Image&gt;, std::__1::less&lt;lsl::UniquePtr&lt;dyld4::Atlas::Image&gt; &gt;, false&gt;::NodeCore&lt;31u, 15u&gt;::deallocateChildren()","symbolLocation":49,"imageIndex":0},{"imageOffset":83923,"symbol":"lsl::BTree&lt;lsl::UniquePtr&lt;dyld4::Atlas::Image&gt;, std::__1::less&lt;lsl::UniquePtr&lt;dyld4::Atlas::Image&gt; &gt;, false&gt;::NodeCore&lt;31u, 15u&gt;::deallocateChildren()","symbolLocation":49,"imageIndex":0},{"imageOffset":83812,"symbol":"lsl::BTree&lt;lsl::UniquePtr&lt;dyld4::Atlas::Image&gt;, std::__1::less&lt;lsl::UniquePtr&lt;dyld4::Atlas::Image&gt; &gt;, false&gt;::clear()","symbolLocation":22,"imageIndex":0},{"imageOffset":82573,"symbol":"dyld4::RuntimeState::freeProcessSnapshot()","symbolLocation":61,"imageIndex":0},{"imageOffset":64630,"symbol":"dyld4::RuntimeState::decDlRefCount(dyld4::Loader const*)","symbolLocation":254,"imageIndex":0},{"imageOffset":227984,"symbol":"dyld4::APIs::dlclose(void*)","symbolLocation":208,"imageIndex":0},{"imageOffset":2043077,"imageIndex":1},{"imageOffset":2020672,"imageIndex":1},{"imageOffset":2032175,"imageIndex":1},{"imageOffset":2017801,"imageIndex":1},{"imageOffset":191519,"symbol":"__cxa_finalize_ranges","symbolLocation":409,"imageIndex":2},{"imageOffset":191033,"symbol":"exit","symbolLocation":35,"imageIndex":2},{"imageOffset":70099,"symbol":"dyld4::LibSystemHelpers::exit(int) const","symbolLocation":11,"imageIndex":3},{"imageOffset":25402,"symbol":"start","symbolLocation":2474,"imageIndex":0}]},{"id":2431924,"name":"com.apple.NSEventThread","frames":[{"imageOffset":5570,"symbol":"mach_msg2_trap","symbolLocation":10,"imageIndex":4},{"imageOffset":62980,"symbol":"mach_msg2_internal","symbolLocation":82,"imageIndex":4},{"imageOffset":34357,"symbol":"mach_msg_overwrite","symbolLocation":723,"imageIndex":4},{"imageOffset":6312,"symbol":"mach_msg","symbolLocation":19,"imageIndex":4},{"imageOffset":523454,"symbol":"__CFRunLoopServiceMachPort","symbolLocation":145,"imageIndex":5},{"imageOffset":517930,"symbol":"__CFRunLoopRun","symbolLocation":1360,"imageIndex":5},{"imageOffset":514912,"symbol":"CFRunLoopRunSpecific","symbolLocation":560,"imageIndex":5},{"imageOffset":1700217,"symbol":"_NSEventThread","symbolLocation":132,"imageIndex":6},{"imageOffset":25177,"symbol":"_pthread_start","symbolLocation":125,"imageIndex":7},{"imageOffset":7291,"symbol":"thread_start","symbolLocation":15,"imageIndex":7}]},{"id":2431991,"name":"QFileInfoGatherer","frames":[{"imageOffset":16666,"symbol":"__psynch_cvwait","symbolLocation":10,"imageIndex":4},{"imageOffset":26593,"symbol":"_pthread_cond_wait","symbolLocation":1243,"imageIndex":7},{"imageOffset":173739,"imageIndex":1},{"imageOffset":173549,"symbol":"QWaitCondition::wait(QMutex*, QDeadlineTimer)","symbolLocation":93,"imageIndex":1},{"imageOffset":2362504,"imageIndex":8},{"imageOffset":140649,"imageIndex":1},{"imageOffset":25177,"symbol":"_pthread_start","symbolLocation":125,"imageIndex":7},{"imageOffset":7291,"symbol":"thread_start","symbolLocation":15,"imageIndex":7}]},{"id":2431992,"name":"QFileInfoGatherer","frames":[{"imageOffset":16666,"symbol":"__psynch_cvwait","symbolLocation":10,"imageIndex":4},{"imageOffset":26593,"symbol":"_pthread_cond_wait","symbolLocation":1243,"imageIndex":7},{"imageOffset":173739,"imageIndex":1},{"imageOffset":173549,"symbol":"QWaitCondition::wait(QMutex*, QDeadlineTimer)","symbolLocation":93,"imageIndex":1},{"imageOffset":2362504,"imageIndex":8},{"imageOffset":140649,"imageIndex":1},{"imageOffset":25177,"symbol":"_pthread_start","symbolLocation":125,"imageIndex":7},{"imageOffset":7291,"symbol":"thread_start","symbolLocation":15,"imageIndex":7}]},{"id":2751824,"frames":[{"imageOffset":7256,"symbol":"start_wqthread","symbolLocation":0,"imageIndex":7}]},{"id":2751955,"frames":[{"imageOffset":7256,"symbol":"start_wqthread","symbolLocation":0,"imageIndex":7}]},{"id":2751957,"frames":[{"imageOffset":7256,"symbol":"start_wqthread","symbolLocation":0,"imageIndex":7}]},{"id":2751958,"frames":[{"imageOffset":7256,"symbol":"start_wqthread","symbolLocation":0,"imageIndex":7}]}],
  "usedImages" : [
  {
    "source" : "P",
    "arch" : "x86_64",
    "base" : 140703321976832,
    "size" : 609456,
    "uuid" : "bba77709-6cad-3592-ab03-09d0f7b8610e",
    "path" : "\/usr\/lib\/dyld",
    "name" : "dyld"
  },
  {
    "source" : "P",
    "arch" : "x86_64",
    "base" : 4508577792,
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
    "base" : 140703324078080,
    "size" : 561152,
    "uuid" : "1aec5d1a-6e43-30f9-a9f2-11eb85d3e70c",
    "path" : "\/usr\/lib\/system\/libsystem_c.dylib",
    "name" : "libsystem_c.dylib"
  },
  {
    "source" : "P",
    "arch" : "x86_64",
    "base" : 140703325380608,
    "size" : 135168,
    "uuid" : "45277dd5-20a4-3c50-b361-a6f18c327027",
    "path" : "\/usr\/lib\/system\/libdyld.dylib",
    "name" : "libdyld.dylib"
  },
  {
    "source" : "P",
    "arch" : "x86_64",
    "base" : 140703325093888,
    "size" : 237560,
    "uuid" : "87ff381c-4d30-3087-bab7-a5a53d232c00",
    "path" : "\/usr\/lib\/system\/libsystem_kernel.dylib",
    "name" : "libsystem_kernel.dylib"
  },
  {
    "source" : "P",
    "arch" : "x86_64h",
    "base" : 140703325732864,
    "CFBundleShortVersionString" : "6.9",
    "CFBundleIdentifier" : "com.apple.CoreFoundation",
    "size" : 4825072,
    "uuid" : "c2615780-0140-315c-a455-7e03bb22d3d6",
    "path" : "\/System\/Library\/Frameworks\/CoreFoundation.framework\/Versions\/A\/CoreFoundation",
    "name" : "CoreFoundation",
    "CFBundleVersion" : "1953.300"
  },
  {
    "source" : "P",
    "arch" : "x86_64",
    "base" : 140703377702912,
    "CFBundleShortVersionString" : "6.9",
    "CFBundleIdentifier" : "com.apple.AppKit",
    "size" : 16814067,
    "uuid" : "540cedfd-5a35-3f35-8953-dcb7c4834eb5",
    "path" : "\/System\/Library\/Frameworks\/AppKit.framework\/Versions\/C\/AppKit",
    "name" : "AppKit",
    "CFBundleVersion" : "2299.40.118"
  },
  {
    "source" : "P",
    "arch" : "x86_64",
    "base" : 140703325331456,
    "size" : 49144,
    "uuid" : "3bd433d4-15bd-3add-a612-95e4d3b20719",
    "path" : "\/usr\/lib\/system\/libsystem_pthread.dylib",
    "name" : "libsystem_pthread.dylib"
  },
  {
    "source" : "P",
    "arch" : "x86_64",
    "base" : 4483256320,
    "CFBundleShortVersionString" : "5.15",
    "CFBundleIdentifier" : "org.qt-project.QtWidgets",
    "size" : 4485120,
    "uuid" : "6a0c4de6-8a12-31d0-90cb-63e5c78b6c35",
    "path" : "\/Applications\/Slicer.app\/Contents\/Frameworks\/QtWidgets.framework\/Versions\/5\/QtWidgets",
    "name" : "QtWidgets",
    "CFBundleVersion" : "5.15.2"
  },
  {
    "size" : 0,
    "source" : "A",
    "base" : 0,
    "uuid" : "00000000-0000-0000-0000-000000000000"
  }
],
  "sharedCache" : {
  "base" : 140703321370624,
  "size" : 21474836480,
  "uuid" : "57815a20-af2c-3b56-9006-23abde7962b0"
},
  "vmSummary" : "ReadOnly portion of Libraries: Total=1.4G resident=0K(0%) swapped_out_or_unallocated=1.4G(100%)\nWritable regions: Total=6.0G written=0K(0%) resident=0K(0%) swapped_out=0K(0%) unallocated=6.0G(100%)\n\n                                VIRTUAL   REGION \nREGION TYPE                        SIZE    COUNT (non-coalesced) \n===========                     =======  ======= \nAccelerate framework               128K        1 \nActivity Tracing                   256K        1 \nCG backing stores                 1920K        8 \nCG image                            92K       16 \nColorSync                          240K       27 \nCoreAnimation                     1152K       20 \nCoreGraphics                        24K        4 \nCoreUI image data                  796K       13 \nFoundation                          16K        1 \nKernel Alloc Once                    8K        1 \nMALLOC                             3.8G      190 \nMALLOC guard page                   48K       12 \nMALLOC_MEDIUM (reserved)           2.2G       20         reserved VM address space (unallocated)\nOpenGL GLSL                        256K        3 \nSTACK GUARD                       56.0M        8 \nStack                             11.6M        8 \nVM_ALLOCATE                       35.5M      188 \nVM_ALLOCATE (reserved)              44K        2         reserved VM address space (unallocated)\n__CTF                               756        1 \n__DATA                            61.3M     1328 \n__DATA_CONST                      51.3M      374 \n__DATA_DIRTY                      1813K      222 \n__FONT_DATA                        2352        1 \n__GLSLBUILTINS                    5174K        1 \n__LINKEDIT                       302.2M      658 \n__OBJC_RO                         65.5M        1 \n__OBJC_RW                         1989K        2 \n__TEXT                             1.1G     1251 \ndyld private memory               3328K       10 \nmapped file                      400.5M      188 \nshared memory                      816K       27 \n===========                     =======  ======= \nTOTAL                              8.0G     4587 \nTOTAL, minus reserved VM space     5.9G     4587 \n",
  "legacyInfo" : {
  "threadTriggered" : {
    "queue" : "com.apple.main-thread"
  }
},
  "trialInfo" : {
  "rollouts" : [
    {
      "rolloutId" : "5fb4245a1bbfe8005e33a1e1",
      "factorPackIds" : {

      },
      "deploymentId" : 240000021
    },
    {
      "rolloutId" : "62cdf63ddb3b7109d6d765cc",
      "factorPackIds" : {
        "SIRI_UNDERSTANDING_TMDC" : "62cdf6dddb3b7109d6d765cd"
      },
      "deploymentId" : 240000007
    }
  ],
  "experiments" : [

  ]
}
}

Model: MacPro7,1, BootROM 1916.60.2.0.0, 20 processors, Intel Core i5-13600KF, 3.5 GHz, 64 GB, SMC 
Graphics: AMD Radeon RX 580, AMD Radeon RX 580, PCIe, 8 GB
Display: Mi Monitor, 2560 x 1440 (QHD/WQHD - Wide Quad High Definition), MirrorOff, Online
Display: Mi Monitor, 2560 x 1440 (QHD/WQHD - Wide Quad High Definition), Main, MirrorOff, Online
Memory Module: BANK 0/Controller0-DIMMA2, 32 GB, DDR4, 3600 MHz, 0x0B92, -
Memory Module: BANK 0/Controller1-DIMMB2, 32 GB, DDR4, 3600 MHz, 0x0B92, -
AirPort: spairport_wireless_card_type_wifi (0x14E4, 0x111), Broadcom BCM43xx 1.0 (7.77.111.1 AirPortDriverBrcmNIC-1766)
AirPort: 
Bluetooth: Version (null), 0 services, 0 devices, 0 incoming serial ports
Network Service: Wi-Fi, AirPort, en1
PCI Card: Realtek ALCS1220A, Audio device, Built In
USB Device: USB32Bus
USB Device: USB3.2 Hub
USB Device: USB3.0 Hub
USB Device: USB3.1 Hub
USB Device: bluetooth_device
USB Device: USB2.0 Hub
USB Device: BRCM20702 Hub
USB Device: Bluetooth USB Host Controller
USB Device: USB 2.4G Keyboard Mouse
USB Device: Hexgears Keyboard
USB Device: USB2.1 Hub
USB Device: USB2.0 Hub
USB Device: USB Receiver
USB Device: USB2.1 Hub
Thunderbolt Bus:
</code></pre>

---

## Post #2 by @pieper (2023-03-10 14:57 UTC)

<p><a class="mention" href="/u/zyy">@zyy</a> please provide more information about what specific steps led to the crash.</p>

---
