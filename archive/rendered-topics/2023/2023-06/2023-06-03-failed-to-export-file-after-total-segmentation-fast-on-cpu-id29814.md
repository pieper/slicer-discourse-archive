---
topic_id: 29814
title: "Failed To Export File After Total Segmentation Fast On Cpu"
date: 2023-06-03
url: https://discourse.slicer.org/t/29814
---

# Failed to export file after total segmentation (fast, on CPU)

**Topic ID**: 29814
**Date**: 2023-06-03
**URL**: https://discourse.slicer.org/t/failed-to-export-file-after-total-segmentation-fast-on-cpu/29814

---

## Post #1 by @simoneb (2023-06-03 17:23 UTC)

<p>Problem report for Slicer 5.2.2 win-amd64: Hello, I am new to 3D Slicer (version 5.2.2) I ran totalsegmentator (fast on CPU) and then tried to export file, but failed. Thanks for any help</p>
<details>
<summary>
Logs</summary>
<p>[DEBUG][Qt] 03.06.2023 17:45:37 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Session start time …: 2023-06-03 17:45:37<br>
[DEBUG][Qt] 03.06.2023 17:45:37 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Slicer version …: 5.2.2 (revision 31382 / fb46bd1) win-amd64 - installed release<br>
[DEBUG][Qt] 03.06.2023 17:45:37 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Operating system …: Windows /  Personal / (Build 19045, Code Page 65001) - 64-bit<br>
[DEBUG][Qt] 03.06.2023 17:45:37 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Memory …: 16234 MB physical, 18666 MB virtual<br>
[DEBUG][Qt] 03.06.2023 17:45:37 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - CPU …: GenuineIntel , 12 cores, 12 logical processors<br>
[DEBUG][Qt] 03.06.2023 17:45:37 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 03.06.2023 17:45:37 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Qt configuration …: version 5.15.2, with SSL, requested OpenGL 3.2 (compatibility profile)<br>
[DEBUG][Qt] 03.06.2023 17:45:37 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Internationalization …: disabled, language=<br>
[DEBUG][Qt] 03.06.2023 17:45:37 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Developer mode …: disabled<br>
[DEBUG][Qt] 03.06.2023 17:45:37 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Application path …: C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/bin<br>
[DEBUG][Qt] 03.06.2023 17:45:37 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Additional module paths …: NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules, NA-MIC/Extensions-31382/PyTorch/lib/Slicer-5.2/qt-scripted-modules, NA-MIC/Extensions-31382/SequenceRegistration/lib/Slicer-5.2/qt-scripted-modules, NA-MIC/Extensions-31382/SlicerElastix/lib/Slicer-5.2/qt-scripted-modules, NA-MIC/Extensions-31382/SlicerVMTK/lib/Slicer-5.2/qt-loadable-modules, NA-MIC/Extensions-31382/SlicerVMTK/lib/Slicer-5.2/qt-scripted-modules, NA-MIC/Extensions-31382/MarkupsToModel/lib/Slicer-5.2/qt-loadable-modules, NA-MIC/Extensions-31382/RVesselX/lib/Slicer-5.2/qt-scripted-modules, NA-MIC/Extensions-31382/ExtraMarkups/lib/Slicer-5.2/qt-loadable-modules, NA-MIC/Extensions-31382/MeshStatisticsExtension/lib/Slicer-5.2/qt-scripted-modules, NA-MIC/Extensions-31382/ModelToModelDistance/lib/Slicer-5.2/cli-modules, NA-MIC/Extensions-31382/DebuggingTools/lib/Slicer-5.2/qt-scripted-modules, NA-MIC/Extensions-31382/MONAILabel/lib/Slicer-5.2/qt-scripted-modules, NA-MIC/Extensions-31382/DensityLungSegmentation/lib/Slicer-5.2/qt-scripted-modules, NA-MIC/Extensions-31382/SurfaceWrapSolidify/lib/Slicer-5.2/qt-scripted-modules, NA-MIC/Extensions-31382/SegmentEditorExtraEffects/lib/Slicer-5.2/qt-loadable-modules, NA-MIC/Extensions-31382/SegmentEditorExtraEffects/lib/Slicer-5.2/qt-scripted-modules, NA-MIC/Extensions-31382/NvidiaAIAssistedAnnotation/lib/Slicer-5.2/qt-scripted-modules, NA-MIC/Extensions-31382/HDBrainExtraction/lib/Slicer-5.2/qt-scripted-modules, NA-MIC/Extensions-31382/Sandbox/lib/Slicer-5.2/qt-loadable-modules, NA-MIC/Extensions-31382/Sandbox/lib/Slicer-5.2/qt-scripted-modules, NA-MIC/Extensions-31382/SegmentMesher/lib/Slicer-5.2/qt-scripted-modules, NA-MIC/Extensions-31382/SegmentRegistration/lib/Slicer-5.2/qt-scripted-modules, NA-MIC/Extensions-31382/SlicerProstate/lib/Slicer-5.2/cli-modules, NA-MIC/Extensions-31382/SlicerProstate/lib/Slicer-5.2/qt-scripted-modules, NA-MIC/Extensions-31382/SlicerOpenAnatomy/lib/Slicer-5.2/qt-scripted-modules, NA-MIC/Extensions-31382/SlicerRT/lib/Slicer-5.2/cli-modules, NA-MIC/Extensions-31382/SlicerRT/lib/Slicer-5.2/qt-loadable-modules, NA-MIC/Extensions-31382/SlicerRT/lib/Slicer-5.2/qt-scripted-modules, NA-MIC/Extensions-31382/SlicerDevelopmentToolbox/lib/Slicer-5.2/qt-scripted-modules, NA-MIC/Extensions-31382/QuantitativeReporting/lib/Slicer-5.2/qt-scripted-modules, NA-MIC/Extensions-31382/DCMQI/lib/Slicer-5.2/cli-modules, NA-MIC/Extensions-31382/PETDICOMExtension/lib/Slicer-5.2/cli-modules, NA-MIC/Extensions-31382/PETDICOMExtension/lib/Slicer-5.2/qt-scripted-modules<br>
[CRITICAL][Qt] 03.06.2023 17:45:44 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Error(s):<br>
CLI executable: C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/NA-MIC/Extensions-31382/SlicerVMTK/lib/Slicer-5.2/qt-loadable-modules/vtkvmtk.py<br>
The process failed to start. Either the invoked program is missing, or you may have insufficient permissions to invoke the program.<br>
[CRITICAL][Qt] 03.06.2023 17:45:44 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Fail to instantiate module  “vtkvmtk”<br>
[CRITICAL][Qt] 03.06.2023 17:45:44 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - The following modules failed to be instantiated:<br>
[CRITICAL][Qt] 03.06.2023 17:45:44 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -    vtkvmtk<br>
[DEBUG][Python] 03.06.2023 17:45:46 [Python] (C:\Users\Simone\AppData\Local\NA-MIC\Slicer-5.2.2\lib\Slicer-5.2\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: Annotations<br>
[CRITICAL][Stream] 03.06.2023 17:45:48 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Failed to load vtkSlicerStenosisMeasurement3DModuleLogicPython: No module named vtkSlicerShapeModuleMRMLPython<br>
[DEBUG][Python] 03.06.2023 17:45:49 [Python] (C:\Users\Simone\AppData\Local\NA-MIC\Slicer-5.2.2\lib\Slicer-5.2\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 03.06.2023 17:45:50 [Python] (C:\Users\Simone\AppData\Local\NA-MIC\Slicer-5.2.2\lib\Slicer-5.2\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 03.06.2023 17:45:50 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “Welcome”<br>
[INFO][Python] 03.06.2023 17:45:51 [Python] (C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/NA-MIC/Extensions-31382/NvidiaAIAssistedAnnotation/lib/Slicer-5.2/qt-scripted-modules/SegmentEditorNvidiaAIAA.py:32) - This plugin dir: C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/NA-MIC/Extensions-31382/NvidiaAIAssistedAnnotation/lib/Slicer-5.2/qt-scripted-modules<br>
[INFO][VTK] 03.06.2023 17:45:51 [vtkMRMLVolumeArchetypeStorageNode (00000237BAB4B310)] (D:\D\S\S-0\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:513) - Loaded volume from file: C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/NA-MIC/Extensions-31382/SlicerVMTK/lib/Slicer-5.2/qt-scripted-modules/Resources/Vesselness.png. Dimensions: 65x50x1. Number of components: 3. Pixel type: unsigned char.<br>
[DEBUG][Qt] 03.06.2023 17:46:30 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “DICOM”<br>
[DEBUG][Python] 03.06.2023 17:46:35 [Python] (C:\Users\Simone\AppData\Local\NA-MIC\Slicer-5.2.2\NA-MIC\Extensions-31382\QuantitativeReporting\lib\Slicer-5.2\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMParametricMapPluginClass : Caching files<br>
[DEBUG][Python] 03.06.2023 17:46:36 [Python] (C:\Users\Simone\AppData\Local\NA-MIC\Slicer-5.2.2\NA-MIC\Extensions-31382\QuantitativeReporting\lib\Slicer-5.2\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMParametricMapPluginClass : Using cached files<br>
[WARNING][Python] 03.06.2023 17:46:39 [Python] (C:\Users\Simone\AppData\Local\NA-MIC\Slicer-5.2.2\lib\Slicer-5.2\qt-scripted-modules\DICOMLib\DICOMUtils.py:697) - Geometric issues were found with 1 of the series. Please use caution.<br>
[DEBUG][Python] 03.06.2023 17:46:39 [Python] (C:\Users\Simone\AppData\Local\NA-MIC\Slicer-5.2.2\NA-MIC\Extensions-31382\QuantitativeReporting\lib\Slicer-5.2\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMSegmentationPluginClass : Caching files<br>
[DEBUG][Python] 03.06.2023 17:46:40 [Python] (C:\Users\Simone\AppData\Local\NA-MIC\Slicer-5.2.2\NA-MIC\Extensions-31382\QuantitativeReporting\lib\Slicer-5.2\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMSegmentationPluginClass : Using cached files<br>
[DEBUG][Python] 03.06.2023 17:46:40 [Python] (C:\Users\Simone\AppData\Local\NA-MIC\Slicer-5.2.2\NA-MIC\Extensions-31382\QuantitativeReporting\lib\Slicer-5.2\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMTID1500PluginClass : Caching files<br>
[DEBUG][Python] 03.06.2023 17:46:50 [Python] (C:\Users\Simone\AppData\Local\NA-MIC\Slicer-5.2.2\NA-MIC\Extensions-31382\QuantitativeReporting\lib\Slicer-5.2\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMTID1500PluginClass : Using cached files<br>
[WARNING][Python] 03.06.2023 17:47:04 [Python] (C:\Users\Simone\AppData\Local\NA-MIC\Slicer-5.2.2\lib\Slicer-5.2\qt-scripted-modules\DICOMLib\DICOMBrowser.py:555) - Warning in DICOM plugin Scalar Volume when examining loadable 12: Venosa  1.5  Br59  1 Osteo: Images are not equally spaced (a difference of 1 vs 1 in spacings was detected).  Slicer will apply a transform to this series trying to regularize the volume. Please use caution.<br>
[INFO][Python] 03.06.2023 17:47:04 [Python] (C:\Users\Simone\AppData\Local\NA-MIC\Slicer-5.2.2\bin\Python\slicer\util.py:2736) - Warnings detected during load.  Examine data in Advanced mode for details.  Load anyway?<br>
[INFO][Python] 03.06.2023 17:48:18 [Python] (C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/bin/…/lib/Slicer-5.2/qt-scripted-modules/DICOMScalarVolumePlugin.py:393) - Loading with imageIOName: GDCM<br>
[WARNING][ITK] 03.06.2023 17:48:28 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - WARNING: In D:\D\S\S-0-build\ITK\Modules\IO\ImageBase\include\itkImageSeriesReader.hxx, line 478<br>
ImageSeriesReader (00000237BF977AE0): Non uniform sampling or missing slices detected,  maximum nonuniformity:1.95963<br>
[WARNING][Python] 03.06.2023 17:48:29 [Python] (C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/bin/…/lib/Slicer-5.2/qt-scripted-modules/DICOMScalarVolumePlugin.py:837) - Irregular volume geometry detected (maximum error of 4.13354 mm is above tolerance threshold of 0.001 mm).  Adding acquisition transform to regularize geometry.<br>
[DEBUG][Python] 03.06.2023 17:49:31 [Python] (C:\Users\Simone\AppData\Local\NA-MIC\Slicer-5.2.2\NA-MIC\Extensions-31382\QuantitativeReporting\lib\Slicer-5.2\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMParametricMapPluginClass : Using cached files<br>
[DEBUG][Python] 03.06.2023 17:49:31 [Python] (C:\Users\Simone\AppData\Local\NA-MIC\Slicer-5.2.2\NA-MIC\Extensions-31382\QuantitativeReporting\lib\Slicer-5.2\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMParametricMapPluginClass : Using cached files<br>
[DEBUG][Python] 03.06.2023 17:49:31 [Python] (C:\Users\Simone\AppData\Local\NA-MIC\Slicer-5.2.2\NA-MIC\Extensions-31382\QuantitativeReporting\lib\Slicer-5.2\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMSegmentationPluginClass : Using cached files<br>
[DEBUG][Python] 03.06.2023 17:49:31 [Python] (C:\Users\Simone\AppData\Local\NA-MIC\Slicer-5.2.2\NA-MIC\Extensions-31382\QuantitativeReporting\lib\Slicer-5.2\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMSegmentationPluginClass : Using cached files<br>
[DEBUG][Python] 03.06.2023 17:49:31 [Python] (C:\Users\Simone\AppData\Local\NA-MIC\Slicer-5.2.2\NA-MIC\Extensions-31382\QuantitativeReporting\lib\Slicer-5.2\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMTID1500PluginClass : Using cached files<br>
[DEBUG][Python] 03.06.2023 17:49:31 [Python] (C:\Users\Simone\AppData\Local\NA-MIC\Slicer-5.2.2\NA-MIC\Extensions-31382\QuantitativeReporting\lib\Slicer-5.2\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMTID1500PluginClass : Using cached files<br>
[WARNING][Python] 03.06.2023 17:49:45 [Python] (C:\Users\Simone\AppData\Local\NA-MIC\Slicer-5.2.2\lib\Slicer-5.2\qt-scripted-modules\DICOMLib\DICOMBrowser.py:555) - Warning in DICOM plugin Scalar Volume when examining loadable 12: Venosa  1.5  Br59  1 Osteo: Images are not equally spaced (a difference of 1 vs 1 in spacings was detected).  Slicer will apply a transform to this series trying to regularize the volume. Please use caution.<br>
[INFO][Python] 03.06.2023 17:49:45 [Python] (C:\Users\Simone\AppData\Local\NA-MIC\Slicer-5.2.2\bin\Python\slicer\util.py:2736) - Warnings detected during load.  Examine data in Advanced mode for details.  Load anyway?<br>
[INFO][Python] 03.06.2023 17:49:47 [Python] (C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/bin/…/lib/Slicer-5.2/qt-scripted-modules/DICOMScalarVolumePlugin.py:393) - Loading with imageIOName: GDCM<br>
[WARNING][ITK] 03.06.2023 17:49:56 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - WARNING: In D:\D\S\S-0-build\ITK\Modules\IO\ImageBase\include\itkImageSeriesReader.hxx, line 478<br>
ImageSeriesReader (00000237BF979A60): Non uniform sampling or missing slices detected,  maximum nonuniformity:1.95963<br>
[WARNING][Python] 03.06.2023 17:49:58 [Python] (C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/bin/…/lib/Slicer-5.2/qt-scripted-modules/DICOMScalarVolumePlugin.py:837) - Irregular volume geometry detected (maximum error of 4.13354 mm is above tolerance threshold of 0.001 mm).  Adding acquisition transform to regularize geometry.<br>
[DEBUG][Qt] 03.06.2023 17:50:05 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “Segmentations”<br>
[DEBUG][Qt] 03.06.2023 17:50:22 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “TotalSegmentator”<br>
[DEBUG][Python] 03.06.2023 17:50:31 [Python] (C:\Users\Simone\AppData\Local\NA-MIC\Slicer-5.2.2\lib\Python\Lib\site-packages\matplotlib_<em>init</em>_.py:337) - matplotlib data path: C:\Users\Simone\AppData\Local\NA-MIC\Slicer-5.2.2\lib\Python\Lib\site-packages\matplotlib\mpl-data<br>
[DEBUG][Python] 03.06.2023 17:50:31 [Python] (C:\Users\Simone\AppData\Local\NA-MIC\Slicer-5.2.2\lib\Python\Lib\site-packages\matplotlib_<em>init</em>_.py:337) - CONFIGDIR=C:\Users\Simone.matplotlib<br>
[DEBUG][Python] 03.06.2023 17:50:31 [Python] (C:\Users\Simone\AppData\Local\NA-MIC\Slicer-5.2.2\lib\Python\Lib\site-packages\matplotlib_<em>init</em>_.py:1505) - interactive is False<br>
[DEBUG][Python] 03.06.2023 17:50:31 [Python] (C:\Users\Simone\AppData\Local\NA-MIC\Slicer-5.2.2\lib\Python\Lib\site-packages\matplotlib_<em>init</em>_.py:1506) - platform is win32<br>
[INFO][Python] 03.06.2023 17:50:31 [Python] (C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:521) - Processing started<br>
[INFO][Python] 03.06.2023 17:50:31 [Python] (C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:521) - Writing input file to C:/Users/Simone/AppData/Local/Temp/Slicer/__SlicerTemp__2023-06-03_17+50+31.634/total-segmentator-input.nii<br>
[INFO][Python] 03.06.2023 17:50:32 [Python] (C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:521) - Creating segmentations with TotalSegmentator AI…<br>
[INFO][Python] 03.06.2023 17:50:32 [Python] (C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:521) - Total Segmentator arguments: [‘-i’, ‘C:/Users/Simone/AppData/Local/Temp/Slicer/__SlicerTemp__2023-06-03_17+50+31.634/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/Simone/AppData/Local/Temp/Slicer/__SlicerTemp__2023-06-03_17+50+31.634/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–fast’]<br>
[INFO][Python] 03.06.2023 17:51:16 [Python] (C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:521) -<br>
[INFO][Python] 03.06.2023 17:51:16 [Python] (C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:521) -<br>
[INFO][Python] 03.06.2023 17:51:16 [Python] (C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:521) - Please cite the following paper when using nnUNet:<br>
[INFO][Python] 03.06.2023 17:51:16 [Python] (C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:521) -<br>
[INFO][Python] 03.06.2023 17:51:16 [Python] (C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:521) - Isensee, F., Jaeger, P.F., Kohl, S.A.A. et al. “nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation.” Nat Methods (2020). <a href="https://doi.org/10.1038/s41592-020-01008-z" class="inline-onebox" rel="noopener nofollow ugc">nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation | Nature Methods</a><br>
[INFO][Python] 03.06.2023 17:51:17 [Python] (C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:521) -<br>
[INFO][Python] 03.06.2023 17:51:17 [Python] (C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:521) -<br>
[INFO][Python] 03.06.2023 17:51:17 [Python] (C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:521) - If you have questions or suggestions, feel free to open an issue at <a href="https://github.com/MIC-DKFZ/nnUNet" class="inline-onebox" rel="noopener nofollow ugc">GitHub - MIC-DKFZ/nnUNet</a><br>
[INFO][Python] 03.06.2023 17:51:17 [Python] (C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:521) -<br>
[INFO][Python] 03.06.2023 17:51:17 [Python] (C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:521) - preprocessing C:\Users\Simone\AppData\Local\Temp\nnunet_tmp_79zcp9bd\s01.nii.gz<br>
[INFO][Python] 03.06.2023 17:51:17 [Python] (C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:521) - using preprocessor GenericPreprocessor<br>
[INFO][Python] 03.06.2023 17:51:17 [Python] (C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:521) - before crop: (1, 224, 117, 117) after crop: (1, 224, 117, 117) spacing: [3. 3. 3.]<br>
[INFO][Python] 03.06.2023 17:51:17 [Python] (C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:521) -<br>
[INFO][Python] 03.06.2023 17:51:17 [Python] (C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:521) - no resampling necessary<br>
[INFO][Python] 03.06.2023 17:51:17 [Python] (C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:521) - no resampling necessary<br>
[INFO][Python] 03.06.2023 17:51:17 [Python] (C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:521) - before: {‘spacing’: array([3., 3., 3.]), ‘spacing_transposed’: array([3., 3., 3.]), ‘data.shape (data is transposed)’: (1, 224, 117, 117)}<br>
[INFO][Python] 03.06.2023 17:51:17 [Python] (C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:521) - after:  {‘spacing’: array([3., 3., 3.]), ‘data.shape (data is resampled)’: (1, 224, 117, 117)}<br>
[INFO][Python] 03.06.2023 17:51:17 [Python] (C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:521) -<br>
[INFO][Python] 03.06.2023 17:51:17 [Python] (C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:521) - (1, 224, 117, 117)<br>
[INFO][Python] 03.06.2023 17:51:17 [Python] (C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:521) - This worker has ended successfully, no errors to report<br>
[INFO][Python] 03.06.2023 17:51:17 [Python] (C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:521) - C:\Users\Simone\AppData\Local\NA-MIC\Slicer-5.2.2\lib\Python\Lib\site-packages\torch\cuda\amp\grad_scaler.py:120: UserWarning: torch.cuda.amp.GradScaler is enabled, but CUDA is not available.  Disabling.<br>
[INFO][Python] 03.06.2023 17:51:17 [Python] (C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:521) -   warnings.warn(“torch.cuda.amp.GradScaler is enabled, but CUDA is not available.  Disabling.”)<br>
[INFO][Python] 03.06.2023 17:51:17 [Python] (C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:521) - C:\Users\Simone\AppData\Local\NA-MIC\Slicer-5.2.2\lib\Python\Lib\site-packages\torch\amp\autocast_mode.py:204: UserWarning: User provided device_type of ‘cuda’, but CUDA is not available. Disabling<br>
[INFO][Python] 03.06.2023 17:51:17 [Python] (C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:521) -   warnings.warn(‘User provided device_type of 'cuda', but CUDA is not available. Disabling’)<br>
[INFO][Python] 03.06.2023 17:53:45 [Python] (C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:521) -<br>
[INFO][Python] 03.06.2023 17:53:45 [Python] (C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:521) -<br>
[INFO][Python] 03.06.2023 17:53:45 [Python] (C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:521) - Please cite the following paper when using nnUNet:<br>
[INFO][Python] 03.06.2023 17:53:45 [Python] (C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:521) -<br>
[INFO][Python] 03.06.2023 17:53:45 [Python] (C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:521) - Isensee, F., Jaeger, P.F., Kohl, S.A.A. et al. “nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation.” Nat Methods (2020). <a href="https://doi.org/10.1038/s41592-020-01008-z" class="inline-onebox" rel="noopener nofollow ugc">nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation | Nature Methods</a><br>
[INFO][Python] 03.06.2023 17:53:45 [Python] (C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:521) -<br>
[INFO][Python] 03.06.2023 17:53:45 [Python] (C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:521) -<br>
[INFO][Python] 03.06.2023 17:53:45 [Python] (C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:521) - If you have questions or suggestions, feel free to open an issue at <a href="https://github.com/MIC-DKFZ/nnUNet" class="inline-onebox" rel="noopener nofollow ugc">GitHub - MIC-DKFZ/nnUNet</a><br>
[INFO][Python] 03.06.2023 17:53:45 [Python] (C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:521) -<br>
[INFO][Python] 03.06.2023 17:53:45 [Python] (C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:521) - force_separate_z: None interpolation order: 0<br>
[INFO][Python] 03.06.2023 17:54:10 [Python] (C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:521) -<br>
[INFO][Python] 03.06.2023 17:54:10 [Python] (C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:521) - If you use this tool please cite: <a href="https://doi.org/10.48550/arXiv.2208.05868" class="inline-onebox" rel="noopener nofollow ugc">[2208.05868] TotalSegmentator: robust segmentation of 104 anatomical structures in CT images</a><br>
[INFO][Python] 03.06.2023 17:54:10 [Python] (C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:521) -<br>
[INFO][Python] 03.06.2023 17:54:10 [Python] (C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:521) - No GPU detected. Running on CPU. This can be very slow. The ‘–fast’ option can help to some extend.<br>
[INFO][Python] 03.06.2023 17:54:10 [Python] (C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:521) - Using ‘fast’ option: resampling to lower resolution (3mm)<br>
[INFO][Python] 03.06.2023 17:54:10 [Python] (C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:521) - Resampling…<br>
[INFO][Python] 03.06.2023 17:54:10 [Python] (C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:521) -   Resampled in 15.60s<br>
[INFO][Python] 03.06.2023 17:54:10 [Python] (C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:521) - Predicting…<br>
[INFO][Python] 03.06.2023 17:54:10 [Python] (C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:521) -   Predicted in 164.26s<br>
[INFO][Python] 03.06.2023 17:54:10 [Python] (C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:521) - Resampling…<br>
[INFO][Python] 03.06.2023 17:54:10 [Python] (C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:521) - Saving segmentations…<br>
[INFO][Python] 03.06.2023 17:54:10 [Python] (C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:521) -   Saved in 10.85s<br>
[INFO][Python] 03.06.2023 17:54:11 [Python] (C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:521) - Importing segmentation results…<br>
[INFO][VTK] 03.06.2023 17:54:11 [vtkMRMLSegmentationStorageNode (00000237BCF8E790)] (D:\D\S\S-0\Libs\MRML\Core\vtkMRMLSegmentationStorageNode.cxx:624) - ReferenceImageExtentOffset attribute was not found in NRRD segmentation file. Assume no offset.<br>
[INFO][Python] 03.06.2023 17:54:33 [Python] (C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:521) - Cleaning up temporary folder…<br>
[INFO][Python] 03.06.2023 17:54:33 [Python] (C:/Users/Simone/AppData/Local/NA-MIC/Slicer-5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py:521) - Processing completed in 242.40 seconds<br>
[DEBUG][Qt] 03.06.2023 17:54:44 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “SegmentEditor”<br>
[WARNING][Qt] 03.06.2023 17:54:44 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - QLayout::addChildLayout: layout “” already has a parent<br>
[WARNING][Qt] 03.06.2023 17:54:56 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - ctkSliderWidget::setSingleStep()  0 is out of bounds. 0 100 1<br>
[DEBUG][Qt] 03.06.2023 17:55:00 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “Segmentations”<br>
[CRITICAL][Qt] 03.06.2023 17:56:20 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - double __cdecl qSlicerSubjectHierarchyFolderPlugin::canOwnSubjectHierarchyItem(__int64) const : Input item is invalid<br>
[WARNING][VTK] 03.06.2023 17:56:20 [vtkMRMLSubjectHierarchyNode (00000237B9D66510)] (D:\D\S\S-0\Libs\MRML\Core\vtkMRMLSubjectHierarchyNode.cxx:2102) - GetItemDataNode: Invalid item ID given</p>
</details>

---

## Post #2 by @lassoan (2023-06-03 17:28 UTC)

<p>How did you try to export it? Into what format?</p>

---

## Post #3 by @simoneb (2023-06-03 21:36 UTC)

<p>I would like to export the segmented organ to one labelmap. As far as I know, I checked export and labelmap and then click “Export”. The “do you want to crop the segmentation”- window popped up, I clicked okay, but then nothing happened.</p>

---

## Post #4 by @lassoan (2023-06-04 19:34 UTC)

<p>The easiest is if you just save the scene (Ctrl-S) and click OK. The segmentation is saved as a standard NRRD file.</p>

---

## Post #5 by @simoneb (2023-06-21 20:04 UTC)

<p>Sorry, for the late reply. Thanks a lot for your help, unfortunately, all I know is that I have to export as a Nifti file.</p>

---

## Post #6 by @lassoan (2023-06-23 11:35 UTC)

<p>“Export” writes the segmentation to a node in the scene. You can then use menu: File / Save and choose nifti format for the exported labelmap volume.</p>
<p>Alternatively, you can use “Export to files” to write the segmentation directly to nifti.</p>
<p>Do you know why you are asked to use the complex and limited nifti file format?  What software will read the nifti file? Most environments where a nifti reader is available, a nrrd reader is available, too.</p>

---

## Post #7 by @simoneb (2023-06-27 12:31 UTC)

<p>Thanks a lot, it worked. I have to process it with ImageJ. I was told to save it as nifti.<br>
Thanks again for you help. I really appreciated it</p>

---

## Post #8 by @lassoan (2023-06-27 12:44 UTC)

<p>Happy to hear that it all works now.</p>
<aside class="quote no-group" data-username="simoneb" data-post="7" data-topic="29814">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/bc8723/48.png" class="avatar"> simoneb:</div>
<blockquote>
<p>I have to process it with ImageJ. I was told to save it as nifti.</p>
</blockquote>
</aside>
<p>You can use SCIFIO plugin in ImageJ to load NRRD files.</p>
<p>ImageJ works nicely for 2D images, but it can barely do anything with 3D images. ImageJ is also limited in that it is implemented in Java, while most new scientific and machine learning developments happen in Python. – What kind of 3D analysis or visualization are you considering doing in ImageJ? Why ImageJ/Java and not Slicer/Python?</p>

---
