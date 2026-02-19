---
topic_id: 33167
title: "Vtkvmtk Module Is Not Loaded Please Help"
date: 2023-12-01
url: https://discourse.slicer.org/t/33167
---

# Vtkvmtk module is not loaded Please help

**Topic ID**: 33167
**Date**: 2023-12-01
**URL**: https://discourse.slicer.org/t/vtkvmtk-module-is-not-loaded-please-help/33167

---

## Post #1 by @Benny_Zamir (2023-12-01 18:37 UTC)

<p>[DEBUG][Qt] 01.12.2023 20:32:46 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Session start time …: 2023-12-01 20:32:46<br>
[DEBUG][Qt] 01.12.2023 20:32:46 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Slicer version …: 5.6.0 (revision 32390 / 0a13b9c) win-amd64 - installed release<br>
[DEBUG][Qt] 01.12.2023 20:32:46 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Operating system …: Windows /  Professional / (Build 19045, Code Page 65001) - 64-bit<br>
[DEBUG][Qt] 01.12.2023 20:32:46 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Memory …: 16255 MB physical, 18687 MB virtual<br>
[DEBUG][Qt] 01.12.2023 20:32:46 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - CPU …: GenuineIntel , 8 cores, 8 logical processors<br>
[DEBUG][Qt] 01.12.2023 20:32:46 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 01.12.2023 20:32:46 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Qt configuration …: version 5.15.2, with SSL, requested OpenGL 3.2 (compatibility profile)<br>
[DEBUG][Qt] 01.12.2023 20:32:46 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Internationalization …: disabled, language=<br>
[DEBUG][Qt] 01.12.2023 20:32:46 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Developer mode …: disabled<br>
[DEBUG][Qt] 01.12.2023 20:32:46 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Application path …: C:/ProgramData/slicer.org/Slicer 5.6.0/bin<br>
[DEBUG][Qt] 01.12.2023 20:32:46 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Additional module paths …: <a href="http://slicer.org/Extensions-32390/ExtraMarkups/lib/Slicer-5.6/qt-loadable-modules" rel="noopener nofollow ugc">slicer.org/Extensions-32390/ExtraMarkups/lib/Slicer-5.6/qt-loadable-modules</a>, <a href="http://slicer.org/Extensions-32390/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-32390/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-32390/PyTorch/lib/Slicer-5.6/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-32390/PyTorch/lib/Slicer-5.6/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-32390/SlicerOpenAnatomy/lib/Slicer-5.6/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-32390/SlicerOpenAnatomy/lib/Slicer-5.6/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-32390/SlicerVMTK/lib/Slicer-5.6/qt-loadable-modules" rel="noopener nofollow ugc">slicer.org/Extensions-32390/SlicerVMTK/lib/Slicer-5.6/qt-loadable-modules</a>, <a href="http://slicer.org/Extensions-32390/SlicerVMTK/lib/Slicer-5.6/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-32390/SlicerVMTK/lib/Slicer-5.6/qt-scripted-modules</a><br>
[CRITICAL][Stream] 01.12.2023 20:32:52 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Failed to load vtkSlicerCrossSectionAnalysisModuleLogicPython: No module named vtkSlicerShapeModuleMRMLPython<br>
[CRITICAL][Stream] 01.12.2023 20:32:52 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Failed to load vtkSlicerStenosisMeasurement3DModuleLogicPython: No module named vtkSlicerShapeModuleMRMLPython<br>
[CRITICAL][Qt] 01.12.2023 20:32:57 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Error(s):<br>
CLI executable: C:/ProgramData/slicer.org/Slicer 5.6.0/slicer.org/Extensions-32390/SlicerVMTK/lib/Slicer-5.6/qt-loadable-modules/vtkvmtk.py<br>
The process failed to start. Either the invoked program is missing, or you may have insufficient permissions to invoke the program.<br>
[CRITICAL][Qt] 01.12.2023 20:32:57 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Fail to instantiate module  “vtkvmtk”<br>
[CRITICAL][Qt] 01.12.2023 20:32:57 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - The following modules failed to be instantiated:<br>
[CRITICAL][Qt] 01.12.2023 20:32:57 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -    vtkvmtk<br>
[WARNING][Qt] 01.12.2023 20:32:58 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - When loading module  “GuidedArterySegmentation” , the dependency “SegmentEditorFloodFilling” failed to be loaded.<br>
[WARNING][Qt] 01.12.2023 20:32:58 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - When loading module  “QuickArterySegmentation” , the dependency “SegmentEditorFloodFilling” failed to be loaded.<br>
[DEBUG][Python] 01.12.2023 20:32:58 [Python] (C:\ProgramData\slicer.org\Slicer 5.6.0\lib\Slicer-5.6\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:39) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 01.12.2023 20:32:58 [Python] (C:\ProgramData\slicer.org\Slicer 5.6.0\lib\Slicer-5.6\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:39) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 01.12.2023 20:32:58 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “Welcome”</p>

---

## Post #2 by @muratmaga (2023-12-01 19:00 UTC)

<aside class="quote no-group" data-username="Benny_Zamir" data-post="1" data-topic="33167">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/benny_zamir/48/68452_2.png" class="avatar"> Benny_Zamir:</div>
<blockquote>
<p>C:/ProgramData/slicer.org/Slicer 5.6.0/slicer.org/Extensions-32390/SlicerVMTK/lib/Slicer-5.6/qt-loadable-modules/vtkvmtk.py</p>
</blockquote>
</aside>
<p>Install the Slicer to a folder accessible to you (e.g., your desktop), and then retry installing the extensions.</p>

---
