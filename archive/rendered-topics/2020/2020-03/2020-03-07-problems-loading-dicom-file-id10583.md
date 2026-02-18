# Problems loading dicom file

**Topic ID**: 10583
**Date**: 2020-03-07
**URL**: https://discourse.slicer.org/t/problems-loading-dicom-file/10583

---

## Post #1 by @hprint3d (2020-03-07 12:51 UTC)

<p>Operating system: windows10<br>
Slicer version: 4.10.2<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hello, first of all, sorry for my English, it is translated by google. I need help with some dicom files that I am unable to load, I have looked a lot around here and I have done several actions, but I cannot load it, I need it to work with it and make it 3D printed. I beg your help, thank you!</p>
<p>Error: could not load: as a 21 frames multivolume by image position pantie + adquisition time as a multivolume.</p>
<p>could not load: 1:  unnamed series as a scalar volume</p>

---

## Post #2 by @pieper (2020-03-07 14:31 UTC)

<p>This is always a good place to start: <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM">https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM</a></p>

---

## Post #3 by @hprint3d (2020-03-10 16:28 UTC)

<p>Hello again, he managed to load the files but selecting any data when incorporating the folder with the files, if I select to load the directory in the DICOM database, I get the multivolume error, he said, I’ve tried everything what you have advised me.</p>
<p>Once loaded, the image appears in the first box, and a flat image in the second and third. Then I try to create the 3D model, but it creates a flat image, will it be a problem with the files? because I already tried for many hours and days and you won’t get the 3D model.</p>
<p>Thank you !!</p>

---

## Post #4 by @pieper (2020-03-10 16:53 UTC)

<p>Unless you are able to share the data we can only guess what might be wrong.  Probably is not a format that is compatible with Slicer (DICOM has many variations) or maybe the data is corrupt.</p>

---

## Post #5 by @hprint3d (2020-03-11 09:19 UTC)

