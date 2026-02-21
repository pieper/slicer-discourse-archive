---
topic_id: 46229
title: "Lung Ct Segmenter From Chest Imaging Platform Bad Quality Im"
date: 2026-02-20
url: https://discourse.slicer.org/t/46229
---

# Lung CT segmenter from Chest Imaging Platform bad quality image and segmentation

**Topic ID**: 46229
**Date**: 2026-02-20
**URL**: https://discourse.slicer.org/t/lung-ct-segmenter-from-chest-imaging-platform-bad-quality-image-and-segmentation/46229

---

## Post #1 by @Khaldoun (2026-02-20 13:22 UTC)

<p>Problem report for 3D Slicer 5.10.0 win-amd64: [please describe expected and actual behavior]</p>
<p>Since the last update of Total Segmentator the Lung CT segmenter module in Chest Imaging Platform is producing very blurry segmentation of the lung lobes as it is shown in the screen capture below while it was perfectly functionning previously without changing any thing on hardware (Windows 11, no GPU and CPU forced on desktop computer with 13th Gen Intel(R) Core™ i5-13500 2.50GHz; 16.0 Go RAM, and INterl(R) UHD GRaphics 770 128 MB.</p>
<p>Below is the screen shot of the result applied to Chest CT from sample data down load</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b7acc8e7c0288535f2bd1d60899206fa7892466.jpeg" data-download-href="/uploads/short-url/mbr6qvdYMjcFM2lLwaqGc9YcGuW.jpeg?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9b7acc8e7c0288535f2bd1d60899206fa7892466_2_690x491.jpeg" alt="Screenshot" data-base62-sha1="mbr6qvdYMjcFM2lLwaqGc9YcGuW" width="690" height="491" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9b7acc8e7c0288535f2bd1d60899206fa7892466_2_690x491.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9b7acc8e7c0288535f2bd1d60899206fa7892466_2_1035x736.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b7acc8e7c0288535f2bd1d60899206fa7892466.jpeg 2x" data-dominant-color="6E6C6F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">1188×847 167 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>and below copy of the log message</p>
<p>Thank you for your help as I am using Lung CT Segmenter on a daily practice in my hospital</p>
<p>[DEBUG][Qt] 20.02.2026 09:22:47 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Session start time …: 20260220_092247<br>
[DEBUG][Qt] 20.02.2026 09:22:47 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Slicer version …: 5.10.0 (revision 34045 / a2b6d08) win-amd64 - installed release<br>
[DEBUG][Qt] 20.02.2026 09:22:47 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Operating system …: Windows /  Professional / (Build 26200, Code Page 65001) - 64-bit<br>
[DEBUG][Qt] 20.02.2026 09:22:47 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Memory …: 16072 MB physical, 34496 MB virtual<br>
[DEBUG][Qt] 20.02.2026 09:22:47 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - CPU …: GenuineIntel , 20 cores, 20 logical processors<br>
[DEBUG][Qt] 20.02.2026 09:22:47 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 20.02.2026 09:22:47 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Qt configuration …: version 5.15.2, with SSL, requested OpenGL 3.2 (core profile)<br>
[DEBUG][Qt] 20.02.2026 09:22:47 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - DCMTK configuration …: version 3.6.8, no SSL<br>
[DEBUG][Qt] 20.02.2026 09:22:47 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Internationalization …: disabled, language=<br>
[DEBUG][Qt] 20.02.2026 09:22:47 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Developer mode …: disabled<br>
[DEBUG][Qt] 20.02.2026 09:22:47 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Application path …: C:/Users/538827/AppData/Local/slicer.org/3D Slicer 5.10.0/bin<br>
[DEBUG][Qt] 20.02.2026 09:22:47 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Additional module paths ..: <a href="http://slicer.org/Extensions-34045/AirwaySegmentation/lib/Slicer-5.10/cli-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34045/AirwaySegmentation/lib/Slicer-5.10/cli-modules</a>, <a href="http://slicer.org/Extensions-34045/AirwaySegmentation/lib/Slicer-5.10/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34045/AirwaySegmentation/lib/Slicer-5.10/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-34045/PyTorch/lib/Slicer-5.10/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34045/PyTorch/lib/Slicer-5.10/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-34045/SegmentEditorExtraEffects/lib/Slicer-5.10/qt-loadable-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34045/SegmentEditorExtraEffects/lib/Slicer-5.10/qt-loadable-modules</a>, <a href="http://slicer.org/Extensions-34045/SegmentEditorExtraEffects/lib/Slicer-5.10/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34045/SegmentEditorExtraEffects/lib/Slicer-5.10/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-34045/SurfaceWrapSolidify/lib/Slicer-5.10/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34045/SurfaceWrapSolidify/lib/Slicer-5.10/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-34045/LungCTAnalyzer/lib/Slicer-5.10/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34045/LungCTAnalyzer/lib/Slicer-5.10/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-34045/MarkupsToModel/lib/Slicer-5.10/qt-loadable-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34045/MarkupsToModel/lib/Slicer-5.10/qt-loadable-modules</a>, <a href="http://slicer.org/Extensions-34045/NNUNet/lib/Slicer-5.10/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34045/NNUNet/lib/Slicer-5.10/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-34045/TotalSegmentator/lib/Slicer-5.10/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34045/TotalSegmentator/lib/Slicer-5.10/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-34045/SlicerPythonTestRunner/lib/Slicer-5.10/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34045/SlicerPythonTestRunner/lib/Slicer-5.10/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-34045/MONAIAuto3DSeg/lib/Slicer-5.10/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34045/MONAIAuto3DSeg/lib/Slicer-5.10/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-34045/NNInteractive/lib/Slicer-5.10/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34045/NNInteractive/lib/Slicer-5.10/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-34045/NvidiaAIAssistedAnnotation/lib/Slicer-5.10/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34045/NvidiaAIAssistedAnnotation/lib/Slicer-5.10/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-34045/PETTumorSegmentation/lib/Slicer-5.10/qt-loadable-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34045/PETTumorSegmentation/lib/Slicer-5.10/qt-loadable-modules</a>, <a href="http://slicer.org/Extensions-34045/PETTumorSegmentation/lib/Slicer-5.10/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34045/PETTumorSegmentation/lib/Slicer-5.10/qt-scripted-modules</a><br>
[INFO][Stream] 20.02.2026 09:22:48 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) -<br>
[DEBUG][Python] 20.02.2026 09:22:51 [Python] (C:\Users\538827\AppData\Local\slicer.org\3D Slicer 5.10.0\lib\Slicer-5.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:40) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 20.02.2026 09:22:51 [Python] (C:\Users\538827\AppData\Local\slicer.org\3D Slicer 5.10.0\lib\Slicer-5.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:40) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 20.02.2026 09:22:51 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Switch to module:  “Welcome”<br>
[WARNING][VTK] 20.02.2026 09:22:51 [vtkSlicerTerminologiesModuleLogic (00000284F7398D40)] (vtkSlicerTerminologiesModuleLogic.cxx:3370) - LoadAnatomicContextFromFile is deprecated. Use LoadRegionContextFromFile instead.<br>
[INFO][Python] 20.02.2026 09:22:52 [Python] (C:/Users/538827/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/NvidiaAIAssistedAnnotation/lib/Slicer-5.10/qt-scripted-modules/SegmentEditorNvidiaAIAA.py:32) - This plugin dir: C:/Users/538827/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/NvidiaAIAssistedAnnotation/lib/Slicer-5.10/qt-scripted-modules<br>
[WARNING][VTK] 20.02.2026 09:22:52 [vtkSlicerTerminologiesModuleLogic (00000284F7398D40)] (vtkSlicerTerminologiesModuleLogic.cxx:3370) - LoadAnatomicContextFromFile is deprecated. Use LoadRegionContextFromFile instead.<br>
[DEBUG][Qt] 20.02.2026 10:55:54 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Switch to module:  “SampleData”<br>
[DEBUG][Qt] 20.02.2026 10:56:27 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Switch to module:  “DICOM”<br>
[DEBUG][Qt] 20.02.2026 10:56:34 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Switch to module:  “Welcome”<br>
[DEBUG][Qt] 20.02.2026 10:56:35 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Switch to module:  “SampleData”<br>
[DEBUG][Python] 20.02.2026 10:56:36 [Python] (C:/Users/538827/AppData/Local/slicer.org/3D Slicer 5.10.0/bin/../lib/Slicer-5.10/qt-scripted-modules/SampleData.py:461) - Verifying checksum<br>
[DEBUG][Python] 20.02.2026 10:56:36 [Python] (C:/Users/538827/AppData/Local/slicer.org/3D Slicer 5.10.0/bin/../lib/Slicer-5.10/qt-scripted-modules/SampleData.py:461) - File already exists and checksum is OK - reusing it.<br>
[DEBUG][Python] 20.02.2026 10:56:36 [Python] (C:/Users/538827/AppData/Local/slicer.org/3D Slicer 5.10.0/bin/../lib/Slicer-5.10/qt-scripted-modules/SampleData.py:461) - Requesting load CTChest from C:/Users/538827/AppData/Local/slicer.org/Slicer/cache/SlicerIO/CT-chest.nrrd …<br>
[DEBUG][Qt] 20.02.2026 10:56:37 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - “Volume” Reader has successfully read the file “C:/Users/538827/AppData/Local/slicer.org/Slicer/cache/SlicerIO/CT-chest.nrrd” “[0.36s]”<br>
[DEBUG][Python] 20.02.2026 10:56:37 [Python] (C:/Users/538827/AppData/Local/slicer.org/3D Slicer 5.10.0/bin/../lib/Slicer-5.10/qt-scripted-modules/SampleData.py:461) - Load finished<br>
[DEBUG][Qt] 20.02.2026 10:57:00 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Switch to module:  “LungCTSegmenter”<br>
[INFO][VTK] 20.02.2026 10:57:11 [vtkSlicerCLIModuleLogic (00000284F88484E0)] (C:\D\S\S-0\Base\Logic\vtkSlicerCLIModuleLogic.cxx:844) - Found CommandLine Module, target is C:/Users/538827/AppData/Local/slicer.org/3D Slicer 5.10.0/bin/../lib/Slicer-5.10/cli-modules/ResampleScalarVolume.exe<br>
[INFO][VTK] 20.02.2026 10:57:11 [vtkSlicerCLIModuleLogic (00000284F88484E0)] (C:\D\S\S-0\Base\Logic\vtkSlicerCLIModuleLogic.cxx:862) - ModuleType: CommandLineModule<br>
[INFO][VTK] 20.02.2026 10:57:12 [vtkSlicerCLIModuleLogic (00000284F88484E0)] (C:\D\S\S-0\Base\Logic\vtkSlicerCLIModuleLogic.cxx:1690) - Resample Scalar Volume command line:</p>
<p>C:/Users/538827/AppData/Local/slicer.org/3D Slicer 5.10.0/bin/../lib/Slicer-5.10/cli-modules/ResampleScalarVolume.exe --spacing 2.0,2.0,2.0 --interpolation linear C:/Users/538827/AppData/Local/Temp/Slicer/CAAIE_vtkMRMLScalarVolumeNodeB.nrrd C:/Users/538827/AppData/Local/Temp/Slicer/CAAIE_vtkMRMLScalarVolumeNodeC.nrrd<br>
[INFO][VTK] 20.02.2026 10:57:12 [vtkSlicerCLIModuleLogic (00000284F88484E0)] (C:\D\S\S-0\Base\Logic\vtkSlicerCLIModuleLogic.cxx:1894) - Resample Scalar Volume completed without errors<br>
[WARNING][Qt] 20.02.2026 10:57:12 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - QLayout::addChildLayout: layout “” already has a parent<br>
[WARNING][Qt] 20.02.2026 10:57:12 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - libpng warning: iCCP: known incorrect sRGB profile<br>
[WARNING][Qt] 20.02.2026 10:57:12 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - ctkSliderWidget::setSingleStep()  0 is out of bounds. 0 1000 1<br>
[INFO][Python] 20.02.2026 10:57:12 [Python] (C:/Users/538827/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/LungCTAnalyzer/lib/Slicer-5.10/qt-scripted-modules/LungCTSegmenter.py:1555) - StartSegmentation completed in 1.28 seconds<br>
[INFO][Python] 20.02.2026 10:57:13 [Python] (C:/Users/538827/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/LungCTAnalyzer/lib/Slicer-5.10/qt-scripted-modules/LungCTSegmenter.py:1126) - Saving markups in temp directory …<br>
[INFO][Stream] 20.02.2026 10:57:19 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Torch version:<br>
[INFO][Python] 20.02.2026 10:57:19 [Python] (C:/Users/538827/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/PyTorch/lib/Slicer-5.10/qt-scripted-modules/PyTorchUtils.py:153) - Importing torch…<br>
[INFO][Python] 20.02.2026 10:57:21 [Python] (C:/Users/538827/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/PyTorch/lib/Slicer-5.10/qt-scripted-modules/PyTorchUtils.py:190) - PyTorch 2.10.0+cpu imported successfully<br>
[INFO][Python] 20.02.2026 10:57:21 [Python] (C:/Users/538827/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/PyTorch/lib/Slicer-5.10/qt-scripted-modules/PyTorchUtils.py:191) - CUDA available: False<br>
[INFO][Stream] 20.02.2026 10:57:21 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - 2.10.0+cpu<br>
[INFO][Python] 20.02.2026 10:57:21 [Python] (C:/Users/538827/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/LungCTAnalyzer/lib/Slicer-5.10/qt-scripted-modules/LungCTSegmenter.py:2296) - Pytorch CUDA is not available. AI will use CPU processing.<br>
[INFO][Python] 20.02.2026 10:57:21 [Python] (C:\Users\538827\AppData\Local\slicer.org\3D Slicer 5.10.0\bin\Python\slicer\util.py:3146) - Warning: Pytorch CUDA is not found on your system. The AI processing will last 3-10 minutes. Are you sure you want to continue AI segmentation?<br>
[WARNING][Qt] 20.02.2026 11:26:22 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - ctkSliderWidget::setSingleStep()  0 is out of bounds. 0 100 1<br>
[INFO][Python] 20.02.2026 11:26:23 [Python] (C:/Users/538827/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/TotalSegmentator/lib/Slicer-5.10/qt-scripted-modules/TotalSegmentator.py:677) - Processing started<br>
[INFO][Python] 20.02.2026 11:26:23 [Python] (C:/Users/538827/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/TotalSegmentator/lib/Slicer-5.10/qt-scripted-modules/TotalSegmentator.py:677) - Writing input file to C:/Users/538827/AppData/Local/Temp/Slicer/__SlicerTemp__2026-02-20_11+26+23.843/total-segmentator-input.nii<br>
[INFO][Python] 20.02.2026 11:26:24 [Python] (C:/Users/538827/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/TotalSegmentator/lib/Slicer-5.10/qt-scripted-modules/TotalSegmentator.py:677) - Creating segmentations with TotalSegmentator AI…<br>
[INFO][Python] 20.02.2026 11:26:24 [Python] (C:/Users/538827/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/TotalSegmentator/lib/Slicer-5.10/qt-scripted-modules/TotalSegmentator.py:677) - Total Segmentator arguments: [‘-i’, ‘C:/Users/538827/AppData/Local/Temp/Slicer/__SlicerTemp__2026-02-20_11+26+23.843/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/538827/AppData/Local/Temp/Slicer/__SlicerTemp__2026-02-20_11+26+23.843/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–fastest’]<br>
[INFO][Python] 20.02.2026 11:26:45 [Python] (C:/Users/538827/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/TotalSegmentator/lib/Slicer-5.10/qt-scripted-modules/TotalSegmentator.py:677) -<br>
[INFO][Python] 20.02.2026 11:26:46 [Python] (C:/Users/538827/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/TotalSegmentator/lib/Slicer-5.10/qt-scripted-modules/TotalSegmentator.py:677) -   0%|          | 0/4 [00:00&lt;?, ?it/s]<br>
[INFO][Python] 20.02.2026 11:26:46 [Python] (C:/Users/538827/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/TotalSegmentator/lib/Slicer-5.10/qt-scripted-modules/TotalSegmentator.py:677) -  25%|#<span class="hashtag-raw">#5</span>       | 1/4 [00:00&lt;00:02,  1.29it/s]<br>
[INFO][Python] 20.02.2026 11:26:47 [Python] (C:/Users/538827/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/TotalSegmentator/lib/Slicer-5.10/qt-scripted-modules/TotalSegmentator.py:677) -  50%|#####     | 2/4 [00:01&lt;00:01,  1.45it/s]<br>
[INFO][Python] 20.02.2026 11:26:47 [Python] (C:/Users/538827/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/TotalSegmentator/lib/Slicer-5.10/qt-scripted-modules/TotalSegmentator.py:677) -  75%|######<span class="hashtag-raw">#5</span>  | 3/4 [00:01&lt;00:00,  1.62it/s]<br>
[INFO][Python] 20.02.2026 11:26:47 [Python] (C:/Users/538827/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/TotalSegmentator/lib/Slicer-5.10/qt-scripted-modules/TotalSegmentator.py:677) - 100%|##########| 4/4 [00:02&lt;00:00,  1.75it/s]<br>
[INFO][Python] 20.02.2026 11:26:47 [Python] (C:/Users/538827/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/TotalSegmentator/lib/Slicer-5.10/qt-scripted-modules/TotalSegmentator.py:677) - 100%|##########| 4/4 [00:02&lt;00:00,  1.64it/s]<br>
[INFO][Python] 20.02.2026 11:26:52 [Python] (C:/Users/538827/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/TotalSegmentator/lib/Slicer-5.10/qt-scripted-modules/TotalSegmentator.py:677) - No GPU detected. Running on CPU. This can be very slow. The ‘–fast’ or the <code>--roi_subset</code> option can help to reduce runtime.<br>
[INFO][Python] 20.02.2026 11:26:52 [Python] (C:/Users/538827/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/TotalSegmentator/lib/Slicer-5.10/qt-scripted-modules/TotalSegmentator.py:677) -<br>
[INFO][Python] 20.02.2026 11:26:52 [Python] (C:/Users/538827/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/TotalSegmentator/lib/Slicer-5.10/qt-scripted-modules/TotalSegmentator.py:677) - If you use this tool please cite: <a href="https://pubs.rsna.org/doi/10.1148/ryai.230024" rel="noopener nofollow ugc">https://pubs.rsna.org/doi/10.1148/ryai.230024</a><br>
[INFO][Python] 20.02.2026 11:26:52 [Python] (C:/Users/538827/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/TotalSegmentator/lib/Slicer-5.10/qt-scripted-modules/TotalSegmentator.py:677) -<br>
[INFO][Python] 20.02.2026 11:26:52 [Python] (C:/Users/538827/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/TotalSegmentator/lib/Slicer-5.10/qt-scripted-modules/TotalSegmentator.py:677) - Using ‘fastest’ option: resampling to lower resolution (6mm)<br>
[INFO][Python] 20.02.2026 11:26:52 [Python] (C:/Users/538827/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/TotalSegmentator/lib/Slicer-5.10/qt-scripted-modules/TotalSegmentator.py:677) - Resampling…<br>
[INFO][Python] 20.02.2026 11:26:52 [Python] (C:/Users/538827/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/TotalSegmentator/lib/Slicer-5.10/qt-scripted-modules/TotalSegmentator.py:677) -   Resampled in 1.64s<br>
[INFO][Python] 20.02.2026 11:26:52 [Python] (C:/Users/538827/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/TotalSegmentator/lib/Slicer-5.10/qt-scripted-modules/TotalSegmentator.py:677) - Predicting…<br>
[INFO][Python] 20.02.2026 11:26:52 [Python] (C:/Users/538827/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/TotalSegmentator/lib/Slicer-5.10/qt-scripted-modules/TotalSegmentator.py:677) -   Predicted in 14.09s<br>
[INFO][Python] 20.02.2026 11:26:52 [Python] (C:/Users/538827/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/TotalSegmentator/lib/Slicer-5.10/qt-scripted-modules/TotalSegmentator.py:677) - Resampling…<br>
[INFO][Python] 20.02.2026 11:26:52 [Python] (C:/Users/538827/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/TotalSegmentator/lib/Slicer-5.10/qt-scripted-modules/TotalSegmentator.py:677) - Saving segmentations…<br>
[INFO][Python] 20.02.2026 11:26:52 [Python] (C:/Users/538827/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/TotalSegmentator/lib/Slicer-5.10/qt-scripted-modules/TotalSegmentator.py:677) -   Saved in 0.43s<br>
[INFO][Python] 20.02.2026 11:26:53 [Python] (C:/Users/538827/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/TotalSegmentator/lib/Slicer-5.10/qt-scripted-modules/TotalSegmentator.py:677) - Importing segmentation results…<br>
[INFO][VTK] 20.02.2026 11:26:53 [vtkMRMLSegmentationStorageNode (00000285137BD930)] (C:\D\S\S-0\Libs\MRML\Core\vtkMRMLSegmentationStorageNode.cxx:608) - ReferenceImageExtentOffset attribute was not found in NRRD segmentation file. Assume no offset.<br>
[INFO][Python] 20.02.2026 11:26:53 [Python] (C:/Users/538827/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/TotalSegmentator/lib/Slicer-5.10/qt-scripted-modules/TotalSegmentator.py:677) - Processing completed in 30.01 seconds<br>
[INFO][Python] 20.02.2026 11:26:53 [Python] (C:/Users/538827/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/TotalSegmentator/lib/Slicer-5.10/qt-scripted-modules/TotalSegmentator.py:677) - Cleaning up temporary folder…<br>
[ERROR][VTK] 20.02.2026 12:42:59 [vtkCompositeDataPipeline (000002849F0468C0)] (vtkDemandDrivenPipeline.cxx:677) - Input port 0 of algorithm vtkTransformPolyDataFilter (000002848908F130) has 0 connections but is not optional.<br>
[ERROR][VTK] 20.02.2026 12:42:59 [vtkCompositeDataPipeline (000002849F0468C0)] (vtkDemandDrivenPipeline.cxx:677) - Input port 0 of algorithm vtkTransformPolyDataFilter (000002848908F130) has 0 connections but is not optional.<br>
[ERROR][VTK] 20.02.2026 12:42:59 [vtkCompositeDataPipeline (000002849F0468C0)] (vtkDemandDrivenPipeline.cxx:677) - Input port 0 of algorithm vtkTransformPolyDataFilter (000002848908F130) has 0 connections but is not optional.<br>
[ERROR][VTK] 20.02.2026 12:42:59 [vtkCompositeDataPipeline (000002849F0468C0)] (vtkDemandDrivenPipeline.cxx:677) - Input port 0 of algorithm vtkTransformPolyDataFilter (000002848908F130) has 0 connections but is not optional.<br>
[ERROR][VTK] 20.02.2026 12:43:00 [vtkCompositeDataPipeline (000002849F0468C0)] (vtkDemandDrivenPipeline.cxx:677) - Input port 0 of algorithm vtkTransformPolyDataFilter (000002848908F130) has 0 connections but is not optional.<br>
[ERROR][VTK] 20.02.2026 12:43:00 [vtkCompositeDataPipeline (000002849F0468C0)] (vtkDemandDrivenPipeline.cxx:677) - Input port 0 of algorithm vtkTransformPolyDataFilter (000002848908F130) has 0 connections but is not optional.<br>
[ERROR][VTK] 20.02.2026 12:43:00 [vtkCompositeDataPipeline (000002849F0468C0)] (vtkDemandDrivenPipeline.cxx:677) - Input port 0 of algorithm vtkTransformPolyDataFilter (000002848908F130) has 0 connections but is not optional.<br>
[ERROR][VTK] 20.02.2026 12:43:00 [vtkCompositeDataPipeline (000002849F0468C0)] (vtkDemandDrivenPipeline.cxx:677) - Input port 0 of algorithm vtkTransformPolyDataFilter (000002848908F130) has 0 connections but is not optional.<br>
[INFO][Stream] 20.02.2026 12:43:00 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Reference: left deep back muscle<br>
[ERROR][VTK] 20.02.2026 12:43:00 [vtkCompositeDataPipeline (000002849F0468C0)] (vtkDemandDrivenPipeline.cxx:677) - Input port 0 of algorithm vtkTransformPolyDataFilter (000002848908F130) has 0 connections but is not optional.<br>
[WARNING][Qt] 20.02.2026 12:43:00 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - ctkSliderWidget::setSingleStep()  0 is out of bounds. 0 100 1<br>
[INFO][Stream] 20.02.2026 12:43:01 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Mean radiodensity of trachea = -787.13 HU<br>
[INFO][Stream] 20.02.2026 12:43:01 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Mean radiodensity of deep back muscle muscle = 38.24 HU<br>
[WARNING][VTK] 20.02.2026 12:43:01 [vtkMRMLMarkupsFiducialNode (00000284FECA49C0)] (vtkMRMLMarkupsFiducialNode.h:113) - vtkMRMLMarkupsFiducialNode::AddFiducialFromArray method is deprecated, please use AddControlPoint instead<br>
[INFO][Python] 20.02.2026 12:43:02 [Python] (C:/Users/538827/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/LungCTAnalyzer/lib/Slicer-5.10/qt-scripted-modules/LungCTSegmenter.py:2565) - Segmentation done.<br>
[ERROR][VTK] 20.02.2026 12:43:03 [vtkImageData (0000028516D7D780)] (vtkImageData.cxx:2082) - GetPointer: Pixel (0, 0, 0) not in current extent: (0, -1, 0, -1, 0, -1)<br>
[ERROR][Python] 20.02.2026 12:43:03 [Python] (C:\Users\538827\AppData\Local\slicer.org\3D Slicer 5.10.0\lib\Slicer-5.10\qt-scripted-modules\SegmentStatisticsPlugins\LabelmapSegmentStatisticsPlugin.py:177) - Could not calculate centroid_ras!<br>
[INFO][Stream] 20.02.2026 12:43:03 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Median radiodensity of lungs = -865.00 HU<br>
[INFO][Stream] 20.02.2026 12:43:03 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - MaximumThreshold: -865.0<br>
[INFO][Stream] 20.02.2026 12:43:03 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - MinimumThreshold: -3024.0<br>
[INFO][Stream] 20.02.2026 12:43:03 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - IJK trachea markup<br>
[INFO][Stream] 20.02.2026 12:43:03 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - [261, 234, 108]<br>
[INFO][Python] 20.02.2026 12:43:14 [Python] (C:/Users/538827/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/LungCTAnalyzer/lib/Slicer-5.10/qt-scripted-modules/LungCTSegmenter.py:2925) - ApplySegmentation completed in 6361.95 seconds<br>
[INFO][Stream] 20.02.2026 12:43:14 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Segmentation completed in 6361.95 seconds<br>
[WARNING][VTK] 20.02.2026 12:43:15 [vtkMRMLSegmentationDisplayNode (000002848B674010)] (vtkMRMLSegmentationDisplayNode.cxx:294) - vtkMRMLSegmentationDisplayNode::GetSegmentDisplayProperties: no display properties are found for segment ID=, return default<br>
[DEBUG][Qt] 20.02.2026 12:44:17 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Switch to module:  “Data”<br>
[DEBUG][Qt] 20.02.2026 13:24:59 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Switch to module:  “Welcome”<br>
[DEBUG][Qt] 20.02.2026 13:25:00 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Switch to module:  “SampleData”<br>
[DEBUG][Qt] 20.02.2026 14:17:47 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Switch to module:  “Welcome”<br>
[DEBUG][Qt] 20.02.2026 14:17:48 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Switch to module:  “SampleData”</p>

