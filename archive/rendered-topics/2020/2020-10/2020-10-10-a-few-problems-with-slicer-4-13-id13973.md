---
topic_id: 13973
title: "A Few Problems With Slicer 4 13"
date: 2020-10-10
url: https://discourse.slicer.org/t/13973
---

# A few problems with Slicer 4.13

**Topic ID**: 13973
**Date**: 2020-10-10
**URL**: https://discourse.slicer.org/t/a-few-problems-with-slicer-4-13/13973

---

## Post #1 by @chir.set (2020-10-10 14:17 UTC)

<p>I know you are in a big process of upgrading Slicer with VTK9 in particular, and some runtime problems can be expected. Just reporting what I found so far on Arch Linux / Qt 5.15.1.</p>
<p>Factory built Slicer</p>
<ol>
<li>
<p>Only Slicer appearence themes are proposed in Application Settings, and not system themes like Breeze and Oxygen.</p>
</li>
<li>
<p>2D slice views are black empty.</p>
</li>
</ol>
<p>Home built Slicer</p>
<ol>
<li>
<p>2D slice views are black empty.</p>
</li>
<li>
<p>Rotating 3D view with left mouse button down changes window state from maximized to ‘restored’ without rotating the view. When left mouse button is released, moving around the mouse rotates the view. Please see <a href="https://yadi.sk/i/gy3Iu-Z6JfrhvQ" rel="noopener nofollow ugc">attached</a> screen capture.</p>
</li>
</ol>
<p>In both cases, no particular error messages are in console or python console. In case it might be useful :</p>
<pre><code>Session start time .......: 2020-10-10 15:47:57
Slicer version ...........: 4.13.0-2020-10-09 (revision 29425 / 5da4da2) linux-amd64 - installed release
Operating system .........: Linux / 5.9.0-rc7-git / #161 SMP Sun Oct 4 10:49:07 CEST 2020 - 64-bit
Memory ...................: 15018 MB physical, 15359 MB virtual
CPU ......................: AuthenticAMD AMD Ryzen 5 2500U with Radeon Vega Mobile Gfx, 4 cores, 8 logical processors
VTK configuration ........: OpenGL2 rendering, Sequential threading
Qt configuration .........: version 5.15.1, with SSL, requested OpenGL 3.2 (core profile)
Developer mode enabled ...: yes
Prefer executable CLI ....: no
Application path .........: /home/user/programs/Slicer-4.13.0-2020-10-09-linux-amd64/bin
Additional module paths ..: (none)
Reversing DICOM dictionary so can look up tag from a keyword...
Scripted subject hierarchy plugin registered: Annotations
Scripted subject hierarchy plugin registered: SegmentEditor
DeserializeTerminologyEntry: Invalid type component
Scripted subject hierarchy plugin registered: SegmentStatistics
Switch to module:  "Volumes"
Assertion `this-&gt;Table-&gt;columnWidth(j) == newWidth` failed in  /home/arc/src/Slicer-SuperBuild/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  242
Assertion `this-&gt;Table-&gt;columnWidth(j) == newWidth` failed in  /home/arc/src/Slicer-SuperBuild/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  242
...
Loading Slicer RC file [/home/user/.slicerrc.py]
Loaded volume from file: /home/user/Desktop/BIG/Slicer/CTA-cardio.nrrd. Dimensions: 512x512x321. Number of components: 1. Pixel type: short.
"Volume" Reader has successfully read the file "/home/user/Desktop/BIG/Slicer/CTA-cardio.nrrd" "[1.04s]"</code></pre>

---

## Post #2 by @chir.set (2020-10-10 14:39 UTC)

<p>This line appears in console when trying to move around the 3D view :</p>
<blockquote>
<p>QGestureManager::deliverEvent: could not find the target for gesture</p>
</blockquote>

---

