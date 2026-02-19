---
topic_id: 43354
title: "Error Messages Showing Such As Reference Image In Series Doe"
date: 2025-06-14
url: https://discourse.slicer.org/t/43354
---

# Error messages showing such as "reference image in series does not contain geometry information. Please use caution.' and ' Could not load: 1000: Key Images as a Scalar Volume'

**Topic ID**: 43354
**Date**: 2025-06-14
**URL**: https://discourse.slicer.org/t/error-messages-showing-such-as-reference-image-in-series-does-not-contain-geometry-information-please-use-caution-and-could-not-load-1000-key-images-as-a-scalar-volume/43354

---

## Post #1 by @schmacko (2025-06-14 06:53 UTC)

<p>Hi all, a total newbie here. I’m using 3d slicer to do segmentation of CT scanned images of carotid artery. However, I receive an error message saying ‘reference image in series does not contain geometry information. Please use caution.’ when I imported the DICOM file and also ‘Could not load: 1000: Key Images as a Scalar Volume’ when I tried to load the data. I’ve tried using ‘DICOM Patcher’ but doesn’t work. Any idea why this is happening?</p>

---

## Post #2 by @schmacko (2025-06-14 06:55 UTC)

<p>Here’s the application log<br>
Here my application log<br>
[DEBUG][Qt] 14.06.2025 16:02:46 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Session start time …: 20250614_160246<br>
[DEBUG][Qt] 14.06.2025 16:02:46 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Slicer version …: 5.8.1 (revision 33241 / 11eaf62) macosx-amd64 - installed release<br>
[DEBUG][Qt] 14.06.2025 16:02:46 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Operating system …: macOS / 14.5 / 23F79 / UTF-8 - 64-bit<br>
[DEBUG][Qt] 14.06.2025 16:02:46 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Memory …: 8192 MB physical, 5120 MB virtual<br>
[DEBUG][Qt] 14.06.2025 16:02:46 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - CPU …: GenuineIntel Intel(R) Core™ i5-8257U CPU @ 1.40GHz, 4 cores, 8 logical processors<br>
[DEBUG][Qt] 14.06.2025 16:02:46 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 14.06.2025 16:02:46 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Qt configuration …: version 5.15.8, with SSL, requested OpenGL 3.2 (core profile)<br>
[DEBUG][Qt] 14.06.2025 16:02:46 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - DCMTK configuration …: version 3.6.8, no SSL<br>
[DEBUG][Qt] 14.06.2025 16:02:46 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Internationalization …: disabled, language=<br>
[DEBUG][Qt] 14.06.2025 16:02:46 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Developer mode …: disabled<br>
[DEBUG][Qt] 14.06.2025 16:02:46 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Application path …: /Applications/Slicer.app/Contents/MacOS<br>
[DEBUG][Qt] 14.06.2025 16:02:46 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Additional module paths ..: Extensions-33241/SegmentEditorExtraEffects/lib/Slicer-5.8/qt-loadable-modules, Extensions-33241/SegmentEditorExtraEffects/lib/Slicer-5.8/qt-scripted-modules, Extensions-33241/MarkupsToModel/lib/Slicer-5.8/qt-loadable-modules, Extensions-33241/MONAIAuto3DSeg/lib/Slicer-5.8/qt-scripted-modules, Extensions-33241/PyTorch/lib/Slicer-5.8/qt-scripted-modules, Extensions-33241/AirwaySegmentation/lib/Slicer-5.8/cli-modules, Extensions-33241/AirwaySegmentation/lib/Slicer-5.8/qt-scripted-modules, Extensions-33241/NvidiaAIAssistedAnnotation/lib/Slicer-5.8/qt-scripted-modules, Extensions-33241/RegularizedFastMarching/lib/Slicer-5.8/qt-scripted-modules<br>
[CRITICAL][FD] 14.06.2025 16:02:47 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - 2025-06-14 16:02:47.025 Slicer[23531:5665161] WARNING: Secure coding is not enabled for restorable state! Enable secure coding by implementing NSApplicationDelegate.applicationSupportsSecureRestorableState: and returning YES.<br>
[DEBUG][Python] 14.06.2025 16:02:51 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:40) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 14.06.2025 16:02:51 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:40) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 14.06.2025 16:02:51 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “Welcome”<br>
[INFO][Python] 14.06.2025 16:03:07 [Python] (/Applications/Slicer.app/Contents/Extensions-33241/NvidiaAIAssistedAnnotation/lib/Slicer-5.8/qt-scripted-modules/SegmentEditorNvidiaAIAA.py:32) - This plugin dir: /Applications/Slicer.app/Contents/Extensions-33241/NvidiaAIAssistedAnnotation/lib/Slicer-5.8/qt-scripted-modules<br>
[CRITICAL][FD] 14.06.2025 16:03:36 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - 2025-06-14 16:03:36.093 Slicer[23531:5665161] TSM AdjustCapsLockLEDForKeyTransitionHandling - _ISSetPhysicalKeyboardCapsLockLED Inhibit<br>
[DEBUG][Qt] 14.06.2025 16:03:37 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Python console user input: YES<br>
[CRITICAL][Stream] 14.06.2025 16:03:37 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Traceback (most recent call last):<br>
[CRITICAL][Stream] 14.06.2025 16:03:37 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “”, line 1, in <br>
[CRITICAL][Stream] 14.06.2025 16:03:37 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - NameError: name ‘YES’ is not defined<br>
[DEBUG][Qt] 14.06.2025 16:03:56 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “DICOM”<br>
[INFO][Python] 14.06.2025 16:11:38 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMLib/DICOMBrowser.py:349) - Imported a DICOM directory, checking for extensions<br>
[WARNING][Python] 14.06.2025 16:16:11 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMLib/DICOMBrowser.py:640) - Warning in DICOM plugin Scalar Volume when examining loadable 252: VR CAROTIDS 1: Reference image in series does not contain geometry information. Please use caution.<br>
[WARNING][Python] 14.06.2025 16:16:11 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMLib/DICOMBrowser.py:640) - Warning in DICOM plugin Scalar Volume when examining loadable 253: VR CAROTIDS 2: Reference image in series does not contain geometry information. Please use caution.<br>
[WARNING][Python] 14.06.2025 16:16:11 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMLib/DICOMBrowser.py:640) - Warning in DICOM plugin Scalar Volume when examining loadable 254: VR CAROTIDS 3: Reference image in series does not contain geometry information. Please use caution.<br>
[WARNING][Python] 14.06.2025 16:16:11 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMLib/DICOMBrowser.py:640) - Warning in DICOM plugin Scalar Volume when examining loadable 256: RICA: Reference image in series does not contain geometry information. Please use caution.<br>
[WARNING][Python] 14.06.2025 16:16:11 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMLib/DICOMBrowser.py:640) - Warning in DICOM plugin Scalar Volume when examining loadable 257: RVA: Reference image in series does not contain geometry information. Please use caution.<br>
[WARNING][Python] 14.06.2025 16:16:11 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMLib/DICOMBrowser.py:640) - Warning in DICOM plugin Scalar Volume when examining loadable 258: LICA: Reference image in series does not contain geometry information. Please use caution.<br>
[WARNING][Python] 14.06.2025 16:16:11 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMLib/DICOMBrowser.py:640) - Warning in DICOM plugin Scalar Volume when examining loadable 259: LVA: Reference image in series does not contain geometry information. Please use caution.<br>
[WARNING][Python] 14.06.2025 16:16:11 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMLib/DICOMBrowser.py:640) - Warning in DICOM plugin Scalar Volume when examining loadable 261: LICA PATHOLOGY: Reference image in series does not contain geometry information. Please use caution.<br>
[WARNING][Python] 14.06.2025 16:16:11 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMLib/DICOMBrowser.py:640) - Warning in DICOM plugin Scalar Volume when examining loadable 262: LICA PATHOLOGY 2: Reference image in series does not contain geometry information. Please use caution.<br>
[WARNING][Python] 14.06.2025 16:16:11 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMLib/DICOMBrowser.py:640) - Warning in DICOM plugin Scalar Volume when examining loadable 999: Dose Report: Reference image in series does not contain geometry information. Please use caution.<br>
[WARNING][Python] 14.06.2025 16:16:11 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMLib/DICOMBrowser.py:640) - Warning in DICOM plugin Scalar Volume when examining loadable 1000: Key Images: Reference image in series does not contain geometry information. Please use caution.<br>
[INFO][Python] 14.06.2025 16:16:11 [Python] (/Applications/Slicer.app/Contents/bin/Python/slicer/util.py:3057) - Warnings detected during load.  Examine data in Advanced mode for details.  Load anyway?<br>
[INFO][Python] 14.06.2025 16:18:05 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:445) - Loading with imageIOName: GDCM<br>
[INFO][Python] 14.06.2025 16:18:07 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:493) - Reverse slice order to force volume ‘1: Scout’ (vtkMRMLScalarVolumeNode1) to use right-handed IJK coordinate system<br>
[DEBUG][Python] 14.06.2025 16:18:07 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:557) - DICOM window/level (200.0/1000.0) set to volume ‘1: Scout’ from SOP instance 1.3.6.1.4.1.5962.99.1.1647006010.1317057211.1749698728250.7.0.<br>
[WARNING][Python] 14.06.2025 16:18:07 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:851) - Cannot get DICOM slice positions for volume 1: Scout<br>
[INFO][Python] 14.06.2025 16:18:07 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:445) - Loading with imageIOName: GDCM<br>
[DEBUG][Python] 14.06.2025 16:22:05 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:557) - DICOM window/level (200.0/1000.0) set to volume ‘2: CAROTID COW CTA’ from SOP instance 1.3.6.1.4.1.5962.99.1.1647006010.1317057211.1749698728250.251.0.<br>
[INFO][Python] 14.06.2025 16:22:05 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:445) - Loading with imageIOName: GDCM<br>
[DEBUG][Python] 14.06.2025 16:22:19 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:557) - DICOM window/level (200.0/700.0) set to volume ‘252: VR CAROTIDS 1’ from SOP instance 1.3.6.1.4.1.5962.99.1.1647006010.1317057211.1749698728250.516.0.<br>
[WARNING][Python] 14.06.2025 16:22:19 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:860) - No geometry information available for DICOM data, skipping corner calculations<br>
[INFO][Python] 14.06.2025 16:22:19 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:445) - Loading with imageIOName: GDCM<br>
[DEBUG][Python] 14.06.2025 16:22:20 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:560) - No window/level found for volume ‘253: VR CAROTIDS 2’ in DICOM tags of SOP instance 1.3.6.1.4.1.5962.99.1.1647006010.1317057211.1749698728250.533.0.<br>
[WARNING][Python] 14.06.2025 16:22:20 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:860) - No geometry information available for DICOM data, skipping corner calculations<br>
[INFO][Python] 14.06.2025 16:22:20 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:445) - Loading with imageIOName: GDCM<br>
[DEBUG][Python] 14.06.2025 16:22:24 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:560) - No window/level found for volume ‘254: VR CAROTIDS 3’ in DICOM tags of SOP instance 1.3.6.1.4.1.5962.99.1.1647006010.1317057211.1749698728250.550.0.<br>
[WARNING][Python] 14.06.2025 16:22:24 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:860) - No geometry information available for DICOM data, skipping corner calculations<br>
[INFO][Python] 14.06.2025 16:22:24 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:445) - Loading with imageIOName: GDCM<br>
[DEBUG][Python] 14.06.2025 16:22:47 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:557) - DICOM window/level (100.0/800.0) set to volume ‘256: RICA’ from SOP instance 1.3.6.1.4.1.5962.99.1.1647006010.1317057211.1749698728250.581.0.<br>
[WARNING][Python] 14.06.2025 16:22:47 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:860) - No geometry information available for DICOM data, skipping corner calculations<br>
[INFO][Python] 14.06.2025 16:22:47 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:445) - Loading with imageIOName: GDCM<br>
[DEBUG][Python] 14.06.2025 16:23:14 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:557) - DICOM window/level (100.0/800.0) set to volume ‘257: RVA’ from SOP instance 1.3.6.1.4.1.5962.99.1.1647006010.1317057211.1749698728250.622.0.<br>
[WARNING][Python] 14.06.2025 16:23:14 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:860) - No geometry information available for DICOM data, skipping corner calculations<br>
[INFO][Python] 14.06.2025 16:23:14 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:445) - Loading with imageIOName: GDCM<br>
[DEBUG][Python] 14.06.2025 16:23:28 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:557) - DICOM window/level (100.0/800.0) set to volume ‘258: LICA’ from SOP instance 1.3.6.1.4.1.5962.99.1.1647006010.1317057211.1749698728250.663.0.<br>
[WARNING][Python] 14.06.2025 16:23:28 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:860) - No geometry information available for DICOM data, skipping corner calculations<br>
[INFO][Python] 14.06.2025 16:23:28 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:445) - Loading with imageIOName: GDCM<br>
[DEBUG][Python] 14.06.2025 16:23:47 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:557) - DICOM window/level (100.0/800.0) set to volume ‘259: LVA’ from SOP instance 1.3.6.1.4.1.5962.99.1.1647006010.1317057211.1749698728250.704.0.<br>
[WARNING][Python] 14.06.2025 16:23:47 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:860) - No geometry information available for DICOM data, skipping corner calculations<br>
[INFO][Python] 14.06.2025 16:23:47 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:445) - Loading with imageIOName: GDCM<br>
[DEBUG][Python] 14.06.2025 16:24:28 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:560) - No window/level found for volume ‘261: LICA PATHOLOGY’ in DICOM tags of SOP instance 1.3.6.1.4.1.5962.99.1.1647006010.1317057211.1749698728250.751.0.<br>
[WARNING][Python] 14.06.2025 16:24:28 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:860) - No geometry information available for DICOM data, skipping corner calculations<br>
[INFO][Python] 14.06.2025 16:24:28 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:445) - Loading with imageIOName: GDCM<br>
[DEBUG][Python] 14.06.2025 16:24:52 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:560) - No window/level found for volume ‘262: LICA PATHOLOGY 2’ in DICOM tags of SOP instance 1.3.6.1.4.1.5962.99.1.1647006010.1317057211.1749698728250.792.0.<br>
[WARNING][Python] 14.06.2025 16:24:52 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:860) - No geometry information available for DICOM data, skipping corner calculations<br>
[INFO][Python] 14.06.2025 16:24:52 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:445) - Loading with imageIOName: GDCM<br>
[DEBUG][Python] 14.06.2025 16:24:53 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:557) - DICOM window/level (-2.0/1.0) set to volume ‘999: Dose Report’ from SOP instance 1.3.6.1.4.1.5962.99.1.1647006010.1317057211.1749698728250.806.0.<br>
[WARNING][Python] 14.06.2025 16:24:53 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:860) - No geometry information available for DICOM data, skipping corner calculations<br>
[INFO][Python] 14.06.2025 16:24:53 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:445) - Loading with imageIOName: GDCM<br>
[ERROR][VTK] 14.06.2025 16:24:54 [vtkITKArchetypeImageSeriesVectorReaderSeries (0x7f8182c187a0)] (vtkITKArchetypeImageSeriesVectorReaderSeries.cxx:163) - Exception from vtkITK MegaMacro:<br>
itk::InvalidRequestedRegionError (0x600004e4ece0)<br>
Location: “unknown”<br>
File: /Users/svc-dashboard/D/S/A/ITK/Modules/IO/ImageBase/include/itkImageFileReader.hxx<br>
Line: 338<br>
Description: ImageIO returns IO region that does not fully contain the requested region. Requested region: ImageRegion (0x7ff7bf38aa00)<br>
Dimension: 3<br>
Index: [0, 0, 0]<br>
Size: [1522, 1678, 1]<br>
StreamableRegion region: ImageRegion (0x7ff7bf38aa38)<br>
Dimension: 3<br>
Index: [0, 0, 0]<br>
Size: [759, 827, 1]<br>
[ERROR][VTK] 14.06.2025 16:24:54 [vtkCompositeDataPipeline (0x6000043cf200)] (vtkExecutive.cxx:742) - Algorithm vtkITKArchetypeImageSeriesVectorReaderSeries (0x7f8182c187a0) returned failure for request: vtkInformation (0x600009bae400)<br>
Debug: Off<br>
Modified Time: 386326<br>
Reference Count: 1<br>
Registered Events: (none)<br>
Request: REQUEST_DATA<br>
FROM_OUTPUT_PORT: 0<br>
ALGORITHM_AFTER_FORWARD: 1<br>
FORWARD_DIRECTION: 0<br>
[ERROR][Python] 14.06.2025 16:24:54 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:451) - Could not read scalar volume using GDCM approach.  Error is: FileFormatError<br>
[INFO][Python] 14.06.2025 16:24:54 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:445) - Loading with imageIOName: DCMTK<br>
[ERROR][VTK] 14.06.2025 16:24:54 [vtkITKArchetypeImageSeriesVectorReaderSeries (0x7f8186c93f60)] (vtkITKArchetypeImageSeriesVectorReaderSeries.cxx:163) - Exception from vtkITK MegaMacro:<br>
itk::InvalidRequestedRegionError (0x60000496f820)<br>
Location: “unknown”<br>
File: /Users/svc-dashboard/D/S/A/ITK/Modules/IO/ImageBase/include/itkImageFileReader.hxx<br>
Line: 338<br>
Description: ImageIO returns IO region that does not fully contain the requested region. Requested region: ImageRegion (0x7ff7bf38aa00)<br>
Dimension: 3<br>
Index: [0, 0, 0]<br>
Size: [1522, 1678, 1]<br>
StreamableRegion region: ImageRegion (0x7ff7bf38aa38)<br>
Dimension: 3<br>
Index: [0, 0, 0]<br>
Size: [759, 827, 1]<br>
[ERROR][VTK] 14.06.2025 16:24:54 [vtkCompositeDataPipeline (0x6000043d7c00)] (vtkExecutive.cxx:742) - Algorithm vtkITKArchetypeImageSeriesVectorReaderSeries (0x7f8186c93f60) returned failure for request: vtkInformation (0x600009b59ec0)<br>
Debug: Off<br>
Modified Time: 386530<br>
Reference Count: 1<br>
Registered Events: (none)<br>
Request: REQUEST_DATA<br>
FROM_OUTPUT_PORT: 0<br>
ALGORITHM_AFTER_FORWARD: 1<br>
FORWARD_DIRECTION: 0<br>
[ERROR][Python] 14.06.2025 16:24:54 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:451) - Could not read scalar volume using DCMTK approach.  Error is: FileFormatError<br>
[INFO][Python] 14.06.2025 16:24:54 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:445) - Loading with imageIOName: GDCM<br>
[INFO][Python] 14.06.2025 16:24:55 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:493) - Reverse slice order to force volume ‘200: Smart Prep Series’ (vtkMRMLScalarVolumeNode9) to use right-handed IJK coordinate system<br>
[DEBUG][Python] 14.06.2025 16:24:55 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:557) - DICOM window/level (200.0/1000.0) set to volume ‘200: Smart Prep Series’ from SOP instance 1.3.6.1.4.1.5962.99.1.1647006010.1317057211.1749698728250.492.0.<br>
[INFO][Python] 14.06.2025 16:24:55 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:445) - Loading with imageIOName: GDCM<br>
[INFO][Python] 14.06.2025 16:24:56 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:493) - Reverse slice order to force volume ‘200: Smart Prep Series_1’ (vtkMRMLScalarVolumeNode11) to use right-handed IJK coordinate system<br>
[DEBUG][Python] 14.06.2025 16:24:56 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:557) - DICOM window/level (200.0/1000.0) set to volume ‘200: Smart Prep Series_1’ from SOP instance 1.3.6.1.4.1.5962.99.1.1647006010.1317057211.1749698728250.495.0.<br>
[INFO][Python] 14.06.2025 16:24:56 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:445) - Loading with imageIOName: GDCM<br>
[INFO][Python] 14.06.2025 16:24:57 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:493) - Reverse slice order to force volume ‘200: Smart Prep Series_2’ (vtkMRMLScalarVolumeNode13) to use right-handed IJK coordinate system<br>
[DEBUG][Python] 14.06.2025 16:24:57 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:557) - DICOM window/level (200.0/1000.0) set to volume ‘200: Smart Prep Series_2’ from SOP instance 1.3.6.1.4.1.5962.99.1.1647006010.1317057211.1749698728250.497.0.<br>
[INFO][Python] 14.06.2025 16:24:57 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:445) - Loading with imageIOName: GDCM<br>
[INFO][Python] 14.06.2025 16:24:59 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:493) - Reverse slice order to force volume ‘200: Smart Prep Series_3’ (vtkMRMLScalarVolumeNode15) to use right-handed IJK coordinate system<br>
[DEBUG][Python] 14.06.2025 16:24:59 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:557) - DICOM window/level (200.0/1000.0) set to volume ‘200: Smart Prep Series_3’ from SOP instance 1.3.6.1.4.1.5962.99.1.1647006010.1317057211.1749698728250.498.0.<br>
[INFO][Python] 14.06.2025 16:24:59 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:445) - Loading with imageIOName: GDCM<br>
[INFO][Python] 14.06.2025 16:25:01 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:493) - Reverse slice order to force volume ‘200: Smart Prep Series_4’ (vtkMRMLScalarVolumeNode17) to use right-handed IJK coordinate system<br>
[DEBUG][Python] 14.06.2025 16:25:01 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:557) - DICOM window/level (200.0/1000.0) set to volume ‘200: Smart Prep Series_4’ from SOP instance 1.3.6.1.4.1.5962.99.1.1647006010.1317057211.1749698728250.499.0.<br>
[INFO][Python] 14.06.2025 16:25:01 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:445) - Loading with imageIOName: GDCM<br>
[INFO][Python] 14.06.2025 16:25:03 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:493) - Reverse slice order to force volume ‘200: Smart Prep Series_5’ (vtkMRMLScalarVolumeNode19) to use right-handed IJK coordinate system<br>
[DEBUG][Python] 14.06.2025 16:25:03 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:557) - DICOM window/level (200.0/1000.0) set to volume ‘200: Smart Prep Series_5’ from SOP instance 1.3.6.1.4.1.5962.99.1.1647006010.1317057211.1749698728250.500.0.<br>
[INFO][Python] 14.06.2025 16:25:03 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:445) - Loading with imageIOName: GDCM<br>
[INFO][Python] 14.06.2025 16:25:04 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:493) - Reverse slice order to force volume ‘200: Smart Prep Series_6’ (vtkMRMLScalarVolumeNode21) to use right-handed IJK coordinate system<br>
[DEBUG][Python] 14.06.2025 16:25:04 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:557) - DICOM window/level (200.0/1000.0) set to volume ‘200: Smart Prep Series_6’ from SOP instance 1.3.6.1.4.1.5962.99.1.1647006010.1317057211.1749698728250.501.0.<br>
[INFO][Python] 14.06.2025 16:25:04 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:445) - Loading with imageIOName: GDCM<br>
[INFO][Python] 14.06.2025 16:25:04 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:493) - Reverse slice order to force volume ‘200: Smart Prep Series_7’ (vtkMRMLScalarVolumeNode23) to use right-handed IJK coordinate system<br>
[DEBUG][Python] 14.06.2025 16:25:04 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:557) - DICOM window/level (200.0/1000.0) set to volume ‘200: Smart Prep Series_7’ from SOP instance 1.3.6.1.4.1.5962.99.1.1647006010.1317057211.1749698728250.502.0.<br>
[INFO][Python] 14.06.2025 16:25:04 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:445) - Loading with imageIOName: GDCM<br>
[INFO][Python] 14.06.2025 16:25:04 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:493) - Reverse slice order to force volume ‘200: Smart Prep Series_8’ (vtkMRMLScalarVolumeNode25) to use right-handed IJK coordinate system<br>
[DEBUG][Python] 14.06.2025 16:25:04 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:557) - DICOM window/level (200.0/1000.0) set to volume ‘200: Smart Prep Series_8’ from SOP instance 1.3.6.1.4.1.5962.99.1.1647006010.1317057211.1749698728250.503.0.<br>
[INFO][Python] 14.06.2025 16:25:04 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:445) - Loading with imageIOName: GDCM<br>
[INFO][Python] 14.06.2025 16:25:05 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:493) - Reverse slice order to force volume ‘200: Smart Prep Series_9’ (vtkMRMLScalarVolumeNode27) to use right-handed IJK coordinate system<br>
[DEBUG][Python] 14.06.2025 16:25:05 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:557) - DICOM window/level (200.0/1000.0) set to volume ‘200: Smart Prep Series_9’ from SOP instance 1.3.6.1.4.1.5962.99.1.1647006010.1317057211.1749698728250.504.0.<br>
[INFO][Python] 14.06.2025 16:25:05 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:445) - Loading with imageIOName: GDCM<br>
[INFO][Python] 14.06.2025 16:25:06 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:493) - Reverse slice order to force volume ‘200: Smart Prep Series_10’ (vtkMRMLScalarVolumeNode29) to use right-handed IJK coordinate system<br>
[DEBUG][Python] 14.06.2025 16:25:06 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:557) - DICOM window/level (200.0/1000.0) set to volume ‘200: Smart Prep Series_10’ from SOP instance 1.3.6.1.4.1.5962.99.1.1647006010.1317057211.1749698728250.505.0.<br>
[INFO][Python] 14.06.2025 16:25:06 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:445) - Loading with imageIOName: GDCM<br>
[INFO][Python] 14.06.2025 16:25:07 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:493) - Reverse slice order to force volume ‘200: Smart Prep Series_11’ (vtkMRMLScalarVolumeNode31) to use right-handed IJK coordinate system<br>
[DEBUG][Python] 14.06.2025 16:25:07 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:557) - DICOM window/level (200.0/1000.0) set to volume ‘200: Smart Prep Series_11’ from SOP instance 1.3.6.1.4.1.5962.99.1.1647006010.1317057211.1749698728250.506.0.<br>
[WARNING][Python] 14.06.2025 16:25:07 [Python] (/Applications/Slicer.app/Contents/bin/Python/slicer/util.py:3057) - Could not load: 1000: Key Images as a Scalar Volume<br>
[INFO][Python] 14.06.2025 16:42:07 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMLib/DICOMBrowser.py:349) - Imported a DICOM directory, checking for extensions<br>
[WARNING][Python] 14.06.2025 16:43:19 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMLib/DICOMBrowser.py:640) - Warning in DICOM plugin Scalar Volume when examining loadable 252: VR CAROTIDS 1: Reference image in series does not contain geometry information. Please use caution.<br>
[WARNING][Python] 14.06.2025 16:43:19 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMLib/DICOMBrowser.py:640) - Warning in DICOM plugin Scalar Volume when examining loadable 253: VR CAROTIDS 2: Reference image in series does not contain geometry information. Please use caution.<br>
[WARNING][Python] 14.06.2025 16:43:19 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMLib/DICOMBrowser.py:640) - Warning in DICOM plugin Scalar Volume when examining loadable 254: VR CAROTIDS 3: Reference image in series does not contain geometry information. Please use caution.<br>
[WARNING][Python] 14.06.2025 16:43:19 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMLib/DICOMBrowser.py:640) - Warning in DICOM plugin Scalar Volume when examining loadable 256: RICA: Reference image in series does not contain geometry information. Please use caution.<br>
[WARNING][Python] 14.06.2025 16:43:19 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMLib/DICOMBrowser.py:640) - Warning in DICOM plugin Scalar Volume when examining loadable 257: RVA: Reference image in series does not contain geometry information. Please use caution.<br>
[WARNING][Python] 14.06.2025 16:43:19 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMLib/DICOMBrowser.py:640) - Warning in DICOM plugin Scalar Volume when examining loadable 258: LICA: Reference image in series does not contain geometry information. Please use caution.<br>
[WARNING][Python] 14.06.2025 16:43:19 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMLib/DICOMBrowser.py:640) - Warning in DICOM plugin Scalar Volume when examining loadable 259: LVA: Reference image in series does not contain geometry information. Please use caution.<br>
[WARNING][Python] 14.06.2025 16:43:19 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMLib/DICOMBrowser.py:640) - Warning in DICOM plugin Scalar Volume when examining loadable 261: LICA PATHOLOGY: Reference image in series does not contain geometry information. Please use caution.<br>
[WARNING][Python] 14.06.2025 16:43:19 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMLib/DICOMBrowser.py:640) - Warning in DICOM plugin Scalar Volume when examining loadable 262: LICA PATHOLOGY 2: Reference image in series does not contain geometry information. Please use caution.<br>
[WARNING][Python] 14.06.2025 16:43:19 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMLib/DICOMBrowser.py:640) - Warning in DICOM plugin Scalar Volume when examining loadable 999: Dose Report: Reference image in series does not contain geometry information. Please use caution.<br>
[WARNING][Python] 14.06.2025 16:43:19 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMLib/DICOMBrowser.py:640) - Warning in DICOM plugin Scalar Volume when examining loadable 1000: Key Images: Reference image in series does not contain geometry information. Please use caution.<br>
[INFO][Python] 14.06.2025 16:43:19 [Python] (/Applications/Slicer.app/Contents/bin/Python/slicer/util.py:3057) - Warnings detected during load.  Examine data in Advanced mode for details.  Load anyway?<br>
[INFO][Python] 14.06.2025 16:43:36 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:445) - Loading with imageIOName: GDCM<br>
[INFO][Python] 14.06.2025 16:43:36 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:493) - Reverse slice order to force volume ‘1: Scout_1’ (vtkMRMLScalarVolumeNode34) to use right-handed IJK coordinate system<br>
[DEBUG][Python] 14.06.2025 16:43:36 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:557) - DICOM window/level (200.0/1000.0) set to volume ‘1: Scout_1’ from SOP instance 1.3.6.1.4.1.5962.99.1.1647006010.1317057211.1749698728250.7.0.<br>
[WARNING][Python] 14.06.2025 16:43:36 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:851) - Cannot get DICOM slice positions for volume 1: Scout_1<br>
[INFO][Python] 14.06.2025 16:43:36 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:445) - Loading with imageIOName: GDCM<br>
[DEBUG][Python] 14.06.2025 16:46:47 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:557) - DICOM window/level (200.0/1000.0) set to volume ‘2: CAROTID COW CTA_1’ from SOP instance 1.3.6.1.4.1.5962.99.1.1647006010.1317057211.1749698728250.251.0.<br>
[INFO][Python] 14.06.2025 16:46:48 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:445) - Loading with imageIOName: GDCM<br>
[DEBUG][Python] 14.06.2025 16:46:57 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:557) - DICOM window/level (200.0/700.0) set to volume ‘252: VR CAROTIDS 1_1’ from SOP instance 1.3.6.1.4.1.5962.99.1.1647006010.1317057211.1749698728250.516.0.<br>
[WARNING][Python] 14.06.2025 16:46:57 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:860) - No geometry information available for DICOM data, skipping corner calculations<br>
[INFO][Python] 14.06.2025 16:46:57 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:445) - Loading with imageIOName: GDCM<br>
[DEBUG][Python] 14.06.2025 16:46:58 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:560) - No window/level found for volume ‘253: VR CAROTIDS 2_1’ in DICOM tags of SOP instance 1.3.6.1.4.1.5962.99.1.1647006010.1317057211.1749698728250.533.0.<br>
[WARNING][Python] 14.06.2025 16:46:58 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:860) - No geometry information available for DICOM data, skipping corner calculations<br>
[INFO][Python] 14.06.2025 16:46:58 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:445) - Loading with imageIOName: GDCM<br>
[DEBUG][Python] 14.06.2025 16:47:01 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:560) - No window/level found for volume ‘254: VR CAROTIDS 3_1’ in DICOM tags of SOP instance 1.3.6.1.4.1.5962.99.1.1647006010.1317057211.1749698728250.550.0.<br>
[WARNING][Python] 14.06.2025 16:47:01 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:860) - No geometry information available for DICOM data, skipping corner calculations<br>
[INFO][Python] 14.06.2025 16:47:01 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:445) - Loading with imageIOName: GDCM<br>
[DEBUG][Python] 14.06.2025 16:47:12 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:557) - DICOM window/level (100.0/800.0) set to volume ‘256: RICA_1’ from SOP instance 1.3.6.1.4.1.5962.99.1.1647006010.1317057211.1749698728250.581.0.<br>
[WARNING][Python] 14.06.2025 16:47:12 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:860) - No geometry information available for DICOM data, skipping corner calculations<br>
[INFO][Python] 14.06.2025 16:47:12 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:445) - Loading with imageIOName: GDCM<br>
[DEBUG][Python] 14.06.2025 16:47:30 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:557) - DICOM window/level (100.0/800.0) set to volume ‘257: RVA_1’ from SOP instance 1.3.6.1.4.1.5962.99.1.1647006010.1317057211.1749698728250.622.0.<br>
[WARNING][Python] 14.06.2025 16:47:30 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:860) - No geometry information available for DICOM data, skipping corner calculations<br>
[INFO][Python] 14.06.2025 16:47:30 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:445) - Loading with imageIOName: GDCM<br>
[DEBUG][Python] 14.06.2025 16:47:43 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:557) - DICOM window/level (100.0/800.0) set to volume ‘258: LICA_1’ from SOP instance 1.3.6.1.4.1.5962.99.1.1647006010.1317057211.1749698728250.663.0.<br>
[WARNING][Python] 14.06.2025 16:47:43 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:860) - No geometry information available for DICOM data, skipping corner calculations<br>
[INFO][Python] 14.06.2025 16:47:43 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:445) - Loading with imageIOName: GDCM<br>
[DEBUG][Python] 14.06.2025 16:47:55 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:557) - DICOM window/level (100.0/800.0) set to volume ‘259: LVA_1’ from SOP instance 1.3.6.1.4.1.5962.99.1.1647006010.1317057211.1749698728250.704.0.<br>
[WARNING][Python] 14.06.2025 16:47:55 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:860) - No geometry information available for DICOM data, skipping corner calculations<br>
[INFO][Python] 14.06.2025 16:47:55 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:445) - Loading with imageIOName: GDCM<br>
[DEBUG][Python] 14.06.2025 16:48:14 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:560) - No window/level found for volume ‘261: LICA PATHOLOGY_1’ in DICOM tags of SOP instance 1.3.6.1.4.1.5962.99.1.1647006010.1317057211.1749698728250.751.0.<br>
[WARNING][Python] 14.06.2025 16:48:14 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:860) - No geometry information available for DICOM data, skipping corner calculations<br>
[INFO][Python] 14.06.2025 16:48:14 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:445) - Loading with imageIOName: GDCM<br>
[DEBUG][Python] 14.06.2025 16:48:20 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:560) - No window/level found for volume ‘262: LICA PATHOLOGY 2_1’ in DICOM tags of SOP instance 1.3.6.1.4.1.5962.99.1.1647006010.1317057211.1749698728250.792.0.<br>
[WARNING][Python] 14.06.2025 16:48:20 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:860) - No geometry information available for DICOM data, skipping corner calculations<br>
[INFO][Python] 14.06.2025 16:48:20 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:445) - Loading with imageIOName: GDCM<br>
[DEBUG][Python] 14.06.2025 16:48:21 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:557) - DICOM window/level (-2.0/1.0) set to volume ‘999: Dose Report_1’ from SOP instance 1.3.6.1.4.1.5962.99.1.1647006010.1317057211.1749698728250.806.0.<br>
[WARNING][Python] 14.06.2025 16:48:21 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:860) - No geometry information available for DICOM data, skipping corner calculations<br>
[INFO][Python] 14.06.2025 16:48:21 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:445) - Loading with imageIOName: GDCM<br>
[ERROR][VTK] 14.06.2025 16:48:21 [vtkITKArchetypeImageSeriesVectorReaderSeries (0x7f81882dac30)] (vtkITKArchetypeImageSeriesVectorReaderSeries.cxx:163) - Exception from vtkITK MegaMacro:<br>
itk::InvalidRequestedRegionError (0x600008eceba0)<br>
Location: “unknown”<br>
File: /Users/svc-dashboard/D/S/A/ITK/Modules/IO/ImageBase/include/itkImageFileReader.hxx<br>
Line: 338<br>
Description: ImageIO returns IO region that does not fully contain the requested region. Requested region: ImageRegion (0x7ff7bf38aa00)<br>
Dimension: 3<br>
Index: [0, 0, 0]<br>
Size: [1522, 1678, 1]<br>
StreamableRegion region: ImageRegion (0x7ff7bf38aa38)<br>
Dimension: 3<br>
Index: [0, 0, 0]<br>
Size: [759, 827, 1]<br>
[ERROR][VTK] 14.06.2025 16:48:21 [vtkCompositeDataPipeline (0x6000043ea300)] (vtkExecutive.cxx:742) - Algorithm vtkITKArchetypeImageSeriesVectorReaderSeries (0x7f81882dac30) returned failure for request: vtkInformation (0x600009ad3240)<br>
Debug: Off<br>
Modified Time: 975758<br>
Reference Count: 1<br>
Registered Events: (none)<br>
Request: REQUEST_DATA<br>
FROM_OUTPUT_PORT: 0<br>
ALGORITHM_AFTER_FORWARD: 1<br>
FORWARD_DIRECTION: 0<br>
[ERROR][Python] 14.06.2025 16:48:21 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:451) - Could not read scalar volume using GDCM approach.  Error is: FileFormatError<br>
[INFO][Python] 14.06.2025 16:48:21 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:445) - Loading with imageIOName: DCMTK<br>
[ERROR][VTK] 14.06.2025 16:48:21 [vtkITKArchetypeImageSeriesVectorReaderSeries (0x7f8186ceba60)] (vtkITKArchetypeImageSeriesVectorReaderSeries.cxx:163) - Exception from vtkITK MegaMacro:<br>
itk::InvalidRequestedRegionError (0x600008eceba0)<br>
Location: “unknown”<br>
File: /Users/svc-dashboard/D/S/A/ITK/Modules/IO/ImageBase/include/itkImageFileReader.hxx<br>
Line: 338<br>
Description: ImageIO returns IO region that does not fully contain the requested region. Requested region: ImageRegion (0x7ff7bf38aa00)<br>
Dimension: 3<br>
Index: [0, 0, 0]<br>
Size: [1522, 1678, 1]<br>
StreamableRegion region: ImageRegion (0x7ff7bf38aa38)<br>
Dimension: 3<br>
Index: [0, 0, 0]<br>
Size: [759, 827, 1]<br>
[ERROR][VTK] 14.06.2025 16:48:21 [vtkCompositeDataPipeline (0x6000043fb700)] (vtkExecutive.cxx:742) - Algorithm vtkITKArchetypeImageSeriesVectorReaderSeries (0x7f8186ceba60) returned failure for request: vtkInformation (0x600009b21380)<br>
Debug: Off<br>
Modified Time: 975962<br>
Reference Count: 1<br>
Registered Events: (none)<br>
Request: REQUEST_DATA<br>
FROM_OUTPUT_PORT: 0<br>
ALGORITHM_AFTER_FORWARD: 1<br>
FORWARD_DIRECTION: 0<br>
[ERROR][Python] 14.06.2025 16:48:21 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:451) - Could not read scalar volume using DCMTK approach.  Error is: FileFormatError<br>
[INFO][Python] 14.06.2025 16:48:21 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:445) - Loading with imageIOName: GDCM<br>
[INFO][Python] 14.06.2025 16:48:22 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:493) - Reverse slice order to force volume ‘200: Smart Prep Series_12’ (vtkMRMLScalarVolumeNode42) to use right-handed IJK coordinate system<br>
[DEBUG][Python] 14.06.2025 16:48:22 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:557) - DICOM window/level (200.0/1000.0) set to volume ‘200: Smart Prep Series_12’ from SOP instance 1.3.6.1.4.1.5962.99.1.1647006010.1317057211.1749698728250.492.0.<br>
[INFO][Python] 14.06.2025 16:48:22 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:445) - Loading with imageIOName: GDCM<br>
[INFO][Python] 14.06.2025 16:48:23 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:493) - Reverse slice order to force volume ‘200: Smart Prep Series_13’ (vtkMRMLScalarVolumeNode44) to use right-handed IJK coordinate system<br>
[DEBUG][Python] 14.06.2025 16:48:23 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:557) - DICOM window/level (200.0/1000.0) set to volume ‘200: Smart Prep Series_13’ from SOP instance 1.3.6.1.4.1.5962.99.1.1647006010.1317057211.1749698728250.495.0.<br>
[INFO][Python] 14.06.2025 16:48:23 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:445) - Loading with imageIOName: GDCM<br>
[INFO][Python] 14.06.2025 16:48:24 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:493) - Reverse slice order to force volume ‘200: Smart Prep Series_14’ (vtkMRMLScalarVolumeNode46) to use right-handed IJK coordinate system<br>
[DEBUG][Python] 14.06.2025 16:48:24 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:557) - DICOM window/level (200.0/1000.0) set to volume ‘200: Smart Prep Series_14’ from SOP instance 1.3.6.1.4.1.5962.99.1.1647006010.1317057211.1749698728250.497.0.<br>
[INFO][Python] 14.06.2025 16:48:24 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:445) - Loading with imageIOName: GDCM<br>
[INFO][Python] 14.06.2025 16:48:25 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:493) - Reverse slice order to force volume ‘200: Smart Prep Series_15’ (vtkMRMLScalarVolumeNode48) to use right-handed IJK coordinate system<br>
[DEBUG][Python] 14.06.2025 16:48:25 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:557) - DICOM window/level (200.0/1000.0) set to volume ‘200: Smart Prep Series_15’ from SOP instance 1.3.6.1.4.1.5962.99.1.1647006010.1317057211.1749698728250.498.0.<br>
[INFO][Python] 14.06.2025 16:48:25 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:445) - Loading with imageIOName: GDCM<br>
[INFO][Python] 14.06.2025 16:48:25 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:493) - Reverse slice order to force volume ‘200: Smart Prep Series_16’ (vtkMRMLScalarVolumeNode50) to use right-handed IJK coordinate system<br>
[DEBUG][Python] 14.06.2025 16:48:25 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:557) - DICOM window/level (200.0/1000.0) set to volume ‘200: Smart Prep Series_16’ from SOP instance 1.3.6.1.4.1.5962.99.1.1647006010.1317057211.1749698728250.499.0.<br>
[INFO][Python] 14.06.2025 16:48:25 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:445) - Loading with imageIOName: GDCM<br>
[INFO][Python] 14.06.2025 16:48:27 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:493) - Reverse slice order to force volume ‘200: Smart Prep Series_17’ (vtkMRMLScalarVolumeNode52) to use right-handed IJK coordinate system<br>
[DEBUG][Python] 14.06.2025 16:48:27 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:557) - DICOM window/level (200.0/1000.0) set to volume ‘200: Smart Prep Series_17’ from SOP instance 1.3.6.1.4.1.5962.99.1.1647006010.1317057211.1749698728250.500.0.<br>
[INFO][Python] 14.06.2025 16:48:27 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:445) - Loading with imageIOName: GDCM<br>
[INFO][Python] 14.06.2025 16:48:27 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:493) - Reverse slice order to force volume ‘200: Smart Prep Series_18’ (vtkMRMLScalarVolumeNode54) to use right-handed IJK coordinate system<br>
[DEBUG][Python] 14.06.2025 16:48:27 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:557) - DICOM window/level (200.0/1000.0) set to volume ‘200: Smart Prep Series_18’ from SOP instance 1.3.6.1.4.1.5962.99.1.1647006010.1317057211.1749698728250.501.0.<br>
[INFO][Python] 14.06.2025 16:48:27 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:445) - Loading with imageIOName: GDCM<br>
[INFO][Python] 14.06.2025 16:48:27 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:493) - Reverse slice order to force volume ‘200: Smart Prep Series_19’ (vtkMRMLScalarVolumeNode56) to use right-handed IJK coordinate system<br>
[DEBUG][Python] 14.06.2025 16:48:27 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:557) - DICOM window/level (200.0/1000.0) set to volume ‘200: Smart Prep Series_19’ from SOP instance 1.3.6.1.4.1.5962.99.1.1647006010.1317057211.1749698728250.502.0.<br>
[INFO][Python] 14.06.2025 16:48:27 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:445) - Loading with imageIOName: GDCM<br>
[INFO][Python] 14.06.2025 16:48:27 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:493) - Reverse slice order to force volume ‘200: Smart Prep Series_20’ (vtkMRMLScalarVolumeNode58) to use right-handed IJK coordinate system<br>
[DEBUG][Python] 14.06.2025 16:48:27 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:557) - DICOM window/level (200.0/1000.0) set to volume ‘200: Smart Prep Series_20’ from SOP instance 1.3.6.1.4.1.5962.99.1.1647006010.1317057211.1749698728250.503.0.<br>
[INFO][Python] 14.06.2025 16:48:27 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:445) - Loading with imageIOName: GDCM<br>
[INFO][Python] 14.06.2025 16:48:27 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:493) - Reverse slice order to force volume ‘200: Smart Prep Series_21’ (vtkMRMLScalarVolumeNode60) to use right-handed IJK coordinate system<br>
[DEBUG][Python] 14.06.2025 16:48:27 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:557) - DICOM window/level (200.0/1000.0) set to volume ‘200: Smart Prep Series_21’ from SOP instance 1.3.6.1.4.1.5962.99.1.1647006010.1317057211.1749698728250.504.0.<br>
[INFO][Python] 14.06.2025 16:48:27 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:445) - Loading with imageIOName: GDCM<br>
[INFO][Python] 14.06.2025 16:48:27 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:493) - Reverse slice order to force volume ‘200: Smart Prep Series_22’ (vtkMRMLScalarVolumeNode62) to use right-handed IJK coordinate system<br>
[DEBUG][Python] 14.06.2025 16:48:27 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:557) - DICOM window/level (200.0/1000.0) set to volume ‘200: Smart Prep Series_22’ from SOP instance 1.3.6.1.4.1.5962.99.1.1647006010.1317057211.1749698728250.505.0.<br>
[INFO][Python] 14.06.2025 16:48:28 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:445) - Loading with imageIOName: GDCM<br>
[INFO][Python] 14.06.2025 16:48:28 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:493) - Reverse slice order to force volume ‘200: Smart Prep Series_23’ (vtkMRMLScalarVolumeNode64) to use right-handed IJK coordinate system<br>
[DEBUG][Python] 14.06.2025 16:48:28 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.8/qt-scripted-modules/DICOMScalarVolumePlugin.py:557) - DICOM window/level (200.0/1000.0) set to volume ‘200: Smart Prep Series_23’ from SOP instance 1.3.6.1.4.1.5962.99.1.1647006010.1317057211.1749698728250.506.0.<br>
[WARNING][Python] 14.06.2025 16:48:28 [Python] (/Applications/Slicer.app/Contents/bin/Python/slicer/util.py:3057) - Could not load: 1000: Key Images as a Scalar Volume</p>

