---
topic_id: 10243
title: "Triangulating A Surface Mesh"
date: 2020-02-13
url: https://discourse.slicer.org/t/10243
---

# Triangulating a Surface Mesh

**Topic ID**: 10243
**Date**: 2020-02-13
**URL**: https://discourse.slicer.org/t/triangulating-a-surface-mesh/10243

---

## Post #1 by @ChristopherWaters (2020-02-13 13:49 UTC)

<p><strong>Goal:</strong></p>
<ul>
<li>Triangulate a Surface Mesh (vtk unstructured grid) for FEM</li>
</ul>
<p><strong>Approach:</strong></p>
<ul>
<li>Load .vtk surface mesh in 3DSlicer</li>
<li>Convert Model to Segmentation Node</li>
<li>Use Segment Mesher + Cleaver Extension to create volumetric mesh</li>
<li>Triangulate further with Cleaver</li>
<li>Export as .vtk</li>
</ul>
<p><strong>Difficulties:</strong></p>
<ul>
<li>
<p>I right-click my imported .vtk surface mesh node and select “Convert Model to Segmentation Node”. A segmentation node is then created within the subject hierarchy.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/863bc90405933ab30599717f9a64473193dd3aa3.png" data-download-href="/uploads/short-url/j9u4m9fXyXrfPLGKr6lwkgcnOZd.png?dl=1" title="cap1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/863bc90405933ab30599717f9a64473193dd3aa3_2_690x206.png" alt="cap1" data-base62-sha1="j9u4m9fXyXrfPLGKr6lwkgcnOZd" width="690" height="206" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/863bc90405933ab30599717f9a64473193dd3aa3_2_690x206.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/863bc90405933ab30599717f9a64473193dd3aa3.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/863bc90405933ab30599717f9a64473193dd3aa3.png 2x" data-dominant-color="6C7088"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">cap1</span><span class="informations">938×281 11.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>I then go into Segment Mesher and have my segmentation node selected as the Input Segmentation, and Cleaver as the Meshing Method. When I click Apply an error occurs.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/2648c7f172322206119ae0789574b6ff731ebb26.png" alt="cap2" data-base62-sha1="5sG4K6x093eD0RJaJgtQ381WqEe" width="494" height="356"><br>
<strong>Questions:</strong></p>
</li>
<li>
<p>Did I forget any steps between converting my model to segmentation node and using Segment Mesher? Within the segmentation editor I see empty segmentation</p>
</li>
</ul>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/834b1b1a77e1e1a9cc9baca2a31deb7b59e8480b.png" alt="asdasd" data-base62-sha1="iJtsELGfVaNYlcHtk5YLqh5i4dR" width="574" height="225"></p>
<p>So I then clicked Segmentations and then Add Segment to create this, selecting Closed Surface and Fractional Labelmap:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f7c2d59252cf3349b264825d546f25a1b33c3ae0.png" data-download-href="/uploads/short-url/zlNmFHhEwf5JBpqPy4VqFMUyqfC.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f7c2d59252cf3349b264825d546f25a1b33c3ae0_2_690x410.png" alt="image" data-base62-sha1="zlNmFHhEwf5JBpqPy4VqFMUyqfC" width="690" height="410" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f7c2d59252cf3349b264825d546f25a1b33c3ae0_2_690x410.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f7c2d59252cf3349b264825d546f25a1b33c3ae0.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f7c2d59252cf3349b264825d546f25a1b33c3ae0.png 2x" data-dominant-color="626474"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">967×575 25 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I am just confused if I can segment before creating a volumetric mesh, and I never see any segmentations show up in my render(not sure if they are supposed to)…</p>

---

## Post #2 by @lassoan (2020-02-13 13:49 UTC)

<p>Thanks for reporting this. Which Slicer version did you use? Could you try with latest Slicer Preview Release?</p>

---

## Post #3 by @ChristopherWaters (2020-02-14 02:28 UTC)

<p>This is in version 4.10.2</p>
<p>So this is not an error on my part (this is my first time using Slicer)?<br>
(Also some additional info that might be helpful: that .vtk model is literally just a vtk Tetrahedron)</p>

---

## Post #4 by @ChristopherWaters (2020-02-15 08:54 UTC)

<p>I have now also tried Preview 4.11.0 and have exactly the same issue. No segments are visible at all.</p>
<p>If there is anything else I can do to solve this please let me know.</p>

---

## Post #5 by @lassoan (2020-02-15 18:44 UTC)

<p>I’ve tested this with latest Slicer Preview Release and it worked well. Probably the issue is how you define the segmentation geometry (origin, spacing, axis directions, and extents of the grid where the model is sampled on). Normally you start from the image and then segmentation geometry is already defined, but if you load a model then some generic geometry is created by default, which may not be ideal for meshing, because its extents just as large as the input model and for meshing it is good to have some margin at the boundaries.</p>
<p>First, I would recommend to follow steps of the <a href="https://github.com/lassoan/SlicerSegmentMesher#tutorial">tutorial</a> to confirm that there are no software issues.</p>
<p>If everything works well the tutorial data then try with your data: load the model as segmentation, define an ROI node (available on the toolbar) that is slightly larger than your model, and use that to define segment geometry (button next to master volume selector in Segment Editor module). If any step is not clear then let me know and I’ll add a few screenshots to make it more clear. You can also upload your model to dropbox/onedrive and post the link here so that I can show how that particular object can be meshed.</p>

---

## Post #6 by @ChristopherWaters (2020-02-17 01:57 UTC)

