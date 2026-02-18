# 3D Slicer Paint/Draw Tool Issue 

**Topic ID**: 32531
**Date**: 2023-11-01
**URL**: https://discourse.slicer.org/t/3d-slicer-paint-draw-tool-issue/32531

---

## Post #1 by @Cameron_Shepherd (2023-11-01 20:12 UTC)

<p>Operating system: Windows 11<br>
Slicer version: 5.0.3<br>
Background:<br>
I am a undergraduate working within a research lab and I have been using 3D Slicer for about a year now. This issue is with the paint tool and has happened previously but a reset from the pc I work on would typically fix it, however that fix did not work. I use the paint/draw tool to create segments within a CT scan of cavefish brains and to ensure the segments are “right”, I am given the proper image spacing for each cluster of scanned individuals. After I ID the proper voxel size for xyz,  I place that within the image spacing tab as I was taught.</p>
<p>Expected behavior:<br>
Typical behavior for the paint tool would be to use circles as a “base” to trace/highlight certain sections I want within the CT scan and transform the highlighted area into a segment that is selected.</p>
<p>Actual behavior:<br>
Instead of the “base” use of a circle to trace/outline what I want on the CT scan, the tool is creating squares across the entire scan. This behavior is happening across multiple CT scans of the same individual and other individuals. I have also figured out the voxel spacing value, when placing within the image spacing within the volumes tab, can cause the issue to happen artificially.</p>
<p>I have attached screenshots and the log messages for today. I replicated the issue multiple times over and over.</p>
<p>Log Messages:<br>
[DEBUG][Qt] 01.11.2023 13:49:42 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Session start time …: 2023-11-01 13:49:42<br>
[DEBUG][Qt] 01.11.2023 13:49:42 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Slicer version …: 5.0.3 (revision 30893 / 7ea0f43) win-amd64 - installed release<br>
[DEBUG][Qt] 01.11.2023 13:49:42 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Operating system …: Windows /  Professional / (Build 22000, Code Page 65001) - 64-bit<br>
[DEBUG][Qt] 01.11.2023 13:49:42 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Memory …: 32559 MB physical, 37423 MB virtual<br>
[DEBUG][Qt] 01.11.2023 13:49:42 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - CPU …: GenuineIntel , 24 cores, 24 logical processors<br>
[DEBUG][Qt] 01.11.2023 13:49:42 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 01.11.2023 13:49:42 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Qt configuration …: version 5.15.2, with SSL, requested OpenGL 3.2 (compatibility profile)<br>
[DEBUG][Qt] 01.11.2023 13:49:42 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Internationalization …: disabled, language=<br>
[DEBUG][Qt] 01.11.2023 13:49:42 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Developer mode …: disabled<br>
[DEBUG][Qt] 01.11.2023 13:49:42 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Application path …: C:/Users/DLC/AppData/Local/NA-MIC/Slicer 5.0.3/bin<br>
[DEBUG][Qt] 01.11.2023 13:49:42 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Additional module paths …: NA-MIC/Extensions-30893/SegmentEditorExtraEffects/lib/Slicer-5.0/qt-loadable-modules, NA-MIC/Extensions-30893/SegmentEditorExtraEffects/lib/Slicer-5.0/qt-scripted-modules, NA-MIC/Extensions-30893/MarkupsToModel/lib/Slicer-5.0/qt-loadable-modules, NA-MIC/Extensions-30893/SlicerMorph/lib/Slicer-5.0/qt-scripted-modules<br>
[WARNING][Qt] 01.11.2023 13:49:46 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - libpng warning: iCCP: profile ‘ICC Profile’: ‘CMYK’: invalid ICC profile color space<br>
[WARNING][Qt] 01.11.2023 13:49:47 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - libpng warning: iCCP: known incorrect sRGB profile<br>
[DEBUG][Python] 01.11.2023 13:49:48 [Python] (C:\Users\DLC\AppData\Local\NA-MIC\Slicer 5.0.3\lib\Slicer-5.0\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 01.11.2023 13:49:49 [Python] (C:\Users\DLC\AppData\Local\NA-MIC\Slicer 5.0.3\lib\Slicer-5.0\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 01.11.2023 13:49:49 [Python] (C:\Users\DLC\AppData\Local\NA-MIC\Slicer 5.0.3\lib\Slicer-5.0\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Python] 01.11.2023 13:49:49 [Python] (C:\Users\DLC\AppData\Local\NA-MIC\Slicer 5.0.3\lib\Slicer-5.0\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: FormatMarkups<br>
[DEBUG][Qt] 01.11.2023 13:49:49 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “Welcome”<br>
[DEBUG][Qt] 01.11.2023 13:49:49 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Local filepath received via command-line:  “E:\DLC\Documents\Harvard\09212022\Contrast\Holtz_asty3_I [2022-10-11 18.43.06]\ZStacks\Crop\Row_4\72\Holtz_asty3_I_0276.jpg”<br>
[ERROR][VTK] 01.11.2023 13:49:50 [vtkITKArchetypeDiffusionTensorImageReaderFile (00000252B99ED3F0)] (D:\D\S\S-0\Libs\vtkITK\vtkITKArchetypeDiffusionTensorImageReaderFile.cxx:166) - There is more than one file, use the vtkITKArchetypeImageSeriesReader instead<br>
[INFO][VTK] 01.11.2023 13:49:50 [vtkMRMLVolumeArchetypeStorageNode (00000252B9D6C0B0)] (D:\D\S\S-0\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:513) - Loaded volume from file: E:/DLC/Documents/Harvard/09212022/Contrast/Holtz_asty3_I [2022-10-11 18.43.06]/ZStacks/Crop/Row_4/72/Holtz_asty3_I_0276.jpg. Dimensions: 419x389x229. Number of components: 3. Pixel type: unsigned char.<br>
[DEBUG][Qt] 01.11.2023 13:49:50 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - “Volume” Reader has successfully read the file “E:/DLC/Documents/Harvard/09212022/Contrast/Holtz_asty3_I [2022-10-11 18.43.06]/ZStacks/Crop/Row_4/72/Holtz_asty3_I_0276.jpg” “[1.03s]”<br>
[DEBUG][Qt] 01.11.2023 13:50:16 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “SegmentEditor”<br>
[WARNING][Qt] 01.11.2023 13:50:16 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - QLayout::addChildLayout: layout “” already has a parent<br>
[DEBUG][Qt] 01.11.2023 13:50:30 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “Volumes”<br>
[WARNING][Qt] 01.11.2023 13:50:30 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - ctkDoubleRangeSlider::setSingleStep( 0.0001 ) is outside of valid bounds.<br>
[DEBUG][Qt] 01.11.2023 13:50:45 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “SegmentEditor”<br>
[DEBUG][Qt] 01.11.2023 13:51:48 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “Volumes”<br>
[DEBUG][Qt] 01.11.2023 13:51:57 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “SegmentEditor”<br>
[DEBUG][Qt] 01.11.2023 13:52:17 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “Volumes”<br>
[DEBUG][Qt] 01.11.2023 13:52:29 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “SegmentEditor”<br>
[DEBUG][Qt] 01.11.2023 14:06:03 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “Volumes”<br>
[DEBUG][Qt] 01.11.2023 14:14:19 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “SegmentEditor”</p>
<hr>
<p>Screenshot of the Issue ~&gt;<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f9ed7a7eb24eb2c34156b02c5bfb502276bef83.png" data-download-href="/uploads/short-url/2ebtMqX91pz9Olc3LeenYK4gCCT.png?dl=1" title="Screenshot (1)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f9ed7a7eb24eb2c34156b02c5bfb502276bef83_2_690x389.png" alt="Screenshot (1)" data-base62-sha1="2ebtMqX91pz9Olc3LeenYK4gCCT" width="690" height="389" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f9ed7a7eb24eb2c34156b02c5bfb502276bef83_2_690x389.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f9ed7a7eb24eb2c34156b02c5bfb502276bef83_2_1035x583.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f9ed7a7eb24eb2c34156b02c5bfb502276bef83_2_1380x778.png 2x" data-dominant-color="34353B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (1)</span><span class="informations">1603×905 232 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Screenshot of Typical Behavior ~&gt;<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b2fba4261c7e4a16097a2e3fbdf2fac2915bf733.jpeg" data-download-href="/uploads/short-url/pxm7Y6jg2ZwzWQIBSeL5h6sJ3s7.jpeg?dl=1" title="Screenshot (2)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2fba4261c7e4a16097a2e3fbdf2fac2915bf733_2_690x388.jpeg" alt="Screenshot (2)" data-base62-sha1="pxm7Y6jg2ZwzWQIBSeL5h6sJ3s7" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2fba4261c7e4a16097a2e3fbdf2fac2915bf733_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2fba4261c7e4a16097a2e3fbdf2fac2915bf733_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2fba4261c7e4a16097a2e3fbdf2fac2915bf733_2_1380x776.jpeg 2x" data-dominant-color="34363B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (2)</span><span class="informations">1606×905 233 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>NOTE: I replicated what the draw tool should look like by making the image spacing 1 mm.</p>

---

## Post #2 by @lassoan (2023-11-01 20:16 UTC)

<p>Segmentation geometry (origin, spacing, axis directions, and extents) is determined <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#cannot-paint-outside-some-boundaries">from the geometry of the image that is selected first</a>. If you select a different image or change the image spacing, etc. then it will not affect the already created segmentation retrospectively. I would recommend to delete the segmentation and create a new one. That will be based on the new/updated image.</p>

---

## Post #3 by @Cameron_Shepherd (2023-11-03 12:08 UTC)

<p>Thank you for your response. It appears that has fixed the problem I was having.</p>

---