## Post #3 by @lassoan (2020-10-10 15:31 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="1" data-topic="13973">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>Only Slicer appearence themes are proposed in Application Settings, and not system themes like Breeze and Oxygen.</p>
</blockquote>
</aside>
<p>“Slicer” uses default color palette that we get from Qt, while “Dark Slicer” and “Light Slicer” are color palettes defined by Slicer. Qt capabilities for getting colors from system theme are different depending on the operating system and we also need to do some overrides for colors that don’t make sense. As Qt improves dark mode support on all operating systems, Slicer will improve, too.</p>
<aside class="quote no-group" data-username="chir.set" data-post="1" data-topic="13973">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>2D slice views are black empty.</p>
</blockquote>
</aside>
<p>Yes, we know about this - <a href="https://github.com/Slicer/Slicer/issues/5220">https://github.com/Slicer/Slicer/issues/5220</a></p>
<aside class="quote no-group" data-username="chir.set" data-post="1" data-topic="13973">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>Rotating 3D view with left mouse button down changes window state from maximized to ‘restored’ without rotating the view. When left mouse button is released, moving around the mouse rotates the view. Please see <a href="https://yadi.sk/i/gy3Iu-Z6JfrhvQ">attached</a> screen capture.</p>
</blockquote>
</aside>
<p>What Qt version do you use? Linux requires very latest Qt (5.15.1), as Wayland support in previous versions was very buggy.</p>

---

## Post #4 by @chir.set (2020-10-10 15:59 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="13973">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>What Qt version do you use?</p>
</blockquote>
</aside>
<p>I’m indeed using Qt 5.15.1.<br>
I must add that this 3D view rotating issue described above is observed in KDE X11 only. The view rotates normally in KDE Wayland, and the main window is not restored.</p>

---

## Post #5 by @lassoan (2020-10-10 17:42 UTC)

<p>Probably a few X11 bugs were introduced as they fixed the Wayland bugs. Probably these errors will be fixed in upcoming patch releases. What is interesting that the problem does not occur with the official build. Can you copy-paste here the application log of running Slicer that you have built?</p>

---

## Post #6 by @chir.set (2020-10-10 18:38 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="13973">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>the application log</p>
</blockquote>
</aside>
<p>I’m afraid I need some precision here.<br>
Do you refer to console stdout messages ? Error log in Slicer UI (Ctrl+0) ? Some other source of messages ?</p>

---

## Post #7 by @lassoan (2020-10-10 18:49 UTC)

<p>I mean the same log for your custom-built Slicer, as you posted before for the installed Slicer (available from menu: Help / Report a bug).</p>

---

## Post #8 by @chir.set (2020-10-10 19:06 UTC)

