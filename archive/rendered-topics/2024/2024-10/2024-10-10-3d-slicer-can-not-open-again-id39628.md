---
topic_id: 39628
title: "3D Slicer Can Not Open Again"
date: 2024-10-10
url: https://discourse.slicer.org/t/39628
---

# 3D Slicer can not open again

**Topic ID**: 39628
**Date**: 2024-10-10
**URL**: https://discourse.slicer.org/t/3d-slicer-can-not-open-again/39628

---

## Post #1 by @doc-xie (2024-10-10 08:29 UTC)

<p>After some modules installed, 3D Slicer can not open with the following information:</p>
<pre><code class="lang-plaintext">-------------------------------------
Translated Report (Full Report Below)
-------------------------------------

Process:               Slicer [2273]
Path:                  /Users/USER/*/Slicer.app/Contents/MacOS/Slicer
Identifier:            org.slicer.slicer
Version:                (5.7.0-2024-07-20)
Code Type:             X86-64 (Native)
Parent Process:        launchd [1]
User ID:               501

Date/Time:             2024-10-10 16:15:09.2231 +0800
OS Version:            macOS 15.0.1 (24A348)
Report Version:        12
Bridge OS Version:     9.0 (22P353)
Anonymous UUID:        A9658DA3-1911-6DB6-33E6-F16504352DB8

Sleep/Wake UUID:       CAC2FFEF-D0C7-4622-8DA4-C997F996E409

Time Awake Since Boot: 2300 seconds
Time Since Wake:       313 seconds

System Integrity Protection: enabled

Crashed Thread:        0  Dispatch queue: com.apple.main-thread

Exception Type:        EXC_ARITHMETIC (SIGFPE)
Exception Codes:       0x0000000000000001, 0x0000000000000000

Termination Reason:    Namespace SIGNAL, Code 8 Floating point exception: 8
Terminating Process:   exc handler [2273]
 Anyone can help to solve the issue.
Thanks
</code></pre>

---

## Post #2 by @cpinter (2024-10-10 10:41 UTC)

<p>Please try with the very latest Slicer.</p>
<p>Also specify the “some modules” please.</p>

---

## Post #3 by @doc-xie (2024-10-11 00:29 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="2" data-topic="39628">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>Also specify the “some modules” please.</p>
</blockquote>
</aside>
<p>Hi,<br>
Because 3D Slicer can not open normally, so the installed modules can not be clarified clearly. Most of the modules in the “Segmentations” were installed and the software run correctly. But after I download the modules (SlicerMorphy, UKF Tractography,et al), the software can not run again. I want to know the reason of the crash. Moreover, is there any method to solve the issue in addition to re-install the software?<br>
Thanks.</p>
<p>Some of the crash informations were following:</p>
<pre><code class="lang-plaintext">Thread 1:
0   libsystem_pthread.dylib       	    0x7ff81c46bbcc start_wqthread + 0

Thread 2:
0   libsystem_pthread.dylib       	    0x7ff81c46bbcc start_wqthread + 0

Thread 3:
0   libsystem_kernel.dylib        	    0x7ff81c431876 __semwait_signal + 10
1   libsystem_c.dylib             	    0x7ff81c31fcf1 nanosleep + 199
2   libsystem_c.dylib             	    0x7ff81c31fc24 usleep + 53
3   libSlicerBaseLogic.dylib      	       0x1092ba203 vtkSlicerApplicationLogic::ProcessProcessingTasks() + 83
4   libSlicerBaseLogic.dylib      	       0x1092b9d78 vtkSlicerApplicationLogic::ProcessingThreaderCallback(void*) + 40
5   libsystem_pthread.dylib       	    0x7ff81c470253 _pthread_start + 99
6   libsystem_pthread.dylib       	    0x7ff81c46bbef thread_start + 15

Thread 4:
0   libsystem_kernel.dylib        	    0x7ff81c431876 __semwait_signal + 10
1   libsystem_c.dylib             	    0x7ff81c31fcf1 nanosleep + 199
2   libsystem_c.dylib             	    0x7ff81c31fc24 usleep + 53
3   libSlicerBaseLogic.dylib      	       0x1092ba3d3 vtkSlicerApplicationLogic::ProcessNetworkingTasks() + 83
4   libSlicerBaseLogic.dylib      	       0x1092b9ed8 vtkSlicerApplicationLogic::NetworkingThreaderCallback(void*) + 40
5   libsystem_pthread.dylib       	    0x7ff81c470253 _pthread_start + 99
6   libsystem_pthread.dylib       	    0x7ff81c46bbef thread_start + 15


Thread 0 crashed with X86 Thread State (64-bit):
  rax: 0x0000000000000001  rbx: 0x00007fbfeb89d0e0  rcx: 0x0000000000000000  rdx: 0x0000000000000000
  rdi: 0x00007fbfeb89d0e0  rsi: 0x0000000000000000  rbp: 0x00007ff7b8d35d40  rsp: 0x00007ff7b8d35d00
   r8: 0x4578497265666675   r9: 0xffffffff00000000  r10: 0x0000000000000000  r11: 0x00007ff68d64deda
  r12: 0x0000000000000001  r13: 0x0000000000000000  r14: 0x00007fbfeb89cf18  r15: 0x00007fbfeb89cf10
  rip: 0x000000013f18f61b  rfl: 0x0000000000010202  cr2: 0x0000000000000000
  
Logical CPU:     2
Error Code:      0x00000000 
Trap Number:     0

Thread 0 instruction stream:
  5b 5b 2a 00 48 8b 75 c8-4c 89 ff e8 67 5b 2a 00  [[*.H.u.L...g[*.
  48 8d 7d c8 e8 58 5b 2a-00 e8 ff 5a 2a 00 48 8d  H.}..X[*...Z*.H.
  7d c8 48 8d 55 d0 48 89-c6 e8 31 5b 2a 00 48 8b  }.H.U.H...1[*.H.
  75 c8 4c 89 f7 e8 3d 5b-2a 00 48 8d 7d c8 e8 2e  u.L...=[*.H.}...
  5b 2a 00 49 8b 1e 48 8b-4b 30 4c 8b 6b 38 4d 8d  [*.I..H.K0L.k8M.
  65 01 49 39 cc 7c 45 48-63 73 40 4c 89 e0 48 99  e.I9.|EHcs@L..H.
 [48]f7 fe 48 85 c0 78 34-48 ff c0 48 0f af f0 48  H..H..x4H..H...H	&lt;==
  8d 56 ff 49 39 d5 7d 24-48 39 f1 7d 1b 48 89 55  .V.I9.}$H9.}.H.U
  c0 48 8b 0b 48 89 df 48-89 c6 ff 91 58 01 00 00  .H..H..H....X...
  85 c0 48 8b 55 c0 74 04-48 89 53 38 4c 89 63 38  ..H.U.t.H.S8L.c8
  48 8b 83 20 01 00 00 48-8b 40 30 4a c7 44 e8 08  H.. ...H.@0J.D..
  00 00 00 00 e8 ee 57 2a-00 84 c0 74 05 41 c6 47  ......W*...t.A.G

Binary Images:
0x1071c2000 -        0x107205fff org.slicer.slicer (*) &lt;d72b322c-9764-31b0-a4bc-767cbc3dcd71&gt; /Users/USER/*/Slicer.app/Contents/MacOS/Slicer
       0x1072fe000 -        0x1073d5fff libqSlicerApp.dylib (*) &lt;c97e4def-b475-3faa-8a0f-efcaa6fcea22&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libqSlicerApp.dylib
       0x1073e6000 -        0x107451fff libqSlicerBaseQTApp.dylib (*) &lt;7f6f92ea-e3bf-3e96-9c4f-a07daca8564e&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libqSlicerBaseQTApp.dylib
       0x10727a000 -        0x1072c9fff libqSlicerModulesCore.dylib (*) &lt;ea9e76d5-39d2-30bd-bcd9-50609cdc6ab8&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libqSlicerModulesCore.dylib
       0x10752d000 -        0x1075b4fff libqSlicerBaseQTCLI.dylib (*) &lt;e8af47d3-a921-3e7d-acd4-66fce6bd2a66&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libqSlicerBaseQTCLI.dylib
       0x10787a000 -        0x107a75fff libqSlicerBaseQTGUI.dylib (*) &lt;a84fc5e3-8896-3a68-af3f-5af09fe742bc&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libqSlicerBaseQTGUI.dylib
       0x107b0e000 -        0x107ca1fff libqMRMLWidgets.dylib (*) &lt;de2cf360-9a90-3190-a835-b9ffb7979016&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libqMRMLWidgets.dylib
       0x107246000 -        0x107261fff libCTKQtTesting.0.1.dylib (*) &lt;8216a009-68ae-360a-8508-2aeb192e0ce7&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libCTKQtTesting.0.1.dylib
       0x1075e9000 -        0x10763cfff libCTKVisualizationVTKWidgets.0.1.dylib (*) &lt;a4aab7c5-9ded-3f89-b590-6d1f45c399ea&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libCTKVisualizationVTKWidgets.0.1.dylib
       0x107472000 -        0x107481fff libCTKScriptingPythonWidgets.0.1.dylib (*) &lt;27195c47-925e-3c0a-b063-c202af77bddf&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libCTKScriptingPythonWidgets.0.1.dylib
       0x107d7e000 -        0x107e4dfff libCTKDICOMWidgets.0.1.dylib (*) &lt;ddff1254-fb02-3a75-9eec-be2c3885ecba&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libCTKDICOMWidgets.0.1.dylib
       0x107eb6000 -        0x107fbdfff libCTKWidgets.0.1.dylib (*) &lt;fbf8641e-1617-346c-b13c-f62a18af4455&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libCTKWidgets.0.1.dylib
       0x107689000 -        0x1076c4fff libQtTesting.dylib (*) &lt;51f71f38-c233-3d5c-a6d3-a905e3623510&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libQtTesting.dylib
       0x10809a000 -        0x108181fff libqSlicerBaseQTCore.dylib (*) &lt;8026e082-f3bf-3655-b2f2-488422134235&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libqSlicerBaseQTCore.dylib
       0x10878f000 -        0x108bdefff org.qt-project.QtWidgets (5.15) &lt;96f78bf3-1287-327e-bc86-86b21c532078&gt; /Users/USER/*/Slicer.app/Contents/Frameworks/QtWidgets.framework/Versions/5/QtWidgets
       0x10934b000 -        0x10983efff org.qt-project.QtGui (5.15) &lt;3d3ad257-ba9d-3076-9d1e-1f60999e2add&gt; /Users/USER/*/Slicer.app/Contents/Frameworks/QtGui.framework/Versions/5/QtGui
       0x109f68000 -        0x10a4affff org.qt-project.QtCore (5.15) &lt;2053c83a-a3d3-3bf8-ab74-fced979f0581&gt; /Users/USER/*/Slicer.app/Contents/Frameworks/QtCore.framework/Versions/5/QtCore
       0x1074d8000 -        0x107507fff org.qt-project.QtXml (5.15) &lt;218292bb-8689-3454-8024-f9f7b3ef0422&gt; /Users/USER/*/Slicer.app/Contents/Frameworks/QtXml.framework/Versions/5/QtXml
       0x108d44000 -        0x109027fff org.qt-project.QtXmlPatterns (5.15) &lt;7d27b8b1-3d02-360e-ba51-4b6d64dc4704&gt; /Users/USER/*/Slicer.app/Contents/Frameworks/QtXmlPatterns.framework/Versions/5/QtXmlPatterns
       0x10774a000 -        0x107781fff org.qt-project.QtSvg (5.15) &lt;97e915fb-02dc-3764-9223-135406a84ec2&gt; /Users/USER/*/Slicer.app/Contents/Frameworks/QtSvg.framework/Versions/5/QtSvg
       0x107496000 -        0x1074a9fff org.qt-project.QtMultimediaWidgets (5.15) &lt;26eb5bfd-8cb0-3778-a966-9f2e582799e6&gt; /Users/USER/*/Slicer.app/Contents/Frameworks/QtMultimediaWidgets.framework/Versions/5/QtMultimediaWidgets
       0x1081da000 -        0x108255fff org.qt-project.QtMultimedia (5.15) &lt;8dd8a1d3-f27d-3bee-9d84-2db9967c9f53&gt; /Users/USER/*/Slicer.app/Contents/Frameworks/QtMultimedia.framework/Versions/5/QtMultimedia
       0x1082a5000 -        0x1082d8fff org.qt-project.QtWebEngine (5.15) &lt;16e1b92e-d194-314e-9477-196a9ef7cfbd&gt; /Users/USER/*/Slicer.app/Contents/Frameworks/QtWebEngine.framework/Versions/5/QtWebEngine
       0x10779f000 -        0x1077c2fff org.qt-project.QtWebEngineWidgets (5.15) &lt;0623baaa-0056-372d-a349-846fe6a1ab40&gt; /Users/USER/*/Slicer.app/Contents/Frameworks/QtWebEngineWidgets.framework/Versions/5/QtWebEngineWidgets
       0x1077eb000 -        0x107816fff org.qt-project.QtPrintSupport (5.15) &lt;743ae84b-6dbe-365f-a77c-a8284cd42487&gt; /Users/USER/*/Slicer.app/Contents/Frameworks/QtPrintSupport.framework/Versions/5/QtPrintSupport
       0x112e6a000 -        0x11b149fff org.qt-project.Qt.QtWebEngineCore (5.15) &lt;d0b64e1b-3d14-3cb8-a354-37d1f224da92&gt; /Users/USER/*/Slicer.app/Contents/Frameworks/QtWebEngineCore.framework/Versions/5/QtWebEngineCore
       0x108392000 -        0x1083f5fff org.qt-project.QtPositioning (5.15) &lt;1bcaa3ec-9258-3440-849e-51ca911dcbdf&gt; /Users/USER/*/Slicer.app/Contents/Frameworks/QtPositioning.framework/Versions/5/QtPositioning
       0x10a57a000 -        0x10a8b1fff org.qt-project.QtQuick (5.15) &lt;b59948f3-b7ab-3713-bacb-fb46951aaa26&gt; /Users/USER/*/Slicer.app/Contents/Frameworks/QtQuick.framework/Versions/5/QtQuick
       0x108413000 -        0x10846afff org.qt-project.QtQmlModels (5.15) &lt;dac86476-3a34-3a79-ad45-d07aa2a41ede&gt; /Users/USER/*/Slicer.app/Contents/Frameworks/QtQmlModels.framework/Versions/5/QtQmlModels
       0x1076f5000 -        0x107710fff org.qt-project.QtWebChannel (5.15) &lt;a2d88e04-a6b4-38e3-81a8-77cd3bf7d46e&gt; /Users/USER/*/Slicer.app/Contents/Frameworks/QtWebChannel.framework/Versions/5/QtWebChannel
       0x10848a000 -        0x1084c1fff org.qt-project.QtTest (5.15) &lt;864c0e12-c069-36d8-9ada-263e4f30cd25&gt; /Users/USER/*/Slicer.app/Contents/Frameworks/QtTest.framework/Versions/5/QtTest
       0x1085c6000 -        0x10865dfff libMRMLDisplayableManager.dylib (*) &lt;ce9a990c-3865-33c3-aea1-dff889cb06d3&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libMRMLDisplayableManager.dylib
       0x107229000 -        0x107230fff libCTKImageProcessingITKCore.0.1.dylib (*) &lt;571dffd9-88ad-336d-8b80-35a3d398739e&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libCTKImageProcessingITKCore.0.1.dylib
       0x1084d9000 -        0x1084f8fff libCTKVisualizationVTKCore.0.1.dylib (*) &lt;84225636-3afe-35b7-999e-28216625c52c&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libCTKVisualizationVTKCore.0.1.dylib
       0x109180000 -        0x10922ffff libCTKDICOMCore.0.1.dylib (*) &lt;d5e854b1-e421-3155-8475-cb5c44ddbda2&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libCTKDICOMCore.0.1.dylib
       0x10a9e6000 -        0x10ad2dfff org.qt-project.QtQml (5.15) &lt;cfb649a9-1a52-360c-b515-14de04c06bab&gt; /Users/USER/*/Slicer.app/Contents/Frameworks/QtQml.framework/Versions/5/QtQml
       0x109acf000 -        0x109bf6fff org.qt-project.QtNetwork (5.15) &lt;d934bb77-f5b3-37f4-840a-5df20c29fbc5&gt; /Users/USER/*/Slicer.app/Contents/Frameworks/QtNetwork.framework/Versions/5/QtNetwork
       0x10851d000 -        0x108548fff libModuleDescriptionParser.dylib (*) &lt;b2f84da6-9156-39a1-9f66-669dd7b99416&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libModuleDescriptionParser.dylib
       0x1074b9000 -        0x1074c4fff libCTKScriptingPythonCore.0.1.dylib (*) &lt;01c8427e-6656-37c2-92e9-f7b29f3d5c6d&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libCTKScriptingPythonCore.0.1.dylib
       0x109075000 -        0x1090c4fff libCTKCore.0.1.dylib (*) &lt;ccf2e3e7-8a22-3e01-a7b4-168bb44ea0f2&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libCTKCore.0.1.dylib
       0x10c292000 -        0x10cb15fff libPythonQt.dylib (*) &lt;9e324eba-cd5c-3e34-9639-515d6178d88f&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libPythonQt.dylib
       0x10928c000 -        0x109313fff libSlicerBaseLogic.dylib (*) &lt;0912f3f8-bd28-3211-9e3b-1b3b08c055b6&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libSlicerBaseLogic.dylib
       0x108561000 -        0x108598fff libMRMLCLI.dylib (*) &lt;655284bc-3a60-304f-b382-217a1c0616aa&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libMRMLCLI.dylib
       0x10995a000 -        0x1099c9fff libMRMLLogic.dylib (*) &lt;cecff8cc-cc92-3b2b-9400-efba47f62cf7&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libMRMLLogic.dylib
       0x1099f6000 -        0x109a79fff libRemoteIO.dylib (*) &lt;4b2a2578-c76c-3b0a-903b-e42531860efe&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libRemoteIO.dylib
       0x10b2b2000 -        0x10b5fdfff libMRMLCore.dylib (*) &lt;2ce6b680-d7b9-39f1-8d73-4ecdb436c63a&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libMRMLCore.dylib
       0x109c44000 -        0x109cd3fff libvtkAddon.dylib (*) &lt;f82517c6-47b8-39df-bca2-2894053a0366&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libvtkAddon.dylib
       0x11023e000 -        0x111db5fff libvtkITK.dylib (*) &lt;c0eaa78a-2720-38b1-877c-0082a94bc71e&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libvtkITK.dylib
       0x1072de000 -        0x1072e5fff libitkGrowCut-5.4.1.dylib (*) &lt;13ce777b-643b-3050-9227-88af6032ea6f&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libitkGrowCut-5.4.1.dylib
       0x10771e000 -        0x107725fff libITKLabelMap-5.4.1.dylib (*) &lt;6010b114-4bc5-3da0-88dc-71ff73659309&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libITKLabelMap-5.4.1.dylib
       0x107732000 -        0x107739fff libITKMathematicalMorphology-5.4.1.dylib (*) &lt;b1d28ad5-ca20-3c59-9be4-894c2043d090&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libITKMathematicalMorphology-5.4.1.dylib
       0x108315000 -        0x108324fff libITKIOGE-5.4.1.dylib (*) &lt;9f2c99b4-9d03-3b5b-ac77-d306fdd7e9f4&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libITKIOGE-5.4.1.dylib
       0x10833d000 -        0x10834cfff libITKIOIPL-5.4.1.dylib (*) &lt;511daa89-e511-3f4a-9641-78d612e48884&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libITKIOIPL-5.4.1.dylib
       0x10783c000 -        0x107843fff libITKRegionGrowing-5.4.1.dylib (*) &lt;5cf6535b-211c-315e-a95c-015400941867&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libITKRegionGrowing-5.4.1.dylib
       0x108361000 -        0x108368fff libITKVTK-5.4.1.dylib (*) &lt;3bd44021-0697-3c97-9506-d553fc891fc1&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libITKVTK-5.4.1.dylib
       0x107850000 -        0x107857fff libITKDeprecated-5.4.1.dylib (*) &lt;6827495c-2a09-33c5-b083-bc7814d6c416&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libITKDeprecated-5.4.1.dylib
       0x10add9000 -        0x10af3cfff libvtkSegmentationCore.dylib (*) &lt;7cd665ae-61af-3fb2-bdb1-d80e1c6c27af&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libvtkSegmentationCore.dylib
       0x1086fb000 -        0x108722fff libITKIOSpatialObjects-5.4.1.dylib (*) &lt;54f98c6b-7ded-3fe0-9255-d2b9185c34c6&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libITKIOSpatialObjects-5.4.1.dylib
       0x108743000 -        0x108756fff libITKIOXML-5.4.1.dylib (*) &lt;ec3da61c-e1e2-3361-a742-903a82dd0dde&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libITKIOXML-5.4.1.dylib
       0x1086b6000 -        0x1086c5fff libITKFactoryRegistration.dylib (*) &lt;86effdc4-9846-3f76-b78d-9d8240713df4&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libITKFactoryRegistration.dylib
       0x10751a000 -        0x10751dfff libITKSmoothing-5.4.1.dylib (*) &lt;09a4e623-f085-375d-8942-ebdeb5e86926&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libITKSmoothing-5.4.1.dylib
       0x107864000 -        0x10786bfff libITKConvolution-5.4.1.dylib (*) &lt;2ef89346-0ed5-3cc3-a1d8-3fec50a28b36&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libITKConvolution-5.4.1.dylib
       0x109d08000 -        0x109d2ffff libITKSpatialObjects-5.4.1.dylib (*) &lt;b9e097e8-7d42-376e-b80e-ec0aed263074&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libITKSpatialObjects-5.4.1.dylib
       0x108379000 -        0x108380fff libITKMesh-5.4.1.dylib (*) &lt;410d014c-e1c8-3eb7-acec-32c25c0a0a1a&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libITKMesh-5.4.1.dylib
       0x1090fd000 -        0x109110fff libITKStatistics-5.4.1.dylib (*) &lt;316d6ae4-d3ed-344a-bd37-3315ee3f64cc&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libITKStatistics-5.4.1.dylib
       0x1085ad000 -        0x1085b4fff libitkNetlibSlatec-5.4.1.dylib (*) &lt;144a6e92-0606-3e1a-9c26-a2810f536c19&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libitkNetlibSlatec-5.4.1.dylib
       0x10876f000 -        0x10877afff libITKPath-5.4.1.dylib (*) &lt;e8186666-cf45-340e-b01a-2fcc1d62269c&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libITKPath-5.4.1.dylib
       0x10af89000 -        0x10b034fff libITKFFT-5.4.1.dylib (*) &lt;5f9211e2-a39c-33ce-a3db-d10a56ca85c7&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libITKFFT-5.4.1.dylib
       0x109d50000 -        0x109d6ffff libITKIOGDCM-5.4.1.dylib (*) &lt;4ff1c503-cf12-3c3e-9284-ebe8850bcb66&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libITKIOGDCM-5.4.1.dylib
       0x10b967000 -        0x10bac6fff libitkgdcmMSFF-5.4.1.dylib (*) &lt;86cbccc4-23d3-3ed6-9635-2d1e787d7870&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libitkgdcmMSFF-5.4.1.dylib
       0x10b78e000 -        0x10b7f5fff libitkgdcmDICT-5.4.1.dylib (*) &lt;05ea46b0-3d3a-3d82-aebe-64bb9f6fe928&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libitkgdcmDICT-5.4.1.dylib
       0x109125000 -        0x109130fff libitkgdcmIOD-5.4.1.dylib (*) &lt;ddc0a901-7a21-39aa-b7ea-a925b9b4a691&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libitkgdcmIOD-5.4.1.dylib
       0x109a92000 -        0x109ab9fff libITKEXPAT-5.4.1.dylib (*) &lt;8ccc7308-4828-3e64-b0d5-91f62d6410c1&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libITKEXPAT-5.4.1.dylib
       0x109e50000 -        0x109edffff libitkgdcmDSED-5.4.1.dylib (*) &lt;097713cf-20ae-3f8f-8071-89a03192216a&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libitkgdcmDSED-5.4.1.dylib
       0x109141000 -        0x10914cfff libitkgdcmCommon-5.4.1.dylib (*) &lt;1545c27e-6a7a-3dab-9bc9-69594f1ab87a&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libitkgdcmCommon-5.4.1.dylib
       0x109d90000 -        0x109d9bfff libITKIOJPEG-5.4.1.dylib (*) &lt;7bcae7a8-7d4b-3fb9-b585-84c5af8a00dc&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libITKIOJPEG-5.4.1.dylib
       0x109db0000 -        0x109dbbfff libITKIOBMP-5.4.1.dylib (*) &lt;c746b514-fefa-3a39-a4f1-a32b7b81f191&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libITKIOBMP-5.4.1.dylib
       0x109161000 -        0x10916cfff libITKIOLSM-5.4.1.dylib (*) &lt;40106adc-e546-362c-89cf-2edef9cf41bc&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libITKIOLSM-5.4.1.dylib
       0x109dfe000 -        0x109e15fff libITKIOTIFF-5.4.1.dylib (*) &lt;2a1158df-37d0-3775-af24-8fc25402a7a6&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libITKIOTIFF-5.4.1.dylib
       0x109dd0000 -        0x109ddbfff libITKIOPNG-5.4.1.dylib (*) &lt;a151f2a2-8ad3-3a9f-a540-670d51bdfd31&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libITKIOPNG-5.4.1.dylib
       0x109f10000 -        0x109f23fff libITKIOVTK-5.4.1.dylib (*) &lt;cea481ca-6e09-3794-a589-a6c94d718836&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libITKIOVTK-5.4.1.dylib
       0x109e2e000 -        0x109e39fff libITKIOStimulate-5.4.1.dylib (*) &lt;e44f5f9d-27f9-34ce-9777-b5ac8467ee2d&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libITKIOStimulate-5.4.1.dylib
       0x109f38000 -        0x109f43fff libITKIOBioRad-5.4.1.dylib (*) &lt;7c48b376-c966-365c-8b02-d16d016183e4&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libITKIOBioRad-5.4.1.dylib
       0x10b16e000 -        0x10b181fff libITKIOMeta-5.4.1.dylib (*) &lt;dac38185-3cac-3d11-a414-f984d8a8716f&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libITKIOMeta-5.4.1.dylib
       0x10bb47000 -        0x10bbd6fff libITKMetaIO-5.4.1.dylib (*) &lt;63c151d3-3441-3414-8f0e-caf4fa8288b7&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libITKMetaIO-5.4.1.dylib
       0x10b141000 -        0x10b150fff libITKIOMRC-5.4.1.dylib (*) &lt;8a5d2261-0208-3c92-b5f1-4eb57c8be50e&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libITKIOMRC-5.4.1.dylib
       0x10b1d4000 -        0x10b1f3fff libITKIONIFTI-5.4.1.dylib (*) &lt;9e9d3659-620f-323e-9825-04695e144778&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libITKIONIFTI-5.4.1.dylib
       0x10b20c000 -        0x10b21ffff libITKIONRRD-5.4.1.dylib (*) &lt;839faa57-cdcf-3969-a7b3-83e8bbeec5bd&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libITKIONRRD-5.4.1.dylib
       0x10b238000 -        0x10b257fff libITKIOGIPL-5.4.1.dylib (*) &lt;e569298a-6600-37bd-8690-c44fdd2d672c&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libITKIOGIPL-5.4.1.dylib
       0x10b26c000 -        0x10b27ffff libITKIOTransformHDF5-5.4.1.dylib (*) &lt;1cf2019b-c450-3d9b-be32-4050a3c651ca&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libITKIOTransformHDF5-5.4.1.dylib
       0x10b936000 -        0x10b949fff libITKIOTransformInsightLegacy-5.4.1.dylib (*) &lt;a6570b52-0051-3141-bfc8-555a2020472c&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libITKIOTransformInsightLegacy-5.4.1.dylib
       0x10b19e000 -        0x10b1adfff libITKIOTransformMatlab-5.4.1.dylib (*) &lt;3d388fde-410b-3fc5-b854-7e83a084ace4&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libITKIOTransformMatlab-5.4.1.dylib
       0x10bc4a000 -        0x10bc71fff libITKIOTransformBase-5.4.1.dylib (*) &lt;ba9bbfc8-ccc7-351e-b9ed-ad99408282b1&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libITKIOTransformBase-5.4.1.dylib
       0x10d78a000 -        0x10da0dfff libITKTransformFactory-5.4.1.dylib (*) &lt;99ab50f3-d352-3943-a146-8055ce3f8258&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libITKTransformFactory-5.4.1.dylib
       0x1086d2000 -        0x1086d5fff libITKTransform-5.4.1.dylib (*) &lt;2d6721f5-056b-34a1-a2d4-baf3294896b8&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libITKTransform-5.4.1.dylib
       0x10bc92000 -        0x10bcb1fff libitkMGHIO-5.4.1.dylib (*) &lt;6f121a92-3272-36ce-ad79-18a56ced274e&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libitkMGHIO-5.4.1.dylib
       0x10bcc6000 -        0x10bcd9fff libITKIOMINC-5.4.1.dylib (*) &lt;77f30129-5e16-3395-90f6-f02d3858045f&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libITKIOMINC-5.4.1.dylib
       0x10bcf2000 -        0x10bd05fff libitkIOScanco-5.4.1.dylib (*) &lt;643ea0f7-912d-3b11-9333-ef9dee899dd5&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libitkIOScanco-5.4.1.dylib
       0x10bd1a000 -        0x10bd41fff libITKIODCMTK-5.4.1.dylib (*) &lt;0758114a-7bab-3b30-80c1-3fe8b3530004&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libITKIODCMTK-5.4.1.dylib
       0x10bd5e000 -        0x10bd7dfff libITKIOImageBase-5.4.1.dylib (*) &lt;c50c2745-da41-39c1-a6cb-262afdbd9b2f&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libITKIOImageBase-5.4.1.dylib
       0x10bd9a000 -        0x10bdb1fff libi2d.16.dylib (*) &lt;5ce8c742-dad1-3e02-a547-6b4578c07afe&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libi2d.16.dylib
       0x10bdc2000 -        0x10bde9fff libdcmjpeg.16.dylib (*) &lt;fedfbcbc-0603-3620-8e0b-58dd215a951e&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libdcmjpeg.16.dylib
       0x10be06000 -        0x10be35fff libijg8.16.dylib (*) &lt;82280e38-a09e-3e7b-9329-0e38682c5ab3&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libijg8.16.dylib
       0x10be46000 -        0x10be75fff libijg12.16.dylib (*) &lt;0ace1a77-2d65-32ba-bc6a-db313e38ca42&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libijg12.16.dylib
       0x10be86000 -        0x10beb5fff libijg16.16.dylib (*) &lt;50785833-8c73-3cda-b4d3-02d279d4eab0&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libijg16.16.dylib
       0x10bc25000 -        0x10bc34fff libdcmjpls.16.dylib (*) &lt;a0a3c887-cff1-34e0-b3e2-0953e0fc7258&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libdcmjpls.16.dylib
       0x10bf07000 -        0x10bf36fff libdcmtkcharls.16.dylib (*) &lt;f6ed0adf-2648-38b0-8e47-3d9048af47a8&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libdcmtkcharls.16.dylib
       0x10c03f000 -        0x10c0defff libcmr.16.dylib (*) &lt;bd3a17af-fef9-39e2-97de-8fe4030c028a&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libcmr.16.dylib
       0x10bf5b000 -        0x10bf76fff libdcmwlm.16.dylib (*) &lt;846f7294-9ff6-33d5-b897-427a6efadb53&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libdcmwlm.16.dylib
       0x10dbea000 -        0x10dcb9fff libdcmpstat.16.dylib (*) &lt;6c961593-0266-300e-b4da-0d36014304fe&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libdcmpstat.16.dylib
       0x10b298000 -        0x10b29ffff libdcmtls.16.dylib (*) &lt;122e134c-6d60-3954-a30e-f1bf41d5958e&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libdcmtls.16.dylib
       0x10dd02000 -        0x10dd8dfff libdcmsr.16.dylib (*) &lt;62471f9a-aeb1-38d7-a58a-a0963ddbccd6&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libdcmsr.16.dylib
       0x10ddee000 -        0x10de9dfff libdcmimage.16.dylib (*) &lt;7d1fb1cd-6411-38e6-901b-557a0db82b10&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libdcmimage.16.dylib
       0x10721b000 -        0x10721efff libdcmdsig.16.dylib (*) &lt;f0c8e99c-6c7c-3d4d-9714-61e2f1be0513&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libdcmdsig.16.dylib
       0x10bfe2000 -        0x10c021fff libdcmqrdb.16.dylib (*) &lt;63a49165-4a26-3c43-8919-0c4b99b27e54&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libdcmqrdb.16.dylib
       0x10dec6000 -        0x10df71fff libdcmnet.16.dylib (*) &lt;8f393129-1f22-3cb9-86cf-23e2f1ebba99&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libdcmnet.16.dylib
       0x10e657000 -        0x10eab6fff libdcmrt.16.dylib (*) &lt;31976d85-451d-3d33-9e08-8a67680cb936&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libdcmrt.16.dylib
       0x10e201000 -        0x10e414fff libdcmimgle.16.dylib (*) &lt;fff1dd3a-14dd-3e28-bc5d-c612df917f87&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libdcmimgle.16.dylib
       0x10bf8b000 -        0x10bfa6fff libdcmseg.16.dylib (*) &lt;9080b45a-fe04-36c0-99fd-45a5595ad81b&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libdcmseg.16.dylib
       0x10c123000 -        0x10c146fff libdcmtract.16.dylib (*) &lt;20f8f7eb-42ca-3dfa-ba5d-74551da65f45&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libdcmtract.16.dylib
       0x10c15f000 -        0x10c17afff libdcmpmap.16.dylib (*) &lt;8deeebe6-4a83-3df2-aa63-3666718ab40f&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libdcmpmap.16.dylib
       0x10c19f000 -        0x10c1b2fff libdcmect.16.dylib (*) &lt;02ef320c-7854-3b1c-85de-90e0301a75c7&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libdcmect.16.dylib
       0x10dfae000 -        0x10e005fff libdcmfg.16.dylib (*) &lt;e7408db2-5f96-3c33-a4fc-fa58b9a99be4&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libdcmfg.16.dylib
       0x10e03a000 -        0x10e0adfff libdcmiod.16.dylib (*) &lt;e581a990-e53f-3037-8a7e-1531a887eae0&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libdcmiod.16.dylib
       0x10ed03000 -        0x10ee22fff libdcmdata.16.dylib (*) &lt;88187e81-2c2f-3b67-87f6-1c5d71dd8939&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libdcmdata.16.dylib
       0x10e0ee000 -        0x10e125fff liboflog.16.dylib (*) &lt;716e5e92-2ee4-3afd-b9bf-96c7fa01656b&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/liboflog.16.dylib
       0x10c218000 -        0x10c243fff libofstd.16.dylib (*) &lt;84ead16d-d21e-3458-97f7-92049bdc5365&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libofstd.16.dylib
       0x10e455000 -        0x10e4b0fff libvtkTeem.dylib (*) &lt;bd9fc430-7070-31c6-9b87-227799dd6a7b&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/libvtkTeem.dylib
       0x10eefb000 -        0x10ef86fff libITKCommon-5.4.1.dylib (*) &lt;37ba6a6d-cba7-3e6c-ad5c-3164d3491943&gt; /Users/USER/*/Slicer.app/Contents/lib/Slicer-5.7/
