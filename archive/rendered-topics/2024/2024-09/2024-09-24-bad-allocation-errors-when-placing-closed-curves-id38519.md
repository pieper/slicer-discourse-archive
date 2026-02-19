---
topic_id: 38519
title: "Bad Allocation Errors When Placing Closed Curves"
date: 2024-09-24
url: https://discourse.slicer.org/t/38519
---

# Bad allocation errors when placing closed curves

**Topic ID**: 38519
**Date**: 2024-09-24
**URL**: https://discourse.slicer.org/t/bad-allocation-errors-when-placing-closed-curves/38519

---

## Post #1 by @Logan_Moore (2024-09-24 15:09 UTC)

<p>Hi all,</p>
<p>I wanted to flag a string of bad allocation errors with closed curves in slicer 5.6 to 5.6.2. I am also using Slicermoprh, so perhaps <a class="mention" href="/u/muratmaga">@muratmaga</a> will have an idea of what is going on.</p>
<p>I haven’t been able to get this to occur consistently, but it has gotten fairly annoying. I have placed several thousand closed curve landmarks on a very large dataset. Every now and then whilst placing the closed curves, the system will lock up, eat up somewhere around 40 gigs of RAM, but if I wait patiently my data will be savable after the bad allocation error. I have only been able to get this to happen when PLACING landmarks, not resampling. Its also very inconsistent, sometimes I will go two or three hours without one, sometimes I will get multiples back to back.</p>
<p>I don’t have logs right now but can post them in a few hours. I just needed to make the post before I forget again.</p>

---

## Post #2 by @muratmaga (2024-09-24 15:28 UTC)

<p>Yeah, we will need log files and sample data to replicate the problem. Though several thousands points on a curve seems a lot!</p>

---

## Post #3 by @Logan_Moore (2024-09-24 15:30 UTC)

<p>Sorry I unintentionally made that unclear, its 11 landmarks on several hundred individuals adding up to several thousand. I have one last course to teach this morning and will be back collecting data on my regular PC. So logs will be soon!</p>

---

## Post #4 by @pieper (2024-09-24 15:53 UTC)

<p>Thanks for reporting this - what would be great is for someone to try replicating this with a python script and public data so that we can more easily isolate the underlying issue.</p>

---

## Post #5 by @Logan_Moore (2024-09-24 17:39 UTC)

