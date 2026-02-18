# Segment editor has disappeared from the screen

**Topic ID**: 19350
**Date**: 2021-08-25
**URL**: https://discourse.slicer.org/t/segment-editor-has-disappeared-from-the-screen/19350

---

## Post #1 by @11122 (2021-08-25 04:48 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/327fd2b9eeb0ccb28a8b556e85287051f5b45f77.png" data-download-href="/uploads/short-url/7cJJt1C4LSlhBAN43uACNHh7Hxl.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/327fd2b9eeb0ccb28a8b556e85287051f5b45f77_2_690x125.png" alt="image" data-base62-sha1="7cJJt1C4LSlhBAN43uACNHh7Hxl" width="690" height="125" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/327fd2b9eeb0ccb28a8b556e85287051f5b45f77_2_690x125.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/327fd2b9eeb0ccb28a8b556e85287051f5b45f77.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/327fd2b9eeb0ccb28a8b556e85287051f5b45f77.png 2x" data-dominant-color="898080"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">759×138 9.63 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ff058e2f80ea99695876b880071a472ed0f52926.png" data-download-href="/uploads/short-url/Ao1EKYcabKxfMczk8kivNmw6Jng.png?dl=1" title="スクリーンショット 2021-08-25 133442 2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff058e2f80ea99695876b880071a472ed0f52926_2_355x500.png" alt="スクリーンショット 2021-08-25 133442 2" data-base62-sha1="Ao1EKYcabKxfMczk8kivNmw6Jng" width="355" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff058e2f80ea99695876b880071a472ed0f52926_2_355x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ff058e2f80ea99695876b880071a472ed0f52926.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ff058e2f80ea99695876b880071a472ed0f52926.png 2x" data-dominant-color="BEBEBF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">スクリーンショット 2021-08-25 133442 2</span><span class="informations">500×703 26.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The 3DSlicer segmentation editor has disappeared from the screen, but if you know how to return it, please let me know.<br>
I also tried uninstalling it, but it will remain gone even if I re-download it.</p>
<p><em>(translated by Google Translate)</em></p>
<details>
<summary>
original text</summary>
<p>3DSlicerのsegmentation editorが画面上から消えてしまったのですが戻す方法がわかる方いらっしゃいましたら教えてください。<br>
アンインストールも試しましたが、再ダウンロードしても消えたままになってしまいます。</p>
</details>

---

## Post #2 by @pieper (2021-08-25 17:45 UTC)

