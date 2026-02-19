---
topic_id: 12185
title: "Fail To Load Openigtlinkif"
date: 2020-06-23
url: https://discourse.slicer.org/t/12185
---

# Fail to load OpenIGTLinkIF

**Topic ID**: 12185
**Date**: 2020-06-23
**URL**: https://discourse.slicer.org/t/fail-to-load-openigtlinkif/12185

---

## Post #1 by @kobidk (2020-06-23 20:22 UTC)

<p>Operating system:Windows<br>
Slicer version:4.10.2<br>
Expected behavior: Load OpenIGTLinkIF<br>
Actual behavior: Doesn’t appear in the Slicer menu “modules” list, after loading it as a package using Extention Manager.</p>

---

## Post #2 by @Sunderlandkyl (2020-06-23 20:53 UTC)

<p>Can you check if there is an error in the application log?<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ErrorLog#To_capture_the_entire_error_log_for_a_report" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ErrorLog#To_capture_the_entire_error_log_for_a_report</a></p>

---

## Post #3 by @kobidk (2020-06-24 08:05 UTC)

<p>Kyle,<br>
Thanks for your quick response.</p>
<ol>
<li>The following is the error log. I couldn’t understand the reason for the mismatch with the Qt library and also  the other error about  “vtkvmtk”</li>
<li>To build the DLLs library I run the following batch file. I hope this will clarify what I did,  maybe wrong.</li>
</ol>
<p>I hope you can clarify these for me.<br>
BR<br>
Kobi</p>
<p>The Batch file :<br>
mkdir N:\dev\3DSlicer\SlicerOpenIGTLink-master\OpenIGTLinkIF\Build<br>
cd /d N:\dev\3DSlicer\SlicerOpenIGTLink-master\OpenIGTLinkIF\Build<br>
“C:\Program Files\CMake\bin\cmake.exe” -G “Visual Studio 15 2017 Win64” -DQt5_DIR:PATH=N:\dev\Qt1\5.9.9\msvc2015_64\lib\cmake\Qt5 -DSlicer_DIR:PATH=N:\dev\DS41\DS41D\Slicer-build -DOpenIGTLinkIO_DIR:Path=N:\dev\3DSlicer\SlicerOpenIGTLink-master\Build\OpenIGTLinkIO-build  N:\dev\3DSlicer\SlicerOpenIGTLink-master\OpenIGTLinkIF<br>
“C:\Program Files\CMake\bin\cmake.exe” --build . --config Debug</p>
<p>The Error Log :</p>
<p>[DEBUG][Qt] 23.06.2020 23:19:23 [] (unknown:0) - Session start time …: 2020-06-23 23:19:23<br>
[DEBUG][Qt] 23.06.2020 23:19:23 [] (unknown:0) - Slicer version …: 4.10.2 (revision 28257) win-amd64 - installed release<br>
[DEBUG][Qt] 23.06.2020 23:19:23 [] (unknown:0) - Operating system …: Windows /  Personal /  (Build 9200) - 64-bit<br>
[DEBUG][Qt] 23.06.2020 23:19:23 [] (unknown:0) - Memory …: 16258 MB physical, 39905 MB virtual<br>
[DEBUG][Qt] 23.06.2020 23:19:23 [] (unknown:0) - CPU …: GenuineIntel , 8 cores, 8 logical processors<br>
[DEBUG][Qt] 23.06.2020 23:19:23 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 23.06.2020 23:19:23 [] (unknown:0) - Developer mode enabled …: yes<br>
[DEBUG][Qt] 23.06.2020 23:19:23 [] (unknown:0) - Prefer executable CLI …: no<br>
[DEBUG][Qt] 23.06.2020 23:19:23 [] (unknown:0) - Additional module paths …: C:/Users/kobid/AppData/Roaming/NA-MIC/Extensions-28257/SlicerIGT/lib/Slicer-4.10/qt-loadable-modules, C:/Users/kobid/AppData/Roaming/NA-MIC/Extensions-28257/SlicerIGT/lib/Slicer-4.10/qt-scripted-modules, C:/Users/kobid/AppData/Roaming/NA-MIC/Extensions-28257/SlicerVirtualReality/lib/Slicer-4.10/qt-loadable-modules, C:/Users/kobid/AppData/Roaming/NA-MIC/Extensions-28257/SlicerIGSIO/lib/Slicer-4.10/qt-loadable-modules, C:/Users/kobid/AppData/Roaming/NA-MIC/Extensions-28257/SlicerJupyter/lib/Slicer-4.10/qt-loadable-modules, C:/Users/kobid/AppData/Roaming/NA-MIC/Extensions-28257/SlicerVMTK/lib/Slicer-4.10/qt-loadable-modules, C:/Users/kobid/AppData/Roaming/NA-MIC/Extensions-28257/SlicerVMTK/lib/Slicer-4.10/qt-scripted-modules, N:/dev/DS41/DS41D/Slicer-build/Extensions/KobiTracker\KobiTracker\KobiTracker, C:/Users/kobid/AppData/Roaming/NA-MIC/Extensions-28866/SlicerIGT/lib/Slicer-4.10/qt-loadable-modules, C:/Users/kobid/AppData/Roaming/NA-MIC/Extensions-28866/SlicerIGT/lib/Slicer-4.10/qt-scripted-modules, C:/Users/kobid/AppData/Roaming/NA-MIC/Extensions-28866/EasyClip/lib/Slicer-4.10/qt-scripted-modules, C:/Users/kobid/AppData/Roaming/NA-MIC/Extensions-28866/AnglePlanesExtension/lib/Slicer-4.10/qt-scripted-modules, C:/Users/kobid/AppData/Roaming/NA-MIC/Extensions-28866/SlicerOpenCV/lib/Slicer-4.10/qt-loadable-modules, N:/dev/3DSlicer/Tutorial/ProgramingTutorial/HelloPython_Nightly/code/HelloPython, N:/dev/3DSlicer/Tutorial/ProgramingTutorial/HelloPython_Nightly/code/HelloLaplace, N:/dev/3DSlicer/Tutorial/ProgramingTutorial/HelloPython_Nightly/code/HelloSharpen, N:/dev/3DSlicer/Tutorial/SlicerSimpleWorkflow, N:/dev/3DSlicer/Tutorial/ExampleGuideletExtension-master/ExampleGuidelet, C:/Users/kobid/AppData/Roaming/NA-MIC/Extensions-28257/SlicerRT/lib/Slicer-4.10/cli-modules, C:/Users/kobid/AppData/Roaming/NA-MIC/Extensions-28257/SlicerRT/lib/Slicer-4.10/qt-loadable-modules, C:/Users/kobid/AppData/Roaming/NA-MIC/Extensions-28257/SlicerRT/lib/Slicer-4.10/qt-scripted-modules, N:/dev/3DSlicer/OpenIGTLinkIF/OpenIGTLinkIF-master/Build, N:/dev/3DSlicer/SlicerOpenIGTLink-master/Build/inner-build/lib/Slicer-4.11/qt-loadable-modules/Debug, C:/Users/kobid/AppData/Roaming/NA-MIC/Extensions-28257/AnglePlanesExtension/lib/Slicer-4.10/qt-scripted-modules, C:/Users/kobid/AppData/Roaming/NA-MIC/Extensions-28257/Sequences/lib/Slicer-4.10/qt-loadable-modules, C:/Users/kobid/AppData/Roaming/NA-MIC/Extensions-28257/Sequences/lib/Slicer-4.10/qt-scripted-modules, C:/Users/kobid/AppData/Roaming/NA-MIC/Extensions-28257/SlicerOpenCV/lib/Slicer-4.10/qt-loadable-modules, C:/Users/kobid/AppData/Roaming/NA-MIC/Extensions-28866/DCMQI/lib/Slicer-4.10/cli-modules, C:/Users/kobid/AppData/Roaming/NA-MIC/Extensions-28866/NeedleFinder/lib/Slicer-4.10/qt-scripted-modules, C:/Users/kobid/AppData/Roaming/NA-MIC/Extensions-28866/DeepInfer/lib/Slicer-4.10/qt-scripted-modules, C:/Users/kobid/AppData/Roaming/NA-MIC/Extensions-28866/ErodeDilateLabel/lib/Slicer-4.10/cli-modules, C:/Users/kobid/AppData/Roaming/NA-MIC/Extensions-28866/IntensitySegmenter/lib/Slicer-4.10/cli-modules<br>
[CRITICAL][Qt] 23.06.2020 23:19:26 [] (unknown:0) -   Error(s):<br>
The plugin ‘N:/dev/3DSlicer/SlicerOpenIGTLink-master/Build/inner-build/lib/Slicer-4.11/qt-loadable-modules/Debug/qSlicerOpenIGTLinkIFModule.dll’ uses incompatible Qt library. (Cannot mix debug and release libraries.)<br>
[CRITICAL][Qt] 23.06.2020 23:19:26 [] (unknown:0) -   Error(s):<br>
The plugin ‘N:/dev/3DSlicer/SlicerOpenIGTLink-master/Build/inner-build/lib/Slicer-4.11/qt-loadable-modules/Debug/qSlicerOpenIGTLinkRemoteModule.dll’ uses incompatible Qt library. (Cannot mix debug and release libraries.)<br>
[CRITICAL][Qt] 23.06.2020 23:19:26 [] (unknown:0) -   Error(s):<br>
The plugin ‘N:/dev/3DSlicer/SlicerOpenIGTLink-master/Build/inner-build/lib/Slicer-4.11/qt-loadable-modules/Debug/qSlicerPlusRemoteModule.dll’ uses incompatible Qt library. (Cannot mix debug and release libraries.)<br>
[INFO][Stream] 23.06.2020 23:19:28 [] (unknown:0) - .<strong>init</strong> -----------------------<br>
[INFO][Stream] 23.06.2020 23:19:28 [] (unknown:0) - .<strong>init</strong> -----------------------<br>
[INFO][Stream] 23.06.2020 23:19:28 [] (unknown:0) - .setLabels -----------------------<br>
[INFO][Stream] 23.06.2020 23:19:28 [] (unknown:0) - .setColors -----------------------<br>
[INFO][Stream] 23.06.2020 23:19:28 [] (unknown:0) - .setColors255 -----------------------<br>
[INFO][Stream] 23.06.2020 23:19:28 [] (unknown:0) - .setColors255 -----------------------<br>
[INFO][Stream] 23.06.2020 23:19:28 [] (unknown:0) - .setHolesCoordinates -----------------------<br>
[CRITICAL][Qt] 23.06.2020 23:19:28 [] (unknown:0) -   Error(s):<br>
CLI executable: C:/Users/kobid/AppData/Roaming/NA-MIC/Extensions-28257/SlicerVMTK/lib/Slicer-4.10/qt-loadable-modules/vtkvmtk.py<br>
The process failed to start. Either the invoked program is missing, or you may have insufficient permissions to invoke the program.<br>
[CRITICAL][Qt] 23.06.2020 23:19:28 [] (unknown:0) - Fail to instantiate module  “vtkvmtk”<br>
[DEBUG][Python] 23.06.2020 23:19:29 [Python] (N:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 23.06.2020 23:19:31 [Python] (N:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 23.06.2020 23:19:31 [Python] (N:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 23.06.2020 23:19:32 [] (unknown:0) - Switch to module:  “Welcome”<br>
[INFO][VTK] 23.06.2020 23:19:33 [vtkMRMLVolumeArchetypeStorageNode (0000022AE618A890)] (D:\D\S\Slicer-4102\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:465) - Loaded volume from file: C:/Users/kobid/AppData/Roaming/NA-MIC/Extensions-28257/SlicerVMTK/lib/Slicer-4.10/qt-scripted-modules/Resources/Vesselness.png. Dimensions: 65x50x1. Number of components: 3. Pixel type: unsigned char.<br>
[INFO][Stream] 23.06.2020 23:19:33 [] (unknown:0) - Loading Slicer RC file [C:/Users/kobid/AppData/Roaming/SPB_16.6/.slicerrc.py]</p>

---

## Post #4 by @Sunderlandkyl (2020-06-24 14:25 UTC)

<p>Can you clarify if you are using a downloaded version of Slicer 4.10.2, or one that you downloaded yourself?</p>
<p>If you are using a downloaded version of Slicer, you should download the SlicerOpenIGTLink extension from the extension manager.<br>
If you are using a version of Slicer that you compiled, you should make sure that you use the same configuration for both. Your Slicer appears to be Release, while SlicerOpenIGTLink is Debug.</p>

---
