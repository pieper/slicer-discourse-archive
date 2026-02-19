---
topic_id: 11881
title: "Slicerrt Dicom Rt Import Issue"
date: 2020-06-05
url: https://discourse.slicer.org/t/11881
---

# SlicerRT DICOM RT import issue

**Topic ID**: 11881
**Date**: 2020-06-05
**URL**: https://discourse.slicer.org/t/slicerrt-dicom-rt-import-issue/11881

---

## Post #1 by @martin (2020-06-05 16:19 UTC)

<p>Hello All,</p>
<p>I tried to import the DICOM RT in 3Dslicer with SlicerRT module, however the log shows the module seems have some issues. I have tried to reinstall the 3dSlicer and the SlicerRT module, but the error still appear. please help<br>
thanks</p>
<p>Martin</p>
<p>[DEBUG][Qt] 05.06.2020 12:21:28 [] (unknown:0) - Session start time …: 2020-06-05 12:21:28<br>
[DEBUG][Qt] 05.06.2020 12:21:28 [] (unknown:0) - Slicer version …: 4.10.2 (revision 28257) win-amd64 - installed release<br>
[DEBUG][Qt] 05.06.2020 12:21:28 [] (unknown:0) - Operating system …: Windows /  Personal /  (Build 9200) - 64-bit<br>
[DEBUG][Qt] 05.06.2020 12:21:28 [] (unknown:0) - Memory …: 16242 MB physical, 18674 MB virtual<br>
[DEBUG][Qt] 05.06.2020 12:21:28 [] (unknown:0) - CPU …: GenuineIntel , 12 cores, 12 logical processors<br>
[DEBUG][Qt] 05.06.2020 12:21:28 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 05.06.2020 12:21:28 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 05.06.2020 12:21:28 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 05.06.2020 12:21:28 [] (unknown:0) - Additional module paths …: C:/Users/user/AppData/Roaming/NA-MIC/Extensions-28257/SlicerRT/lib/Slicer-4.10/cli-modules, C:/Users/user/AppData/Roaming/NA-MIC/Extensions-28257/SlicerRT/lib/Slicer-4.10/qt-loadable-modules, C:/Users/user/AppData/Roaming/NA-MIC/Extensions-28257/SlicerRT/lib/Slicer-4.10/qt-scripted-modules<br>
[CRITICAL][Qt] 05.06.2020 12:21:29 [] (unknown:0) -   Error(s):<br>
Cannot load library C:\Users\user\AppData\Roaming\NA-MIC\Extensions-28257\SlicerRT\lib\Slicer-4.10\qt-loadable-modules\qSlicerBeamsModule.dll: The specified module could not be found.<br>
[CRITICAL][Qt] 05.06.2020 12:21:29 [] (unknown:0) -   Error(s):<br>
Cannot load library C:\Users\user\AppData\Roaming\NA-MIC\Extensions-28257\SlicerRT\lib\Slicer-4.10\qt-loadable-modules\qSlicerDicomRtImportExportModule.dll: The specified module could not be found.<br>
[CRITICAL][Qt] 05.06.2020 12:21:29 [] (unknown:0) -   Error(s):<br>
Cannot load library C:\Users\user\AppData\Roaming\NA-MIC\Extensions-28257\SlicerRT\lib\Slicer-4.10\qt-loadable-modules\qSlicerDicomSroImportModule.dll: The specified module could not be found.<br>
[CRITICAL][Qt] 05.06.2020 12:21:29 [] (unknown:0) -   Error(s):<br>
Cannot load library C:\Users\user\AppData\Roaming\NA-MIC\Extensions-28257\SlicerRT\lib\Slicer-4.10\qt-loadable-modules\qSlicerDoseAccumulationModule.dll: The specified module could not be found.<br>
[CRITICAL][Qt] 05.06.2020 12:21:29 [] (unknown:0) -   Error(s):<br>
Cannot load library C:\Users\user\AppData\Roaming\NA-MIC\Extensions-28257\SlicerRT\lib\Slicer-4.10\qt-loadable-modules\qSlicerDoseComparisonModule.dll: The specified module could not be found.<br>
[CRITICAL][Qt] 05.06.2020 12:21:29 [] (unknown:0) -   Error(s):<br>
Cannot load library C:\Users\user\AppData\Roaming\NA-MIC\Extensions-28257\SlicerRT\lib\Slicer-4.10\qt-loadable-modules\qSlicerDoseVolumeHistogramModule.dll: The specified module could not be found.<br>
[CRITICAL][Qt] 05.06.2020 12:21:29 [] (unknown:0) -   Error(s):<br>
Cannot load library C:\Users\user\AppData\Roaming\NA-MIC\Extensions-28257\SlicerRT\lib\Slicer-4.10\qt-loadable-modules\qSlicerDosxyzNrc3dDoseFileReaderModule.dll: The specified module could not be found.<br>
[CRITICAL][Qt] 05.06.2020 12:21:29 [] (unknown:0) -   Error(s):<br>
Cannot load library C:\Users\user\AppData\Roaming\NA-MIC\Extensions-28257\SlicerRT\lib\Slicer-4.10\qt-loadable-modules\qSlicerExternalBeamPlanningModule.dll: The specified module could not be found.<br>
[CRITICAL][Qt] 05.06.2020 12:21:30 [] (unknown:0) -   Error(s):<br>
Cannot load library C:\Users\user\AppData\Roaming\NA-MIC\Extensions-28257\SlicerRT\lib\Slicer-4.10\qt-loadable-modules\qSlicerIsodoseModule.dll: The specified module could not be found.<br>
[CRITICAL][Qt] 05.06.2020 12:21:30 [] (unknown:0) -   Error(s):<br>
Cannot load library C:\Users\user\AppData\Roaming\NA-MIC\Extensions-28257\SlicerRT\lib\Slicer-4.10\qt-loadable-modules\qSlicerPlanarImageModule.dll: The specified module could not be found.<br>
[CRITICAL][Qt] 05.06.2020 12:21:30 [] (unknown:0) -   Error(s):<br>
Cannot load library C:\Users\user\AppData\Roaming\NA-MIC\Extensions-28257\SlicerRT\lib\Slicer-4.10\qt-loadable-modules\qSlicerPlastimatchPyModule.dll: The specified module could not be found.<br>
[CRITICAL][Qt] 05.06.2020 12:21:30 [] (unknown:0) -   Error(s):<br>
Cannot load library C:\Users\user\AppData\Roaming\NA-MIC\Extensions-28257\SlicerRT\lib\Slicer-4.10\qt-loadable-modules\qSlicerPlmProtonDoseEngineModule.dll: The specified module could not be found.<br>
[CRITICAL][Qt] 05.06.2020 12:21:30 [] (unknown:0) -   Error(s):<br>
Cannot load library C:\Users\user\AppData\Roaming\NA-MIC\Extensions-28257\SlicerRT\lib\Slicer-4.10\qt-loadable-modules\qSlicerSegmentComparisonModule.dll: The specified module could not be found.<br>
[CRITICAL][Qt] 05.06.2020 12:21:30 [] (unknown:0) -   Error(s):<br>
Cannot load library C:\Users\user\AppData\Roaming\NA-MIC\Extensions-28257\SlicerRT\lib\Slicer-4.10\qt-loadable-modules\qSlicerSegmentMorphologyModule.dll: The specified module could not be found.<br>
[CRITICAL][Qt] 05.06.2020 12:21:30 [] (unknown:0) -   Error(s):<br>
Cannot load library C:\Users\user\AppData\Roaming\NA-MIC\Extensions-28257\SlicerRT\lib\Slicer-4.10\qt-loadable-modules\qSlicerVffFileReaderModule.dll: The specified module could not be found.<br>
[DEBUG][Python] 05.06.2020 12:21:31 [Python] (C:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[WARNING][Qt] 05.06.2020 12:21:31 [] (unknown:0) - When loading module  “BatchStructureSetConversion” , the dependency “DicomRtImportExport” failed to be loaded.<br>
[CRITICAL][Stream] 05.06.2020 12:21:31 [] (unknown:0) - DLL load failed: The specified module could not be found.<br>
[CRITICAL][Stream] 05.06.2020 12:21:31 [] (unknown:0) - DLL load failed: The specified module could not be found.<br>
[CRITICAL][Stream] 05.06.2020 12:21:31 [] (unknown:0) - DLL load failed: The specified module could not be found.<br>
[CRITICAL][Stream] 05.06.2020 12:21:31 [] (unknown:0) - DLL load failed: The specified module could not be found.<br>
[CRITICAL][Stream] 05.06.2020 12:21:31 [] (unknown:0) - DLL load failed: The specified module could not be found.<br>
[CRITICAL][Stream] 05.06.2020 12:21:31 [] (unknown:0) - DLL load failed: The specified module could not be found.<br>
[CRITICAL][Stream] 05.06.2020 12:21:32 [] (unknown:0) - DLL load failed: The specified module could not be found.<br>
[CRITICAL][Stream] 05.06.2020 12:21:32 [] (unknown:0) - DLL load failed: The specified module could not be found.<br>
[CRITICAL][Stream] 05.06.2020 12:21:32 [] (unknown:0) - DLL load failed: The specified module could not be found.<br>
[CRITICAL][Stream] 05.06.2020 12:21:32 [] (unknown:0) - DLL load failed: The specified module could not be found.<br>
[CRITICAL][Stream] 05.06.2020 12:21:32 [] (unknown:0) - DLL load failed: The specified module could not be found.<br>
[CRITICAL][Stream] 05.06.2020 12:21:32 [] (unknown:0) - DLL load failed: The specified module could not be found.<br>
[CRITICAL][Stream] 05.06.2020 12:21:32 [] (unknown:0) - DLL load failed: The specified module could not be found.<br>
[CRITICAL][Stream] 05.06.2020 12:21:32 [] (unknown:0) - DLL load failed: The specified module could not be found.<br>
[CRITICAL][Stream] 05.06.2020 12:21:32 [] (unknown:0) - DLL load failed: The specified module could not be found.<br>
[CRITICAL][Stream] 05.06.2020 12:21:32 [] (unknown:0) - DLL load failed: The specified module could not be found.<br>
[CRITICAL][Stream] 05.06.2020 12:21:32 [] (unknown:0) - DLL load failed: The specified module could not be found.<br>
[CRITICAL][Stream] 05.06.2020 12:21:32 [] (unknown:0) - DLL load failed: The specified module could not be found.<br>
[CRITICAL][Stream] 05.06.2020 12:21:32 [] (unknown:0) - DLL load failed: The specified module could not be found.<br>
[CRITICAL][Stream] 05.06.2020 12:21:32 [] (unknown:0) - DLL load failed: The specified module could not be found.<br>
[CRITICAL][Stream] 05.06.2020 12:21:32 [] (unknown:0) - DLL load failed: The specified module could not be found.<br>
[CRITICAL][Stream] 05.06.2020 12:21:32 [] (unknown:0) - DLL load failed: The specified module could not be found.<br>
[CRITICAL][Stream] 05.06.2020 12:21:32 [] (unknown:0) - DLL load failed: The specified module could not be found.<br>
[WARNING][Qt] 05.06.2020 12:21:32 [] (unknown:0) - When loading module  “DvhComparison” , the dependency “DoseVolumeHistogram” failed to be loaded.<br>
[WARNING][Qt] 05.06.2020 12:21:32 [] (unknown:0) - When loading module  “IGRTWorkflow_SelfTest” , the dependency “DicomRtImportExport” failed to be loaded.<br>
[DEBUG][Python] 05.06.2020 12:21:32 [Python] (C:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 05.06.2020 12:21:32 [Python] (C:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 05.06.2020 12:21:32 [] (unknown:0) - Switch to module:  “Welcome”<br>
[WARNING][Qt] 05.06.2020 12:28:46 [] (unknown:0) - An OpenGL Core Profile was requested, but it is not supported on the current platform. Falling back to a non-Core profile. Note that this might cause rendering issues.<br>
[WARNING][Qt] 05.06.2020 12:28:46 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 05.06.2020 12:28:46 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 05.06.2020 12:28:46 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[DEBUG][Qt] 05.06.2020 12:29:20 [] (unknown:0) - Switch to module:  “Models”<br>
[DEBUG][Qt] 05.06.2020 12:29:27 [] (unknown:0) - Switch to module:  “DICOM”<br>
[WARNING][Qt] 05.06.2020 12:29:37 [] (unknown:0) - QSqlDatabasePrivate::removeDatabase: connection ‘SLICER’ is still in use, all queries will cease to work.<br>
[WARNING][Qt] 05.06.2020 12:29:37 [] (unknown:0) - QSqlDatabasePrivate::addDatabase: duplicate connection name ‘SLICER’, old connection removed.<br>
[DEBUG][Python] 05.06.2020 12:29:47 [Python] (C:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:455) - MultiVolumeImportPlugin::examine<br>
[DEBUG][Python] 05.06.2020 12:29:54 [Python] (C:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:495) - DICOMMultiVolumePlugin found 1 multivolumes!<br>
[DEBUG][Python] 05.06.2020 12:29:55 [Python] (C:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:455) - MultiVolumeImportPlugin::examine<br>
[DEBUG][Python] 05.06.2020 12:29:58 [Python] (C:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:495) - DICOMMultiVolumePlugin found 0 multivolumes!<br>
[DEBUG][Python] 05.06.2020 12:29:58 [Python] (C:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:165) - MultiVolumeImportPlugin:examineMultiseries<br>
[DEBUG][Python] 05.06.2020 12:29:58 [Python] (C:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:170) - DICOMMultiVolumePlugin found 0 multivolumes!<br>
[WARNING][Python] 05.06.2020 12:29:58 [Python] (C:\Program Files\Slicer 4.10.2\bin\Python\slicer\util.py:1110) - Warning: Plugin failed: DicomSroImportPlugin</p>
<p>See python console for error message.<br>
[CRITICAL][Stream] 05.06.2020 12:29:58 [] (unknown:0) - Traceback (most recent call last):<br>
[CRITICAL][Stream] 05.06.2020 12:29:58 [] (unknown:0) -   File “C:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\DICOMLib\DICOMWidgets.py”, line 737, in getLoadablesFromFileLists<br>
[CRITICAL][Stream] 05.06.2020 12:29:58 [] (unknown:0) -     loadablesByPlugin[plugin] = plugin.examine(fileLists)<br>
[CRITICAL][Stream] 05.06.2020 12:29:58 [] (unknown:0) -   File “C:/Users/user/AppData/Roaming/NA-MIC/Extensions-28257/SlicerRT/lib/Slicer-4.10/qt-scripted-modules/DicomSroImportPlugin.py”, line 30, in examine<br>
[CRITICAL][Stream] 05.06.2020 12:29:58 [] (unknown:0) -     examineInfo = slicer.vtkDICOMImportInfo()<br>
[CRITICAL][Stream] 05.06.2020 12:29:58 [] (unknown:0) - AttributeError: ‘module’ object has no attribute ‘vtkDICOMImportInfo’<br>
[CRITICAL][Stream] 05.06.2020 12:29:58 [] (unknown:0) - Warning: Plugin failed: DicomSroImportPlugin<br>
[CRITICAL][Stream] 05.06.2020 12:29:58 [] (unknown:0) -<br>
[CRITICAL][Stream] 05.06.2020 12:29:58 [] (unknown:0) - See python console for error message.<br>
[INFO][Stream] 05.06.2020 12:30:01 [] (unknown:0) - DICOM Plugin failed: ‘module’ object has no attribute ‘vtkDICOMImportInfo’<br>
[WARNING][Python] 05.06.2020 12:30:01 [Python] (C:\Program Files\Slicer 4.10.2\bin\Python\slicer\util.py:1110) - Warning: Plugin failed: DicomRtImportExportPlugin</p>
<p>See python console for error message.<br>
[CRITICAL][Stream] 05.06.2020 12:30:01 [] (unknown:0) - Traceback (most recent call last):<br>
[CRITICAL][Stream] 05.06.2020 12:30:01 [] (unknown:0) -   File “C:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\DICOMLib\DICOMWidgets.py”, line 733, in getLoadablesFromFileLists<br>
[CRITICAL][Stream] 05.06.2020 12:30:01 [] (unknown:0) -     loadablesByPlugin[plugin] = plugin.examineForImport(fileLists)<br>
[CRITICAL][Stream] 05.06.2020 12:30:01 [] (unknown:0) -   File “C:/Users/user/AppData/Roaming/NA-MIC/Extensions-28257/SlicerRT/lib/Slicer-4.10/qt-scripted-modules/DicomRtImportExportPlugin.py”, line 41, in examineForImport<br>
[CRITICAL][Stream] 05.06.2020 12:30:01 [] (unknown:0) -     slicer.modules.dicomrtimportexport.logic().ExamineForLoad(vtkFileList, loadablesCollection)<br>
[CRITICAL][Stream] 05.06.2020 12:30:01 [] (unknown:0) - AttributeError: ‘module’ object has no attribute ‘dicomrtimportexport’<br>
[CRITICAL][Stream] 05.06.2020 12:30:01 [] (unknown:0) - Warning: Plugin failed: DicomRtImportExportPlugin<br>
[CRITICAL][Stream] 05.06.2020 12:30:01 [] (unknown:0) -<br>
[CRITICAL][Stream] 05.06.2020 12:30:01 [] (unknown:0) - See python console for error message.<br>
[INFO][Stream] 05.06.2020 12:30:02 [] (unknown:0) - DICOM Plugin failed: ‘module’ object has no attribute ‘dicomrtimportexport’</p>

---

## Post #2 by @cpinter (2020-06-05 18:55 UTC)

<p>It seems that the SlicerRT extension has not been successfully installed. Can you try uninstalling and installing it again?</p>

---

## Post #3 by @lassoan (2020-06-05 19:02 UTC)

<aside class="quote no-group" data-username="martin" data-post="1" data-topic="11881">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/martin/48/5422_2.png" class="avatar"> martin:</div>
<blockquote>
<p>DLL load failed: The specified module could not be found</p>
</blockquote>
</aside>
<p>The error looks very similar to <a href="https://github.com/Slicer/Slicer/issues/4958">this issue</a>. Could you check if installing <a href="https://aka.ms/vs/16/release/vc_redist.x64.exe">Microsoft Visual Studio redistributables</a> fixes the problem?</p>

---

## Post #4 by @erin5116 (2020-06-19 01:52 UTC)

<p>I had the same issue, and it worked after installing Microsoft Visual Studio redistributables.</p>

---

## Post #5 by @lassoan (2020-06-23 02:11 UTC)

<p>Thank you, this information is very useful. I’ve filed a bug report <a href="https://github.com/Slicer/Slicer/issues/5001">here</a>.</p>

---