<p>Hi all,</p>
<p>I am here with logs. I will post a few but it looks like I have 9 from yesterday alone.</p>
<pre><code class="lang-auto">[DEBUG][Qt] 24.09.2024 12:37:09 [] (unknown:0) - Session start time .......: 20240924_123709
[DEBUG][Qt] 24.09.2024 12:37:09 [] (unknown:0) - Slicer version ...........: 5.6.2 (revision 32448 / f10cd8c) win-amd64 - installed release
[DEBUG][Qt] 24.09.2024 12:37:09 [] (unknown:0) - Operating system .........: Windows /  Personal / (Build 22631, Code Page 65001) - 64-bit
[DEBUG][Qt] 24.09.2024 12:37:09 [] (unknown:0) - Memory ...................: 65265 MB physical, 77549 MB virtual
[DEBUG][Qt] 24.09.2024 12:37:09 [] (unknown:0) - CPU ......................: AuthenticAMD AMD Ryzen 9 7950X 16-Core Processor            , 32 cores, 32 logical processors
[DEBUG][Qt] 24.09.2024 12:37:09 [] (unknown:0) - VTK configuration ........: OpenGL2 rendering, TBB threading
[DEBUG][Qt] 24.09.2024 12:37:09 [] (unknown:0) - Qt configuration .........: version 5.15.2, with SSL, requested OpenGL 3.2 (compatibility profile)
[DEBUG][Qt] 24.09.2024 12:37:09 [] (unknown:0) - Internationalization .....: disabled, language=
[DEBUG][Qt] 24.09.2024 12:37:09 [] (unknown:0) - Developer mode ...........: disabled
[DEBUG][Qt] 24.09.2024 12:37:09 [] (unknown:0) - Application path .........: C:/Users/Logan/AppData/Local/slicer.org/Slicer 5.6.2/bin
[DEBUG][Qt] 24.09.2024 12:37:09 [] (unknown:0) - Additional module paths ..: slicer.org/Extensions-32448/AnglePlanesExtension/lib/Slicer-5.6/qt-scripted-modules, slicer.org/Extensions-32448/Auto3dgm/lib/Slicer-5.6/cli-modules, slicer.org/Extensions-32448/Auto3dgm/lib/Slicer-5.6/qt-scripted-modules, slicer.org/Extensions-32448/CurveMaker/lib/Slicer-5.6/qt-scripted-modules, slicer.org/Extensions-32448/EasyClip/lib/Slicer-5.6/qt-scripted-modules, slicer.org/Extensions-32448/ExtraMarkups/lib/Slicer-5.6/qt-loadable-modules, slicer.org/Extensions-32448/SegmentEditorExtraEffects/lib/Slicer-5.6/qt-loadable-modules, slicer.org/Extensions-32448/SegmentEditorExtraEffects/lib/Slicer-5.6/qt-scripted-modules, slicer.org/Extensions-32448/MarkupsToModel/lib/Slicer-5.6/qt-loadable-modules, slicer.org/Extensions-32448/FiducialsToModelDistance/lib/Slicer-5.6/qt-scripted-modules, slicer.org/Extensions-32448/MONAIAuto3DSeg/lib/Slicer-5.6/qt-scripted-modules, slicer.org/Extensions-32448/PyTorch/lib/Slicer-5.6/qt-scripted-modules, slicer.org/Extensions-32448/MeshStatisticsExtension/lib/Slicer-5.6/qt-scripted-modules, slicer.org/Extensions-32448/ModelClip/lib/Slicer-5.6/qt-loadable-modules, slicer.org/Extensions-32448/ModelCropper/lib/Slicer-5.6/qt-scripted-modules, slicer.org/Extensions-32448/SlicerBiomech/lib/Slicer-5.6/qt-scripted-modules, slicer.org/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules, slicer.org/Extensions-32448/SurfaceMarkup/lib/Slicer-5.6/qt-loadable-modules, slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules, slicer.org/Extensions-32448/MeshToLabelMap/lib/Slicer-5.6/cli-modules, slicer.org/Extensions-32448/MeshToLabelMap/lib/Slicer-5.6/qt-scripted-modules
[CRITICAL][Stream] 24.09.2024 12:37:12 [] (unknown:0) - Traceback (most recent call last):
[CRITICAL][Stream] 24.09.2024 12:37:12 [] (unknown:0) -   File "&lt;string&gt;", line 1, in &lt;module&gt;
[CRITICAL][Stream] 24.09.2024 12:37:12 [] (unknown:0) -   File "C:\Users\Logan\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\imp.py", line 169, in load_source
[CRITICAL][Stream] 24.09.2024 12:37:12 [] (unknown:0) -     module = _exec(spec, sys.modules[name])
[CRITICAL][Stream] 24.09.2024 12:37:12 [] (unknown:0) -   File "&lt;frozen importlib._bootstrap&gt;", line 613, in _exec
[CRITICAL][Stream] 24.09.2024 12:37:12 [] (unknown:0) -   File "&lt;frozen importlib._bootstrap_external&gt;", line 850, in exec_module
[CRITICAL][Stream] 24.09.2024 12:37:12 [] (unknown:0) -   File "&lt;frozen importlib._bootstrap&gt;", line 228, in _call_with_frames_removed
[CRITICAL][Stream] 24.09.2024 12:37:12 [] (unknown:0) -   File "C:/Users/Logan/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/CurveMaker/lib/Slicer-5.6/qt-scripted-modules/CurveMaker.py", line 6, in &lt;module&gt;
[CRITICAL][Stream] 24.09.2024 12:37:12 [] (unknown:0) -     from Endoscopy import EndoscopyComputePath
[CRITICAL][Stream] 24.09.2024 12:37:12 [] (unknown:0) - ImportError: cannot import name 'EndoscopyComputePath' from 'Endoscopy' (C:\Users\Logan\AppData\Local\slicer.org\Slicer 5.6.2\lib\Slicer-5.6\qt-scripted-modules\Endoscopy.py)
[CRITICAL][Qt] 24.09.2024 12:37:12 [] (unknown:0) - loadSourceAsModule - Failed to load file "C:/Users/Logan/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/CurveMaker/lib/Slicer-5.6/qt-scripted-modules/CurveMaker.py"  as module "CurveMaker" !
[CRITICAL][Qt] 24.09.2024 12:37:12 [] (unknown:0) - Fail to instantiate module  "CurveMaker"
[WARNING][Qt] 24.09.2024 12:37:15 [] (unknown:0) - libpng warning: iCCP: profile 'ICC Profile': 'CMYK': invalid ICC profile color space
[WARNING][Qt] 24.09.2024 12:37:15 [] (unknown:0) - libpng warning: iCCP: known incorrect sRGB profile
[WARNING][Qt] 24.09.2024 12:37:15 [] (unknown:0) - libpng warning: iCCP: known incorrect sRGB profile
[WARNING][Qt] 24.09.2024 12:37:15 [] (unknown:0) - libpng warning: iCCP: known incorrect sRGB profile
[CRITICAL][Qt] 24.09.2024 12:37:16 [] (unknown:0) - The following modules failed to be instantiated:
[CRITICAL][Qt] 24.09.2024 12:37:16 [] (unknown:0) -    CurveMaker
[WARNING][Qt] 24.09.2024 12:37:16 [] (unknown:0) - libpng warning: iCCP: known incorrect sRGB profile
[WARNING][Qt] 24.09.2024 12:37:16 [] (unknown:0) - libpng warning: iCCP: known incorrect sRGB profile
[WARNING][Qt] 24.09.2024 12:37:16 [] (unknown:0) - libpng warning: iCCP: known incorrect sRGB profile
[WARNING][Qt] 24.09.2024 12:37:16 [] (unknown:0) - libpng warning: iCCP: known incorrect sRGB profile
[WARNING][Qt] 24.09.2024 12:37:16 [] (unknown:0) - libpng warning: iCCP: known incorrect sRGB profile
[DEBUG][Python] 24.09.2024 12:37:16 [Python] (C:\Users\Logan\AppData\Local\slicer.org\Slicer 5.6.2\lib\Slicer-5.6\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:39) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 24.09.2024 12:37:16 [Python] (C:\Users\Logan\AppData\Local\slicer.org\Slicer 5.6.2\lib\Slicer-5.6\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:39) - Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Qt] 24.09.2024 12:37:16 [] (unknown:0) - Switch to module:  "Data"
[DEBUG][Python] 24.09.2024 12:37:16 [Python] (C:\Users\Logan\AppData\Local\slicer.org\Slicer 5.6.2\lib\Slicer-5.6\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:39) - Scripted subject hierarchy plugin registered: FormatMarkups
[INFO][Python] 24.09.2024 12:37:16 [Python] (&lt;string&gt;:3) - Adding SlicerMorph Volume Rendering Presets
[INFO][Python] 24.09.2024 12:37:16 [Python] (&lt;string&gt;:3) - Customizing with SlicerMorphRC.py
[INFO][Python] 24.09.2024 12:37:16 [Python] (&lt;string&gt;:10) -   Volume nodes will be stored uncompressed by default
[INFO][Python] 24.09.2024 12:37:16 [Python] (&lt;string&gt;:18) -   Segmentation nodes will be stored uncompressed
[INFO][Python] 24.09.2024 12:37:16 [Python] (&lt;string&gt;:170) -   5 keyboard shortcuts installed
[INFO][Python] 24.09.2024 12:37:16 [Python] (&lt;string&gt;:173) - Set up undo/redo buttons for markups
[INFO][Python] 24.09.2024 12:37:16 [Python] (&lt;string&gt;:211) - Done customizing with SlicerMorphRC.py
[INFO][Python] 24.09.2024 12:37:16 [Python] (&lt;string&gt;:212) - On first load of customization, restart Slicer to take effect.
</code></pre>
<pre><code class="lang-auto">[DEBUG][Qt] 23.09.2024 23:49:50 [] (unknown:0) - Session start time .......: 20240923_234950
[DEBUG][Qt] 23.09.2024 23:49:50 [] (unknown:0) - Slicer version ...........: 5.6.2 (revision 32448 / f10cd8c) win-amd64 - installed release
[DEBUG][Qt] 23.09.2024 23:49:50 [] (unknown:0) - Operating system .........: Windows /  Personal / (Build 22631, Code Page 65001) - 64-bit
[DEBUG][Qt] 23.09.2024 23:49:50 [] (unknown:0) - Memory ...................: 65265 MB physical, 77549 MB virtual
[DEBUG][Qt] 23.09.2024 23:49:50 [] (unknown:0) - CPU ......................: AuthenticAMD AMD Ryzen 9 7950X 16-Core Processor            , 32 cores, 32 logical processors
[DEBUG][Qt] 23.09.2024 23:49:50 [] (unknown:0) - VTK configuration ........: OpenGL2 rendering, TBB threading
[DEBUG][Qt] 23.09.2024 23:49:50 [] (unknown:0) - Qt configuration .........: version 5.15.2, with SSL, requested OpenGL 3.2 (compatibility profile)
[DEBUG][Qt] 23.09.2024 23:49:50 [] (unknown:0) - Internationalization .....: disabled, language=
[DEBUG][Qt] 23.09.2024 23:49:50 [] (unknown:0) - Developer mode ...........: disabled
[DEBUG][Qt] 23.09.2024 23:49:50 [] (unknown:0) - Application path .........: C:/Users/Logan/AppData/Local/slicer.org/Slicer 5.6.2/bin
[DEBUG][Qt] 23.09.2024 23:49:50 [] (unknown:0) - Additional module paths ..: slicer.org/Extensions-32448/AnglePlanesExtension/lib/Slicer-5.6/qt-scripted-modules, slicer.org/Extensions-32448/Auto3dgm/lib/Slicer-5.6/cli-modules, slicer.org/Extensions-32448/Auto3dgm/lib/Slicer-5.6/qt-scripted-modules, slicer.org/Extensions-32448/CurveMaker/lib/Slicer-5.6/qt-scripted-modules, slicer.org/Extensions-32448/EasyClip/lib/Slicer-5.6/qt-scripted-modules, slicer.org/Extensions-32448/ExtraMarkups/lib/Slicer-5.6/qt-loadable-modules, slicer.org/Extensions-32448/SegmentEditorExtraEffects/lib/Slicer-5.6/qt-loadable-modules, slicer.org/Extensions-32448/SegmentEditorExtraEffects/lib/Slicer-5.6/qt-scripted-modules, slicer.org/Extensions-32448/MarkupsToModel/lib/Slicer-5.6/qt-loadable-modules, slicer.org/Extensions-32448/FiducialsToModelDistance/lib/Slicer-5.6/qt-scripted-modules, slicer.org/Extensions-32448/MONAIAuto3DSeg/lib/Slicer-5.6/qt-scripted-modules, slicer.org/Extensions-32448/PyTorch/lib/Slicer-5.6/qt-scripted-modules, slicer.org/Extensions-32448/MeshStatisticsExtension/lib/Slicer-5.6/qt-scripted-modules, slicer.org/Extensions-32448/ModelClip/lib/Slicer-5.6/qt-loadable-modules, slicer.org/Extensions-32448/ModelCropper/lib/Slicer-5.6/qt-scripted-modules, slicer.org/Extensions-32448/SlicerBiomech/lib/Slicer-5.6/qt-scripted-modules, slicer.org/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules, slicer.org/Extensions-32448/SurfaceMarkup/lib/Slicer-5.6/qt-loadable-modules, slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules, slicer.org/Extensions-32448/MeshToLabelMap/lib/Slicer-5.6/cli-modules, slicer.org/Extensions-32448/MeshToLabelMap/lib/Slicer-5.6/qt-scripted-modules
[CRITICAL][Stream] 23.09.2024 23:49:51 [] (unknown:0) - Traceback (most recent call last):
[CRITICAL][Stream] 23.09.2024 23:49:51 [] (unknown:0) -   File "&lt;string&gt;", line 1, in &lt;module&gt;
[CRITICAL][Stream] 23.09.2024 23:49:51 [] (unknown:0) -   File "C:\Users\Logan\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\imp.py", line 169, in load_source
[CRITICAL][Stream] 23.09.2024 23:49:51 [] (unknown:0) -     module = _exec(spec, sys.modules[name])
[CRITICAL][Stream] 23.09.2024 23:49:51 [] (unknown:0) -   File "&lt;frozen importlib._bootstrap&gt;", line 613, in _exec
[CRITICAL][Stream] 23.09.2024 23:49:51 [] (unknown:0) -   File "&lt;frozen importlib._bootstrap_external&gt;", line 850, in exec_module
[CRITICAL][Stream] 23.09.2024 23:49:51 [] (unknown:0) -   File "&lt;frozen importlib._bootstrap&gt;", line 228, in _call_with_frames_removed
[CRITICAL][Stream] 23.09.2024 23:49:51 [] (unknown:0) -   File "C:/Users/Logan/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/CurveMaker/lib/Slicer-5.6/qt-scripted-modules/CurveMaker.py", line 6, in &lt;module&gt;
[CRITICAL][Stream] 23.09.2024 23:49:51 [] (unknown:0) -     from Endoscopy import EndoscopyComputePath
[CRITICAL][Stream] 23.09.2024 23:49:51 [] (unknown:0) - ImportError: cannot import name 'EndoscopyComputePath' from 'Endoscopy' (C:\Users\Logan\AppData\Local\slicer.org\Slicer 5.6.2\lib\Slicer-5.6\qt-scripted-modules\Endoscopy.py)
[CRITICAL][Qt] 23.09.2024 23:49:51 [] (unknown:0) - loadSourceAsModule - Failed to load file "C:/Users/Logan/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/CurveMaker/lib/Slicer-5.6/qt-scripted-modules/CurveMaker.py"  as module "CurveMaker" !
[CRITICAL][Qt] 23.09.2024 23:49:51 [] (unknown:0) - Fail to instantiate module  "CurveMaker"
[WARNING][Qt] 23.09.2024 23:49:51 [] (unknown:0) - libpng warning: iCCP: profile 'ICC Profile': 'CMYK': invalid ICC profile color space
[WARNING][Qt] 23.09.2024 23:49:51 [] (unknown:0) - libpng warning: iCCP: known incorrect sRGB profile
[WARNING][Qt] 23.09.2024 23:49:51 [] (unknown:0) - libpng warning: iCCP: known incorrect sRGB profile
[WARNING][Qt] 23.09.2024 23:49:51 [] (unknown:0) - libpng warning: iCCP: known incorrect sRGB profile
[CRITICAL][Qt] 23.09.2024 23:49:52 [] (unknown:0) - The following modules failed to be instantiated:
[CRITICAL][Qt] 23.09.2024 23:49:52 [] (unknown:0) -    CurveMaker
[WARNING][Qt] 23.09.2024 23:49:52 [] (unknown:0) - libpng warning: iCCP: known incorrect sRGB profile
[WARNING][Qt] 23.09.2024 23:49:52 [] (unknown:0) - libpng warning: iCCP: known incorrect sRGB profile
[WARNING][Qt] 23.09.2024 23:49:52 [] (unknown:0) - libpng warning: iCCP: known incorrect sRGB profile
[WARNING][Qt] 23.09.2024 23:49:52 [] (unknown:0) - libpng warning: iCCP: known incorrect sRGB profile
[WARNING][Qt] 23.09.2024 23:49:52 [] (unknown:0) - libpng warning: iCCP: known incorrect sRGB profile
[DEBUG][Python] 23.09.2024 23:49:52 [Python] (C:\Users\Logan\AppData\Local\slicer.org\Slicer 5.6.2\lib\Slicer-5.6\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:39) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 23.09.2024 23:49:52 [Python] (C:\Users\Logan\AppData\Local\slicer.org\Slicer 5.6.2\lib\Slicer-5.6\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:39) - Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Qt] 23.09.2024 23:49:52 [] (unknown:0) - Switch to module:  "Data"
[DEBUG][Python] 23.09.2024 23:49:52 [Python] (C:\Users\Logan\AppData\Local\slicer.org\Slicer 5.6.2\lib\Slicer-5.6\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:39) - Scripted subject hierarchy plugin registered: FormatMarkups
[INFO][Python] 23.09.2024 23:49:52 [Python] (&lt;string&gt;:3) - Adding SlicerMorph Volume Rendering Presets
[INFO][Python] 23.09.2024 23:49:52 [Python] (&lt;string&gt;:3) - Customizing with SlicerMorphRC.py
[INFO][Python] 23.09.2024 23:49:52 [Python] (&lt;string&gt;:10) -   Volume nodes will be stored uncompressed by default
[INFO][Python] 23.09.2024 23:49:52 [Python] (&lt;string&gt;:18) -   Segmentation nodes will be stored uncompressed
[INFO][Python] 23.09.2024 23:49:52 [Python] (&lt;string&gt;:170) -   5 keyboard shortcuts installed
[INFO][Python] 23.09.2024 23:49:52 [Python] (&lt;string&gt;:173) - Set up undo/redo buttons for markups
[INFO][Python] 23.09.2024 23:49:52 [Python] (&lt;string&gt;:211) - Done customizing with SlicerMorphRC.py
[INFO][Python] 23.09.2024 23:49:52 [Python] (&lt;string&gt;:212) - On first load of customization, restart Slicer to take effect.
[DEBUG][Qt] 23.09.2024 23:49:58 [] (unknown:0) - "Model" Reader has successfully read the file "G:/rights/214-10/214-10.ply" "[0.08s]"
[DEBUG][Qt] 23.09.2024 23:50:01 [] (unknown:0) - Switch to module:  "Markups"
[WARNING][VTK] 23.09.2024 23:54:27 [vtkDelaunay2D (000002DD994C39A0)] (vtkMRMLMarkupsClosedCurveNode.cxx, line 244
FitSurfaceProjectWarp failed: error triangulating the surface area of the closed curve. Details: Warning: Warning: In vtkDelaunay2D.cxx:1447) - Edge not recovered, polygon fill not possible
[WARNING][VTK] 23.09.2024 23:54:27 [vtkDelaunay2D (000002DD994C7170)] (vtkMRMLMarkupsClosedCurveNode.cxx, line 244
FitSurfaceProjectWarp failed: error triangulating the surface area of the closed curve. Details: Warning: Warning: In vtkDelaunay2D.cxx:1447) - Edge not recovered, polygon fill not possible
[WARNING][VTK] 23.09.2024 23:54:27 [vtkDelaunay2D (000002DD994C7170)] (vtkMRMLMarkupsClosedCurveNode.cxx, line 244
FitSurfaceProjectWarp failed: error triangulating the surface area of the closed curve. Details: Warning: Warning: In vtkDelaunay2D.cxx:1447) - Edge not recovered, polygon fill not possible
[WARNING][VTK] 23.09.2024 23:54:27 [vtkDelaunay2D (000002DD994C39A0)] (vtkMRMLMarkupsClosedCurveNode.cxx, line 244
FitSurfaceProjectWarp failed: error triangulating the surface area of the closed curve. Details: Warning: Warning: In vtkDelaunay2D.cxx:1447) - Edge not recovered, polygon fill not possible
[WARNING][VTK] 23.09.2024 23:54:30 [vtkDelaunay2D (000002DD94BBAE00)] (vtkMRMLMarkupsClosedCurveNode.cxx, line 244
FitSurfaceProjectWarp failed: error triangulating the surface area of the closed curve. Details: Warning: Warning: In vtkDelaunay2D.cxx:1447) - Edge not recovered, polygon fill not possible
[WARNING][VTK] 23.09.2024 23:54:30 [vtkDelaunay2D (000002DD94BBB060)] (vtkMRMLMarkupsClosedCurveNode.cxx, line 244
FitSurfaceProjectWarp failed: error triangulating the surface area of the closed curve. Details: Warning: Warning: In vtkDelaunay2D.cxx:1447) - Edge not recovered, polygon fill not possible
[WARNING][VTK] 23.09.2024 23:54:30 [vtkDelaunay2D (000002DD585D1320)] (vtkMRMLMarkupsClosedCurveNode.cxx, line 244
FitSurfaceProjectWarp failed: error triangulating the surface area of the closed curve. Details: Warning: Warning: In vtkDelaunay2D.cxx:1447) - Edge not recovered, polygon fill not possible
[WARNING][VTK] 23.09.2024 23:54:30 [vtkDelaunay2D (000002DD585D1580)] (vtkMRMLMarkupsClosedCurveNode.cxx, line 244
FitSurfaceProjectWarp failed: error triangulating the surface area of the closed curve. Details: Warning: Warning: In vtkDelaunay2D.cxx:1447) - Edge not recovered, polygon fill not possible
[WARNING][VTK] 23.09.2024 23:54:30 [vtkDelaunay2D (000002DD585D17E0)] (vtkMRMLMarkupsClosedCurveNode.cxx, line 244
FitSurfaceProjectWarp failed: error triangulating the surface area of the closed curve. Details: Warning: Warning: In vtkDelaunay2D.cxx:1447) - Edge not recovered, polygon fill not possible
[WARNING][VTK] 23.09.2024 23:54:53 [vtkDelaunay2D (000002DD94BBC230)] (vtkMRMLMarkupsClosedCurveNode.cxx, line 244
FitSurfaceProjectWarp failed: error triangulating the surface area of the closed curve. Details: Warning: Warning: In vtkDelaunay2D.cxx:1447) - Edge not recovered, polygon fill not possible
[WARNING][VTK] 23.09.2024 23:54:53 [vtkDelaunay2D (000002DD94BBACD0)] (vtkMRMLMarkupsClosedCurveNode.cxx, line 244
FitSurfaceProjectWarp failed: error triangulating the surface area of the closed curve. Details: Warning: Warning: In vtkDelaunay2D.cxx:1447) - Edge not recovered, polygon fill not possible
[DEBUG][Qt] 23.09.2024 23:55:15 [] (unknown:0) - void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: ""
[DEBUG][Qt] 23.09.2024 23:55:15 [] (unknown:0) - void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: ""
[DEBUG][Qt] 23.09.2024 23:55:15 [] (unknown:0) - void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: ""
[DEBUG][Qt] 23.09.2024 23:55:15 [] (unknown:0) - void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: ""
[DEBUG][Qt] 23.09.2024 23:55:15 [] (unknown:0) - void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: ""
[DEBUG][Qt] 23.09.2024 23:55:15 [] (unknown:0) - void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: ""
[DEBUG][Qt] 23.09.2024 23:55:15 [] (unknown:0) - void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: ""
[DEBUG][Qt] 23.09.2024 23:55:15 [] (unknown:0) - void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: ""
[DEBUG][Qt] 23.09.2024 23:55:15 [] (unknown:0) - void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: ""
[DEBUG][Qt] 23.09.2024 23:55:15 [] (unknown:0) - void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: ""
[DEBUG][Qt] 23.09.2024 23:55:15 [] (unknown:0) - void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: ""
[DEBUG][Qt] 23.09.2024 23:57:25 [] (unknown:0) - Switch to module:  ""
[WARNING][Qt] 23.09.2024 23:57:25 [] (unknown:0) - QMainWindow::saveState(): 'objectName' not set for QToolBar 0x2dd147785d0 'Undo/Redo'
[WARNING][Qt] 23.09.2024 23:57:25 [] (unknown:0) - External WM_DESTROY received for  QWidgetWindow(0x2dd14b10fd0, name="qSlicerDataDialogWindow") , parent:  QWindow(0x0) , transient parent:  QWindow(0x0)
</code></pre>
<pre><code class="lang-auto">[DEBUG][Qt] 23.09.2024 23:43:54 [] (unknown:0) - Session start time .......: 20240923_234354
[DEBUG][Qt] 23.09.2024 23:43:54 [] (unknown:0) - Slicer version ...........: 5.6.2 (revision 32448 / f10cd8c) win-amd64 - installed release
[DEBUG][Qt] 23.09.2024 23:43:54 [] (unknown:0) - Operating system .........: Windows /  Personal / (Build 22631, Code Page 65001) - 64-bit
[DEBUG][Qt] 23.09.2024 23:43:54 [] (unknown:0) - Memory ...................: 65265 MB physical, 77549 MB virtual
[DEBUG][Qt] 23.09.2024 23:43:54 [] (unknown:0) - CPU ......................: AuthenticAMD AMD Ryzen 9 7950X 16-Core Processor            , 32 cores, 32 logical processors
[DEBUG][Qt] 23.09.2024 23:43:54 [] (unknown:0) - VTK configuration ........: OpenGL2 rendering, TBB threading
[DEBUG][Qt] 23.09.2024 23:43:54 [] (unknown:0) - Qt configuration .........: version 5.15.2, with SSL, requested OpenGL 3.2 (compatibility profile)
[DEBUG][Qt] 23.09.2024 23:43:54 [] (unknown:0) - Internationalization .....: disabled, language=
[DEBUG][Qt] 23.09.2024 23:43:54 [] (unknown:0) - Developer mode ...........: disabled
[DEBUG][Qt] 23.09.2024 23:43:54 [] (unknown:0) - Application path .........: C:/Users/Logan/AppData/Local/slicer.org/Slicer 5.6.2/bin
[DEBUG][Qt] 23.09.2024 23:43:54 [] (unknown:0) - Additional module paths ..: slicer.org/Extensions-32448/AnglePlanesExtension/lib/Slicer-5.6/qt-scripted-modules, slicer.org/Extensions-32448/Auto3dgm/lib/Slicer-5.6/cli-modules, slicer.org/Extensions-32448/Auto3dgm/lib/Slicer-5.6/qt-scripted-modules, slicer.org/Extensions-32448/CurveMaker/lib/Slicer-5.6/qt-scripted-modules, slicer.org/Extensions-32448/EasyClip/lib/Slicer-5.6/qt-scripted-modules, slicer.org/Extensions-32448/ExtraMarkups/lib/Slicer-5.6/qt-loadable-modules, slicer.org/Extensions-32448/SegmentEditorExtraEffects/lib/Slicer-5.6/qt-loadable-modules, slicer.org/Extensions-32448/SegmentEditorExtraEffects/lib/Slicer-5.6/qt-scripted-modules, slicer.org/Extensions-32448/MarkupsToModel/lib/Slicer-5.6/qt-loadable-modules, slicer.org/Extensions-32448/FiducialsToModelDistance/lib/Slicer-5.6/qt-scripted-modules, slicer.org/Extensions-32448/MONAIAuto3DSeg/lib/Slicer-5.6/qt-scripted-modules, slicer.org/Extensions-32448/PyTorch/lib/Slicer-5.6/qt-scripted-modules, slicer.org/Extensions-32448/MeshStatisticsExtension/lib/Slicer-5.6/qt-scripted-modules, slicer.org/Extensions-32448/ModelClip/lib/Slicer-5.6/qt-loadable-modules, slicer.org/Extensions-32448/ModelCropper/lib/Slicer-5.6/qt-scripted-modules, slicer.org/Extensions-32448/SlicerBiomech/lib/Slicer-5.6/qt-scripted-modules, slicer.org/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules, slicer.org/Extensions-32448/SurfaceMarkup/lib/Slicer-5.6/qt-loadable-modules, slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules, slicer.org/Extensions-32448/MeshToLabelMap/lib/Slicer-5.6/cli-modules, slicer.org/Extensions-32448/MeshToLabelMap/lib/Slicer-5.6/qt-scripted-modules
[CRITICAL][Stream] 23.09.2024 23:43:55 [] (unknown:0) - Traceback (most recent call last):
[CRITICAL][Stream] 23.09.2024 23:43:55 [] (unknown:0) -   File "&lt;string&gt;", line 1, in &lt;module&gt;
[CRITICAL][Stream] 23.09.2024 23:43:55 [] (unknown:0) -   File "C:\Users\Logan\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\imp.py", line 169, in load_source
[CRITICAL][Stream] 23.09.2024 23:43:55 [] (unknown:0) -     module = _exec(spec, sys.modules[name])
[CRITICAL][Stream] 23.09.2024 23:43:55 [] (unknown:0) -   File "&lt;frozen importlib._bootstrap&gt;", line 613, in _exec
[CRITICAL][Stream] 23.09.2024 23:43:55 [] (unknown:0) -   File "&lt;frozen importlib._bootstrap_external&gt;", line 850, in exec_module
[CRITICAL][Stream] 23.09.2024 23:43:55 [] (unknown:0) -   File "&lt;frozen importlib._bootstrap&gt;", line 228, in _call_with_frames_removed
[CRITICAL][Stream] 23.09.2024 23:43:55 [] (unknown:0) -   File "C:/Users/Logan/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/CurveMaker/lib/Slicer-5.6/qt-scripted-modules/CurveMaker.py", line 6, in &lt;module&gt;
[CRITICAL][Stream] 23.09.2024 23:43:55 [] (unknown:0) -     from Endoscopy import EndoscopyComputePath
[CRITICAL][Stream] 23.09.2024 23:43:55 [] (unknown:0) - ImportError: cannot import name 'EndoscopyComputePath' from 'Endoscopy' (C:\Users\Logan\AppData\Local\slicer.org\Slicer 5.6.2\lib\Slicer-5.6\qt-scripted-modules\Endoscopy.py)
[CRITICAL][Qt] 23.09.2024 23:43:55 [] (unknown:0) - loadSourceAsModule - Failed to load file "C:/Users/Logan/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/CurveMaker/lib/Slicer-5.6/qt-scripted-modules/CurveMaker.py"  as module "CurveMaker" !
[CRITICAL][Qt] 23.09.2024 23:43:55 [] (unknown:0) - Fail to instantiate module  "CurveMaker"
[WARNING][Qt] 23.09.2024 23:43:55 [] (unknown:0) - libpng warning: iCCP: profile 'ICC Profile': 'CMYK': invalid ICC profile color space
[WARNING][Qt] 23.09.2024 23:43:55 [] (unknown:0) - libpng warning: iCCP: known incorrect sRGB profile
[WARNING][Qt] 23.09.2024 23:43:55 [] (unknown:0) - libpng warning: iCCP: known incorrect sRGB profile
[WARNING][Qt] 23.09.2024 23:43:55 [] (unknown:0) - libpng warning: iCCP: known incorrect sRGB profile
[CRITICAL][Qt] 23.09.2024 23:43:56 [] (unknown:0) - The following modules failed to be instantiated:
[CRITICAL][Qt] 23.09.2024 23:43:56 [] (unknown:0) -    CurveMaker
[WARNING][Qt] 23.09.2024 23:43:56 [] (unknown:0) - libpng warning: iCCP: known incorrect sRGB profile
[WARNING][Qt] 23.09.2024 23:43:56 [] (unknown:0) - libpng warning: iCCP: known incorrect sRGB profile
[WARNING][Qt] 23.09.2024 23:43:56 [] (unknown:0) - libpng warning: iCCP: known incorrect sRGB profile
[WARNING][Qt] 23.09.2024 23:43:56 [] (unknown:0) - libpng warning: iCCP: known incorrect sRGB profile
[WARNING][Qt] 23.09.2024 23:43:56 [] (unknown:0) - libpng warning: iCCP: known incorrect sRGB profile
[DEBUG][Python] 23.09.2024 23:43:56 [Python] (C:\Users\Logan\AppData\Local\slicer.org\Slicer 5.6.2\lib\Slicer-5.6\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:39) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 23.09.2024 23:43:56 [Python] (C:\Users\Logan\AppData\Local\slicer.org\Slicer 5.6.2\lib\Slicer-5.6\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:39) - Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Qt] 23.09.2024 23:43:56 [] (unknown:0) - Switch to module:  "Data"
[DEBUG][Python] 23.09.2024 23:43:56 [Python] (C:\Users\Logan\AppData\Local\slicer.org\Slicer 5.6.2\lib\Slicer-5.6\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:39) - Scripted subject hierarchy plugin registered: FormatMarkups
[INFO][Python] 23.09.2024 23:43:56 [Python] (&lt;string&gt;:3) - Adding SlicerMorph Volume Rendering Presets
[INFO][Python] 23.09.2024 23:43:56 [Python] (&lt;string&gt;:3) - Customizing with SlicerMorphRC.py
[INFO][Python] 23.09.2024 23:43:56 [Python] (&lt;string&gt;:10) -   Volume nodes will be stored uncompressed by default
[INFO][Python] 23.09.2024 23:43:56 [Python] (&lt;string&gt;:18) -   Segmentation nodes will be stored uncompressed
[INFO][Python] 23.09.2024 23:43:56 [Python] (&lt;string&gt;:170) -   5 keyboard shortcuts installed
[INFO][Python] 23.09.2024 23:43:56 [Python] (&lt;string&gt;:173) - Set up undo/redo buttons for markups
[INFO][Python] 23.09.2024 23:43:56 [Python] (&lt;string&gt;:211) - Done customizing with SlicerMorphRC.py
[INFO][Python] 23.09.2024 23:43:56 [Python] (&lt;string&gt;:212) - On first load of customization, restart Slicer to take effect.
[DEBUG][Qt] 23.09.2024 23:44:00 [] (unknown:0) - "Model" Reader has successfully read the file "G:/rights/214-9/214-9.ply" "[0.09s]"
[DEBUG][Qt] 23.09.2024 23:44:03 [] (unknown:0) - Switch to module:  "Markups"
[WARNING][VTK] 23.09.2024 23:47:55 [vtkDelaunay2D (000001C513E6C520)] (vtkMRMLMarkupsClosedCurveNode.cxx, line 244
FitSurfaceProjectWarp failed: error triangulating the surface area of the closed curve. Details: Warning: Warning: In vtkDelaunay2D.cxx:1447) - Edge not recovered, polygon fill not possible
[WARNING][VTK] 23.09.2024 23:47:55 [vtkDelaunay2D (000001C513792920)] (vtkMRMLMarkupsClosedCurveNode.cxx, line 244
FitSurfaceProjectWarp failed: error triangulating the surface area of the closed curve. Details: Warning: Warning: In vtkDelaunay2D.cxx:1447) - Edge not recovered, polygon fill not possible
[WARNING][VTK] 23.09.2024 23:48:11 [vtkDelaunay2D (000001C4A572C350)] (vtkMRMLMarkupsClosedCurveNode.cxx, line 244
FitSurfaceProjectWarp failed: error triangulating the surface area of the closed curve. Details: Warning: Warning: In vtkDelaunay2D.cxx:1447) - Edge not recovered, polygon fill not possible
[WARNING][VTK] 23.09.2024 23:48:11 [vtkDelaunay2D (000001C4A572D2C0)] (vtkMRMLMarkupsClosedCurveNode.cxx, line 244
FitSurfaceProjectWarp failed: error triangulating the surface area of the closed curve. Details: Warning: Warning: In vtkDelaunay2D.cxx:1447) - Edge not recovered, polygon fill not possible
[DEBUG][Qt] 23.09.2024 23:49:39 [] (unknown:0) - void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: ""
[DEBUG][Qt] 23.09.2024 23:49:39 [] (unknown:0) - void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: ""
[DEBUG][Qt] 23.09.2024 23:49:39 [] (unknown:0) - void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: ""
[DEBUG][Qt] 23.09.2024 23:49:39 [] (unknown:0) - void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: ""
[DEBUG][Qt] 23.09.2024 23:49:39 [] (unknown:0) - void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: ""
[DEBUG][Qt] 23.09.2024 23:49:39 [] (unknown:0) - void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: ""
[DEBUG][Qt] 23.09.2024 23:49:39 [] (unknown:0) - void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: ""
[DEBUG][Qt] 23.09.2024 23:49:39 [] (unknown:0) - void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: ""
[DEBUG][Qt] 23.09.2024 23:49:39 [] (unknown:0) - void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: ""
[DEBUG][Qt] 23.09.2024 23:49:39 [] (unknown:0) - void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: ""
[DEBUG][Qt] 23.09.2024 23:49:39 [] (unknown:0) - void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: ""
[DEBUG][Qt] 23.09.2024 23:49:47 [] (unknown:0) - Switch to module:  ""
[WARNING][Qt] 23.09.2024 23:49:47 [] (unknown:0) - QMainWindow::saveState(): 'objectName' not set for QToolBar 0x1c495bfdd70 'Undo/Redo'
[WARNING][Qt] 23.09.2024 23:49:47 [] (unknown:0) - External WM_DESTROY received for  QWidgetWindow(0x1c495a27fe0, name="qSlicerDataDialogWindow") , parent:  QWindow(0x0) , transient parent:  QWindow(0x0)
</code></pre>

