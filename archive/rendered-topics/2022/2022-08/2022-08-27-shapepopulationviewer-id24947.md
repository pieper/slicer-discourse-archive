---
topic_id: 24947
title: "Shapepopulationviewer"
date: 2022-08-27
url: https://discourse.slicer.org/t/24947
---

# ShapePopulationViewer

**Topic ID**: 24947
**Date**: 2022-08-27
**URL**: https://discourse.slicer.org/t/shapepopulationviewer/24947

---

## Post #1 by @jegberink (2022-08-27 16:30 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 5.0.3</p>
<p>Hello,</p>
<p>ShapePopulationViewer does not seem to be working for me on 2 different pc’s. On one system Slicer will crash, on the other system it just won’t load and i have to close Slicer.</p>
<p>I would like to confirm if the problem is on my end or if anyone else is having the same problem.</p>
<p>Thank you in advance.</p>

---

## Post #2 by @lassoan (2022-08-29 04:08 UTC)

<p>I’ve just tested ShapePopulationViewer extension on two Windows10 computers and it worked well on both (I just tested that I switch to the module and its GUI shows up).</p>
<p>Maybe you have installed some other extensions that interfere with it? You can install Slicer into an empty folder and install only the ShapePopulationViewer extension to see if it works for you then.</p>

---

## Post #3 by @jegberink (2022-08-29 09:05 UTC)

<p>Thank you for the quick response. Unfortunately it does not seem to be working. I’ll try to figure it out.<br>
To be sure i’ll add the log file from the crash, i however do not see anything that could cause the issue.</p>
<p>[DEBUG][Qt] 29.08.2022 11:03:05 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Session start time …: 2022-08-29 11:03:05<br>
[DEBUG][Qt] 29.08.2022 11:03:05 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Slicer version …: 5.0.3 (revision 30893 / 7ea0f43) win-amd64 - installed release<br>
[DEBUG][Qt] 29.08.2022 11:03:05 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Operating system …: Windows /  Professional / (Build 19043, Code Page 65001) - 64-bit<br>
[DEBUG][Qt] 29.08.2022 11:03:05 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Memory …: 16269 MB physical, 45965 MB virtual<br>
[DEBUG][Qt] 29.08.2022 11:03:05 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - CPU …: GenuineIntel , 8 cores, 8 logical processors<br>
[DEBUG][Qt] 29.08.2022 11:03:05 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 29.08.2022 11:03:05 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Qt configuration …: version 5.15.2, with SSL, requested OpenGL 3.2 (compatibility profile)<br>
[DEBUG][Qt] 29.08.2022 11:03:05 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Internationalization …: disabled, language=<br>
[DEBUG][Qt] 29.08.2022 11:03:05 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Developer mode …: disabled<br>
[DEBUG][Qt] 29.08.2022 11:03:05 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Application path …: C:/Users/Jeroen/Desktop/slicer/Slicer 5.0.3/bin<br>
[DEBUG][Qt] 29.08.2022 11:03:05 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Additional module paths …: NA-MIC/Extensions-30893/ShapePopulationViewer/lib/Slicer-5.0/qt-loadable-modules<br>
[DEBUG][Python] 29.08.2022 11:03:09 [Python] (C:\Users\Jeroen\Desktop\slicer\Slicer 5.0.3\lib\Slicer-5.0\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 29.08.2022 11:03:11 [Python] (C:\Users\Jeroen\Desktop\slicer\Slicer 5.0.3\lib\Slicer-5.0\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 29.08.2022 11:03:11 [Python] (C:\Users\Jeroen\Desktop\slicer\Slicer 5.0.3\lib\Slicer-5.0\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 29.08.2022 11:03:12 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “Welcome”</p>

---

## Post #4 by @lassoan (2022-08-29 12:24 UTC)

<p>Does the crash happen when you switch to the Shape Population Viewer module or when you try to use it? Does it help if the application window is not maximized (the module GUI is very large and it may be difficult to fit it in the application window if the font size is large or screen resolution is low)? Also try to to remove (or temporarily rename) your <a href="https://slicer.readthedocs.io/en/latest/user_guide/settings.html?highlight=settings#settings-file-location">Slicer.ini settings file</a> - maybe it got corrupted somehow (after that you may need to reinstall the extension).</p>

---
