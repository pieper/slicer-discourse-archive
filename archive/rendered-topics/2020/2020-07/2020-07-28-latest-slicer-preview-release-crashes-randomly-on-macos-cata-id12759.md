---
topic_id: 12759
title: "Latest Slicer Preview Release Crashes Randomly On Macos Cata"
date: 2020-07-28
url: https://discourse.slicer.org/t/12759
---

# Latest Slicer Preview Release crashes randomly on macOS Catalina

**Topic ID**: 12759
**Date**: 2020-07-28
**URL**: https://discourse.slicer.org/t/latest-slicer-preview-release-crashes-randomly-on-macos-catalina/12759

---

## Post #1 by @Fernando (2020-07-28 18:42 UTC)

<p>Unfortunately, I can’t consistently reproduce this, but in the last couple of weeks Slicer has crashed many times. Today it’s happened when playing with the threshold in the <code>Volumes</code> module, but I’m not sure it’s related to that. I think the message in the shell is always the same, however, or very similar:</p>
<pre><code class="lang-auto">Assertion `this-&gt;Table-&gt;rowHeight(i) == newHeight` failed in  /Volumes/D/P/S-0-build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253
Assertion `this-&gt;Table-&gt;rowHeight(i) == newHeight` failed in  /Volumes/D/P/S-0-build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253
Assertion `this-&gt;Table-&gt;rowHeight(i) == newHeight` failed in  /Volumes/D/P/S-0-build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253
Assertion `this-&gt;Table-&gt;rowHeight(i) == newHeight` failed in  /Volumes/D/P/S-0-build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253
Assertion `this-&gt;Table-&gt;rowHeight(i) == newHeight` failed in  /Volumes/D/P/S-0-build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253
Assertion `this-&gt;Table-&gt;rowHeight(i) == newHeight` failed in  /Volumes/D/P/S-0-build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253
Assertion `this-&gt;Table-&gt;rowHeight(i) == newHeight` failed in  /Volumes/D/P/S-0-build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253
Assertion `this-&gt;Table-&gt;rowHeight(i) == newHeight` failed in  /Volumes/D/P/S-0-build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253
Assertion `this-&gt;Table-&gt;rowHeight(i) == newHeight` failed in  /Volumes/D/P/S-0-build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253
Assertion `this-&gt;Table-&gt;rowHeight(i) == newHeight` failed in  /Volumes/D/P/S-0-build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253
Assertion `this-&gt;Table-&gt;rowHeight(i) == newHeight` failed in  /Volumes/D/P/S-0-build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253
Failed to lock QIOSurfaceGraphicsBuffer(0x7fea4769d100, surface=0x0, size=QSize(1022, 0), isLocked=false, isInUse=false) -536870206
[1]    46337 illegal hardware instruction  /Applications/Slicer.app/Contents/MacOS/Slicer
</code></pre>
<p>I hope others have faced the same issue, and that the developers can get an idea of where the issue might be coming from. Let me know if there’s anything else I can do to help.</p>
<p>I’m using today’s preview on macOS Catalina <code>10.15.5</code>.</p>

---

## Post #2 by @lassoan (2020-07-28 19:20 UTC)

<p>Thanks for letting us know. Have you built Slicer yourself or you use an official build? Which Slicer version is this? Has this version worked robustly before? Have you installed any extensions or added any modules? Do the two last lines (“Failed to lock QIOSurfaceGraphicsBuffer…” and “illegal hardware instruction”) appear right before the application crashes?</p>

---

## Post #3 by @Fernando (2020-07-28 19:59 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="12759">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Have you built Slicer yourself or you use an official build?</p>
</blockquote>
</aside>
<p>Official build.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="12759">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Which Slicer version is this?</p>
</blockquote>
</aside>
<p>Today’s preview, i.e. <code>4.11.0-2020-07-27 r29229 / 1217275</code>. It has happened with other versions, I think all in this month.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="12759">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Has this version worked robustly before?</p>
</blockquote>
</aside>
<p>I update Slicer often, so it’s hard to know.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="12759">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Have you installed any extensions or added any modules?</p>
</blockquote>
</aside>
<p>I add a couple of modules and so some other stuff in my <code>.slicerrc.py</code>, but I haven’t touched it in months.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="12759">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Do the two last lines (“Failed to lock QIOSurfaceGraphicsBuffer…” and “illegal hardware instruction”) appear right before the application crashes?</p>
</blockquote>
</aside>
<p>I don’t know, I see them in the console after Slicer crashes, so that seems to be the case.</p>