---

## Post #2 by @pieper (2026-02-20 16:16 UTC)

<p>I’m not sure why this resolution would have changed, by you could try reporting on github issues for either <a href="https://github.com/wasserth/TotalSegmentator/issues">TotalSegmentator</a> or the <a href="https://github.com/lassoan/SlicerTotalSegmentator/issues">Slicer extension</a>.</p>
<p>In the meantime you could just install the <a href="https://slicer-packages.kitware.com/#collection/5f4474d0e1d8c75dfc70547e/folder/5f4474d0e1d8c75dfc705482">older release version.</a></p>

---

## Post #3 by @jamesobutler (2026-02-20 17:26 UTC)

<aside class="quote no-group" data-username="Khaldoun" data-post="1" data-topic="46229">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/3ab097/48.png" class="avatar"> Khaldoun:</div>
<blockquote>
<p>Total Segmentator arguments: [‘-i’, ‘C:/Users/538827/AppData/Local/Temp/Slicer/__SlicerTemp__2026-02-20_11+26+23.843/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/538827/AppData/Local/Temp/Slicer/__SlicerTemp__2026-02-20_11+26+23.843/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–fastest’]</p>
</blockquote>
</aside>
<p>^Isn’t this just using the new <code>--fastest</code> option which is the lower resolution (6mm) option?</p>
<p>It was part of latest commit of SlicerTotalSegmentator:</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/lassoan/SlicerTotalSegmentator/commit/a1f8b4a4f902fd101a54a100231770e7406040f9">
  <header class="source">

      <a href="https://github.com/lassoan/SlicerTotalSegmentator/commit/a1f8b4a4f902fd101a54a100231770e7406040f9" target="_blank" rel="noopener nofollow ugc">github.com/lassoan/SlicerTotalSegmentator</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/lassoan/SlicerTotalSegmentator/commit/a1f8b4a4f902fd101a54a100231770e7406040f9" target="_blank" rel="noopener nofollow ugc">Update TotalSegmentator to v2.12.0</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2026-02-12" data-time="14:33:45" data-timezone="UTC">02:33PM - 12 Feb 26 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/mhalle" target="_blank" rel="noopener nofollow ugc">
          <img alt="" src="https://avatars.githubusercontent.com/u/649467?v=4" class="onebox-avatar-inline" width="20" height="20">
          mhalle
        </a>
      </div>

      <div class="lines" title="changed 4 files with 972 additions and 59 deletions">
        <a href="https://github.com/lassoan/SlicerTotalSegmentator/commit/a1f8b4a4f902fd101a54a100231770e7406040f9" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+972</span>
          <span class="removed">-59</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Summary:

