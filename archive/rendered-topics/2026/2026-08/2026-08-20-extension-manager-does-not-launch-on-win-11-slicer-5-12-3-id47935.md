---
topic_id: 47935
title: "Extension Manager does not launch on Win 11 (Slicer 5.12.3)"
date: 2026-08-20
url: https://discourse.slicer.org/t/47935
last_bumped: 2026-08-24T12:37:25.718Z
---

# Extension Manager does not launch on Win 11 (Slicer 5.12.3)

**Topic ID**: 47935
**Date**: 2026-08-20
**URL**: https://discourse.slicer.org/t/extension-manager-does-not-launch-on-win-11-slicer-5-12-3/47935

---

## Post #1 by @dumichgh (2026-08-20 13:07 UTC)

<p>Problem report for 3D Slicer 5.12.3 win-amd64: [please describe expected and actual behavior]</p>
<p>Extension manager does not launch  on Windows 11 system after 30min</p>
<p>Log:</p>
<p>[DEBUG][Qt] 19.08.2026 17:14:18 [] (unknown:0) - Session start time …: 20260819_171418</p>
<p>[DEBUG][Qt] 19.08.2026 17:14:18 [] (unknown:0) - Slicer version …: 5.12.3 (revision 34627 / 9034c71) win-amd64 - installed release</p>
<p>[DEBUG][Qt] 19.08.2026 17:14:18 [] (unknown:0) - Operating system …: Windows / Professional / (Build 26100, Code Page 65001) - 64-bit</p>
<p>[DEBUG][Qt] 19.08.2026 17:14:18 [] (unknown:0) - Memory …: 65218 MB physical, 69314 MB virtual</p>
<p>[DEBUG][Qt] 19.08.2026 17:14:18 [] (unknown:0) - CPU …: GenuineIntel , 8 cores, 8 logical processors</p>
<p>[DEBUG][Qt] 19.08.2026 17:14:18 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading</p>
<p>[DEBUG][Qt] 19.08.2026 17:14:18 [] (unknown:0) - Qt configuration …: version 5.15.2, with SSL, requested OpenGL 3.2 (core profile)</p>
<p>[DEBUG][Qt] 19.08.2026 17:14:18 [] (unknown:0) - DCMTK configuration …: version 3.7.0, no SSL</p>
<p>[DEBUG][Qt] 19.08.2026 17:14:18 [] (unknown:0) - Internationalization …: disabled, language=</p>
<p>[DEBUG][Qt] 19.08.2026 17:14:18 [] (unknown:0) - Developer mode …: disabled</p>
<p>[DEBUG][Qt] 19.08.2026 17:14:18 [] (unknown:0) - Application path …: C:/Users/xxxx/AppData/Local/slicer.org/3D Slicer 5.12.3/bin</p>
<p>[DEBUG][Qt] 19.08.2026 17:14:18 [] (unknown:0) - Additional module paths ..: (none)</p>
<p>[INFO][Stream] 19.08.2026 17:14:19 [] (unknown:0) -</p>
<p>[DEBUG][Python] 19.08.2026 17:14:22 [Python] (C:\Users\xxxx\AppData\Local\slicer.org\3D Slicer 5.12.3\lib\Slicer-5.12\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:40) - Scripted subject hierarchy plugin registered: SegmentEditor</p>
<p>[DEBUG][Python] 19.08.2026 17:14:22 [Python] (C:\Users\xxxx\AppData\Local\slicer.org\3D Slicer 5.12.3\lib\Slicer-5.12\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:40) - Scripted subject hierarchy plugin registered: SegmentStatistics</p>
<p>[DEBUG][Qt] 19.08.2026 17:14:22 [] (unknown:0) - Switch to module: “Welcome”</p>

---

## Post #2 by @ebrahim (2026-08-20 19:18 UTC)

<p>It looks like there are no errors in the log; the extension manager is just hanging.</p>
<p>(You said it does work for you in Slicer 5.6 right?)</p>
<p>In Task Manager, does QtWebEngineProcess.exe appear after clicking Extensions Manager?</p>
<p>Is this a corporate or university managed computer with any IT policies that could be blocking something? Are you on a network that could be blocking something?</p>
<p>You could try from another network if so<br>
You can try just once running slicer as administrator and see if that fixes it, that might be informative</p>

---

## Post #3 by @dumichgh (2026-08-20 22:16 UTC)

<p>Extension Manager does not launch in 5.12.3. (See bug <span class="hashtag-raw">#9363</span>). Tried it on both hospital and home network.</p>
<p>EM launched in 5.6.2, so was able to install TotalSegmentator there, but TS gave error during the test run (not able to install Pythorch dependencies).  You informed that you are not supporting 5.6.2 extensions any more (and closed bug <span class="hashtag-raw">#9364</span>), so guess need to wait to have <span class="hashtag-raw">#9363</span> fixed in 5.12.3.</p>

---

## Post #4 by @ebrahim (2026-08-24 12:37 UTC)

<p>Glad you found a solution at <a href="https://github.com/Slicer/Slicer/issues/9363#issuecomment-5383695511" class="inline-onebox">Extension Manager does not launch on Win 11 in Slicer 5.12.3 · Issue #9363 · Slicer/Slicer · GitHub</a></p>

---
