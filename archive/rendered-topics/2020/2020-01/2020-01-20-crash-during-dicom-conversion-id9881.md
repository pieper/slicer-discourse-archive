# Crash during DICOM conversion

**Topic ID**: 9881
**Date**: 2020-01-20
**URL**: https://discourse.slicer.org/t/crash-during-dicom-conversion/9881

---

## Post #1 by @Stoberoth (2020-01-20 11:11 UTC)

<p>Problem report for Slicer 4.11.0-2020-01-08 win-amd64: [please describe expected and actual behavior]<br>
I report to you a program interrupt with the following steps :</p>
<ol>
<li>i load a DICOM file</li>
<li>i convert this file with the castImageFilter to float and the software crash</li>
</ol>
<p>[DEBUG][Qt] 20.01.2020 11:06:20 [] (unknown:0) - Session start time …: 2020-01-20 11:06:20<br>
[DEBUG][Qt] 20.01.2020 11:06:20 [] (unknown:0) - Slicer version …: 4.11.0-2020-01-08 (revision 28723) win-amd64 - installed release<br>
[DEBUG][Qt] 20.01.2020 11:06:21 [] (unknown:0) - Operating system …: Windows /  Professional /  (Build 9200) - 64-bit<br>
[DEBUG][Qt] 20.01.2020 11:06:21 [] (unknown:0) - Memory …: 32626 MB physical, 37746 MB virtual<br>
[DEBUG][Qt] 20.01.2020 11:06:21 [] (unknown:0) - CPU …: GenuineIntel , 12 cores, 12 logical processors<br>
[DEBUG][Qt] 20.01.2020 11:06:21 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 20.01.2020 11:06:21 [] (unknown:0) - Qt configuration …: version 5.10.1, with SSL, requested OpenGL 3.2 (compatibility profile)<br>
[DEBUG][Qt] 20.01.2020 11:06:21 [] (unknown:0) - Developer mode enabled …: yes<br>
[DEBUG][Qt] 20.01.2020 11:06:21 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 20.01.2020 11:06:21 [] (unknown:0) - Application path …: C:/Users/Nicolas Lenoir/AppData/Local/NA-MIC/Slicer 4.11.0-2020-01-08/bin<br>
[DEBUG][Qt] 20.01.2020 11:06:21 [] (unknown:0) - Additional module paths …: (none)<br>
[DEBUG][Python] 20.01.2020 11:06:22 [Python] (C:\Users\Nicolas Lenoir\AppData\Local\NA-MIC\Slicer 4.11.0-2020-01-08\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 20.01.2020 11:06:22 [Python] (C:\Users\Nicolas Lenoir\AppData\Local\NA-MIC\Slicer 4.11.0-2020-01-08\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 20.01.2020 11:06:22 [Python] (C:\Users\Nicolas Lenoir\AppData\Local\NA-MIC\Slicer 4.11.0-2020-01-08\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 20.01.2020 11:06:22 [] (unknown:0) - Switch to module:  “Welcome”<br>
[DEBUG][Qt] 20.01.2020 11:06:26 [] (unknown:0) - Switch to module:  “DICOM”<br>
[DEBUG][Python] 20.01.2020 11:06:34 [Python] (C:/Users/Nicolas Lenoir/AppData/Local/NA-MIC/Slicer 4.11.0-2020-01-08/bin/…/lib/Slicer-4.11/qt-scripted-modules/MultiVolumeImporterPlugin.py:456) - MultiVolumeImportPlugin::examine<br>
[DEBUG][Python] 20.01.2020 11:06:36 [Python] (C:/Users/Nicolas Lenoir/AppData/Local/NA-MIC/Slicer 4.11.0-2020-01-08/bin/…/lib/Slicer-4.11/qt-scripted-modules/MultiVolumeImporterPlugin.py:496) - DICOMMultiVolumePlugin found 1 multivolumes!<br>
[DEBUG][Python] 20.01.2020 11:06:39 [Python] (C:/Users/Nicolas Lenoir/AppData/Local/NA-MIC/Slicer 4.11.0-2020-01-08/bin/…/lib/Slicer-4.11/qt-scripted-modules/MultiVolumeImporterPlugin.py:168) - MultiVolumeImportPlugin:examineMultiseries<br>
[DEBUG][Python] 20.01.2020 11:06:39 [Python] (C:/Users/Nicolas Lenoir/AppData/Local/NA-MIC/Slicer 4.11.0-2020-01-08/bin/…/lib/Slicer-4.11/qt-scripted-modules/MultiVolumeImporterPlugin.py:173) - DICOMMultiVolumePlugin found 0 multivolumes!<br>
[INFO][Python] 20.01.2020 11:06:39 [Python] (C:/Users/Nicolas Lenoir/AppData/Local/NA-MIC/Slicer 4.11.0-2020-01-08/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:319) - Loading with imageIOName: GDCM<br>
[INFO][Python] 20.01.2020 11:07:37 [Python] (C:/Users/Nicolas Lenoir/AppData/Local/NA-MIC/Slicer 4.11.0-2020-01-08/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:391) - Window/level found in DICOM tags (center=40.0, width=600.0) has been applied to volume 3: Aorte<br>
[DEBUG][Python] 20.01.2020 11:07:38 [Python] (C:/Users/Nicolas Lenoir/AppData/Local/NA-MIC/Slicer 4.11.0-2020-01-08/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:722) - Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 3.05176e-06 mm, tolerance threshold is 0.001 mm).<br>
[INFO][Stream] 20.01.2020 11:06:39 [] (unknown:0) - Loading with imageIOName: GDCM<br>
[INFO][Stream] 20.01.2020 11:07:37 [] (unknown:0) - Window/level found in DICOM tags (center=40.0, width=600.0) has been applied to volume 3: Aorte<br>
[DEBUG][Python] 20.01.2020 11:07:38 [Python] (C:/Users/Nicolas Lenoir/AppData/Local/NA-MIC/Slicer 4.11.0-2020-01-08/bin/…/lib/Slicer-4.11/qt-scripted-modules/MultiVolumeImporterPlugin.py:456) - MultiVolumeImportPlugin::examine<br>
[DEBUG][Python] 20.01.2020 11:07:40 [Python] (C:/Users/Nicolas Lenoir/AppData/Local/NA-MIC/Slicer 4.11.0-2020-01-08/bin/…/lib/Slicer-4.11/qt-scripted-modules/MultiVolumeImporterPlugin.py:496) - DICOMMultiVolumePlugin found 1 multivolumes!<br>
[DEBUG][Python] 20.01.2020 11:07:43 [Python] (C:/Users/Nicolas Lenoir/AppData/Local/NA-MIC/Slicer 4.11.0-2020-01-08/bin/…/lib/Slicer-4.11/qt-scripted-modules/MultiVolumeImporterPlugin.py:168) - MultiVolumeImportPlugin:examineMultiseries<br>
[DEBUG][Python] 20.01.2020 11:07:43 [Python] (C:/Users/Nicolas Lenoir/AppData/Local/NA-MIC/Slicer 4.11.0-2020-01-08/bin/…/lib/Slicer-4.11/qt-scripted-modules/MultiVolumeImporterPlugin.py:173) - DICOMMultiVolumePlugin found 0 multivolumes!<br>
[INFO][Python] 20.01.2020 11:07:43 [Python] (C:/Users/Nicolas Lenoir/AppData/Local/NA-MIC/Slicer 4.11.0-2020-01-08/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:319) - Loading with imageIOName: GDCM<br>
[INFO][Python] 20.01.2020 11:08:55 [Python] (C:/Users/Nicolas Lenoir/AppData/Local/NA-MIC/Slicer 4.11.0-2020-01-08/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:391) - Window/level found in DICOM tags (center=40.0, width=600.0) has been applied to volume 3: Aorte_1<br>
[DEBUG][Python] 20.01.2020 11:08:55 [Python] (C:/Users/Nicolas Lenoir/AppData/Local/NA-MIC/Slicer 4.11.0-2020-01-08/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:722) - Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 3.05176e-06 mm, tolerance threshold is 0.001 mm).<br>
[INFO][Stream] 20.01.2020 11:07:43 [] (unknown:0) - Loading with imageIOName: GDCM<br>
[INFO][Stream] 20.01.2020 11:08:55 [] (unknown:0) - Window/level found in DICOM tags (center=40.0, width=600.0) has been applied to volume 3: Aorte_1<br>
[DEBUG][Qt] 20.01.2020 11:09:03 [] (unknown:0) - Switch to module:  “SimpleFilters”<br>
[INFO][Stream] 20.01.2020 11:09:13 [] (unknown:0) - myFilter = CastImageFilter()<br>
[INFO][Stream] 20.01.2020 11:09:13 [] (unknown:0) - myFilter.SetDebug(False)<br>
[INFO][Stream] 20.01.2020 11:09:13 [] (unknown:0) - myFilter.SetNumberOfThreads(12)<br>
[INFO][Stream] 20.01.2020 11:09:13 [] (unknown:0) - myFilter.SetOutputPixelType(6)<br>
[INFO][Stream] 20.01.2020 11:09:40 [] (unknown:0) - myFilter = MedianImageFilter()<br>
[INFO][Stream] 20.01.2020 11:09:40 [] (unknown:0) - myFilter.SetDebug(False)<br>
[INFO][Stream] 20.01.2020 11:09:40 [] (unknown:0) - myFilter.SetNumberOfThreads(12)<br>
[INFO][Stream] 20.01.2020 11:09:40 [] (unknown:0) - myFilter.SetRadius((5, 5, 1))<br>
[INFO][Stream] 20.01.2020 11:11:28 [] (unknown:0) - myFilter = UnsharpMaskImageFilter()<br>
[INFO][Stream] 20.01.2020 11:11:28 [] (unknown:0) - myFilter.SetAmount(7.0)<br>
[INFO][Stream] 20.01.2020 11:11:28 [] (unknown:0) - myFilter.SetDebug(False)<br>
[INFO][Stream] 20.01.2020 11:11:28 [] (unknown:0) - myFilter.SetNumberOfThreads(12)<br>
[INFO][Stream] 20.01.2020 11:11:28 [] (unknown:0) - myFilter.SetSigmas((15.0, 15.0, 1.0))<br>
[INFO][Stream] 20.01.2020 11:11:28 [] (unknown:0) - myFilter.SetThreshold(0.0)<br>
[INFO][Stream] 20.01.2020 11:11:42 [] (unknown:0) - myFilter = CastImageFilter()<br>
[INFO][Stream] 20.01.2020 11:11:42 [] (unknown:0) - myFilter.SetDebug(False)<br>
[INFO][Stream] 20.01.2020 11:11:42 [] (unknown:0) - myFilter.SetNumberOfThreads(12)<br>
[INFO][Stream] 20.01.2020 11:11:42 [] (unknown:0) - myFilter.SetOutputPixelType(6)<br>
[INFO][Stream] 20.01.2020 11:11:55 [] (unknown:0) - myFilter = UnsharpMaskImageFilter()<br>
[INFO][Stream] 20.01.2020 11:11:55 [] (unknown:0) - myFilter.SetAmount(7.0)<br>
[INFO][Stream] 20.01.2020 11:11:55 [] (unknown:0) - myFilter.SetDebug(False)<br>
[INFO][Stream] 20.01.2020 11:11:55 [] (unknown:0) - myFilter.SetNumberOfThreads(12)<br>
[INFO][Stream] 20.01.2020 11:11:55 [] (unknown:0) - myFilter.SetSigmas((15.0, 15.0, 1.0))<br>
[INFO][Stream] 20.01.2020 11:11:55 [] (unknown:0) - myFilter.SetThreshold(0.0)<br>
[INFO][Stream] 20.01.2020 11:12:21 [] (unknown:0) - myFilter = GradientMagnitudeImageFilter()<br>
[INFO][Stream] 20.01.2020 11:12:21 [] (unknown:0) - myFilter.SetDebug(False)<br>
[INFO][Stream] 20.01.2020 11:12:21 [] (unknown:0) - myFilter.SetNumberOfThreads(12)<br>
[INFO][Stream] 20.01.2020 11:12:21 [] (unknown:0) - myFilter.SetUseImageSpacing(True)<br>
[DEBUG][Qt] 20.01.2020 11:12:26 [] (unknown:0) - Switch to module:  “Data”<br>
[DEBUG][Qt] 20.01.2020 11:12:28 [] (unknown:0) - Switch to module:  “Volumes”<br>
[DEBUG][Qt] 20.01.2020 11:12:46 [] (unknown:0) - Switch to module:  “SimpleFilters”<br>
[INFO][Stream] 20.01.2020 11:13:15 [] (unknown:0) - myFilter = AddImageFilter()<br>
[INFO][Stream] 20.01.2020 11:13:15 [] (unknown:0) - myFilter.SetDebug(False)<br>
[INFO][Stream] 20.01.2020 11:13:15 [] (unknown:0) - myFilter.SetNumberOfThreads(12)<br>
[DEBUG][Qt] 20.01.2020 11:13:20 [] (unknown:0) - Switch to module:  “Data”<br>
[DEBUG][Qt] 20.01.2020 11:13:22 [] (unknown:0) - Switch to module:  “Volumes”<br>
[DEBUG][Qt] 20.01.2020 11:13:31 [] (unknown:0) - Switch to module:  “SimpleFilters”<br>
[DEBUG][Qt] 20.01.2020 11:13:45 [] (unknown:0) - class QColor __cdecl qSlicerSubjectHierarchyMarkupsPlugin::getDisplayColor(__int64,class QMap&lt;int,class QVariant&gt; &amp;) const : No display node<br>
[DEBUG][Qt] 20.01.2020 11:13:45 [] (unknown:0) - class QColor __cdecl qSlicerSubjectHierarchyMarkupsPlugin::getDisplayColor(__int64,class QMap&lt;int,class QVariant&gt; &amp;) const : No display node<br>
[INFO][Stream] 20.01.2020 11:13:57 [] (unknown:0) - myFilter = ConfidenceConnectedImageFilter()<br>
[INFO][Stream] 20.01.2020 11:13:57 [] (unknown:0) - myFilter.SetDebug(False)<br>
[INFO][Stream] 20.01.2020 11:13:57 [] (unknown:0) - myFilter.SetInitialNeighborhoodRadius(1)<br>
[INFO][Stream] 20.01.2020 11:13:57 [] (unknown:0) - myFilter.SetMultiplier(2.5)<br>
[INFO][Stream] 20.01.2020 11:13:57 [] (unknown:0) - myFilter.SetNumberOfIterations(1)<br>
[INFO][Stream] 20.01.2020 11:13:57 [] (unknown:0) - myFilter.SetNumberOfThreads(12)<br>
[INFO][Stream] 20.01.2020 11:13:57 [] (unknown:0) - myFilter.SetReplaceValue(1)<br>
[INFO][Stream] 20.01.2020 11:13:57 [] (unknown:0) - myFilter.SetSeedList(((278, 224, 342),))<br>
[DEBUG][Qt] 20.01.2020 11:14:45 [] (unknown:0) - Switch to module:  “Data”<br>
[DEBUG][Qt] 20.01.2020 11:15:32 [] (unknown:0) - Switch to module:  “SimpleFilters”<br>
[INFO][Stream] 20.01.2020 11:15:50 [] (unknown:0) - myFilter = BinaryThresholdImageFilter()<br>
[INFO][Stream] 20.01.2020 11:15:50 [] (unknown:0) - myFilter.SetDebug(False)<br>
[INFO][Stream] 20.01.2020 11:15:50 [] (unknown:0) - myFilter.SetInsideValue(1)<br>
[INFO][Stream] 20.01.2020 11:15:50 [] (unknown:0) - myFilter.SetLowerThreshold(400.0)<br>
[INFO][Stream] 20.01.2020 11:15:50 [] (unknown:0) - myFilter.SetNumberOfThreads(12)<br>
[INFO][Stream] 20.01.2020 11:15:50 [] (unknown:0) - myFilter.SetOutsideValue(0)<br>
[INFO][Stream] 20.01.2020 11:15:50 [] (unknown:0) - myFilter.SetUpperThreshold(1000.0)<br>
[INFO][Stream] 20.01.2020 11:16:11 [] (unknown:0) - myFilter = BinaryThresholdImageFilter()<br>
[INFO][Stream] 20.01.2020 11:16:11 [] (unknown:0) - myFilter.SetDebug(False)<br>
[INFO][Stream] 20.01.2020 11:16:11 [] (unknown:0) - myFilter.SetInsideValue(1)<br>
[INFO][Stream] 20.01.2020 11:16:11 [] (unknown:0) - myFilter.SetLowerThreshold(200.0)<br>
[INFO][Stream] 20.01.2020 11:16:11 [] (unknown:0) - myFilter.SetNumberOfThreads(12)<br>
[INFO][Stream] 20.01.2020 11:16:11 [] (unknown:0) - myFilter.SetOutsideValue(0)<br>
[INFO][Stream] 20.01.2020 11:16:11 [] (unknown:0) - myFilter.SetUpperThreshold(1000.0)<br>
[INFO][Stream] 20.01.2020 11:16:40 [] (unknown:0) - myFilter = AddImageFilter()<br>
[INFO][Stream] 20.01.2020 11:16:40 [] (unknown:0) - myFilter.SetDebug(False)<br>
[INFO][Stream] 20.01.2020 11:16:40 [] (unknown:0) - myFilter.SetNumberOfThreads(12)<br>
[INFO][Stream] 20.01.2020 11:16:57 [] (unknown:0) - myFilter = CastImageFilter()<br>
[INFO][Stream] 20.01.2020 11:16:57 [] (unknown:0) - myFilter.SetDebug(False)<br>
[INFO][Stream] 20.01.2020 11:16:57 [] (unknown:0) - myFilter.SetNumberOfThreads(12)<br>
[INFO][Stream] 20.01.2020 11:16:57 [] (unknown:0) - myFilter.SetOutputPixelType(6)<br>
[INFO][Stream] 20.01.2020 11:17:10 [] (unknown:0) - myFilter = AddImageFilter()<br>
[INFO][Stream] 20.01.2020 11:17:10 [] (unknown:0) - myFilter.SetDebug(False)<br>
[INFO][Stream] 20.01.2020 11:17:10 [] (unknown:0) - myFilter.SetNumberOfThreads(12)<br>
[INFO][Stream] 20.01.2020 11:17:33 [] (unknown:0) - myFilter = ConfidenceConnectedImageFilter()<br>
[INFO][Stream] 20.01.2020 11:17:33 [] (unknown:0) - myFilter.SetDebug(False)<br>
[INFO][Stream] 20.01.2020 11:17:33 [] (unknown:0) - myFilter.SetInitialNeighborhoodRadius(1)<br>
[INFO][Stream] 20.01.2020 11:17:33 [] (unknown:0) - myFilter.SetMultiplier(2.5)<br>
[INFO][Stream] 20.01.2020 11:17:33 [] (unknown:0) - myFilter.SetNumberOfIterations(1)<br>
[INFO][Stream] 20.01.2020 11:17:33 [] (unknown:0) - myFilter.SetNumberOfThreads(12)<br>
[INFO][Stream] 20.01.2020 11:17:33 [] (unknown:0) - myFilter.SetReplaceValue(1)<br>
[INFO][Stream] 20.01.2020 11:17:33 [] (unknown:0) - myFilter.SetSeedList(((278, 224, 342),))<br>
[WARNING][VTK] 20.01.2020 11:18:40 [vtkMRMLVolumeArchetypeStorageNode (0000021458222FA0)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:544) - WriteData: removing old version of file C:/Users/Nicolas Lenoir/Documents/BinaryThresholdImageFilter Output.nii.gz<br>
[WARNING][VTK] 20.01.2020 11:20:37 [vtkMRMLVolumeArchetypeStorageNode (0000021458222640)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:544) - WriteData: removing old version of file C:/Users/Nicolas Lenoir/Documents/ConfidenceConnectedImageFilter Output.nii.gz<br>
[DEBUG][Qt] 20.01.2020 11:26:36 [] (unknown:0) - Switch to module:  “Segmentations”<br>
[DEBUG][Qt] 20.01.2020 11:26:58 [] (unknown:0) - Switch to module:  “SegmentEditor”<br>
[DEBUG][Qt] 20.01.2020 11:35:42 [] (unknown:0) - Switch to module:  “Segmentations”<br>
[DEBUG][Qt] 20.01.2020 11:51:53 [] (unknown:0) - Switch to module:  “DICOM”<br>
[WARNING][Python] 20.01.2020 11:52:03 [Python] (C:\Users\Nicolas Lenoir\AppData\Local\NA-MIC\Slicer 4.11.0-2020-01-08\lib\Slicer-4.11\qt-scripted-modules\DICOMLib\DICOMUtils.py:555) - Geometric issues were found with 1 of the series. Please use caution.<br>
[CRITICAL][Stream] 20.01.2020 11:52:03 [] (unknown:0) - Geometric issues were found with 1 of the series. Please use caution.<br>
[CRITICAL][Stream] 20.01.2020 11:52:03 [] (unknown:0) -<br>
[DEBUG][Python] 20.01.2020 11:52:03 [Python] (C:/Users/Nicolas Lenoir/AppData/Local/NA-MIC/Slicer 4.11.0-2020-01-08/bin/…/lib/Slicer-4.11/qt-scripted-modules/MultiVolumeImporterPlugin.py:456) - MultiVolumeImportPlugin::examine<br>
[DEBUG][Python] 20.01.2020 11:52:06 [Python] (C:/Users/Nicolas Lenoir/AppData/Local/NA-MIC/Slicer 4.11.0-2020-01-08/bin/…/lib/Slicer-4.11/qt-scripted-modules/MultiVolumeImporterPlugin.py:496) - DICOMMultiVolumePlugin found 1 multivolumes!<br>
[DEBUG][Python] 20.01.2020 11:52:11 [Python] (C:/Users/Nicolas Lenoir/AppData/Local/NA-MIC/Slicer 4.11.0-2020-01-08/bin/…/lib/Slicer-4.11/qt-scripted-modules/MultiVolumeImporterPlugin.py:168) - MultiVolumeImportPlugin:examineMultiseries<br>
[DEBUG][Python] 20.01.2020 11:52:12 [Python] (C:/Users/Nicolas Lenoir/AppData/Local/NA-MIC/Slicer 4.11.0-2020-01-08/bin/…/lib/Slicer-4.11/qt-scripted-modules/MultiVolumeImporterPlugin.py:173) - DICOMMultiVolumePlugin found 0 multivolumes!<br>
[WARNING][Python] 20.01.2020 11:52:12 [Python] (C:\Users\Nicolas Lenoir\AppData\Local\NA-MIC\Slicer 4.11.0-2020-01-08\lib\Slicer-4.11\qt-scripted-modules\DICOMLib\DICOMBrowser.py:591) - Warning in DICOM plugin Scalar Volume when examining loadable 401: AORTE TOTALE, iDose (5): Images are not equally spaced (a difference of 0.5 vs 0.5 in spacings was detected).  If loaded image appears distorted, enable ‘Acquisition geometry regularization’ in Application settings / DICOM / DICOMScalarVolumePlugin. Please use caution.<br>
[CRITICAL][Stream] 20.01.2020 11:52:12 [] (unknown:0) - Warning in DICOM plugin Scalar Volume when examining loadable 401: AORTE TOTALE, iDose (5): Images are not equally spaced (a difference of 0.5 vs 0.5 in spacings was detected).  If loaded image appears distorted, enable ‘Acquisition geometry regularization’ in Application settings / DICOM / DICOMScalarVolumePlugin. Please use caution.<br>
[CRITICAL][Stream] 20.01.2020 11:52:12 [] (unknown:0) -<br>
[INFO][Python] 20.01.2020 11:52:15 [Python] (C:/Users/Nicolas Lenoir/AppData/Local/NA-MIC/Slicer 4.11.0-2020-01-08/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:319) - Loading with imageIOName: GDCM<br>
[WARNING][Python] 20.01.2020 11:54:26 [Python] (C:/Users/Nicolas Lenoir/AppData/Local/NA-MIC/Slicer 4.11.0-2020-01-08/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:719) - Irregular volume geometry detected (maximum error of 5.39588 mm is above tolerance threshold of 0.001 mm).  Regularization transform is not added, as the option is disabled.<br>
[INFO][Stream] 20.01.2020 11:52:15 [] (unknown:0) - Loading with imageIOName: GDCM<br>
[CRITICAL][Stream] 20.01.2020 11:54:26 [] (unknown:0) - Irregular volume geometry detected (maximum error of 5.39588 mm is above tolerance threshold of 0.001 mm).  Regularization transform is not added, as the option is disabled.<br>
[DEBUG][Qt] 20.01.2020 11:54:49 [] (unknown:0) - Switch to module:  “Segmentations”<br>
[DEBUG][Qt] 20.01.2020 11:54:57 [] (unknown:0) - Switch to module:  “SimpleFilters”<br>
[DEBUG][Qt] 20.01.2020 11:55:03 [] (unknown:0) - Switch to module:  “Data”<br>
[DEBUG][Qt] 20.01.2020 11:55:09 [] (unknown:0) - Switch to module:  “SimpleFilters”<br>
[INFO][Stream] 20.01.2020 11:55:25 [] (unknown:0) - myFilter = MedianImageFilter()<br>
[INFO][Stream] 20.01.2020 11:55:25 [] (unknown:0) - myFilter.SetDebug(False)<br>
[INFO][Stream] 20.01.2020 11:55:25 [] (unknown:0) - myFilter.SetNumberOfThreads(12)<br>
[INFO][Stream] 20.01.2020 11:55:25 [] (unknown:0) - myFilter.SetRadius((5, 5, 1))<br>
[INFO][Stream] 20.01.2020 11:59:17 [] (unknown:0) - myFilter = CastImageFilter()<br>
[INFO][Stream] 20.01.2020 11:59:17 [] (unknown:0) - myFilter.SetDebug(False)<br>
[INFO][Stream] 20.01.2020 11:59:17 [] (unknown:0) - myFilter.SetNumberOfThreads(12)<br>
[INFO][Stream] 20.01.2020 11:59:17 [] (unknown:0) - myFilter.SetOutputPixelType(6)</p>

---

## Post #2 by @lassoan (2020-01-20 23:04 UTC)

<p>Can you reproduce the problem just by saving the median filter output to file, restarting Slicer, loading the saved file, and running CastImageFilter? Can you share the saved file?</p>
<p>Can you cast the image using “Cast scalar volume” module?</p>

---

## Post #3 by @Stoberoth (2020-01-23 16:07 UTC)

<p>i can’t reproduce the crash, it work now when a i cast the file in another type without crashing if i reproduce the bug i will send you the files you need.</p>
<p>Le mar. 21 janv. 2020 à 00:15, Andras Lasso via 3D Slicer Community <a href="mailto:slicer@discoursemail.com">slicer@discoursemail.com</a> a écrit :</p>

---