Update version pin to v2.12.0 (commit a4a906) and bump minimum
depende<span class="show-more-container"><a href="https://github.com/lassoan/SlicerTotalSegmentator/commit/a1f8b4a4f902fd101a54a100231770e7406040f9" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">ncy versions (torch&gt;=2.1.2, nnunetv2&gt;=2.3.1).

Add 5 new segmentation tasks:
- craniofacial_structures
- abdominal_muscles
- teeth (77 classes)
- trunk_cavities
- brain_aneurysm (TOF MRI)

Expose new CLI options in the UI: fastest mode (6mm), robust cropping,
remove small blobs, and higher-order resampling.

Add Apple Silicon (MPS) GPU device detection and pass --device mps
when available.

Add SNOMED-CT mappings and terminology entries for all new structures
(~109 new labels). Fix pre-existing bug where Fast mode default used
wrong case ("True" vs "true"), and fix pericardium SNOMED code
collision with breast (76752008 -&gt; 76848001).

Detailed report:

---

# Porting SlicerTotalSegmentator to TotalSegmentator v2.12.0

## Overview

This document describes the changes made to port the SlicerTotalSegmentator
3D Slicer extension from its previous TotalSegmentator version (~v2.6.0/v2.9.0
depending on Python version) to **TotalSegmentator v2.12.0**. The work is
tracked in PR #81 on `lassoan/SlicerTotalSegmentator`.

