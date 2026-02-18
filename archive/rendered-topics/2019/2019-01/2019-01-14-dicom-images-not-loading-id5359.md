# DICOM Images not loading

**Topic ID**: 5359
**Date**: 2019-01-14
**URL**: https://discourse.slicer.org/t/dicom-images-not-loading/5359

---

## Post #1 by @cormacclarke (2019-01-14 15:21 UTC)

<p>I have issue loading my DICOM files to the Slicer software.<br>
I have uploaded these files successfully on my desktop but I am getting the following error when I try on my laptop.</p>
<details>
<summary>
Application logs</summary>
<pre><code class="lang-auto">[DEBUG][Qt] 14.01.2019 14:23:23 [] (unknown:0) - Session start time .......: 2019-01-14 14:23:23
[DEBUG][Qt] 14.01.2019 14:23:23 [] (unknown:0) - Slicer version ...........: 4.10.0 (revision 27501) win-amd64 - installed release
[DEBUG][Qt] 14.01.2019 14:23:24 [] (unknown:0) - Operating system .........: Windows /  Professional /  (Build 9200) - 64-bit
[DEBUG][Qt] 14.01.2019 14:23:24 [] (unknown:0) - Memory ...................: 16264 MB physical, 19208 MB virtual
[DEBUG][Qt] 14.01.2019 14:23:24 [] (unknown:0) - CPU ......................: GenuineIntel , 8 cores, 8 logical processors
[DEBUG][Qt] 14.01.2019 14:23:24 [] (unknown:0) - VTK configuration ........: OpenGL2 rendering, TBB threading
[DEBUG][Qt] 14.01.2019 14:23:24 [] (unknown:0) - Developer mode enabled ...: no
[DEBUG][Qt] 14.01.2019 14:23:24 [] (unknown:0) - Prefer executable CLI ....: yes
[DEBUG][Qt] 14.01.2019 14:23:24 [] (unknown:0) - Additional module paths ..: C:/Users/CormacClarke/AppData/Roaming/NA-MIC/Extensions-27501/SlicerHeart/lib/Slicer-4.10/qt-loadable-modules, C:/Users/CormacClarke/AppData/Roaming/NA-MIC/Extensions-27501/SlicerHeart/lib/Slicer-4.10/qt-scripted-modules, C:/Users/CormacClarke/AppData/Roaming/NA-MIC/Extensions-27501/Sequences/lib/Slicer-4.10/qt-loadable-modules, C:/Users/CormacClarke/AppData/Roaming/NA-MIC/Extensions-27501/Sequences/lib/Slicer-4.10/qt-scripted-modules
[DEBUG][Python] 14.01.2019 14:23:30 [Python] (C:\Program Files\Slicer 4.10.0\lib\Python\Lib\site-packages\git\cmd.py:719) - Popen(['git', 'version'], cwd=C:\Program Files\Slicer 4.10.0, universal_newlines=False, shell=None)
[DEBUG][Python] 14.01.2019 14:23:30 [Python] (C:\Program Files\Slicer 4.10.0\lib\Python\Lib\site-packages\git\cmd.py:719) - Popen(['git', 'version'], cwd=C:\Program Files\Slicer 4.10.0, universal_newlines=False, shell=None)
[DEBUG][Python] 14.01.2019 14:23:33 [Python] (C:\Program Files\Slicer 4.10.0\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations
[DEBUG][Python] 14.01.2019 14:23:34 [Python] (C:\Program Files\Slicer 4.10.0\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 14.01.2019 14:23:34 [Python] (C:\Program Files\Slicer 4.10.0\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Qt] 14.01.2019 14:23:34 [] (unknown:0) - Switch to module:  "Welcome"
[DEBUG][Qt] 14.01.2019 14:23:52 [] (unknown:0) - Switch to module:  "DICOM"
[CRITICAL][Stream] 14.01.2019 14:23:52 [] (unknown:0) - Traceback (most recent call last):
[CRITICAL][Stream] 14.01.2019 14:23:52 [] (unknown:0) -   File "C:/Program Files/Slicer 4.10.0/bin/../lib/Slicer-4.10/qt-scripted-modules/DICOM.py", line 332, in setup
[CRITICAL][Stream] 14.01.2019 14:23:52 [] (unknown:0) -     self.detailsPopup = self.getSavedDICOMDetailsWidgetType()()
[CRITICAL][Stream] 14.01.2019 14:23:52 [] (unknown:0) -   File "C:\Program Files\Slicer 4.10.0\lib\Slicer-4.10\qt-scripted-modules\DICOMLib\DICOMWidgets.py", line 1015, in __init__
[CRITICAL][Stream] 14.01.2019 14:23:52 [] (unknown:0) -     super(DICOMDetailsWindow, self).__init__(dicomBrowser, parent)
[CRITICAL][Stream] 14.01.2019 14:23:52 [] (unknown:0) -   File "C:\Program Files\Slicer 4.10.0\lib\Slicer-4.10\qt-scripted-modules\DICOMLib\DICOMWidgets.py", line 984, in __init__
[CRITICAL][Stream] 14.01.2019 14:23:52 [] (unknown:0) -     DICOMDetailsBase.__init__(self, dicomBrowser)
[CRITICAL][Stream] 14.01.2019 14:23:52 [] (unknown:0) -   File "C:\Program Files\Slicer 4.10.0\lib\Slicer-4.10\qt-scripted-modules\DICOMLib\DICOMWidgets.py", line 93, in __init__
[CRITICAL][Stream] 14.01.2019 14:23:52 [] (unknown:0) -     self.promptForDatabaseDirectory()
[CRITICAL][Stream] 14.01.2019 14:23:52 [] (unknown:0) -   File "C:\Program Files\Slicer 4.10.0\lib\Slicer-4.10\qt-scripted-modules\DICOMLib\DICOMWidgets.py", line 540, in promptForDatabaseDirectory
[CRITICAL][Stream] 14.01.2019 14:23:52 [] (unknown:0) -     os.makedirs(databaseDirectory)
[CRITICAL][Stream] 14.01.2019 14:23:52 [] (unknown:0) -   File "C:/Program Files/Slicer 4.10.0/bin/../lib/Python/Lib\os.py", line 157, in makedirs
[CRITICAL][Stream] 14.01.2019 14:23:52 [] (unknown:0) -     mkdir(name, mode)
[CRITICAL][Stream] 14.01.2019 14:23:52 [] (unknown:0) - WindowsError: [Error 2] The system cannot find the file specified: u'C:/Users/CormacClarke/Documents\\SlicerDICOMDatabase'
[CRITICAL][Stream] 14.01.2019 14:23:52 [] (unknown:0) - Traceback (most recent call last):
[CRITICAL][Stream] 14.01.2019 14:23:52 [] (unknown:0) -   File "C:/Program Files/Slicer 4.10.0/bin/../lib/Slicer-4.10/qt-scripted-modules/DICOM.py", line 273, in enter
[CRITICAL][Stream] 14.01.2019 14:23:52 [] (unknown:0) -     self.onOpenDetailsPopup()
[CRITICAL][Stream] 14.01.2019 14:23:52 [] (unknown:0) -   File "C:/Program Files/Slicer 4.10.0/bin/../lib/Slicer-4.10/qt-scripted-modules/DICOM.py", line 373, in onOpenDetailsPopup
[CRITICAL][Stream] 14.01.2019 14:23:52 [] (unknown:0) -     if not isinstance(self.detailsPopup, self.getSavedDICOMDetailsWidgetType()):
[CRITICAL][Stream] 14.01.2019 14:23:52 [] (unknown:0) - AttributeError: DICOMWidget instance has no attribute 'detailsPopup'
[CRITICAL][Stream] 14.01.2019 14:23:52 [] (unknown:0) - Traceback (most recent call last):
[CRITICAL][Stream] 14.01.2019 14:23:52 [] (unknown:0) -   File "C:/Program Files/Slicer 4.10.0/bin/../lib/Slicer-4.10/qt-scripted-modules/DICOM.py", line 206, in dropEvent
[CRITICAL][Stream] 14.01.2019 14:23:52 [] (unknown:0) -     dicomWidget.detailsPopup.dicomBrowser.importDirectories(self.directoriesToAdd)
[CRITICAL][Stream] 14.01.2019 14:23:52 [] (unknown:0) - AttributeError: DICOMWidget instance has no attribute 'detailsPopup'
</code></pre>
</details>

---

## Post #2 by @pieper (2019-01-14 17:58 UTC)

<p>Looks like it can’t create this directory.  Do you have a Documents folder there?</p>
<p><em><strong>C:/Users/CormacClarke/Documents\SlicerDICOMDatabase’</strong></em></p>

---

## Post #3 by @cormacclarke (2019-01-15 08:43 UTC)

<p>Thanks for your reply Steve<br>
No there isn’t any docs folder in that location</p>

---

## Post #4 by @pieper (2019-01-15 13:18 UTC)

<p>Does creating C:/Users/CormacClarke/Documents fix the problem?</p>

---

## Post #5 by @cormacclarke (2019-01-15 14:33 UTC)

<p>Hi Steve,</p>
<p>Got it fixed.<br>
I set up the folder SlicerDICOMDatabase in the folder.<br>
Also had to make slicerapp-real.exe an approved app.</p>
<p>Thanks for your help</p>

---
