---
topic_id: 11759
title: "New Module Dynamic Modeler Parametric Surface Editing For Bi"
date: 2020-05-28
url: https://discourse.slicer.org/t/11759
---

# New module: Dynamic Modeler - parametric surface editing for biomedical applications

**Topic ID**: 11759
**Date**: 2020-05-28
**URL**: https://discourse.slicer.org/t/new-module-dynamic-modeler-parametric-surface-editing-for-biomedical-applications/11759

---

## Post #1 by @Sunderlandkyl (2020-05-28 21:43 UTC)

<p>We have added a new module called “Dynamic Modeler” to the latest Slicer preview releases (4.11). This module provides an extensible framework for automatic processing of mesh nodes by executing “Tools” on the input to generate output mesh.</p>
<div class="youtube-onebox lazy-video-container" data-video-id="F6fNMQTxD-4" data-video-title="3D Slicer: Dynamic Modeler - Parametric Surface Editing for Biomedical Applications" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=F6fNMQTxD-4" target="_blank" class="video-thumbnail" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/F6fNMQTxD-4/maxresdefault.jpg" title="3D Slicer: Dynamic Modeler - Parametric Surface Editing for Biomedical Applications" width="" height="">
  </a>
</div>

<p>Output of a tool can be used as input in another tool, which allows specification of complex editing operations. This is similar to “parametric editing” in engineering CAD software, but this module is specifically developed to work well on complex meshes used in biomedical applications (while most engineering CAD software does not directly support parametric editing of complex polygonal meshes).</p>
<p>Current tools:</p>
<ul>
<li>Plane cut: Cut a plane into two separate meshes using any number of markup planes or slice views. The planes can be combined using union, intersection and difference boolean operations.</li>
<li>Mirror: Reflect the points in a model across the input plane. Useful in conjunction with the plane cut tool to cut a model in half and then mirror the selected half accross the cutting plane.</li>
<li>Curve cut: Extract a region from the surface that is enclosed by a markup curve.</li>
<li>Boundary cut: Extract a region from the surface that is enclosed by many markup curves and planes. In instances where there is ambiguity about which region should be extracted, a markup fiducial can be used to specify the region of interest.</li>
<li>Append: Combine multiple models into a single output model.</li>
</ul>
<p>Notes:</p>
<ul>
<li>To enable automatic update (so that outputs are automatically recomputed whenever inputs change), check the checkbox on the Apply button.</li>
<li>Tools cannot be run continuously if one of the input nodes is present in the output. The tool can still be run on demand by clicking the apply button.</li>
</ul>
<p>Any suggestions and feature requests are welcome. Based on feedback we get, we may add more tools, such as: rotate around axis, shell, extrude, intersect, parametric shapes (cube, cylinder, etc.).</p>
<p><strong>Parcellating white matter surface with curves and planes:</strong><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/8085fd2da306adeaf208b78766b0b4fa8f8d2c98.jpeg" data-download-href="/uploads/short-url/ikYby3hdsSQ4Q74DjmDGTaYgiPS.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8085fd2da306adeaf208b78766b0b4fa8f8d2c98_2_690x373.jpeg" alt="image" data-base62-sha1="ikYby3hdsSQ4Q74DjmDGTaYgiPS" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8085fd2da306adeaf208b78766b0b4fa8f8d2c98_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8085fd2da306adeaf208b78766b0b4fa8f8d2c98_2_1035x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8085fd2da306adeaf208b78766b0b4fa8f8d2c98_2_1380x746.jpeg 2x" data-dominant-color="9F9DB6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1040 514 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>Skull mirroring for facial deformity reconstruction:</strong><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/be9ba6c6275b554ac6fa6662182c3bd2b3e5ab3f.png" data-download-href="/uploads/short-url/rccct2p0dNM8pMOLPziWICKfD43.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be9ba6c6275b554ac6fa6662182c3bd2b3e5ab3f_2_690x373.png" alt="image" data-base62-sha1="rccct2p0dNM8pMOLPziWICKfD43" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be9ba6c6275b554ac6fa6662182c3bd2b3e5ab3f_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be9ba6c6275b554ac6fa6662182c3bd2b3e5ab3f_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be9ba6c6275b554ac6fa6662182c3bd2b3e5ab3f_2_1380x746.png 2x" data-dominant-color="A3A0A8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1040 242 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>For developers:</p>
<ul>
<li>New tools can be added by any module by subclassing the vtkSlicerDynamicModelerTool class and registering the new tool with the vtkSlicerDynamicModelerToolFactory.</li>
<li>Tools can be added to models in the scene by adding a vtkMRMLDynamicModelerNode to the scene, specifying the tool name, setting the parameters, and setting the input/output node references as defined by the tool.</li>
</ul>
<p>Development was funded in part by CANARIE’s Research Software Program, OpenAnatomy, and Brigham and Women’s Hospital through NIH grant R01MH112748.</p>