<p>Look for any messages in the log (under Help-&gt;Report a bug) and copy anything you find or the whole log here.  Also try the instructions linked below, in particular this part: “Try launching slicer using Slicer.exe --disable-settings (if it fixes the problem, delete Slicer.ini and Slicer-.ini files from your Slicer settings directory.”</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/get_help.html#slicer-application-does-not-start" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/get_help.html#slicer-application-does-not-start</a></p>

---

## Post #3 by @11122 (2021-08-26 02:50 UTC)

<p>[DEBUG][Qt] 26.08.2021 11:35:05 [] (unknown:0) - Session start time …: 2021-08-26 11:35:05<br>
[DEBUG][Qt] 26.08.2021 11:35:05 [] (unknown:0) - Slicer version …: 4.11.20210226 (revision 29738 / 7a593c8) win-amd64 - installed release<br>
[DEBUG][Qt] 26.08.2021 11:35:05 [] (unknown:0) - Operating system …: Windows /  Professional / (Build 19042, Code Page 65001) - 64-bit<br>
[DEBUG][Qt] 26.08.2021 11:35:05 [] (unknown:0) - Memory …: 8062 MB physical, 9342 MB virtual<br>
[DEBUG][Qt] 26.08.2021 11:35:05 [] (unknown:0) - CPU …: GenuineIntel , 8 cores, 8 logical processors<br>
[DEBUG][Qt] 26.08.2021 11:35:05 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 26.08.2021 11:35:05 [] (unknown:0) - Qt configuration …: version 5.15.1, with SSL, requested OpenGL 3.2 (compatibility profile)<br>
[DEBUG][Qt] 26.08.2021 11:35:05 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 26.08.2021 11:35:05 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 26.08.2021 11:35:05 [] (unknown:0) - Application path …: C:/Users/demo1/Desktop/Slicer 4.11.20210226/bin<br>
[DEBUG][Qt] 26.08.2021 11:35:05 [] (unknown:0) - Additional module paths …: (none)<br>
[DEBUG][Python] 26.08.2021 11:35:06 [Python] (C:\Users\demo1\Desktop\Slicer 4.11.20210226\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Qt] 26.08.2021 11:35:07 [] (unknown:0) - Switch to module:  “Welcome”<br>
[DEBUG][Qt] 26.08.2021 11:37:26 [] (unknown:0) - The module “DICOM” has not been registered.<br>
[DEBUG][Qt] 26.08.2021 11:37:26 [] (unknown:0) - The following modules have been registered: (“ACPCTransform”, “AddScalarVolumes”, “Annotations”, “BRAINSDWICleanup”, “BRAINSFit”, “BRAINSLabelStats”, “BRAINSROIAuto”, “BRAINSResample”, “BRAINSResize”, “BRAINSStripRotation”, “BRAINSTransformConvert”, “BordersOut”, “Cameras”, “CastScalarVolume”, “CheckerBoardFilter”, “Cleaner”, “Colors”, “Connectivity”, “CreateDICOMSeries”, “CropVolume”, “CurvatureAnisotropicDiffusion”, “DWIConvert”, “Data”, “DataStore”, “Decimation”, “DoubleArrays”, “DynamicModeler”, “EventBroker”, “ExecutionModelTour”, “ExpertAutomatedRegistration”, “ExtractSkeleton”, “FiducialRegistration”, “FillHoles”, “GaussianBlurImageFilter”, “GradientAnisotropicDiffusion”, “GrayscaleFillHoleImageFilter”, “GrayscaleGrindPeakImageFilter”, “GrayscaleModelMaker”, “HistogramMatching”, “ImageLabelCombine”, “LabelMapSmoothing”, “MC2Origin”, “Markups”, “MaskScalarVolume”, “MedianImageFilter”, “MergeModels”, “Mirror”, “ModelMaker”, “ModelToLabelMap”, “Models”, “MultiVolumeExplorer”, “MultiplyScalarVolumes”, “N4ITKBiasFieldCorrection”, “Normals”, “OrientScalarVolume”, “PETStandardUptakeValueComputation”, “PerformMetricTest”, “Plots”, “ProbeVolumeWithModel”, “Reformat”, “ResampleDTIVolume”, “ResampleScalarVectorDWIVolume”, “ResampleScalarVolume”, “RobustStatisticsSegmenter”, “SceneViews”, “Segmentations”, “Sequences”, “SimpleRegionGrowingSegmentation”, “Smoothing”, “SubjectHierarchy”, “SubtractScalarVolumes”, “Tables”, “Terminologies”, “Texts”, “ThresholdScalarVolume”, “Transforms”, “Units”, “ViewControllers”, “VolumeRendering”, “Volumes”, “VotingBinaryHoleFillingImageFilter”, “Welcome”, “relaxPolygons”, “scaleMesh”, “translateMesh”)</p>

---

## Post #5 by @11122 (2021-08-26 02:57 UTC)

<p>Mr.Pieper</p>
<p>Thank you for your reply.</p>

---

## Post #6 by @11122 (2021-08-26 04:26 UTC)

<p>[DEBUG][Qt] 26.08.2021 11:35:05 [] (unknown:0) - Session start time …: 2021-08-26 11:35:05<br>
[DEBUG][Qt] 26.08.2021 11:35:05 [] (unknown:0) - Slicer version …: 4.11.20210226 (revision 29738 / 7a593c8) win-amd64 - installed release<br>
[DEBUG][Qt] 26.08.2021 11:35:05 [] (unknown:0) - Operating system …: Windows /  Professional / (Build 19042, Code Page 65001) - 64-bit<br>
[DEBUG][Qt] 26.08.2021 11:35:05 [] (unknown:0) - Memory …: 8062 MB physical, 9342 MB virtual<br>
[DEBUG][Qt] 26.08.2021 11:35:05 [] (unknown:0) - CPU …: GenuineIntel , 8 cores, 8 logical processors<br>
[DEBUG][Qt] 26.08.2021 11:35:05 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 26.08.2021 11:35:05 [] (unknown:0) - Qt configuration …: version 5.15.1, with SSL, requested OpenGL 3.2 (compatibility profile)<br>
[DEBUG][Qt] 26.08.2021 11:35:05 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 26.08.2021 11:35:05 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 26.08.2021 11:35:05 [] (unknown:0) - Application path …: C:/Users/demo1/Desktop/Slicer 4.11.20210226/bin<br>
[DEBUG][Qt] 26.08.2021 11:35:05 [] (unknown:0) - Additional module paths …: (none)<br>
[DEBUG][Python] 26.08.2021 11:35:06 [Python] (C:\Users\demo1\Desktop\Slicer 4.11.20210226\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Qt] 26.08.2021 11:35:07 [] (unknown:0) - Switch to module:  “Welcome”<br>
[DEBUG][Qt] 26.08.2021 11:37:26 [] (unknown:0) - The module “DICOM” has not been registered.<br>
[DEBUG][Qt] 26.08.2021 11:37:26 [] (unknown:0) - The following modules have been registered: (“ACPCTransform”, “AddScalarVolumes”, “Annotations”, “BRAINSDWICleanup”, “BRAINSFit”, “BRAINSLabelStats”, “BRAINSROIAuto”, “BRAINSResample”, “BRAINSResize”, “BRAINSStripRotation”, “BRAINSTransformConvert”, “BordersOut”, “Cameras”, “CastScalarVolume”, “CheckerBoardFilter”, “Cleaner”, “Colors”, “Connectivity”, “CreateDICOMSeries”, “CropVolume”, “CurvatureAnisotropicDiffusion”, “DWIConvert”, “Data”, “DataStore”, “Decimation”, “DoubleArrays”, “DynamicModeler”, “EventBroker”, “ExecutionModelTour”, “ExpertAutomatedRegistration”, “ExtractSkeleton”, “FiducialRegistration”, “FillHoles”, “GaussianBlurImageFilter”, “GradientAnisotropicDiffusion”, “GrayscaleFillHoleImageFilter”, “GrayscaleGrindPeakImageFilter”, “GrayscaleModelMaker”, “HistogramMatching”, “ImageLabelCombine”, “LabelMapSmoothing”, “MC2Origin”, “Markups”, “MaskScalarVolume”, “MedianImageFilter”, “MergeModels”, “Mirror”, “ModelMaker”, “ModelToLabelMap”, “Models”, “MultiVolumeExplorer”, “MultiplyScalarVolumes”, “N4ITKBiasFieldCorrection”, “Normals”, “OrientScalarVolume”, “PETStandardUptakeValueComputation”, “PerformMetricTest”, “Plots”, “ProbeVolumeWithModel”, “Reformat”, “ResampleDTIVolume”, “ResampleScalarVectorDWIVolume”, “ResampleScalarVolume”, “RobustStatisticsSegmenter”, “SceneViews”, “Segmentations”, “Sequences”, “SimpleRegionGrowingSegmentation”, “Smoothing”, “SubjectHierarchy”, “SubtractScalarVolumes”, “Tables”, “Terminologies”, “Texts”, “ThresholdScalarVolume”, “Transforms”, “Units”, “ViewControllers”, “VolumeRendering”, “Volumes”, “VotingBinaryHoleFillingImageFilter”, “Welcome”, “relaxPolygons”, “scaleMesh”, “translateMesh”)<br>
[DEBUG][Qt] 26.08.2021 11:59:46 [] (unknown:0) - Switch to module:  “”</p>

---

## Post #7 by @lassoan (2021-08-26 05:10 UTC)

<p>It seems that all the Python scripted modules failed to load.</p>
<p>Have you ran Slicer on this same computer, installed in the same location before?</p>
<p>If yes, then most likely Slicer is broken due to installation of another application. Probably that other application incorrectly installs some shared libraries in system folders.</p>
<p>It may also be possible that some Python packages that an extension installed misbehaves. Install Slicer in a clean folder and see if it helps.</p>

---

## Post #9 by @11122 (2021-08-27 02:02 UTC)

<p>Thank you for your kind attention.</p>
<p>I’ve installed it on this computer before.<br>
It worked fine then, but once I uninstalled it, it didn’t work anymore.</p>
<p>I tried to install it in another folder, but it didn’t change.</p>
<p>Is there anything else I can do?</p>

---

## Post #10 by @lassoan (2021-08-27 02:06 UTC)

<aside class="quote no-group" data-username="11122" data-post="9" data-topic="19350">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/11122/48/12106_2.png" class="avatar"> 11122:</div>
<blockquote>
<p>Is there anything else I can do?</p>
</blockquote>
</aside>
<p>Yes, you need to go through all the steps described in the <a href="https://slicer.readthedocs.io/en/latest/user_guide/get_help.html#slicer-application-does-not-start">“Slicer application does not start” section</a> as <a class="mention" href="/u/pieper">@pieper</a> suggested above.</p>

---

## Post #11 by @11122 (2021-08-27 02:27 UTC)

<p>How do I use Slicer.exe --disable-settings?</p>
<p>Do I need to copy and paste it somewhere?</p>
<p>I don’t have much computer knowledge, so if possible, please tell me more.</p>
<p>Thank you very much for your time.</p>

---

## Post #12 by @slicer365 (2021-08-27 03:47 UTC)

<p>Reinstall Slicer after closing the antivirus software</p>

---

## Post #13 by @pieper (2021-08-27 12:49 UTC)

<aside class="quote no-group" data-username="11122" data-post="11" data-topic="19350">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/11122/48/12106_2.png" class="avatar"> 11122:</div>
<blockquote>
<p>How do I use Slicer.exe --disable-settings?</p>
<p>Do I need to copy and paste it somewhere?</p>
</blockquote>
</aside>
<p>Yes, it means open a command prompt, changing to the directory where Slicer is installed, and then running the <code>Slicer.exe --disable-settings</code> command.  You can find the install directory by getting the properties of the start menu icon (it will be something like <code>"C:\ProgramData\NA-MIC\Slicer 4.11.20210226\Slicer.exe"</code>)</p>
<p>If that works (Slicer starts with the Segment Editor) then somehow your settings got corrupted.  Use <code>Slicer.exe --settings-path | more</code> to find the path and delete the contents.</p>
<p>If you aren’t familiar with computers these may sound mysterious but maybe you can get a local expert to help you run them.</p>

---