---

## Post #6 by @muratmaga (2024-09-24 17:48 UTC)

<p>I haven’t seen anything out of ordinary, though there are a bunch of VTK warning. From here I cannot tell what might be causing the problem.</p>
<p>However, I noticed that you are using SlicerMorph customizations. One of our customization is to enable undo for pointList Markups, which works, but not extensively tested and perhaps have unintended consequences. I don’t think it has any effect, but you can try to disable the customizations and see if it helps.</p>
<p>As I understand the issues are happening when you are interacting with the cclosed curve on the model. Those are core Slicer features. It think if you can find a case it is happening consistently, and share us the data to replicate that can be the way forward for you.</p>

---

## Post #7 by @pieper (2024-09-24 17:54 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="6" data-topic="38519">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>enable undo for pointList Markups</p>
</blockquote>
</aside>
<p>This could definitely be an issue.</p>

---

## Post #8 by @Logan_Moore (2024-09-24 19:11 UTC)

<p>Yeah, I’ve tried everything to make it happen consistently. For example, in my error analysis, I landmarked the same elements repeatedly; sometimes, it would happen, and sometimes, it wouldn’t. So, I cannot even get it to occur consistently on the same elements. The most consistent thing about the error is that it only happens when placing landmarks in a closed curve, not in any other utility.</p>
<p>The only other thing that is fairly consistent is when reloading the data, oftentimes one of the landmarks for the curve that caused it will be way off the model in the middle of space.</p>
<p>Once I get it to happen again I can package up the files. I recently tried to boot Slicer from the generated associated scene and noticed it would crash consistently until the curve was adjusted. Hopefully when its in that state something will become more apparent.</p>

