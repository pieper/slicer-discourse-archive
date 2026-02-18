# VTK multi-volume ROI not working

**Topic ID**: 10000
**Date**: 2020-01-29
**URL**: https://discourse.slicer.org/t/vtk-multi-volume-roi-not-working/10000

---

## Post #1 by @fbordignon (2020-01-29 16:47 UTC)

<p>See image below.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b9ac5f9843e78320daebb01fc287c7f9e700d8b0.jpeg" data-download-href="/uploads/short-url/quxDHBxHjJycbVgDwZEywuHUhtS.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b9ac5f9843e78320daebb01fc287c7f9e700d8b0_2_690x402.jpeg" alt="image" data-base62-sha1="quxDHBxHjJycbVgDwZEywuHUhtS" width="690" height="402" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b9ac5f9843e78320daebb01fc287c7f9e700d8b0_2_690x402.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b9ac5f9843e78320daebb01fc287c7f9e700d8b0_2_1035x603.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b9ac5f9843e78320daebb01fc287c7f9e700d8b0_2_1380x804.jpeg 2x" data-dominant-color="8B8897"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1851×1080 300 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Also if I go from VTK multi-volume back to GPU ray casting, slicer crashes.</p>
<details>
<summary>
Error log</summary>
<p>[DEBUG][Qt] 29.01.2020 13:32:04 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Session start time …: 2020-01-29 13:32:04<br>
[DEBUG][Qt] 29.01.2020 13:32:04 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Slicer version …: 4.11.0-2020-01-20 (revision 28737) win-amd64 - installed release<br>
[DEBUG][Qt] 29.01.2020 13:32:04 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Operating system …: Windows /  Professional /  (Build 9200) - 64-bit<br>
[DEBUG][Qt] 29.01.2020 13:32:04 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Memory …: 130742 MB physical, 174630 MB virtual<br>
[DEBUG][Qt] 29.01.2020 13:32:04 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - CPU …: GenuineIntel , 12 cores, 12 logical processors<br>
[DEBUG][Qt] 29.01.2020 13:32:04 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 29.01.2020 13:32:04 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Qt configuration …: version 5.10.1, with SSL, requested OpenGL 3.2 (compatibility profile)<br>
[DEBUG][Qt] 29.01.2020 13:32:04 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 29.01.2020 13:32:04 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 29.01.2020 13:32:04 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Application path …: C:/Users/bordi/AppData/Local/NA-MIC/Slicer 4.11.0-2020-01-20/bin<br>
[DEBUG][Qt] 29.01.2020 13:32:04 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Additional module paths …: C:/Users/bordi/slicerltrace/Multicore, C:/Users/bordi/AppData/Roaming/NA-MIC/Extensions-28737/SegmentEditorExtraEffects/lib/Slicer-4.11/qt-scripted-modules<br>
[DEBUG][Python] 29.01.2020 13:32:07 [Python] (C:\Users\bordi\AppData\Local\NA-MIC\Slicer 4.11.0-2020-01-20\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 29.01.2020 13:32:07 [Python] (C:\Users\bordi\AppData\Local\NA-MIC\Slicer 4.11.0-2020-01-20\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 29.01.2020 13:32:07 [Python] (C:\Users\bordi\AppData\Local\NA-MIC\Slicer 4.11.0-2020-01-20\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 29.01.2020 13:32:08 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “Welcome”<br>
[INFO][VTK] 29.01.2020 13:32:16 [vtkMRMLVolumeArchetypeStorageNode (00000195E4B6D600)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:471) - Loaded volume from file: C:/Users/bordi/AppData/Local/Temp/Slicer/RemoteIO/MR-head.nrrd. Dimensions: 256x256x130. Number of components: 1. Pixel type: short.<br>
[DEBUG][Qt] 29.01.2020 13:32:16 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - “Volume” Reader has successfully read the file “C:/Users/bordi/AppData/Local/Temp/Slicer/RemoteIO/MR-head.nrrd” “[0.16s]”<br>
[DEBUG][Qt] 29.01.2020 13:32:23 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “VolumeRendering”<br>
[ERROR][VTK] 29.01.2020 13:33:01 [vtkShaderProgram (00000195F03AC460)] (D:\D\P\Slicer-0-build\VTK\Rendering\OpenGL2\vtkShaderProgram.cxx:461) - 1: <span class="hashtag">#version</span> 150</p>
<p>========A LOT OF CODE HERE========</p>
<p>[ERROR][VTK] 29.01.2020 13:33:03 [vtkShaderProgram (00000195E4292220)] (D:\D\P\Slicer-0-build\VTK\Rendering\OpenGL2\vtkShaderProgram.cxx:462) - 0(816) : error C7623: implicit narrowing of type from “vec4” to “float”<br>
0(816) : error C1103: too few parameters in function call<br>
0(815) : error C7623: implicit narrowing of type from “vec4” to “float”<br>
0(816) : error C1102: incompatible type for parameter <span class="hashtag">#2</span> (“colorTF.72”)<br>
0(815) : error C1035: assignment of incompatible types<br>
[ERROR][VTK] 29.01.2020 13:33:03 [vtkOpenGLGPUVolumeRayCastMapper (00000195E0FC9810)] (D:\D\P\Slicer-0-build\VTK\Rendering\VolumeOpenGL2\vtkOpenGLGPUVolumeRayCastMapper.cxx:2938) - Shader failed to compile</p>
</details>

---

## Post #2 by @lassoan (2020-01-29 16:48 UTC)

<p>Multi-volume rendering is still experimental. Shading and clipping are not supported yet.</p>

---

## Post #3 by @fbordignon (2020-01-29 17:05 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> indicated that we need to use the multi-volume if we need to display multiple volumes: <a href="https://discourse.slicer.org/t/display-incorrectly-when-two-volume-rendering-by3d-slicer-4-10-0/4669/2" class="inline-onebox">display incorrectly when two volume rendering  by3D slicer 4.10.0 - #2 by pieper</a></p>
<p>When I use the GPU ray-casting, I have the same isse as in <a href="https://discourse.slicer.org/t/display-incorrectly-when-two-volume-rendering-by3d-slicer-4-10-0/4669" class="inline-onebox">display incorrectly when two volume rendering  by3D slicer 4.10.0</a></p>
<p>The top head is always showing in foreground:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e9f78b4d27f5a352b4dbf9019474d6fda90f148a.png" alt="image" data-base62-sha1="xnLBUBWxmveXd9rwXgrqwvNknHQ" width="420" height="352"></p>

---

## Post #4 by @lassoan (2020-01-29 17:13 UTC)

<p>Multi-volume rendering will allow you to intermix multiple volumes correctly. However, until its limitations (shading, cropping, and maybe a few others that we are not aware yet) are addressed, you can use workarounds including using independent volume renderers (for highly transparent volumes they may provide acceptable quality), merging multiple volumes into a single volume, and/or using model and segmentation nodes for visualization.</p>
<p>I’ve added an issue to track resolving of mult-volume rendering limitations: <a href="https://issues.slicer.org/view.php?id=4719">https://issues.slicer.org/view.php?id=4719</a></p>

---

## Post #5 by @fbordignon (2020-01-29 17:40 UTC)

<p>Thank you, I think it would be a great improvement for Slicer. Great job.</p>

---

## Post #6 by @MissMac (2021-05-05 13:19 UTC)

<p>Hello,</p>
<p>I would like to reopen this question to ask if VTK multi-volume ROI works now with the latest VTK version.</p>

---
