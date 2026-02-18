# DICOM Browser could not pop-up

**Topic ID**: 1528
**Date**: 2017-11-27
**URL**: https://discourse.slicer.org/t/dicom-browser-could-not-pop-up/1528

---

## Post #1 by @researchtomliu (2017-11-27 16:02 UTC)

<pre><code class="lang-auto">[DEBUG][Qt] 27.11.2017 23:21:12 [] (unknown:0) - Session start time .......: 2017-11-27 23:21:12
[DEBUG][Qt] 27.11.2017 23:21:12 [] (unknown:0) - Slicer version ...........: 4.8.0 (revision 26489) win-amd64 - installed
[DEBUG][Qt] 27.11.2017 23:21:12 [] (unknown:0) - Operating system .........: Windows / 7 / Service Pack 1 (Build 7601) - 64-bit
[DEBUG][Qt] 27.11.2017 23:21:12 [] (unknown:0) - Memory ...................: 8159 MB physical, 16316 MB virtual
[DEBUG][Qt] 27.11.2017 23:21:12 [] (unknown:0) - CPU ......................: GenuineIntel , 8 cores, 16 logical processors
[DEBUG][Qt] 27.11.2017 23:21:12 [] (unknown:0) - Developer mode enabled ...: no
[DEBUG][Qt] 27.11.2017 23:21:12 [] (unknown:0) - Prefer executable CLI ....: yes
[DEBUG][Qt] 27.11.2017 23:21:12 [] (unknown:0) - Additional module paths ..: (none)
[DEBUG][Python] 27.11.2017 23:21:12 [Python] (D:\Program Files\Slicer 4.8.0\lib\Python\Lib\site-packages\git\cmd.py:719) - Popen(%s, cwd=%s, universal_newlines=%s, shell=%s)
[DEBUG][Python] 27.11.2017 23:21:12 [Python] (D:\Program Files\Slicer 4.8.0\lib\Python\Lib\site-packages\git\cmd.py:719) - Popen(%s, cwd=%s, universal_newlines=%s, shell=%s)
[DEBUG][Python] 27.11.2017 23:21:13 [Python] (D:\Program Files\Slicer 4.8.0\lib\Slicer-4.8\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations
[DEBUG][Python] 27.11.2017 23:21:13 [Python] (D:\Program Files\Slicer 4.8.0\lib\Slicer-4.8\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 27.11.2017 23:21:13 [Python] (D:\Program Files\Slicer 4.8.0\lib\Slicer-4.8\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Qt] 27.11.2017 23:21:12 [] (unknown:0) - Number of registered modules: 135
[DEBUG][Qt] 27.11.2017 23:21:12 [] (unknown:0) - Number of instantiated modules: 135
[DEBUG][Qt] 27.11.2017 23:21:13 [] (unknown:0) - Number of loaded modules: 135
[DEBUG][Qt] 27.11.2017 23:21:13 [] (unknown:0) - Switch to module:  "Welcome"
[DEBUG][Qt] 27.11.2017 23:21:15 [] (unknown:0) - Switch to module:  "DICOM"
[CRITICAL][Stream] 27.11.2017 23:21:15 [] (unknown:0) - Traceback (most recent call last):
[CRITICAL][Stream] 27.11.2017 23:21:15 [] (unknown:0) -   File "D:/Program Files/Slicer 4.8.0/lib/Slicer-4.8/qt-scripted-modules/DICOM.py", line 327, in setup
[CRITICAL][Stream] 27.11.2017 23:21:15 [] (unknown:0) -     self.detailsPopup = self.getSavedDICOMDetailsWidgetType()()
[CRITICAL][Stream] 27.11.2017 23:21:15 [] (unknown:0) -   File "D:\Program Files\Slicer 4.8.0\lib\Slicer-4.8\qt-scripted-modules\DICOMLib\DICOMWidgets.py", line 996, in __init__
[CRITICAL][Stream] 27.11.2017 23:21:15 [] (unknown:0) -     super(DICOMDetailsWindow, self).__init__(dicomBrowser, parent)
[CRITICAL][Stream] 27.11.2017 23:21:15 [] (unknown:0) -   File "D:\Program Files\Slicer 4.8.0\lib\Slicer-4.8\qt-scripted-modules\DICOMLib\DICOMWidgets.py", line 965, in __init__
[CRITICAL][Stream] 27.11.2017 23:21:15 [] (unknown:0) -     DICOMDetailsBase.__init__(self, dicomBrowser)
[CRITICAL][Stream] 27.11.2017 23:21:15 [] (unknown:0) -   File "D:\Program Files\Slicer 4.8.0\lib\Slicer-4.8\qt-scripted-modules\DICOMLib\DICOMWidgets.py", line 86, in __init__
[CRITICAL][Stream] 27.11.2017 23:21:15 [] (unknown:0) -     self.promptForDatabaseDirectory()
[CRITICAL][Stream] 27.11.2017 23:21:15 [] (unknown:0) -   File "D:\Program Files\Slicer 4.8.0\lib\Slicer-4.8\qt-scripted-modules\DICOMLib\DICOMWidgets.py", line 526, in promptForDatabaseDirectory
[CRITICAL][Stream] 27.11.2017 23:21:15 [] (unknown:0) -     "the DICOM Browser to pick a different location.".format(databaseDirectory)
[CRITICAL][Stream] 27.11.2017 23:21:15 [] (unknown:0) - UnicodeEncodeError: 'ascii' codec can't encode characters in position 11-14: ordinal not in range(128)
[CRITICAL][Stream] 27.11.2017 23:21:15 [] (unknown:0) - Traceback (most recent call last):
[CRITICAL][Stream] 27.11.2017 23:21:15 [] (unknown:0) -   File "D:/Program Files/Slicer 4.8.0/lib/Slicer-4.8/qt-scripted-modules/DICOM.py", line 268, in enter
[CRITICAL][Stream] 27.11.2017 23:21:15 [] (unknown:0) -     self.onOpenDetailsPopup()
[CRITICAL][Stream] 27.11.2017 23:21:15 [] (unknown:0) -   File "D:/Program Files/Slicer 4.8.0/lib/Slicer-4.8/qt-scripted-modules/DICOM.py", line 368, in onOpenDetailsPopup
[CRITICAL][Stream] 27.11.2017 23:21:15 [] (unknown:0) -     if not isinstance(self.detailsPopup, self.getSavedDICOMDetailsWidgetType()):
[CRITICAL][Stream] 27.11.2017 23:21:15 [] (unknown:0) - AttributeError: DICOMWidget instance has no attribute 'detailsPopup'
[WARNING][Python] 27.11.2017 23:21:27 [Python] (D:\Program Files\Slicer 4.8.0\bin\Python\slicer\util.py:906) - Could not start listener:
 Database directory not set: cannot start DICOMListener
[CRITICAL][Stream] 27.11.2017 23:21:27 [] (unknown:0) - Could not start listener:
[CRITICAL][Stream] 27.11.2017 23:21:27 [] (unknown:0) -  Database directory not set: cannot start DICOMListener
</code></pre>

---

## Post #2 by @cpinter (2017-11-27 16:24 UTC)

<p>It seems to me based on the log that there are special characters in the patient’s name possibly that could not be handled.</p>

---

## Post #3 by @lassoan (2017-11-28 03:32 UTC)

<p>The issue is probably that your user profile directory contains non-ascii characters, and Slicer tries to create the DICOM database directory in that folder.</p>
<p>You either have to change your user profile directory name or set database folder manually, by adding DatabaseDirectory value to Slicer.ini:</p>
<pre><code>[General]
...
DatabaseDirectory=C:/Users/msliv/OneDrive/Documents/SlicerDicomDatabase2
...</code></pre>

---

## Post #4 by @lassoan (2017-11-28 04:17 UTC)

<p><a href="https://github.com/Slicer/Slicer/commit/6683b83bbc40073689b1d3b7fad1b28ecbad89e7">Implemented a fix</a> in the nightly build (available for download on Wednesday) that at least allows the popup to be displayed. You may still need to set a Slicer DICOM database folder that has only Latin1 character in its name.</p>

---

## Post #5 by @researchtomliu (2017-12-03 13:58 UTC)

<p>Thanks a lot, the problem has been solved!</p>

---
