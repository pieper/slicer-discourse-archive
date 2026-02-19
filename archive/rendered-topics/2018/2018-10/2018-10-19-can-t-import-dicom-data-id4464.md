---
topic_id: 4464
title: "Can T Import Dicom Data"
date: 2018-10-19
url: https://discourse.slicer.org/t/4464
---

# Can`t import DICOM data

**Topic ID**: 4464
**Date**: 2018-10-19
**URL**: https://discourse.slicer.org/t/can-t-import-dicom-data/4464

---

## Post #1 by @hide (2018-10-19 14:08 UTC)

<p>Operating system:windows10<br>
Slicer version:slicer 4.7.0-2017-08-07</p>
<p>i have a problem with load of DICOM datas.<br>
i can`t import DICOM data into 3D slicer with error message.</p>
<p>i tried to use DICOM pacher, but failing.</p>
<p>have no way to import DICOM datas.<br>
please help.</p>

---

## Post #2 by @lassoan (2018-10-19 14:13 UTC)

<p>Please use latest nightly Slicer version and send the application log.</p>

---

## Post #3 by @hide (2018-10-19 14:32 UTC)

<p>i  attach bug log below.</p>
<p>DEBUG][Qt] 19.10.2018 23:16:26 [] (unknown:0) - Session start time …: 2018-10-19 23:16:26<br>
[DEBUG][Qt] 19.10.2018 23:16:26 [] (unknown:0) - Slicer version …: 4.7.0-2017-08-07 (revision 26212) win-amd64 - installed<br>
[DEBUG][Qt] 19.10.2018 23:16:26 [] (unknown:0) - Operating system …: Windows /  Professional /  (Build 9200) - 64-bit<br>
[DEBUG][Qt] 19.10.2018 23:16:26 [] (unknown:0) - Memory …: 16309 MB physical, 18741 MB virtual<br>
[DEBUG][Qt] 19.10.2018 23:16:26 [] (unknown:0) - CPU …: GenuineIntel , 4 cores, 16 logical processors<br>
[DEBUG][Qt] 19.10.2018 23:16:26 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 19.10.2018 23:16:26 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 19.10.2018 23:16:26 [] (unknown:0) - Additional module paths …: (none)<br>
[DEBUG][Python] 19.10.2018 23:16:27 [Python] (C:\Program Files\Slicer 4.7.0-2017-08-07\lib\Slicer-4.7\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 19.10.2018 23:16:28 [Python] (C:\Program Files\Slicer 4.7.0-2017-08-07\lib\Slicer-4.7\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 19.10.2018 23:16:28 [Python] (C:\Program Files\Slicer 4.7.0-2017-08-07\lib\Slicer-4.7\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 19.10.2018 23:16:26 [] (unknown:0) - Number of registered modules: 135<br>
[DEBUG][Qt] 19.10.2018 23:16:27 [] (unknown:0) - Number of instantiated modules: 135<br>
[DEBUG][Qt] 19.10.2018 23:16:28 [] (unknown:0) - Number of loaded modules: 135<br>
[DEBUG][Qt] 19.10.2018 23:16:28 [] (unknown:0) - Switch to module:  “Welcome”<br>
[DEBUG][Qt] 19.10.2018 23:16:46 [] (unknown:0) - Switch to module:  “DICOM”<br>
[DEBUG][Qt] 19.10.2018 23:16:47 [] (unknown:0) - Could not load  “C:/Users/kiyom/OneDrive/?h?L???g/SlicerDICOMDatabase/dicom/1.3.12.2.1107.5.1.4.50155.30000016022606012550000000004/1.3.12.2.1107.5.1.4.50155.30000016022606211407800002769/1.3.12.2.1107.5.1.4.50155.30000016022606211407800002770”<br>
DCMTK says:  Invalid argument<br>
[DEBUG][Qt] 19.10.2018 23:16:47 [] (unknown:0) - Could not load  “C:/Users/kiyom/OneDrive/?h?L???g/SlicerDICOMDatabase/dicom/1.3.12.2.1107.5.1.4.50155.30000016022606012550000000004/1.3.12.2.1107.5.1.4.50155.30000016022606211407800002769/1.3.12.2.1107.5.1.4.50155.30000016022606211407800002770”<br>
DCMTK says:  Invalid argument<br>
[DEBUG][Qt] 19.10.2018 23:17:09 [] (unknown:0) - Could not load  “C:/Users/kiyom/OneDrive/?h?L???g/SlicerDICOMDatabase/dicom/1.3.12.2.1107.5.1.4.50155.30000016022606012550000000004/1.3.12.2.1107.5.1.4.50155.30000016022606211407800002769/1.3.12.2.1107.5.1.4.50155.30000016022606211407800002770”<br>
DCMTK says:  Invalid argument<br>
[DEBUG][Qt] 19.10.2018 23:17:09 [] (unknown:0) - Could not load  “C:/Users/kiyom/OneDrive/?h?L???g/SlicerDICOMDatabase/dicom/1.3.12.2.1107.5.1.4.50155.30000016022606012550000000004/1.3.12.2.1107.5.1.4.50155.30000016022606211407800002769/1.3.12.2.1107.5.1.4.50155.30000016022606211407800002770”<br>
DCMTK says:  Invalid argument<br>
[DEBUG][Qt] 19.10.2018 23:17:09 [] (unknown:0) - Could not load  “C:/Users/kiyom/OneDrive/?h?L???g/SlicerDICOMDatabase/dicom/1.3.12.2.1107.5.1.4.50155.30000016022606012550000000004/1.3.12.2.1107.5.1.4.50155.30000016022606211407800002769/1.3.12.2.1107.5.1.4.50155.30000016022606211407800002770”<br>
DCMTK says:  Invalid argument<br>
[DEBUG][Qt] 19.10.2018 23:17:09 [] (unknown:0) - Could not load  “C:/Users/kiyom/OneDrive/?h?L???g/SlicerDICOMDatabase/dicom/1.3.12.2.1107.5.1.4.50155.30000016022606012550000000004/1.3.12.2.1107.5.1.4.50155.30000016022606211407800002769/1.3.12.2.1107.5.1.4.50155.30000016022606211407800002770”<br>
DCMTK says:  Invalid argument<br>
[DEBUG][Qt] 19.10.2018 23:17:09 [] (unknown:0) - Could not load  “C:/Users/kiyom/OneDrive/?h?L???g/SlicerDICOMDatabase/dicom/1.3.12.2.1107.5.1.4.50155.30000016022606012550000000004/1.3.12.2.1107.5.1.4.50155.30000016022606211407800002769/1.3.12.2.1107.5.1.4.50155.30000016022606211407800002770”<br>
DCMTK says:  Invalid argument<br>
[DEBUG][Qt] 19.10.2018 23:17:09 [] (unknown:0) - Could not load  “C:/Users/kiyom/OneDrive/?h?L???g/SlicerDICOMDatabase/dicom/1.3.12.2.1107.5.1.4.50155.30000016022606012550000000004/1.3.12.2.1107.5.1.4.50155.30000016022606211407800002769/1.3.12.2.1107.5.1.4.50155.30000016022606211407800002770”<br>
DCMTK says:  Invalid argument<br>
[DEBUG][Qt] 19.10.2018 23:17:09 [] (unknown:0) - Could not load  “C:/Users/kiyom/OneDrive/?h?L???g/SlicerDICOMDatabase/dicom/1.3.12.2.1107.5.1.4.50155.30000016022606012550000000004/1.3.12.2.1107.5.1.4.50155.30000016022606211407800002769/1.3.12.2.1107.5.1.4.50155.30000016022606211407800002770”<br>
DCMTK says:  Invalid argument<br>
[DEBUG][Qt] 19.10.2018 23:17:09 [] (unknown:0) - Could not load  “C:/Users/kiyom/OneDrive/?h?L???g/SlicerDICOMDatabase/dicom/1.3.12.2.1107.5.1.4.50155.30000016022606012550000000004/1.3.12.2.1107.5.1.4.50155.30000016022606211407800002769/1.3.12.2.1107.5.1.4.50155.30000016022606211407800002770”<br>
DCMTK says:  Invalid argument<br>
[DEBUG][Python] 19.10.2018 23:17:09 [Python] (C:/Program Files/Slicer 4.7.0-2017-08-07/lib/Slicer-4.7/qt-scripted-modules/MultiVolumeImporterPlugin.py:392) - MultiVolumeImportPlugin::examine<br>
[WARNING][Python] 19.10.2018 23:17:09 [Python] (C:\Program Files\Slicer 4.7.0-2017-08-07\bin\Python\slicer\util.py:862) - Warning: Plugin failed: MultiVolumeImporterPlugin</p>
<p>See python console for error message.<br>
[DEBUG][Qt] 19.10.2018 23:17:09 [] (unknown:0) - Could not load  “C:/Users/kiyom/OneDrive/?h?L???g/SlicerDICOMDatabase/dicom/1.3.12.2.1107.5.1.4.50155.30000016022606012550000000004/1.3.12.2.1107.5.1.4.50155.30000016022606211407800002769/1.3.12.2.1107.5.1.4.50155.30000016022606211407800002770”<br>
DCMTK says:  Invalid argument<br>
[DEBUG][Qt] 19.10.2018 23:17:09 [] (unknown:0) - Could not load  “C:/Users/kiyom/OneDrive/?h?L???g/SlicerDICOMDatabase/dicom/1.3.12.2.1107.5.1.4.50155.30000016022606012550000000004/1.3.12.2.1107.5.1.4.50155.30000016022606211407800002769/1.3.12.2.1107.5.1.4.50155.30000016022606211407800002770”<br>
DCMTK says:  Invalid argument<br>
[DEBUG][Qt] 19.10.2018 23:17:09 [] (unknown:0) - Could not load  “C:/Users/kiyom/OneDrive/?h?L???g/SlicerDICOMDatabase/dicom/1.3.12.2.1107.5.1.4.50155.30000016022606012550000000004/1.3.12.2.1107.5.1.4.50155.30000016022606211407800002769/1.3.12.2.1107.5.1.4.50155.30000016022606211407800002770”<br>
DCMTK says:  Invalid argument<br>
[DEBUG][Qt] 19.10.2018 23:17:09 [] (unknown:0) - Could not load  “C:/Users/kiyom/OneDrive/?h?L???g/SlicerDICOMDatabase/dicom/1.3.12.2.1107.5.1.4.50155.30000016022606012550000000004/1.3.12.2.1107.5.1.4.50155.30000016022606211407800002769/1.3.12.2.1107.5.1.4.50155.30000016022606211407800002770”<br>
DCMTK says:  Invalid argument<br>
[DEBUG][Qt] 19.10.2018 23:17:09 [] (unknown:0) - Could not load  “C:/Users/kiyom/OneDrive/?h?L???g/SlicerDICOMDatabase/dicom/1.3.12.2.1107.5.1.4.50155.30000016022606012550000000004/1.3.12.2.1107.5.1.4.50155.30000016022606211407800002769/1.3.12.2.1107.5.1.4.50155.30000016022606211407800002770”<br>
DCMTK says:  Invalid argument<br>
[CRITICAL][Stream] 19.10.2018 23:17:09 [] (unknown:0) - Traceback (most recent call last):<br>
[CRITICAL][Stream] 19.10.2018 23:17:09 [] (unknown:0) -   File “C:\Program Files\Slicer 4.7.0-2017-08-07\lib\Slicer-4.7\qt-scripted-modules\DICOMLib\DICOMWidgets.py”, line 708, in getLoadablesFromFileLists<br>
[CRITICAL][Stream] 19.10.2018 23:17:09 [] (unknown:0) -     loadablesByPlugin[plugin] = plugin.examine(fileLists)<br>
[CRITICAL][Stream] 19.10.2018 23:17:09 [] (unknown:0) -   File “C:/Program Files/Slicer 4.7.0-2017-08-07/lib/Slicer-4.7/qt-scripted-modules/MultiVolumeImporterPlugin.py”, line 80, in examine<br>
[CRITICAL][Stream] 19.10.2018 23:17:09 [] (unknown:0) -     loadables += self.examineFiles(files)<br>
[CRITICAL][Stream] 19.10.2018 23:17:09 [] (unknown:0) -   File “C:/Program Files/Slicer 4.7.0-2017-08-07/lib/Slicer-4.7/qt-scripted-modules/MultiVolumeImporterPlugin.py”, line 430, in examineFiles<br>
[CRITICAL][Stream] 19.10.2018 23:17:09 [] (unknown:0) -     mvNodes = self.initMultiVolumes(subseriesLists[key])<br>
[CRITICAL][Stream] 19.10.2018 23:17:09 [] (unknown:0) -   File “C:/Program Files/Slicer 4.7.0-2017-08-07/lib/Slicer-4.7/qt-scripted-modules/MultiVolumeImporterPlugin.py”, line 644, in initMultiVolumes<br>
[CRITICAL][Stream] 19.10.2018 23:17:09 [] (unknown:0) -     tagValue = self.tm2ms(tagValueStr) # convert to ms<br>
[CRITICAL][Stream] 19.10.2018 23:17:09 [] (unknown:0) -   File “C:/Program Files/Slicer 4.7.0-2017-08-07/lib/Slicer-4.7/qt-scripted-modules/MultiVolumeImporterPlugin.py”, line 613, in tm2ms<br>
[CRITICAL][Stream] 19.10.2018 23:17:09 [] (unknown:0) -     sec = sec+ssfrac<br>
[CRITICAL][Stream] 19.10.2018 23:17:09 [] (unknown:0) - UnboundLocalError: local variable ‘sec’ referenced before assignment<br>
[CRITICAL][Stream] 19.10.2018 23:17:09 [] (unknown:0) - Warning: Plugin failed: MultiVolumeImporterPlugin<br>
[CRITICAL][Stream] 19.10.2018 23:17:09 [] (unknown:0) -<br>
[CRITICAL][Stream] 19.10.2018 23:17:09 [] (unknown:0) - See python console for error message.<br>
[INFO][Stream] 19.10.2018 23:17:11 [] (unknown:0) - DICOM Plugin failed: local variable ‘sec’ referenced before assignment<br>
[DEBUG][Qt] 19.10.2018 23:17:11 [] (unknown:0) - Could not load  “C:/Users/kiyom/OneDrive/?h?L???g/SlicerDICOMDatabase/dicom/1.3.12.2.1107.5.1.4.50155.30000016022606012550000000004/1.3.12.2.1107.5.1.4.50155.30000016022606211407800002769/1.3.12.2.1107.5.1.4.50155.30000016022606211407800002770”<br>
DCMTK says:  Invalid argument<br>
[WARNING][Python] 19.10.2018 23:17:12 [Python] (C:\Program Files\Slicer 4.7.0-2017-08-07\bin\Python\slicer\util.py:862) -<br>
Could not load: Unknown - as Slicer Scene as a Slicer Data Bundle<br>
[DEBUG][Qt] 19.10.2018 23:17:11 [] (unknown:0) - Could not load  “C:/Users/kiyom/OneDrive/?h?L???g/SlicerDICOMDatabase/dicom/1.3.12.2.1107.5.1.4.50155.30000016022606012550000000004/1.3.12.2.1107.5.1.4.50155.30000016022606211407800002769/1.3.12.2.1107.5.1.4.50155.30000016022606211407800002770”<br>
DCMTK says:  Invalid argument<br>
[INFO][Stream] 19.10.2018 23:17:12 [] (unknown:0) - Could not get zipSize for C:/Users/kiyom/OneDrive/?h?L???g/SlicerDICOMDatabase/dicom/1.3.12.2.1107.5.1.4.50155.30000016022606012550000000004/1.3.12.2.1107.5.1.4.50155.30000016022606211407800002769/1.3.12.2.1107.5.1.4.50155.30000016022606211407800002770<br>
[CRITICAL][Stream] 19.10.2018 23:17:12 [] (unknown:0) -<br>
[CRITICAL][Stream] 19.10.2018 23:17:12 [] (unknown:0) - Could not load: Unknown - as Slicer Scene as a Slicer Data Bundle<br>
[DEBUG][Qt] 19.10.2018 23:17:27 [] (unknown:0) - SQLITE: removing seriesInstanceUID 1.3.12.2.1107.5.1.4.50155.30000016022606211407800002769<br>
[WARNING][Qt] 19.10.2018 23:17:27 [] (unknown:0) - Failed to remove file C:/Users/kiyom/OneDrive/?h?L???g/SlicerDICOMDatabase/dicom/1.3.12.2.1107.5.1.4.50155.30000016022606012550000000004/1.3.12.2.1107.5.1.4.50155.30000016022606211407800002769/1.3.12.2.1107.5.1.4.50155.30000016022606211407800002770<br>
[WARNING][Qt] 19.10.2018 23:17:27 [] (unknown:0) - Failed to remove thumbnail C:/Users/kiyom/OneDrive/?h?L???g/SlicerDICOMDatabase/thumbs/1.3.12.2.1107.5.1.4.50155.30000016022606012550000000004/1.3.12.2.1107.5.1.4.50155.30000016022606211407800002769/1.3.12.2.1107.5.1.4.50155.30000016022606211407800002770.png<br>
[WARNING][Qt] 19.10.2018 23:17:33 [] (unknown:0) - Ignoring destinationDirectoryName parameter, just taking it as indication we should copy!<br>
[DEBUG][Qt] 19.10.2018 23:17:33 [] (unknown:0) - Indexing</p>
<p>“C:/Users/kiyom/C/2016.12.6/supine/CT1”<br>
[DEBUG][Qt] 19.10.2018 23:17:33 [] (unknown:0) - Processing C:/Users/kiyom/C/2016.12.6/supine/CT1<br>
[DEBUG][Qt] 19.10.2018 23:17:33 [] (unknown:0) - inserting filePath:  “C:/Users/kiyom/C/2016.12.6/supine/CT1”<br>
[DEBUG][Qt] 19.10.2018 23:17:33 [] (unknown:0) - Copy file from: C:/Users/kiyom/C/2016.12.6/supine/CT1<br>
[DEBUG][Qt] 19.10.2018 23:17:33 [] (unknown:0) - Copy file to  : C:/Users/kiyom/OneDrive/?h?L???g/SlicerDICOMDatabase/dicom/1.3.12.2.1107.5.1.4.50155.30000016120603500467100000001/1.3.12.2.1107.5.1.4.50155.30000016120604083659300004022/1.2.392.200036.9107.630.491.20161207.160604.10004004953<br>
[DEBUG][Qt] 19.10.2018 23:17:33 [] (unknown:0) - This looks like a different patient from last insert:  “002-002”<br>
[DEBUG][Qt] 19.10.2018 23:17:33 [] (unknown:0) - New patient inserted: 5<br>
[DEBUG][Qt] 19.10.2018 23:17:33 [] (unknown:0) - New patient inserted as :  5<br>
[DEBUG][Qt] 19.10.2018 23:17:33 [] (unknown:0) - Going to insert this instance with dbPatientID:  5<br>
[DEBUG][Qt] 19.10.2018 23:17:33 [] (unknown:0) - Used existing study:  “1.3.12.2.1107.5.1.4.50155.30000016120603500467100000001”<br>
[DEBUG][Qt] 19.10.2018 23:17:33 [] (unknown:0) - Study Added<br>
[WARNING][Qt] 19.10.2018 23:17:33 [] (unknown:0) - Statement: SELECT * FROM Series WHERE SeriesInstanceUID = ?<br>
[DEBUG][Qt] 19.10.2018 23:17:33 [] (unknown:0) - Used existing series:  “1.3.12.2.1107.5.1.4.50155.30000016120604083659300004022”<br>
[DEBUG][Qt] 19.10.2018 23:17:33 [] (unknown:0) - Series Added<br>
[DEBUG][Qt] 19.10.2018 23:17:33 [] (unknown:0) - Maybe add Instance<br>
[DEBUG][Qt] 19.10.2018 23:17:33 [] (unknown:0) - Could not load  “C:/Users/kiyom/OneDrive/?h?L???g/SlicerDICOMDatabase/dicom/1.3.12.2.1107.5.1.4.50155.30000016120603500467100000001/1.3.12.2.1107.5.1.4.50155.30000016120604083659300004022/1.2.392.200036.9107.630.491.20161207.160604.10004004953”<br>
DCMTK says:  Invalid argument<br>
[CRITICAL][Qt] 19.10.2018 23:17:33 [] (unknown:0) - "Slicer has caught an internal error.</p>
<p>You may be able to continue from this point, but results are undefined.</p>
<p>Suggested action is to save your work and restart.</p>
<p>If you have a repeatable sequence of steps that causes this message, please report the issue following instructions available at <a href="http://slicer.org" rel="nofollow noopener">http://slicer.org</a></p>
<p>The message detail is:</p>
<p>Exception thrown in event: Calling methods on uninitialized ctkDICOMItem"<br>
[INFO][Python] 19.10.2018 23:17:37 [Python] (C:\Program Files\Slicer 4.7.0-2017-08-07\lib\Slicer-4.7\qt-scripted-modules\DICOMLib\DICOMWidgets.py:455) - Imported a DICOM directory, checking for extensions<br>
[INFO][Stream] 19.10.2018 23:17:37 [] (unknown:0) - C:/Users/kiyom/C/2016.12.6/supine/CT1Imported a DICOM directory, checking for extensions<br>
[WARNING][Qt] 19.10.2018 23:17:46 [] (unknown:0) - libpng warning: iCCP: known incorrect sRGB profile<br>
[WARNING][Qt] 19.10.2018 23:17:46 [] (unknown:0) - libpng warning: iCCP: known incorrect sRGB profile<br>
[DEBUG][Qt] 19.10.2018 23:17:48 [] (unknown:0) - Switch to module:  “DICOMPatcher”<br>
[INFO][Python] 19.10.2018 23:18:12 [Python] (C:/Program Files/Slicer 4.7.0-2017-08-07/lib/Slicer-4.7/qt-scripted-modules/DICOMPatcher.py:502) - DICOM patching started…<br>
[INFO][Stream] 19.10.2018 23:18:12 [] (unknown:0) - DICOM patching started…<br>
[DEBUG][Python] 19.10.2018 23:18:12 [Python] (C:/Program Files/Slicer 4.7.0-2017-08-07/lib/Slicer-4.7/qt-scripted-modules/DICOMPatcher.py:525) - DICOM patch input directory: C:/Users/kiyom/C/2016.12.6/supine<br>
[DEBUG][Python] 19.10.2018 23:18:12 [Python] (C:/Program Files/Slicer 4.7.0-2017-08-07/lib/Slicer-4.7/qt-scripted-modules/DICOMPatcher.py:526) - DICOM patch output directory: C:/Users/kiyom/C/2016.12.6/NEW1<br>
[INFO][Python] 19.10.2018 23:18:12 [Python] (C:/Program Files/Slicer 4.7.0-2017-08-07/lib/Slicer-4.7/qt-scripted-modules/DICOMPatcher.py:502) - Examining .\CT1…<br>
[INFO][Stream] 19.10.2018 23:18:12 [] (unknown:0) - Examining .\CT1…<br>
[INFO][Python] 19.10.2018 23:18:12 [Python] (C:/Program Files/Slicer 4.7.0-2017-08-07/lib/Slicer-4.7/qt-scripted-modules/DICOMPatcher.py:502) -   Patching…<br>
[INFO][Stream] 19.10.2018 23:18:12 [] (unknown:0) -   Patching…<br>
[INFO][Python] 19.10.2018 23:18:12 [Python] (C:/Program Files/Slicer 4.7.0-2017-08-07/lib/Slicer-4.7/qt-scripted-modules/DICOMPatcher.py:502) -   Writing DICOM…<br>
[INFO][Stream] 19.10.2018 23:18:12 [] (unknown:0) -   Writing DICOM…<br>
[INFO][Python] 19.10.2018 23:18:12 [Python] (C:/Program Files/Slicer 4.7.0-2017-08-07/lib/Slicer-4.7/qt-scripted-modules/DICOMPatcher.py:502) -   Created DICOM file: C:/Users/kiyom/C/2016.12.6/NEW1/pa000/st000/se000/ct000.dcm<br>
[INFO][Stream] 19.10.2018 23:18:12 [] (unknown:0) -   Created DICOM file: C:/Users/kiyom/C/2016.12.6/NEW1/pa000/st000/se000/ct000.dcm<br>
[INFO][Python] 19.10.2018 23:18:12 [Python] (C:/Program Files/Slicer 4.7.0-2017-08-07/lib/Slicer-4.7/qt-scripted-modules/DICOMPatcher.py:502) - Examining .\CT10…<br>
[INFO][Stream] 19.10.2018 23:18:12 [] (unknown:0) - Examining .\CT10…<br>
[INFO][Python] 19.10.2018 23:18:12 [Python] (C:/Program Files/Slicer 4.7.0-2017-08-07/lib/Slicer-4.7/qt-scripted-modules/DICOMPatcher.py:502) -   Patching…<br>
[INFO][Stream] 19.10.2018 23:18:12 [] (unknown:0) -   Patching…<br>
[INFO][Python] 19.10.2018 23:18:12 [Python] (C:/Program Files/Slicer 4.7.0-2017-08-07/lib/Slicer-4.7/qt-scripted-modules/DICOMPatcher.py:502) -   Writing DICOM…<br>
[INFO][Stream] 19.10.2018 23:18:12 [] (unknown:0) -   Writing DICOM…<br>
[INFO][Python] 19.10.2018 23:18:12 [Python] (C:/Program Files/Slicer 4.7.0-2017-08-07/lib/Slicer-4.7/qt-scripted-modules/DICOMPatcher.py:502) -   Created DICOM file: C:/Users/kiyom/C/2016.12.6/NEW1/pa000/st000/se000/ct001.dcm<br>
[INFO][Stream] 19.10.2018 23:18:12 [] (unknown:0) -   Created DICOM file: C:/Users/kiyom/C/2016.12.6/NEW1/pa000/st000/se000/ct001.dcm<br>
[INFO][Python] 19.10.2018 23:18:12 [Python] (C:/Program Files/Slicer 4.7.0-2017-08-07/lib/Slicer-4.7/qt-scripted-modules/DICOMPatcher.py:502) - Examining .\CT100…<br>
[INFO][Stream] 19.10.2018 23:18:12 [] (unknown:0) - Examining .\CT100…<br>
[INFO][Python] 19.10.2018 23:18:12 [Python] (C:/Program Files/Slicer 4.7.0-2017-08-07/lib/Slicer-4.7/qt-scripted-modules/DICOMPatcher.py:502) -   Patching…<br>
[INFO][Stream] 19.10.2018 23:18:12 [] (unknown:0) -   Patching…<br>
[INFO][Python] 19.10.2018 23:18:12 [Python] (C:/Program Files/Slicer 4.7.0-2017-08-07/lib/Slicer-4.7/qt-scripted-modules/DICOMPatcher.py:502) -   Writing DICOM…<br>
[INFO][Stream] 19.10.2018 23:18:12 [] (unknown:0) -   Writing DICOM…<br>
[INFO][Python] 19.10.2018 23:18:12 [Python] (C:/Program Files/Slicer 4.7.0-2017-08-07/lib/Slicer-4.7/qt-scripted-modules/DICOMPatcher.py:502) -   Created DICOM file: C:/Users/kiyom/C/2016.12.6/NEW1/pa000/st000/se000/ct002.dcm<br>
[INFO][Stream] 19.10.2018 23:18:12 [] (unknown:0) -   Created DICOM file: C:/Users/kiyom/C/2016.12.6/NEW1/pa000/st000/se000/ct002.dcm<br>
[INFO][Python] 19.10.2018 23:18:12 [Python] (C:/Program Files/Slicer 4.7.0-2017-08-07/lib/Slicer-4.7/qt-scripted-modules/DICOMPatcher.py:502) - Examining .\CT101…<br>
[INFO][Stream] 19.10.2018 23:18:12 [] (unknown:0) - Examining .\CT101…<br>
[INFO][Python] 19.10.2018 23:18:12 [Python] (C:/Program Files/Slicer 4.7.0-2017-08-07/lib/Slicer-4.7/qt-scripted-modules/DICOMPatcher.py:502) -   Patching…<br>
[INFO][Stream] 19.10.2018 23:18:12 [] (unknown:0) -   Patching…<br>
[INFO][Python] 19.10.2018 23:18:12 [Python] (C:/Program Files/Slicer 4.7.0-2017-08-07/lib/Slicer-4.7/qt-scripted-modules/DICOMPatcher.py:502) -   Writing DICOM…<br>
[INFO][Stream] 19.10.2018 23:18:12 [] (unknown:0) -   Writing DICOM…<br>
[INFO][Python] 19.10.2018 23:18:12 [Python] (C:/Program Files/Slicer 4.7.0-2017-08-07/lib/Slicer-4.7/qt-scripted-modules/DICOMPatcher.py:502) -   Created DICOM file: C:/Users/kiyom/C/2016.12.6/NEW1/pa000/st000/se000/ct003.dcm</p>
<p>too long bug log to attach, so attached only a portion of all.</p>

---

## Post #4 by @hide (2018-10-19 14:42 UTC)

<p>i attach the end of bug log.</p>
<p>“C:/Users/kiyom/C/2016.12.6/NEW1/pa000/st000/se000/ct000.dcm”<br>
[DEBUG][Qt] 19.10.2018 23:18:30 [] (unknown:0) - Processing C:/Users/kiyom/C/2016.12.6/NEW1/pa000/st000/se000/ct000.dcm<br>
[WARNING][Qt] 19.10.2018 23:18:30 [] (unknown:0) - QSqlQuery::value: not positioned on a valid record<br>
[WARNING][Qt] 19.10.2018 23:18:30 [] (unknown:0) - QSqlQuery::value: not positioned on a valid record<br>
[DEBUG][Qt] 19.10.2018 23:18:30 [] (unknown:0) - inserting filePath:  “C:/Users/kiyom/C/2016.12.6/NEW1/pa000/st000/se000/ct000.dcm”<br>
[DEBUG][Qt] 19.10.2018 23:18:30 [] (unknown:0) - database filename for  “2.25.276038533200814578284225619608846648424”  is empty - we should insert on top of it<br>
[DEBUG][Qt] 19.10.2018 23:18:30 [] (unknown:0) - Copy file from: C:/Users/kiyom/C/2016.12.6/NEW1/pa000/st000/se000/ct000.dcm<br>
[DEBUG][Qt] 19.10.2018 23:18:30 [] (unknown:0) - Copy file to  : C:/Users/kiyom/OneDrive/?h?L???g/SlicerDICOMDatabase/dicom/1.3.12.2.1107.5.1.4.50155.30000016120603500467100000001/1.3.12.2.1107.5.1.4.50155.30000016120604083659300004022/2.25.276038533200814578284225619608846648424<br>
[DEBUG][Qt] 19.10.2018 23:18:30 [] (unknown:0) - Going to insert this instance with dbPatientID:  5<br>
[DEBUG][Qt] 19.10.2018 23:18:30 [] (unknown:0) - Used existing study:  “1.3.12.2.1107.5.1.4.50155.30000016120603500467100000001”<br>
[DEBUG][Qt] 19.10.2018 23:18:30 [] (unknown:0) - Study Added<br>
[WARNING][Qt] 19.10.2018 23:18:30 [] (unknown:0) - Statement: SELECT * FROM Series WHERE SeriesInstanceUID = ?<br>
[DEBUG][Qt] 19.10.2018 23:18:30 [] (unknown:0) - Used existing series:  “1.3.12.2.1107.5.1.4.50155.30000016120604083659300004022”<br>
[DEBUG][Qt] 19.10.2018 23:18:30 [] (unknown:0) - Series Added<br>
[DEBUG][Qt] 19.10.2018 23:18:30 [] (unknown:0) - Maybe add Instance<br>
[DEBUG][Qt] 19.10.2018 23:18:30 [] (unknown:0) - Could not load  “C:/Users/kiyom/OneDrive/?h?L???g/SlicerDICOMDatabase/dicom/1.3.12.2.1107.5.1.4.50155.30000016120603500467100000001/1.3.12.2.1107.5.1.4.50155.30000016120604083659300004022/2.25.276038533200814578284225619608846648424”<br>
DCMTK says:  Invalid argument<br>
[CRITICAL][Qt] 19.10.2018 23:18:30 [] (unknown:0) - "Slicer has caught an internal error.</p>
<p>You may be able to continue from this point, but results are undefined.</p>
<p>Suggested action is to save your work and restart.</p>
<p>If you have a repeatable sequence of steps that causes this message, please report the issue following instructions available at <a href="http://slicer.org" rel="nofollow noopener">http://slicer.org</a></p>
<p>The message detail is:</p>
<p>Exception thrown in event: Calling methods on uninitialized ctkDICOMItem"<br>
[INFO][Python] 19.10.2018 23:18:33 [Python] (C:\Program Files\Slicer 4.7.0-2017-08-07\lib\Slicer-4.7\qt-scripted-modules\DICOMLib\DICOMWidgets.py:455) - Imported a DICOM directory, checking for extensions<br>
[INFO][Stream] 19.10.2018 23:18:33 [] (unknown:0) - C:/Users/kiyom/C/2016.12.6/NEW1/pa000/st000/se000/ct000.dcmImported a DICOM directory, checking for extensions</p>
<p>Do I need to uninstall 3D slicer that i now use, when i install the latest 3D slicer?</p>

---

## Post #5 by @pieper (2018-10-19 15:02 UTC)

<p>Looks like something to do with the data an not with Slicer so reinstalling is unlikely to make a difference.  Does it work for you try with other dicom data?</p>
<p>You should be able to load this sample data for example:</p>
<p><a href="https://s3.amazonaws.com/IsomicsPublic/SampleData/QIN-HEADNECK-01-0024-CT.zip" class="onebox" target="_blank">https://s3.amazonaws.com/IsomicsPublic/SampleData/QIN-HEADNECK-01-0024-CT.zip</a></p>

---

## Post #6 by @hide (2018-10-19 15:18 UTC)

<p>thanks a lot.<br>
tried to import your sample data, but failed.<br>
attach a bug log.<br>
You may be able to continue from this point, but results are undefined.</p>
<p>Suggested action is to save your work and restart.</p>
<p>If you have a repeatable sequence of steps that causes this message, please report the issue following instructions available at <a href="http://slicer.org" rel="nofollow noopener">http://slicer.org</a></p>
<p>The message detail is:</p>
<p>Exception thrown in event: Calling methods on uninitialized ctkDICOMItem"</p>
<p>[INFO][Python] 20.10.2018 00:14:31 [Python] (C:\Program Files\Slicer 4.7.0-2017-08-07\lib\Slicer-4.7\qt-scripted-modules\DICOMLib\DICOMWidgets.py:455) - Imported a DICOM directory, checking for extensions</p>
<p>[INFO][Stream] 20.10.2018 00:14:31 [] (unknown:0) - C:/Users/kiyom/C/QIN-HEADNECK-01-0024-CT/000000.dcmImported a DICOM directory, checking for extensions</p>
<p>[DEBUG][Qt] 20.10.2018 00:14:31 [] (unknown:0) - Could not load "C:/Users/kiyom/OneDrive/?h?L???g/SlicerDICOMDatabase/dicom/1.3.6.1.4.1.14519.5.2.1.2744.7002.271803936741289691489150315969/1.3.6.1.4.1.14519.5.2.1.2744.7002.453958960749354309542907936863/1.3.6.1.4.1.14519.5.2.1.2744.7002.115318280284078568523785104293"</p>
<p>DCMTK says: Invalid argument</p>
<p>[DEBUG][Qt] 20.10.2018 00:14:32 [] (unknown:0) - Could not load "C:/Users/kiyom/OneDrive/?h?L???g/SlicerDICOMDatabase/dicom/1.3.6.1.4.1.14519.5.2.1.2744.7002.271803936741289691489150315969/1.3.6.1.4.1.14519.5.2.1.2744.7002.453958960749354309542907936863/1.3.6.1.4.1.14519.5.2.1.2744.7002.115318280284078568523785104293"</p>
<p>DCMTK says: Invalid argument</p>
<p>i don`t know what is happening.</p>

---

## Post #7 by @pieper (2018-10-19 15:34 UTC)

<p>The problem is likely due to this:</p>
<p>“C:/Users/kiyom/OneDrive/?h?L???g/SlicerDICOMDatabase</p>
<p>Sorry, we don’t handle non-English characters well.  Please set your directory to point to an ascii-only path.</p>
<p>Hope that helps,<br>
Steve</p>

---

## Post #8 by @lassoan (2018-10-19 16:26 UTC)

<p>Also, please update to a more recent version of Slicer. Since version 4.7 we have implemented hundreds of fixes and improvements.</p>

---

## Post #9 by @hide (2018-10-19 16:37 UTC)

<p>thanks.<br>
i try.<br>
and do i need to uninstall Slicer version 4.7 when to install the latest Slicer?</p>

---

## Post #10 by @pieper (2018-10-20 01:47 UTC)

<aside class="quote no-group" data-username="hide" data-post="9" data-topic="4464">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/a4c791/48.png" class="avatar"> hide:</div>
<blockquote>
<p>and do i need to uninstall Slicer version 4.7 when to install the latest Slicer?</p>
</blockquote>
</aside>
<p>No need to uninstall the old version, you can have as many versions installed as you want and they won’t interfere.</p>

---