<p>Thank you for the response, it has helped me get a couple of steps closer.</p>
<p>Here is what I see after I load the model, convert to segmentation, create ROI node, and then use the ROI to define the segment geo (it is now generating a master volume, though Slicer says that the volume is out of frame in the bottom views):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/77944f7ab166a71478ba74923319d7d2048e79b6.png" data-download-href="/uploads/short-url/h3QzvqkW9kPAFu9wLmC5h3hJ5Q2.png?dl=1" title="cap1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/77944f7ab166a71478ba74923319d7d2048e79b6_2_690x410.png" alt="cap1" data-base62-sha1="h3QzvqkW9kPAFu9wLmC5h3hJ5Q2" width="690" height="410" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/77944f7ab166a71478ba74923319d7d2048e79b6_2_690x410.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/77944f7ab166a71478ba74923319d7d2048e79b6_2_1035x615.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/77944f7ab166a71478ba74923319d7d2048e79b6_2_1380x820.png 2x" data-dominant-color="50505F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">cap1</span><span class="informations">1757×1046 61.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>When I then run Segment Mesher on the segmentation I get the same error as before, but a Label Map Volume is created (when I enable view of it nothing seems to show up except its name in the bottom views):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c0801d138c46d1e291442a14346c1f6841d381ec.png" data-download-href="/uploads/short-url/rsW9HdyQkX1059LiVwwJIGFu4sQ.png?dl=1" title="cap2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c0801d138c46d1e291442a14346c1f6841d381ec_2_690x399.png" alt="cap2" data-base62-sha1="rsW9HdyQkX1059LiVwwJIGFu4sQ" width="690" height="399" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c0801d138c46d1e291442a14346c1f6841d381ec_2_690x399.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c0801d138c46d1e291442a14346c1f6841d381ec_2_1035x598.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c0801d138c46d1e291442a14346c1f6841d381ec_2_1380x798.png 2x" data-dominant-color="505161"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">cap2</span><span class="informations">1724×999 63.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Ignoring Segment Mesher and going straight to using Cleaver Test Mesher extensions, I can run the mesher on my segmentation master volume without error but nothing seems to change at all…</p>
<p>(At one point I was able to get the sides of the cube to render in the bottom views but I cannot recreate it again)</p>
<p>I would appreciate any form of clarification of the steps to go from a simple model(surface mesh) to Cleaver’s output.</p>

---

## Post #7 by @lassoan (2020-02-17 06:32 UTC)

<p>I’ve updated the extension so that padding can be automatically added (you don’t need to create a ROI) and made creation of internal labelmap representation more robust. With the update extension you should be able to just load the mesh file as segmentation then go to Segment Mesher module, select an output model, and click Apply.</p>
<p>The updated extension will be available in the Extension manager from Tuesday or you can update <code>SegmentMesher.py</code> file in your installed extension with the <a href="https://github.com/lassoan/SlicerSegmentMesher/blob/master/SegmentMesher/SegmentMesher.py">new version</a>.</p>

---

## Post #8 by @ChristopherWaters (2020-02-17 08:54 UTC)

<p>Thank you so much for taking the time to update the extension, but unfortunately I get the same error as before.</p>
<p><strong>How I Updated:</strong></p>
<pre><code class="lang-auto">C:\Users\MyName\AppData\Roaming\NA-MIC\Extensions-28257\SegmentMesher\lib\Slicer-4.10\qt-scripted-modules
</code></pre>
<p>to update <code>SegmentMesher.py</code>. (note: this is the extension folder for my current Slicer version, I deleted the one that was for my preview build I had yesterday)</p>
<p>I have also tried:</p>
<ul>
<li>Deleting the compiled .pyc file right after updating the .py (having Slicer generate an updated .pyc at run-time)</li>
<li>Completely  reinstalling the extension then updating it once again</li>
</ul>
<p>Let me know if there are any other small details that will help clarify the issue.</p>

---

## Post #9 by @lassoan (2020-02-17 14:05 UTC)

<p>Have you downloaded the file from github - <a href="https://github.com/lassoan/SlicerSegmentMesher/blob/master/SegmentMesher/SegmentMesher.py">https://github.com/lassoan/SlicerSegmentMesher/blob/master/SegmentMesher/SegmentMesher.py</a>? Do you have <code>self.addLog('Failed to create binary labelmap representation')</code> in line 512?</p>

---

## Post #10 by @ChristopherWaters (2020-02-18 01:31 UTC)

<p>My file does contain the proper 512. I was just copying the raw code over before, but now I have actually replaced the file and the error persists:</p>
<pre><code class="lang-auto">Mesh generation using Cleaver is started in working directory: C:/Users/MeName/AppData/Local/Temp/Slicer/SegmentMesher/20200218_102026_202
Error: 'NoneType' object has no attribute 'GetColorNode'
</code></pre>
<p>I have quadruple checked everything as well. I load in the .vtk as a Model, create the segmentation node, and then run Segment Mesher on the seg node (selecting my model as the output model and cleaver as the method (I also have cleaver extension installed)).</p>

---

## Post #11 by @lassoan (2020-02-18 01:40 UTC)

<p>Could you attach the log file? (I’m particularly interested in which line number the error occurs and also what additional module paths are defined)</p>
<p>“Error: ‘NoneType’ object has no attribute ‘GetColorNode’” error is used to be logged when for some reason export of segmentation to labelmap failed. But now that error is detected before, in line 512, so I suspect that there may be two versions of the same module included in the “additional module paths”.</p>
<p>If that’s not the issue then maybe it is something related to the input mesh. For that, it would be great if you could test with some other data set (for example, I’ve tested with this <a href="https://1drv.ms/u/s!Arm_AFxB9yqHurgQU3DpNbfsZDsUHA?e=yrlapP">prostate gland STL file</a>) and report what you find.</p>

---

## Post #12 by @ChristopherWaters (2020-02-18 01:49 UTC)

