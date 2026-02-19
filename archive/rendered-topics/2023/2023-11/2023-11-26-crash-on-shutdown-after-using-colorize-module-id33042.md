---
topic_id: 33042
title: "Crash On Shutdown After Using Colorize Module"
date: 2023-11-26
url: https://discourse.slicer.org/t/33042
---

# Crash on shutdown after using Colorize module

**Topic ID**: 33042
**Date**: 2023-11-26
**URL**: https://discourse.slicer.org/t/crash-on-shutdown-after-using-colorize-module/33042

---

## Post #1 by @muratmaga (2023-11-26 18:58 UTC)

<p>Slicer seems to create a crash report in MacOS, when closed normally.  It is too long to paste the whole thing.</p>
<details><summary>Crash report</summary>
<pre><code class="lang-auto">-------------------------------------
Translated Report (Full Report Below)
-------------------------------------

Process:               Slicer [82367]
Path:                  /Users/USER/Desktop/Slicer.app/Contents/MacOS/Slicer
Identifier:            org.slicer.slicer
Version:               5.6.0 (5.6.0)
Code Type:             X86-64 (Native)
Parent Process:        launchd [1]
User ID:               1950572333

Date/Time:             2023-11-26 10:55:47.8440 -0800
OS Version:            macOS 12.7.1 (21G920)
Report Version:        12
Bridge OS Version:     8.2 (21P52047d)
Anonymous UUID:        061333B8-0FD5-DBE2-ED53-7B373F48D0CE

Sleep/Wake UUID:       9F030B79-320F-441B-9B27-5D2332D230B3

Time Awake Since Boot: 200000 seconds
Time Since Wake:       1982 seconds

System Integrity Protection: enabled

Crashed Thread:        0  Dispatch queue: com.apple.main-thread

Exception Type:        EXC_BAD_ACCESS (SIGSEGV)
Exception Codes:       KERN_INVALID_ADDRESS at 0x0000000000000000
Exception Codes:       0x0000000000000001, 0x0000000000000000
Exception Note:        EXC_CORPSE_NOTIFY

Termination Reason:    Namespace SIGNAL, Code 11 Segmentation fault: 11
Terminating Process:   exc handler [82367]

VM Region Info: 0 is not in any region.  Bytes before following region: 4516671488
      REGION TYPE                    START - END         [ VSIZE] PRT/MAX SHRMOD  REGION DETAIL
      UNUSED SPACE AT START
---&gt;  
      __TEXT                      10d36f000-10d3b3000    [  272K] r-x/r-x SM=COW  .../MacOS/Slicer

Kernel Triage:
VM - Fault hit memory shortage
VM - Fault hit memory shortage
VM - Fault hit memory shortage
VM - Fault hit memory shortage
VM - Fault hit memory shortage


