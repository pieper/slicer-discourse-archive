---
topic_id: 11969
title: "Slicerrt Error No Image Data In Input Volume 0"
date: 2020-06-09
url: https://discourse.slicer.org/t/11969
---

# SlicerRT ERROR No image data in input volume #0

**Topic ID**: 11969
**Date**: 2020-06-09
**URL**: https://discourse.slicer.org/t/slicerrt-error-no-image-data-in-input-volume-0/11969

---

## Post #1 by @annigilus (2020-06-09 20:08 UTC)

<p>Greetings everyone!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/16226e67928b6fb1c16d001149f9de8b037fce62.png" data-download-href="/uploads/short-url/39OgVpOdGj68OCTSbgekjCBNqhk.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/16226e67928b6fb1c16d001149f9de8b037fce62.png" alt="image" data-base62-sha1="39OgVpOdGj68OCTSbgekjCBNqhk" width="481" height="500" data-dominant-color="F4F4F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">536×557 15.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Trying to calculate dose, error appears.<br>
ERROR: No image data in nput volume <span class="hashtag-raw">#0</span><br>
What is volume <span class="hashtag-raw">#0</span>?<br>
Thank you!</p>

---

## Post #2 by @Sunderlandkyl (2020-06-09 20:26 UTC)

<p>The error message means that the dose volume for the beam was not calculated.</p>
<p>Probably this is because there was an error when running Dosxyznrc. Could you upload the <a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ErrorLog#To_capture_the_entire_error_log_for_a_report" rel="nofollow noopener">log file</a>? It should contain more info that describes the what went wrong.</p>

---

## Post #3 by @annigilus (2020-06-09 20:45 UTC)

