# Unable to load DICOM segmentation file

**Topic ID**: 15134
**Date**: 2020-12-18
**URL**: https://discourse.slicer.org/t/unable-to-load-dicom-segmentation-file/15134

---

## Post #1 by @AshrafM (2020-12-18 14:30 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.10.2<br>
Expected behavior: Load segmentation DICOM images<br>
Actual behavior: Unable to load, with error message</p>
<p>Hi,<br>
I am trying to open a DICOM file with segmentation of an MRI in slicer, unsuccessfully.  I have checked a couple post on similar issues before, but it seems to be a different issue. The segmentation was generated on a Siemens workstation.</p>
<p>I have the following toolboxes<br>
QuantiativeReporting<br>
SlicerRT<br>
SlicerDevelopmentToolbox</p>
<h2>The log is below.<br>
Any suggestions?<br>
Thank you.</h2>
<p>[DEBUG][Qt] 18.12.2020 22:36:44 [] (unknown:0) - Session start time …: 2020-12-18 22:36:44<br>
[DEBUG][Qt] 18.12.2020 22:36:44 [] (unknown:0) - Slicer version …: 4.10.2 (revision 28257) win-amd64 - installed release<br>
[DEBUG][Qt] 18.12.2020 22:36:44 [] (unknown:0) - Operating system …: Windows /  Professional /  (Build 9200) - 64-bit<br>
[DEBUG][Qt] 18.12.2020 22:36:44 [] (unknown:0) - Memory …: 8035 MB physical, 15715 MB virtual<br>
[DEBUG][Qt] 18.12.2020 22:36:44 [] (unknown:0) - CPU …: GenuineIntel , 8 cores, 8 logical processors<br>
[DEBUG][Qt] 18.12.2020 22:36:44 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 18.12.2020 22:36:44 [] (unknown:0) - Developer mode enabled …: yes<br>
[DEBUG][Qt] 18.12.2020 22:36:44 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 18.12.2020 22:36:44 [] (unknown:0) - Additional module paths …: C:/Users/mohaas01/AppData/Roaming/NA-MIC/Extensions-28257/SlicerDevelopmentToolbox/lib/Slicer-4.10/qt-scripted-modules, C:/Users/mohaas01/AppData/Roaming/NA-MIC/Extensions-28257/SlicerRT/lib/Slicer-4.10/cli-modules, C:/Users/mohaas01/AppData/Roaming/NA-MIC/Extensions-28257/SlicerRT/lib/Slicer-4.10/qt-loadable-modules, C:/Users/mohaas01/AppData/Roaming/NA-MIC/Extensions-28257/SlicerRT/lib/Slicer-4.10/qt-scripted-modules, C:/Users/mohaas01/AppData/Roaming/NA-MIC/Extensions-28257/DCMQI/lib/Slicer-4.10/cli-modules, C:/Users/mohaas01/AppData/Roaming/NA-MIC/Extensions-28257/QuantitativeReporting/lib/Slicer-4.10/qt-scripted-modules<br>
[DEBUG][Python] 18.12.2020 22:36:56 [Python] (C:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 18.12.2020 22:36:59 [Python] (C:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 18.12.2020 22:36:59 [Python] (C:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 18.12.2020 22:36:59 [] (unknown:0) - Switch to module:  “Welcome”<br>
[WARNING][Qt] 18.12.2020 22:39:27 [] (unknown:0) - An OpenGL Core Profile was requested, but it is not supported on the current platform. Falling back to a non-Core profile. Note that this might cause rendering issues.<br>
[WARNING][Qt] 18.12.2020 22:39:27 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 18.12.2020 22:39:27 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 18.12.2020 22:39:27 [] (unknown:0) - Remote debugging server started successfully. Try pointing a Chromium-based browser to <a href="http://127.0.0.1:1337" rel="noopener nofollow ugc">http://127.0.0.1:1337</a><br>
[DEBUG][Qt] 18.12.2020 22:41:51 [] (unknown:0) - Switch to module:  “DICOM”<br>
[DEBUG][Qt] 18.12.2020 22:41:54 [] (unknown:0) - Deleting  1  patients<br>
[DEBUG][Qt] 18.12.2020 22:41:54 [] (unknown:0) - SQLITE: removing seriesInstanceUID 1.3.12.2.1107.5.4.5.164247.30000020072022243746900000203<br>
[DEBUG][Qt] 18.12.2020 22:41:54 [] (unknown:0) - SQLITE: removing seriesInstanceUID 1.3.12.2.1107.5.4.5.164247.30000020072022243746900000397<br>
[CRITICAL][Stream] 18.12.2020 22:42:09 [] (unknown:0) - DICOM dataset contains some encoding that we never thought we would see(ISO 2022 IR 100). Using default encoding.<br>
[CRITICAL][Stream] 18.12.2020 22:42:09 [] (unknown:0) - DICOM dataset contains some encoding that we never thought we would see(ISO 2022 IR 100). Using default encoding.<br>
[CRITICAL][Stream] 18.12.2020 22:42:09 [] (unknown:0) - DICOM dataset contains some encoding that we never thought we would see(ISO 2022 IR 100). Using default encoding.<br>
[CRITICAL][Stream] 18.12.2020 22:42:09 [] (unknown:0) - DICOM dataset contains some encoding that we never thought we would see(ISO 2022 IR 100). Using default encoding.<br>
[DEBUG][Qt] 18.12.2020 22:42:09 [] (unknown:0) - New patient inserted: 109<br>
[DEBUG][Qt] 18.12.2020 22:42:09 [] (unknown:0) - New patient inserted as :  109<br>
[DEBUG][Qt] 18.12.2020 22:42:09 [] (unknown:0) - Need to insert new study:  “1.3.12.2.1107.5.4.5.164247.30000020072022243746900000202”<br>
[CRITICAL][Stream] 18.12.2020 22:42:09 [] (unknown:0) - DICOM dataset contains some encoding that we never thought we would see(ISO 2022 IR 100). Using default encoding.<br>
[CRITICAL][Stream] 18.12.2020 22:42:09 [] (unknown:0) - DICOM dataset contains some encoding that we never thought we would see(ISO 2022 IR 100). Using default encoding.<br>
[CRITICAL][Stream] 18.12.2020 22:42:09 [] (unknown:0) - DICOM dataset contains some encoding that we never thought we would see(ISO 2022 IR 100). Using default encoding.<br>
[DEBUG][Qt] 18.12.2020 22:42:09 [] (unknown:0) - Study Added<br>
[DEBUG][Qt] 18.12.2020 22:42:09 [] (unknown:0) - Need to insert new series:  “1.3.12.2.1107.5.4.5.164247.30000020072022243746900000397”<br>
[DEBUG][Qt] 18.12.2020 22:42:09 [] (unknown:0) - Series Added<br>
[DEBUG][Qt] 18.12.2020 22:42:09 [] (unknown:0) - “DICOM indexer has successfully processed 1 files [0.19s]”<br>
[INFO][Python] 18.12.2020 22:42:11 [Python] (C:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\DICOMLib\DICOMWidgets.py:471) - Imported a DICOM directory, checking for extensions<br>
[INFO][Stream] 18.12.2020 22:42:11 [] (unknown:0) - Imported a DICOM directory, checking for extensions<br>
[DEBUG][Python] 18.12.2020 22:42:37 [Python] (C:\Users\mohaas01\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMParametricMapPluginClass : Caching files<br>
[DEBUG][Python] 18.12.2020 22:42:37 [Python] (C:\Users\mohaas01\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMParametricMapPluginClass : Caching files<br>
[DEBUG][Python] 18.12.2020 22:42:44 [Python] (C:\Users\mohaas01\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMParametricMapPluginClass : Using cached files<br>
[DEBUG][Python] 18.12.2020 22:42:44 [Python] (C:\Users\mohaas01\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMParametricMapPluginClass : Using cached files<br>
[DEBUG][Python] 18.12.2020 22:42:44 [Python] (C:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:455) - MultiVolumeImportPlugin::examine<br>
[DEBUG][Python] 18.12.2020 22:42:47 [Python] (C:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:495) - DICOMMultiVolumePlugin found 1 multivolumes!<br>
[DEBUG][Python] 18.12.2020 22:42:48 [Python] (C:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:455) - MultiVolumeImportPlugin::examine<br>
[DEBUG][Python] 18.12.2020 22:43:24 [Python] (C:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:495) - DICOMMultiVolumePlugin found 1 multivolumes!<br>
[DEBUG][Python] 18.12.2020 22:43:55 [Python] (C:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:165) - MultiVolumeImportPlugin:examineMultiseries<br>
[DEBUG][Python] 18.12.2020 22:44:07 [Python] (C:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:170) - DICOMMultiVolumePlugin found 0 multivolumes!<br>
[INFO][Stream] 18.12.2020 22:44:12 [] (unknown:0) - reg inside examine<br>
[DEBUG][Python] 18.12.2020 22:44:13 [Python] (C:\Users\mohaas01\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMSegmentationPluginClass : Caching files<br>
[DEBUG][Python] 18.12.2020 22:44:13 [Python] (C:/Users/mohaas01/AppData/Roaming/NA-MIC/Extensions-28257/QuantitativeReporting/lib/Slicer-4.10/qt-scripted-modules/DICOMSegmentationPlugin.py:60) - DICOM SEG modality found<br>
[DEBUG][Python] 18.12.2020 22:44:13 [Python] (C:/Users/mohaas01/AppData/Roaming/NA-MIC/Extensions-28257/QuantitativeReporting/lib/Slicer-4.10/qt-scripted-modules/DICOMSegmentationPlugin.py:60) - DICOM SEG modality found<br>
[DEBUG][Python] 18.12.2020 22:44:13 [Python] (C:\Users\mohaas01\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMSegmentationPluginClass : Caching files<br>
[DEBUG][Python] 18.12.2020 22:44:20 [Python] (C:\Users\mohaas01\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMTID1500PluginClass : Caching files<br>
[DEBUG][Python] 18.12.2020 22:44:20 [Python] (C:\Users\mohaas01\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMTID1500PluginClass : Caching files<br>
[DEBUG][Python] 18.12.2020 22:44:20 [Python] (C:\Users\mohaas01\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMTID1500PluginClass : Using cached files<br>
[DEBUG][Python] 18.12.2020 22:44:20 [Python] (C:\Users\mohaas01\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMTID1500PluginClass : Using cached files<br>
[DEBUG][Python] 18.12.2020 22:44:44 [Python] (C:/Users/mohaas01/AppData/Roaming/NA-MIC/Extensions-28257/QuantitativeReporting/lib/Slicer-4.10/qt-scripted-modules/DICOMSegmentationPlugin.py:81) - DICOM SEG load()<br>
[DEBUG][Python] 18.12.2020 22:44:44 [Python] (C:/Users/mohaas01/AppData/Roaming/NA-MIC/Extensions-28257/QuantitativeReporting/lib/Slicer-4.10/qt-scripted-modules/DICOMSegmentationPlugin.py:84) - in load(): uid = 1.3.12.2.1107.5.4.5.164247.30000020072022243746900000399<br>
[ERROR][Python] 18.12.2020 22:44:45 [Python] (C:/Users/mohaas01/AppData/Roaming/NA-MIC/Extensions-28257/QuantitativeReporting/lib/Slicer-4.10/qt-scripted-modules/DICOMSegmentationPlugin.py:117) - SEG2NRRD did not complete successfully, unable to load DICOM Segmentation<br>
[DEBUG][Python] 18.12.2020 22:44:45 [Python] (C:\Users\mohaas01\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:34) - Cleaning up temporarily created directory C:/Users/mohaas01/AppData/Local/Temp/Slicer\QIICR\SEG\2020-12-18_224444\1.3.12.2.1107.5.4.5.164247.30000020072022243746900000399<br>
[DEBUG][Qt] 18.12.2020 22:44:44 [] (unknown:0) - Found CommandLine Module, target is  C:/Users/mohaas01/AppData/Roaming/NA-MIC/Extensions-28257/DCMQI/lib/Slicer-4.10/cli-modules/segimage2itkimage.exe<br>
[DEBUG][Qt] 18.12.2020 22:44:44 [] (unknown:0) - ModuleType: CommandLineModule<br>
[DEBUG][Qt] 18.12.2020 22:44:44 [] (unknown:0) - Convert DICOM Segmentation Image into ITK image(s) command line:</p>
<p>C:/Users/mohaas01/AppData/Roaming/NA-MIC/Extensions-28257/DCMQI/lib/Slicer-4.10/cli-modules/segimage2itkimage.exe --inputDICOM D:/MyData/JikeiTumorSegmentation/Test/CASE3_MRI_PRE_1.SEG.0016.0002.2020_20200730_103640831_003331.IMA --outputDirectory C:/Users/mohaas01/AppData/Local/Temp/Slicer\QIICR\SEG\2020-12-18_224444\1.3.12.2.1107.5.4.5.164247.30000020072022243746900000399 --outputType nrrd<br>
[DEBUG][Qt] 18.12.2020 22:44:45 [] (unknown:0) - Convert DICOM Segmentation Image into ITK image(s) standard output:</p>
<p>dcmqi repository URL: git://github.com/QIICR/dcmqi.git revision: a33fa9e tag: v1.2.2<br>
[ERROR][VTK] 18.12.2020 22:44:45 [vtkSlicerCLIModuleLogic (000002595ED33990)] (D:\D\S\Slicer-4102\Base\QTCLI\vtkSlicerCLIModuleLogic.cxx:2056) - Convert DICOM Segmentation Image into ITK image(s) standard error:</p>
<p>W: CodingSchemeDesignator (0008,0102) absent in CodeSequenceMacro (type 1)<br>
W: CodeMeaning (0008,0104) absent in CodeSequenceMacro (type 1)<br>
W: FrameOfReferenceUID (0020,0052) absent in FrameOfReferenceModule (type 1)<br>
W: DeviceSerialNumber (0018,1000) absent in EnhancedGeneralEquipmentModule (type 1)<br>
Plane Orientation (Patient) is missing, cannot parse input<br>
ERROR: Failed to get image directions!<br>
Fatal error encountered.<br>
[ERROR][VTK] 18.12.2020 22:44:45 [vtkSlicerCLIModuleLogic (000002595ED33990)] (D:\D\S\Slicer-4102\Base\QTCLI\vtkSlicerCLIModuleLogic.cxx:2087) - Convert DICOM Segmentation Image into ITK image(s) completed with errors<br>
[CRITICAL][Stream] 18.12.2020 22:44:45 [] (unknown:0) - SEG2NRRD did not complete successfully, unable to load DICOM Segmentation<br>
[DEBUG][Python] 18.12.2020 22:44:45 [Python] (C:/Users/mohaas01/AppData/Roaming/NA-MIC/Extensions-28257/QuantitativeReporting/lib/Slicer-4.10/qt-scripted-modules/DICOMSegmentationPlugin.py:81) - DICOM SEG load()<br>
[DEBUG][Python] 18.12.2020 22:44:45 [Python] (C:/Users/mohaas01/AppData/Roaming/NA-MIC/Extensions-28257/QuantitativeReporting/lib/Slicer-4.10/qt-scripted-modules/DICOMSegmentationPlugin.py:84) - in load(): uid = 1.3.12.2.1107.5.4.5.164247.30000020072022243746900000398<br>
[ERROR][Python] 18.12.2020 22:44:45 [Python] (C:/Users/mohaas01/AppData/Roaming/NA-MIC/Extensions-28257/QuantitativeReporting/lib/Slicer-4.10/qt-scripted-modules/DICOMSegmentationPlugin.py:117) - SEG2NRRD did not complete successfully, unable to load DICOM Segmentation<br>
[DEBUG][Python] 18.12.2020 22:44:45 [Python] (C:\Users\mohaas01\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:34) - Cleaning up temporarily created directory C:/Users/mohaas01/AppData/Local/Temp/Slicer\QIICR\SEG\2020-12-18_224444\1.3.12.2.1107.5.4.5.164247.30000020072022243746900000398<br>
[DEBUG][Qt] 18.12.2020 22:44:45 [] (unknown:0) - Found CommandLine Module, target is  C:/Users/mohaas01/AppData/Roaming/NA-MIC/Extensions-28257/DCMQI/lib/Slicer-4.10/cli-modules/segimage2itkimage.exe<br>
[DEBUG][Qt] 18.12.2020 22:44:45 [] (unknown:0) - ModuleType: CommandLineModule<br>
[DEBUG][Qt] 18.12.2020 22:44:45 [] (unknown:0) - Convert DICOM Segmentation Image into ITK image(s) command line:</p>
<p>C:/Users/mohaas01/AppData/Roaming/NA-MIC/Extensions-28257/DCMQI/lib/Slicer-4.10/cli-modules/segimage2itkimage.exe --outputDirectory C:/Users/mohaas01/AppData/Local/Temp/Slicer\QIICR\SEG\2020-12-18_224444\1.3.12.2.1107.5.4.5.164247.30000020072022243746900000398 --outputType nrrd<br>
[DEBUG][Qt] 18.12.2020 22:44:45 [] (unknown:0) - Convert DICOM Segmentation Image into ITK image(s) standard output:</p>
<p>dcmqi repository URL: git://github.com/QIICR/dcmqi.git revision: a33fa9e tag: v1.2.2<br>
[ERROR][VTK] 18.12.2020 22:44:45 [vtkSlicerCLIModuleLogic (000002595ED33990)] (D:\D\S\Slicer-4102\Base\QTCLI\vtkSlicerCLIModuleLogic.cxx:2056) - Convert DICOM Segmentation Image into ITK image(s) standard error:</p>
<p>Error: Input DICOM file must be specified!<br>
[ERROR][VTK] 18.12.2020 22:44:45 [vtkSlicerCLIModuleLogic (000002595ED33990)] (D:\D\S\Slicer-4102\Base\QTCLI\vtkSlicerCLIModuleLogic.cxx:2087) - Convert DICOM Segmentation Image into ITK image(s) completed with errors<br>
[CRITICAL][Stream] 18.12.2020 22:44:45 [] (unknown:0) - SEG2NRRD did not complete successfully, unable to load DICOM Segmentation<br>
[INFO][Python] 18.12.2020 22:44:45 [Python] (C:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py:303) - Loading with imageIOName: GDCM<br>
[INFO][Python] 18.12.2020 22:44:52 [Python] (C:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py:375) - Window/level found in DICOM tags (center=33.0, width=88.0) has been applied to volume Unnamed Series<br>
[WARNING][Python] 18.12.2020 22:44:53 [Python] (C:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py:697) - Irregular volume geometry detected (maximum error of 0.00133695 mm is above tolerance threshold of 0.001 mm).  Adding acquisition transform to regularize geometry.<br>
[WARNING][Python] 18.12.2020 22:44:53 [Python] (C:\Program Files\Slicer 4.10.2\bin\Python\slicer\util.py:1110) -<br>
Could not load: Unknown as a DICOMSegmentation<br>
Could not load: Unknown as a DICOMSegmentation</p>

---

## Post #2 by @lassoan (2020-12-18 14:42 UTC)

<p>Please try with laatest Slicer Preview Release. If it does not work then enable detailed logging in DICOM section of application settings and post the log here.</p>

---

## Post #3 by @AshrafM (2020-12-18 15:20 UTC)

<p>Thank you for the quick reply. I am getting a similar error with the latest Preview Release 4.13.0 2020-12-17. It seems to be a similar error message as before.<br>
Thank you</p>
<h1>Here is the log</h1>
<p>[DEBUG][Qt] 19.12.2020 00:13:57 [] (unknown:0) - Session start time …: 2020-12-19 00:13:57<br>
[DEBUG][Qt] 19.12.2020 00:13:57 [] (unknown:0) - Slicer version …: 4.13.0-2020-12-17 (revision 29531 / 0b5169e) win-amd64 - installed release<br>
[DEBUG][Qt] 19.12.2020 00:13:57 [] (unknown:0) - Operating system …: Windows /  Professional / (Build 17134, Code Page 932) - 64-bit<br>
[DEBUG][Qt] 19.12.2020 00:13:57 [] (unknown:0) - Memory …: 8035 MB physical, 15715 MB virtual<br>
[DEBUG][Qt] 19.12.2020 00:13:57 [] (unknown:0) - CPU …: GenuineIntel , 8 cores, 8 logical processors<br>
[DEBUG][Qt] 19.12.2020 00:13:57 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 19.12.2020 00:13:57 [] (unknown:0) - Qt configuration …: version 5.15.1, with SSL, requested OpenGL 3.2 (compatibility profile)<br>
[DEBUG][Qt] 19.12.2020 00:13:57 [] (unknown:0) - Developer mode enabled …: yes<br>
[DEBUG][Qt] 19.12.2020 00:13:57 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 19.12.2020 00:13:57 [] (unknown:0) - Application path …: C:/Users/mohaas01/AppData/Local/NA-MIC/Slicer 4.13.0-2020-12-17/bin<br>
[DEBUG][Qt] 19.12.2020 00:13:57 [] (unknown:0) - Additional module paths …: C:/Users/mohaas01/AppData/Roaming/NA-MIC/Extensions-29531/QuantitativeReporting/lib/Slicer-4.13/qt-scripted-modules, C:/Users/mohaas01/AppData/Roaming/NA-MIC/Extensions-29531/SlicerDevelopmentToolbox/lib/Slicer-4.13/qt-scripted-modules, C:/Users/mohaas01/AppData/Roaming/NA-MIC/Extensions-29531/SlicerRT/lib/Slicer-4.13/cli-modules, C:/Users/mohaas01/AppData/Roaming/NA-MIC/Extensions-29531/SlicerRT/lib/Slicer-4.13/qt-loadable-modules, C:/Users/mohaas01/AppData/Roaming/NA-MIC/Extensions-29531/SlicerRT/lib/Slicer-4.13/qt-scripted-modules, C:/Users/mohaas01/AppData/Roaming/NA-MIC/Extensions-29531/DCMQI/lib/Slicer-4.13/cli-modules<br>
[DEBUG][Python] 19.12.2020 00:14:00 [Python] (C:\Users\mohaas01\AppData\Local\NA-MIC\Slicer 4.13.0-2020-12-17\lib\Python\Lib\site-packages\pydicom\datadict.py:432) - Reversing DICOM dictionary so can look up tag from a keyword…<br>
[DEBUG][Python] 19.12.2020 00:14:02 [Python] (C:\Users\mohaas01\AppData\Local\NA-MIC\Slicer 4.13.0-2020-12-17\lib\Slicer-4.13\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 19.12.2020 00:14:03 [Python] (C:\Users\mohaas01\AppData\Local\NA-MIC\Slicer 4.13.0-2020-12-17\lib\Slicer-4.13\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 19.12.2020 00:14:03 [Python] (C:\Users\mohaas01\AppData\Local\NA-MIC\Slicer 4.13.0-2020-12-17\lib\Slicer-4.13\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 19.12.2020 00:14:04 [] (unknown:0) - Switch to module:  “Welcome”<br>
[DEBUG][Qt] 19.12.2020 00:14:23 [] (unknown:0) - Switch to module:  “DICOM”<br>
[DEBUG][Python] 19.12.2020 00:14:31 [Python] (C:\Users\mohaas01\AppData\Roaming\NA-MIC\Extensions-29531\QuantitativeReporting\lib\Slicer-4.13\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMParametricMapPluginClass : Caching files<br>
[DEBUG][Python] 19.12.2020 00:14:31 [Python] (C:\Users\mohaas01\AppData\Roaming\NA-MIC\Extensions-29531\QuantitativeReporting\lib\Slicer-4.13\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMParametricMapPluginClass : Using cached files<br>
[DEBUG][Python] 19.12.2020 00:14:31 [Python] (C:\Users\mohaas01\AppData\Roaming\NA-MIC\Extensions-29531\QuantitativeReporting\lib\Slicer-4.13\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMSegmentationPluginClass : Caching files<br>
[DEBUG][Python] 19.12.2020 00:14:31 [Python] (C:/Users/mohaas01/AppData/Roaming/NA-MIC/Extensions-29531/QuantitativeReporting/lib/Slicer-4.13/qt-scripted-modules/DICOMSegmentationPlugin.py:62) - DICOM SEG modality found<br>
[DEBUG][Python] 19.12.2020 00:14:31 [Python] (C:/Users/mohaas01/AppData/Roaming/NA-MIC/Extensions-29531/QuantitativeReporting/lib/Slicer-4.13/qt-scripted-modules/DICOMSegmentationPlugin.py:62) - DICOM SEG modality found<br>
[DEBUG][Python] 19.12.2020 00:14:31 [Python] (C:\Users\mohaas01\AppData\Roaming\NA-MIC\Extensions-29531\QuantitativeReporting\lib\Slicer-4.13\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMTID1500PluginClass : Caching files<br>
[ERROR][Python] 19.12.2020 00:14:31 [Python] (C:\Users\mohaas01\AppData\Roaming\NA-MIC\Extensions-29531\SlicerDevelopmentToolbox\lib\Slicer-4.13\qt-scripted-modules\SlicerDevelopmentToolboxUtils\mixins.py:729) - ‘FileDataset’ object has no attribute ‘SeriesDescription’<br>
[ERROR][Python] 19.12.2020 00:14:31 [Python] (C:\Users\mohaas01\AppData\Roaming\NA-MIC\Extensions-29531\SlicerDevelopmentToolbox\lib\Slicer-4.13\qt-scripted-modules\SlicerDevelopmentToolboxUtils\mixins.py:729) - ‘FileDataset’ object has no attribute ‘SeriesDescription’<br>
[DEBUG][Python] 19.12.2020 00:14:31 [Python] (C:\Users\mohaas01\AppData\Roaming\NA-MIC\Extensions-29531\QuantitativeReporting\lib\Slicer-4.13\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMTID1500PluginClass : Using cached files<br>
[CRITICAL][Stream] 19.12.2020 00:14:31 [] (unknown:0) - ‘FileDataset’ object has no attribute ‘SeriesDescription’<br>
[CRITICAL][Stream] 19.12.2020 00:14:31 [] (unknown:0) - ‘FileDataset’ object has no attribute ‘SeriesDescription’<br>
[DEBUG][Python] 19.12.2020 00:14:42 [Python] (C:/Users/mohaas01/AppData/Roaming/NA-MIC/Extensions-29531/QuantitativeReporting/lib/Slicer-4.13/qt-scripted-modules/DICOMSegmentationPlugin.py:83) - DICOM SEG load()<br>
[DEBUG][Python] 19.12.2020 00:14:42 [Python] (C:/Users/mohaas01/AppData/Roaming/NA-MIC/Extensions-29531/QuantitativeReporting/lib/Slicer-4.13/qt-scripted-modules/DICOMSegmentationPlugin.py:86) - in load(): uid = 1.3.12.2.1107.5.4.5.164007.30000020080308240198200000581<br>
[ERROR][Python] 19.12.2020 00:14:44 [Python] (C:/Users/mohaas01/AppData/Roaming/NA-MIC/Extensions-29531/QuantitativeReporting/lib/Slicer-4.13/qt-scripted-modules/DICOMSegmentationPlugin.py:119) - SEG2NRRD did not complete successfully, unable to load DICOM Segmentation<br>
[DEBUG][Python] 19.12.2020 00:14:44 [Python] (C:\Users\mohaas01\AppData\Roaming\NA-MIC\Extensions-29531\QuantitativeReporting\lib\Slicer-4.13\qt-scripted-modules\base\DICOMPluginBase.py:34) - Cleaning up temporarily created directory C:/Users/mohaas01/AppData/Local/Temp/Slicer\QIICR\SEG\2020-12-19_001442\1.3.12.2.1107.5.4.5.164007.30000020080308240198200000581<br>
[WARNING][Python] 19.12.2020 00:14:44 [Python] (C:\Users\mohaas01\AppData\Local\NA-MIC\Slicer 4.13.0-2020-12-17\bin\Python\slicer\util.py:1988) - Could not load: Unknown as a DICOMSegmentation<br>
[DEBUG][Qt] 19.12.2020 00:14:42 [] (unknown:0) - Found CommandLine Module, target is  C:/Users/mohaas01/AppData/Roaming/NA-MIC/Extensions-29531/DCMQI/lib/Slicer-4.13/cli-modules/segimage2itkimage.exe<br>
[DEBUG][Qt] 19.12.2020 00:14:42 [] (unknown:0) - ModuleType: CommandLineModule<br>
[DEBUG][Qt] 19.12.2020 00:14:42 [] (unknown:0) - Convert DICOM Segmentation Image into ITK image(s) command line:</p>
<p>C:/Users/mohaas01/AppData/Roaming/NA-MIC/Extensions-29531/DCMQI/lib/Slicer-4.13/cli-modules/segimage2itkimage.exe --inputDICOM D:/MyData/JikeiTumorSegmentation/DICOM-Original/OR5/MR1/Case3_MRI_pre/CASE3_MRI_PRE_1.SEG.0016.0001.2020_20200803_181121804_003330.IMA --outputDirectory C:/Users/mohaas01/AppData/Local/Temp/Slicer\QIICR\SEG\2020-12-19_001442\1.3.12.2.1107.5.4.5.164007.30000020080308240198200000581 --outputType nrrd<br>
[DEBUG][Qt] 19.12.2020 00:14:44 [] (unknown:0) - Convert DICOM Segmentation Image into ITK image(s) standard output:</p>
<p>dcmqi repository URL: git://github.com/QIICR/dcmqi.git revision: 99192b7 tag: latest<br>
[ERROR][VTK] 19.12.2020 00:14:44 [vtkSlicerCLIModuleLogic (0000020C1DF76560)] (D:\D\P\Slicer-0\Base\QTCLI\vtkSlicerCLIModuleLogic.cxx:2017) - Convert DICOM Segmentation Image into ITK image(s) standard error:</p>
<p>W: CodingSchemeDesignator (0008,0102) absent in CodeSequenceMacro (type 1)<br>
W: CodeMeaning (0008,0104) absent in CodeSequenceMacro (type 1)<br>
W: FrameOfReferenceUID (0020,0052) absent in FrameOfReferenceModule (type 1)<br>
W: DeviceSerialNumber (0018,1000) absent in EnhancedGeneralEquipmentModule (type 1)<br>
W: SegmentLabel (0062,0005) empty in SegmentDescriptionMacro (type 1)<br>
Plane Orientation (Patient) is missing, cannot parse input<br>
ERROR: Failed to get image directions!<br>
Fatal error encountered.<br>
[ERROR][VTK] 19.12.2020 00:14:44 [vtkSlicerCLIModuleLogic (0000020C1DF76560)] (D:\D\P\Slicer-0\Base\QTCLI\vtkSlicerCLIModuleLogic.cxx:2048) - Convert DICOM Segmentation Image into ITK image(s) completed with errors<br>
[CRITICAL][Stream] 19.12.2020 00:14:44 [] (unknown:0) - SEG2NRRD did not complete successfully, unable to load DICOM Segmentation<br>
[CRITICAL][Stream] 19.12.2020 00:14:44 [] (unknown:0) - Could not load: Unknown as a DICOMSegmentation</p>

---

## Post #4 by @AshrafM (2020-12-18 15:26 UTC)

<p>With Detailed logging:</p>
<p>[DEBUG][Qt] 19.12.2020 00:13:57 [] (unknown:0) - Session start time …: 2020-12-19 00:13:57<br>
[DEBUG][Qt] 19.12.2020 00:13:57 [] (unknown:0) - Slicer version …: 4.13.0-2020-12-17 (revision 29531 / 0b5169e) win-amd64 - installed release<br>
[DEBUG][Qt] 19.12.2020 00:13:57 [] (unknown:0) - Operating system …: Windows /  Professional / (Build 17134, Code Page 932) - 64-bit<br>
[DEBUG][Qt] 19.12.2020 00:13:57 [] (unknown:0) - Memory …: 8035 MB physical, 15715 MB virtual<br>
[DEBUG][Qt] 19.12.2020 00:13:57 [] (unknown:0) - CPU …: GenuineIntel , 8 cores, 8 logical processors<br>
[DEBUG][Qt] 19.12.2020 00:13:57 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 19.12.2020 00:13:57 [] (unknown:0) - Qt configuration …: version 5.15.1, with SSL, requested OpenGL 3.2 (compatibility profile)<br>
[DEBUG][Qt] 19.12.2020 00:13:57 [] (unknown:0) - Developer mode enabled …: yes<br>
[DEBUG][Qt] 19.12.2020 00:13:57 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 19.12.2020 00:13:57 [] (unknown:0) - Application path …: C:/Users/mohaas01/AppData/Local/NA-MIC/Slicer 4.13.0-2020-12-17/bin<br>
[DEBUG][Qt] 19.12.2020 00:13:57 [] (unknown:0) - Additional module paths …: C:/Users/mohaas01/AppData/Roaming/NA-MIC/Extensions-29531/QuantitativeReporting/lib/Slicer-4.13/qt-scripted-modules, C:/Users/mohaas01/AppData/Roaming/NA-MIC/Extensions-29531/SlicerDevelopmentToolbox/lib/Slicer-4.13/qt-scripted-modules, C:/Users/mohaas01/AppData/Roaming/NA-MIC/Extensions-29531/SlicerRT/lib/Slicer-4.13/cli-modules, C:/Users/mohaas01/AppData/Roaming/NA-MIC/Extensions-29531/SlicerRT/lib/Slicer-4.13/qt-loadable-modules, C:/Users/mohaas01/AppData/Roaming/NA-MIC/Extensions-29531/SlicerRT/lib/Slicer-4.13/qt-scripted-modules, C:/Users/mohaas01/AppData/Roaming/NA-MIC/Extensions-29531/DCMQI/lib/Slicer-4.13/cli-modules<br>
[DEBUG][Python] 19.12.2020 00:14:00 [Python] (C:\Users\mohaas01\AppData\Local\NA-MIC\Slicer 4.13.0-2020-12-17\lib\Python\Lib\site-packages\pydicom\datadict.py:432) - Reversing DICOM dictionary so can look up tag from a keyword…<br>
[DEBUG][Python] 19.12.2020 00:14:02 [Python] (C:\Users\mohaas01\AppData\Local\NA-MIC\Slicer 4.13.0-2020-12-17\lib\Slicer-4.13\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 19.12.2020 00:14:03 [Python] (C:\Users\mohaas01\AppData\Local\NA-MIC\Slicer 4.13.0-2020-12-17\lib\Slicer-4.13\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 19.12.2020 00:14:03 [Python] (C:\Users\mohaas01\AppData\Local\NA-MIC\Slicer 4.13.0-2020-12-17\lib\Slicer-4.13\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 19.12.2020 00:14:04 [] (unknown:0) - Switch to module:  “Welcome”<br>
[DEBUG][Qt] 19.12.2020 00:14:23 [] (unknown:0) - Switch to module:  “DICOM”<br>
[DEBUG][Python] 19.12.2020 00:14:31 [Python] (C:\Users\mohaas01\AppData\Roaming\NA-MIC\Extensions-29531\QuantitativeReporting\lib\Slicer-4.13\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMParametricMapPluginClass : Caching files<br>
[DEBUG][Python] 19.12.2020 00:14:31 [Python] (C:\Users\mohaas01\AppData\Roaming\NA-MIC\Extensions-29531\QuantitativeReporting\lib\Slicer-4.13\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMParametricMapPluginClass : Using cached files<br>
[DEBUG][Python] 19.12.2020 00:14:31 [Python] (C:\Users\mohaas01\AppData\Roaming\NA-MIC\Extensions-29531\QuantitativeReporting\lib\Slicer-4.13\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMSegmentationPluginClass : Caching files<br>
[DEBUG][Python] 19.12.2020 00:14:31 [Python] (C:/Users/mohaas01/AppData/Roaming/NA-MIC/Extensions-29531/QuantitativeReporting/lib/Slicer-4.13/qt-scripted-modules/DICOMSegmentationPlugin.py:62) - DICOM SEG modality found<br>
[DEBUG][Python] 19.12.2020 00:14:31 [Python] (C:/Users/mohaas01/AppData/Roaming/NA-MIC/Extensions-29531/QuantitativeReporting/lib/Slicer-4.13/qt-scripted-modules/DICOMSegmentationPlugin.py:62) - DICOM SEG modality found<br>
[DEBUG][Python] 19.12.2020 00:14:31 [Python] (C:\Users\mohaas01\AppData\Roaming\NA-MIC\Extensions-29531\QuantitativeReporting\lib\Slicer-4.13\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMTID1500PluginClass : Caching files<br>
[ERROR][Python] 19.12.2020 00:14:31 [Python] (C:\Users\mohaas01\AppData\Roaming\NA-MIC\Extensions-29531\SlicerDevelopmentToolbox\lib\Slicer-4.13\qt-scripted-modules\SlicerDevelopmentToolboxUtils\mixins.py:729) - ‘FileDataset’ object has no attribute ‘SeriesDescription’<br>
[ERROR][Python] 19.12.2020 00:14:31 [Python] (C:\Users\mohaas01\AppData\Roaming\NA-MIC\Extensions-29531\SlicerDevelopmentToolbox\lib\Slicer-4.13\qt-scripted-modules\SlicerDevelopmentToolboxUtils\mixins.py:729) - ‘FileDataset’ object has no attribute ‘SeriesDescription’<br>
[DEBUG][Python] 19.12.2020 00:14:31 [Python] (C:\Users\mohaas01\AppData\Roaming\NA-MIC\Extensions-29531\QuantitativeReporting\lib\Slicer-4.13\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMTID1500PluginClass : Using cached files<br>
[CRITICAL][Stream] 19.12.2020 00:14:31 [] (unknown:0) - ‘FileDataset’ object has no attribute ‘SeriesDescription’<br>
[CRITICAL][Stream] 19.12.2020 00:14:31 [] (unknown:0) - ‘FileDataset’ object has no attribute ‘SeriesDescription’<br>
[DEBUG][Python] 19.12.2020 00:14:42 [Python] (C:/Users/mohaas01/AppData/Roaming/NA-MIC/Extensions-29531/QuantitativeReporting/lib/Slicer-4.13/qt-scripted-modules/DICOMSegmentationPlugin.py:83) - DICOM SEG load()<br>
[DEBUG][Python] 19.12.2020 00:14:42 [Python] (C:/Users/mohaas01/AppData/Roaming/NA-MIC/Extensions-29531/QuantitativeReporting/lib/Slicer-4.13/qt-scripted-modules/DICOMSegmentationPlugin.py:86) - in load(): uid = 1.3.12.2.1107.5.4.5.164007.30000020080308240198200000581<br>
[ERROR][Python] 19.12.2020 00:14:44 [Python] (C:/Users/mohaas01/AppData/Roaming/NA-MIC/Extensions-29531/QuantitativeReporting/lib/Slicer-4.13/qt-scripted-modules/DICOMSegmentationPlugin.py:119) - SEG2NRRD did not complete successfully, unable to load DICOM Segmentation<br>
[DEBUG][Python] 19.12.2020 00:14:44 [Python] (C:\Users\mohaas01\AppData\Roaming\NA-MIC\Extensions-29531\QuantitativeReporting\lib\Slicer-4.13\qt-scripted-modules\base\DICOMPluginBase.py:34) - Cleaning up temporarily created directory C:/Users/mohaas01/AppData/Local/Temp/Slicer\QIICR\SEG\2020-12-19_001442\1.3.12.2.1107.5.4.5.164007.30000020080308240198200000581<br>
[WARNING][Python] 19.12.2020 00:14:44 [Python] (C:\Users\mohaas01\AppData\Local\NA-MIC\Slicer 4.13.0-2020-12-17\bin\Python\slicer\util.py:1988) - Could not load: Unknown as a DICOMSegmentation<br>
[DEBUG][Qt] 19.12.2020 00:14:42 [] (unknown:0) - Found CommandLine Module, target is  C:/Users/mohaas01/AppData/Roaming/NA-MIC/Extensions-29531/DCMQI/lib/Slicer-4.13/cli-modules/segimage2itkimage.exe<br>
[DEBUG][Qt] 19.12.2020 00:14:42 [] (unknown:0) - ModuleType: CommandLineModule<br>
[DEBUG][Qt] 19.12.2020 00:14:42 [] (unknown:0) - Convert DICOM Segmentation Image into ITK image(s) command line:</p>
<p>C:/Users/mohaas01/AppData/Roaming/NA-MIC/Extensions-29531/DCMQI/lib/Slicer-4.13/cli-modules/segimage2itkimage.exe --inputDICOM D:/MyData/JikeiTumorSegmentation/DICOM-Original/OR5/MR1/Case3_MRI_pre/CASE3_MRI_PRE_1.SEG.0016.0001.2020_20200803_181121804_003330.IMA --outputDirectory C:/Users/mohaas01/AppData/Local/Temp/Slicer\QIICR\SEG\2020-12-19_001442\1.3.12.2.1107.5.4.5.164007.30000020080308240198200000581 --outputType nrrd<br>
[DEBUG][Qt] 19.12.2020 00:14:44 [] (unknown:0) - Convert DICOM Segmentation Image into ITK image(s) standard output:</p>
<p>dcmqi repository URL: git://github.com/QIICR/dcmqi.git revision: 99192b7 tag: latest<br>
[ERROR][VTK] 19.12.2020 00:14:44 [vtkSlicerCLIModuleLogic (0000020C1DF76560)] (D:\D\P\Slicer-0\Base\QTCLI\vtkSlicerCLIModuleLogic.cxx:2017) - Convert DICOM Segmentation Image into ITK image(s) standard error:</p>
<p>W: CodingSchemeDesignator (0008,0102) absent in CodeSequenceMacro (type 1)<br>
W: CodeMeaning (0008,0104) absent in CodeSequenceMacro (type 1)<br>
W: FrameOfReferenceUID (0020,0052) absent in FrameOfReferenceModule (type 1)<br>
W: DeviceSerialNumber (0018,1000) absent in EnhancedGeneralEquipmentModule (type 1)<br>
W: SegmentLabel (0062,0005) empty in SegmentDescriptionMacro (type 1)<br>
Plane Orientation (Patient) is missing, cannot parse input<br>
ERROR: Failed to get image directions!<br>
Fatal error encountered.<br>
[ERROR][VTK] 19.12.2020 00:14:44 [vtkSlicerCLIModuleLogic (0000020C1DF76560)] (D:\D\P\Slicer-0\Base\QTCLI\vtkSlicerCLIModuleLogic.cxx:2048) - Convert DICOM Segmentation Image into ITK image(s) completed with errors<br>
[CRITICAL][Stream] 19.12.2020 00:14:44 [] (unknown:0) - SEG2NRRD did not complete successfully, unable to load DICOM Segmentation<br>
[CRITICAL][Stream] 19.12.2020 00:14:44 [] (unknown:0) - Could not load: Unknown as a DICOMSegmentation<br>
[DEBUG][Qt] 19.12.2020 00:21:13 [] (unknown:0) - Switch to module:  “DICOMSegmentationPlugin”<br>
[DEBUG][Qt] 19.12.2020 00:21:13 [] (unknown:0) - Warning, there is no UI for the module “DICOMSegmentationPlugin”<br>
[DEBUG][Qt] 19.12.2020 00:21:29 [] (unknown:0) - Switch to module:  “Data”<br>
[DEBUG][Qt] 19.12.2020 00:21:42 [] (unknown:0) - Switch to module:  “DICOMSegmentationPlugin”<br>
[DEBUG][Qt] 19.12.2020 00:21:42 [] (unknown:0) - Warning, there is no UI for the module “DICOMSegmentationPlugin”<br>
[DEBUG][Qt] 19.12.2020 00:21:50 [] (unknown:0) - Switch to module:  “Data”<br>
[DEBUG][Qt] 19.12.2020 00:24:50 [] (unknown:0) - Switch to module:  “DICOM”<br>
[DEBUG][Python] 19.12.2020 00:24:54 [Python] (C:\Users\mohaas01\AppData\Local\NA-MIC\Slicer 4.13.0-2020-12-17\lib\Slicer-4.13\qt-scripted-modules\DICOMLib\DICOMUtils.py:673) - Examine for import using DICOMImageSequencePlugin<br>
[DEBUG][Python] 19.12.2020 00:24:54 [Python] (C:\Users\mohaas01\AppData\Local\NA-MIC\Slicer 4.13.0-2020-12-17\lib\Slicer-4.13\qt-scripted-modules\DICOMLib\DICOMUtils.py:673) - Examine for import using DICOMParametricMapPlugin<br>
[DEBUG][Python] 19.12.2020 00:24:54 [Python] (C:\Users\mohaas01\AppData\Roaming\NA-MIC\Extensions-29531\QuantitativeReporting\lib\Slicer-4.13\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMParametricMapPluginClass : Using cached files<br>
[DEBUG][Python] 19.12.2020 00:24:54 [Python] (C:\Users\mohaas01\AppData\Roaming\NA-MIC\Extensions-29531\QuantitativeReporting\lib\Slicer-4.13\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMParametricMapPluginClass : Using cached files<br>
[DEBUG][Python] 19.12.2020 00:24:54 [Python] (C:\Users\mohaas01\AppData\Local\NA-MIC\Slicer 4.13.0-2020-12-17\lib\Slicer-4.13\qt-scripted-modules\DICOMLib\DICOMUtils.py:673) - Examine for import using DICOMScalarVolumePlugin<br>
[DEBUG][Python] 19.12.2020 00:24:54 [Python] (C:\Users\mohaas01\AppData\Local\NA-MIC\Slicer 4.13.0-2020-12-17\lib\Slicer-4.13\qt-scripted-modules\DICOMLib\DICOMUtils.py:673) - Examine for import using DICOMSegmentationPlugin<br>
[DEBUG][Python] 19.12.2020 00:24:54 [Python] (C:\Users\mohaas01\AppData\Roaming\NA-MIC\Extensions-29531\QuantitativeReporting\lib\Slicer-4.13\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMSegmentationPluginClass : Using cached files<br>
[DEBUG][Python] 19.12.2020 00:24:54 [Python] (C:\Users\mohaas01\AppData\Local\NA-MIC\Slicer 4.13.0-2020-12-17\lib\Slicer-4.13\qt-scripted-modules\DICOMLib\DICOMUtils.py:673) - Examine for import using DICOMSlicerDataBundlePlugin<br>
[DEBUG][Python] 19.12.2020 00:24:54 [Python] (C:\Users\mohaas01\AppData\Local\NA-MIC\Slicer 4.13.0-2020-12-17\lib\Slicer-4.13\qt-scripted-modules\DICOMLib\DICOMUtils.py:673) - Examine for import using DICOMTID1500Plugin<br>
[DEBUG][Python] 19.12.2020 00:24:54 [Python] (C:\Users\mohaas01\AppData\Roaming\NA-MIC\Extensions-29531\QuantitativeReporting\lib\Slicer-4.13\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMTID1500PluginClass : Using cached files<br>
[DEBUG][Python] 19.12.2020 00:24:54 [Python] (C:\Users\mohaas01\AppData\Roaming\NA-MIC\Extensions-29531\QuantitativeReporting\lib\Slicer-4.13\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMTID1500PluginClass : Using cached files<br>
[DEBUG][Python] 19.12.2020 00:24:54 [Python] (C:\Users\mohaas01\AppData\Local\NA-MIC\Slicer 4.13.0-2020-12-17\lib\Slicer-4.13\qt-scripted-modules\DICOMLib\DICOMUtils.py:673) - Examine for import using DICOMVolumeSequencePlugin<br>
[DEBUG][Python] 19.12.2020 00:24:54 [Python] (C:\Users\mohaas01\AppData\Local\NA-MIC\Slicer 4.13.0-2020-12-17\lib\Slicer-4.13\qt-scripted-modules\DICOMLib\DICOMUtils.py:673) - Examine for import using DicomRtImportExportPlugin<br>
[DEBUG][Python] 19.12.2020 00:24:54 [Python] (C:\Users\mohaas01\AppData\Local\NA-MIC\Slicer 4.13.0-2020-12-17\lib\Slicer-4.13\qt-scripted-modules\DICOMLib\DICOMUtils.py:673) - Examine for import using DicomSroImportExportPlugin<br>
[DEBUG][Python] 19.12.2020 00:24:55 [Python] (C:\Users\mohaas01\AppData\Local\NA-MIC\Slicer 4.13.0-2020-12-17\lib\Slicer-4.13\qt-scripted-modules\DICOMLib\DICOMUtils.py:673) - Examine for import using MultiVolumeImporterPlugin<br>
[DEBUG][Python] 19.12.2020 00:24:55 [Python] (C:/Users/mohaas01/AppData/Local/NA-MIC/Slicer 4.13.0-2020-12-17/bin/…/lib/Slicer-4.13/qt-scripted-modules/MultiVolumeImporterPlugin.py:472) - MultiVolumeImporterPlugin: examine<br>
[DEBUG][Python] 19.12.2020 00:24:55 [Python] (C:/Users/mohaas01/AppData/Local/NA-MIC/Slicer 4.13.0-2020-12-17/bin/…/lib/Slicer-4.13/qt-scripted-modules/MultiVolumeImporterPlugin.py:513) - MultiVolumeImporterPlugin: found 1 multivolumes!<br>
[DEBUG][Python] 19.12.2020 00:24:55 [Python] (C:/Users/mohaas01/AppData/Local/NA-MIC/Slicer 4.13.0-2020-12-17/bin/…/lib/Slicer-4.13/qt-scripted-modules/MultiVolumeImporterPlugin.py:181) - MultiVolumeImporterPlugin: examineMultiseries<br>
[DEBUG][Python] 19.12.2020 00:24:55 [Python] (C:/Users/mohaas01/AppData/Local/NA-MIC/Slicer 4.13.0-2020-12-17/bin/…/lib/Slicer-4.13/qt-scripted-modules/MultiVolumeImporterPlugin.py:188) - MultiVolumeImporterPlugin: found 0 multivolumes!<br>
[DEBUG][Python] 19.12.2020 00:24:55 [Python] (C:/Users/mohaas01/AppData/Local/NA-MIC/Slicer 4.13.0-2020-12-17/bin/…/lib/Slicer-4.13/qt-scripted-modules/MultiVolumeImporterPlugin.py:169) - MultiVolumeImporterPlugin: found 0 loadables in 2 files in 0.0sec.<br>
[DEBUG][Python] 19.12.2020 00:24:59 [Python] (C:/Users/mohaas01/AppData/Roaming/NA-MIC/Extensions-29531/QuantitativeReporting/lib/Slicer-4.13/qt-scripted-modules/DICOMSegmentationPlugin.py:83) - DICOM SEG load()<br>
[DEBUG][Python] 19.12.2020 00:24:59 [Python] (C:/Users/mohaas01/AppData/Roaming/NA-MIC/Extensions-29531/QuantitativeReporting/lib/Slicer-4.13/qt-scripted-modules/DICOMSegmentationPlugin.py:86) - in load(): uid = 1.3.12.2.1107.5.4.5.164007.30000020080308240198200000581<br>
[ERROR][Python] 19.12.2020 00:25:00 [Python] (C:/Users/mohaas01/AppData/Roaming/NA-MIC/Extensions-29531/QuantitativeReporting/lib/Slicer-4.13/qt-scripted-modules/DICOMSegmentationPlugin.py:119) - SEG2NRRD did not complete successfully, unable to load DICOM Segmentation<br>
[DEBUG][Python] 19.12.2020 00:25:00 [Python] (C:\Users\mohaas01\AppData\Roaming\NA-MIC\Extensions-29531\QuantitativeReporting\lib\Slicer-4.13\qt-scripted-modules\base\DICOMPluginBase.py:34) - Cleaning up temporarily created directory C:/Users/mohaas01/AppData/Local/Temp/Slicer\QIICR\SEG\2020-12-19_001442\1.3.12.2.1107.5.4.5.164007.30000020080308240198200000581<br>
[WARNING][Python] 19.12.2020 00:25:00 [Python] (C:\Users\mohaas01\AppData\Local\NA-MIC\Slicer 4.13.0-2020-12-17\bin\Python\slicer\util.py:1988) - Could not load: Unknown as a DICOMSegmentation<br>
[DEBUG][Qt] 19.12.2020 00:24:59 [] (unknown:0) - Found CommandLine Module, target is  C:/Users/mohaas01/AppData/Roaming/NA-MIC/Extensions-29531/DCMQI/lib/Slicer-4.13/cli-modules/segimage2itkimage.exe<br>
[DEBUG][Qt] 19.12.2020 00:24:59 [] (unknown:0) - ModuleType: CommandLineModule<br>
[DEBUG][Qt] 19.12.2020 00:24:59 [] (unknown:0) - Convert DICOM Segmentation Image into ITK image(s) command line:</p>
<p>C:/Users/mohaas01/AppData/Roaming/NA-MIC/Extensions-29531/DCMQI/lib/Slicer-4.13/cli-modules/segimage2itkimage.exe --inputDICOM D:/MyData/JikeiTumorSegmentation/DICOM-Original/OR5/MR1/Case3_MRI_pre/CASE3_MRI_PRE_1.SEG.0016.0001.2020_20200803_181121804_003330.IMA --outputDirectory C:/Users/mohaas01/AppData/Local/Temp/Slicer\QIICR\SEG\2020-12-19_001442\1.3.12.2.1107.5.4.5.164007.30000020080308240198200000581 --outputType nrrd<br>
[DEBUG][Qt] 19.12.2020 00:25:00 [] (unknown:0) - Convert DICOM Segmentation Image into ITK image(s) standard output:</p>
<p>dcmqi repository URL: git://github.com/QIICR/dcmqi.git revision: 99192b7 tag: latest<br>
[ERROR][VTK] 19.12.2020 00:25:00 [vtkSlicerCLIModuleLogic (0000020C1DF76560)] (D:\D\P\Slicer-0\Base\QTCLI\vtkSlicerCLIModuleLogic.cxx:2017) - Convert DICOM Segmentation Image into ITK image(s) standard error:</p>
<p>W: CodingSchemeDesignator (0008,0102) absent in CodeSequenceMacro (type 1)<br>
W: CodeMeaning (0008,0104) absent in CodeSequenceMacro (type 1)<br>
W: FrameOfReferenceUID (0020,0052) absent in FrameOfReferenceModule (type 1)<br>
W: DeviceSerialNumber (0018,1000) absent in EnhancedGeneralEquipmentModule (type 1)<br>
W: SegmentLabel (0062,0005) empty in SegmentDescriptionMacro (type 1)<br>
Plane Orientation (Patient) is missing, cannot parse input<br>
ERROR: Failed to get image directions!<br>
Fatal error encountered.<br>
[ERROR][VTK] 19.12.2020 00:25:00 [vtkSlicerCLIModuleLogic (0000020C1DF76560)] (D:\D\P\Slicer-0\Base\QTCLI\vtkSlicerCLIModuleLogic.cxx:2048) - Convert DICOM Segmentation Image into ITK image(s) completed with errors<br>
[CRITICAL][Stream] 19.12.2020 00:25:00 [] (unknown:0) - SEG2NRRD did not complete successfully, unable to load DICOM Segmentation<br>
[CRITICAL][Stream] 19.12.2020 00:25:00 [] (unknown:0) - Could not load: Unknown as a DICOMSegmentation</p>

---

## Post #5 by @lassoan (2020-12-18 16:50 UTC)

<p>Thank you for the logs.  The relevant part of this:</p>
<pre><code class="lang-auto">W: CodingSchemeDesignator (0008,0102) absent in CodeSequenceMacro (type 1)
W: CodeMeaning (0008,0104) absent in CodeSequenceMacro (type 1)
W: FrameOfReferenceUID (0020,0052) absent in FrameOfReferenceModule (type 1)
W: DeviceSerialNumber (0018,1000) absent in EnhancedGeneralEquipmentModule (type 1)
W: SegmentLabel (0062,0005) empty in SegmentDescriptionMacro (type 1)
Plane Orientation (Patient) is missing, cannot parse input
ERROR: Failed to get image directions!
</code></pre>
<p>The segmentation file has several errors. Several Type 1 (required) DICOM fields are missing, but the reader is quite robust so it could recover from most of these. However, the last straw is that even <a href="http://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.7.6.16.2.html#sect_C.7.6.16.2.4">Plane Orientation (Patient)</a> tag is missing.</p>
<p>What software was used to create this segmentation?</p>

---

## Post #6 by @issakomi (2020-12-18 19:48 UTC)

<p>SEG modality could be “Surface Segmentation Storage” too, mesh, some Siemens workstations can export meshes in that SOP Class directly. Just guessing, of course, i didn’t find SOP Class in debug output. If it is mesh  - 0x0008, 0x0016 tag has a value “1.2.840.10008.5.1.4.1.1.66.5”.</p>
<p>P.S. If it is such mesh file, may be that <a href="https://gist.github.com/issakomi/29e48917e77201f2b73bfa5fe7b30451" rel="noopener nofollow ugc">script</a> can work.</p>

---

## Post #8 by @pieper (2020-12-18 21:57 UTC)

<p>Thanks for reporting <a class="mention" href="/u/issakomi">@issakomi</a> - Slicer’s vtk should behave the same as the debian version and I’m curious why it doesn’t.</p>
<p>Is it possible for you to provide a sample dataset that illustrates this issue?</p>

---

## Post #10 by @AshrafM (2020-12-18 23:01 UTC)

<p>Thanks, everyone for your replies.<br>
The issue is different from what Issakomi described. The file I have is not a surface segmentation storage.  The file posted by Issakomi is not relevant to my issue.</p>
<p>The segmentation I have was generated by “syngo 3D Segmentation” tool on the Siemens workstation. I see that it is missing Plane Orientation (Patient) tag. I believe it is referring to the original image (non-segmented) DICOM file where this information is. Perhaps that is how this segmentation file works. I can re-load everything back from DICOM onto the Siemens workstation successfully. So the files are not corrupted.</p>
<p>While I am still having issues, a good sign is that I was able to read some segmentation files with pynrrd,  convert into nrrd, then glue  header info from the original (non-segmented) image nrrd onto the segmented image nrrd generated by pynrrd. This worked for some images (especially with square matrix size, like 512 x 512), but not others. Specifically, the one below (segmentation of MR images) are still not possible to load even with this work around.</p>
<p>I would appreciate any ideas, even if it involves manual conversion with another tool before loading into slicer as nrrd.</p>
<p>Here is a link to a sample file <a href="https://drive.google.com/file/d/1HBhlDnSDVJUJE9kAXK_qqnV14QLeSFNj/view?usp=sharing" rel="noopener nofollow ugc">HERE</a>.</p>

---

## Post #11 by @lassoan (2020-12-18 23:14 UTC)

<p>The file does not seem to be DICOM compliant. Siemens software developers made a questionable decision to accept such images in their DICOM reader. Or maybe they thought that this field is optional (and that’s why they missed it in their DICOM exporter, too).</p>
<p><a class="mention" href="/u/david_clunie">@David_Clunie</a> Do you have any comment on this? Are you aware of this potential non-compliance of Siemens "syngo 3D Segmentation” tool?</p>

---

## Post #12 by @pieper (2020-12-19 00:06 UTC)

<p><a class="mention" href="/u/fedorov">@fedorov</a> also has some experience with this issue.</p>

---

## Post #14 by @issakomi (2020-12-19 20:58 UTC)

<p>Played again with the puzzle and got better result. <a href="https://drive.google.com/file/d/18T1NIvd5pXcxQG3xQlLBvjxK5OPDXq_C/view?usp=sharing" rel="noopener nofollow ugc">MHA file</a><br>
Having referenced images is possible to do it clean (dimensions,origin, orientation, spacing, etc.)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a89ff068a2aed7e855cfdf5e0df7a1014079bb8d.png" data-download-href="/uploads/short-url/o3ISK8mVdZctnmpIkhMRISrqRBz.png?dl=1" title="Screenshot at 2020-12-19 21-50-17" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a89ff068a2aed7e855cfdf5e0df7a1014079bb8d_2_690x452.png" alt="Screenshot at 2020-12-19 21-50-17" data-base62-sha1="o3ISK8mVdZctnmpIkhMRISrqRBz" width="690" height="452" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a89ff068a2aed7e855cfdf5e0df7a1014079bb8d_2_690x452.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a89ff068a2aed7e855cfdf5e0df7a1014079bb8d_2_1035x678.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a89ff068a2aed7e855cfdf5e0df7a1014079bb8d.png 2x" data-dominant-color="B8B9D6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot at 2020-12-19 21-50-17</span><span class="informations">1224×803 93.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<pre><code class="lang-auto">#include &lt;fstream&gt;
#include &lt;vector&gt;
#include &lt;cstring&gt;
#include &lt;cstdlib&gt;
#include &lt;cstdint&gt;
#include &lt;iostream&gt;

int main(int, char**)
{
  char * data1 = new char[(284*320*192)/8];
  // input is raw binary data from 0x7fe0, 0x0010
  std::ifstream file("binary.bin", std::ios::in | std::ios::binary);
  file.read(data1, (284*320*192)/8);
  file.close();
  unsigned char * data2 = new unsigned char[284*320*192];
  size_t count_data2 = 0;
  for (size_t x = 0; x &lt; (284*320*192)/8; x++)
  {
    const unsigned char c = data1[x];
    data2[count_data2 + 0] = (c &amp; 0x01) ? 255 : 0;
    data2[count_data2 + 1] = (c &amp; 0x02) ? 255 : 0;
    data2[count_data2 + 2] = (c &amp; 0x04) ? 255 : 0;
    data2[count_data2 + 3] = (c &amp; 0x08) ? 255 : 0;
    data2[count_data2 + 4] = (c &amp; 0x10) ? 255 : 0;
    data2[count_data2 + 5] = (c &amp; 0x20) ? 255 : 0;
    data2[count_data2 + 6] = (c &amp; 0x40) ? 255 : 0;
    data2[count_data2 + 7] = (c &amp; 0x80) ? 255 : 0;
    count_data2 += 8;
  }
  std::cout &lt;&lt; "count_data2=" &lt;&lt; count_data2 &lt;&lt; std::endl;
  std::ofstream out_file("out_data.raw", std::ios::out | std::ios::binary);
#if 0
  out_file.write((char*)data2, 284*320*192);
#else
  const size_t out_x = 288;
  const size_t out_y = 320;
  char * data3 = new char[out_x*out_y*192];
  std::memset(data3, 0, out_x*out_y*192);
  //std::memcpy(&amp;data3[(out_x*out_y*192) - (284*320*192)], data2, 284*320*192);
  std::memcpy(&amp;data3[0], data2, 284*320*192);
  out_file.write((char*)data3, out_x*out_y*192);
#endif
  out_file.close();
  delete [] data2;
  delete [] data3;
  return 0;
}
</code></pre>
<p><strong>Edit</strong>:<br>
<a href="https://drive.google.com/file/d/1KefpgcLuNQ2W4YIQ1IRho_W7kxD949gY/view?usp=sharing" rel="noopener nofollow ugc">Here</a> is that raw binary data (input for code above) and MetaIO header (for mhd/raw):</p>
<pre><code class="lang-auto">ObjectType = Image
NDims = 3
BinaryData = True
BinaryDataByteOrderMSB = False
CompressedData = False
TransformMatrix = 1 0 0 0 1 0 0 0 1
Offset = 0 0 0
CenterOfRotation = 0 0 0
AnatomicalOrientation = RAI
ElementSpacing = 1 1 1
DimSize = 288 320 192
ElementType = MET_UCHAR
ElementDataFile = out_data.raw
</code></pre>

---

## Post #15 by @AshrafM (2020-12-20 01:45 UTC)

<p>Many thanks, <a class="mention" href="/u/issakomi">@issakomi</a> . You actually did solve the puzzle! I converted into nrrd and added the correct header info from the nrrd of the original MR image. FYI, if you are interested, the result is <a href="https://drive.google.com/file/d/1wYG7j32bm6vrjnE3w9k7cBsFlJRyXcIE/view?usp=sharing" rel="noopener nofollow ugc">here</a>.</p>
<p>The segmented tumor now is perfectly aligned with the tumor on the original image. Great!</p>
<p>As I have around 20-30 more files with the same issue, let me try to confirm a couple of points so that I can repeat what you did for the other files. I have not checked yet whether all have the same matrix size exactly (the few I checked so far do have the same matrix size)</p>
<ul>
<li>
<p>It seems your code is mainly converting to uchar and padding the size from 284 to 288, keeping the other matrix sizes the same. How did you figure out the padding from 284 to 288? The next higher number divisible by 8?</p>
</li>
<li>
<p>How did you get the binary.bin file from the .IMA? Did you just extract the pixel data from the DICOM file directly?<br>
Which program did you use? I have not done any significant DICOM manipulation and coding in over 12 years. I would appreciate if you could point me in the right direction (e.g., which library or tools did you use to get binary.bin from .IMA?)</p>
</li>
</ul>
<p>Now that it seems that Issakomi figured out how to read that segmentation file, it would be helpful if there is a way to read the DICOM directly into Slicer in the future. Not sure that would be easy to implement, but perhaps others may find it useful to load these segmentation files.</p>
<p>Very helpful community.<br>
Thank you.</p>

---

## Post #16 by @lassoan (2020-12-20 02:39 UTC)

<aside class="quote no-group" data-username="AshrafM" data-post="15" data-topic="15134">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/0ea827/48.png" class="avatar"> AshrafM:</div>
<blockquote>
<p>Now that it seems that Issakomi figured out how to read that segmentation file, it would be helpful if there is a way to read the DICOM directly into Slicer in the future</p>
</blockquote>
</aside>
<p>My understanding is that this is a seriously flawed DICOM file (<a class="mention" href="/u/fedorov">@fedorov</a> and <a class="mention" href="/u/david_clunie">@David_Clunie</a> need to confirm). By giving in and just silently accepting DICOM implementation errors that manufacturers make (especially if it is a big one, such as Siemens), we would do a disservice to the medical imaging community: we would damage credibility of the DICOM standard, make DICOM readers more complicated (by adding manufacturer-specific workarounds), and increase the risk that data sets are interpreted incorrectly.</p>
<p>Depending on what I hear back from the DICOM experts, we may add a rule to the DICOM patcher module to fix up these files.</p>

---

## Post #17 by @fedorov (2020-12-20 03:16 UTC)

<p>I agree with Andras - it appears that this file has a lot of issues, and it is also not possible to properly interpret this file without access to the referenced MR images from which the segmentation was created. In my opinion, this is an example of a dataset where you unfortunately need to write a custom code to make sense out of it. I don’t think such code belongs to Slicer, since this type of data is very uncommon, vendor-specific (more precisely, specific to a certain product line from a vendor), and I agree with Andras arguments.</p>
<p><a class="mention" href="/u/ashrafm">@AshrafM</a> were you using a recent version of Siemens Artis to create that object? Can you, or whoever created this object, report the issue to the technical support of the product? Siemens Artis team could be pointed out that Siemens syngo.via team are able to produce valid DICOM segmentation objects, so why can’t Artis?</p>
<p><a class="mention" href="/u/issakomi">@issakomi</a> one of your earlier posts (now deleted) had a very different rendering that looked more like a surface mesh. Was it this example file, or something else? What you are showing in your most recent screenshot is very different.</p>

---

## Post #20 by @AshrafM (2020-12-20 13:42 UTC)

<p><a class="mention" href="/u/fedorov">@fedorov</a> and <a class="mention" href="/u/lassoan">@lassoan</a> .  I understand it is an issue of compliance with the DICOM standard.</p>
<p>The files were generated using a recent version of the Artis system. I will see if I can reach to the Artis technical support on this. It is  good to get to the bottom of the issue quickly and glad that <a class="mention" href="/u/issakomi">@issakomi</a>  provided a work around. Thank you both for your quick feedback.</p>
<p><a class="mention" href="/u/issakomi">@issakomi</a> Thank you very much for your help with this. I was able to extract the pixel data using pydicom and save it as a binary file, then your code takes over.<br>
I guess the multiples of 8 size here is because the segmentation is stored in 1 bit per pixel in the DICOM file, so they had to pad to make it divisible by 8 for storage in bytes.</p>
<p>Things seem to be smooth from here forward, but if I run into issues, I might pick up this thread again.</p>
<p>Thank you very much.</p>

---

## Post #21 by @David_Clunie (2020-12-20 17:35 UTC)

<p>I agree with <a class="mention" href="/u/issakomi">@issakomi</a> that the fundamental error Siemens seems may have made is to encode the wrong value for Columns in the DICOM attributes.</p>
<p>If one patches the DICOM SEG file to have:</p>
<ul>
<li>a Columns of 288 instead of 284</li>
<li>changes the value length of PixelData from  320x284x192/8 2181120 (0x214800) to  320x288x192/8=2211840 (0x21C000)</li>
<li>adds 320x(288-284)x192/8 = 30720 bytes of null to the end of PixelData</li>
</ul>
<p>then the SEG at least displays OK in its binary form - I don’t have the source DICOM images to attempt to overly this on to see if the positioning is actually correct.</p>
<p>There are also some other issues with the DICOM attributes that dciodvfy exposes (such as the DimensionIndexValue numbers being wrong, InStackPositionNumber and SegmentNumber not starting from 1, malformed ProcedureCodeSequence), but these don’t prevent use of the pixel data array.</p>
<p>I will mention it to Siemens DICOM colleagues</p>
<p>David</p>

---

## Post #22 by @fedorov (2020-12-20 23:23 UTC)

<aside class="quote no-group quote-post-not-found" data-username="issakomi" data-post="18" data-topic="15134">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/i/b9e5f3/48.png" class="avatar"> issakomi:</div>
<blockquote>
<p>Yes, it is surface mesh.</p>
</blockquote>
</aside>
<p>I am afraid I am not following the conversation. I downloaded the sample file from this link <a href="https://drive.google.com/file/d/1HBhlDnSDVJUJE9kAXK_qqnV14QLeSFNj/view" class="inline-onebox">CASE3_MRI_PRE_1.SEG.0016.0002.2020_20200730_103640831_003331.IMA - Google Drive</a> posted by <a class="mention" href="/u/ashrafm">@AshrafM</a>, and that file does not have SurfaceSequence, and has SOPClassUID = 1.2.840.10008.5.1.4.1.1.66.4 (Segmentation IOD, not Surface Segmentation IOD). Was I looking at a wrong file?</p>

---

## Post #23 by @lassoan (2020-12-20 23:44 UTC)

<p>The problem is with the DICOM file that <a class="mention" href="/u/ashrafm">@AshrafM</a> shared, with Segmentation IOD.</p>
<p>The surface segmentation discussion was just a side topic, you can ignore that (it was brought up because at that point we did not have the failing file, just speculated that it could be a surface segmentation).</p>

---

## Post #24 by @issakomi (2020-12-21 01:42 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="22" data-topic="15134">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>I am afraid I am not following the conversation.</p>
</blockquote>
</aside>
<p>With “Yes, it is surface mesh” i meant screenshots in deleted post, you asked about it. I deleted to avoid confusion, but it happened. As Andras Lasso have written, it was a speculation before we got link to failing file. Sorry, my fault.</p>

---

## Post #25 by @David_Clunie (2020-12-21 11:38 UTC)

<p>By the way, another problem with this SEG file is that it is not 3D.</p>
<p>I.e., it does not have a frame of reference (UID) and does not specify a 3D orientation or 3D positions per slice (nor for that matter pixel spacing information).</p>
<p>Rather, for each slice, it references the original image that slice is to be applied to (and a 1:1 pixel correspondence is specified).</p>
<p>That is not really the way the SEG IOD was intended to be used with 3D cross-sectional modalities, but it is valid (which is why dciodvfy doesn’t complain about missing Frame of Reference UID, Pixel Measures Sequence &gt; Pixel Spacing, Plane Position Sequence &gt; Image Position (Patient), Plane Orientation Sequence &gt; Image Orientation (Patient)); see:</p>
<p><a href="http://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_A.51.5.html#sect_A.51.5.1" rel="noopener nofollow ugc">http://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_A.51.5.html#sect_A.51.5.1</a></p>
<p>AFAIK, 3DSlicer only supports the “Frame of Reference relative” approach, and not the “corresponding pixel in a referenced image” approach (which was intended for projection X-rays and photographs, etc.), so even if Siemens had encoded Columns to match PixelData, it still wouldn’t work with this SEG instance.</p>
<p>To work around this, you could copy in the corresponding attributes and values from the referenced slices as a pre-processing step.</p>
<p>A corollary of this may be that fixing Columns to match PixelData (rather than fixing PixelData to match Columns) is that the result will no longer match the referenced images (which I haven’t seen), which would no longer be valid per the standard.</p>
<p>David</p>
<p>PS. Strangely, in the top level data set (as opposed to per-frame functional group item) Source Image Sequence, Siemens says Spatial Locations Preserved = “NO”, which is rather contradictory, since the whole point of the “corresponding pixel in a referenced image” approach is that spatial locations are consistent (since they are not communicated in any other way than by reference). I.e., this value should “YES” IMHO, if sent at all (which it does not need to be, nor indeed does Source Image Sequence  in the top level data set).</p>

---

## Post #26 by @bjorn (2020-12-21 13:55 UTC)

<p>I would be happy to have our R&amp;D group responsible for the Artis software looking into this in detail.</p>
<p>Could you supply me with the original 3D data set / MRI volume?</p>
<p>As noted in the thread, the software copies attributed one to one from the original images into the Surface IOD. Therefore it is necessary to have the original data to troubleshoot efficiently.</p>

---

## Post #27 by @issakomi (2020-12-21 14:45 UTC)

<p>Thank you very much.<br>
For clarity, many programs with support for <em>SINGLEBIT</em> data (tried PixelMed, MircoDicom, Weasis, Aliza) can open that file standalone (setting spacing, origin, etc. to defaults).<br>
It looks like this (<strong>284</strong>x320x192), here slice <span class="hashtag">#128</span> (<em>PixelMed</em>, the same in other programs)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/29bc9217be7ec3dc87d2399b783144e3cc2d88a6.png" data-download-href="/uploads/short-url/5XdAoNonkICUpn8VHcNMpwLDzlc.png?dl=1" title="Screenshot at 2020-12-21 13-18-06" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/29bc9217be7ec3dc87d2399b783144e3cc2d88a6_2_690x486.png" alt="Screenshot at 2020-12-21 13-18-06" data-base62-sha1="5XdAoNonkICUpn8VHcNMpwLDzlc" width="690" height="486" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/29bc9217be7ec3dc87d2399b783144e3cc2d88a6_2_690x486.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/29bc9217be7ec3dc87d2399b783144e3cc2d88a6.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/29bc9217be7ec3dc87d2399b783144e3cc2d88a6.png 2x" data-dominant-color="7E7F80"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot at 2020-12-21 13-18-06</span><span class="informations">928×654 40.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Here is how it looks like after manually solving the puzzle, <strong>288</strong>x320x192, same slice</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f2b02a8718e3aead3d78f678eab999398141ecc.png" alt="20201221-130319" data-base62-sha1="fRr9cZdicdo8IwGeTUQcbIbaSq8" width="440" height="445"></p>
<p>Were also interested to see referenced images or at least know dimensions.</p>

---

## Post #28 by @AshrafM (2020-12-22 08:50 UTC)

<p>Thank you all for your comments.</p>
<p>As for the MR images, I am not able to provide the original images without further processing. The data comes from  clinical collaborators working on a confidential brain imaging project, with the data not yet published. I do not have their permission to share the data. Another concern is that, although the  metadata is already anonymized, with these MR head datasets, it is possible to reconstruct the facial features, which can violate the GDPR !</p>
<p>Would pydicom or another tool be able to zero out the pixel data and save the files without any changes to the DICOM metadata? If so, then I can send such cleaned out data. If you have experience with this on pydicom or another library, let me know. I could try it myself in a couple of days, but I have no experience which tool can clean up the pixel data while keeping the meta data untouched.  Any ideas? Thanks.</p>

---

## Post #29 by @bjorn (2020-12-22 10:14 UTC)

<p><a class="mention" href="/u/ashrafm">@AshrafM</a> I understand your valid concern. It would be great if you could dump the MR images as anonymized TEXT files. It should be sufficient for the analysis.</p>
<p>You can do this with mDicom (MicroDicom Viewer) for example. Under the file menu you can export a whole study or series as TEXT files. That would be one way of omitting pixel data.</p>
<p>Screenshot of “Export as text”</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/31457cdcf6e145b653f4ffda075cb3983d086876.png" data-download-href="/uploads/short-url/71SgUSNfMseKiUqv1zI79fIBeIu.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/31457cdcf6e145b653f4ffda075cb3983d086876.png" alt="image" data-base62-sha1="71SgUSNfMseKiUqv1zI79fIBeIu" width="676" height="500" data-dominant-color="C1C2C3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">782×578 44 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Screenshot of “Select source” and “Create subfolders”</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c47d500cb08456dc2a99f05d9fe4fbf9e24ae3d8.png" alt="image" data-base62-sha1="s2e43sr8i6kdFy8PZBQOdfFqiec" width="334" height="254"></p>

---

## Post #30 by @lassoan (2020-12-22 17:48 UTC)

<p>In Slicer, you can export all DICOM metadata of all the selected patients/studies/series from the DICOM browser:</p>
<ul>
<li>right-click in the DICOM browser</li>
<li>choose “View DICOM metadata…”</li>
<li>click “Copy all files metadata” (may take a couple of seconds to complete if you selected hundreds of files)</li>
<li>paste it into a text file</li>
</ul>

---

## Post #31 by @AshrafM (2020-12-25 19:59 UTC)

<p>Thank you for your suggestions. I wrote some code with pydicom to replace the pixel data with an ellipsoid, while trying to keep everything else in the dicom unchanged. I also extracted he DICOM meta data via both Slicer and mDICOM and I am providing the text files here.</p>
<ul>
<li><a href="https://drive.google.com/file/d/1BJw7I8r1VWtMVzBPqalvPa4Le7fiv5Jm/view?usp=sharing" rel="noopener nofollow ugc">DICOM images with pixel data replaced by an ellipsoid.</a></li>
<li><a href="https://drive.google.com/file/d/1iF2TZ-R3Lfw6YVvYjCpBy_8yi4-0t8GQ/view?usp=sharing" rel="noopener nofollow ugc">Metadata text file for the original MR images obtained using Slicer</a></li>
<li><a href="https://drive.google.com/file/d/1Z2pChk5YHOj6r6Ey_RfOesdw1WiUdBPm/view?usp=sharing" rel="noopener nofollow ugc">DICOM dump as text using mDICOM</a></li>
<li><a href="https://drive.google.com/file/d/1HBhlDnSDVJUJE9kAXK_qqnV14QLeSFNj/view?usp=sharing" rel="noopener nofollow ugc">Original DICOM image for segmentation (cannot be loaded in slicer).</a></li>
<li>
<a href="https://drive.google.com/file/d/1l51KkngQ9X_aaQPtRS2PQ1mD5BLzynAR/view?usp=sharing" rel="noopener nofollow ugc">Segmentation file after converting to nrrd</a> (using the code sent by <a class="mention" href="/u/issakomi">@issakomi</a> , converting to nrrd and copying some header information from nrrd of the MRI images).</li>
</ul>
<p>I hope it helps.<br>
Thanks.</p>

---

## Post #32 by @bjorn (2020-12-28 23:14 UTC)

<p>Thank you <a class="mention" href="/u/ashrafm">@AshrafM</a>, I got your data extraction from the links. Great preparation for an analysis. <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=9" title=":grinning:" class="emoji" alt=":grinning:"></p>
<p>I will get your extractions to the development team. Due to XMas and New Year, I am not sure how fast they can react and analyze.</p>
<p>One possible problem could be that the algorithm assumes rows to be a multiple of 16.</p>
<p>I will get back in this thread, when I have more info from the analysis.</p>

---

## Post #33 by @bjorn (2021-03-22 13:34 UTC)

<p>The development team has completed the analysis and implemented the necessary changes. The prototype has been successfully tested.</p>
<p>I will inform further as I get the information of which versions and software will be updated.</p>

---

## Post #34 by @bjorn (2021-04-06 07:03 UTC)

<p>Siemens Healthineers’ current plan is to solve this problem in the upcoming Artis VE22 software.</p>
<p>The rows and columns mismatch behavior has been corrected.</p>
<p>Note:<br>
“Corresponding pixel in a referenced image“ approach is used over the “frame of reference image” approach.</p>
<p>Potentially 3DSlicer can’t currently handle both these valid approaches.</p>

---

## Post #35 by @fedorov (2021-04-06 12:33 UTC)

<p>Bjorn, would it be possible to share a sample of the segmentation that is expected to be produced by the upcoming Artis VE22 software?</p>

---
