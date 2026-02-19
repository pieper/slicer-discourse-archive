---
topic_id: 13196
title: "Slicerjupyter Extension"
date: 2020-08-27
url: https://discourse.slicer.org/t/13196
---

# SlicerJupyter Extension

**Topic ID**: 13196
**Date**: 2020-08-27
**URL**: https://discourse.slicer.org/t/slicerjupyter-extension/13196

---

## Post #1 by @Fereshte_J (2020-08-27 16:25 UTC)

<p>Problem report for Slicer 4.11.0-2020-08-26 win-amd64: [please describe expected and actual behavior]<br>
I want to install SlicerJupyter extension on slicer4.11 version 29320 however I cannot find the extension in the extension manager. It is very important for me please give me a solution.<br>
with slicer 4.10 I could install the extension however I got an error while importing jupyternotebooksib in the jupyter notebook, so I decided to install a higher version, and this problem occured.</p>
<p>[DEBUG][Qt] 27.08.2020 20:01:20 [] (unknown:0) - Session start time …: 2020-08-27 20:01:20</p>
<p>[DEBUG][Qt] 27.08.2020 20:01:20 [] (unknown:0) - Slicer version …: 4.11.0-2020-08-26 (revision 29320 / 1f08201) win-amd64 - installed release</p>
<p>[DEBUG][Qt] 27.08.2020 20:01:20 [] (unknown:0) - Operating system …: Windows / Personal / (Build 18363, Code Page 65001) - 64-bit</p>
<p>[DEBUG][Qt] 27.08.2020 20:01:20 [] (unknown:0) - Memory …: 8078 MB physical, 16782 MB virtual</p>
<p>[DEBUG][Qt] 27.08.2020 20:01:20 [] (unknown:0) - CPU …: GenuineIntel , 4 cores, 4 logical processors</p>
<p>[DEBUG][Qt] 27.08.2020 20:01:20 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading</p>
<p>[DEBUG][Qt] 27.08.2020 20:01:20 [] (unknown:0) - Qt configuration …: version 5.15.0, with SSL, requested OpenGL 3.2 (compatibility profile)</p>
<p>[DEBUG][Qt] 27.08.2020 20:01:20 [] (unknown:0) - Developer mode enabled …: no</p>
<p>[DEBUG][Qt] 27.08.2020 20:01:20 [] (unknown:0) - Prefer executable CLI …: yes</p>
<p>[DEBUG][Qt] 27.08.2020 20:01:20 [] (unknown:0) - Application path …: C:/Users/feres/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-26/bin</p>
<p>[DEBUG][Qt] 27.08.2020 20:01:20 [] (unknown:0) - Additional module paths …: (none)</p>
<p>[DEBUG][Python] 27.08.2020 20:01:23 [Python] (C:\Users\feres\AppData\Local\NA-MIC\Slicer 4.11.0-2020-08-26\lib\Python\Lib\site-packages\pydicom\datadict.py:432) - Reversing DICOM dictionary so can look up tag from a keyword…</p>
<p>[DEBUG][Python] 27.08.2020 20:01:24 [Python] (C:\Users\feres\AppData\Local\NA-MIC\Slicer 4.11.0-2020-08-26\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations</p>
<p>[DEBUG][Python] 27.08.2020 20:01:25 [Python] (C:\Users\feres\AppData\Local\NA-MIC\Slicer 4.11.0-2020-08-26\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor</p>
<p>[DEBUG][Python] 27.08.2020 20:01:25 [Python] (C:\Users\feres\AppData\Local\NA-MIC\Slicer 4.11.0-2020-08-26\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics</p>
<p>[DEBUG][Qt] 27.08.2020 20:01:25 [] (unknown:0) - Switch to module: “Welcome”</p>

---

## Post #2 by @lassoan (2020-08-27 20:58 UTC)

<p>Thanks for reporting this. We are working on this issue. Until this gets fixed, you can use Slicer release from a few weeks ago: <a href="https://download.slicer.org/?date=2020-08-14">https://download.slicer.org/?date=2020-08-14</a></p>

---

## Post #3 by @Fereshte_J (2020-08-28 15:51 UTC)

<p>Thank you for your response. The problem is solved.</p>

---