<p>[DEBUG][Qt] 10.06.2020 03:43:05 [] (unknown:0) - Session start time …: 2020-06-10 03:43:05<br>
[DEBUG][Qt] 10.06.2020 03:43:05 [] (unknown:0) - Slicer version …: 4.11.0-2020-06-08 (revision 29117 / 6256f99) win-amd64 - installed release<br>
[DEBUG][Qt] 10.06.2020 03:43:05 [] (unknown:0) - Operating system …: Windows /  Professional / (Build 17763, Code Page 1251) - 64-bit<br>
[DEBUG][Qt] 10.06.2020 03:43:05 [] (unknown:0) - Memory …: 16316 MB physical, 28092 MB virtual<br>
[DEBUG][Qt] 10.06.2020 03:43:05 [] (unknown:0) - CPU …: AuthenticAMD AMD Ryzen 7 2700 Eight-Core Processor          , 16 cores, 16 logical processors<br>
[DEBUG][Qt] 10.06.2020 03:43:05 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 10.06.2020 03:43:05 [] (unknown:0) - Qt configuration …: version 5.15.0, with SSL, requested OpenGL 3.2 (compatibility profile)<br>
[DEBUG][Qt] 10.06.2020 03:43:05 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 10.06.2020 03:43:05 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 10.06.2020 03:43:05 [] (unknown:0) - Application path …: C:/ProgramData/NA-MIC/Slicer 4.11.0-2020-06-08/bin<br>
[DEBUG][Qt] 10.06.2020 03:43:05 [] (unknown:0) - Additional module paths …: C:/Users/svm18/AppData/Roaming/NA-MIC/Extensions-29117/MarkupsToModel/lib/Slicer-4.11/qt-loadable-modules, C:/Users/svm18/AppData/Roaming/NA-MIC/Extensions-29117/SegmentationWizard/lib/Slicer-4.11/qt-scripted-modules, C:/Users/svm18/AppData/Roaming/NA-MIC/Extensions-29117/SegmentEditorExtraEffects/lib/Slicer-4.11/qt-scripted-modules, C:/Users/svm18/AppData/Roaming/NA-MIC/Extensions-29117/SlicerRT/lib/Slicer-4.11/cli-modules, C:/Users/svm18/AppData/Roaming/NA-MIC/Extensions-29117/SlicerRT/lib/Slicer-4.11/qt-loadable-modules, C:/Users/svm18/AppData/Roaming/NA-MIC/Extensions-29117/SlicerRT/lib/Slicer-4.11/qt-scripted-modules<br>
[CRITICAL][Stream] 10.06.2020 03:43:07 [] (unknown:0) - Traceback (most recent call last):<br>
[CRITICAL][Stream] 10.06.2020 03:43:07 [] (unknown:0) -   File “”, line 1, in <br>
[CRITICAL][Stream] 10.06.2020 03:43:07 [] (unknown:0) -   File “C:\ProgramData\NA-MIC\Slicer 4.11.0-2020-06-08\lib\Python\Lib\imp.py”, line 170, in load_source<br>
[CRITICAL][Stream] 10.06.2020 03:43:07 [] (unknown:0) -     module = _exec(spec, sys.modules[name])<br>
[CRITICAL][Stream] 10.06.2020 03:43:07 [] (unknown:0) -   File “”, line 618, in _exec<br>
[CRITICAL][Stream] 10.06.2020 03:43:07 [] (unknown:0) -   File “”, line 674, in exec_module<br>
[CRITICAL][Stream] 10.06.2020 03:43:07 [] (unknown:0) -   File “”, line 781, in get_code<br>
[CRITICAL][Stream] 10.06.2020 03:43:07 [] (unknown:0) -   File “”, line 741, in source_to_code<br>
[CRITICAL][Stream] 10.06.2020 03:43:07 [] (unknown:0) -   File “”, line 219, in _call_with_frames_removed<br>
[CRITICAL][Stream] 10.06.2020 03:43:07 [] (unknown:0) -   File “C:/Users/svm18/AppData/Roaming/NA-MIC/Extensions-29117/SegmentationWizard/lib/Slicer-4.11/qt-scripted-modules/SegmentationWizard.py”, line 290<br>
[CRITICAL][Stream] 10.06.2020 03:43:07 [] (unknown:0) -     except Exception, e:<br>
[CRITICAL][Stream] 10.06.2020 03:43:07 [] (unknown:0) -                     ^<br>
[CRITICAL][Stream] 10.06.2020 03:43:07 [] (unknown:0) - SyntaxError: invalid syntax<br>
[CRITICAL][Qt] 10.06.2020 03:43:07 [] (unknown:0) - loadSourceAsModule - Failed to load file “C:/Users/svm18/AppData/Roaming/NA-MIC/Extensions-29117/SegmentationWizard/lib/Slicer-4.11/qt-scripted-modules/SegmentationWizard.py”  as module “SegmentationWizard” !<br>
[CRITICAL][Qt] 10.06.2020 03:43:07 [] (unknown:0) - Fail to instantiate module  “SegmentationWizard”<br>
[CRITICAL][Stream] 10.06.2020 03:43:07 [] (unknown:0) - Traceback (most recent call last):<br>
[CRITICAL][Stream] 10.06.2020 03:43:07 [] (unknown:0) -   File “”, line 1, in <br>
[CRITICAL][Stream] 10.06.2020 03:43:07 [] (unknown:0) -   File “C:\ProgramData\NA-MIC\Slicer 4.11.0-2020-06-08\lib\Python\Lib\imp.py”, line 170, in load_source<br>
[CRITICAL][Stream] 10.06.2020 03:43:07 [] (unknown:0) -     module = _exec(spec, sys.modules[name])<br>
[CRITICAL][Stream] 10.06.2020 03:43:07 [] (unknown:0) -   File “”, line 618, in _exec<br>
[CRITICAL][Stream] 10.06.2020 03:43:07 [] (unknown:0) -   File “”, line 674, in exec_module<br>
[CRITICAL][Stream] 10.06.2020 03:43:07 [] (unknown:0) -   File “”, line 781, in get_code<br>
[CRITICAL][Stream] 10.06.2020 03:43:07 [] (unknown:0) -   File “”, line 741, in source_to_code<br>
[CRITICAL][Stream] 10.06.2020 03:43:07 [] (unknown:0) -   File “”, line 219, in _call_with_frames_removed<br>
[CRITICAL][Stream] 10.06.2020 03:43:07 [] (unknown:0) -   File “C:/Users/svm18/AppData/Roaming/NA-MIC/Extensions-29117/SegmentationWizard/lib/Slicer-4.11/qt-scripted-modules/SegmentationWizardSelfTest.py”, line 227<br>
[CRITICAL][Stream] 10.06.2020 03:43:07 [] (unknown:0) -     except Exception, e:<br>
[CRITICAL][Stream] 10.06.2020 03:43:07 [] (unknown:0) -                     ^<br>
[CRITICAL][Stream] 10.06.2020 03:43:07 [] (unknown:0) - SyntaxError: invalid syntax<br>
[CRITICAL][Qt] 10.06.2020 03:43:07 [] (unknown:0) - loadSourceAsModule - Failed to load file “C:/Users/svm18/AppData/Roaming/NA-MIC/Extensions-29117/SegmentationWizard/lib/Slicer-4.11/qt-scripted-modules/SegmentationWizardSelfTest.py”  as module “SegmentationWizardSelfTest” !<br>
[CRITICAL][Qt] 10.06.2020 03:43:07 [] (unknown:0) - Fail to instantiate module  “SegmentationWizardSelfTest”<br>
[CRITICAL][Qt] 10.06.2020 03:43:07 [] (unknown:0) - The following modules failed to be instantiated:<br>
[CRITICAL][Qt] 10.06.2020 03:43:07 [] (unknown:0) -    SegmentationWizardSelfTest<br>
[CRITICAL][Qt] 10.06.2020 03:43:07 [] (unknown:0) -    SegmentationWizard<br>
[DEBUG][Python] 10.06.2020 03:43:08 [Python] (C:\ProgramData\NA-MIC\Slicer 4.11.0-2020-06-08\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 10.06.2020 03:43:09 [Python] (C:\ProgramData\NA-MIC\Slicer 4.11.0-2020-06-08\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 10.06.2020 03:43:09 [Python] (C:\ProgramData\NA-MIC\Slicer 4.11.0-2020-06-08\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 10.06.2020 03:43:09 [] (unknown:0) - Switch to module:  “Welcome”<br>
[INFO][VTK] 10.06.2020 03:43:27 [vtkMRMLVolumeArchetypeStorageNode (0000014296378820)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:470) - Loaded volume from file: D:/Stepan/PhantomHollowNRRDFull/3 Head 1.0.nrrd. Dimensions: 512x512x616. Number of components: 1. Pixel type: short.<br>
[DEBUG][Qt] 10.06.2020 03:43:27 [] (unknown:0) - “Volume” Reader has successfully read the file “D:/Stepan/PhantomHollowNRRDFull/3 Head 1.0.nrrd” “[1.35s]”<br>
[INFO][VTK] 10.06.2020 03:43:28 [vtkMRMLVolumeArchetypeStorageNode (0000014296379990)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:470) - Loaded volume from file: D:/Stepan/PhantomHollowNRRDFull/3 Head 1.0.nrrd. Dimensions: 512x512x616. Number of components: 1. Pixel type: short.<br>
[DEBUG][Qt] 10.06.2020 03:43:28 [] (unknown:0) - “MRML Scene” Reader has successfully read the file “D:/Stepan/PhantomHollowNRRDFull/2020-06-10-Scene.mrml” “[1.89s]”<br>
[DEBUG][Qt] 10.06.2020 03:43:29 [] (unknown:0) - “Segmentation” Reader has successfully read the file “D:/Stepan/PhantomHollowNRRDFull/Segmentation.seg.nrrd” “[0.55s]”<br>
[DEBUG][Qt] 10.06.2020 03:43:31 [] (unknown:0) - Switch to module:  “Data”<br>
[DEBUG][Qt] 10.06.2020 03:43:48 [] (unknown:0) - Switch to module:  “ExternalBeamPlanning”<br>
[DEBUG][Qt] 10.06.2020 03:43:50 [] (unknown:0) - class QColor __cdecl qSlicerSubjectHierarchyMarkupsPlugin::getDisplayColor(__int64,class QMap&lt;int,class QVariant&gt; &amp;) const : No display node<br>
[DEBUG][Qt] 10.06.2020 03:43:50 [] (unknown:0) - Dose engine selection changed to  “Mock random”<br>
[DEBUG][Qt] 10.06.2020 03:44:25 [] (unknown:0) - Dose engine selection changed to  “Orthovoltage”<br>
[DEBUG][Qt] 10.06.2020 03:44:29 [] (unknown:0) - Switch to module:  “Beams”<br>
[DEBUG][Qt] 10.06.2020 03:45:02 [] (unknown:0) - Switch to module:  “ExternalBeamPlanning”<br>
[INFO][Python] 10.06.2020 03:45:22 [Python] (C:/Users/svm18/AppData/Roaming/NA-MIC/Extensions-29117/SlicerRT/lib/Slicer-4.11/qt-scripted-modules/DoseEngines/OrthovoltageDoseEngine.py:203) - Isocenter (cm): [0.29, -0.533, -103.719]<br>
[ERROR][Python] 10.06.2020 03:45:22 [Python] (C:/Users/svm18/AppData/Roaming/NA-MIC/Extensions-29117/SlicerRT/lib/Slicer-4.11/qt-scripted-modules/DoseEngines/OrthovoltageDoseEngine.py:222) - Unable to get ROI by name R<br>
[INFO][Python] 10.06.2020 03:45:22 [Python] (C:\Users\svm18\AppData\Roaming\NA-MIC\Extensions-29117\SlicerRT\lib\Slicer-4.11\qt-scripted-modules\DoseEngines\EGSnrcUtil.py:50) - Run ctcreate: D:\Research\VoxelBased_radiotherapy\EGSnrc\HEN_HOUSE\bin\win3264\ctcreate.exe D:\Stepan\OrthoOutput\Beam1_HollowPhantom\ctcreate.inp<br>
[DEBUG][Python] 10.06.2020 03:45:22 [Python] (C:\Users\svm18\AppData\Roaming\NA-MIC\Extensions-29117\SlicerRT\lib\Slicer-4.11\qt-scripted-modules\DoseEngines\EGSnrcUtil.py:57) - -----------------------------<br>
[DEBUG][Python] 10.06.2020 03:45:22 [Python] (C:\Users\svm18\AppData\Roaming\NA-MIC\Extensions-29117\SlicerRT\lib\Slicer-4.11\qt-scripted-modules\DoseEngines\EGSnrcUtil.py:58) - ctcreate output:<br>
b’’<br>
[INFO][Python] 10.06.2020 03:45:22 [Python] (C:\Users\svm18\AppData\Roaming\NA-MIC\Extensions-29117\SlicerRT\lib\Slicer-4.11\qt-scripted-modules\DoseEngines\EGSnrcUtil.py:62) - ctcreate output (last paragraph):<br>
’<br>
[DEBUG][Python] 10.06.2020 03:45:22 [Python] (C:/Users/svm18/AppData/Roaming/NA-MIC/Extensions-29117/SlicerRT/lib/Slicer-4.11/qt-scripted-modules/DoseEngines/OrthovoltageDoseEngine.py:375) - -----------------------------<br>
[DEBUG][Python] 10.06.2020 03:45:22 [Python] (C:/Users/svm18/AppData/Roaming/NA-MIC/Extensions-29117/SlicerRT/lib/Slicer-4.11/qt-scripted-modules/DoseEngines/OrthovoltageDoseEngine.py:376) - DOSXYZ output:<br>
b’’<br>
[INFO][Python] 10.06.2020 03:45:22 [Python] (C:/Users/svm18/AppData/Roaming/NA-MIC/Extensions-29117/SlicerRT/lib/Slicer-4.11/qt-scripted-modules/DoseEngines/OrthovoltageDoseEngine.py:380) - DOSXYZ output (last paragraph):<br>
’<br>
[INFO][Stream] 10.06.2020 03:45:22 [] (unknown:0) - Isocenter (cm): [0.29, -0.533, -103.719]<br>
[CRITICAL][Qt] 10.06.2020 03:45:22 [] (unknown:0) - class QString __cdecl qSlicerAbstractDoseEngine::parameter(class vtkMRMLRTBeamNode *,class QString) : Parameter named  “VolumeName”  cannot be found for beam  NewBeam_1<br>
[CRITICAL][Stream] 10.06.2020 03:45:22 [] (unknown:0) - Unable to get ROI by name R<br>
[INFO][Stream] 10.06.2020 03:45:22 [] (unknown:0) - Run ctcreate: D:\Research\VoxelBased_radiotherapy\EGSnrc\HEN_HOUSE\bin\win3264\ctcreate.exe D:\Stepan\OrthoOutput\Beam1_HollowPhantom\ctcreate.inp<br>
[INFO][Stream] 10.06.2020 03:45:22 [] (unknown:0) - ctcreate output (last paragraph):<br>
[INFO][Stream] 10.06.2020 03:45:22 [] (unknown:0) - ’<br>
[INFO][Stream] 10.06.2020 03:45:22 [] (unknown:0) - DOSXYZ output (last paragraph):<br>
[INFO][Stream] 10.06.2020 03:45:22 [] (unknown:0) - ’<br>
[CRITICAL][Stream] 10.06.2020 03:45:22 [] (unknown:0) - Traceback (most recent call last):<br>
[CRITICAL][Stream] 10.06.2020 03:45:22 [] (unknown:0) -   File “C:/Users/svm18/AppData/Roaming/NA-MIC/Extensions-29117/SlicerRT/lib/Slicer-4.11/qt-scripted-modules/DoseEngines/OrthovoltageDoseEngine.py”, line 388, in calculateDoseUsingEngine<br>
[CRITICAL][Stream] 10.06.2020 03:45:22 [] (unknown:0) -     loadedVolumeNode = slicer.util.loadNodeFromFile(dosXyznrcOutputFilePath, ‘DosxyzNrc3dDoseFile’, {})<br>
[CRITICAL][Stream] 10.06.2020 03:45:22 [] (unknown:0) -   File “C:\ProgramData\NA-MIC\Slicer 4.11.0-2020-06-08\bin\Python\slicer\util.py”, line 472, in loadNodeFromFile<br>
[CRITICAL][Stream] 10.06.2020 03:45:22 [] (unknown:0) -     raise RuntimeError(errorMessage)<br>
[CRITICAL][Stream] 10.06.2020 03:45:22 [] (unknown:0) - RuntimeError: Failed to load node from file: D:\Research\VoxelBased_radiotherapy\EGSnrc\EGS_HOME\dosxyznrc\20200610_034522_dosxyznrc.3ddose<br>
[CRITICAL][Qt] 10.06.2020 03:45:22 [] (unknown:0) - “C:/Users/svm18/AppData/Roaming/NA-MIC/Extensions-29117/SlicerRT/lib/Slicer-4.11/qt-scripted-modules/DoseEngines/OrthovoltageDoseEngine.py” : clone: Failed to call mandatory calculateDoseUsingEngine method! If it is implemented, please see python output for errors.<br>
[WARNING][Qt] 10.06.2020 03:45:22 [] (unknown:0) - void __cdecl qSlicerAbstractDoseEngine::addResultDose(class vtkMRMLScalarVolumeNode *,class vtkMRMLRTBeamNode *,bool) : Unable to find study item that contains the plan! Creating a study item and adding the reference dose and the plan under it is necessary in order for dose evaluation steps to work properly<br>
[ERROR][VTK] 10.06.2020 03:45:22 [vtkSlicerDoseAccumulationModuleLogic (0000014298A38D90)] (D:\D\P\S-0-E-b\SlicerRT\DoseAccumulation\Logic\vtkSlicerDoseAccumulationModuleLogic.cxx:218) - AccumulateDoseVolumes: No image data in input volume <span class="hashtag">#0</span><br>
[CRITICAL][Qt] 10.06.2020 03:45:22 [] (unknown:0) - class QString __cdecl qSlicerDoseEngineLogic::calculateDose(class vtkMRMLRTPlanNode *) :  “No image data in input volume <span class="hashtag">#0</span>”<br>
[CRITICAL][Qt] 10.06.2020 03:45:22 [] (unknown:0) - void __cdecl qSlicerExternalBeamPlanningModuleWidget::calculateDoseClicked(void) :  “ERROR: No image data in input volume <span class="hashtag">#0</span>”</p>

---

## Post #4 by @cpinter (2020-06-10 09:05 UTC)

<p>I have seen the same error recently, when the lab where it was originally developed picked up the project again, and the person who started working on it asked me. I developed the Slicer part of this dose engine, but unfortunately I don’t have the capacity to work on it anymore. I will tell the medical physics student about this forum topic, maybe you could team up.</p>

---

## Post #5 by @Sunderlandkyl (2020-06-10 13:33 UTC)

<p>The Dosxyznrc output doesn’t seem to be complete in the log.<br>
If the executable was found, the log should contain something like this:</p>
<pre><code class="lang-auto">b"================================================================================
EGSnrc version 4 for win3264                           Tue Jun  2 15:17:15 2020
================================================================================
</code></pre>
<p>I helped the student that <a class="mention" href="/u/cpinter">@cpinter</a> mentioned fix their issue, so maybe the same problem is happening here.<br>
The Orthovoltage dose engine is harded-coded to use AIR512ICRU and WATER512ICRU mediums. If you are using the 521icru.pegs4dat or 700icru.pegs4dat that comes with EGSnrc, then the dose calculation will fail. You could test this by changing/adding the air and water values in the pegs4dat file to AIR512ICRU and WATER512ICRU, or by using a pegs4dat file that has them already defined.</p>

---

## Post #6 by @annigilus (2020-06-10 14:54 UTC)

<p>Thank you a lot! But how can I fix these pegs4dat icru files or find correct icru file?</p>

---

## Post #7 by @Sunderlandkyl (2020-06-10 15:48 UTC)

<p>This is not a permanent solution, just trying to determine if this is what’s causing the problem.</p>
<p>If you open the pegs4dat file that you specified in the orthovoltage config, look for the AIR medium (search for  MEDIUM=AIR), and replace both MEDIUM and STERNCID values with AIR512ICRU.</p>

---

## Post #8 by @TomNB (2020-06-11 16:45 UTC)

<p>As Kyle said, EGSnrc comes with pegs data that use high energy cut offs (ECUT and PCUT) that do not work for lower energies such as that of orthovoltage. So you need to create your pegs based on the materials of your simulation and photon energies. Refer to egs manual pirs 701 on how to create pegs.</p>

---

## Post #9 by @Space (2020-11-15 03:47 UTC)

<p>Hi, I have this problem too, I just can’t seem to get the Orthovoltage system working. Here is my first error in log<br>
“ctcreate output (last paragraph):<br>
Input the x,y,z dimensions (cm) of the dosxyznrc voxelson one line<br>
(min=      0.42969 x     0.42969 x     0.26953 cm)<br>
:     0.10742     0.10742     0.25000<br>
Dimensions in at least one direction &lt; min allowed. Either increase<br>
dimension(s) or go into dosxyznrc_user_macros.mortran and increase IMAX,<br>
JMAX and/or KMAX”</p>
<p>I have changed these numbers as suggested by little endian but it never seems to register the change. Do I have to recompile the ctcreate data files?I tried that and was given an error, 1d etc etc… <img src="https://emoji.discourse-cdn.com/twitter/exploding_head.png?v=9" title=":exploding_head:" class="emoji" alt=":exploding_head:"></p>
<p>haha, if anyone can offer suggestions that be be fantastic.</p>

---
