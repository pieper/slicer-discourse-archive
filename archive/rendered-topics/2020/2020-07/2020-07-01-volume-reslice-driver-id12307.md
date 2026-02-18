# Volume Reslice Driver

**Topic ID**: 12307
**Date**: 2020-07-01
**URL**: https://discourse.slicer.org/t/volume-reslice-driver/12307

---

## Post #1 by @mariaelh (2020-07-01 00:08 UTC)

<p>Does this module still exist? I cannot find it. Is it under another name?</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2020-07-01 00:09 UTC)

<p>Volume reslice driver module is provided by SlicerIGT extension.</p>

---

## Post #3 by @mariaelh (2020-07-01 00:27 UTC)

<p>I did download it. However, it only contains:<br>
1- Fiducials- Model registration<br>
2- Model Registration<br>
3- Viewpoint</p>
<p>Volume Reslice Driver does not show for me. What can I do?</p>

---

## Post #4 by @lassoan (2020-07-01 00:38 UTC)

<p>You can try to uninstall and reinstall SlicerIGT. Make sure you wait for the installation to complete (do not click “Close” button, but wait for “Restart” button to become active).</p>
<p>Which Slicer version and operating system do you use?</p>

---

## Post #5 by @mariaelh (2020-07-01 01:08 UTC)

<p>Slicer 4.10.2<br>
Windows 10 Home</p>

---

## Post #6 by @lassoan (2020-07-01 04:39 UTC)

<p>I’ve just tested and SlicerIGT extension is available and installs correctly for SLicer-4.10.2. If uninstalling and reinstalling (waiting for “Restart”) does not fix the issue then please send the application log (menu: Help / Report a bug).</p>

---

## Post #7 by @mariaelh (2020-07-01 12:26 UTC)

