---
topic_id: 28502
title: "Whats Wrong After Upgrading To The New Version Of The Mac Op"
date: 2023-03-21
url: https://discourse.slicer.org/t/28502
---

# What's wrong, after upgrading to the new version of the Mac, opening the Slicer reported '[FD]' error?

**Topic ID**: 28502
**Date**: 2023-03-21
**URL**: https://discourse.slicer.org/t/whats-wrong-after-upgrading-to-the-new-version-of-the-mac-opening-the-slicer-reported-fd-error/28502

---

## Post #1 by @jumbojing (2023-03-21 18:06 UTC)

<p>After upgrading to the new version(13.2.1 (22D68),macOS Ventura) of the Mac, opening the Slicer reported ‘[FD]’ error?</p>
<pre><code class="lang-auto">[DEBUG][Qt] 22.03.2023 01:52:08 [] (unknown:0) - Session start time .......: 2023-03-22 01:52:08
[DEBUG][Qt] 22.03.2023 01:52:08 [] (unknown:0) - Slicer version ...........: 5.2.2 (revision 31382 / fb46bd1) macosx-amd64 - installed release
[DEBUG][Qt] 22.03.2023 01:52:08 [] (unknown:0) - Operating system .........: macOS / 13.2.1 / 22D68 / UTF-8 - 64-bit
[DEBUG][Qt] 22.03.2023 01:52:08 [] (unknown:0) - Memory ...................: 8192 MB physical, 9216 MB virtual
[DEBUG][Qt] 22.03.2023 01:52:08 [] (unknown:0) - CPU ......................: GenuineIntel Intel(R) Core(TM) i5-8279U CPU @ 2.40GHz, 4 cores, 8 logical processors
[DEBUG][Qt] 22.03.2023 01:52:08 [] (unknown:0) - VTK configuration ........: OpenGL2 rendering, Sequential threading
[DEBUG][Qt] 22.03.2023 01:52:08 [] (unknown:0) - Qt configuration .........: version 5.15.2, with SSL, requested OpenGL 3.2 (core profile)
[DEBUG][Qt] 22.03.2023 01:52:08 [] (unknown:0) - Internationalization .....: disabled, language=
[DEBUG][Qt] 22.03.2023 01:52:08 [] (unknown:0) - Developer mode ...........: disabled
[DEBUG][Qt] 22.03.2023 01:52:08 [] (unknown:0) - Application path .........: /Applications/Slicer.app/Contents/MacOS
[DEBUG][Qt] 22.03.2023 01:52:08 [] (unknown:0) - Additional module paths ..: /Users/liguimei/Documents/PTP
[CRITICAL][FD] 22.03.2023 01:52:08 [] (unknown:0) - 1   HIToolbox                           0x00007ff823e30726 _ZN15MenuBarInstance22EnsureAutoShowObserverEv + 102
[CRITICAL][FD] 22.03.2023 01:52:08 [] (unknown:0) - 2   HIToolbox                           0x00007ff823e302b8 _ZN15MenuBarInstance14EnableAutoShowEv + 52
[CRITICAL][FD] 22.03.2023 01:52:08 [] (unknown:0) - 3   HIToolbox                           0x00007ff823dd4908 SetMenuBarObscured + 408
[CRITICAL][FD] 22.03.2023 01:52:08 [] (unknown:0) - 4   HIToolbox                           0x00007ff823dd44ca _ZN13HIApplication15HandleActivatedEP14OpaqueEventRefhP15OpaqueWindowPtrh + 164
[CRITICAL][FD] 22.03.2023 01:52:08 [] (unknown:0) - 5   HIToolbox                           0x00007ff823dce996 _ZN13HIApplication13EventObserverEjP14OpaqueEventRefPv + 252
[CRITICAL][FD] 22.03.2023 01:52:08 [] (unknown:0) - 6   HIToolbox                           0x00007ff823d96bd2 _NotifyEventLoopObservers + 153
[CRITICAL][FD] 22.03.2023 01:52:08 [] (unknown:0) - 7   HIToolbox                           0x00007ff823dce3e6 AcquireEventFromQueue + 494
[CRITICAL][FD] 22.03.2023 01:52:08 [] (unknown:0) - 8   HIToolbox                           0x00007ff823dbd5a4 ReceiveNextEventCommon + 725
[CRITICAL][FD] 22.03.2023 01:52:08 [] (unknown:0) - 9   HIToolbox                           0x00007ff823dbd2b3 _BlockUntilNextEventMatchingListInModeWithFilter + 70
[CRITICAL][FD] 22.03.2023 01:52:08 [] (unknown:0) - 10  AppKit                              0x00007ff81d5c02f3 _DPSNextEvent + 909
[CRITICAL][FD] 22.03.2023 01:52:08 [] (unknown:0) - 11  AppKit                              0x00007ff81d5bf174 -[NSApplication(NSEvent) _nextEventMatchingEventMask:untilDate:inMode:dequeue:] + 1219
[CRITICAL][FD] 22.03.2023 01:52:08 [] (unknown:0) - 12  libqcocoa.dylib                     0x0000000123e312fa qt_plugin_instance + 195738
[CRITICAL][FD] 22.03.2023 01:52:08 [] (unknown:0) - 13  QtCore                              0x000000010f327ec7 _ZN16QCoreApplication13processEventsE6QFlagsIN10QEventLoop17ProcessEventsFlagEE + 39
[CRITICAL][FD] 22.03.2023 01:52:08 [] (unknown:0) - 14  QtWidgets                           0x000000010dac0505 _ZN13QSplashScreen11showMessageERK7QStringiRK6QColor + 133
[CRITICAL][FD] 22.03.2023 01:52:08 [] (unknown:0) - 15  Slicer                              0x000000010c1c6ec9 _ZN24qSlicerApplicationHelper25postInitializeApplicationI20qSlicerAppMainWindowEEiR18qSlicerApplicationR14QScopedPointerI13QSplashScreen21QScopedPointerDeleterIS5_EERS4_IT_S6_ISA_EE + 585
[CRITICAL][FD] 22.03.2023 01:52:08 [] (unknown:0) - 16  Slicer                              0x000000010c1c6990 main + 144
[CRITICAL][FD] 22.03.2023 01:52:08 [] (unknown:0) - 17  dyld                                0x00007ff81a063310 start + 2432
[CRITICAL][Stream] 22.03.2023 01:52:10 [] (unknown:0) - TypeError: Helper() takes no arguments
[CRITICAL][Qt] 22.03.2023 01:52:10 [] (unknown:0) - qSlicerPythonCppAPI::instantiateClass  - [ "Helper" ] - Failed to instantiate scripted pythonqt class "Helper" 0x7fcbca806da0
[CRITICAL][Qt] 22.03.2023 01:52:10 [] (unknown:0) - Fail to instantiate module  "Helper"
[CRITICAL][Stream] 22.03.2023 01:52:10 [] (unknown:0) - RuntimeError: qSlicerScriptedLoadableModule::setPythonSource - Failed to load scripted loadable module: class rotCir was not found in file /Users/liguimei/Documents/PTP/rotCir.py
[CRITICAL][Qt] 22.03.2023 01:52:10 [] (unknown:0) - Fail to instantiate module  "rotCir"
[CRITICAL][Qt] 22.03.2023 01:52:10 [] (unknown:0) - The following modules failed to be instantiated:
[CRITICAL][Qt] 22.03.2023 01:52:10 [] (unknown:0) -    Helper
[CRITICAL][Qt] 22.03.2023 01:52:10 [] (unknown:0) -    rotCir
[DEBUG][Python] 22.03.2023 01:52:11 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.2/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: Annotations
[DEBUG][Python] 22.03.2023 01:52:11 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.2/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 22.03.2023 01:52:11 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.2/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Qt] 22.03.2023 01:52:11 [] (unknown:0) - Switch to module:  "PedicleTrianglePlanner"
[INFO][Python] 22.03.2023 01:52:12 [Python] (/Users/liguimei/Documents/PTP/Helper.py:2231) - 

