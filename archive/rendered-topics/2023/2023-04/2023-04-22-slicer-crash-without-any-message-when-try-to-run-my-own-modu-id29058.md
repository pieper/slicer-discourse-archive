# Slicer crash without any message when try to run my own module

**Topic ID**: 29058
**Date**: 2023-04-22
**URL**: https://discourse.slicer.org/t/slicer-crash-without-any-message-when-try-to-run-my-own-module/29058

---

## Post #1 by @Lorenzo_Lasagni (2023-04-22 13:41 UTC)

<p>Problem report for Slicer 4.11.20210226 win-amd64: [please describe expected and actual behavior]</p>
<p>Me and a colleague of mine have write a new module for slicer, but since he sent me last version it crash when i press the first bottom to make it start.</p>
<p>I leave as attach the log file:</p>
<p>Thansk in advance,<br>
Lorenzo</p>
<p>[DEBUG][Qt] 22.04.2023 15:36:49 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Session start time …: 2023-04-22 15:36:49<br>
[DEBUG][Qt] 22.04.2023 15:36:49 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Slicer version …: 4.11.20210226 (revision 29738 / 7a593c8) win-amd64 - installed release<br>
[DEBUG][Qt] 22.04.2023 15:36:50 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Operating system …: Windows /  Personal / (Build 22621, Code Page 65001) - 64-bit<br>
[DEBUG][Qt] 22.04.2023 15:36:50 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Memory …: 16086 MB physical, 18518 MB virtual<br>
[DEBUG][Qt] 22.04.2023 15:36:50 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - CPU …: GenuineIntel , 8 cores, 8 logical processors<br>
[DEBUG][Qt] 22.04.2023 15:36:50 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 22.04.2023 15:36:50 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Qt configuration …: version 5.15.1, with SSL, requested OpenGL 3.2 (compatibility profile)<br>
[DEBUG][Qt] 22.04.2023 15:36:50 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Developer mode enabled …: yes<br>
[DEBUG][Qt] 22.04.2023 15:36:50 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 22.04.2023 15:36:50 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Application path …: C:/ProgramData/NA-MIC/Slicer 4.11.20210226/bin<br>
[DEBUG][Qt] 22.04.2023 15:36:50 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Additional module paths …: NA-MIC/Extensions-29738/SlicerRadiomics/lib/Slicer-4.11/cli-modules, NA-MIC/Extensions-29738/SlicerRadiomics/lib/Slicer-4.11/qt-scripted-modules, NA-MIC/Extensions-29738/MarkupsToModel/lib/Slicer-4.11/qt-loadable-modules, NA-MIC/Extensions-29738/SegmentEditorExtraEffects/lib/Slicer-4.11/qt-scripted-modules, C:/Users/lasa_/Documents/Firenze/Universita/Covid/slicer_guglielmo/Estensioni\Features_seg\Features_seg, NA-MIC/Extensions-29738/SlicerVMTK/lib/Slicer-4.11/qt-loadable-modules, NA-MIC/Extensions-29738/SlicerVMTK/lib/Slicer-4.11/qt-scripted-modules, NA-MIC/Extensions-29738/SlicerRT/lib/Slicer-4.11/cli-modules, NA-MIC/Extensions-29738/SlicerRT/lib/Slicer-4.11/qt-loadable-modules, NA-MIC/Extensions-29738/SlicerRT/lib/Slicer-4.11/qt-scripted-modules, NA-MIC/Extensions-29738/QuantitativeReporting/lib/Slicer-4.11/qt-scripted-modules, NA-MIC/Extensions-29738/PETDICOMExtension/lib/Slicer-4.11/cli-modules, NA-MIC/Extensions-29738/PETDICOMExtension/lib/Slicer-4.11/qt-scripted-modules, NA-MIC/Extensions-29738/SlicerDevelopmentToolbox/lib/Slicer-4.11/qt-scripted-modules, NA-MIC/Extensions-29738/DCMQI/lib/Slicer-4.11/cli-modules, C:/Users/lasa_/Documents/Firenze/Universita/Covid/slicer_guglielmo/Estensioni/Diap_SX\Diap_SX, NA-MIC/Extensions-29738/SlicerJupyter/lib/Slicer-4.11/qt-loadable-modules, NA-MIC/Extensions-29738/SlicerJupyter/lib/Slicer-4.11/qt-scripted-modules, C:/Users/lasa_/Documents/Firenze/Universita/Covid/slicer_guglielmo/Estensioni/Diap_DX\Diap_DX, NA-MIC/Extensions-29738/SlicerProstate/lib/Slicer-4.11/cli-modules, NA-MIC/Extensions-29738/SlicerProstate/lib/Slicer-4.11/qt-scripted-modules, C:/Users/lasa_/Documents/Firenze/Universita/Covid/slicer_guglielmo/Estensioni/Covid19LungLesion4\Covid19LungLesion4<br>
[DEBUG][Python] 22.04.2023 15:36:51 [Python] (C:\ProgramData\NA-MIC\Slicer 4.11.20210226\lib\Python\Lib\site-packages\pydicom\datadict.py:432) - Reversing DICOM dictionary so can look up tag from a keyword…<br>
[CRITICAL][Stream] 22.04.2023 15:36:51 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - RuntimeError: qSlicerScriptedLoadableModule::setPythonSource - Failed to load scripted loadable module: class Diap_DX was not found in file C:/Users/lasa_/Documents/Firenze/Universita/Covid/slicer_guglielmo/Estensioni/Diap_DX/Diap_DX/Diap_DX.py<br>
[CRITICAL][Qt] 22.04.2023 15:36:51 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Fail to instantiate module  “Diap_DX”<br>
[CRITICAL][Stream] 22.04.2023 15:36:52 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - RuntimeError: qSlicerScriptedLoadableModule::setPythonSource - Failed to load scripted loadable module: class VesselsRemovalimport was not found in file C:/Users/lasa_/Documents/Firenze/Universita/Covid/slicer_guglielmo/Estensioni/Covid19LungLesion4/Covid19LungLesion4/VesselsRemovalimport.py<br>
[CRITICAL][Qt] 22.04.2023 15:36:52 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Fail to instantiate module  “VesselsRemovalimport”<br>
[CRITICAL][Qt] 22.04.2023 15:36:52 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Error(s):<br>
CLI executable: C:/Users/lasa_/Documents/Firenze/Universita/Covid/slicer_guglielmo/Estensioni/Covid19LungLesion4/Covid19LungLesion4/myfunctions.py<br>
The process failed to start. Either the invoked program is missing, or you may have insufficient permissions to invoke the program.<br>
[CRITICAL][Qt] 22.04.2023 15:36:52 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Fail to instantiate module  “myfunctions”<br>
[CRITICAL][Qt] 22.04.2023 15:36:52 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Error(s):<br>
CLI executable: C:/ProgramData/NA-MIC/Slicer 4.11.20210226/NA-MIC/Extensions-29738/SlicerVMTK/lib/Slicer-4.11/qt-loadable-modules/vtkvmtk.py<br>
The process failed to start. Either the invoked program is missing, or you may have insufficient permissions to invoke the program.<br>
[CRITICAL][Qt] 22.04.2023 15:36:52 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Fail to instantiate module  “vtkvmtk”<br>
[CRITICAL][Qt] 22.04.2023 15:36:52 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - The following modules failed to be instantiated:<br>
[CRITICAL][Qt] 22.04.2023 15:36:52 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -    VesselsRemovalimport<br>
[CRITICAL][Qt] 22.04.2023 15:36:52 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -    Diap_DX<br>
[CRITICAL][Qt] 22.04.2023 15:36:52 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -    myfunctions<br>
[CRITICAL][Qt] 22.04.2023 15:36:52 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -    vtkvmtk<br>
[DEBUG][Python] 22.04.2023 15:36:52 [Python] (C:\ProgramData\NA-MIC\Slicer 4.11.20210226\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 22.04.2023 15:36:53 [Python] (C:\ProgramData\NA-MIC\Slicer 4.11.20210226\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 22.04.2023 15:36:53 [Python] (C:\ProgramData\NA-MIC\Slicer 4.11.20210226\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 22.04.2023 15:36:53 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “Welcome”<br>
[INFO][VTK] 22.04.2023 15:36:53 [vtkMRMLVolumeArchetypeStorageNode (0000019B073F5B80)] (D:\D\S\Slicer-1\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:509) - Loaded volume from file: C:/ProgramData/NA-MIC/Slicer 4.11.20210226/NA-MIC/Extensions-29738/SlicerVMTK/lib/Slicer-4.11/qt-scripted-modules/Resources/Vesselness.png. Dimensions: 65x50x1. Number of components: 3. Pixel type: unsigned char.<br>
[DEBUG][Qt] 22.04.2023 15:37:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Python console user input: import os<br>
[DEBUG][Qt] 22.04.2023 15:37:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Python console user input: os.chdir(‘C:/Users/lasa_/Documents/Firenze/Universita/Covid/slicer_guglielmo/Estensioni/Covid19LungLesion4/Covid19LungLesion4/’)<br>
[DEBUG][Qt] 22.04.2023 15:37:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Python console user input: import VesselsRemovalimport<br>
[DEBUG][Qt] 22.04.2023 15:37:10 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “DICOM”<br>
[DEBUG][Python] 22.04.2023 15:37:15 [Python] (C:\ProgramData\NA-MIC\Slicer 4.11.20210226\NA-MIC\Extensions-29738\QuantitativeReporting\lib\Slicer-4.11\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMParametricMapPluginClass : Caching files<br>
[DEBUG][Python] 22.04.2023 15:37:15 [Python] (C:\ProgramData\NA-MIC\Slicer 4.11.20210226\NA-MIC\Extensions-29738\QuantitativeReporting\lib\Slicer-4.11\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMParametricMapPluginClass : Using cached files<br>
[DEBUG][Python] 22.04.2023 15:37:15 [Python] (C:\ProgramData\NA-MIC\Slicer 4.11.20210226\NA-MIC\Extensions-29738\QuantitativeReporting\lib\Slicer-4.11\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMSegmentationPluginClass : Caching files<br>
[DEBUG][Python] 22.04.2023 15:37:15 [Python] (C:\ProgramData\NA-MIC\Slicer 4.11.20210226\NA-MIC\Extensions-29738\QuantitativeReporting\lib\Slicer-4.11\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMSegmentationPluginClass : Using cached files<br>
[DEBUG][Python] 22.04.2023 15:37:15 [Python] (C:\ProgramData\NA-MIC\Slicer 4.11.20210226\NA-MIC\Extensions-29738\QuantitativeReporting\lib\Slicer-4.11\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMTID1500PluginClass : Caching files<br>
[DEBUG][Python] 22.04.2023 15:37:15 [Python] (C:\ProgramData\NA-MIC\Slicer 4.11.20210226\NA-MIC\Extensions-29738\QuantitativeReporting\lib\Slicer-4.11\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMTID1500PluginClass : Using cached files<br>
[INFO][Python] 22.04.2023 15:37:16 [Python] (C:/ProgramData/NA-MIC/Slicer 4.11.20210226/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:384) - Loading with imageIOName: GDCM<br>
[INFO][Stream] 22.04.2023 15:37:16 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Loading with imageIOName: GDCM<br>
[DEBUG][Qt] 22.04.2023 15:37:29 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “Data”<br>
[DEBUG][Qt] 22.04.2023 15:37:33 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - “Markups” Reader has successfully read the file “C:/Users/lasa_/Desktop/F.mrk.json” “[0.02s]”<br>
[DEBUG][Qt] 22.04.2023 15:37:37 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “Covid19LungLesion4”<br>
[INFO][Stream] 22.04.2023 15:37:38 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -<br>
[INFO][Stream] 22.04.2023 15:37:38 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -<br>
[INFO][Stream] 22.04.2023 15:37:38 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -<br>
[INFO][Stream] 22.04.2023 15:37:38 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - ------------------------------<br>
[INFO][Stream] 22.04.2023 15:37:38 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Reloading module: Covid19LungLesion4<br>
[INFO][Stream] 22.04.2023 15:37:38 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - ------------------------------<br>
[INFO][Stream] 22.04.2023 15:37:38 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -<br>
[INFO][Stream] 22.04.2023 15:37:38 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -<br>
[INFO][Stream] 22.04.2023 15:37:38 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -</p>

---
