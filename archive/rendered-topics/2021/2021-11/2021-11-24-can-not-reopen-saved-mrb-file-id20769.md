---
topic_id: 20769
title: "Can Not Reopen Saved Mrb File"
date: 2021-11-24
url: https://discourse.slicer.org/t/20769
---

# Can not reopen saved mrb file

**Topic ID**: 20769
**Date**: 2021-11-24
**URL**: https://discourse.slicer.org/t/can-not-reopen-saved-mrb-file/20769

---

## Post #1 by @Ash_Alarfaj (2021-11-24 10:03 UTC)

<p>Operating system: mac os<br>
Slicer version: 4.11<br>
Expected behavior: open saved mrb file<br>
Actual behavior: can not open or import the mrb file</p>

---

## Post #2 by @lassoan (2021-11-25 04:27 UTC)

<p>What Slicer version did you use to save the file?<br>
Have you saved the scene on a virtual file system (Box, Google cloud drive) or network drive (shared network drive)?</p>
<p>Could you copy here the error messages from the application log (menu: Help / Report a bug) after attempting to load the scene?</p>
<p>Could you try renaming the file to have .zip extension and unzip it?</p>

---

## Post #3 by @Ash_Alarfaj (2021-11-26 15:01 UTC)

<p>HELLO Andras</p>
<p>Thanks a lot for your response. the version slices4.11, MAC OS. the problem is I can not open any saved work in mrb. format. I usually open many files at the same time before one year but now it seems not, I need to review my work on some occasion please help me on that. no error appeared but the programme did not import or reopen the mrb. files in one drive or local drive. However, the original file can open easily. I have attached a screenshot please find it.</p>
<p>Regards<br>
Ashwaj</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/eac259a80a8c0c26612d7e5210512db1f63cd727.jpeg" data-download-href="/uploads/short-url/xuM7x5FeHBCcztiP7Y5eekEqB3F.jpeg?dl=1" title="Screenshot 2021-11-26 at 1.51.30 pm.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eac259a80a8c0c26612d7e5210512db1f63cd727_2_690x327.jpeg" alt="Screenshot 2021-11-26 at 1.51.30 pm.jpg" data-base62-sha1="xuM7x5FeHBCcztiP7Y5eekEqB3F" width="690" height="327" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eac259a80a8c0c26612d7e5210512db1f63cd727_2_690x327.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eac259a80a8c0c26612d7e5210512db1f63cd727_2_1035x490.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eac259a80a8c0c26612d7e5210512db1f63cd727_2_1380x654.jpeg 2x" data-dominant-color="EBE9EB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2021-11-26 at 1.51.30 pm.jpg</span><span class="informations">1729×820 199 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2021-11-26 15:07 UTC)

<p>Try with latest Slicer Preview Release. It gives a detailed report about what is going wrong during scene reading.</p>
<p>Note that in general you cannot open a file created by a future Slicer version (Slicer-4.11 cannot open all files saved by Slicer-4.13), so if you start saving data using the latest Slicer Preview Release then you cannot switch back to the Slicer Stable Release.</p>

---

## Post #5 by @Ash_Alarfaj (2021-11-29 13:29 UTC)