<p>Here is the full error log, I was unaware that it showed more than the small console within the extension’s gui. (your link seems to be a file path from your computer, and does not work)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5eb7a22a73b5842ed32cb9ae0e62370f6582bb93.png" data-download-href="/uploads/short-url/dvUjxehmiw3nTMwwIf9sYgtiM6v.png?dl=1" title="ErrorLog" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5eb7a22a73b5842ed32cb9ae0e62370f6582bb93.png" alt="ErrorLog" data-base62-sha1="dvUjxehmiw3nTMwwIf9sYgtiM6v" width="690" height="295" data-dominant-color="565650"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ErrorLog</span><span class="informations">1125×481 22.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I guess this means that my model is causing an issue, but as I stated before it is simply a large cube from vtk that I write to a .vtk file using <code>vtkUnstructuredGridWriter</code>.</p>

---

## Post #13 by @lassoan (2020-02-18 01:53 UTC)

<aside class="quote no-group" data-username="ChristopherWaters" data-post="12" data-topic="10243">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/d78d45/48.png" class="avatar"> ChristopherWaters:</div>
<blockquote>
<p>your link seems to be a file path from your computer, and does not work</p>
</blockquote>
</aside>
<p>Sorry, fixed.</p>
<aside class="quote no-group" data-username="ChristopherWaters" data-post="12" data-topic="10243">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/d78d45/48.png" class="avatar"> ChristopherWaters:</div>
<blockquote>
<p>Here is the full error log</p>
</blockquote>
</aside>
<p>Only a tiny fraction of the full log is visible in the screenshot. Please use menu: Help / Report a bug to get log as text. If it’s too long then upload the text to somewhere and post the link here. Thank you!</p>
<p>I see that much as "Failed to import model ‘testCube’ to segmentation. So, the segmentation is probably empty, which explain why do you have this error. Is testCube a surface mesh (vtkPolyData) or already a volumetric mesh (vtkUnstructuredGrid)? It should be a vtkPolyData. We could easily get a surface mesh from a volumetric mesh (just need to apply vtkGeometryFilter), but this has never come up before.</p>

---

## Post #14 by @ChristopherWaters (2020-02-18 02:02 UTC)

