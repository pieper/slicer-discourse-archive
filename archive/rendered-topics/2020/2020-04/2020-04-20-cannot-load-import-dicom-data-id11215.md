# Cannot load/import Dicom data

**Topic ID**: 11215
**Date**: 2020-04-20
**URL**: https://discourse.slicer.org/t/cannot-load-import-dicom-data/11215

---

## Post #1 by @tnmd33 (2020-04-20 19:12 UTC)

<p>Problem report for Slicer 4.10.2 win-amd64: Hi, I’m new to 3D slicer, I wanted to import DICOM data from a CT but got this error that I don’t understand, this is from the log file:</p>
<p>[DEBUG][Qt] 20.04.2020 20:40:06 [] (unknown:0) - Session start time …: 2020-04-20 20:40:06<br>
[DEBUG][Qt] 20.04.2020 20:40:06 [] (unknown:0) - Slicer version …: 4.10.2 (revision 28257) win-amd64 - installed release<br>
[DEBUG][Qt] 20.04.2020 20:40:06 [] (unknown:0) - Operating system …: Windows /  Personal /  (Build 9200) - 64-bit<br>
[DEBUG][Qt] 20.04.2020 20:40:06 [] (unknown:0) - Memory …: 24474 MB physical, 28058 MB virtual<br>
[DEBUG][Qt] 20.04.2020 20:40:06 [] (unknown:0) - CPU …: GenuineIntel , 8 cores, 8 logical processors<br>
[DEBUG][Qt] 20.04.2020 20:40:06 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 20.04.2020 20:40:06 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 20.04.2020 20:40:06 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 20.04.2020 20:40:06 [] (unknown:0) - Additional module paths …: C:/Users/Thomas/AppData/Roaming/NA-MIC/Extensions-28257/QuantitativeReporting/lib/Slicer-4.10/qt-scripted-modules, C:/Users/Thomas/AppData/Roaming/NA-MIC/Extensions-28257/SlicerDevelopmentToolbox/lib/Slicer-4.10/qt-scripted-modules, C:/Users/Thomas/AppData/Roaming/NA-MIC/Extensions-28257/PETDICOMExtension/lib/Slicer-4.10/cli-modules, C:/Users/Thomas/AppData/Roaming/NA-MIC/Extensions-28257/PETDICOMExtension/lib/Slicer-4.10/qt-scripted-modules, C:/Users/Thomas/AppData/Roaming/NA-MIC/Extensions-28257/DCMQI/lib/Slicer-4.10/cli-modules<br>
[DEBUG][Python] 20.04.2020 20:40:19 [Python] (D:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 20.04.2020 20:40:20 [Python] (D:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 20.04.2020 20:40:20 [Python] (D:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 20.04.2020 20:40:21 [] (unknown:0) - Switch to module:  “Welcome”<br>
[DEBUG][Qt] 20.04.2020 20:42:51 [] (unknown:0) - Switch to module:  “DICOM”<br>
[DEBUG][Python] 20.04.2020 20:43:00 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMParametricMapPluginClass : Caching files<br>
[DEBUG][Python] 20.04.2020 20:43:01 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMParametricMapPluginClass : Caching files<br>
[DEBUG][Python] 20.04.2020 20:43:01 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMParametricMapPluginClass : Caching files<br>
[DEBUG][Python] 20.04.2020 20:43:02 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMParametricMapPluginClass : Caching files<br>
[DEBUG][Python] 20.04.2020 20:43:03 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMParametricMapPluginClass : Caching files<br>
[DEBUG][Python] 20.04.2020 20:43:03 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMParametricMapPluginClass : Caching files<br>
[DEBUG][Python] 20.04.2020 20:43:04 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMParametricMapPluginClass : Caching files<br>
[DEBUG][Python] 20.04.2020 20:43:04 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMParametricMapPluginClass : Caching files<br>
[DEBUG][Python] 20.04.2020 20:43:04 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMParametricMapPluginClass : Caching files<br>
[DEBUG][Python] 20.04.2020 20:43:04 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMParametricMapPluginClass : Caching files<br>
[DEBUG][Python] 20.04.2020 20:43:04 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMParametricMapPluginClass : Caching files<br>
[DEBUG][Python] 20.04.2020 20:43:04 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMParametricMapPluginClass : Using cached files<br>
[DEBUG][Python] 20.04.2020 20:43:04 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMParametricMapPluginClass : Using cached files<br>
[DEBUG][Python] 20.04.2020 20:43:04 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMParametricMapPluginClass : Using cached files<br>
[DEBUG][Python] 20.04.2020 20:43:04 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMParametricMapPluginClass : Using cached files<br>
[DEBUG][Python] 20.04.2020 20:43:04 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMParametricMapPluginClass : Using cached files<br>
[DEBUG][Python] 20.04.2020 20:43:04 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMParametricMapPluginClass : Using cached files<br>
[DEBUG][Python] 20.04.2020 20:43:04 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMParametricMapPluginClass : Using cached files<br>
[DEBUG][Python] 20.04.2020 20:43:04 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMParametricMapPluginClass : Using cached files<br>
[DEBUG][Python] 20.04.2020 20:43:04 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMParametricMapPluginClass : Using cached files<br>
[DEBUG][Python] 20.04.2020 20:43:04 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMParametricMapPluginClass : Using cached files<br>
[DEBUG][Python] 20.04.2020 20:43:04 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMParametricMapPluginClass : Using cached files<br>
[DEBUG][Python] 20.04.2020 20:43:04 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMSegmentationPluginClass : Caching files<br>
[DEBUG][Python] 20.04.2020 20:43:05 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMSegmentationPluginClass : Caching files<br>
[DEBUG][Python] 20.04.2020 20:43:05 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMSegmentationPluginClass : Caching files<br>
[DEBUG][Python] 20.04.2020 20:43:05 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMSegmentationPluginClass : Caching files<br>
[DEBUG][Python] 20.04.2020 20:43:05 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMSegmentationPluginClass : Caching files<br>
[DEBUG][Python] 20.04.2020 20:43:05 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMSegmentationPluginClass : Caching files<br>
[DEBUG][Python] 20.04.2020 20:43:06 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMSegmentationPluginClass : Caching files<br>
[DEBUG][Python] 20.04.2020 20:43:06 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMSegmentationPluginClass : Caching files<br>
[DEBUG][Python] 20.04.2020 20:43:06 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMSegmentationPluginClass : Caching files<br>
[DEBUG][Python] 20.04.2020 20:43:06 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMSegmentationPluginClass : Caching files<br>
[DEBUG][Python] 20.04.2020 20:43:06 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMSegmentationPluginClass : Caching files<br>
[DEBUG][Python] 20.04.2020 20:43:06 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMSegmentationPluginClass : Using cached files<br>
[DEBUG][Python] 20.04.2020 20:43:06 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMSegmentationPluginClass : Using cached files<br>
[DEBUG][Python] 20.04.2020 20:43:06 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMSegmentationPluginClass : Using cached files<br>
[DEBUG][Python] 20.04.2020 20:43:06 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMSegmentationPluginClass : Using cached files<br>
[DEBUG][Python] 20.04.2020 20:43:06 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMSegmentationPluginClass : Using cached files<br>
[DEBUG][Python] 20.04.2020 20:43:06 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMSegmentationPluginClass : Using cached files<br>
[DEBUG][Python] 20.04.2020 20:43:06 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMSegmentationPluginClass : Using cached files<br>
[DEBUG][Python] 20.04.2020 20:43:06 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMSegmentationPluginClass : Using cached files<br>
[DEBUG][Python] 20.04.2020 20:43:06 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMSegmentationPluginClass : Using cached files<br>
[DEBUG][Python] 20.04.2020 20:43:06 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMSegmentationPluginClass : Using cached files<br>
[DEBUG][Python] 20.04.2020 20:43:06 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMSegmentationPluginClass : Using cached files<br>
[DEBUG][Python] 20.04.2020 20:43:06 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMTID1500PluginClass : Caching files<br>
[DEBUG][Python] 20.04.2020 20:43:08 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMTID1500PluginClass : Caching files<br>
[DEBUG][Python] 20.04.2020 20:43:09 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMTID1500PluginClass : Caching files<br>
[DEBUG][Python] 20.04.2020 20:43:11 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMTID1500PluginClass : Caching files<br>
[DEBUG][Python] 20.04.2020 20:43:12 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMTID1500PluginClass : Caching files<br>
[DEBUG][Python] 20.04.2020 20:43:14 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMTID1500PluginClass : Caching files<br>
[DEBUG][Python] 20.04.2020 20:43:16 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMTID1500PluginClass : Caching files<br>
[DEBUG][Python] 20.04.2020 20:43:17 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMTID1500PluginClass : Caching files<br>
[DEBUG][Python] 20.04.2020 20:43:17 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMTID1500PluginClass : Caching files<br>
[DEBUG][Python] 20.04.2020 20:43:17 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMTID1500PluginClass : Caching files<br>
[DEBUG][Python] 20.04.2020 20:43:17 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMTID1500PluginClass : Caching files<br>
[DEBUG][Python] 20.04.2020 20:43:20 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMTID1500PluginClass : Using cached files<br>
[DEBUG][Python] 20.04.2020 20:43:20 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMTID1500PluginClass : Using cached files<br>
[DEBUG][Python] 20.04.2020 20:43:20 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMTID1500PluginClass : Using cached files<br>
[DEBUG][Python] 20.04.2020 20:43:20 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMTID1500PluginClass : Using cached files<br>
[DEBUG][Python] 20.04.2020 20:43:20 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMTID1500PluginClass : Using cached files<br>
[DEBUG][Python] 20.04.2020 20:43:20 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMTID1500PluginClass : Using cached files<br>
[DEBUG][Python] 20.04.2020 20:43:20 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMTID1500PluginClass : Using cached files<br>
[DEBUG][Python] 20.04.2020 20:43:20 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMTID1500PluginClass : Using cached files<br>
[DEBUG][Python] 20.04.2020 20:43:20 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMTID1500PluginClass : Using cached files<br>
[DEBUG][Python] 20.04.2020 20:43:20 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMTID1500PluginClass : Using cached files<br>
[DEBUG][Python] 20.04.2020 20:43:20 [Python] (C:\Users\Thomas\AppData\Roaming\NA-MIC\Extensions-28257\QuantitativeReporting\lib\Slicer-4.10\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMTID1500PluginClass : Using cached files<br>
[DEBUG][Python] 20.04.2020 20:43:20 [Python] (D:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:455) - MultiVolumeImportPlugin::examine<br>
[DEBUG][Python] 20.04.2020 20:43:21 [Python] (D:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:495) - DICOMMultiVolumePlugin found 0 multivolumes!<br>
[DEBUG][Python] 20.04.2020 20:43:21 [Python] (D:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:455) - MultiVolumeImportPlugin::examine<br>
[DEBUG][Python] 20.04.2020 20:43:22 [Python] (D:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:495) - DICOMMultiVolumePlugin found 0 multivolumes!<br>
[DEBUG][Python] 20.04.2020 20:43:23 [Python] (D:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:455) - MultiVolumeImportPlugin::examine<br>
[DEBUG][Python] 20.04.2020 20:43:24 [Python] (D:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:495) - DICOMMultiVolumePlugin found 0 multivolumes!<br>
[DEBUG][Python] 20.04.2020 20:43:24 [Python] (D:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:455) - MultiVolumeImportPlugin::examine<br>
[DEBUG][Python] 20.04.2020 20:43:25 [Python] (D:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:495) - DICOMMultiVolumePlugin found 0 multivolumes!<br>
[DEBUG][Python] 20.04.2020 20:43:25 [Python] (D:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:455) - MultiVolumeImportPlugin::examine<br>
[DEBUG][Python] 20.04.2020 20:43:26 [Python] (D:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:495) - DICOMMultiVolumePlugin found 0 multivolumes!<br>
[DEBUG][Python] 20.04.2020 20:43:26 [Python] (D:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:455) - MultiVolumeImportPlugin::examine<br>
[DEBUG][Python] 20.04.2020 20:43:27 [Python] (D:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:495) - DICOMMultiVolumePlugin found 0 multivolumes!<br>
[DEBUG][Python] 20.04.2020 20:43:27 [Python] (D:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:455) - MultiVolumeImportPlugin::examine<br>
[DEBUG][Python] 20.04.2020 20:43:28 [Python] (D:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:495) - DICOMMultiVolumePlugin found 0 multivolumes!<br>
[DEBUG][Python] 20.04.2020 20:43:28 [Python] (D:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:455) - MultiVolumeImportPlugin::examine<br>
[DEBUG][Python] 20.04.2020 20:43:28 [Python] (D:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:495) - DICOMMultiVolumePlugin found 0 multivolumes!<br>
[DEBUG][Python] 20.04.2020 20:43:28 [Python] (D:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:455) - MultiVolumeImportPlugin::examine<br>
[DEBUG][Python] 20.04.2020 20:43:28 [Python] (D:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:495) - DICOMMultiVolumePlugin found 0 multivolumes!<br>
[DEBUG][Python] 20.04.2020 20:43:28 [Python] (D:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:455) - MultiVolumeImportPlugin::examine<br>
[DEBUG][Python] 20.04.2020 20:43:28 [Python] (D:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:495) - DICOMMultiVolumePlugin found 0 multivolumes!<br>
[DEBUG][Python] 20.04.2020 20:43:28 [Python] (D:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:455) - MultiVolumeImportPlugin::examine<br>
[DEBUG][Python] 20.04.2020 20:43:28 [Python] (D:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:495) - DICOMMultiVolumePlugin found 0 multivolumes!<br>
[WARNING][Python] 20.04.2020 20:43:28 [Python] (D:\Program Files\Slicer 4.10.2\bin\Python\slicer\util.py:1110) - Warning: Plugin failed: MultiVolumeImporterPlugin</p>
<p>See python console for error message.<br>
[CRITICAL][Stream] 20.04.2020 20:43:28 [] (unknown:0) - Traceback (most recent call last):<br>
[CRITICAL][Stream] 20.04.2020 20:43:28 [] (unknown:0) -   File “D:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\DICOMLib\DICOMWidgets.py”, line 737, in getLoadablesFromFileLists<br>
[CRITICAL][Stream] 20.04.2020 20:43:28 [] (unknown:0) -     loadablesByPlugin[plugin] = plugin.examine(fileLists)<br>
[CRITICAL][Stream] 20.04.2020 20:43:28 [] (unknown:0) -   File “D:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py”, line 109, in examine<br>
[CRITICAL][Stream] 20.04.2020 20:43:28 [] (unknown:0) -     loadables += self.examineFilesIPPAcqTime(files)<br>
[CRITICAL][Stream] 20.04.2020 20:43:28 [] (unknown:0) -   File “D:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py”, line 404, in examineFilesIPPAcqTime<br>
[CRITICAL][Stream] 20.04.2020 20:43:28 [] (unknown:0) -     frameFileListStr = frameFileListStr+str(file)+’,’<br>
[CRITICAL][Stream] 20.04.2020 20:43:28 [] (unknown:0) - UnicodeEncodeError: ‘ascii’ codec can’t encode character u’\xe9’ in position 4: ordinal not in range(128)<br>
[CRITICAL][Stream] 20.04.2020 20:43:28 [] (unknown:0) - Warning: Plugin failed: MultiVolumeImporterPlugin<br>
[CRITICAL][Stream] 20.04.2020 20:43:28 [] (unknown:0) -<br>
[CRITICAL][Stream] 20.04.2020 20:43:28 [] (unknown:0) - See python console for error message.<br>
[INFO][Stream] 20.04.2020 20:56:19 [] (unknown:0) - DICOM Plugin failed: ‘ascii’ codec can’t encode character u’\xe9’ in position 4: ordinal not in range(128)<br>
[WARNING][Python] 20.04.2020 20:56:21 [Python] (D:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\DICOMLib\DICOMWidgets.py:904) - Warning in DICOM plugin Scalar Volume when examining loadable 504: Dose Report: Reference image in series does not contain geometry information. Please use caution.<br>
[WARNING][Python] 20.04.2020 20:56:21 [Python] (D:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\DICOMLib\DICOMWidgets.py:904) - Warning in DICOM plugin Scalar Volume when examining loadable 502: Patient Protocol: Reference image in series does not contain geometry information. Please use caution.<br>
[WARNING][Python] 20.04.2020 20:56:21 [Python] (D:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\DICOMLib\DICOMWidgets.py:904) - Warning in DICOM plugin Scalar Volume when examining loadable 530: snapshots: Reference image in series does not contain geometry information. Please use caution.<br>
[CRITICAL][Stream] 20.04.2020 20:56:21 [] (unknown:0) - Warning in DICOM plugin Scalar Volume when examining loadable 504: Dose Report: Reference image in series does not contain geometry information. Please use caution.<br>
[CRITICAL][Stream] 20.04.2020 20:56:21 [] (unknown:0) -<br>
[CRITICAL][Stream] 20.04.2020 20:56:21 [] (unknown:0) - Warning in DICOM plugin Scalar Volume when examining loadable 502: Patient Protocol: Reference image in series does not contain geometry information. Please use caution.<br>
[CRITICAL][Stream] 20.04.2020 20:56:21 [] (unknown:0) -<br>
[CRITICAL][Stream] 20.04.2020 20:56:21 [] (unknown:0) - Warning in DICOM plugin Scalar Volume when examining loadable 530: snapshots: Reference image in series does not contain geometry information. Please use caution.<br>
[CRITICAL][Stream] 20.04.2020 20:56:21 [] (unknown:0) -<br>
[CRITICAL][Stream] 20.04.2020 20:56:32 [] (unknown:0) - W: DcmUniqueIdentifier: Element ReferencedSOPClassUID (0008,1150) contains one or more space characters, which were removed</p>
<p>I add that I could open the dicom data with a dicom viewer so the data set is not corrupted.</p>
<p>Many thanks for your help</p>

---

## Post #2 by @pieper (2020-04-20 20:20 UTC)

<p>It appears the data file path has a non-ascii character in it.  If you rename to remove special characters it should work.  Or you can try with the nightly build, which should support these characters correctly (let us know if it doesn’t).</p>

---

## Post #3 by @tnmd33 (2020-04-21 18:21 UTC)

<p>Hi,</p>
<p>Many thanks for your quick answer.</p>
<p>I could not make sense of the log but with your suggestion, the import works now that I have moved the dicom data in another folder.</p>

---
