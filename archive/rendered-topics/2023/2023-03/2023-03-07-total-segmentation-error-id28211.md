---
topic_id: 28211
title: "Total Segmentation Error"
date: 2023-03-07
url: https://discourse.slicer.org/t/28211
---

# Total Segmentation error

**Topic ID**: 28211
**Date**: 2023-03-07
**URL**: https://discourse.slicer.org/t/total-segmentation-error/28211

---

## Post #1 by @Ackta (2023-03-07 10:50 UTC)

<p>Hi , i`ve update slicer to 5.2.2, and i receive this error from total segmentation.<br>
“Traceback (most recent call last):<br>
File “C:\Users\Administrator\AppData\Local\NA-MIC\Slicer 5.2.2\bin\Python\slicer\util.py”, line 2967, in tryWithErrorDisplay<br>
yield<br>
File “C:/Users/Administrator/AppData/Local/NA-MIC/Slicer 5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 264, in onApplyButton<br>
self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),<br>
File “C:/Users/Administrator/AppData/Local/NA-MIC/Slicer 5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 749, in process<br>
self.logProcessOutput(proc)<br>
File “C:/Users/Administrator/AppData/Local/NA-MIC/Slicer 5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 656, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[‘C:/Users/Administrator/AppData/Local/NA-MIC/Slicer 5.2.2/bin/…/bin\PythonSlicer.EXE’, ‘C:\Users\Administrator\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Scripts\TotalSegmentator’, ‘-i’, ‘F:/3dSlicer TMP/__SlicerTemp__2023-03-07_11+42+36.788/total-segmentator-input.nii’, ‘-o’, ‘F:/3dSlicer TMP/__SlicerTemp__2023-03-07_11+42+36.788/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–fast’]’ returned non-zero exit status 1.”<br>
Thanks</p>

---

## Post #2 by @rbumm (2023-03-07 14:48 UTC)

<p>Have you installed PyTorch first with the SlicerPyTorch extension? Restarted?<br>
And have you selected an input volume?</p>

---

## Post #3 by @lassoan (2023-03-08 03:47 UTC)

<p>Let us know what additional details you see in the application log (menu: Help / Report a bug).</p>

---

## Post #4 by @Ackta (2023-03-08 09:27 UTC)

<p>[DEBUG][Qt] 06.03.2023 17:17:28 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Session start time …: 2023-03-06 17:17:28<br>
[DEBUG][Qt] 06.03.2023 17:17:28 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Slicer version …: 5.2.2 (revision 31382 / fb46bd1) win-amd64 - installed release<br>
[DEBUG][Qt] 06.03.2023 17:17:28 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Operating system …: Windows /  Professional / (Build 19044, Code Page 65001) - 64-bit<br>
[DEBUG][Qt] 06.03.2023 17:17:28 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Memory …: 65203 MB physical, 130739 MB virtual<br>
[DEBUG][Qt] 06.03.2023 17:17:28 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - CPU …: GenuineIntel , 24 cores, 24 logical processors<br>
[DEBUG][Qt] 06.03.2023 17:17:28 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 06.03.2023 17:17:28 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Qt configuration …: version 5.15.2, with SSL, requested OpenGL 3.2 (compatibility profile)<br>
[DEBUG][Qt] 06.03.2023 17:17:28 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Internationalization …: disabled, language=<br>
[DEBUG][Qt] 06.03.2023 17:17:28 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Developer mode …: enabled<br>
[DEBUG][Qt] 06.03.2023 17:17:28 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Application path …: C:/Users/Administrator/AppData/Local/NA-MIC/Slicer 5.2.2/bin<br>
[DEBUG][Qt] 06.03.2023 17:17:28 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Additional module paths …: C:/Users/Administrator/AppData/Roaming/Blender Foundation/Blender/3.3/scripts/addons/linkSlicerBlender-socket/slicer_module, NA-MIC/Extensions-31382/AnglePlanesExtension/lib/Slicer-5.2/qt-scripted-modules, NA-MIC/Extensions-31382/BoneTextureExtension/lib/Slicer-5.2/cli-modules, NA-MIC/Extensions-31382/BoneTextureExtension/lib/Slicer-5.2/qt-scripted-modules, NA-MIC/Extensions-31382/DatabaseInteractor/lib/Slicer-5.2/qt-scripted-modules, NA-MIC/Extensions-31382/CMFreg/lib/Slicer-5.2/cli-modules, NA-MIC/Extensions-31382/CMFreg/lib/Slicer-5.2/qt-scripted-modules, NA-MIC/Extensions-31382/EasyClip/lib/Slicer-5.2/qt-scripted-modules, NA-MIC/Extensions-31382/MeshStatisticsExtension/lib/Slicer-5.2/qt-scripted-modules, NA-MIC/Extensions-31382/MeshToLabelMap/lib/Slicer-5.2/cli-modules, NA-MIC/Extensions-31382/MeshToLabelMap/lib/Slicer-5.2/qt-scripted-modules, NA-MIC/Extensions-31382/ModelToModelDistance/lib/Slicer-5.2/cli-modules, NA-MIC/Extensions-31382/Q3DC/lib/Slicer-5.2/qt-scripted-modules, NA-MIC/Extensions-31382/SPHARM-PDM/lib/Slicer-5.2/cli-modules, NA-MIC/Extensions-31382/SPHARM-PDM/lib/Slicer-5.2/qt-scripted-modules, NA-MIC/Extensions-31382/ShapePopulationViewer/lib/Slicer-5.2/qt-loadable-modules, NA-MIC/Extensions-31382/SlicerCMF/lib/Slicer-5.2/qt-scripted-modules, NA-MIC/Extensions-31382/SlicerMarkupConstraints/lib/Slicer-5.2/qt-scripted-modules, NA-MIC/Extensions-31382/ShapeVariationAnalyzer/lib/Slicer-5.2/cli-modules, NA-MIC/Extensions-31382/ShapeVariationAnalyzer/lib/Slicer-5.2/qt-scripted-modules, NA-MIC/Extensions-31382/CurveMaker/lib/Slicer-5.2/qt-scripted-modules, NA-MIC/Extensions-31382/SegmentEditorExtraEffects/lib/Slicer-5.2/qt-loadable-modules, NA-MIC/Extensions-31382/SegmentEditorExtraEffects/lib/Slicer-5.2/qt-scripted-modules, NA-MIC/Extensions-31382/MarkupsToModel/lib/Slicer-5.2/qt-loadable-modules, NA-MIC/Extensions-31382/PickAndPaintExtension/lib/Slicer-5.2/qt-scripted-modules, NA-MIC/Extensions-31382/SlicerAutomatedDentalTools/lib/Slicer-5.2/cli-modules, NA-MIC/Extensions-31382/SlicerAutomatedDentalTools/lib/Slicer-5.2/qt-scripted-modules, NA-MIC/Extensions-31382/SlicerDentalModelSeg/lib/Slicer-5.2/cli-modules, NA-MIC/Extensions-31382/SlicerDentalModelSeg/lib/Slicer-5.2/qt-scripted-modules, NA-MIC/Extensions-31382/Sandbox/lib/Slicer-5.2/qt-loadable-modules, NA-MIC/Extensions-31382/Sandbox/lib/Slicer-5.2/qt-scripted-modules, NA-MIC/Extensions-31382/NvidiaAIAssistedAnnotation/lib/Slicer-5.2/qt-scripted-modules, NA-MIC/Extensions-31382/ModelCropper/lib/Slicer-5.2/qt-scripted-modules, NA-MIC/Extensions-31382/OrthodonticAnalysis/lib/Slicer-5.2/qt-scripted-modules, NA-MIC/Extensions-31382/SurfaceWrapSolidify/lib/Slicer-5.2/qt-scripted-modules, NA-MIC/Extensions-31382/BoneReconstructionPlanner/lib/Slicer-5.2/qt-scripted-modules, NA-MIC/Extensions-31382/SlicerRT/lib/Slicer-5.2/cli-modules, NA-MIC/Extensions-31382/SlicerRT/lib/Slicer-5.2/qt-loadable-modules, NA-MIC/Extensions-31382/SlicerRT/lib/Slicer-5.2/qt-scripted-modules, NA-MIC/Extensions-31382/MONAILabel/lib/Slicer-5.2/qt-scripted-modules, NA-MIC/Extensions-31382/IntensitySegmenter/lib/Slicer-5.2/cli-modules, NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules, NA-MIC/Extensions-31382/PyTorch/lib/Slicer-5.2/qt-scripted-modules<br>
[CRITICAL][Stream] 06.03.2023 17:17:32 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - C:\Users\Administrator\AppData\Local\NA-MIC\Slicer 5.2.2\NA-MIC\Extensions-31382\ShapeVariationAnalyzer\lib\Slicer-5.2\qt-scripted-modules\cpns\cpns.py:57: SyntaxWarning: “is” with a literal. Did you mean “==”?<br>
[CRITICAL][Stream] 06.03.2023 17:17:32 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   if len(self.fileList) is 0:<br>
[WARNING][Qt] 06.03.2023 17:17:33 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - libpng warning: iCCP: known incorrect sRGB profile<br>
[DEBUG][Python] 06.03.2023 17:17:33 [Python] (C:\Users\Administrator\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Slicer-5.2\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 06.03.2023 17:17:35 [Python] (C:\Users\Administrator\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Slicer-5.2\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 06.03.2023 17:17:35 [Python] (C:\Users\Administrator\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Slicer-5.2\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 06.03.2023 17:17:35 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “Welcome”<br>
[INFO][Python] 06.03.2023 17:17:35 [Python] (C:/Users/Administrator/AppData/Local/NA-MIC/Slicer 5.2.2/NA-MIC/Extensions-31382/NvidiaAIAssistedAnnotation/lib/Slicer-5.2/qt-scripted-modules/SegmentEditorNvidiaAIAA.py:32) - This plugin dir: C:/Users/Administrator/AppData/Local/NA-MIC/Slicer 5.2.2/NA-MIC/Extensions-31382/NvidiaAIAssistedAnnotation/lib/Slicer-5.2/qt-scripted-modules<br>
[DEBUG][Qt] 06.03.2023 17:17:49 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “DICOM”<br>
[INFO][Python] 06.03.2023 17:18:06 [Python] (C:/Users/Administrator/AppData/Local/NA-MIC/Slicer 5.2.2/bin/…/lib/Slicer-5.2/qt-scripted-modules/DICOMScalarVolumePlugin.py:393) - Loading with imageIOName: GDCM<br>
[INFO][Python] 06.03.2023 17:18:12 [Python] (C:/Users/Administrator/AppData/Local/NA-MIC/Slicer 5.2.2/bin/…/lib/Slicer-5.2/qt-scripted-modules/DICOMScalarVolumePlugin.py:472) - Window/level found in DICOM tags (center=1048.0, width=4096.0) has been applied to volume 11: Assiale<br>
[DEBUG][Qt] 06.03.2023 17:18:31 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “SegmentEditor”<br>
[WARNING][Qt] 06.03.2023 17:18:31 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - QLayout::addChildLayout: layout “” already has a parent<br>
[WARNING][Qt] 06.03.2023 17:18:31 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - ctkSliderWidget::setSingleStep()  0 is out of bounds. 0 100 1<br>
[DEBUG][Qt] 06.03.2023 18:31:35 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “”</p>

---