---

## Post #2 by @muratmaga (2020-08-08 06:31 UTC)

<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> <a class="mention" href="/u/lassoan">@lassoan</a><br>
I am trying the curveCut implementation, and getting “Can’t follow edge. No input data” error. Are these implemented or they are place holders?</p>
<p>This is what I am trying to cut:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/16a1b6dcd4ca4c426e5a7bef4cd2ace78995571b.jpeg" data-download-href="/uploads/short-url/3ecYupTDpi7SHWulTu8KdSWm7LJ.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/16a1b6dcd4ca4c426e5a7bef4cd2ace78995571b_2_690x469.jpeg" alt="image" data-base62-sha1="3ecYupTDpi7SHWulTu8KdSWm7LJ" width="690" height="469" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/16a1b6dcd4ca4c426e5a7bef4cd2ace78995571b_2_690x469.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/16a1b6dcd4ca4c426e5a7bef4cd2ace78995571b_2_1035x703.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/16a1b6dcd4ca4c426e5a7bef4cd2ace78995571b_2_1380x938.jpeg 2x" data-dominant-color="AFB066"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1611×1096 292 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @lassoan (2020-08-08 12:58 UTC)

<p>It is fully implemented and should work well. Can you share your scene with us so that we can investigate?</p>

---

## Post #4 by @muratmaga (2020-08-08 15:25 UTC)

<p>Sure. here it is:<br>
<a href="https://app.box.com/s/x5y85fzrcxwueefox7i53eep6whhqqiv" class="onebox" target="_blank" rel="nofollow noopener">https://app.box.com/s/x5y85fzrcxwueefox7i53eep6whhqqiv</a></p>
<p>I am using the resampled curve to cut.</p>

---

## Post #5 by @lassoan (2020-08-08 16:34 UTC)

<p>There are two issues:</p>
<ul>
<li>the mesh has has very large, unevenly sized, ill-shaped cells, so methods that rely on path searching between points run into trouble (similarly to how some image processing algorithms cannot operate on very low-resolution images)</li>
<li>the mesh has multiple disconnected regions (internal cavities), so when the surface cut is completed and the curve cut tool finds the largest mesh piece, it finds and extracts an already disconnected region (because that is larger than the small extracted patch) - <a class="mention" href="/u/sunderlandkyl">@sunderlandkyl</a>, do you have an idea if we could fix this?</li>
</ul>
<p>You can solve these issues using Surface toolbox:</p>
<ul>
<li>Enable “Decimation”, set reduction to 0.5% (to force resampling, and remove very small cells, but still keep enough points), this uses the recently introduced Quadric decimation method, which provides much higher quality mesh than the previously used DecimatePro</li>
<li>Enable “Connectivity” (this keeps only the largest connected region)</li>
<li>Optional: Enable “Normals” (just to improve appearance)</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f508b20c502cc7ccc1bfb98087eeb6657c82b130.jpeg" data-download-href="/uploads/short-url/yXFBPVGznb42hQ3tG863MR84TS0.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f508b20c502cc7ccc1bfb98087eeb6657c82b130_2_614x500.jpeg" alt="image" data-base62-sha1="yXFBPVGznb42hQ3tG863MR84TS0" width="614" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f508b20c502cc7ccc1bfb98087eeb6657c82b130_2_614x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f508b20c502cc7ccc1bfb98087eeb6657c82b130_2_921x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f508b20c502cc7ccc1bfb98087eeb6657c82b130.jpeg 2x" data-dominant-color="908E8C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1145×931 536 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Full scene: <a href="https://1drv.ms/u/s!Arm_AFxB9yqHw70xlDR_uOifvDbc-Q?e=ljUnrm" class="inline-onebox">Microsoft OneDrive - Access files anywhere. Create docs with free Office Online.</a></p>
<p>I would recommend to re-create the simplified gorilla head mesh from the original high-resolution mesh using the new quadric decimation method. You will get much higher quality mesh with the same number of points.</p>