---

## Post #4 by @lassoan (2020-07-28 20:07 UTC)

<p><a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> Have we ended up updating Qt version on Mac when we updated it on other platforms?</p>

---

## Post #5 by @jamesobutler (2020-07-29 01:08 UTC)

<p>Looks like it is hitting the same assert that was crashing QtDesigner previously (See <a href="https://github.com/commontk/CTK/commit/0e1d94593d900fd144f50af38e3240063ab30484#diff-6f073d1f96143635788f382f18279749" rel="nofollow noopener">https://github.com/commontk/CTK/commit/0e1d94593d900fd144f50af38e3240063ab30484#diff-6f073d1f96143635788f382f18279749</a>)</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> Yes, the macOS nightly build is using Qt 5.15.0 which was done around the same time as the Windows upgrade.</p>

---

## Post #6 by @lassoan (2020-07-29 01:22 UTC)

<aside class="quote no-group quote-modified" data-username="jamesobutler" data-post="5" data-topic="12759">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Looks like it is hitting the same assert that was crashing QtDesigner previously (See <a href="https://github.com/commontk/CTK/commit/0e1d94593d900fd144f50af38e3240063ab30484#diff-6f073d1f96143635788f382f18279749" class="inline-onebox">Fix QtDesigner crash in debug mode · commontk/CTK@0e1d945 · GitHub</a>)</p>
</blockquote>
</aside>
<p>First I thought so, too, but it is not a debug-mode build, so assert does not cause crash.</p>

---

## Post #7 by @pieper (2020-07-31 18:54 UTC)

<p>I got this message and crash today too with a local debug build of slicer on mac with Qt 5.15.  Nothing about illegal hardware instruction though.</p>
<pre><code class="lang-auto">Switch to module:  "Volumes"
Failed to lock QIOSurfaceGraphicsBuffer(0x7fbc063721a0, surface=0x0, size=QSize(484, 0), isLocked=false, isInUse=false) -536870206
error: [/opt/s/Slicer-build/bin/Slicer.app/Contents/MacOS/./Slicer] exit abnormally - Report the problem.
</code></pre>

---

## Post #8 by @lassoan (2020-07-31 19:05 UTC)

<aside class="quote no-group" data-username="pieper" data-post="7" data-topic="12759">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p><code>Failed to lock QIOSurfaceGraphicsBuffer</code></p>
</blockquote>
</aside>
<p>Is there a chance you can get a stack trace?</p>

---

## Post #9 by @pieper (2020-07-31 20:09 UTC)

<p>I did, but it wan’t informative.  I’ll share it next time it happens.</p>

---

## Post #10 by @Fernando (2020-08-05 18:08 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="12759">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Is there a chance you can get a stack trace?</p>
</blockquote>
</aside>
<p>Does this help?<br>
<a href="https://gist.github.com/fepegar/131d0562088550e9fd8ecba7f4436005" class="onebox" target="_blank" rel="noopener nofollow ugc">https://gist.github.com/fepegar/131d0562088550e9fd8ecba7f4436005</a></p>

---

## Post #11 by @pieper (2020-08-05 18:20 UTC)

<p>That looks like what I’ve been seeing.   Something between Qt and macOS.</p>

---

## Post #12 by @lassoan (2020-08-06 03:45 UTC)

<p>Thank you <a class="mention" href="/u/fernando">@Fernando</a>, this is very useful. In this stack trace the crash is triggered by <code>ctkBasePopupWidget::setEffectGeometry(QRect)</code> making a widget visible.</p>
<p>I did some web search for Qt crashes on MacOS Catalina and there were just a few that were vaguely similar, so most probably it is also something special about how Qt is used - most probably something in VTK but maybe in CTK.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> do you know if Paraview started to use Qt-5.15 yet?</p>

---

## Post #13 by @lassoan (2020-08-06 03:46 UTC)

<p>Similar issue reported by another user:</p>
<blockquote>
<p>I am experiencing a similar problem. My 3D Slicer didn’t crash until I returned to it after some time (I was working inside google docs for approx. 30minutes). I am not 100% certain, but I think it happened when clicking into the scene after returning.</p>
<p>Looks like an OpenGL/VTK issue to me. Here the Stack Trace:<br>
<a href="https://gist.github.com/che85/f050d34b59ba7bf4463dc849b1f89723" class="inline-onebox">Slicer_crash_08_04_2020 · GitHub</a></p>
</blockquote>

---

## Post #14 by @lassoan (2020-08-06 03:55 UTC)

<p>Another occurrence reported by a user, just after starting Slicer, he started screen recording, then moved the Slicer application window a bit, then when the mouse was moved over the top-left corner of the 3D view, Slicer crashed. Probably it went over the push-pin icon.</p>
<details>
<summary>
Slicer application log</summary>
<pre><code class="lang-auto">##[DEBUG][Qt] 05.08.2020 11:40:01 [] (unknown:0) - Session start time .......: 2020-08-05 11:40:01
[DEBUG][Qt] 05.08.2020 11:40:01 [] (unknown:0) - Slicer version ...........: 4.11.0-2020-08-02 (revision 29250 / 1a8a340) macosx-amd64 - installed release
[DEBUG][Qt] 05.08.2020 11:40:01 [] (unknown:0) - Operating system .........: Mac OS X / 10.15.5 / 19F101 - 64-bit
[DEBUG][Qt] 05.08.2020 11:40:01 [] (unknown:0) - Memory ...................: 32768 MB physical, 2048 MB virtual
[DEBUG][Qt] 05.08.2020 11:40:01 [] (unknown:0) - CPU ......................: GenuineIntel Intel(R) Core(TM) i9-9880H CPU @ 2.30GHz, 8 cores, 16 logical processors
[DEBUG][Qt] 05.08.2020 11:40:01 [] (unknown:0) - VTK configuration ........: OpenGL2 rendering, Sequential threading
[DEBUG][Qt] 05.08.2020 11:40:01 [] (unknown:0) - Qt configuration .........: version 5.15.0, with SSL, requested OpenGL 3.2 (core profile)
[DEBUG][Qt] 05.08.2020 11:40:01 [] (unknown:0) - Developer mode enabled ...: no
[DEBUG][Qt] 05.08.2020 11:40:01 [] (unknown:0) - Prefer executable CLI ....: yes
[DEBUG][Qt] 05.08.2020 11:40:01 [] (unknown:0) - Application path .........: /Applications/Slicer 5.app/Contents/MacOS
[DEBUG][Qt] 05.08.2020 11:40:01 [] (unknown:0) - Additional module paths ..: /Users/cianciulla/sources/SlicerHeart/CardiacDeviceSimulator, /Users/cianciulla/sources/SlicerHeart/Philips4dUsDicomPatcher, /Users/cianciulla/sources/SlicerHeartCollaborators/LeafletAnalysis, /Users/cianciulla/sources/SlicerHeartCollaborators/ValveAnnulusAnalysis, /Users/cianciulla/sources/SlicerHeartCollaborators/ValveQuantification, /Users/cianciulla/sources/SlicerHeartCollaborators/ValveSegmentation, /Users/cianciulla/sources/SlicerHeartPrivate/BafflePlanner, /Users/cianciulla/sources/SlicerHeartPrivate/CardiacDeviceSimulatorExtender, /Users/cianciulla/sources/SlicerHeartPrivate/CrossSectionAnalyzer, /Users/cianciulla/sources/SlicerHeartPrivate/EchoVolumeRender, /Users/cianciulla/sources/SlicerHeartPrivate/LeafletEditorTest, /Users/cianciulla/sources/SlicerHeartPrivate/LeafletMoldGenerator, /Users/cianciulla/sources/SlicerHeartPrivate/MitraClipDeviceSimulator, /Users/cianciulla/sources/SlicerHeartPrivate/TranscatheterDeviceSimulator, /Users/cianciulla/sources/SlicerHeartPrivate/ValveBatchExport, /Users/cianciulla/sources/SlicerHeartPrivate/ValveFemExport, /Users/cianciulla/sources/SlicerHeartPrivate/ValvePapillaryAnalysis, /Users/cianciulla/sources/SlicerHeartPrivate/ValveQuantificationExtender, /Applications/Slicer 5.app/Contents/Extensions-29250/MarkupsToModel/lib/Slicer-4.11/qt-loadable-modules, /Applications/Slicer 5.app/Contents/Extensions-29250/SlicerHeart/lib/Slicer-4.11/cli-modules, /Applications/Slicer 5.app/Contents/Extensions-29250/SlicerHeart/lib/Slicer-4.11/qt-loadable-modules, /Applications/Slicer 5.app/Contents/Extensions-29250/SlicerHeart/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer 5.app/Contents/Extensions-29250/SlicerIGT/lib/Slicer-4.11/qt-loadable-modules, /Applications/Slicer 5.app/Contents/Extensions-29250/SlicerIGT/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer 5.app/Contents/Extensions-29250/SlicerOpenIGTLink/lib/Slicer-4.11/qt-loadable-modules, /Applications/Slicer 5.app/Contents/Extensions-29250/SlicerOpenIGTLink/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer 5.app/Contents/Extensions-29250/VolumeClip/lib/Slicer-4.11/qt-scripted-modules
[DEBUG][Python] 05.08.2020 11:40:02 [Python] (/Applications/Slicer 5.app/Contents/lib/Python/lib/python3.6/site-packages/pydicom/datadict.py:432) - Reversing DICOM dictionary so can look up tag from a keyword...
[DEBUG][Python] 05.08.2020 11:40:03 [Python] (/Applications/Slicer 5.app/Contents/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations
[DEBUG][Python] 05.08.2020 11:40:04 [Python] (/Applications/Slicer 5.app/Contents/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 05.08.2020 11:40:04 [Python] (/Applications/Slicer 5.app/Contents/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Python] 05.08.2020 11:40:05 [Python] (/Users/cianciulla/sources/SlicerHeartCollaborators/ValveAnnulusAnalysis/HeartValveLib/HeartValves.py:407) - updateLegacyHeartValveNodes
[DEBUG][Python] 05.08.2020 11:40:05 [Python] (/Users/cianciulla/sources/SlicerHeartCollaborators/ValveAnnulusAnalysis/HeartValveLib/HeartValves.py:25) - Added scene end import observer for HeartValves
[DEBUG][Python] 05.08.2020 11:40:05 [Python] (/Applications/Slicer 5.app/Contents/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: HeartValves
[DEBUG][Qt] 05.08.2020 11:40:04 [] (unknown:0) - Switch to module:  "Welcome"
[INFO][VTK] 05.08.2020 11:40:05 [vtkMRMLVolumeArchetypeStorageNode (0x7f83fcce1a20)] (/Volumes/D/P/S-0/Libs/MRML/Core/vtkMRMLVolumeArchetypeStorageNode.cxx:470) - Loaded volume from file: /Users/cianciulla/sources/SlicerHeartCollaborators/ValveAnnulusAnalysis/Resources/VrPresets/US-Red-Tinge.png. Dimensions: 65x50x1. Number of components: 4. Pixel type: unsigned char.
[INFO][VTK] 05.08.2020 11:40:05 [vtkMRMLVolumeArchetypeStorageNode (0x7f83fcce1da0)] (/Volumes/D/P/S-0/Libs/MRML/Core/vtkMRMLVolumeArchetypeStorageNode.cxx:470) - Loaded volume from file: /Users/cianciulla/sources/SlicerHeartCollaborators/ValveAnnulusAnalysis/Resources/VrPresets/US-Red.png. Dimensions: 65x50x1. Number of components: 4. Pixel type: unsigned char.
[INFO][VTK] 05.08.2020 11:40:05 [vtkMRMLVolumeArchetypeStorageNode (0x7f83fcce1fa0)] (/Volumes/D/P/S-0/Libs/MRML/Core/vtkMRMLVolumeArchetypeStorageNode.cxx:470) - Loaded volume from file: /Users/cianciulla/sources/SlicerHeartCollaborators/ValveAnnulusAnalysis/Resources/VrPresets/US-Ocean.png. Dimensions: 65x50x1. Number of components: 4. Pixel type: unsigned char.
[INFO][VTK] 05.08.2020 11:40:05 [vtkMRMLVolumeArchetypeStorageNode (0x7f83fcce21a0)] (/Volumes/D/P/S-0/Libs/MRML/Core/vtkMRMLVolumeArchetypeStorageNode.cxx:470) - Loaded volume from file: /Users/cianciulla/sources/SlicerHeartCollaborators/ValveAnnulusAnalysis/Resources/VrPresets/US-Grey.png. Dimensions: 65x50x1. Number of components: 4. Pixel type: unsigned char.
[INFO][VTK] 05.08.2020 11:40:05 [vtkMRMLVolumeArchetypeStorageNode (0x7f83fcce23a0)] (/Volumes/D/P/S-0/Libs/MRML/Core/vtkMRMLVolumeArchetypeStorageNode.cxx:470) - Loaded volume from file: /Users/cianciulla/sources/SlicerHeartCollaborators/ValveAnnulusAnalysis/Resources/VrPresets/US-Silver.png. Dimensions: 65x50x1. Number of components: 4. Pixel type: unsigned char.
[INFO][VTK] 05.08.2020 11:40:05 [vtkMRMLVolumeArchetypeStorageNode (0x7f83fcce25a0)] (/Volumes/D/P/S-0/Libs/MRML/Core/vtkMRMLVolumeArchetypeStorageNode.cxx:470) - Loaded volume from file: /Users/cianciulla/sources/SlicerHeartCollaborators/ValveAnnulusAnalysis/Resources/VrPresets/US-Green.png. Dimensions: 65x50x1. Number of components: 4. Pixel type: unsigned char.
[INFO][VTK] 05.08.2020 11:40:05 [vtkMRMLVolumeArchetypeStorageNode (0x7f83fcce27a0)] (/Volumes/D/P/S-0/Libs/MRML/Core/vtkMRMLVolumeArchetypeStorageNode.cxx:470) - Loaded volume from file: /Users/cianciulla/sources/SlicerHeartCollaborators/ValveAnnulusAnalysis/Resources/VrPresets/US-InverseGreen.png. Dimensions: 65x50x1. Number of components: 3. Pixel type: unsigned char.
[INFO][VTK] 05.08.2020 11:40:05 [vtkMRMLVolumeArchetypeStorageNode (0x7f83fcce29a0)] (/Volumes/D/P/S-0/Libs/MRML/Core/vtkMRMLVolumeArchetypeStorageNode.cxx:470) - Loaded volume from file: /Users/cianciulla/sources/SlicerHeartCollaborators/ValveAnnulusAnalysis/Resources/VrPresets/CT-EndoVascular.png. Dimensions: 65x50x1. Number of components: 3. Pixel type: unsigned char.
[WARNING][Qt] 05.08.2020 11:40:31 [] (unknown:0) - Tried to flush backingstore without painting to it first
</code></pre>
</details>

---

## Post #15 by @pieper (2020-08-06 21:01 UTC)

<p>I just got another crash with a stack trace like <a class="mention" href="/u/fernando">@Fernando</a>’s.  I believe the cursor just brushed over the pin icon.</p>
<p>It looks like it is the <code>QAnimation</code> used by <code>ctkPopupWidget</code>.  Maybe the exit event happens and the widget is deleted before the animation gets started or something like that.</p>
<p>Perhaps the easiest would be to turn off that animation feature and just have popup appear and disappear instantly.  I personally wouldn’t miss the animation and would prefer a more stable application.</p>
<pre><code class="lang-auto">Process:               Slicer [44397]
Path:                  /Applications/Slicer.app/Contents/MacOS/Slicer
Identifier:            ???
Version:               ??? (4.11.0-2020-07-24)
Code Type:             X86-64 (Native)
Parent Process:        ??? [44396]
Responsible:           Terminal [349]
User ID:               501

Date/Time:             2020-08-06 16:52:56.791 -0400
OS Version:            Mac OS X 10.15.6 (19G73)
Report Version:        12
Bridge OS Version:     4.6 (17P6065)
Anonymous UUID:        3797FBED-83D2-B47D-D4EA-26F22AA011DE


Time Awake Since Boot: 690000 seconds

System Integrity Protection: enabled

Crashed Thread:        0  Dispatch queue: com.apple.main-thread

Exception Type:        EXC_BAD_INSTRUCTION (SIGILL)
Exception Codes:       0x0000000000000001, 0x0000000000000000
Exception Note:        EXC_CORPSE_NOTIFY

Termination Signal:    Illegal instruction: 4
Termination Reason:    Namespace SIGNAL, Code 0x4
Terminating Process:   exc handler [44397]

Application Specific Information:
*** CFRetain() called with NULL ***

Thread 0 Crashed:: Dispatch queue: com.apple.main-thread
0   com.apple.CoreFoundation      	0x00007fff39b4398f CFRetain.cold.1 + 14
1   com.apple.CoreFoundation      	0x00007fff39996a08 CFRetain + 109
2   libqcocoa.dylib               	0x000000012277d487 0x122764000 + 103559
3   libqcocoa.dylib               	0x000000012277d5a1 0x122764000 + 103841
4   org.qt-project.QtGui          	0x0000000103d61f50 QBackingStore::beginPaint(QRegion const&amp;) + 208
5   org.qt-project.QtWidgets      	0x00000001035ec5e4 0x1035ce000 + 124388
6   org.qt-project.QtWidgets      	0x00000001035ead45 0x1035ce000 + 118085
7   org.qt-project.QtWidgets      	0x000000010363a404 0x1035ce000 + 443396
8   org.qt-project.QtWidgets      	0x00000001036373fd 0x1035ce000 + 431101
9   org.qt-project.QtWidgets      	0x00000001035df01a QApplicationPrivate::notify_helper(QObject*, QEvent*) + 266
10  org.qt-project.QtWidgets      	0x00000001035e04a6 QApplication::notify(QObject*, QEvent*) + 598
11  libqSlicerBaseQTGUI.dylib     	0x00000001027e1f75 qSlicerApplication::notify(QObject*, QEvent*) + 21
12  org.qt-project.QtCore         	0x0000000104374cf4 QCoreApplication::notifyInternal2(QObject*, QEvent*) + 212
13  org.qt-project.QtGui          	0x0000000103bb8a82 QGuiApplicationPrivate::processExposeEvent(QWindowSystemInterfacePrivate::ExposeEvent*) + 306
14  org.qt-project.QtGui          	0x0000000103b94d83 bool QWindowSystemInterfacePrivate::handleWindowSystemEvent&lt;QWindowSystemInterface::SynchronousDelivery&gt;(QWindowSystemInterfacePrivate::WindowSystemEvent*) + 115
15  org.qt-project.QtGui          	0x0000000103b9c442 void QWindowSystemInterface::handleExposeEvent&lt;QWindowSystemInterface::SynchronousDelivery&gt;(QWindow*, QRegion const&amp;) + 178
16  libqcocoa.dylib               	0x0000000122785fbc 0x122764000 + 139196
17  libqcocoa.dylib               	0x000000012278e7bb 0x122764000 + 174011
18  com.apple.QuartzCore          	0x00007fff4550853c -[CALayer display] + 180
19  com.apple.AppKit              	0x00007fff36e1069a -[_NSBackingLayer display] + 537
20  com.apple.AppKit              	0x00007fff36d72187 -[_NSViewBackingLayer display] + 800
21  com.apple.QuartzCore          	0x00007fff45507e09 CA::Layer::display_if_needed(CA::Transaction*) + 757
22  com.apple.QuartzCore          	0x00007fff454e6106 CA::Context::commit_transaction(CA::Transaction*, double) + 334
23  com.apple.QuartzCore          	0x00007fff454e4cf0 CA::Transaction::commit() + 644
24  com.apple.AppKit              	0x00007fff370dcaeb -[_NSOrderOutAnimationProxyWindow initWithSnapshotOfWindow:] + 50
25  com.apple.AppKit              	0x00007fff36f2b5a1 -[_NSWindowTransformAnimation initWithWindow:type:interruptingAnimation:] + 702
26  com.apple.AppKit              	0x00007fff36f2b2cf +[_NSWindowTransformAnimation windowTransformAnimationWithWindow:type:interruptingAnimation:] + 49
27  com.apple.AppKit              	0x00007fff36de507f -[NSWindow _doOrderWindow:relativeTo:findKey:forCounter:force:isModal:] + 614
28  com.apple.AppKit              	0x00007fff36de4db7 -[NSWindow orderWindow:relativeTo:] + 155
29  libqcocoa.dylib               	0x000000012278201a 0x122764000 + 122906
30  org.qt-project.QtGui          	0x0000000103bbf948 QWindowPrivate::setVisible(bool) + 1112
31  org.qt-project.QtWidgets      	0x0000000103617055 QWidgetPrivate::hide_sys() + 229
32  org.qt-project.QtWidgets      	0x0000000103616711 QWidgetPrivate::setGeometry_sys(int, int, int, int, bool) + 945
33  org.qt-project.QtWidgets      	0x0000000103616ec8 QWidget::setGeometry(QRect const&amp;) + 264
34  libCTKWidgets.0.1.dylib       	0x0000000102e56452 ctkBasePopupWidget::setEffectGeometry(QRect) + 34
35  libCTKWidgets.0.1.dylib       	0x0000000102ef0ee7 ctkBasePopupWidget::qt_metacall(QMetaObject::Call, int, void**) + 71
36  libCTKWidgets.0.1.dylib       	0x0000000102efe258 ctkPopupWidget::qt_metacall(QMetaObject::Call, int, void**) + 24
37  org.qt-project.QtCore         	0x000000010418acff 0x10417d000 + 56575
38  org.qt-project.QtCore         	0x000000010418783a 0x10417d000 + 43066
39  org.qt-project.QtCore         	0x0000000104187679 0x10417d000 + 42617
40  org.qt-project.QtCore         	0x0000000104183e89 QAbstractAnimation::setCurrentTime(int) + 297
41  org.qt-project.QtCore         	0x0000000104183d06 0x10417d000 + 27910
42  org.qt-project.QtCore         	0x0000000104182488 QUnifiedTimer::updateAnimationTimers(long long) + 328
43  org.qt-project.QtCore         	0x0000000104184ea6 QAnimationDriver::advance() + 38
44  org.qt-project.QtCore         	0x000000010439fb3f QObject::event(QEvent*) + 111
45  org.qt-project.QtWidgets      	0x00000001035df01a QApplicationPrivate::notify_helper(QObject*, QEvent*) + 266
46  org.qt-project.QtWidgets      	0x00000001035e04a6 QApplication::notify(QObject*, QEvent*) + 598
47  libqSlicerBaseQTGUI.dylib     	0x00000001027e1f75 qSlicerApplication::notify(QObject*, QEvent*) + 21
48  org.qt-project.QtCore         	0x0000000104374cf4 QCoreApplication::notifyInternal2(QObject*, QEvent*) + 212
49  org.qt-project.QtCore         	0x00000001043da24f QTimerInfoList::activateTimers() + 991
50  libqcocoa.dylib               	0x000000012279c4a2 0x122764000 + 230562
51  com.apple.CoreFoundation      	0x00007fff39a16d52 __CFRUNLOOP_IS_CALLING_OUT_TO_A_SOURCE0_PERFORM_FUNCTION__ + 17
52  com.apple.CoreFoundation      	0x00007fff39a16cf1 __CFRunLoopDoSource0 + 103
53  com.apple.CoreFoundation      	0x00007fff39a16b0b __CFRunLoopDoSources0 + 209
54  com.apple.CoreFoundation      	0x00007fff39a1583a __CFRunLoopRun + 927
55  com.apple.CoreFoundation      	0x00007fff39a14e3e CFRunLoopRunSpecific + 462
56  com.apple.HIToolbox           	0x00007fff38641abd RunCurrentEventLoopInMode + 292
57  com.apple.HIToolbox           	0x00007fff386417d5 ReceiveNextEventCommon + 584
58  com.apple.HIToolbox           	0x00007fff38641579 _BlockUntilNextEventMatchingListInModeWithFilter + 64
59  com.apple.AppKit              	0x00007fff36c87039 _DPSNextEvent + 883
60  com.apple.AppKit              	0x00007fff36c85880 -[NSApplication(NSEvent) _nextEventMatchingEventMask:untilDate:inMode:dequeue:] + 1352
61  com.apple.AppKit              	0x00007fff36c7758e -[NSApplication run] + 658
62  libqcocoa.dylib               	0x000000012279d1df 0x122764000 + 233951
63  org.qt-project.QtCore         	0x0000000104370d9f QEventLoop::exec(QFlags&lt;QEventLoop::ProcessEventsFlag&gt;) + 431
64  org.qt-project.QtCore         	0x0000000104375302 QCoreApplication::exec() + 130
65  libqSlicerBaseQTCore.dylib    	0x00000001030f8079 qSlicerCoreApplication::exec() + 9
66                                	0x0000000102461423 main + 483
67  libdyld.dylib                 	0x00007fff738e8cc9 start + 1
</code></pre>

---

## Post #16 by @lassoan (2020-08-07 03:11 UTC)

<p>Yes, that animation is not very useful and slownthings down, so I would not mind disabling it.</p>
<p>The popup window of slider widget in Volumes module caused crash, too.</p>

---

## Post #17 by @lassoan (2020-08-11 01:47 UTC)

<p>We have fixed the issue (<a href="https://github.com/Slicer/Slicer/issues/5092">https://github.com/Slicer/Slicer/issues/5092</a>), no crash should occur in Slicer Preview Releases downloaded 2020-08-11 or later. Let us know if you still experience similar problems.</p>
<p>I’ve also shortened the animation duration to 10% of the original, so popup windows appear immediately now.</p>

---