Thread 0 Crashed::  Dispatch queue: com.apple.main-thread
0   libvtkCommon-9.2.1.dylib      	       0x13177451a void vtk::detail::smp::vtkSMPToolsAPI::For&lt;vtk::detail::smp::vtkSMPTools_FunctorInternal&lt;vtkThreadedImageAlgorithmFunctor, false&gt; &gt;(long long, long long, long long, vtk::detail::smp::vtkSMPTools_FunctorInternal&lt;vtkThreadedImageAlgorithmFunctor, false&gt;&amp;) + 218
1   libvtkCommon-9.2.1.dylib      	       0x131773dda vtkThreadedImageAlgorithm::RequestData(vtkInformation*, vtkInformationVector**, vtkInformationVector*) + 1498
2   libvtkCommon-9.2.1.dylib      	       0x1316f08f4 vtkExecutive::CallAlgorithm(vtkInformation*, int, vtkInformationVector**, vtkInformationVector*) + 68
3   libvtkCommon-9.2.1.dylib      	       0x1316eacdd vtkDemandDrivenPipeline::ExecuteData(vtkInformation*, vtkInformationVector**, vtkInformationVector*) + 61
4   libvtkCommon-9.2.1.dylib      	       0x1316ea40b vtkDemandDrivenPipeline::ProcessRequest(vtkInformation*, vtkInformationVector**, vtkInformationVector*) + 1259
5   libvtkCommon-9.2.1.dylib      	       0x13176402f vtkStreamingDemandDrivenPipeline::ProcessRequest(vtkInformation*, vtkInformationVector**, vtkInformationVector*) + 815
6   libvtkCommon-9.2.1.dylib      	       0x131764647 vtkStreamingDemandDrivenPipeline::Update(int, vtkInformationVector*) + 279
7   libvtkSegmentationCore.dylib  	       0x11130abd4 vtkSegmentation::SeparateSegmentLabelmap(std::__1::basic_string&lt;char, std::__1::char_traits&lt;char&gt;, std::__1::allocator&lt;char&gt; &gt;) + 436
8   libvtkSegmentationCore.dylib  	       0x11130a43e vtkSegmentation::RemoveSegment(std::__1::__map_iterator&lt;std::__1::__tree_iterator&lt;std::__1::__value_type&lt;std::__1::basic_string&lt;char, std::__1::char_traits&lt;char&gt;, std::__1::allocator&lt;char&gt; &gt;, vtkSmartPointer&lt;vtkSegment&gt; &gt;, std::__1::__tree_node&lt;std::__1::__value_type&lt;std::__1::basic_string&lt;char, std::__1::char_traits&lt;char&gt;, std::__1::allocator&lt;char&gt; &gt;, vtkSmartPointer&lt;vtkSegment&gt; &gt;, void*&gt;*, long&gt; &gt;) + 94
9   libvtkSegmentationCore.dylib  	       0x111305da0 vtkSegmentation::RemoveAllSegments() + 96
10  libvtkSegmentationCore.dylib  	       0x111305bdd vtkSegmentation::~vtkSegmentation() + 29
11  libvtkSegmentationCore.dylib  	       0x111305e7e vtkSegmentation::~vtkSegmentation() + 14
12  libMRMLCore.dylib             	       0x11182ea3f vtkMRMLSegmentationNode::SetSegmentation(vtkSegmentation*) + 63
13  libMRMLCore.dylib             	       0x111826a21 vtkMRMLSegmentationNode::SetAndObserveSegmentation(vtkSegmentation*) + 81
14  libMRMLCore.dylib             	       0x111826b7b vtkMRMLSegmentationNode::~vtkMRMLSegmentationNode() + 27
15  libMRMLCore.dylib             	       0x111826c0e vtkMRMLSegmentationNode::~vtkMRMLSegmentationNode() + 14
16  libMRMLCore.dylib             	       0x1117fb33e vtkMRMLScene::RemoveNode(vtkMRMLNode*) + 1022
17  libMRMLCore.dylib             	       0x1117fa420 vtkMRMLScene::RemoveAllNodes(bool) + 368
18  libMRMLCore.dylib             	       0x1117f9b6c vtkMRMLScene::Clear(int) + 60
19  libvtkCommon-9.2.1.dylib      	       0x1320e75e1 vtkCallbackCommand::Execute(vtkObject*, unsigned long, void*) + 33
20  libvtkCommon-9.2.1.dylib      	       0x13228dc40 vtkSubjectHelper::InvokeEvent(unsigned long, void*, vtkObject*) + 992
21  libvtkCommon-9.2.1.dylib      	       0x13228eeb5 vtkObject::ObjectFinalize() + 37
22  libvtkCommon-9.2.1.dylib      	       0x13228fd59 vtkObjectBase::UnRegisterInternal(vtkObjectBase*, int) + 73
23  libMRMLLogic.dylib            	       0x10f5c9a4c vtkMRMLAbstractLogic::~vtkMRMLAbstractLogic() + 44
24  libSlicerBaseLogic.dylib      	       0x10f51b9ce vtkSlicerApplicationLogic::~vtkSlicerApplicationLogic() + 14
25  libvtkCommon-9.2.1.dylib      	       0x132308bee vtkSmartPointerBase::~vtkSmartPointerBase() + 30
26  libMRMLDisplayableManager.dylib	       0x10e952caa vtkMRMLDisplayableManagerFactory::~vtkMRMLDisplayableManagerFactory() + 42
27  libMRMLDisplayableManager.dylib	       0x10e95579e vtkMRMLThreeDViewDisplayableManagerFactory::~vtkMRMLThreeDViewDisplayableManagerFactory() + 14
28  libMRMLDisplayableManager.dylib	       0x10e9555fc vtkMRMLThreeDViewDisplayableManagerFactoryInitialize::~vtkMRMLThreeDViewDisplayableManagerFactoryInitialize() + 28
29  libsystem_c.dylib             	    0x7ff81baaadd4 __cxa_finalize_ranges + 409
30  libsystem_c.dylib             	    0x7ff81baaabee exit + 35
31  libdyld.dylib                 	    0x7ff81bbbe375 dyld4::LibSystemHelpers::exit(int) const + 11
32  dyld                          	       0x1163c7558 start + 504