<p>Uninstall and reinstall did not work.</p>
<p>[DEBUG][Qt] 01.07.2020 08:24:11 [] (unknown:0) - Session start time …: 2020-07-01 08:24:11<br>
[DEBUG][Qt] 01.07.2020 08:24:11 [] (unknown:0) - Slicer version …: 4.10.2 (revision 28257) win-amd64 - installed release<br>
[DEBUG][Qt] 01.07.2020 08:24:11 [] (unknown:0) - Operating system …: Windows /  Personal /  (Build 9200) - 64-bit<br>
[DEBUG][Qt] 01.07.2020 08:24:11 [] (unknown:0) - Memory …: 8113 MB physical, 9905 MB virtual<br>
[DEBUG][Qt] 01.07.2020 08:24:11 [] (unknown:0) - CPU …: GenuineIntel , 8 cores, 8 logical processors<br>
[DEBUG][Qt] 01.07.2020 08:24:11 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 01.07.2020 08:24:11 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 01.07.2020 08:24:11 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 01.07.2020 08:24:11 [] (unknown:0) - Additional module paths …: C:/Users/maria/AppData/Roaming/NA-MIC/Extensions-28257/SlicerOpenIGTLink/lib/Slicer-4.10/qt-loadable-modules, C:/Users/maria/AppData/Roaming/NA-MIC/Extensions-28257/SlicerOpenIGTLink/lib/Slicer-4.10/qt-scripted-modules, C:/Users/maria/AppData/Roaming/NA-MIC/Extensions-28257/SlicerIGT/lib/Slicer-4.10/qt-loadable-modules, C:/Users/maria/AppData/Roaming/NA-MIC/Extensions-28257/SlicerIGT/lib/Slicer-4.10/qt-scripted-modules<br>
[CRITICAL][Qt] 01.07.2020 08:24:13 [] (unknown:0) -   Error(s):<br>
Cannot load library C:\Users\maria\AppData\Roaming\NA-MIC\Extensions-28257\SlicerOpenIGTLink\lib\Slicer-4.10\qt-loadable-modules\qSlicerOpenIGTLinkIFModule.dll: The specified module could not be found.<br>
[CRITICAL][Qt] 01.07.2020 08:24:13 [] (unknown:0) -   Error(s):<br>
Cannot load library C:\Users\maria\AppData\Roaming\NA-MIC\Extensions-28257\SlicerOpenIGTLink\lib\Slicer-4.10\qt-loadable-modules\qSlicerOpenIGTLinkRemoteModule.dll: The specified module could not be found.<br>
[CRITICAL][Qt] 01.07.2020 08:24:13 [] (unknown:0) -   Error(s):<br>
Cannot load library C:\Users\maria\AppData\Roaming\NA-MIC\Extensions-28257\SlicerOpenIGTLink\lib\Slicer-4.10\qt-loadable-modules\qSlicerPlusRemoteModule.dll: The specified module could not be found.<br>
[CRITICAL][Qt] 01.07.2020 08:24:13 [] (unknown:0) -   Error(s):<br>
Cannot load library C:\Users\maria\AppData\Roaming\NA-MIC\Extensions-28257\SlicerIGT\lib\Slicer-4.10\qt-loadable-modules\qSlicerBreachWarningModule.dll: The specified module could not be found.<br>
[CRITICAL][Qt] 01.07.2020 08:24:13 [] (unknown:0) -   Error(s):<br>
Cannot load library C:\Users\maria\AppData\Roaming\NA-MIC\Extensions-28257\SlicerIGT\lib\Slicer-4.10\qt-loadable-modules\qSlicerCollectPointsModule.dll: The specified module could not be found.<br>
[CRITICAL][Qt] 01.07.2020 08:24:13 [] (unknown:0) -   Error(s):<br>
Cannot load library C:\Users\maria\AppData\Roaming\NA-MIC\Extensions-28257\SlicerIGT\lib\Slicer-4.10\qt-loadable-modules\qSlicerCreateModelsModule.dll: The specified module could not be found.<br>
[CRITICAL][Qt] 01.07.2020 08:24:13 [] (unknown:0) -   Error(s):<br>
Cannot load library C:\Users\maria\AppData\Roaming\NA-MIC\Extensions-28257\SlicerIGT\lib\Slicer-4.10\qt-loadable-modules\qSlicerFiducialRegistrationWizardModule.dll: The specified module could not be found.<br>
[CRITICAL][Qt] 01.07.2020 08:24:13 [] (unknown:0) -   Error(s):<br>
Cannot load library C:\Users\maria\AppData\Roaming\NA-MIC\Extensions-28257\SlicerIGT\lib\Slicer-4.10\qt-loadable-modules\qSlicerPathExplorerModule.dll: The specified module could not be found.<br>
[CRITICAL][Qt] 01.07.2020 08:24:13 [] (unknown:0) -   Error(s):<br>
Cannot load library C:\Users\maria\AppData\Roaming\NA-MIC\Extensions-28257\SlicerIGT\lib\Slicer-4.10\qt-loadable-modules\qSlicerPivotCalibrationModule.dll: The specified module could not be found.<br>
[CRITICAL][Qt] 01.07.2020 08:24:13 [] (unknown:0) -   Error(s):<br>
Cannot load library C:\Users\maria\AppData\Roaming\NA-MIC\Extensions-28257\SlicerIGT\lib\Slicer-4.10\qt-loadable-modules\qSlicerTransformProcessorModule.dll: The specified module could not be found.<br>
[CRITICAL][Qt] 01.07.2020 08:24:13 [] (unknown:0) -   Error(s):<br>
Cannot load library C:\Users\maria\AppData\Roaming\NA-MIC\Extensions-28257\SlicerIGT\lib\Slicer-4.10\qt-loadable-modules\qSlicerUltrasoundSnapshotsModule.dll: The specified module could not be found.<br>
[CRITICAL][Qt] 01.07.2020 08:24:13 [] (unknown:0) -   Error(s):<br>
Cannot load library C:\Users\maria\AppData\Roaming\NA-MIC\Extensions-28257\SlicerIGT\lib\Slicer-4.10\qt-loadable-modules\qSlicerVolumeResliceDriverModule.dll: The specified module could not be found.<br>
[CRITICAL][Qt] 01.07.2020 08:24:14 [] (unknown:0) -   Error(s):<br>
Cannot load library C:\Users\maria\AppData\Roaming\NA-MIC\Extensions-28257\SlicerIGT\lib\Slicer-4.10\qt-loadable-modules\qSlicerWatchdogModule.dll: The specified module could not be found.<br>
[DEBUG][Python] 01.07.2020 08:24:15 [Python] (C:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[WARNING][Qt] 01.07.2020 08:24:15 [] (unknown:0) - When loading module  “BreachWarningSelfTest” , the dependency “CreateModels” failed to be loaded.<br>
[CRITICAL][Stream] 01.07.2020 08:24:16 [] (unknown:0) - DLL load failed: The specified module could not be found.<br>
[CRITICAL][Stream] 01.07.2020 08:24:16 [] (unknown:0) - DLL load failed: The specified module could not be found.<br>
[CRITICAL][Stream] 01.07.2020 08:24:16 [] (unknown:0) - DLL load failed: The specified module could not be found.<br>
[CRITICAL][Stream] 01.07.2020 08:24:16 [] (unknown:0) - DLL load failed: The specified module could not be found.<br>
[CRITICAL][Stream] 01.07.2020 08:24:16 [] (unknown:0) - DLL load failed: The specified module could not be found.<br>
[CRITICAL][Stream] 01.07.2020 08:24:16 [] (unknown:0) - DLL load failed: The specified module could not be found.<br>
[CRITICAL][Stream] 01.07.2020 08:24:16 [] (unknown:0) - DLL load failed: The specified module could not be found.<br>
[CRITICAL][Stream] 01.07.2020 08:24:16 [] (unknown:0) - DLL load failed: The specified module could not be found.<br>
[CRITICAL][Stream] 01.07.2020 08:24:17 [] (unknown:0) - DLL load failed: The specified module could not be found.<br>
[CRITICAL][Stream] 01.07.2020 08:24:17 [] (unknown:0) - DLL load failed: The specified module could not be found.<br>
[CRITICAL][Stream] 01.07.2020 08:24:17 [] (unknown:0) - DLL load failed: The specified module could not be found.<br>
[CRITICAL][Stream] 01.07.2020 08:24:17 [] (unknown:0) - DLL load failed: The specified module could not be found.<br>
[CRITICAL][Stream] 01.07.2020 08:24:17 [] (unknown:0) - DLL load failed: The specified module could not be found.<br>
[CRITICAL][Stream] 01.07.2020 08:24:17 [] (unknown:0) - DLL load failed: The specified module could not be found.<br>
[CRITICAL][Stream] 01.07.2020 08:24:17 [] (unknown:0) - DLL load failed: The specified module could not be found.<br>
[CRITICAL][Stream] 01.07.2020 08:24:17 [] (unknown:0) - DLL load failed: The specified module could not be found.<br>
[CRITICAL][Stream] 01.07.2020 08:24:17 [] (unknown:0) - DLL load failed: The specified module could not be found.<br>
[CRITICAL][Stream] 01.07.2020 08:24:17 [] (unknown:0) - DLL load failed: The specified module could not be found.<br>
[CRITICAL][Stream] 01.07.2020 08:24:17 [] (unknown:0) - DLL load failed: The specified module could not be found.<br>
[CRITICAL][Stream] 01.07.2020 08:24:17 [] (unknown:0) - DLL load failed: The specified module could not be found.<br>
[DEBUG][Python] 01.07.2020 08:24:18 [Python] (C:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 01.07.2020 08:24:18 [Python] (C:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[WARNING][Qt] 01.07.2020 08:24:18 [] (unknown:0) - When loading module  “UltrasoundRemoteControl” , the dependency “OpenIGTLinkRemote” failed to be loaded.<br>
[DEBUG][Qt] 01.07.2020 08:24:18 [] (unknown:0) - Switch to module:  “Welcome”</p>

---

## Post #8 by @lassoan (2020-07-17 19:25 UTC)

<p>You can try installing Visual C++ Runtime libraries: <a href="https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads">https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads</a></p>
<p>If that does not work, please try the latest Slicer Preview Release.</p>

---
