# Problem in loading dicom ("Could NOT load image as Scalar Volume")

**Topic ID**: 9634
**Date**: 2019-12-28
**URL**: https://discourse.slicer.org/t/problem-in-loading-dicom-could-not-load-image-as-scalar-volume/9634

---

## Post #1 by @sam_javidi (2019-12-28 08:23 UTC)

<p>Hi<br>
I have a problem with loading Dicom MR images.<br>
Images are ‘RGB’ (true color), it is not loaded because of an error “Could NOT load image as Scalar Volume”. I am wondering if anyone knows how to solve this issue.</p>
<p>images are available at this link: <a href="https://1drv.ms/f/s!AqivmPTPK3iQ9zLtqBQoU216B0_w" rel="noopener nofollow ugc">link</a><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/5259f310e582c9adc7dfd36546fb7eafb267b647.jpeg" alt="err" data-base62-sha1="bKvRQhWyUlsN4SRwEzBdQYOOpCv" width="321" height="97"></p>
<p>Thanks</p>
<details>
<summary>
log file</summary>
<pre data-code-wrap="log"><code class="lang-plaintext">[DEBUG][Qt] 28.12.2019 11:24:44 [] (unknown:0) - Session start time .......: 2019-12-28 11:24:44
[DEBUG][Qt] 28.12.2019 11:24:44 [] (unknown:0) - Slicer version ...........: 4.10.2 (revision 28257) win-amd64 - installed release
[DEBUG][Qt] 28.12.2019 11:24:44 [] (unknown:0) - Operating system .........: Windows / 7 / Service Pack 1 (Build 7601) - 64-bit
[DEBUG][Qt] 28.12.2019 11:24:44 [] (unknown:0) - Memory ...................: 4028 MB physical, 15602 MB virtual
[DEBUG][Qt] 28.12.2019 11:24:44 [] (unknown:0) - CPU ......................: GenuineIntel , 4 cores, 4 logical processors
[DEBUG][Qt] 28.12.2019 11:24:44 [] (unknown:0) - VTK configuration ........: OpenGL2 rendering, TBB threading
[DEBUG][Qt] 28.12.2019 11:24:44 [] (unknown:0) - Developer mode enabled ...: no
[DEBUG][Qt] 28.12.2019 11:24:44 [] (unknown:0) - Prefer executable CLI ....: yes
[DEBUG][Qt] 28.12.2019 11:24:44 [] (unknown:0) - Additional module paths ..: (none)
[DEBUG][Python] 28.12.2019 11:24:46 [Python] (D:\PROGRAMfile\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations
[DEBUG][Python] 28.12.2019 11:24:47 [Python] (D:\PROGRAMfile\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 28.12.2019 11:24:47 [Python] (D:\PROGRAMfile\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Qt] 28.12.2019 11:24:47 [] (unknown:0) - Switch to module:  "Welcome"
[DEBUG][Qt] 28.12.2019 11:24:49 [] (unknown:0) - Switch to module:  "DICOM"
[DEBUG][Qt] 28.12.2019 11:25:09 [] (unknown:0) - New patient inserted: 21
[DEBUG][Qt] 28.12.2019 11:25:09 [] (unknown:0) - New patient inserted as :  21
[DEBUG][Qt] 28.12.2019 11:25:09 [] (unknown:0) - Need to insert new study:  "1.3.12.2.1107.5.2.43.66088.30000019031204544832400000013"
[DEBUG][Qt] 28.12.2019 11:25:09 [] (unknown:0) - Study Added
[DEBUG][Qt] 28.12.2019 11:25:09 [] (unknown:0) - Need to insert new series:  "1.3.12.2.1107.5.2.43.66088.201903121504271391151736.0.0.0"
[DEBUG][Qt] 28.12.2019 11:25:09 [] (unknown:0) - Series Added
[DEBUG][Qt] 28.12.2019 11:25:12 [] (unknown:0) - "DICOM indexer has successfully processed 176 files [2.96s]"
[INFO][Python] 28.12.2019 11:25:14 [Python] (D:\PROGRAMfile\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\DICOMLib\DICOMWidgets.py:471) - Imported a DICOM directory, checking for extensions
[INFO][Stream] 28.12.2019 11:25:14 [] (unknown:0) - Imported a DICOM directory, checking for extensions
[DEBUG][Python] 28.12.2019 11:25:29 [Python] (D:/PROGRAMfile/Slicer 4.10.2/bin/../lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:455) - MultiVolumeImportPlugin::examine
[DEBUG][Python] 28.12.2019 11:25:30 [Python] (D:/PROGRAMfile/Slicer 4.10.2/bin/../lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:495) - DICOMMultiVolumePlugin found 1 multivolumes!
[DEBUG][Python] 28.12.2019 11:25:30 [Python] (D:/PROGRAMfile/Slicer 4.10.2/bin/../lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:165) - MultiVolumeImportPlugin:examineMultiseries
[DEBUG][Python] 28.12.2019 11:25:31 [Python] (D:/PROGRAMfile/Slicer 4.10.2/bin/../lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:170) - DICOMMultiVolumePlugin found 0 multivolumes!
[INFO][Python] 28.12.2019 11:25:31 [Python] (D:/PROGRAMfile/Slicer 4.10.2/bin/../lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py:303) - Loading with imageIOName: GDCM
[ERROR][Python] 28.12.2019 11:25:31 [Python] (D:/PROGRAMfile/Slicer 4.10.2/bin/../lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py:309) - Could not read scalar volume using GDCM approach.  Error is: FileFormatError
[INFO][Python] 28.12.2019 11:25:31 [Python] (D:/PROGRAMfile/Slicer 4.10.2/bin/../lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py:303) - Loading with imageIOName: DCMTK
[ERROR][Python] 28.12.2019 11:25:32 [Python] (D:/PROGRAMfile/Slicer 4.10.2/bin/../lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py:309) - Could not read scalar volume using DCMTK approach.  Error is: FileFormatError
[WARNING][Python] 28.12.2019 11:25:32 [Python] (D:\PROGRAMfile\Slicer 4.10.2\bin\Python\slicer\util.py:1110) - 
Could not load: 5: t1_mprage_sag_p2 as a Scalar Volume
[INFO][Stream] 28.12.2019 11:25:31 [] (unknown:0) - Loading with imageIOName: GDCM
[ERROR][VTK] 28.12.2019 11:25:31 [vtkITKArchetypeImageSeriesScalarReader (0000000010ACEFE0)] (D:\D\S\Slicer-4102\Libs\vtkITK\vtkITKArchetypeImageSeriesScalarReader.cxx:257) - UpdateFromSeries: Unsupported number of components: 1 != 3
[CRITICAL][Stream] 28.12.2019 11:25:31 [] (unknown:0) - Could not read scalar volume using GDCM approach.  Error is: FileFormatError
[INFO][Stream] 28.12.2019 11:25:31 [] (unknown:0) - Loading with imageIOName: DCMTK
[ERROR][VTK] 28.12.2019 11:25:32 [vtkITKArchetypeImageSeriesScalarReader (0000000010ACF740)] (D:\D\S\Slicer-4102\Libs\vtkITK\vtkITKArchetypeImageSeriesScalarReader.cxx:257) - UpdateFromSeries: Unsupported number of components: 1 != 3
[CRITICAL][Stream] 28.12.2019 11:25:32 [] (unknown:0) - Could not read scalar volume using DCMTK approach.  Error is: FileFormatError
[CRITICAL][Stream] 28.12.2019 11:25:32 [] (unknown:0) -
[CRITICAL][Stream] 28.12.2019 11:25:32 [] (unknown:0) - Could not load: 5: t1_mprage_sag_p2 as a Scalar Volume
[DEBUG][Python] 28.12.2019 11:37:20 [Python] (D:/PROGRAMfile/Slicer 4.10.2/bin/../lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:455) - MultiVolumeImportPlugin::examine
[DEBUG][Python] 28.12.2019 11:37:21 [Python] (D:/PROGRAMfile/Slicer 4.10.2/bin/../lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:495) - DICOMMultiVolumePlugin found 1 multivolumes!
[DEBUG][Python] 28.12.2019 11:37:22 [Python] (D:/PROGRAMfile/Slicer 4.10.2/bin/../lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:165) - MultiVolumeImportPlugin:examineMultiseries
[DEBUG][Python] 28.12.2019 11:37:22 [Python] (D:/PROGRAMfile/Slicer 4.10.2/bin/../lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:170) - DICOMMultiVolumePlugin found 0 multivolumes!
[INFO][Python] 28.12.2019 11:37:22 [Python] (D:/PROGRAMfile/Slicer 4.10.2/bin/../lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py:303) - Loading with imageIOName: GDCM
[ERROR][Python] 28.12.2019 11:37:22 [Python] (D:/PROGRAMfile/Slicer 4.10.2/bin/../lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py:309) - Could not read scalar volume using GDCM approach.  Error is: FileFormatError
[INFO][Python] 28.12.2019 11:37:22 [Python] (D:/PROGRAMfile/Slicer 4.10.2/bin/../lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py:303) - Loading with imageIOName: DCMTK
[ERROR][Python] 28.12.2019 11:37:23 [Python] (D:/PROGRAMfile/Slicer 4.10.2/bin/../lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py:309) - Could not read scalar volume using DCMTK approach.  Error is: FileFormatError
[WARNING][Python] 28.12.2019 11:37:23 [Python] (D:\PROGRAMfile\Slicer 4.10.2\bin\Python\slicer\util.py:1110) - 
Could not load: 5: t1_mprage_sag_p2 as a Scalar Volume
[INFO][Stream] 28.12.2019 11:37:22 [] (unknown:0) - Loading with imageIOName: GDCM
[ERROR][VTK] 28.12.2019 11:37:22 [vtkITKArchetypeImageSeriesScalarReader (0000000010ACFAF0)] (D:\D\S\Slicer-4102\Libs\vtkITK\vtkITKArchetypeImageSeriesScalarReader.cxx:257) - UpdateFromSeries: Unsupported number of components: 1 != 3
[CRITICAL][Stream] 28.12.2019 11:37:22 [] (unknown:0) - Could not read scalar volume using GDCM approach.  Error is: FileFormatError
[INFO][Stream] 28.12.2019 11:37:22 [] (unknown:0) - Loading with imageIOName: DCMTK
[ERROR][VTK] 28.12.2019 11:37:23 [vtkITKArchetypeImageSeriesScalarReader (0000000010ACF740)] (D:\D\S\Slicer-4102\Libs\vtkITK\vtkITKArchetypeImageSeriesScalarReader.cxx:257) - UpdateFromSeries: Unsupported number of components: 1 != 3
[CRITICAL][Stream] 28.12.2019 11:37:23 [] (unknown:0) - Could not read scalar volume using DCMTK approach.  Error is: FileFormatError
[CRITICAL][Stream] 28.12.2019 11:37:23 [] (unknown:0) -
[CRITICAL][Stream] 28.12.2019 11:37:23 [] (unknown:0) - Could not load: 5: t1_mprage_sag_p2 as a Scalar Volume
[DEBUG][Python] 28.12.2019 11:42:09 [Python] (D:/PROGRAMfile/Slicer 4.10.2/bin/../lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:455) - MultiVolumeImportPlugin::examine
[DEBUG][Python] 28.12.2019 11:42:10 [Python] (D:/PROGRAMfile/Slicer 4.10.2/bin/../lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:495) - DICOMMultiVolumePlugin found 1 multivolumes!
[DEBUG][Python] 28.12.2019 11:42:11 [Python] (D:/PROGRAMfile/Slicer 4.10.2/bin/../lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:165) - MultiVolumeImportPlugin:examineMultiseries
[DEBUG][Python] 28.12.2019 11:42:11 [Python] (D:/PROGRAMfile/Slicer 4.10.2/bin/../lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:170) - DICOMMultiVolumePlugin found 0 multivolumes!
[INFO][Python] 28.12.2019 11:42:11 [Python] (D:/PROGRAMfile/Slicer 4.10.2/bin/../lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py:303) - Loading with imageIOName: GDCM
[ERROR][Python] 28.12.2019 11:42:11 [Python] (D:/PROGRAMfile/Slicer 4.10.2/bin/../lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py:309) - Could not read scalar volume using GDCM approach.  Error is: FileFormatError
[INFO][Python] 28.12.2019 11:42:11 [Python] (D:/PROGRAMfile/Slicer 4.10.2/bin/../lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py:303) - Loading with imageIOName: DCMTK
[ERROR][Python] 28.12.2019 11:42:12 [Python] (D:/PROGRAMfile/Slicer 4.10.2/bin/../lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py:309) - Could not read scalar volume using DCMTK approach.  Error is: FileFormatError
[WARNING][Python] 28.12.2019 11:42:12 [Python] (D:\PROGRAMfile\Slicer 4.10.2\bin\Python\slicer\util.py:1110) - 
Could not load: 5: t1_mprage_sag_p2 as a Scalar Volume
[INFO][Stream] 28.12.2019 11:42:11 [] (unknown:0) - Loading with imageIOName: GDCM
[ERROR][VTK] 28.12.2019 11:42:11 [vtkITKArchetypeImageSeriesScalarReader (0000000010ACFAF0)] (D:\D\S\Slicer-4102\Libs\vtkITK\vtkITKArchetypeImageSeriesScalarReader.cxx:257) - UpdateFromSeries: Unsupported number of components: 1 != 3
[CRITICAL][Stream] 28.12.2019 11:42:11 [] (unknown:0) - Could not read scalar volume using GDCM approach.  Error is: FileFormatError
[INFO][Stream] 28.12.2019 11:42:11 [] (unknown:0) - Loading with imageIOName: DCMTK
[ERROR][VTK] 28.12.2019 11:42:12 [vtkITKArchetypeImageSeriesScalarReader (0000000010ACF740)] (D:\D\S\Slicer-4102\Libs\vtkITK\vtkITKArchetypeImageSeriesScalarReader.cxx:257) - UpdateFromSeries: Unsupported number of components: 1 != 3
[CRITICAL][Stream] 28.12.2019 11:42:12 [] (unknown:0) - Could not read scalar volume using DCMTK approach.  Error is: FileFormatError
[CRITICAL][Stream] 28.12.2019 11:42:12 [] (unknown:0) -
[CRITICAL][Stream] 28.12.2019 11:42:12 [] (unknown:0) - Could not load: 5: t1_mprage_sag_p2 as a Scalar Volume
[DEBUG][Python] 28.12.2019 11:43:53 [Python] (D:/PROGRAMfile/Slicer 4.10.2/bin/../lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:455) - MultiVolumeImportPlugin::examine
[DEBUG][Python] 28.12.2019 11:43:53 [Python] (D:/PROGRAMfile/Slicer 4.10.2/bin/../lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:495) - DICOMMultiVolumePlugin found 1 multivolumes!
[DEBUG][Python] 28.12.2019 11:43:54 [Python] (D:/PROGRAMfile/Slicer 4.10.2/bin/../lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:165) - MultiVolumeImportPlugin:examineMultiseries
[DEBUG][Python] 28.12.2019 11:43:54 [Python] (D:/PROGRAMfile/Slicer 4.10.2/bin/../lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:170) - DICOMMultiVolumePlugin found 0 multivolumes!
[INFO][Python] 28.12.2019 11:43:54 [Python] (D:/PROGRAMfile/Slicer 4.10.2/bin/../lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py:303) - Loading with imageIOName: GDCM
[ERROR][Python] 28.12.2019 11:43:55 [Python] (D:/PROGRAMfile/Slicer 4.10.2/bin/../lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py:309) - Could not read scalar volume using GDCM approach.  Error is: FileFormatError
[INFO][Python] 28.12.2019 11:43:55 [Python] (D:/PROGRAMfile/Slicer 4.10.2/bin/../lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py:303) - Loading with imageIOName: DCMTK
[ERROR][Python] 28.12.2019 11:43:55 [Python] (D:/PROGRAMfile/Slicer 4.10.2/bin/../lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py:309) - Could not read scalar volume using DCMTK approach.  Error is: FileFormatError
[WARNING][Python] 28.12.2019 11:43:55 [Python] (D:\PROGRAMfile\Slicer 4.10.2\bin\Python\slicer\util.py:1110) - 
Could not load: 5: t1_mprage_sag_p2 as a Scalar Volume
[INFO][Stream] 28.12.2019 11:43:54 [] (unknown:0) - Loading with imageIOName: GDCM
[ERROR][VTK] 28.12.2019 11:43:55 [vtkITKArchetypeImageSeriesScalarReader (0000000010ACFEA0)] (D:\D\S\Slicer-4102\Libs\vtkITK\vtkITKArchetypeImageSeriesScalarReader.cxx:257) - UpdateFromSeries: Unsupported number of components: 1 != 3
[CRITICAL][Stream] 28.12.2019 11:43:55 [] (unknown:0) - Could not read scalar volume using GDCM approach.  Error is: FileFormatError
[INFO][Stream] 28.12.2019 11:43:55 [] (unknown:0) - Loading with imageIOName: DCMTK
[ERROR][VTK] 28.12.2019 11:43:55 [vtkITKArchetypeImageSeriesScalarReader (0000000010ACF740)] (D:\D\S\Slicer-4102\Libs\vtkITK\vtkITKArchetypeImageSeriesScalarReader.cxx:257) - UpdateFromSeries: Unsupported number of components: 1 != 3
[CRITICAL][Stream] 28.12.2019 11:43:55 [] (unknown:0) - Could not read scalar volume using DCMTK approach.  Error is: FileFormatError
[CRITICAL][Stream] 28.12.2019 11:43:55 [] (unknown:0) -
[CRITICAL][Stream] 28.12.2019 11:43:55 [] (unknown:0) - Could not load: 5: t1_mprage_sag_p2 as a Scalar Volume
</code></pre>
</details>

---

## Post #2 by @lassoan (2019-12-29 02:14 UTC)

<p>There is no color volume reader plugin in DICOM module, because we very rarely see them in clinical practice and they are usually not suitable for any further processing or analysis.</p>
<p>You can still load them by forcing to use ITK’s image reader: drag-and-drop any of the DICOM files (a single file, not multiple files or a folder), make sure “Single slice” is disabled (shown when “Show options” is enabled).</p>
<p>What generates these RGB color images? Do you think they are valid? What you would like to achieve with them? For example, if you want to save segmentation then don’t stored it as RGB overlay in MR modality image but save as a separate DICOM segmentation object.</p>

---

## Post #3 by @jjuguilon (2019-12-29 13:36 UTC)

<p>Thank you! it really helps. most of the files i am encountering were mostly .MVL and .VOL coming from the ultrasound images. was there any way, we can extract 3D out of the MP4 video formats or some series of jpegs generated during the ultrasound?</p>

---

## Post #4 by @lassoan (2019-12-29 15:23 UTC)

<aside class="quote no-group" data-username="jjuguilon" data-post="3" data-topic="9634">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/4bbf92/48.png" class="avatar"> jjuguilon:</div>
<blockquote>
<p>we can extract 3D out of the MP4 video formats or some series of jpegs generated during the ultrasound</p>
</blockquote>
</aside>
<p>If you know the probe position and orientation for each image frame then <a href="https://www.plustoolkit.org">Plus toolkit</a> can reconstruct a 3D volume from the series of 2D frames.</p>

---

## Post #5 by @jjuguilon (2019-12-29 16:11 UTC)

<p>wow, i will surely try this method. thank you</p>

---