---

## What Was Done

### 1. Version Pin Update

**File:** `TotalSegmentator/TotalSegmentator.py` (line ~400)

The extension previously maintained two separate commit-hash pins depending on
the Python version:

- Python &lt; 3.12 (Slicer 5.8-): commit `25a8586` (~v2.6.0)
- Python &gt;= 3.12 (Slicer 5.9+): commit `0a1c3c3` (~v2.9.0)

Both were replaced with a single pin to v2.12.0:

```python
self.totalSegmentatorPythonPackageDownloadUrl = \
    "https://github.com/wasserth/TotalSegmentator/archive/a4a9060012a4b7c39d15fe93772af3f7c1239fbf.zip"  # v2.12.0
```

The Python-version branching was removed because v2.12.0 supports both
Python 3.9 and 3.12+.

### 2. Dependency Version Bumps

**File:** `TotalSegmentator/TotalSegmentator.py` (lines ~809, ~819)

| Dependency | Previous Min | New Min |
|-----------|-------------|---------|
| torch     | &gt;= 2.0.0    | &gt;= 2.1.2 |
| nnunetv2  | &gt;= 2.2.1    | &gt;= 2.3.1 |

These match the requirements of TotalSegmentator v2.12.0.

### 3. Seven New Segmentation Tasks