</code></pre>

---

## Post #4 by @muratmaga (2024-10-11 00:33 UTC)

<aside class="quote no-group" data-username="doc-xie" data-post="3" data-topic="39628">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/c77e96/48.png" class="avatar"> doc-xie:</div>
<blockquote>
<p><em>/Users/USER/</em>/Slicer.app/Contents/MacOS/Slicer</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="doc-xie" data-post="1" data-topic="39628">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/c77e96/48.png" class="avatar"> doc-xie:</div>
<blockquote>
<h2>Translated Report (Full Report Below)</h2>
<p>Process: Slicer [2273]<br>
Path: /Users/USER/*/Slicer.app/Contents/MacOS/Slicer<br>
Identifier: org.slicer.slicer<br>
Version: (5.7.0-2024-07-20)<br>
Code Type: X86-64 (Native)<br>
Parent Process: launchd [1]<br>
User ID: 501</p>
</blockquote>
</aside>
<p>That path looks suspiciously  wrong is there really a ‘*’ (asterisk) there?</p>

---

## Post #5 by @doc-xie (2024-10-11 00:52 UTC)

<p>Hi,<br>
Maybe the ‘*’ stands for Chinese words. But Slicer can run normally before I installed several modules yesterday. The version of Slicer was 5.7.0 and the software is compatible with Chinese. So I think the reason of crash should be some others.<br>
Thanks.</p>

---

## Post #6 by @muratmaga (2024-10-11 01:05 UTC)

<aside class="quote no-group" data-username="doc-xie" data-post="5" data-topic="39628">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/c77e96/48.png" class="avatar"> doc-xie:</div>
<blockquote>
<p>. But Slicer can run normally before I installed several modules yesterday. The version of Slicer was 5.7.0 and the software is compatible with Chinese.</p>
</blockquote>
</aside>
<p>From this, it is clear that one of the modules have a problem with these chinese characters. To find out which one, you can uninstall them all, add one at a time and find the problematic extension and then report here. Even then it is not clear if it is something fixable because these extensions bring other packages that are not part of Slicer.</p>
<p>Alternatively, you can install in a path that does not have any Chinese characters and all should be good.</p>

---

## Post #7 by @doc-xie (2024-10-11 01:20 UTC)

<p>Hi,<br>
I will try re-install Slicer and modules again.<br>
Thanks a lot.</p>

---

## Post #8 by @lassoan (2024-10-11 12:13 UTC)

<p>It would be useful if you could install the extensions one by one to see which one causes the problem. We can then have a closer look at that extension.</p>

---