---

## Post #3 by @schmacko (2025-06-14 06:58 UTC)

<p>and also here’s the errors in console<br>
Python] Warning in DICOM plugin Scalar Volume when examining loadable 252: VR CAROTIDS 1: Reference image in series does not contain geometry information. Please use caution.</p>
<p>[Python] Warning in DICOM plugin Scalar Volume when examining loadable 253: VR CAROTIDS 2: Reference image in series does not contain geometry information. Please use caution.</p>
<p>[Python] Warning in DICOM plugin Scalar Volume when examining loadable 254: VR CAROTIDS 3: Reference image in series does not contain geometry information. Please use caution.</p>
<p>[Python] Warning in DICOM plugin Scalar Volume when examining loadable 256: RICA: Reference image in series does not contain geometry information. Please use caution.</p>
<p>[Python] Warning in DICOM plugin Scalar Volume when examining loadable 257: RVA: Reference image in series does not contain geometry information. Please use caution.</p>
<p>[Python] Warning in DICOM plugin Scalar Volume when examining loadable 258: LICA: Reference image in series does not contain geometry information. Please use caution.</p>
<p>[Python] Warning in DICOM plugin Scalar Volume when examining loadable 259: LVA: Reference image in series does not contain geometry information. Please use caution.</p>
<p>[Python] Warning in DICOM plugin Scalar Volume when examining loadable 261: LICA PATHOLOGY: Reference image in series does not contain geometry information. Please use caution.</p>
<p>[Python] Warning in DICOM plugin Scalar Volume when examining loadable 262: LICA PATHOLOGY 2: Reference image in series does not contain geometry information. Please use caution.</p>
<p>[Python] Warning in DICOM plugin Scalar Volume when examining loadable 999: Dose Report: Reference image in series does not contain geometry information. Please use caution.</p>
<p>[Python] Warning in DICOM plugin Scalar Volume when examining loadable 1000: Key Images: Reference image in series does not contain geometry information. Please use caution.</p>
<p>[Python] Cannot get DICOM slice positions for volume 1: Scout</p>
<p>[Python] No geometry information available for DICOM data, skipping corner calculations</p>
<p>[Python] No geometry information available for DICOM data, skipping corner calculations</p>
<p>[Python] No geometry information available for DICOM data, skipping corner calculations</p>
<p>[Python] No geometry information available for DICOM data, skipping corner calculations</p>
<p>[Python] No geometry information available for DICOM data, skipping corner calculations</p>
<p>[Python] No geometry information available for DICOM data, skipping corner calculations</p>
<p>[Python] No geometry information available for DICOM data, skipping corner calculations</p>
<p>[Python] No geometry information available for DICOM data, skipping corner calculations</p>
<p>[Python] No geometry information available for DICOM data, skipping corner calculations</p>
<p>[Python] No geometry information available for DICOM data, skipping corner calculations</p>
<p>[VTK] Exception from vtkITK MegaMacro:</p>
<p>[VTK] itk::InvalidRequestedRegionError (0x600004e4ece0)</p>
<p>[VTK] Location: “unknown”</p>
<p>[VTK] File: /Users/svc-dashboard/D/S/A/ITK/Modules/IO/ImageBase/include/itkImageFileReader.hxx</p>
<p>[VTK] Line: 338</p>
<p>[VTK] Description: ImageIO returns IO region that does not fully contain the requested region. Requested region: ImageRegion (0x7ff7bf38aa00)</p>
<p>[VTK] Dimension: 3</p>
<p>[VTK] Index: [0, 0, 0]</p>
<p>[VTK] Size: [1522, 1678, 1]</p>
<p>[VTK] StreamableRegion region: ImageRegion (0x7ff7bf38aa38)</p>
<p>[VTK] Dimension: 3</p>
<p>[VTK] Index: [0, 0, 0]</p>
<p>[VTK] Size: [759, 827, 1]</p>
<p>[VTK] Algorithm vtkITKArchetypeImageSeriesVectorReaderSeries (0x7f8182c187a0) returned failure for request: vtkInformation (0x600009bae400)</p>
<p>[VTK] Debug: Off</p>
<p>[VTK] Modified Time: 386326</p>
<p>[VTK] Reference Count: 1</p>
<p>[VTK] Registered Events: (none)</p>
<p>[VTK] Request: REQUEST_DATA</p>
<p>[VTK] FROM_OUTPUT_PORT: 0</p>
<p>[VTK] ALGORITHM_AFTER_FORWARD: 1</p>
<p>[VTK] FORWARD_DIRECTION: 0</p>
<p>[Python] Could not read scalar volume using GDCM approach. Error is: FileFormatError</p>
<p>[VTK] Exception from vtkITK MegaMacro:</p>
<p>[VTK] itk::InvalidRequestedRegionError (0x60000496f820)</p>
<p>[VTK] Location: “unknown”</p>
<p>[VTK] File: /Users/svc-dashboard/D/S/A/ITK/Modules/IO/ImageBase/include/itkImageFileReader.hxx</p>
<p>[VTK] Line: 338</p>
<p>[VTK] Description: ImageIO returns IO region that does not fully contain the requested region. Requested region: ImageRegion (0x7ff7bf38aa00)</p>
<p>[VTK] Dimension: 3</p>
<p>[VTK] Index: [0, 0, 0]</p>
<p>[VTK] Size: [1522, 1678, 1]</p>
<p>[VTK] StreamableRegion region: ImageRegion (0x7ff7bf38aa38)</p>
<p>[VTK] Dimension: 3</p>
<p>[VTK] Index: [0, 0, 0]</p>
<p>[VTK] Size: [759, 827, 1]</p>
<p>[VTK] Algorithm vtkITKArchetypeImageSeriesVectorReaderSeries (0x7f8186c93f60) returned failure for request: vtkInformation (0x600009b59ec0)</p>
<p>[VTK] Debug: Off</p>
<p>[VTK] Modified Time: 386530</p>
<p>[VTK] Reference Count: 1</p>
<p>[VTK] Registered Events: (none)</p>
<p>[VTK] Request: REQUEST_DATA</p>
<p>[VTK] FROM_OUTPUT_PORT: 0</p>
<p>[VTK] ALGORITHM_AFTER_FORWARD: 1</p>
<p>[VTK] FORWARD_DIRECTION: 0</p>
<p>[Python] Could not read scalar volume using DCMTK approach. Error is: FileFormatError</p>
<p>[Python] Could not load: 1000: Key Images as a Scalar Volume</p>
<p>[Python] Warning in DICOM plugin Scalar Volume when examining loadable 252: VR CAROTIDS 1: Reference image in series does not contain geometry information. Please use caution.</p>
<p>[Python] Warning in DICOM plugin Scalar Volume when examining loadable 253: VR CAROTIDS 2: Reference image in series does not contain geometry information. Please use caution.</p>
<p>[Python] Warning in DICOM plugin Scalar Volume when examining loadable 254: VR CAROTIDS 3: Reference image in series does not contain geometry information. Please use caution.</p>
<p>[Python] Warning in DICOM plugin Scalar Volume when examining loadable 256: RICA: Reference image in series does not contain geometry information. Please use caution.</p>
<p>[Python] Warning in DICOM plugin Scalar Volume when examining loadable 257: RVA: Reference image in series does not contain geometry information. Please use caution.</p>
<p>[Python] Warning in DICOM plugin Scalar Volume when examining loadable 258: LICA: Reference image in series does not contain geometry information. Please use caution.</p>
<p>[Python] Warning in DICOM plugin Scalar Volume when examining loadable 259: LVA: Reference image in series does not contain geometry information. Please use caution.</p>
<p>[Python] Warning in DICOM plugin Scalar Volume when examining loadable 261: LICA PATHOLOGY: Reference image in series does not contain geometry information. Please use caution.</p>
<p>[Python] Warning in DICOM plugin Scalar Volume when examining loadable 262: LICA PATHOLOGY 2: Reference image in series does not contain geometry information. Please use caution.</p>
<p>[Python] Warning in DICOM plugin Scalar Volume when examining loadable 999: Dose Report: Reference image in series does not contain geometry information. Please use caution.</p>
<p>[Python] Warning in DICOM plugin Scalar Volume when examining loadable 1000: Key Images: Reference image in series does not contain geometry information. Please use caution.</p>
<p>[Python] Cannot get DICOM slice positions for volume 1: Scout_1</p>
<p>[Python] No geometry information available for DICOM data, skipping corner calculations</p>
<p>[Python] No geometry information available for DICOM data, skipping corner calculations</p>
<p>[Python] No geometry information available for DICOM data, skipping corner calculations</p>
<p>[Python] No geometry information available for DICOM data, skipping corner calculations</p>
<p>[Python] No geometry information available for DICOM data, skipping corner calculations</p>
<p>[Python] No geometry information available for DICOM data, skipping corner calculations</p>
<p>[Python] No geometry information available for DICOM data, skipping corner calculations</p>
<p>[Python] No geometry information available for DICOM data, skipping corner calculations</p>
<p>[Python] No geometry information available for DICOM data, skipping corner calculations</p>
<p>[Python] No geometry information available for DICOM data, skipping corner calculations</p>
<p>[VTK] Exception from vtkITK MegaMacro:</p>
<p>[VTK] itk::InvalidRequestedRegionError (0x600008eceba0)</p>
<p>[VTK] Location: “unknown”</p>
<p>[VTK] File: /Users/svc-dashboard/D/S/A/ITK/Modules/IO/ImageBase/include/itkImageFileReader.hxx</p>
<p>[VTK] Line: 338</p>
<p>[VTK] Description: ImageIO returns IO region that does not fully contain the requested region. Requested region: ImageRegion (0x7ff7bf38aa00)</p>
<p>[VTK] Dimension: 3</p>
<p>[VTK] Index: [0, 0, 0]</p>
<p>[VTK] Size: [1522, 1678, 1]</p>
<p>[VTK] StreamableRegion region: ImageRegion (0x7ff7bf38aa38)</p>
<p>[VTK] Dimension: 3</p>
<p>[VTK] Index: [0, 0, 0]</p>
<p>[VTK] Size: [759, 827, 1]</p>
<p>[VTK] Algorithm vtkITKArchetypeImageSeriesVectorReaderSeries (0x7f81882dac30) returned failure for request: vtkInformation (0x600009ad3240)</p>
<p>[VTK] Debug: Off</p>
<p>[VTK] Modified Time: 975758</p>
<p>[VTK] Reference Count: 1</p>
<p>[VTK] Registered Events: (none)</p>
<p>[VTK] Request: REQUEST_DATA</p>
<p>[VTK] FROM_OUTPUT_PORT: 0</p>
<p>[VTK] ALGORITHM_AFTER_FORWARD: 1</p>
<p>[VTK] FORWARD_DIRECTION: 0</p>
<p>[Python] Could not read scalar volume using GDCM approach. Error is: FileFormatError</p>
<p>[VTK] Exception from vtkITK MegaMacro:</p>
<p>[VTK] itk::InvalidRequestedRegionError (0x600008eceba0)</p>
<p>[VTK] Location: “unknown”</p>
<p>[VTK] File: /Users/svc-dashboard/D/S/A/ITK/Modules/IO/ImageBase/include/itkImageFileReader.hxx</p>
<p>[VTK] Line: 338</p>
<p>[VTK] Description: ImageIO returns IO region that does not fully contain the requested region. Requested region: ImageRegion (0x7ff7bf38aa00)</p>
<p>[VTK] Dimension: 3</p>
<p>[VTK] Index: [0, 0, 0]</p>
<p>[VTK] Size: [1522, 1678, 1]</p>
<p>[VTK] StreamableRegion region: ImageRegion (0x7ff7bf38aa38)</p>
<p>[VTK] Dimension: 3</p>
<p>[VTK] Index: [0, 0, 0]</p>
<p>[VTK] Size: [759, 827, 1]</p>
<p>[VTK] Algorithm vtkITKArchetypeImageSeriesVectorReaderSeries (0x7f8186ceba60) returned failure for request: vtkInformation (0x600009b21380)</p>
<p>[VTK] Debug: Off</p>
<p>[VTK] Modified Time: 975962</p>
<p>[VTK] Reference Count: 1</p>
<p>[VTK] Registered Events: (none)</p>
<p>[VTK] Request: REQUEST_DATA</p>
<p>[VTK] FROM_OUTPUT_PORT: 0</p>
<p>[VTK] ALGORITHM_AFTER_FORWARD: 1</p>
<p>[VTK] FORWARD_DIRECTION: 0</p>
<p>[Python] Could not read scalar volume using DCMTK approach. Error is: FileFormatError</p>
<p>[Python] Could not load: 1000: Key Images as a Scalar Volume</p>

---
