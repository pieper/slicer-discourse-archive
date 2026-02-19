---
topic_id: 23067
title: "Mrml None Not Found"
date: 2022-04-21
url: https://discourse.slicer.org/t/23067
---

# MRML None not found

**Topic ID**: 23067
**Date**: 2022-04-21
**URL**: https://discourse.slicer.org/t/mrml-none-not-found/23067

---

## Post #1 by @jpdefrutos (2022-04-21 07:40 UTC)

<p>Hi!<br>
This issue is related to the SlicerLiver extension development (<a href="https://github.com/ALive-research/Slicer-Liver/issues/98" rel="noopener nofollow ugc">issue:</a>). We are having problems a MRML node creation in our extension, on Windows 10. The error message is as follows:</p>
<pre><code class="lang-auto">ASSERT failure in createNode: "Failed to create node of type [vtkMRMLLiverResectionNode]", file C:\S\Slicer\Libs\MRML\Widgets\qMRMLNodeFactory.cxx, line 74
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/034bda5dfc5ee0333e2677115b5543229c00615d.png" data-download-href="/uploads/short-url/t9WH8NQtRao6MO9iosq6fKgK6N.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/034bda5dfc5ee0333e2677115b5543229c00615d_2_690x369.png" alt="image" data-base62-sha1="t9WH8NQtRao6MO9iosq6fKgK6N" width="690" height="369" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/034bda5dfc5ee0333e2677115b5543229c00615d_2_690x369.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/034bda5dfc5ee0333e2677115b5543229c00615d_2_1035x553.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/034bda5dfc5ee0333e2677115b5543229c00615d_2_1380x738.png 2x" data-dominant-color="CCCBDF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1029 274 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I’m compiling Slicer v. 4.13.0 (debug) on VS Community 2022. On Windows 10 (v. 21H1 (build 19043.1466)). I tried using the VS debugger, but because the extension objects do not show up in the object list, I can’t track where is this error triggered within the extension.<br>
I can get when the CreateNodeByClass() (qMRMLNodeFactory.cxx L:74) method is called, just before the error.<br>
Any guidance on why the node is not created would be of great help!<br>
<a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a></p>

---

## Post #2 by @lassoan (2022-04-23 05:02 UTC)

<p>Your custom <code>vtkMRMLLiverResectionNode</code> is <a href="https://github.com/ALive-research/Slicer-Liver/blob/02e7f8a180fb19534d94e4ecb58c948a085af60f/LiverResections/Logic/vtkSlicerLiverResectionsLogic.cxx#L100">registered in LiverResections module logic</a>, so if that module is successfully loaded and initialized then the instantiation of the node will succeed. Make sure you <a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#test-an-extension">add the folder that contains your module DLLs to additional module paths</a>.</p>

---

## Post #3 by @jpdefrutos (2022-04-24 12:11 UTC)

<p>Thank you very much <a class="mention" href="/u/lassoan">@lassoan</a>. I’ll look into it!</p>

---

## Post #4 by @jpdefrutos (2022-05-20 17:54 UTC)

<p>Indeed, the extension is not loaded properly.<br>
I tried debugging the extension following the docs (<a href="https://slicer.readthedocs.io/en/latest/developer_guide/debugging/windowscpp.html" class="inline-onebox" rel="noopener nofollow ugc">C++ debugging on Windows — 3D Slicer documentation</a>), but the only thing I got so far is that no symbols are loaded for SlicerLiverResectionModule (where the error is triggered).<br>
The libraries are created and stored as expected in “qt-loadable-modules”, and this directory is added to the “Additional modules path”. Also there is no DLL error event recorded in the Event Viewer either, so I guess Slicer is not even attempting to load the module, only the scripted one. I tried using Dependency Walker, though with little success as no log related to the SlicerLiverResectionModule is logged.</p>
<p>When debugging, I see no log regarding the loading of symbols related to additional extension in the Output. Is there a way of logging this information?</p>

---

## Post #5 by @lassoan (2022-05-21 03:29 UTC)