**File:** `TotalSegmentator/TotalSegmentator.py` (lines ~476-483)

Five new tasks were added:

| Task ID | Title | Modality | Labels | License | Notes |
|---------|-------|----------|--------|---------|-------|
| `craniofacial_structures` | head: craniofacial structures | CT | 7 | Open | New |
| `abdominal_muscles` | abdominal muscles | CT | 22 | Open | New, bilateral muscles |
| `teeth` | teeth | CT | 77 | Open | New, FDI-numbered teeth + pulps |
| `trunk_cavities` | trunk cavities | CT | 4 | Open | New |
| `brain_aneurysm` | brain: aneurysm (TOF MRI) | **MR** | 1 | Open | New, TOF MRI only |

**Total new labels across all 7 tasks: 127**

None of the new tasks support `fast` or `fastest` mode. The `teeth` task
internally cascades through `craniofacial_structures` for cropping, but this
is handled entirely by TotalSegmentator itself -- no Slicer-side logic needed.

### 4. SNOMED-CT Mappings

**File:** `TotalSegmentator/Resources/totalsegmentator_snomed_mapping.csv`

Added ~109 new rows mapping TotalSegmentator structure names to SNOMED-CT codes.
Each row specifies:

- Structure name (must match TotalSegmentator's `class_map` label exactly)
- Category (Anatomical Structure, Morphologically Altered Structure, etc.)
- Type (SNOMED code for the anatomical structure)
- Type modifier (laterality: Left/Right where applicable)
- Region and region modifier (for non-anatomical categories like dental pulp)
- Display color (RGB)

**Breakdown by task:**

| Task | New CSV Rows | Notes |
|------|-------------|-------|
| `craniofacial_structures` | 6 | `skull` already existed |
| `abdominal_muscles` | 20 | `trapezius_right/left` already existed from `headneck_muscles` |
| `teeth` | 77 | Jawbones, canals, 32 teeth, 32 pulps, bridge/crown/implant, pharynx |
| `trunk_cavities` | 4 | abdominal_cavity, thoracic_cavity, pericardium, mediastinum |
| `brain_aneurysm` | 1 | Uses "Morphologically Altered Structure" category |
| `ventricle_parts` | 0 | All 12 labels already had mappings |
| `aortic_sinuses` | 0 | All 4 labels already had mappings |

**Cross-reference verification:** A script was run to confirm that every label
in TotalSegmentator's `class_map` for all 7 tasks has a corresponding CSV
entry. No missing or duplicate names exist.

### 5. Terminology JSON

**File:** `TotalSegmentator/Resources/SegmentationCategoryTypeModifier-TotalSegmentator.term.json`

Added terminology entries for all new structures under the appropriate
categories:

- **Anatomical Structure** (SCT 123037004): ~30 new Type entries including
  mandible, maxilla, maxillary sinus (paired), frontal sinus, head, tooth
  types (central incisor through third molar, all paired), muscles (pectoralis
  major, rectus abdominis, latissimus dorsi, external/internal oblique,
  erector spinae, transversospinalis, psoas major, quadratus lumborum -- all
  paired), dental structures (dental pulp, inferior alveolar nerve, lingual
  canal, dental prosthesis, dental crown, implant), and cavities (abdominal,
  thoracic, pericardium, mediastinum).

- **Morphologically Altered Structure** (SCT 49755003): 1 new entry for
  cerebral aneurysm.

Each entry includes `recommendedDisplayRGBValue`, `3dSlicerLabel`, laterality
modifiers where applicable, and SNOMED concept IDs.

### 6. New UI Controls

**File:** `TotalSegmentator/Resources/UI/TotalSegmentator.ui`

Added the following widgets:

| Widget | Section | Type | Notes |
|--------|---------|------|-------|
| `fastestCheckBox` + `fastestNotAvailableLabel` | Inputs | Checkbox + Label | Only visible for `total` and `total_mr` |
| `robustCropCheckBox` | Advanced | Checkbox | "Use 3mm model for cropping" |
| `removeSmallBlobsCheckBox` | Advanced | Checkbox | "Remove regions &lt; 0.2 ml" |
| `higherOrderResamplingCheckBox` | Advanced | Checkbox | "Smoother but more memory" |

The `fastest` row follows the same visibility pattern as the existing `fast`
row: checkbox shown when supported, "not available" label shown otherwise.

### 7. Python Logic Updates

**File:** `TotalSegmentator/TotalSegmentator.py`

#### Widget connections (lines ~106-113)
All new checkboxes connected to `updateParameterNodeFromGUI`.

#### Parameter node persistence (lines ~216-269)
All new parameters (`Fastest`, `RobustCrop`, `RemoveSmallBlobs`,
`HigherOrderResampling`, `Statistics`) are read from and written to the
MRML parameter node, preserving user settings across scene save/load.

#### `isFastestModeSupportedForTask()` (line ~593)
New method mirroring the existing `isFastModeSupportedForTask()`.

#### `process()` signature (line ~983)
Extended with keyword arguments: `fastest`, `robustCrop`, `removeSmallBlobs`,
`higherOrderResampling`, `statistics`.

#### `processVolume()` CLI argument building (lines ~1143-1166)
- `--fastest` and `--fast` are mutually exclusive (fastest takes priority)
- `--device` flag supports `gpu` (default), `cpu`, and `mps`
- New flags: `--robust_crop`, `--remove_small_blobs`,
  `--higher_order_resampling`, `--statistics`

### 8. Apple Silicon (MPS) Device Detection

**File:** `TotalSegmentator/TotalSegmentator.py` (lines ~1028-1056)

Added detection of Apple Metal Performance Shaders (MPS) as a third GPU
backend alongside CUDA:

```python
cuda = torch.cuda if torch.backends.cuda.is_built() and torch.cuda.is_available() else None
mps = hasattr(torch.backends, 'mps') and torch.backends.mps.is_available()
hasGPU = cuda is not None or mps
```

Device selection priority: user-forced CPU &gt; MPS &gt; CUDA GPU.

The "no GPU" and "low GPU memory" interactive warnings were updated to account
for both `fast` and `fastest` modes. The GPU memory check only applies to CUDA
(MPS does not expose a comparable memory reporting API).

### 9. Bug Fixes

#### Fix 1: Pericardium SNOMED code collision (Critical)

The `pericardium` entry in the CSV used SNOMED code `76752008`, which is
actually "Breast structure" (already used by the `breast` entry on line 301).
Changed to `76848001` (Pericardial sac structure) in both the CSV and the
terminology JSON.

#### Fix 2: Orphaned trapezius CSV entries (Medium)

Added `trapezius_right_abdominal` and `trapezius_left_abdominal` entries, but
TotalSegmentator's `abdominal_muscles` class_map uses `trapezius_right` and
`trapezius_left` -- which were already mapped from the `headneck_muscles` task.
The `_abdominal` suffixed entries would never match any output. Removed them.

#### Fix 3: Fast mode default case mismatch (Medium, pre-existing)

`setDefaultParameters()` set `"True"` (capital T) for the Fast parameter, but
`updateGUIFromParameterNode()` compared against `"true"` (lowercase). This
meant the Fast checkbox was effectively OFF by default on first module load.
Changed to lowercase `"true"`.

---

## What Remains To Be Done

### High Priority

#### Terminology Completeness Audit

While all 127 new labels have SNOMED mappings, a thorough audit should verify:

- All SNOMED codes are semantically correct (not just syntactically valid)
- The `implant` entry (teeth task) uses "Anatomical Structure" category but
  should arguably use "Physical object" (260787004) for consistency with
  `hip_implant`. Low impact since DICOM master list fallback handles it.
- Dental pulp Region entries reference specific tooth types via SNOMED -- these
  should be spot-checked against the SNOMED CT browser.

### Medium Priority

#### Modality Auto-Detection for Task Filtering

The task metadata already includes `modalities` (CT, MR). After the user
selects an input volume, the module could:

- Detect whether the volume is CT or MR (from DICOM metadata or volume
  properties)
- Filter or highlight the task dropdown to show only compatible tasks
- Show a warning if the user selects a task incompatible with the input
  modality (e.g., `brain_aneurysm` on a CT volume)

This is a UI convenience enhancement, not a functional requirement.

### Low Priority

#### Expose `--body_seg` Option

Controls whether to use body segmentation for cropping. Advanced users might
want to disable this for non-standard anatomies.

#### Expose `--quiet` / `--verbose` Logging Levels

TotalSegmentator supports `--quiet` and `--verbose` flags. Could be tied to
Slicer's logging level.

## Reference Material

| Source | Purpose |
|--------|---------|
| `TotalSegmentator/totalsegmentator/python_api.py` | Task definitions (resample, trainer, crop, model, folds) |
| `TotalSegmentator/totalsegmentator/map_to_binary.py` | Label value-to-name mappings per task |
| `TotalSegmentator/totalsegmentator/bin/TotalSegmentator.py` | CLI argument definitions |
| `TotalSegmentator/CHANGELOG.md` | Version history v2.9.0 through v2.12.0 |

## Testing

The following should be verified before merging:

1. Load extension in Slicer -- all tasks appear in dropdown including 7 new ones
2. Trigger package install -- confirms v2.12.0 is downloaded
3. Run `total` task on a CT volume -- basic segmentation works end-to-end
4. Run a new task (e.g., `trunk_cavities`) -- segments load with correct names/colors
5. `fastest` checkbox visible only for `total` and `total_mr`
6. Advanced options pass correct CLI flags
7. Fast checkbox defaults to ON for new parameter nodes
8. On Apple Silicon: MPS detection works and `--device mps` is passed

---

Co-Authored-By: Claude Opus 4.6 &lt;noreply@anthropic.com&gt;
Co-Authored-By: Andras Lasso &lt;lasso@queensu.ca&gt;</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @Khaldoun (2026-02-20 19:06 UTC)

<p>Hi Steve, thank you for your quick reply. I will try reporting on github issues for both even if I a not used to it but I will give it a try. Meantime, I am back to the latest relase version that I have kept installed ! Thank you once more</p>

---

## Post #5 by @Khaldoun (2026-02-20 19:12 UTC)

<p>Hi James, Thank you for your quick reply and suggestion. As I told Steve I am phycisian with poor knowledge in python and github etc.. even if I am learning and improving but you are probably right so I will try to use the faster, fast and normal option on the Chest CT demo with total segmentator and see what it will look like. Still I dont know how to set “normal” on Lung CT Segment module in Chest Imaging Platform. Thaks again</p>

---