<p>I have now also tried the prostate model, but it too causes an error. One big difference between it and my model is that right when I create the segmentation node it automaticaly creates a segmentation within the node; my model did not do this…</p>
<hr>
<p><strong>Here is the log from my model:</strong></p>
<p>[DEBUG][Qt] 18.02.2020 10:51:29 [] (unknown:0) - Session start time …: 2020-02-18 10:51:29<br>
[DEBUG][Qt] 18.02.2020 10:51:29 [] (unknown:0) - Slicer version …: 4.10.2 (revision 28257) win-amd64 - installed release<br>
[DEBUG][Qt] 18.02.2020 10:51:29 [] (unknown:0) - Operating system …: Windows /  Personal /  (Build 9200) - 64-bit<br>
[DEBUG][Qt] 18.02.2020 10:51:29 [] (unknown:0) - Memory …: 16119 MB physical, 18551 MB virtual<br>
[DEBUG][Qt] 18.02.2020 10:51:29 [] (unknown:0) - CPU …: GenuineIntel , 12 cores, 12 logical processors<br>
[DEBUG][Qt] 18.02.2020 10:51:29 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 18.02.2020 10:51:29 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 18.02.2020 10:51:29 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 18.02.2020 10:51:29 [] (unknown:0) - Additional module paths …: C:/Users/thefl/AppData/Roaming/NA-MIC/Extensions-28257/CleaverExtension/lib/Slicer-4.10/cli-modules, C:/Users/thefl/AppData/Roaming/NA-MIC/Extensions-28257/SegmentMesher/lib/Slicer-4.10/qt-scripted-modules<br>
[DEBUG][Python] 18.02.2020 10:51:30 [Python] (C:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 18.02.2020 10:51:31 [Python] (C:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 18.02.2020 10:51:31 [Python] (C:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 18.02.2020 10:51:31 [] (unknown:0) - Switch to module:  “Data”<br>
[DEBUG][Qt] 18.02.2020 10:52:04 [] (unknown:0) - “Model” Reader has successfully read the file “C:/Users/thefl/Downloads/testCube.vtk” “[0.00s]”<br>
[ERROR][VTK] 18.02.2020 10:52:09 [vtkMRMLSegmentationNode (000001FFF5205210)] (D:\D\S\Slicer-4102\Modules\Loadable\Segmentations\Logic\vtkSlicerSegmentationsModuleLogic.cxx:1171) - ImportModelToSegmentationNode: Invalid model node<br>
[CRITICAL][Qt] 18.02.2020 10:52:09 [] (unknown:0) - void __cdecl qSlicerSubjectHierarchySegmentationsPlugin::convertModelToSegmentation(void) : Failed to import model ’ testCube ’ to segmentation ’ testCube-segmentation ’<br>
[DEBUG][Qt] 18.02.2020 10:52:12 [] (unknown:0) - Switch to module:  “SegmentMesher”<br>
[INFO][Python] 18.02.2020 10:52:13 [Python] (C:/Users/thefl/AppData/Roaming/NA-MIC/Extensions-28257/SegmentMesher/lib/Slicer-4.10/qt-scripted-modules/SegmentMesher.py:361) - Mesh generation using Cleaver is started in working directory: C:/Users/thefl/AppData/Local/Temp/Slicer/SegmentMesher/20200218_105213_730<br>
[INFO][Stream] 18.02.2020 10:52:13 [] (unknown:0) - CLEAVER<br>
[INFO][Stream] 18.02.2020 10:52:13 [] (unknown:0) - Mesh generation using Cleaver is started in working directory: C:/Users/thefl/AppData/Local/Temp/Slicer/SegmentMesher/20200218_105213_730<br>
[ERROR][VTK] 18.02.2020 10:52:13 [vtkOrientedImageData (000001FFF51417E0)] (D:\D\S\Slicer-4102\Libs\vtkSegmentationCore\vtkSegmentationConverter.cxx:214) - DeserializeImageGeometry: Failed to de-serialize geometry string<br>
[ERROR][VTK] 18.02.2020 10:52:13 [vtkMRMLSegmentationNode (000001FFF5205210)] (D:\D\S\Slicer-4102\Libs\MRML\Core\vtkMRMLSegmentationNode.cxx:527) - GenerateMergedLabelmap: Segmentation does not contain binary labelmap representation<br>
[ERROR][VTK] 18.02.2020 10:52:13 [vtkMRMLSegmentationNode (000001FFF5205210)] (D:\D\S\Slicer-4102\Modules\Loadable\Segmentations\Logic\vtkSlicerSegmentationsModuleLogic.cxx:1021) - ExportSegmentsToLabelmapNode: Failed to generate merged labelmap<br>
[WARNING][VTK] 18.02.2020 10:52:13 [] (unknown:0) - Generic Warning: In D:\D\S\Slicer-4102\Libs\MRML\Core\vtkDataFileFormatHelper.cxx, line 237<br>
vtkDataFileFormatHelper::GetFileExtensionFromFormatString: please update deprecated extension-only format specifier to ‘File format name (.ext)’ format! Current format string: .nrrd<br>
[ERROR][VTK] 18.02.2020 10:52:13 [vtkITKImageWriter (000001FFF4E805E0)] (D:\D\S\Slicer-4102\Libs\vtkITK\vtkITKImageWriter.cxx:514) - Can only export 1 or 3 component images, current image has 0 components<br>
[ERROR][VTK] 18.02.2020 10:52:13 [vtkMRMLVolumeArchetypeStorageNode (000001FFF2F28CA0)] (D:\D\S\Slicer-4102\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:866) - UpdateFileList: the archetype file ‘inputLabelmap.nrrd’ wasn’t written out when writing ‘C:/Users/thefl/AppData/Local/Temp/Slicer/SegmentMesher/20200218_105213_730/TempWriteinputLabelmap/inputLabelmap.nrrd’ in ‘C:/Users/thefl/AppData/Local/Temp/Slicer/SegmentMesher/20200218_105213_730/TempWriteinputLabelmap’. Only those 0 file(s) have been written: . Old name is ‘C:/Users/thefl/AppData/Local/Temp/Slicer/SegmentMesher/20200218_105213_730\inputLabelmap.nrrd’.<br>
[WARNING][VTK] 18.02.2020 10:52:13 [] (unknown:0) - Generic Warning: In D:\D\S\Slicer-4102\Libs\MRML\Core\vtkDataFileFormatHelper.cxx, line 237<br>
vtkDataFileFormatHelper::GetFileExtensionFromFormatString: please update deprecated extension-only format specifier to ‘File format name (.ext)’ format! Current format string: .nrrd<br>
[ERROR][VTK] 18.02.2020 10:52:13 [vtkITKImageWriter (000001FFF4E80ED0)] (D:\D\S\Slicer-4102\Libs\vtkITK\vtkITKImageWriter.cxx:514) - Can only export 1 or 3 component images, current image has 0 components<br>
[INFO][Stream] 18.02.2020 10:52:13 [] (unknown:0) - ‘NoneType’ object has no attribute ‘GetColorNode’<br>
[CRITICAL][Stream] 18.02.2020 10:52:13 [] (unknown:0) - Traceback (most recent call last):<br>
[CRITICAL][Stream] 18.02.2020 10:52:13 [] (unknown:0) -   File “C:/Users/thefl/AppData/Roaming/NA-MIC/Extensions-28257/SegmentMesher/lib/Slicer-4.10/qt-scripted-modules/SegmentMesher.py”, line 296, in onApplyButton<br>
[CRITICAL][Stream] 18.02.2020 10:52:13 [] (unknown:0) -     self.cleaverPaddingPercentSpinBox.value * 0.01)<br>
[CRITICAL][Stream] 18.02.2020 10:52:13 [] (unknown:0) -   File “C:/Users/thefl/AppData/Roaming/NA-MIC/Extensions-28257/SegmentMesher/lib/Slicer-4.10/qt-scripted-modules/SegmentMesher.py”, line 548, in createMeshFromSegmentationCleaver<br>
[CRITICAL][Stream] 18.02.2020 10:52:13 [] (unknown:0) -     colorTableNode = labelmapVolumeNode.GetDisplayNode().GetColorNode()<br>
[CRITICAL][Stream] 18.02.2020 10:52:13 [] (unknown:0) - AttributeError: ‘NoneType’ object has no attribute ‘GetColorNode’</p>
<hr>
<p><strong>Here is the prostate model’s log:</strong></p>
<p>[DEBUG][Qt] 18.02.2020 10:55:15 [] (unknown:0) - Session start time …: 2020-02-18 10:55:15<br>
[DEBUG][Qt] 18.02.2020 10:55:15 [] (unknown:0) - Slicer version …: 4.10.2 (revision 28257) win-amd64 - installed release<br>
[DEBUG][Qt] 18.02.2020 10:55:15 [] (unknown:0) - Operating system …: Windows /  Personal /  (Build 9200) - 64-bit<br>
[DEBUG][Qt] 18.02.2020 10:55:15 [] (unknown:0) - Memory …: 16119 MB physical, 18551 MB virtual<br>
[DEBUG][Qt] 18.02.2020 10:55:15 [] (unknown:0) - CPU …: GenuineIntel , 12 cores, 12 logical processors<br>
[DEBUG][Qt] 18.02.2020 10:55:15 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 18.02.2020 10:55:15 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 18.02.2020 10:55:15 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 18.02.2020 10:55:15 [] (unknown:0) - Additional module paths …: C:/Users/thefl/AppData/Roaming/NA-MIC/Extensions-28257/CleaverExtension/lib/Slicer-4.10/cli-modules, C:/Users/thefl/AppData/Roaming/NA-MIC/Extensions-28257/SegmentMesher/lib/Slicer-4.10/qt-scripted-modules<br>
[DEBUG][Python] 18.02.2020 10:55:17 [Python] (C:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 18.02.2020 10:55:17 [Python] (C:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 18.02.2020 10:55:17 [Python] (C:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 18.02.2020 10:55:17 [] (unknown:0) - Switch to module:  “Data”<br>
[DEBUG][Qt] 18.02.2020 10:55:29 [] (unknown:0) - “Model” Reader has successfully read the file “C:/Users/thefl/Downloads/ProstateMeanShape2.stl” “[0.07s]”<br>
[INFO][VTK] 18.02.2020 10:55:31 [vtkClosedSurfaceToBinaryLabelmapConversionRule (00000279C06AAB10)] (D:\D\S\Slicer-4102\Libs\vtkSegmentationCore\vtkClosedSurfaceToBinaryLabelmapConversionRule.cxx:251) - CalculateOutputGeometry: No image geometry specified, default geometry is calculated (0.165357492443735;0;0;41.1088981628418;0;0.165357492443735;0;52.828800201416;0;0;0.165357492443735;18.8999996185303;0;0;0;1;0;322;0;221;0;219;)<br>
[DEBUG][Qt] 18.02.2020 10:55:41 [] (unknown:0) - Switch to module:  “SegmentMesher”<br>
[INFO][Python] 18.02.2020 10:55:48 [Python] (C:/Users/thefl/AppData/Roaming/NA-MIC/Extensions-28257/SegmentMesher/lib/Slicer-4.10/qt-scripted-modules/SegmentMesher.py:361) - Mesh generation using Cleaver is started in working directory: C:/Users/thefl/AppData/Local/Temp/Slicer/SegmentMesher/20200218_105548_245<br>
[INFO][Stream] 18.02.2020 10:55:48 [] (unknown:0) - CLEAVER<br>
[INFO][Stream] 18.02.2020 10:55:48 [] (unknown:0) - Mesh generation using Cleaver is started in working directory: C:/Users/thefl/AppData/Local/Temp/Slicer/SegmentMesher/20200218_105548_245<br>
[DEBUG][Python] 18.02.2020 10:55:48 [Python] (C:/Users/thefl/AppData/Roaming/NA-MIC/Extensions-28257/SegmentMesher/lib/Slicer-4.10/qt-scripted-modules/SegmentMesher.py:375) - Attempt to find executable at: C:\Users\thefl\AppData\Roaming\NA-MIC\Extensions-28257\SegmentMesher\lib\Slicer-4.10\cleaver-cli.exe<br>
[INFO][Python] 18.02.2020 10:55:48 [Python] (C:/Users/thefl/AppData/Roaming/NA-MIC/Extensions-28257/SegmentMesher/lib/Slicer-4.10/qt-scripted-modules/SegmentMesher.py:361) - Generating volumetric mesh…<br>
[WARNING][VTK] 18.02.2020 10:55:48 [] (unknown:0) - Generic Warning: In D:\D\S\Slicer-4102\Libs\MRML\Core\vtkDataFileFormatHelper.cxx, line 237<br>
vtkDataFileFormatHelper::GetFileExtensionFromFormatString: please update deprecated extension-only format specifier to ‘File format name (.ext)’ format! Current format string: .nrrd<br>
[INFO][Stream] 18.02.2020 10:55:48 [] (unknown:0) - Generating volumetric mesh…<br>
[INFO][Python] 18.02.2020 10:55:48 [Python] (C:/Users/thefl/AppData/Roaming/NA-MIC/Extensions-28257/SegmentMesher/lib/Slicer-4.10/qt-scripted-modules/SegmentMesher.py:448) - Generate mesh using: C:\Users\thefl\AppData\Roaming\NA-MIC\Extensions-28257\SegmentMesher\lib\Slicer-4.10\cleaver-cli.exe: [’–input_files’, u’C:/Users/thefl/AppData/Local/Temp/Slicer/SegmentMesher/20200218_105548_245\inputLabelmap.nrrd’, ‘–segmentation’, ‘–output_path’, u’C:/Users/thefl/AppData/Local/Temp/Slicer/SegmentMesher/20200218_105548_245/’, ‘–output_format’, ‘vtkUSG’, ‘–fix_tet_windup’, ‘–strip_exterior’, ‘–verbose’, ‘–scale’, ‘0.2’, ‘–multiplier’, ‘2’, ‘–grading’, ‘5’]<br>
[INFO][Stream] 18.02.2020 10:55:48 [] (unknown:0) - Generate mesh using: C:\Users\thefl\AppData\Roaming\NA-MIC\Extensions-28257\SegmentMesher\lib\Slicer-4.10\cleaver-cli.exe: [’–input_files’, u’C:/Users/thefl/AppData/Local/Temp/Slicer/SegmentMesher/20200218_105548_245\inputLabelmap.nrrd’, ‘–segmentation’, ‘–output_path’, u’C:/Users/thefl/AppData/Local/Temp/Slicer/SegmentMesher/20200218_105548_245/’, ‘–output_format’, ‘vtkUSG’, ‘–fix_tet_windup’, ‘–strip_exterior’, ‘–verbose’, ‘–scale’, ‘0.2’, ‘–multiplier’, ‘2’, ‘–grading’, ‘5’]<br>
[INFO][Stream] 18.02.2020 10:56:16 [] (unknown:0) - ‘NoneType’ object has no attribute ‘GetType’<br>
[CRITICAL][Stream] 18.02.2020 10:56:16 [] (unknown:0) - Traceback (most recent call last):<br>
[CRITICAL][Stream] 18.02.2020 10:56:16 [] (unknown:0) -   File “C:/Users/thefl/AppData/Roaming/NA-MIC/Extensions-28257/SegmentMesher/lib/Slicer-4.10/qt-scripted-modules/SegmentMesher.py”, line 296, in onApplyButton<br>
[CRITICAL][Stream] 18.02.2020 10:56:16 [] (unknown:0) -     self.cleaverPaddingPercentSpinBox.value * 0.01)<br>
[CRITICAL][Stream] 18.02.2020 10:56:16 [] (unknown:0) -   File “C:/Users/thefl/AppData/Roaming/NA-MIC/Extensions-28257/SegmentMesher/lib/Slicer-4.10/qt-scripted-modules/SegmentMesher.py”, line 625, in createMeshFromSegmentationCleaver<br>
[CRITICAL][Stream] 18.02.2020 10:56:16 [] (unknown:0) -     if currentColorNode.GetType() == currentColorNode.User and currentColorNode.IsA(“vtkMRMLColorTableNode”):<br>
[CRITICAL][Stream] 18.02.2020 10:56:16 [] (unknown:0) - AttributeError: ‘NoneType’ object has no attribute ‘GetType’</p>

---

## Post #15 by @lassoan (2020-02-18 03:47 UTC)

<p>Thank you. The two executions are completely different.</p>
<p>Your mesh cannot be imported into the segmentation. Can you upload it somewhere and send the download link?</p>
<p>In the second case, I was able to reproduce the problem based on the logs. It seems that in Segment mesher module, you have accidentally left the “Output model” as “ProstateMeanShape2” (the original input surface mesh). This was unexpected and this case was not handled properly, but I’ve fixed the logic now (the updated file is available at the same URL). I would recommend to load the mesh file directly as a segmentation node by choosing “Segmentation” in Add data dialog’s description column (then you would not need to convert the model node to segmentation node and end up with an extra model node in the scene that you don’t need).</p>

---

## Post #16 by @ChristopherWaters (2020-02-18 05:25 UTC)

<p>Thank you, I got the prostate model to work by directly loading it in as a mesh, and was able to play with Cleaver’s parameters without breaking anything.</p>
<p>In regards to my model, I never get the option to add it as a segment, only Model / Volume / Scalar Overlay.</p>
<p>My .vtk file: <a href="https://pastebin.com/zTvj9LE1" rel="nofollow noopener">https://pastebin.com/zTvj9LE1</a></p>

---

## Post #17 by @lassoan (2020-02-18 06:30 UTC)

<p>Your VTK file is already as volumetric mesh, and so it is already perfectly accurate and the simplest possible as is - there is nothing to do for the segment mesher.</p>
<p>If you want to have more elements then you can convert to tetrahedra and subdivide it as many times as needed, for example:</p>
<pre><code class="lang-python">unstructuredGridNode = getNode('testCube')
unstructuredGridNode.GetDisplayNode().SetBackfaceCulling(False)
unstructuredGridNode.GetDisplayNode().EdgeVisibilityOn()

tetrahedralize=vtk.vtkDataSetTriangleFilter()
tetrahedralize.SetInputData(unstructuredGridNode.GetMesh())

subdivide=vtk.vtkSubdivideTetra()
subdivide.SetInputConnection(tetrahedralize.GetOutputPort())
subdivide.Update()

subdivide2=vtk.vtkSubdivideTetra()
subdivide2.SetInputData(subdivide.GetOutput())
subdivide2.Update()

unstructuredGridNode.SetAndObserveMesh(subdivide2.GetOutput())
</code></pre>
<p>If you want to use Segment Mesher module on a volumetric mesh grid then you have to convert it to labelmap or surface mesh first (using vtkResampleToImage or vtkGeometryFilter).</p>

---

## Post #18 by @ChristopherWaters (2020-02-18 06:38 UTC)

<p>Thank you for all of your help, but now I am completely confused… How did you know it was a volumetric mesh? In my perspective, all I do in VTK is define a surface using points and cells.</p>

---

## Post #19 by @lassoan (2020-02-18 06:57 UTC)

<aside class="quote no-group" data-username="ChristopherWaters" data-post="18" data-topic="10243">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/d78d45/48.png" class="avatar"> ChristopherWaters:</div>
<blockquote>
<p>How did you know it was a volumetric mesh?</p>
</blockquote>
</aside>
<p>Typically, surfaces meshes are stored in vtkPolyData, while volumetric meshes are stored in vtkUnstructuredGrid. Your vtk file contained an unstructured grid, which suggested that it is a volumetric mesh, and the cell type = 12 confirmed that indeed your mesh had a single volumetric cell: a <a href="https://github.com/Kitware/VTK/blob/master/Common/DataModel/vtkCellType.h#L58">hexahedron</a>.</p>
<pre><code class="lang-plaintext"># vtk DataFile Version 4.2
vtk output
ASCII
DATASET UNSTRUCTURED_GRID
POINTS 8 float
20 20 -20 -20 20 -20 -20 -20 -20
20 -20 -20 20 20 20 -20 20 20
-20 -20 20 20 -20 20
CELLS 1 9
8 0 1 2 3 4 5 6 7
 
CELL_TYPES 1
12
</code></pre>
<aside class="quote no-group" data-username="ChristopherWaters" data-post="18" data-topic="10243">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/d78d45/48.png" class="avatar"> ChristopherWaters:</div>
<blockquote>
<p>Thank you for all of your help, but now I am completely confused</p>
</blockquote>
</aside>
<p>We seem to use completely different terminologies - in the title you call your input data “surface mesh”, while I would say it is a volumetric mesh; you say “triangulating”, while I would say that triangulation is the trivial operation of subdividing meshes to triangles or tetrahedra (performed by vtkDataSetTriangleFilter) and probably you want to do adaptive remeshing.</p>
<p>Perhaps switching to a real data set will make it more clear what you would like to do and what is a good approach to achieve it.</p>

---

## Post #20 by @ChristopherWaters (2020-02-19 04:32 UTC)

<p>My apolgoies for the confusion. To be clear, I only care about the <strong>surface and wish to triangulate/subdivide it in a controlled manner</strong>.</p>
<p>With this new understanding my plan is to go from vtkUnstructredGrid (volumetric) → vtkGeometryFilter → vtkPolyData(surface mesh) → 3DSlicer Segmentation → SegMesher(Cleaver).</p>
<p>I have successfully done this, but there are 2 difficulties I am having:</p>
<ul>
<li>I cannot load my polydata in as a Segmentation directly, but when I load it in as a Model and then convert to segmentation it behaves fine, creating the segmentation automatically and working with SegMesher.</li>
<li>I cannot fully control the amount of subdivisions cleaver applies to my model. I have played with the parameters but cannot make Cleaver increase the amount of triangles/tetrahedra</li>
</ul>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d5937acbc603983b7457aa8603d44df9a8b189dc.png" alt="cap" data-base62-sha1="utnFQumA57h215VFoMCD1IKSUzi" width="464" height="441"><br>
(as you can see there are only 2 triangles per surface, I would like to add many more and also set boundaries in which triangulation would increase in fineness as you aproach them)</p>
<hr>
<p>My .vtk file to avoid any confusion:</p>
<pre><code class="lang-auto"># vtk DataFile Version 4.2
vtk output
ASCII
DATASET POLYDATA
POINTS 8 float
-20 20 20 20 20 20 20 20 -20 
-20 20 -20 20 -20 20 -20 -20 20 
-20 -20 -20 20 -20 -20 
POLYGONS 6 30
4 0 1 2 3 
4 4 5 6 7 
4 5 0 3 6 
4 1 4 7 2 
4 1 0 5 4 
4 7 6 3 2 
</code></pre>

---

## Post #21 by @lassoan (2020-02-20 03:48 UTC)

<aside class="quote no-group" data-username="ChristopherWaters" data-post="20" data-topic="10243">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/d78d45/48.png" class="avatar"> ChristopherWaters:</div>
<blockquote>
<p>To be clear, I only care about the <strong>surface and wish to triangulate/subdivide it in a controlled manner</strong> .</p>
</blockquote>
</aside>
<p>Do you only need adaptive remeshing of the surface mesh? Then you don’t need volumetric mesher at all. What is your goal? What are you going to use the mesh for?</p>

---

## Post #22 by @ChristopherWaters (2020-02-20 05:17 UTC)

<p>My apologies, I will try to explain myself the best I can:</p>
<ul>
<li>Users will design devices (vtk) that will then go through Cleaver in order to produces meshes for 2D/3D FEM.</li>
<li>If users cho0se 2D FEM I only look at a specific 2D surface, while if they chose 3D FEM a volumetric mesh is used. I would like to use Cleaver for both applications.</li>
</ul>
<p>Currently I am having trouble adjusting the amount of elements Cleaver produces, as shown above. I am able to control the accuracy of the mesh, but would also like to control the amount of elements created (fineness) and apply boundary conditions that increase the density of elements(fineness) if possible.</p>

---

## Post #23 by @lassoan (2020-02-20 05:23 UTC)

<p>You can control element sizes as described in <a href="https://sciinstitute.github.io/cleaver.pages/manual.html#command-line-tool">Cleaver documentation</a>. I haven’t tried this, but based on the documentation my understanding is that you can even specify a sizing field ( <code>--sizing_field</code> argument), which allows you to designate regions where you want the mesh to be finer or coarser. You may also experiment with the mesh generation parameters using GUI application that can be downloaded from Cleaver’s website.</p>

---

## Post #24 by @ChristopherWaters (2020-02-20 05:26 UTC)

<p>If I created a surface mesh using vtkGeometryFilter can I use that as input for Cleaver or do I need convert my surface mesh file (.vtk) to NRRD format? Could Slicer help with this conversion process?</p>
<p>I am confused as to what type of input Cleaver takes, as finding detailed Cleaver documentation seems impossible.</p>

---

## Post #25 by @lassoan (2020-02-20 05:35 UTC)

<aside class="quote no-group" data-username="ChristopherWaters" data-post="24" data-topic="10243">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/d78d45/48.png" class="avatar"> ChristopherWaters:</div>
<blockquote>
<p>If I created a surface mesh using vtkGeometryFilter</p>
</blockquote>
</aside>
<p>How did you create that surface? What is your input? Normally you would only need vtkGeometryFilter to create a surface mesh from a volumetric mesh using Cleaver - but if you already had a volumetric mesh then why would you create it again?</p>
<aside class="quote no-group" data-username="ChristopherWaters" data-post="24" data-topic="10243">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/d78d45/48.png" class="avatar"> ChristopherWaters:</div>
<blockquote>
<p>Cleaver or do I need convert my surface mesh file (.vtk) to NRRD format? Could Slicer help with this conversion process?</p>
</blockquote>
</aside>
<p>Cleaver’s input is binary or fractional labelmap volume (.nrrd). Note that .vtk file can contain anything (surface mesh - polydata, volumetric mesh - unstructured grid, image volume, etc.).</p>

---

## Post #26 by @ChristopherWaters (2020-02-20 06:03 UTC)

<p>I was going from volume to surface to volume because my original format is vtkUnstrucredGrid(.vtk file) and I need to get to NRRD.</p>
<p>What would be the best way to go from my original format to binary/fractional labelmap volume?</p>

---

## Post #27 by @lassoan (2020-02-20 13:40 UTC)

<p>Could you draw a simple diagram of your full processing workflow, including indication of where your inputs come from and where the outputs go?</p>

---

## Post #28 by @ChristopherWaters (2020-02-25 01:39 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/7066441f391786f057e9fbd08e89bbc9180cc5c4.png" data-download-href="/uploads/short-url/g2kA0BoZbGdl6s7nDFWTvaE4Hbe.png?dl=1" title="cap" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/7066441f391786f057e9fbd08e89bbc9180cc5c4.png" alt="cap" data-base62-sha1="g2kA0BoZbGdl6s7nDFWTvaE4Hbe" width="690" height="336" data-dominant-color="F1F0F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">cap</span><span class="informations">1215×593 19.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The only thing I am unsure about is if I can use <strong>Cleaver for 2D Models</strong></p>

---

## Post #29 by @lassoan (2020-02-25 03:11 UTC)

<p>Thank you, this helps. What is in Model Creation step’s VTK unstructured grid? Are you working with simple geometric primitives only (or you also import some complex shape from 3D scans, etc.)? What do you mean by “Discretised mesh”?</p>

---

## Post #30 by @ChristopherWaters (2020-02-25 04:55 UTC)

<ul>
<li>The unGrid is created purely from simple 2D VTK Cells</li>
<li>By Discretised I mean a Mesh that is suitable for FEM, with nodes created from partitioned geometry that are collectively sufficient to serve as the domain of analysis for the model</li>
</ul>

---

## Post #31 by @lassoan (2020-02-25 05:26 UTC)

<p>In Slicer, we rarely work with 2D structures (because real life is mostly 3D) and we usually have very complex geometries (from imaging data). If you only need triangulation of simple geometry then you may be able to get that by using a few simple VTK filters, such as vtkDelaunay2D.</p>

---

## Post #32 by @ChristopherWaters (2020-02-26 05:25 UTC)

<p>Though they are created from 2D Cells, my 3D models can become quite complex; they also contain different types of materials. This is why I am interested in Cleaver, I really like what the latice cleaving method outputs.</p>
<p>In terms of my 2D models, does Cleaver support 2D input? I have read some of Ross Whitaker’s papers, and 2D examples are talked about.</p>

---

## Post #33 by @lassoan (2020-02-26 18:05 UTC)

<p>I don’t know if Cleaver supports 2D meshes. You can ask Cleaver developers about it.</p>

---

## Post #34 by @Ross (2020-02-26 19:50 UTC)

<p>Hi Christopher,</p>
<p>For Cleaver-specific questions, there is also a separate project that supports Cleaver.    Would you willing to push your 2D question to that list:</p>
<p><a href="https://www.sci.utah.edu/software/cleaver.html" class="onebox" target="_blank" rel="nofollow noopener">https://www.sci.utah.edu/software/cleaver.html</a></p>
<p>Regards.</p>

---

## Post #35 by @ChristopherWaters (2020-03-01 10:56 UTC)

<p>My apologies for all of the confusion caused in this thread (I am a c++ dev that has ben thrown into sci vis), let me try to clarify everything so that people can still find this useful:</p>
<hr>
<aside class="quote no-group" data-username="Ross" data-post="34" data-topic="10243">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/e274bd/48.png" class="avatar"> Ross:</div>
<blockquote>
<p>For Cleaver-specific questions, there is also a separate project that supports Cleaver. Would you willing to push your 2D question to that list:</p>
<p><a href="https://www.sci.utah.edu/software/cleaver.html" rel="noopener nofollow ugc">https://www.sci.utah.edu/software/cleaver.html </a></p>
</blockquote>
</aside>
<p>I will stop straying to Cleaver specific discourse(that mailing list is dead and not working, I can not find a single place to discus Cleaver or any doc besides the src).</p>
<hr>
<aside class="quote no-group" data-username="lassoan" data-post="17" data-topic="10243">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Your VTK file is <strong>already as volumetric mesh, and so it is already perfectly accurate and the simplest possible as is</strong> - there is nothing to do for the segment mesher.</p>
<p>If you want to have more elements then you can convert to tetrahedra and subdivide it as many times as needed</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="lassoan" data-post="19" data-topic="10243">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>We seem to use completely different terminologies - in the title you call your input data “surface mesh”, while I would say it is a volumetric mesh; you say “triangulating”, while <strong>I would say that triangulation is the trivial operation of subdividing meshes to triangles or tetrahedra</strong> (performed by vtkDataSetTriangleFilter) and probably you want to do adaptive remeshing.</p>
</blockquote>
</aside>
<p>Does this mean that Cleaver/SegMesher is only used to generate Volumetric Meshes, and that since I already have one all I need to do is subdivide it?</p>
<aside class="quote no-group" data-username="lassoan" data-post="31" data-topic="10243">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>In Slicer, we rarely work with 2D structures (because real life is mostly 3D) and <strong>we usually have very complex geometries</strong> (from imaging data). If you <strong>only need triangulation of simple geometry</strong> then you may be able to get that by using a few simple VTK filters, such as vtkDelaunay2D.</p>
</blockquote>
</aside>
<p>What do you mean by complex geometries, i.e. geometries that are too complex to simply subdivide in a manner such as above?</p>

---

## Post #36 by @lassoan (2020-03-01 19:47 UTC)

<aside class="quote no-group" data-username="ChristopherWaters" data-post="35" data-topic="10243">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/d78d45/48.png" class="avatar"> ChristopherWaters:</div>
<blockquote>
<p>will stop straying to Cleaver specific discourse(that mailing list is dead and not working, I can not find a single place to discus Cleaver or any doc besides the src).</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/ross">@Ross</a> could you tell where exactly Cleaver users/developers  can be reached?</p>
<aside class="quote no-group" data-username="ChristopherWaters" data-post="35" data-topic="10243">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/d78d45/48.png" class="avatar"> ChristopherWaters:</div>
<blockquote>
<p>Does this mean that Cleaver/SegMesher is only used to generate Volumetric Meshes, and that since I already have one all I need to do is subdivide it?</p>
</blockquote>
</aside>
<p>It depends on what exactly you would like to do. Maybe you can use your mesh as is, or try simple tetrahedralization, maybe uniform subdivision. Cleaver does complete remeshing, with adaptive adjustment of element sizes, which is useful for finite element analysis.</p>
<aside class="quote no-group" data-username="ChristopherWaters" data-post="35" data-topic="10243">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/d78d45/48.png" class="avatar"> ChristopherWaters:</div>
<blockquote>
<p>What do you mean by complex geometries</p>
</blockquote>
</aside>
<p>For example, what you create by segmenting complex anatomical structures.</p>

---