<p>Good morning, then I paste the message that throws me. Thank you!</p>
<p>[DEBUG][Qt] 11.03.2020 10:13:53 [] (unknown:0) - Session start time …: 2020-03-11 10:13:53<br>
[DEBUG][Qt] 11.03.2020 10:13:53 [] (unknown:0) - Slicer version …: 4.10.2 (revision 28257) win-amd64 - installed release<br>
[DEBUG][Qt] 11.03.2020 10:13:53 [] (unknown:0) - Operating system …: Windows /  Professional /  (Build 9200) - 64-bit<br>
[DEBUG][Qt] 11.03.2020 10:13:53 [] (unknown:0) - Memory …: 12252 MB physical, 18689 MB virtual<br>
[DEBUG][Qt] 11.03.2020 10:13:53 [] (unknown:0) - CPU …: GenuineIntel , 4 cores, 4 logical processors<br>
[DEBUG][Qt] 11.03.2020 10:13:53 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 11.03.2020 10:13:53 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 11.03.2020 10:13:53 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 11.03.2020 10:13:53 [] (unknown:0) - Additional module paths …: (none)<br>
[DEBUG][Python] 11.03.2020 10:14:01 [Python] (C:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 11.03.2020 10:14:02 [Python] (C:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 11.03.2020 10:14:02 [Python] (C:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 11.03.2020 10:14:02 [] (unknown:0) - Switch to module:  “Welcome”<br>
[DEBUG][Qt] 11.03.2020 10:14:49 [] (unknown:0) - Switch to module:  “DICOM”<br>
[DEBUG][Qt] 11.03.2020 10:14:49 [] (unknown:0) - New patient inserted: 3<br>
[DEBUG][Qt] 11.03.2020 10:14:49 [] (unknown:0) - New patient inserted as :  3<br>
[DEBUG][Qt] 11.03.2020 10:14:49 [] (unknown:0) - Need to insert new study:  “1.2.410.200001.101.11.501.1501431310.1.20200213164927794”<br>
[DEBUG][Qt] 11.03.2020 10:14:49 [] (unknown:0) - Study Added<br>
[DEBUG][Qt] 11.03.2020 10:14:49 [] (unknown:0) - Need to insert new series:  “1.2.410.200001.101.11.501.1501431310.2.20200213165249399”<br>
[DEBUG][Qt] 11.03.2020 10:14:49 [] (unknown:0) - Series Added<br>
[DEBUG][Qt] 11.03.2020 10:14:50 [] (unknown:0) - “DICOM indexer has successfully processed 26 files [1.00s]”<br>
[INFO][Python] 11.03.2020 10:14:51 [Python] (C:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\DICOMLib\DICOMWidgets.py:471) - Imported a DICOM directory, checking for extensions<br>
[INFO][Stream] 11.03.2020 10:14:51 [] (unknown:0) - Imported a DICOM directory, checking for extensions<br>
[DEBUG][Python] 11.03.2020 10:14:58 [Python] (C:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:455) - MultiVolumeImportPlugin::examine<br>
[DEBUG][Python] 11.03.2020 10:14:58 [Python] (C:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:495) - DICOMMultiVolumePlugin found 2 multivolumes!<br>
[DEBUG][Python] 11.03.2020 10:14:58 [Python] (C:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:165) - MultiVolumeImportPlugin:examineMultiseries<br>
[DEBUG][Python] 11.03.2020 10:14:58 [Python] (C:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:170) - DICOMMultiVolumePlugin found 1 multivolumes!<br>
[INFO][Python] 11.03.2020 10:14:59 [Python] (C:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py:303) - Loading with imageIOName: GDCM<br>
[ERROR][Python] 11.03.2020 10:14:59 [Python] (C:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py:309) - Could not read scalar volume using GDCM approach.  Error is: FileFormatError<br>
[INFO][Python] 11.03.2020 10:14:59 [Python] (C:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py:303) - Loading with imageIOName: DCMTK<br>
[ERROR][Python] 11.03.2020 10:14:59 [Python] (C:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py:309) - Could not read scalar volume using DCMTK approach.  Error is: FileFormatError<br>
[ERROR][Python] 11.03.2020 10:14:59 [Python] (C:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:728) - Failed to read a multivolume: ‘NoneType’ object has no attribute ‘GetImageData’<br>
[WARNING][Python] 11.03.2020 10:14:59 [Python] (C:\Program Files\Slicer 4.10.2\bin\Python\slicer\util.py:1110) -<br>
Could not load:  - as a 22 frames MultiVolume by ImagePositionPatient+AcquisitionTime as a MultiVolume<br>
[INFO][Stream] 11.03.2020 10:14:59 [] (unknown:0) - Loading with imageIOName: GDCM<br>
[ERROR][VTK] 11.03.2020 10:14:59 [vtkITKArchetypeImageSeriesScalarReader (000002BF40C21260)] (D:\D\S\Slicer-4102\Libs\vtkITK\vtkITKArchetypeImageSeriesScalarReader.cxx:230) - UpdateFromFile: Unsupported number of components (only 1 allowed): 3<br>
[CRITICAL][Stream] 11.03.2020 10:14:59 [] (unknown:0) - Could not read scalar volume using GDCM approach.  Error is: FileFormatError<br>
[INFO][Stream] 11.03.2020 10:14:59 [] (unknown:0) - Loading with imageIOName: DCMTK<br>
[CRITICAL][Stream] 11.03.2020 10:14:59 [] (unknown:0) - D:\D\S\Slicer-4102-build\ITK\Modules\ThirdParty\VNL\src\vxl\core\vnl/algo/vnl_svd.hxx: suspicious return value (3) from SVDC<br>
[CRITICAL][Stream] 11.03.2020 10:14:59 [] (unknown:0) - D:\D\S\Slicer-4102-build\ITK\Modules\ThirdParty\VNL\src\vxl\core\vnl/algo/vnl_svd.hxx: M is 3x3<br>
[CRITICAL][Stream] 11.03.2020 10:14:59 [] (unknown:0) - M = [ …<br>
[CRITICAL][Stream] 11.03.2020 10:14:59 [] (unknown:0) -  0.0000000000000             -nan                0<br>
[CRITICAL][Stream] 11.03.2020 10:14:59 [] (unknown:0) -                0             -nan                0<br>
[CRITICAL][Stream] 11.03.2020 10:14:59 [] (unknown:0) -                0             -nan  0.0000000000000  ]<br>
[ERROR][VTK] 11.03.2020 10:14:59 [vtkITKArchetypeImageSeriesScalarReader (000002BF40C23A40)] (D:\D\S\Slicer-4102\Libs\vtkITK\vtkITKArchetypeImageSeriesScalarReader.cxx:230) - UpdateFromFile: Unsupported number of components (only 1 allowed): 3<br>
[CRITICAL][Stream] 11.03.2020 10:14:59 [] (unknown:0) - Could not read scalar volume using DCMTK approach.  Error is: FileFormatError<br>
[CRITICAL][Stream] 11.03.2020 10:14:59 [] (unknown:0) - Failed to read a multivolume: ‘NoneType’ object has no attribute ‘GetImageData’<br>
[CRITICAL][Stream] 11.03.2020 10:14:59 [] (unknown:0) - Traceback (most recent call last):<br>
[CRITICAL][Stream] 11.03.2020 10:14:59 [] (unknown:0) -   File “C:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py”, line 619, in load<br>
[CRITICAL][Stream] 11.03.2020 10:14:59 [] (unknown:0) -     if frame.GetImageData() == None:<br>
[CRITICAL][Stream] 11.03.2020 10:14:59 [] (unknown:0) - AttributeError: ‘NoneType’ object has no attribute ‘GetImageData’<br>
[CRITICAL][Stream] 11.03.2020 10:14:59 [] (unknown:0) -<br>
[CRITICAL][Stream] 11.03.2020 10:14:59 [] (unknown:0) - Could not load:  - as a 22 frames MultiVolume by ImagePositionPatient+AcquisitionTime as a MultiVolume<br>
[INFO][Stream] 11.03.2020 10:15:03 [] (unknown:0) - selected row 0<br>
[INFO][Stream] 11.03.2020 10:15:03 [] (unknown:0) - Today:  for HERRERA ROMERO^CRISTINA<br>
[INFO][Stream] 11.03.2020 10:15:03 [] (unknown:0) - selected row 0<br>
[INFO][Stream] 11.03.2020 10:15:03 [] (unknown:0) - Today:  for HERRERA ROMERO^CRISTINA<br>
[DEBUG][Python] 11.03.2020 10:15:04 [Python] (C:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:455) - MultiVolumeImportPlugin::examine<br>
[DEBUG][Python] 11.03.2020 10:15:04 [Python] (C:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:495) - DICOMMultiVolumePlugin found 2 multivolumes!<br>
[DEBUG][Python] 11.03.2020 10:15:04 [Python] (C:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:165) - MultiVolumeImportPlugin:examineMultiseries<br>
[DEBUG][Python] 11.03.2020 10:15:04 [Python] (C:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:170) - DICOMMultiVolumePlugin found 1 multivolumes!<br>
[INFO][Python] 11.03.2020 10:16:03 [Python] (C:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py:303) - Loading with imageIOName: GDCM<br>
[ERROR][Python] 11.03.2020 10:16:03 [Python] (C:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py:309) - Could not read scalar volume using GDCM approach.  Error is: FileFormatError<br>
[INFO][Python] 11.03.2020 10:16:04 [Python] (C:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py:303) - Loading with imageIOName: DCMTK<br>
[ERROR][Python] 11.03.2020 10:16:04 [Python] (C:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py:309) - Could not read scalar volume using DCMTK approach.  Error is: FileFormatError<br>
[ERROR][Python] 11.03.2020 10:16:04 [Python] (C:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:728) - Failed to read a multivolume: ‘NoneType’ object has no attribute ‘GetImageData’<br>
[WARNING][Python] 11.03.2020 10:16:04 [Python] (C:\Program Files\Slicer 4.10.2\bin\Python\slicer\util.py:1110) -<br>
Could not load:  - as a 22 frames MultiVolume by ImagePositionPatient+AcquisitionTime as a MultiVolume<br>
[INFO][Stream] 11.03.2020 10:16:03 [] (unknown:0) - Loading with imageIOName: GDCM<br>
[ERROR][VTK] 11.03.2020 10:16:03 [vtkITKArchetypeImageSeriesScalarReader (000002BF40C219A0)] (D:\D\S\Slicer-4102\Libs\vtkITK\vtkITKArchetypeImageSeriesScalarReader.cxx:230) - UpdateFromFile: Unsupported number of components (only 1 allowed): 3<br>
[CRITICAL][Stream] 11.03.2020 10:16:04 [] (unknown:0) - Could not read scalar volume using GDCM approach.  Error is: FileFormatError<br>
[INFO][Stream] 11.03.2020 10:16:04 [] (unknown:0) - Loading with imageIOName: DCMTK<br>
[CRITICAL][Stream] 11.03.2020 10:16:04 [] (unknown:0) - D:\D\S\Slicer-4102-build\ITK\Modules\ThirdParty\VNL\src\vxl\core\vnl/algo/vnl_svd.hxx: suspicious return value (3) from SVDC<br>
[CRITICAL][Stream] 11.03.2020 10:16:04 [] (unknown:0) - D:\D\S\Slicer-4102-build\ITK\Modules\ThirdParty\VNL\src\vxl\core\vnl/algo/vnl_svd.hxx: M is 3x3<br>
[CRITICAL][Stream] 11.03.2020 10:16:04 [] (unknown:0) - M = [ …<br>
[CRITICAL][Stream] 11.03.2020 10:16:04 [] (unknown:0) -  0.0000000000000             -nan                0<br>
[CRITICAL][Stream] 11.03.2020 10:16:04 [] (unknown:0) -                0             -nan                0<br>
[CRITICAL][Stream] 11.03.2020 10:16:04 [] (unknown:0) -                0             -nan  0.0000000000000  ]<br>
[ERROR][VTK] 11.03.2020 10:16:04 [vtkITKArchetypeImageSeriesScalarReader (000002BF40C23A40)] (D:\D\S\Slicer-4102\Libs\vtkITK\vtkITKArchetypeImageSeriesScalarReader.cxx:230) - UpdateFromFile: Unsupported number of components (only 1 allowed): 3<br>
[CRITICAL][Stream] 11.03.2020 10:16:04 [] (unknown:0) - Could not read scalar volume using DCMTK approach.  Error is: FileFormatError<br>
[CRITICAL][Stream] 11.03.2020 10:16:04 [] (unknown:0) - Failed to read a multivolume: ‘NoneType’ object has no attribute ‘GetImageData’<br>
[CRITICAL][Stream] 11.03.2020 10:16:04 [] (unknown:0) - Traceback (most recent call last):<br>
[CRITICAL][Stream] 11.03.2020 10:16:04 [] (unknown:0) -   File “C:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py”, line 619, in load<br>
[CRITICAL][Stream] 11.03.2020 10:16:04 [] (unknown:0) -     if frame.GetImageData() == None:<br>
[CRITICAL][Stream] 11.03.2020 10:16:04 [] (unknown:0) - AttributeError: ‘NoneType’ object has no attribute ‘GetImageData’<br>
[CRITICAL][Stream] 11.03.2020 10:16:04 [] (unknown:0) -<br>
[CRITICAL][Stream] 11.03.2020 10:16:04 [] (unknown:0) - Could not load:  - as a 22 frames MultiVolume by ImagePositionPatient+AcquisitionTime as a MultiVolume</p>

---