<p>You need to add the path to additional module paths that contain the module files. It is not <code>...\lib\Slicer-5.1\qt-loadable-modules</code> but ``…\lib\Slicer-5.1\qt-loadable-modules\Debug`.</p>

---

## Post #6 by @jpdefrutos (2022-05-22 13:06 UTC)

<p>Thank you very much for your help. You are right, the path to the loadable module was wrong.</p>
<p>After pointing to the right path (<code>...qt-loadable-mdoules\Debug</code>), the error is still triggered though. Here is an excerpt of the log when I try to create a <code>VTK MRML Liver Resection Node</code>:</p>
<pre><code class="lang-auto">[DEBUG][Qt] 22.05.2022 14:54:29 [] (unknown:0) - Session start time .......: 2022-05-22 14:54:29
[DEBUG][Qt] 22.05.2022 14:54:29 [] (unknown:0) - Slicer version ...........: 5.1.0-2022-05-19 (revision 30956 / ba34656) win-amd64 - not installed debug
[DEBUG][Qt] 22.05.2022 14:54:29 [] (unknown:0) - Operating system .........: Windows /  Professional / (Build 19043, Code Page 65001) - 64-bit
[DEBUG][Qt] 22.05.2022 14:54:29 [] (unknown:0) - Memory ...................: 32540 MB physical, 49948 MB virtual
[DEBUG][Qt] 22.05.2022 14:54:29 [] (unknown:0) - CPU ......................: GenuineIntel , 12 cores, 12 logical processors
[DEBUG][Qt] 22.05.2022 14:54:29 [] (unknown:0) - VTK configuration ........: OpenGL2 rendering, TBB threading
[DEBUG][Qt] 22.05.2022 14:54:29 [] (unknown:0) - Qt configuration .........: version 5.15.2, with SSL, requested OpenGL 3.2 (compatibility profile)
[DEBUG][Qt] 22.05.2022 14:54:29 [] (unknown:0) - Internationalization .....: disabled, language=
[DEBUG][Qt] 22.05.2022 14:54:29 [] (unknown:0) - Developer mode ...........: enabled
[DEBUG][Qt] 22.05.2022 14:54:29 [] (unknown:0) - Application path .........: C:/S/SD/Slicer-build/bin/Debug
[DEBUG][Qt] 22.05.2022 14:54:29 [] (unknown:0) - Additional module paths ..: C:/S/VMTK_build/inner-build/lib/Slicer-5.1/Debug, C:/S/DebTools/lib/Slicer-5.1/qt-scripted-modules, C:/S/VMTK_build/inner-build/lib/Slicer-5.1/qt-scripted-modules, C:/S/SL_debug/lib/Slicer-5.1/qt-loadable-modules/Debug, C:/S/SL_debug/lib/Slicer-5.1/qt-scripted-modules
[DEBUG][Python] 22.05.2022 14:54:39 [Python] (C:\S\SD\Slicer-build\lib\Slicer-5.1\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: Annotations
[WARNING][Qt] 22.05.2022 14:54:41 [] (unknown:0) - When loading module  "CurveCenterlineExtraction" , the dependency "SegmentEditorDrawTube" failed to be loaded.
[WARNING][Qt] 22.05.2022 14:54:41 [] (unknown:0) - When loading module  "FiducialCenterlineExtraction" , the dependency "SegmentEditorFloodFilling" failed to be loaded.
[DEBUG][Python] 22.05.2022 14:54:42 [Python] (C:\S\SD\Slicer-build\lib\Slicer-5.1\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 22.05.2022 14:54:42 [Python] (C:\S\SD\Slicer-build\lib\Slicer-5.1\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Qt] 22.05.2022 14:54:43 [] (unknown:0) - Switch to module:  "Welcome"
[INFO][VTK] 22.05.2022 14:54:44 [vtkMRMLVolumeArchetypeStorageNode (0000020CC3DD5240)] (C:\S\S_src\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:513) - Loaded volume from file: C:/S/VMTK_build/inner-build/lib/Slicer-5.1/qt-scripted-modules/Resources/Vesselness.png. Dimensions: 65x50x1. Number of components: 3. Pixel type: unsigned char.
[DEBUG][Qt] 22.05.2022 14:55:10 [] (unknown:0) - Switch to module:  "Liver"
[FATAL][Qt] 22.05.2022 14:55:13 [] (unknown:0) - ASSERT failure in createNode: "Failed to create node of type [vtkMRMLLiverResectionNode]", file C:\S\S_src\Libs\MRML\Widgets\qMRMLNodeFactory.cxx, line 74
[WARNING][Qt] 22.05.2022 14:55:16 [] (unknown:0) - qMRMLNodeComboBox::addNode() failed with node type vtkMRMLLiverResectionNode
</code></pre>
<p>What puzzles me the most is not getting a fail to load module message, if in fact the module couldn’t be loaded.</p>

---

## Post #7 by @lassoan (2022-05-23 02:43 UTC)

<p>I’ve built <code>Slicer-Liver</code> in debug mode on Windows and then launched Slicer by executing <code>SlicerWithSlicerLiver.exe</code> and I had no problem with instantiating <code>vtkMRMLLiverResectionNode</code> in the Python console:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLiverResectionNode')
&lt;vtkSlicerLiverResectionsModuleMRML.vtkMRMLLiverResectionNode(0x00000279CDC48380) at 0x00000279D4B9B220&gt;
&gt;&gt;&gt;
</code></pre>
<p>I then started Slicer normally (using Slicer.exe) and added <code>c:\D\Slicer-Liver_D\lib\Slicer-5.1\qt-loadable-modules\Debug</code> to the additional module paths in application settings, restarted Slicer, and again I did not get any error and <code>vtkMRMLLiverResectionNode</code> was instantiated without issues.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/8420e0489628229f3050a1545d5ba7eb8e76262a.png" data-download-href="/uploads/short-url/iQRsH8wit6fOQkLylWGLNvNoTcS.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8420e0489628229f3050a1545d5ba7eb8e76262a_2_690x420.png" alt="image" data-base62-sha1="iQRsH8wit6fOQkLylWGLNvNoTcS" width="690" height="420" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8420e0489628229f3050a1545d5ba7eb8e76262a_2_690x420.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8420e0489628229f3050a1545d5ba7eb8e76262a_2_1035x630.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8420e0489628229f3050a1545d5ba7eb8e76262a_2_1380x840.png 2x" data-dominant-color="383839"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1373 288 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>So there is nothing wrong with the source code, everything works fine on my computer. There is something wrong with your configuration. You can try to find out what exactly does not work by running Slicer in a debugger and placing breakpoints in the code (e.g., where you register and use the <code>vtkMRMLLiverResectionNode</code> class).</p>

---

## Post #8 by @jpdefrutos (2022-05-23 05:39 UTC)

<p>Glad to hear that the extension can run on Windows!<br>
Thank you very much for your help! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"><br>
I’ll keep debugging it then</p>

---