---

## Post #9 by @Logan_Moore (2024-09-24 19:30 UTC)

<p>Ironically enough, I was able to capture this on my very first element of the day: <a href="https://www.twitch.tv/videos/2259412662" class="inline-onebox" rel="noopener nofollow ugc">Twitch</a>. I was just placing landmarks; you can see it looks like I continue to move for the curve and it simply locked up. I also called up my task manager so you can see how it eats away at memory and then it just comes back.</p>

---

## Post #10 by @pieper (2024-09-24 19:34 UTC)

<p>Do try turning off the undo/redo option.  But if you can get this to replicate and share the data it would help.</p>

---

## Post #11 by @Logan_Moore (2024-09-24 19:47 UTC)

<p>I went into the customizations and set the undo module to false, I will let you know what happens.</p>

---

## Post #12 by @Logan_Moore (2024-09-29 19:51 UTC)

<p>Returning to this after a couple of days of data collection, after turning the undo module to false within the Slicermorph customizations, it seems to occur less frequently. I still haven’t been able to reproduce it consistently, which is frustrating, as I wish I could nail this down better. If I happen to notice any trends, I will flag them.</p>

---

## Post #13 by @lassoan (2024-09-29 21:43 UTC)

<p>When you are editing a closed curve and you enabled computing surface area then a complex algorithm is at every point move to create a triangulated surface inside (kind of like a soap bubble surface). This algorithm can fail or take a long time (several seconds, but maybe even more) if the curve is highly non-planar. Therefore, if you are not interested in surface area or your closed curve is not planar then I would recommend to diaable computation of surface area for your closed curvebon Markups module / Measurements section.</p>

---