---

## Post #6 by @muratmaga (2020-08-09 04:19 UTC)

<p>Thanks Andras.</p>
<p>I do not have the original high-res mesh anymore, but I do have the volume it came from:<br>
<a href="https://raw.githubusercontent.com/muratmaga/Hominoid_Skulls/master/Gorilla_gorilla/gor_template0_cleaned.nrrd" class="onebox" target="_blank" rel="nofollow noopener">https://raw.githubusercontent.com/muratmaga/Hominoid_Skulls/master/Gorilla_gorilla/gor_template0_cleaned.nrrd</a></p>
<p>After segmentation via threshold (10.15-Max), I am trying what you suggested and whenever I enable the Connectivity and/or Normal, output is blank. Decimation by itself works. Here is the log file, if there is anything helpful:</p>
<pre><code>"Model" Reader has successfully read the file "C:/Users/murat/Desktop/Gorilla_Skull_original_segmentation.obj" "[14.24s]"
Found CommandLine Module, target is  C:/Users/murat/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-04/bin/../lib/Slicer-4.11/cli-modules/Decimation.exe
ModuleType: CommandLineModule
Decimation command line: 

C:/Users/murat/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-04/bin/../lib/Slicer-4.11/cli-modules/Decimation.exe --reductionFactor 0.5 --method FastQuadric --deleteBoundary --aggressiveness 7.0 C:/Users/murat/AppData/Local/Temp/Slicer/DFCHC_vtkMRMLModelNodeF.obj C:/Users/murat/AppData/Local/Temp/Slicer/DFCHC_vtkMRMLModelNodeF.obj 

Decimation standard output:

Input: 2388660 vertices,4779192 triangles (target 2389596)
Output: 1192449 vertices,2389596 triangles (0.5 reduction)
vtkDebugLeaks has found no leaks.

Decimation completed without errors

ReadDataInternal (vtkMRMLModelStorageNode2): File C:/Users/murat/AppData/Local/Temp/Slicer/DFCHC_vtkMRMLModelNodeF.obj does not contain coordinate system information. Assuming LPS.


Found CommandLine Module, target is  C:/Users/murat/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-04/bin/../lib/Slicer-4.11/cli-modules/Normals.exe
ModuleType: CommandLineModule
Normals command line: 

C:/Users/murat/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-04/bin/../lib/Slicer-4.11/cli-modules/Normals.exe --angle 30 C:/Users/murat/AppData/Local/Temp/Slicer/DFCHC_vtkMRMLModelNodeF.vtp C:/Users/murat/AppData/Local/Temp/Slicer/DFCHC_vtkMRMLModelNodeF.vtp 

Normals standard output:

vtkDebugLeaks has found no leaks.

Normals completed without errors

ReadDataInternal (vtkMRMLModelStorageNode2): File C:/Users/murat/AppData/Local/Temp/Slicer/DFCHC_vtkMRMLModelNodeF.vtp does not contain coordinate system information. Assuming LPS.


Found CommandLine Module, target is  C:/Users/murat/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-04/bin/../lib/Slicer-4.11/cli-modules/Connectivity.exe
ModuleType: CommandLineModule
Connectivity command line: 

C:/Users/murat/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-04/bin/../lib/Slicer-4.11/cli-modules/Connectivity.exe C:/Users/murat/AppData/Local/Temp/Slicer/DFCHC_vtkMRMLModelNodeF.vtp C:/Users/murat/AppData/Local/Temp/Slicer/DFCHC_vtkMRMLModelNodeF.vtp 

Connectivity standard output:

vtkDebugLeaks has found no leaks.

Connectivity completed without errors

ReadDataInternal (vtkMRMLModelStorageNode2): File C:/Users/murat/AppData/Local/Temp/Slicer/DFCHC_vtkMRMLModelNodeF.vtp does not contain coordinate system information. Assuming LPS.</code></pre>

---

## Post #7 by @lassoan (2020-08-09 14:47 UTC)

<p>I segmented using Threshold and Smoothing (Fill holes), exported to surface, and then used Surface Toolbox successfully:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/dd9a960a3a83a73a8aa43335f6c1d3fefa7d1136.png" data-download-href="/uploads/short-url/vCoIEffLD3tg2r4RruzrKNMSb7E.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd9a960a3a83a73a8aa43335f6c1d3fefa7d1136_2_447x499.png" alt="image" data-base62-sha1="vCoIEffLD3tg2r4RruzrKNMSb7E" width="447" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd9a960a3a83a73a8aa43335f6c1d3fefa7d1136_2_447x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd9a960a3a83a73a8aa43335f6c1d3fefa7d1136_2_670x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd9a960a3a83a73a8aa43335f6c1d3fefa7d1136_2_894x998.png 2x" data-dominant-color="F3F4F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1083×1211 37.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>Complete scene:</strong> <a href="https://1drv.ms/u/s!Arm_AFxB9yqHw71U9_FPmLMQrx0PPw?e=OmQnvK" class="inline-onebox">Microsoft OneDrive</a></p>
<p>With 95% decimation, curve cut is quite usable but it sometimes requires some adjustment of the curve to find path between points. Probably the underlying VTK filters could be made more robust.</p>

---

## Post #8 by @muratmaga (2020-08-09 15:58 UTC)

<p>These settings worked for me too! Thanks.</p>

---

## Post #9 by @Sunderlandkyl (2020-08-10 14:43 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="11759">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>the mesh has multiple disconnected regions (internal cavities), so when the surface cut is completed and the curve cut tool finds the largest mesh piece, it finds and extracts an already disconnected region (because that is larger than the small extracted patch) - <a class="mention" href="/u/sunderlandkyl">@sunderlandkyl</a>, do you have an idea if we could fix this?</p>
</blockquote>
</aside>
<p>Currently the curve cut tool finds the smallest region as the “inside”, and the largest region as the outside. I think there are a couple of ways that it can be improved, including adding an optional seed fiducial to select the “inside” (similar to boundary cut).</p>

---

## Post #10 by @lassoan (2020-08-10 14:51 UTC)

<p>An optional seed would be great.</p>
<p>Instead of smallest/largest region, we should return the inside and “inverse of inside” (I don’t remember which filter we use, but there should be either an option to return both inside and outside surface or a flag to invert the selection).</p>

---

## Post #11 by @lassoan (2022-03-10 21:24 UTC)

<p>I’ve implemented multiple fixes in the VTK filter that the Curve cut tool uses. As a result, cuts are now always successful (<code>Can’t follow edge</code> never occurs) and also more accurate (previously the cuts sometimes did not go all the way to the boundaries). I’ve also added an additional option for straight cut (switches between following the input curve more accurately / preserving the original cells) and a fiducial point input to select what region is considered as being “inside”.</p>

---

## Post #12 by @mau_igna_06 (2022-04-05 15:07 UTC)

<aside class="quote quote-modified" data-post="1" data-topic="22165">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/new-dynamic-modeler-tool-select-by-points/22165/1">New Dynamic Modeler Tool: Select by Points</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    <a href="https://www.youtube.com/watch?v=Klsi6x3F5D4" target="_blank" rel="noopener nofollow ugc">
    [Select By Points Tool, Dynamic Modeler, 3D Slicer]
  </a>


Select by points tool is available on the Dynamic Modeler module since end of October 2021 Slicer Preview Release 
This tools allows you to create 2 types of output models from an input model, a fiducial list, a selection-distance and a selection-algorithm. 
One of the possible outputs is copy of the input model with selection scalars (unselected=0, selected=1) according to the selection-algorithm and selection-distance using the f…
  </blockquote>
</aside>


---