=======================================
= Welcome to Pedicle Triangle Planner =
=======================================
[WARNING][VTK] 22.03.2023 01:52:12 [vtkMRMLSliceCompositeNode (0x7fcbcbe0fb90)] (/Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLSliceCompositeNode.cxx:301) - SetSliceIntersectionVisibility method is deprecated. Use SetIntersectingSlicesVisibility method of vtkMRMLSliceDisplayNode object instead.
[WARNING][VTK] 22.03.2023 01:52:12 [vtkMRMLSliceCompositeNode (0x7fcbcbf0c850)] (/Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLSliceCompositeNode.cxx:301) - SetSliceIntersectionVisibility method is deprecated. Use SetIntersectingSlicesVisibility method of vtkMRMLSliceDisplayNode object instead.
[WARNING][VTK] 22.03.2023 01:52:12 [vtkMRMLSliceCompositeNode (0x7fcbcc012b00)] (/Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLSliceCompositeNode.cxx:301) - SetSliceIntersectionVisibility method is deprecated. Use SetIntersectingSlicesVisibility method of vtkMRMLSliceDisplayNode object instead.
[INFO][Stream] 22.03.2023 01:52:13 [] (unknown:0) - Loading Slicer RC file [/Users/liguimei/.slicerrc.py]
[INFO][VTK] 22.03.2023 01:52:16 [vtkMRMLVolumeArchetypeStorageNode (0x7fcbcd44a430)] (/Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLVolumeArchetypeStorageNode.cxx:513) - Loaded volume from file: /Users/liguimei/Library/Caches/NA-MIC/Slicer/SlicerIO/__BundleLoadTemp-2023-03-22_015213_611/test/Data/8 Unnamed Series.nrrd. Dimensions: 512x512x623. Number of components: 1. Pixel type: short.
[DEBUG][Qt] 22.03.2023 01:52:16 [] (unknown:0) - "MRB Slicer Data Bundle" Reader has successfully read the file "/Users/liguimei/Documents/PTP/Resources/test.mrb" "[3.51s]"
[DEBUG][Qt] 22.03.2023 01:54:00 [] (unknown:0) - Python console user input: Helper.p2pexLine([0,0,0],[20,30,50],'L')
[INFO][Stream] 22.03.2023 01:54:00 [] (unknown:0) - (array([39.46657054, 59.1998558 , 98.66642634]), array([0.32444284, 0.48666426, 0.81110711]), &lt;function Helper.p2pexLine.&lt;locals&gt;.&lt;lambda&gt; at 0x1635ff310&gt;, None)
[DEBUG][Qt] 22.03.2023 01:54:24 [] (unknown:0) - Switch to module:  "Data"
</code></pre>
<p>Symptom 1: Unable to instantiate extensions in the console</p>

---

## Post #2 by @lassoan (2023-03-21 20:43 UTC)

<p>This seems to be a known macOS Ventura bug - see <a href="https://stackoverflow.com/questions/75430926/r-warning-message-1-hitoolbox-0x00007ff80a4fc726-zn15menubarinstance22ensureau" class="inline-onebox">rstudio - R warning message [1 HIToolbox 0x00007ff80a4fc726 _ZN15MenuBarInstance22EnsureAutoShowObserverEv + 102] - Stack Overflow</a></p>
<p>You can probably ignore it, Apple should fix it soon.</p>
<p>Errors related to <code>Helper</code> and <code>rotCir</code> are because you added Python files to “additional module paths” folders in Slicer. All .py files in these folders must be Slicer Python scripted modules. All other .py files can go into subfolders.</p>

---
