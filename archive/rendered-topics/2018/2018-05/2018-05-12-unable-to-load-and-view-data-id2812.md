---
topic_id: 2812
title: "Unable To Load And View Data"
date: 2018-05-12
url: https://discourse.slicer.org/t/2812
---

# Unable to load and view data

**Topic ID**: 2812
**Date**: 2018-05-12
**URL**: https://discourse.slicer.org/t/unable-to-load-and-view-data/2812

---

## Post #1 by @itakeitapart (2018-05-12 19:10 UTC)

<p>Operating system:windows 7<br>
Slicer version:4.8.1<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hello All,<br>
I am a very novice user.  Around 6-9 months ago I was working with some of the demo videos found on you tube.  I had used some of the samples and some of my own files from a dental CBCT.  I returned to these projects and others today and am unable to open anything.  I can see them in the DICOM Browser but when I select load, nothing happens. Or the program crashes. Or i get “SlicerApp-real.exe is not responding”  I have tried reloading slicer, loading different files, tried the demo sample data sets. all to no avail.  Not sure where to turn or what to do next.   Thanks All  in advance!</p>

---

## Post #2 by @yasernakib (2018-05-12 21:34 UTC)

<p>Looks odd!<br>
What’s the file extensions you’re trying to load with dicom browser? Are you using ‘add data’ option?<br>
Have you tried remove the application and try a new fresh install?</p>

---

## Post #3 by @lassoan (2018-05-13 12:39 UTC)

<p>How much space do you have on your hard drive? Can you send the application logs of a failed loading attempt (menu: Help / Report a bug)? Try updating your video card drivers, try latest nightly version of Slicer, and try to remove your <a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ApplicationSettings#Settings_file_location">Slicer.ini files</a>.</p>

---

## Post #4 by @itakeitapart (2018-05-14 13:43 UTC)

<p>[DEBUG][Qt] 14.05.2018 07:41:18 [] (unknown:0) - Session start time …: 2018-05-14 07:41:18<br>
[DEBUG][Qt] 14.05.2018 07:41:18 [] (unknown:0) - Slicer version …: 4.8.1 (revision 26813) win-amd64 - installed<br>
[DEBUG][Qt] 14.05.2018 07:41:18 [] (unknown:0) - Operating system …: Windows / 7 / Service Pack 1 (Build 7601) - 64-bit<br>
[DEBUG][Qt] 14.05.2018 07:41:18 [] (unknown:0) - Memory …: 16319 MB physical, 32637 MB virtual<br>
[DEBUG][Qt] 14.05.2018 07:41:18 [] (unknown:0) - CPU …: GenuineIntel , 4 cores, 16 logical processors<br>
[DEBUG][Qt] 14.05.2018 07:41:18 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 14.05.2018 07:41:18 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 14.05.2018 07:41:18 [] (unknown:0) - Additional module paths …: (none)<br>
[DEBUG][Python] 14.05.2018 07:41:21 [Python] (C:\Program Files\Slicer 4.8.1\lib\Python\Lib\site-packages\git\cmd.py:719) - Popen(%s, cwd=%s, universal_newlines=%s, shell=%s)<br>
[DEBUG][Python] 14.05.2018 07:41:22 [Python] (C:\Program Files\Slicer 4.8.1\lib\Python\Lib\site-packages\git\cmd.py:719) - Popen(%s, cwd=%s, universal_newlines=%s, shell=%s)<br>
[DEBUG][Python] 14.05.2018 07:41:24 [Python] (C:\Program Files\Slicer 4.8.1\lib\Slicer-4.8\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 14.05.2018 07:41:25 [Python] (C:\Program Files\Slicer 4.8.1\lib\Slicer-4.8\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 14.05.2018 07:41:25 [Python] (C:\Program Files\Slicer 4.8.1\lib\Slicer-4.8\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 14.05.2018 07:41:19 [] (unknown:0) - Number of registered modules: 135<br>
[DEBUG][Qt] 14.05.2018 07:41:22 [] (unknown:0) - Number of instantiated modules: 135<br>
[DEBUG][Qt] 14.05.2018 07:41:25 [] (unknown:0) - Number of loaded modules: 135<br>
[DEBUG][Qt] 14.05.2018 07:41:25 [] (unknown:0) - Switch to module:  “Welcome”</p>

---

## Post #5 by @itakeitapart (2018-05-14 18:49 UTC)

<p>Well I think the problem is resolved (I hope).  I found and deleted the slicer.ini files, restarted and was then able to load the data.  I think my hard drive and video card are OK as I can open and work with these same files in other 3d programs.    Thank You for the help!</p>

---

## Post #6 by @lassoan (2018-05-14 20:07 UTC)

<p>Thanks for the update. Maybe the Slicer DICOM database location had to be reset.</p>

---