Thread 1:: QFileInfoGatherer
0   libsystem_kernel.dylib        	    0x7ff81bb783da __psynch_cvwait + 10
1   libsystem_pthread.dylib       	    0x7ff81bbb2a6f _pthread_cond_wait + 1249
2   QtCore                        	       0x110381a8b 0x110358000 + 170635
3   QtCore                        	       0x110381a04 QWaitCondition::wait(QMutex*, QDeadlineTimer) + 84
4   QtWidgets                     	       0x10ed817ba 0x10eb3a000 + 2389946
5   QtCore                        	       0x110379d20 0x110358000 + 138528
6   libsystem_pthread.dylib       	    0x7ff81bbb24e1 _pthread_start + 125
7   libsystem_pthread.dylib       	    0x7ff81bbadf6b thread_start + 15

Thread 2:: com.apple.NSEventThread
0   libsystem_kernel.dylib        	    0x7ff81bb7596a mach_msg_trap + 10
1   libsystem_kernel.dylib        	    0x7ff81bb75cd8 mach_msg + 56
2   CoreFoundation                	    0x7ff81bc7929d __CFRunLoopServiceMachPort + 319
3   CoreFoundation                	    0x7ff81bc77928 __CFRunLoopRun + 1276
4   CoreFoundation                	    0x7ff81bc76d6c CFRunLoopRunSpecific + 562
5   AppKit                        	    0x7ff81e81f98e _NSEventThread + 132
6   libsystem_pthread.dylib       	    0x7ff81bbb24e1 _pthread_start + 125
7   libsystem_pthread.dylib       	    0x7ff81bbadf6b thread_start + 15

Thread 3:
0   libsystem_kernel.dylib        	    0x7ff81bb759a6 semaphore_wait_trap + 10
1   libtbb.12.dylib               	       0x118df95f9 tbb::detail::r1::rml::private_worker::run() + 697
2   libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
3   libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
4   libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
5   libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
6   libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
7   libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
8   libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
9   libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
10  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
11  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
12  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
13  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
14  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
15  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
16  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
17  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
18  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
19  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
20  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
21  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
22  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
23  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
24  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
25  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
26  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
27  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
28  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
29  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
30  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
31  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
32  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
33  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
34  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
35  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
36  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
37  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
38  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
39  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
40  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
41  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
42  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
43  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
44  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
45  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
46  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
47  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
48  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
49  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
50  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
51  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
52  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
53  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
54  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
55  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
56  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
57  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
58  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
59  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
60  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
61  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
62  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
63  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
64  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
65  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
66  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
67  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
68  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
69  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
70  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
71  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
72  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
73  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
74  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
75  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
76  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
77  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
78  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
79  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
80  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
81  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
82  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
83  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
84  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
85  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
86  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
87  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
88  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
89  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
90  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
91  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
92  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
93  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
94  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
95  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
96  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
97  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
98  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
99  libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
100 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
101 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
102 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
103 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
104 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
105 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
106 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
107 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
108 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
109 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
110 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
111 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
112 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
113 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
114 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
115 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
116 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
117 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
118 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
119 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
120 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
121 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
122 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
123 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
124 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
125 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
126 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
127 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
128 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
129 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
130 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
131 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
132 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
133 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
134 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
135 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
136 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
137 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
138 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
139 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
140 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
141 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
142 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
143 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
144 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
145 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
146 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
147 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
148 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
149 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
150 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
151 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
152 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
153 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
154 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
155 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
156 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
157 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
158 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
159 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
160 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
161 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
162 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
163 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
164 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
165 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
166 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
167 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
168 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
169 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
170 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
171 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
172 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
173 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
174 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
175 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
176 libtbb.12.dylib               	       0x118df9339 tbb::detail::r1::rml::private_worker::thread_routine(void*) + 9
177 libtbb.12.dylib
</code></pre>
</details>

---

## Post #2 by @muratmaga (2023-11-26 19:03 UTC)

<p>seems to happen when interact with the Colorize Volumes and Light… (i.e., crash report happens after I close the slicer. Both modules seemed to be working normally).</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a></p>

---