<p>Hello Andras</p>
<p>These are the information you need regarding not opening the mrb post-processed images,I have tried sliceser 4.11 and 4.13 they are not responded, the images processed in slicer 4.11. The only one version opened the mrb is the old version slicer 4.10 it gives only the statistic measurement without the images.</p>
<p>[DEBUG][Qt] 29.11.2021 13:21:46 [] (unknown:0) - Session start time …: 2021-11-29 13:21:46<br>
[DEBUG][Qt] 29.11.2021 13:21:46 [] (unknown:0) - Slicer version …: 4.13.0-2021-11-25 (revision 30440 / 9ecc30b) macosx-amd64 - installed release<br>
[DEBUG][Qt] 29.11.2021 13:21:46 [] (unknown:0) - Operating system …: macOS / 11.6 / 20G165 / UTF-8 - 64-bit<br>
[DEBUG][Qt] 29.11.2021 13:21:46 [] (unknown:0) - Memory …: 8192 MB physical, 3072 MB virtual<br>
[DEBUG][Qt] 29.11.2021 13:21:46 [] (unknown:0) - CPU …: GenuineIntel Intel(R) Core™ i5-1030NG7 CPU @ 1.10GHz, 4 cores, 8 logical processors<br>
[DEBUG][Qt] 29.11.2021 13:21:46 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, Sequential threading<br>
[DEBUG][Qt] 29.11.2021 13:21:46 [] (unknown:0) - Qt configuration …: version 5.15.2, with SSL, requested OpenGL 3.2 (core profile)<br>
[DEBUG][Qt] 29.11.2021 13:21:46 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 29.11.2021 13:21:46 [] (unknown:0) - Application path …: /Applications/Slicer 3.app/Contents/MacOS<br>
[DEBUG][Qt] 29.11.2021 13:21:46 [] (unknown:0) - Additional module paths …: (none)<br>
[DEBUG][Python] 29.11.2021 13:21:49 [Python] (/Applications/Slicer 3.app/Contents/lib/Slicer-4.13/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 29.11.2021 13:21:50 [Python] (/Applications/Slicer 3.app/Contents/lib/Slicer-4.13/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 29.11.2021 13:21:50 [Python] (/Applications/Slicer 3.app/Contents/lib/Slicer-4.13/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 29.11.2021 13:21:50 [] (unknown:0) - Switch to module: “Welcome”</p>

---

## Post #6 by @lassoan (2021-11-29 13:55 UTC)

<p>It seems that you have very little virtual memory available. On macOS I think it is due to low disk space. Please free up at least a few 10GB more disk space and see if the problem is resolved.</p>
<p>If not then you can share an example mrb file - upload it to your dropbox, onedrive, google drive, etc. and send the link - and we can investigate if there is any problem with the file. If you don’t want to share the file publicly then you can send the link in a private message.</p>

---

## Post #7 by @lassoan (2021-12-01 22:05 UTC)

<p>I’ve tested loading of the file that you shared using the latest Slicer Preview Release on Windows, Linux, and macOS. The image and segmentation appeared without any problems.</p>
<p>Could you copy here the error messages from the application log (menu: Help / Report a bug) after attempting to load the scene? (the log that you copied above was created before attempting to load the scene)</p>

---

## Post #8 by @Ash_Alarfaj (2021-12-01 22:10 UTC)

<p>Yes sure, that is<br>
[DEBUG][Qt] 01.12.2021 15:57:48 [] (unknown:0) - Session start time …: 2021-12-01 15:57:48<br>
[DEBUG][Qt] 01.12.2021 15:57:48 [] (unknown:0) - Slicer version …: 4.11.20210226 (revision 29738 / 7a593c8) macosx-amd64 - installed release<br>
[DEBUG][Qt] 01.12.2021 15:57:48 [] (unknown:0) - Operating system …: macOS / 11.6 / 20G165 / UTF-8 - 64-bit<br>
[DEBUG][Qt] 01.12.2021 15:57:48 [] (unknown:0) - Memory …: 8192 MB physical, 2048 MB virtual<br>
[DEBUG][Qt] 01.12.2021 15:57:48 [] (unknown:0) - CPU …: GenuineIntel Intel(R) Core™ i5-1030NG7 CPU @ 1.10GHz, 4 cores, 8 logical processors<br>
[DEBUG][Qt] 01.12.2021 15:57:48 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, Sequential threading<br>
[DEBUG][Qt] 01.12.2021 15:57:48 [] (unknown:0) - Qt configuration …: version 5.15.1, with SSL, requested OpenGL 3.2 (core profile)<br>
[DEBUG][Qt] 01.12.2021 15:57:48 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 01.12.2021 15:57:48 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 01.12.2021 15:57:48 [] (unknown:0) - Application path …: /Applications/Slicer 2.app/Contents/MacOS<br>
[DEBUG][Qt] 01.12.2021 15:57:48 [] (unknown:0) - Additional module paths …: (none)<br>
[DEBUG][Python] 01.12.2021 15:57:50 [Python] (/Applications/Slicer 2.app/Contents/lib/Python/lib/python3.6/site-packages/pydicom/datadict.py:432) - Reversing DICOM dictionary so can look up tag from a keyword…<br>
[CRITICAL][Qt] 01.12.2021 15:57:51 [] (unknown:0) - setViewLabel should be called before setViewNode !<br>
[CRITICAL][Qt] 01.12.2021 15:57:51 [] (unknown:0) - setViewLabel should be called before setViewNode !<br>
[DEBUG][Python] 01.12.2021 15:57:53 [Python] (/Applications/Slicer 2.app/Contents/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[CRITICAL][Qt] 01.12.2021 15:57:53 [] (unknown:0) - setViewLabel should be called before setViewNode !<br>
[CRITICAL][Qt] 01.12.2021 15:57:53 [] (unknown:0) - setViewLabel should be called before setViewNode !<br>
[CRITICAL][Qt] 01.12.2021 15:57:53 [] (unknown:0) - setViewLabel should be called before setViewNode !<br>
[CRITICAL][Qt] 01.12.2021 15:57:53 [] (unknown:0) - setViewLabel should be called before setViewNode !<br>
[CRITICAL][Qt] 01.12.2021 15:57:53 [] (unknown:0) - setViewLabel should be called before setViewNode !<br>
[CRITICAL][Qt] 01.12.2021 15:57:53 [] (unknown:0) - setViewLabel should be called before setViewNode !<br>
[CRITICAL][Qt] 01.12.2021 15:57:53 [] (unknown:0) - setViewLabel should be called before setViewNode !<br>
[CRITICAL][Qt] 01.12.2021 15:57:53 [] (unknown:0) - setViewLabel should be called before setViewNode !<br>
[CRITICAL][Qt] 01.12.2021 15:57:53 [] (unknown:0) - setViewLabel should be called before setViewNode !<br>
[DEBUG][Python] 01.12.2021 15:57:53 [Python] (/Applications/Slicer 2.app/Contents/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 01.12.2021 15:57:53 [Python] (/Applications/Slicer 2.app/Contents/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[CRITICAL][Qt] 01.12.2021 15:57:53 [] (unknown:0) - setViewLabel should be called before setViewNode !<br>
[CRITICAL][Qt] 01.12.2021 15:57:53 [] (unknown:0) - setViewLabel should be called before setViewNode !<br>
[CRITICAL][Qt] 01.12.2021 15:57:53 [] (unknown:0) - setViewLabel should be called before setViewNode !<br>
[DEBUG][Qt] 01.12.2021 15:57:54 [] (unknown:0) - Switch to module: “Welcome”<br>
[CRITICAL][Qt] 01.12.2021 15:57:55 [] (unknown:0) - setViewLabel should be called before setViewNode !<br>
[CRITICAL][Qt] 01.12.2021 15:57:55 [] (unknown:0) - setViewLabel should be called before setViewNode !<br>
[DEBUG][Qt] 01.12.2021 15:58:04 [] (unknown:0) - Switch to module: “DICOM”<br>
[WARNING][VTK] 01.12.2021 15:58:05 [vtkMRMLSubjectHierarchyNode (0x7fe7e13b9910)] (/Volumes/D/S/S-1/Libs/MRML/Core/vtkMRMLSubjectHierarchyNode.cxx:2226) - GetItemOwnerPluginName: Invalid item ID given<br>
[WARNING][VTK] 01.12.2021 15:58:05 [vtkMRMLSubjectHierarchyNode (0x7fe7e13b9910)] (/Volumes/D/S/S-1/Libs/MRML/Core/vtkMRMLSubjectHierarchyNode.cxx:2147) - GetItemName: Invalid item ID given<br>
[CRITICAL][Qt] 01.12.2021 15:58:05 [] (unknown:0) - qSlicerSubjectHierarchyAbstractPlugin *qSlicerSubjectHierarchyPluginHandler::getOwnerPluginForSubjectHierarchyItem(vtkIdType) : Item ’ ’ is not owned by any plugin<br>
[CRITICAL][Qt] 01.12.2021 15:58:05 [] (unknown:0) - setViewLabel should be called before setViewNode !<br>
[DEBUG][Qt] 01.12.2021 15:58:05 [] (unknown:0) - Skipped 104 files that were already in the database: /Users/ashwajalarfaj/OneDrive - University of Exeter/MRI-Ramadan-2021/UOE_RAM_13_UOE_RAM_13/V1_MUSCLE_RAMADAN_20210401_113334_975000_MUSCLE/T1_VIBE_DIXON_TRA_P2_1_5MM_F_0007/UOE_RAM_13.MR.MUSCLE_RAMADAN.0007.0035.2021.06.29.11.06.47.259679.71343899.IMA, /Users/ashwajalarfaj/OneDrive - University of Exeter/MRI-Ramadan-2021/UOE_RAM_13_UOE_RAM_13/V1_MUSCLE_RAMADAN_20210401_113334_975000_MUSCLE/T1_VIBE_DIXON_TRA_P2_1_5MM_F_0007/UOE_RAM_13.MR.MUSCLE_RAMADAN.0007.0003.2021.06.29.11.06.47.259679.71343323.IMA, /Users/ashwajalarfaj/OneDrive - University of Exeter/MRI-Ramadan-2021/UOE_RAM_13_UOE_RAM_13/V1_MUSCLE_RAMADAN_20210401_113334_975000_MUSCLE/T1_VIBE_DIXON_TRA_P2_1_5MM_F_0007/UOE_RAM_13.MR.MUSCLE_RAMADAN.0007.0004.2021.06.29.11.06.47.259679.71343341.IMA, /Users/ashwajalarfaj/OneDrive - University of Exeter/MRI-Ramadan-2021/UOE_RAM_13_UOE_RAM_13/V1_MUSCLE_RAMADAN_20210401_113334_975000_MUSCLE/T1_VIBE_DIXON_TRA_P2_1_5MM_F_0007/UOE_RAM_13.MR.MUSCLE_RAMADAN.0007.0001.2021.06.29.11.06.47.259679.71343287.IMA, /Users/ashwajalarfaj/OneDrive - University of Exeter/MRI-Ramadan-2021/UOE_RAM_13_UOE_RAM_13/V1_MUSCLE_RAMADAN_20210401_113334_975000_MUSCLE/T1_VIBE_DIXON_TRA_P2_1_5MM_F_0007/UOE_RAM_13.MR.MUSCLE_RAMADAN.0007.0036.2021.06.29.11.06.47.259679.71343917.IMA, /Users/ashwajalarfaj/OneDrive - University of Exeter/MRI-Ramadan-2021/UOE_RAM_13_UOE_RAM_13/V1_MUSCLE_RAMADAN_20210401_113334_975000_MUSCLE/T1_VIBE_DIXON_TRA_P2_1_5MM_F_0007/UOE_RAM_13.MR.MUSCLE_RAMADAN.0007.0087.2021.06.29.11.06.47.259679.71344835.IMA, /Users/ashwajalarfaj/OneDrive - University of Exeter/MRI-Ramadan-2021/UOE_RAM_13_UOE_RAM_13/V1_MUSCLE_RAMADAN_20210401_113334_975000_MUSCLE/T1_VIBE_DIXON_TRA_P2_1_5MM_F_0007/UOE_RAM_13.MR.MUSCLE_RAMADAN.0007.0078.2021.06.29.11.06.47.259679.71344673.IMA, /Users/ashwajalarfaj/OneDrive - University of Exeter/MRI-Ramadan-2021/UOE_RAM_13_UOE_RAM_13/V1_MUSCLE_RAMADAN_20210401_113334_975000_MUSCLE/T1_VIBE_DIXON_TRA_P2_1_5MM_F_0007/UOE_RAM_13.MR.MUSCLE_RAMADAN.0007.0050.2021.06.29.11.06.47.259679.71344169.IMA, /Users/ashwajalarfaj/OneDrive - University of Exeter/MRI-Ramadan-2021/UOE_RAM_13_UOE_RAM_13/V1_MUSCLE_RAMADAN_20210401_113334_975000_MUSCLE/T1_VIBE_DIXON_TRA_P2_1_5MM_F_0007/UOE_RAM_13.MR.MUSCLE_RAMADAN.0007.0057.2021.06.29.11.06.47.259679.71344295.IMA…<br>
[DEBUG][Qt] 01.12.2021 15:58:05 [] (unknown:0) - “DICOM indexer has successfully processed 104 files [0.01s]”<br>
[DEBUG][Qt] 01.12.2021 15:58:05 [] (unknown:0) - “DICOM indexer has updated display fields for 0 files [0.00s]”<br>
[INFO][Python] 01.12.2021 15:58:05 [Python] (/Applications/Slicer 2.app/Contents/lib/Slicer-4.11/qt-scripted-modules/DICOMLib/DICOMBrowser.py:268) - Imported a DICOM directory, checking for extensions<br>
[INFO][Stream] 01.12.2021 15:58:05 [] (unknown:0) - Imported a DICOM directory, checking for extensions<br>
[INFO][Python] 01.12.2021 15:58:11 [Python] (/Applications/Slicer 2.app/Contents/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:384) - Loading with imageIOName: GDCM<br>
[INFO][Python] 01.12.2021 15:58:12 [Python] (/Applications/Slicer 2.app/Contents/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:458) - Window/level found in DICOM tags (center=596.0, width=1263.0) has been applied to volume 7: t1_vibe_dixon_tra_p2_1.5mm_F<br>
[DEBUG][Python] 01.12.2021 15:58:12 [Python] (/Applications/Slicer 2.app/Contents/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:799) - Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 7.57482e-06 mm, tolerance threshold is 0.001 mm).<br>
[INFO][Stream] 01.12.2021 15:58:11 [] (unknown:0) - Loading with imageIOName: GDCM<br>
[INFO][Stream] 01.12.2021 15:58:12 [] (unknown:0) - Window/level found in DICOM tags (center=596.0, width=1263.0) has been applied to volume 7: t1_vibe_dixon_tra_p2_1.5mm_F<br>
[CRITICAL][Qt] 01.12.2021 15:58:12 [] (unknown:0) - setViewLabel should be called before setViewNode !<br>
[DEBUG][Qt] 01.12.2021 15:58:25 [] (unknown:0) - Switch to module: “CropVolume”<br>
[DEBUG][Qt] 01.12.2021 15:58:47 [] (unknown:0) - Found CommandLine Module, target is /Applications/Slicer 2.app/Contents/lib/Slicer-4.11/cli-modules/ResampleScalarVectorDWIVolume<br>
[DEBUG][Qt] 01.12.2021 15:58:47 [] (unknown:0) - ModuleType: CommandLineModule<br>
[DEBUG][Qt] 01.12.2021 15:58:47 [] (unknown:0) - Resample Scalar/Vector/DWI Volume command line:</p>
<p>/Applications/Slicer 2.app/Contents/lib/Slicer-4.11/cli-modules/ResampleScalarVectorDWIVolume --hfieldtype h-Field --interpolation linear --transform_order output-to-input --image_center input --spacing 0.9598,0.9598,1.50000000000001 --size 230,218,104 --origin -198.477,-79.4778,-160.246 --direction_matrix 0.999657324989487,0,-0.0261769477759099,0,1,0,0.0261769477759099,0,0.999657324989487 --number_of_thread 0 --default_pixel_value 0 --window_function c --spline_order 3 --transform_matrix 1,0,0,0,1,0,0,0,1,0,0,0 --transform a /private/var/folders/36/zgh4v70j1bqgsbfmvdprqt6m0000gn/T/Slicer-ashwajalarfaj/EDAG_vtkMRMLScalarVolumeNodeB.nrrd /private/var/folders/36/zgh4v70j1bqgsbfmvdprqt6m0000gn/T/Slicer-ashwajalarfaj/EDAG_vtkMRMLScalarVolumeNodeC.nrrd<br>
[DEBUG][Qt] 01.12.2021 15:58:48 [] (unknown:0) - Resample Scalar/Vector/DWI Volume completed without errors<br>
[INFO][VTK] 01.12.2021 15:58:49 [vtkMRMLVolumeArchetypeStorageNode (0x7fe7d144d280)] (/Volumes/D/S/S-1/Libs/MRML/Core/vtkMRMLVolumeArchetypeStorageNode.cxx:509) - Loaded volume from file: /private/var/folders/36/zgh4v70j1bqgsbfmvdprqt6m0000gn/T/Slicer-ashwajalarfaj/EDAG_vtkMRMLScalarVolumeNodeC.nrrd. Dimensions: 230x218x104. Number of components: 1. Pixel type: unsigned short.<br>
[DEBUG][Qt] 01.12.2021 15:58:51 [] (unknown:0) - Switch to module: “SegmentEditor”<br>
[INFO][Python] 01.12.2021 16:01:26 [Python] (/Applications/Slicer 2.app/Contents/lib/Slicer-4.11/qt-scripted-modules/SegmentEditorEffects/SegmentEditorIslandsEffect.py:158) - 1 islands created (0 ignored)<br>
[INFO][Stream] 01.12.2021 16:01:26 [] (unknown:0) - 1 islands created (0 ignored)<br>
[INFO][Python] 01.12.2021 16:01:28 [Python] (/Applications/Slicer 2.app/Contents/lib/Slicer-4.11/qt-scripted-modules/SegmentEditorEffects/SegmentEditorIslandsEffect.py:158) - 1 islands created (0 ignored)<br>
[INFO][Stream] 01.12.2021 16:01:28 [] (unknown:0) - 1 islands created (0 ignored)<br>
[DEBUG][Qt] 01.12.2021 16:01:32 [] (unknown:0) - Switch to module: “SegmentStatistics”<br>
[CRITICAL][Qt] 01.12.2021 16:01:36 [] (unknown:0) - setViewLabel should be called before setViewNode !<br>
[CRITICAL][Qt] 01.12.2021 16:01:36 [] (unknown:0) - setViewLabel should be called before setViewNode !<br>
[CRITICAL][Qt] 01.12.2021 16:03:34 [] (unknown:0) - setViewLabel should be called before setViewNode !<br>
[INFO][VTK] 01.12.2021 16:04:42 [] (unknown:0) - Info: In /Volumes/D/S/S-1/Libs/MRML/Core/vtkArchive.cxx, line 39<br>
Zip: adding: /Users/ashwajalarfaj/Documents/RAM_2021_MUSCLE VOLUME/__BundleSaveTemp-2021-12-01_160440_664/C13.V1.F.R.THIGH.TRUE.2021-12-01-Scene/C13.mrml<br>
[INFO][VTK] 01.12.2021 16:04:42 [] (unknown:0) - Info: In /Volumes/D/S/S-1/Libs/MRML/Core/vtkArchive.cxx, line 39<br>
Zip: adding rel: C13.V1.F.R.THIGH.TRUE.2021-12-01-Scene/C13.mrml<br>
[INFO][VTK] 01.12.2021 16:04:42 [] (unknown:0) - Info: In /Volumes/D/S/S-1/Libs/MRML/Core/vtkArchive.cxx, line 39<br>
Zip: adding: /Users/ashwajalarfaj/Documents/RAM_2021_MUSCLE VOLUME/__BundleSaveTemp-2021-12-01_160440_664/C13.V1.F.R.THIGH.TRUE.2021-12-01-Scene/C13.png<br>
[INFO][VTK] 01.12.2021 16:04:42 [] (unknown:0) - Info: In /Volumes/D/S/S-1/Libs/MRML/Core/vtkArchive.cxx, line 39<br>
Zip: adding rel: C13.V1.F.R.THIGH.TRUE.2021-12-01-Scene/C13.png<br>
[INFO][VTK] 01.12.2021 16:04:42 [] (unknown:0) - Info: In /Volumes/D/S/S-1/Libs/MRML/Core/vtkArchive.cxx, line 39<br>
Zip: adding: /Users/ashwajalarfaj/Documents/RAM_2021_MUSCLE VOLUME/__BundleSaveTemp-2021-12-01_160440_664/C13.V1.F.R.THIGH.TRUE.2021-12-01-Scene/Data/7 t1_vibe_dixon_tra_p2_1.5mm_F.nrrd<br>
[INFO][VTK] 01.12.2021 16:04:42 [] (unknown:0) - Info: In /Volumes/D/S/S-1/Libs/MRML/Core/vtkArchive.cxx, line 39<br>
Zip: adding rel: C13.V1.F.R.THIGH.TRUE.2021-12-01-Scene/Data/7 t1_vibe_dixon_tra_p2_1.5mm_F.nrrd<br>
[INFO][VTK] 01.12.2021 16:04:42 [] (unknown:0) - Info: In /Volumes/D/S/S-1/Libs/MRML/Core/vtkArchive.cxx, line 39<br>
Zip: adding: /Users/ashwajalarfaj/Documents/RAM_2021_MUSCLE VOLUME/__BundleSaveTemp-2021-12-01_160440_664/C13.V1.F.R.THIGH.TRUE.2021-12-01-Scene/Data/Crop volume ROI alignment.h5<br>
[INFO][VTK] 01.12.2021 16:04:42 [] (unknown:0) - Info: In /Volumes/D/S/S-1/Libs/MRML/Core/vtkArchive.cxx, line 39<br>
Zip: adding rel: C13.V1.F.R.THIGH.TRUE.2021-12-01-Scene/Data/Crop volume ROI alignment.h5<br>
[INFO][VTK] 01.12.2021 16:04:42 [] (unknown:0) - Info: In /Volumes/D/S/S-1/Libs/MRML/Core/vtkArchive.cxx, line 39<br>
Zip: adding: /Users/ashwajalarfaj/Documents/RAM_2021_MUSCLE VOLUME/__BundleSaveTemp-2021-12-01_160440_664/C13.V1.F.R.THIGH.TRUE.2021-12-01-Scene/Data/Segmentation.seg.nrrd<br>
[INFO][VTK] 01.12.2021 16:04:42 [] (unknown:0) - Info: In /Volumes/D/S/S-1/Libs/MRML/Core/vtkArchive.cxx, line 39<br>
Zip: adding rel: C13.V1.F.R.THIGH.TRUE.2021-12-01-Scene/Data/Segmentation.seg.nrrd<br>
[INFO][VTK] 01.12.2021 16:04:42 [] (unknown:0) - Info: In /Volumes/D/S/S-1/Libs/MRML/Core/vtkArchive.cxx, line 39<br>
Zip: adding: /Users/ashwajalarfaj/Documents/RAM_2021_MUSCLE VOLUME/__BundleSaveTemp-2021-12-01_160440_664/C13.V1.F.R.THIGH.TRUE.2021-12-01-Scene/Data/Crop Volume ROI.acsv<br>
[INFO][VTK] 01.12.2021 16:04:42 [] (unknown:0) - Info: In /Volumes/D/S/S-1/Libs/MRML/Core/vtkArchive.cxx, line 39<br>
Zip: adding rel: C13.V1.F.R.THIGH.TRUE.2021-12-01-Scene/Data/Crop Volume ROI.acsv<br>
[INFO][VTK] 01.12.2021 16:04:42 [] (unknown:0) - Info: In /Volumes/D/S/S-1/Libs/MRML/Core/vtkArchive.cxx, line 39<br>
Zip: adding: /Users/ashwajalarfaj/Documents/RAM_2021_MUSCLE VOLUME/__BundleSaveTemp-2021-12-01_160440_664/C13.V1.F.R.THIGH.TRUE.2021-12-01-Scene/Data/Table.tsv<br>
[INFO][VTK] 01.12.2021 16:04:42 [] (unknown:0) - Info: In /Volumes/D/S/S-1/Libs/MRML/Core/vtkArchive.cxx, line 39<br>
Zip: adding rel: C13.V1.F.R.THIGH.TRUE.2021-12-01-Scene/Data/Table.tsv<br>
[INFO][VTK] 01.12.2021 16:04:42 [] (unknown:0) - Info: In /Volumes/D/S/S-1/Libs/MRML/Core/vtkArchive.cxx, line 39<br>
Zip: adding: /Users/ashwajalarfaj/Documents/RAM_2021_MUSCLE VOLUME/__BundleSaveTemp-2021-12-01_160440_664/C13.V1.F.R.THIGH.TRUE.2021-12-01-Scene/Data/Table.schema.tsv<br>
[INFO][VTK] 01.12.2021 16:04:42 [] (unknown:0) - Info: In /Volumes/D/S/S-1/Libs/MRML/Core/vtkArchive.cxx, line 39<br>
Zip: adding rel: C13.V1.F.R.THIGH.TRUE.2021-12-01-Scene/Data/Table.schema.tsv<br>
[INFO][VTK] 01.12.2021 16:04:42 [] (unknown:0) - Info: In /Volumes/D/S/S-1/Libs/MRML/Core/vtkArchive.cxx, line 39<br>
Zip: adding: /Users/ashwajalarfaj/Documents/RAM_2021_MUSCLE VOLUME/__BundleSaveTemp-2021-12-01_160440_664/C13.V1.F.R.THIGH.TRUE.2021-12-01-Scene/Data/7 t1_vibe_dixon_tra_p2_1.5mm_F.C13.V1.R.TH…nrrd<br>
[INFO][VTK] 01.12.2021 16:04:42 [] (unknown:0) - Info: In /Volumes/D/S/S-1/Libs/MRML/Core/vtkArchive.cxx, line 39<br>
Zip: adding rel: C13.V1.F.R.THIGH.TRUE.2021-12-01-Scene/Data/7 t1_vibe_dixon_tra_p2_1.5mm_F.C13.V1.R.TH…nrrd<br>
[DEBUG][Qt] 01.12.2021 16:04:42 [] (unknown:0) - saved “/Users/ashwajalarfaj/Documents/RAM_2021_MUSCLE VOLUME/C13.V1.F.R.THIGH.TRUE.2021-12-01-Scene.mrb”<br>
[DEBUG][Qt] 01.12.2021 16:05:14 [] (unknown:0) - Switch to module: “DICOM”<br>
[CRITICAL][Qt] 01.12.2021 16:05:14 [] (unknown:0) - setViewLabel should be called before setViewNode !<br>
[DEBUG][Qt] 01.12.2021 16:05:21 [] (unknown:0) - Switch to module: “SegmentStatistics”<br>
[CRITICAL][Qt] 01.12.2021 16:05:21 [] (unknown:0) - setViewLabel should be called before setViewNode !<br>
[DEBUG][Qt] 01.12.2021 16:05:31 [] (unknown:0) - Close main MRML scene<br>
[CRITICAL][Qt] 01.12.2021 16:05:31 [] (unknown:0) - setViewLabel should be called before setViewNode !<br>
[CRITICAL][Qt] 01.12.2021 16:05:32 [] (unknown:0) - setViewLabel should be called before setViewNode !<br>
[CRITICAL][Qt] 01.12.2021 16:05:32 [] (unknown:0) - setViewLabel should be called before setViewNode !<br>
[CRITICAL][Qt] 01.12.2021 16:05:32 [] (unknown:0) - setViewLabel should be called before setViewNode !<br>
[CRITICAL][Qt] 01.12.2021 16:05:32 [] (unknown:0) - setViewLabel should be called before setViewNode !<br>
[DEBUG][Qt] 01.12.2021 16:05:33 [] (unknown:0) - Switch to module: “DICOM”<br>
[CRITICAL][Qt] 01.12.2021 16:05:33 [] (unknown:0) - setViewLabel should be called before setViewNode !<br>
[DEBUG][Qt] 01.12.2021 16:05:38 [] (unknown:0) - SQLITE: removing seriesInstanceUID 1.3.12.2.1107.5.2.43.166144.2021040111505216647315522.0.0.0<br>
[DEBUG][Qt] 01.12.2021 22:08:45 [] (unknown:0) - Could not load “/Users/ashwajalarfaj/Documents/RAM_2021_MUSCLE VOLUME/C13.V1.F.R.THIGH.2021-12-01-Scene.mrb”<br>
DCMTK says: I/O suspension or premature end of stream<br>
[WARNING][Qt] 01.12.2021 22:08:45 [] (unknown:0) - Could not read DICOM file:/Users/ashwajalarfaj/Documents/RAM_2021_MUSCLE VOLUME/C13.V1.F.R.THIGH.2021-12-01-Scene.mrb<br>
[DEBUG][Qt] 01.12.2021 22:08:45 [] (unknown:0) - “DICOM indexer has successfully processed 1 files [0.00s]”<br>
[DEBUG][Qt] 01.12.2021 22:08:45 [] (unknown:0) - “DICOM indexer has updated display fields for 0 files [0.00s]”<br>
[INFO][Python] 01.12.2021 22:08:46 [Python] (/Applications/Slicer 2.app/Contents/lib/Slicer-4.11/qt-scripted-modules/DICOMLib/DICOMBrowser.py:268) - Imported a DICOM directory, checking for extensions<br>
[INFO][Stream] 01.12.2021 22:08:46 [] (unknown:0) - Imported a DICOM directory, checking for extensions</p>

---

## Post #9 by @lassoan (2021-12-02 00:24 UTC)

<p>The problem is that you drag-and-dropped the mrb file to the application when the DICOM module was active. In this case, all files are interpreted as DICOM. Since the MRB file is not DICOM, the file was not loaded. You can either use the menu (File/Add data) or switch to a different module before drag-and-drop the mrb file to the application window.</p>

---

## Post #10 by @Ash_Alarfaj (2021-12-02 09:41 UTC)

<p>That’s great, yes you have resolved the problem, thanks a lot Andras for your kind support and guide it is such a relive. I switch to data mode, and then all the needed information with the subject hierarchy is there. Just a quick question why we can not save the images in the same original DICOM format?</p>
<p><strong>Warm Regards</strong></p>

---

## Post #11 by @lassoan (2021-12-02 13:39 UTC)

<aside class="quote no-group" data-username="Ash_Alarfaj" data-post="10" data-topic="20769">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ash_alarfaj/48/3327_2.png" class="avatar"> Ash_Alarfaj:</div>
<blockquote>
<p>Just a quick question why we can not save the images in the same original DICOM format?</p>
</blockquote>
</aside>
<p>DICOM files are very good for archival due to pervasive use of unique identifiers, cross-references, and rich structured metadata. However, the same properties make it practically unusable as a working file format (that stores data that is being modified). If your were interested in more details then please create a new topic for this and explain if you have any unmet need related to this question.</p>

---