<p>Here is the log from ‘Help/Report a bug’ after loading CTA-Cardio, Volume Rendering, moving the 3D view and closing the scene.</p>
<blockquote>
<p>[DEBUG][Qt] 10.10.2020 20:59:17 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Session start time …: 2020-10-10 20:59:17<br>
[DEBUG][Qt] 10.10.2020 20:59:17 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Slicer version …: 4.13.0-2020-10-09 (revision 29425 / 5da4da2) linux-amd64 - installed release<br>
[DEBUG][Qt] 10.10.2020 20:59:17 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Operating system …: Linux / 5.9.0-rc7-git / <span class="hashtag-raw">#161</span> SMP Sun Oct 4 10:49:07 CEST 2020 - 64-bit<br>
[DEBUG][Qt] 10.10.2020 20:59:17 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Memory …: 15018 MB physical, 15359 MB virtual<br>
[DEBUG][Qt] 10.10.2020 20:59:17 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - CPU …: AuthenticAMD AMD Ryzen 5 2500U with Radeon Vega Mobile Gfx, 4 cores, 8 logical processors<br>
[DEBUG][Qt] 10.10.2020 20:59:17 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - VTK configuration …: OpenGL2 rendering, Sequential threading<br>
[DEBUG][Qt] 10.10.2020 20:59:17 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Qt configuration …: version 5.15.1, with SSL, requested OpenGL 3.2 (core profile)<br>
[DEBUG][Qt] 10.10.2020 20:59:17 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Developer mode enabled …: yes<br>
[DEBUG][Qt] 10.10.2020 20:59:17 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Prefer executable CLI …: no<br>
[DEBUG][Qt] 10.10.2020 20:59:17 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Application path …: /home/user/programs/Slicer-4.13.0-2020-10-09-linux-amd64/bin<br>
[DEBUG][Qt] 10.10.2020 20:59:17 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Additional module paths …: (none)<br>
[DEBUG][Python] 10.10.2020 20:59:18 [Python] (/home/user/programs/Slicer-4.13.0-2020-10-09-linux-amd64/lib/Python/lib/python3.6/site-packages/pydicom/datadict.py:432) - Reversing DICOM dictionary so can look up tag from a keyword…<br>
[DEBUG][Python] 10.10.2020 20:59:20 [Python] (/home/user/programs/Slicer-4.13.0-2020-10-09-linux-amd64/lib/Slicer-4.13/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 10.10.2020 20:59:21 [Python] (/home/user/programs/Slicer-4.13.0-2020-10-09-linux-amd64/lib/Slicer-4.13/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[ERROR][VTK] 10.10.2020 20:59:21 [vtkSlicerTerminologyEntry (0x563f5b35d670)] (/home/arc/src/Slicer/Modules/Loadable/Terminologies/Logic/vtkSlicerTerminologiesModuleLogic.cxx:2079) - DeserializeTerminologyEntry: Invalid type component<br>
[DEBUG][Python] 10.10.2020 20:59:21 [Python] (/home/user/programs/Slicer-4.13.0-2020-10-09-linux-amd64/lib/Slicer-4.13/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 10.10.2020 20:59:21 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “Volumes”<br>
[WARNING][Qt] 10.10.2020 20:59:22 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Assertion <code>this-&gt;Table-&gt;columnWidth(j) == newWidth</code> failed in  /home/arc/src/Slicer-SuperBuild/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  242<br>
[WARNING][Qt] 10.10.2020 20:59:22 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Assertion <code>this-&gt;Table-&gt;columnWidth(j) == newWidth</code> failed in  /home/arc/src/Slicer-SuperBuild/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  242<br>
[WARNING][Qt] 10.10.2020 20:59:22 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Assertion <code>this-&gt;Table-&gt;columnWidth(j) == newWidth</code> failed in  /home/arc/src/Slicer-SuperBuild/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  242<br>
[WARNING][Qt] 10.10.2020 20:59:22 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Assertion <code>this-&gt;Table-&gt;columnWidth(j) == newWidth</code> failed in  /home/arc/src/Slicer-SuperBuild/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  242<br>
[WARNING][Qt] 10.10.2020 20:59:22 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  /home/arc/src/Slicer-SuperBuild/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253<br>
[WARNING][Qt] 10.10.2020 20:59:22 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  /home/arc/src/Slicer-SuperBuild/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253<br>
[WARNING][Qt] 10.10.2020 20:59:22 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  /home/arc/src/Slicer-SuperBuild/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253<br>
[WARNING][Qt] 10.10.2020 20:59:22 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  /home/arc/src/Slicer-SuperBuild/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253<br>
[WARNING][Qt] 10.10.2020 20:59:22 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Assertion <code>this-&gt;Table-&gt;columnWidth(j) == newWidth</code> failed in  /home/arc/src/Slicer-SuperBuild/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  242<br>
[WARNING][Qt] 10.10.2020 20:59:22 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Assertion <code>this-&gt;Table-&gt;columnWidth(j) == newWidth</code> failed in  /home/arc/src/Slicer-SuperBuild/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  242<br>
[WARNING][Qt] 10.10.2020 20:59:22 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Assertion <code>this-&gt;Table-&gt;columnWidth(j) == newWidth</code> failed in  /home/arc/src/Slicer-SuperBuild/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  242<br>
[WARNING][Qt] 10.10.2020 20:59:22 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  /home/arc/src/Slicer-SuperBuild/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253<br>
[WARNING][Qt] 10.10.2020 20:59:22 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  /home/arc/src/Slicer-SuperBuild/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253<br>
[WARNING][Qt] 10.10.2020 20:59:22 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  /home/arc/src/Slicer-SuperBuild/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253<br>
[WARNING][Qt] 10.10.2020 20:59:22 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  /home/arc/src/Slicer-SuperBuild/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253<br>
[WARNING][Qt] 10.10.2020 20:59:22 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Assertion <code>this-&gt;Table-&gt;columnWidth(j) == newWidth</code> failed in  /home/arc/src/Slicer-SuperBuild/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  242<br>
[WARNING][Qt] 10.10.2020 20:59:22 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Assertion <code>this-&gt;Table-&gt;columnWidth(j) == newWidth</code> failed in  /home/arc/src/Slicer-SuperBuild/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  242<br>
[WARNING][Qt] 10.10.2020 20:59:22 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Assertion <code>this-&gt;Table-&gt;columnWidth(j) == newWidth</code> failed in  /home/arc/src/Slicer-SuperBuild/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  242<br>
[WARNING][Qt] 10.10.2020 20:59:22 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  /home/arc/src/Slicer-SuperBuild/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253<br>
[WARNING][Qt] 10.10.2020 20:59:22 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  /home/arc/src/Slicer-SuperBuild/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253<br>
[WARNING][Qt] 10.10.2020 20:59:22 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  /home/arc/src/Slicer-SuperBuild/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253<br>
[WARNING][Qt] 10.10.2020 20:59:22 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  /home/arc/src/Slicer-SuperBuild/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253<br>
[WARNING][Qt] 10.10.2020 20:59:22 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  /home/arc/src/Slicer-SuperBuild/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253<br>
[WARNING][Qt] 10.10.2020 20:59:22 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  /home/arc/src/Slicer-SuperBuild/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253<br>
[INFO][Stream] 10.10.2020 20:59:23 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Loading Slicer RC file [/home/user/.slicerrc.py]<br>
[INFO][VTK] 10.10.2020 21:00:00 [vtkMRMLVolumeArchetypeStorageNode (0x563f5f73dd70)] (/home/arc/src/Slicer/Libs/MRML/Core/vtkMRMLVolumeArchetypeStorageNode.cxx:470) - Loaded volume from file: /home/user/Desktop/BIG/Slicer/CTA-cardio.nrrd. Dimensions: 512x512x321. Number of components: 1. Pixel type: short.<br>
[DEBUG][Qt] 10.10.2020 21:00:00 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - “Volume” Reader has successfully read the file “/home/user/Desktop/BIG/Slicer/CTA-cardio.nrrd” “[1.15s]”<br>
[DEBUG][Qt] 10.10.2020 21:01:18 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “VolumeRendering”<br>
[WARNING][Qt] 10.10.2020 21:01:29 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - QGestureManager::deliverEvent: could not find the target for gesture<br>
[WARNING][Qt] 10.10.2020 21:01:34 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - QGestureManager::deliverEvent: could not find the target for gesture<br>
[DEBUG][Qt] 10.10.2020 21:01:50 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Close main MRML scene<br>
[ERROR][VTK] 10.10.2020 21:01:50 [vtkImageMapToColors (0x563f5f5aea80)] (/home/arc/src/Slicer-SuperBuild/VTK/Imaging/Core/vtkImageMapToColors.cxx:151) - RequestInformation: No LookupTable was set but number of components in input doesn’t match OutputFormat, therefore input can’t be passed through!<br>
[ERROR][VTK] 10.10.2020 21:01:50 [vtkImageExtractComponents (0x563f5f776800)] (/home/arc/src/Slicer-SuperBuild/VTK/Imaging/Core/vtkImageExtractComponents.cxx:230) - Execute: Component 1 is not in input.<br>
[ERROR][VTK] 10.10.2020 21:01:50 [vtkImageExtractComponents (0x563f5f776800)] (/home/arc/src/Slicer-SuperBuild/VTK/Imaging/Core/vtkImageExtractComponents.cxx:230) - Execute: Component 1 is not in input.<br>
[ERROR][VTK] 10.10.2020 21:01:50 [vtkImageExtractComponents (0x563f5f776800)] (/home/arc/src/Slicer-SuperBuild/VTK/Imaging/Core/vtkImageExtractComponents.cxx:230) - Execute: Component 1 is not in input.<br>
[ERROR][VTK] 10.10.2020 21:01:50 [vtkImageExtractComponents (0x563f5f776800)] (/home/arc/src/Slicer-SuperBuild/VTK/Imaging/Core/vtkImageExtractComponents.cxx:230) - Execute: Component 1 is not in input.<br>
[ERROR][VTK] 10.10.2020 21:01:50 [vtkImageExtractComponents (0x563f5f776800)] (/home/arc/src/Slicer-SuperBuild/VTK/Imaging/Core/vtkImageExtractComponents.cxx:230) - Execute: Component 1 is not in input.<br>
[ERROR][VTK] 10.10.2020 21:01:50 [vtkImageExtractComponents (0x563f5f776800)] (/home/arc/src/Slicer-SuperBuild/VTK/Imaging/Core/vtkImageExtractComponents.cxx:230) - Execute: Component 1 is not in input.<br>
[ERROR][VTK] 10.10.2020 21:01:50 [vtkImageExtractComponents (0x563f5f776800)] (/home/arc/src/Slicer-SuperBuild/VTK/Imaging/Core/vtkImageExtractComponents.cxx:230) - Execute: Component 1 is not in input.<br>
[ERROR][VTK] 10.10.2020 21:01:50 [vtkImageExtractComponents (0x563f5f776800)] (/home/arc/src/Slicer-SuperBuild/VTK/Imaging/Core/vtkImageExtractComponents.cxx:230) - Execute: Component 1 is not in input.<br>
[ERROR][VTK] 10.10.2020 21:01:50 [vtkImageExtractComponents (0x7fa8d400e5e0)] (/home/arc/src/Slicer-SuperBuild/VTK/Imaging/Core/vtkImageExtractComponents.cxx:230) - Execute: Component 3 is not in input.<br>
[ERROR][VTK] 10.10.2020 21:01:50 [vtkImageExtractComponents (0x7fa8d400e5e0)] (/home/arc/src/Slicer-SuperBuild/VTK/Imaging/Core/vtkImageExtractComponents.cxx:230) - Execute: Component 3 is not in input.<br>
[ERROR][VTK] 10.10.2020 21:01:50 [vtkImageExtractComponents (0x7fa8d400e5e0)] (/home/arc/src/Slicer-SuperBuild/VTK/Imaging/Core/vtkImageExtractComponents.cxx:230) - Execute: Component 3 is not in input.<br>
[ERROR][VTK] 10.10.2020 21:01:50 [vtkImageExtractComponents (0x7fa8d400e5e0)] (/home/arc/src/Slicer-SuperBuild/VTK/Imaging/Core/vtkImageExtractComponents.cxx:230) - Execute: Component 3 is not in input.<br>
[ERROR][VTK] 10.10.2020 21:01:50 [vtkImageExtractComponents (0x7fa8d400e5e0)] (/home/arc/src/Slicer-SuperBuild/VTK/Imaging/Core/vtkImageExtractComponents.cxx:230) - Execute: Component 3 is not in input.<br>
[ERROR][VTK] 10.10.2020 21:01:50 [vtkImageExtractComponents (0x7fa8d400e5e0)] (/home/arc/src/Slicer-SuperBuild/VTK/Imaging/Core/vtkImageExtractComponents.cxx:230) - Execute: Component 3 is not in input.<br>
[ERROR][VTK] 10.10.2020 21:01:50 [vtkImageExtractComponents (0x7fa8d400e5e0)] (/home/arc/src/Slicer-SuperBuild/VTK/Imaging/Core/vtkImageExtractComponents.cxx:230) - Execute: Component 3 is not in input.<br>
[ERROR][VTK] 10.10.2020 21:01:50 [vtkImageExtractComponents (0x7fa8d400e5e0)] (/home/arc/src/Slicer-SuperBuild/VTK/Imaging/Core/vtkImageExtractComponents.cxx:230) - Execute: Component 3 is not in input.</p>
</blockquote>

---

## Post #9 by @chir.set (2020-10-10 19:07 UTC)

<p>On one previous run, I had this in console, can’t remember what I did exactly.</p>
<blockquote>
<p>Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  /home/arc/src/Slicer-SuperBuild/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253<br>
Loading Slicer RC file [/home/user/.slicerrc.py]<br>
An OpenGL Core Profile was requested, but it is not supported on the current platform. Falling back to a non-Core profile. Note that this might cause rendering issues.<br>
Error: Unknown module: ext.SmjCDN.mobile<br>
libpng warning: iCCP: known incorrect sRGB profile<br>
Switch to module:  “”<br>
Switch to module:  “”<br>
vtkDebugLeaks has found no leaks.</p>
</blockquote>

---

## Post #10 by @lassoan (2020-10-10 19:16 UTC)

<p>The warnings look harmless. The OpenGL core profile complaint is somewhat surprising. Try to use <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/overview.html#runtime-environment-variables">compatibility profile</a> (set SLICER_OPENGL_PROFILE=compatibility) and see if it makes any difference.</p>

---

## Post #11 by @chir.set (2020-10-10 22:17 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="13973">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>SLICER_OPENGL_PROFILE=compatibility</p>
</blockquote>
</aside>
<p>No better luck with either no, core and compatibility. I won’t waste your time further as it’s custom built. It may well get fixed unintentionally next. 4.11 will still run on Arch until ICU libs get upgraded here. Thanks.</p>

---

## Post #12 by @chir.set (2020-10-11 12:05 UTC)

<p>I could trace the 3D rotation issue to the selected Appearance Style.</p>
<p>System Breeze and Oxygen styles trigger the window resize to ‘restored’.<br>
System QtCurve does not misbehave.<br>
The 3 Slicer styles do not misbehave.</p>
<p>Switching to Slicer Dark, and hoping the 2D view issue gets fixed soon.</p>
<p>Thanks for your consideration.</p>

---

## Post #13 by @Harry-Muzart (2020-10-13 08:55 UTC)

<p>thanks all for the info</p>

---
