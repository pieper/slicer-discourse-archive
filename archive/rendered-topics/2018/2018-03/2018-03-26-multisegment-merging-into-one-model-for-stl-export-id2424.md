---
topic_id: 2424
title: "Multisegment Merging Into One Model For Stl Export"
date: 2018-03-26
url: https://discourse.slicer.org/t/2424
---

# Multisegment merging into one model for STL export

**Topic ID**: 2424
**Date**: 2018-03-26
**URL**: https://discourse.slicer.org/t/multisegment-merging-into-one-model-for-stl-export/2424

---

## Post #1 by @J_Scales (2018-03-26 13:30 UTC)

<p>New to using 3D slicer and have followed the cardiac segmentation video and had a question regarding export of the segments into STL. It seems that when one goes to export each segment as a model they are exported as there own segment (meaning 8 stl files for 8 segments). Is there anyway to combine the segments as one STL file? I have tried the logical operator tab Add function (not sure if I used it correctly) but am not sure if this would be the solution. I am using Slicer 4.8.</p>
<p>Anyway thanks for any tips and answers. This is a great program.</p>

---

## Post #2 by @lassoan (2018-03-26 16:16 UTC)

<p>Latest nightly version of Slicer has a dedicated file export feature. You have the option of saving as merged STL (all segments merged into a single mesh) or OBJ (single file, segments are different objects). See details here:</p>
<aside class="quote quote-modified" data-post="1" data-topic="2428">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/save-segmentation-directly-to-stl-or-obj/2428">Save segmentation directly to STL or OBJ files</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    We often received questions about how to export segmentation to STL file for 3D printing. We’ve added a simplified, dedicated tool to make this step easier. 
1-minute demo video: 

  <a href="https://www.youtube.com/watch?v=WfuYPVYA5cA" target="_blank" rel="noopener">
    [Export Slicer image segmentation to STL or OBJ file]
  </a>


Main features: 

Export STL file: each segment as a separate file or all segments merged into a single mesh
Export OBJ file: all segments are saved in one file, segment colors and opacities are preserved
Export all or visible segments only
Coordinate sy…
  </blockquote>
</aside>


---

## Post #3 by @J_Scales (2018-03-26 16:25 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="2424">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Latest nightly version of Slicer has a dedicated file export feature. You have the option of saving as merged STL (all segments merged into a single mesh) or OBJ (single file, segments are different objects). See details here:</p>
</blockquote>
</aside>
<p>Really appreciate this response and the video. Good to know the latest nightly build has this built in.</p>

---

## Post #4 by @Anis (2019-04-26 10:03 UTC)

<p>Operating system:Windows 7<br>
Slicer version:Slicer4.9.0<br>
Expected behavior: stl file for the merged model<br>
Actual behavior:error in merging the two segment model<br>
Hi,</p>
<p>I am working with Slicer4.9.0. I want to generate stl for a sample having two regions.</p>
<p>I could generate stl for both regions individually but when I try to merge model Slicer shows error and gets close.If I try to add the two segments using logical operation I get an stl but that shows error in Gmsh which I use for further mesh refinement.I have tried this process with Slicer4.8.1 also.<br>
I don’t have dropbox to tranfer files.The mrml for segmentation and the snapshot showing errors could be sent through mail.</p>

---

## Post #5 by @lassoan (2019-04-26 12:29 UTC)

<aside class="quote no-group" data-username="Anis" data-post="4" data-topic="2424">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/anis/48/3547_2.png" class="avatar"> Anis:</div>
<blockquote>
<p>I am working with Slicer4.9.0.</p>
</blockquote>
</aside>
<p>Use latest stable version (Slicer-4.10.1) or later.</p>
<aside class="quote no-group" data-username="Anis" data-post="4" data-topic="2424">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/anis/48/3547_2.png" class="avatar"> Anis:</div>
<blockquote>
<p>Gmsh which I use for further mesh refinement</p>
</blockquote>
</aside>
<p>You can use SegmentMesher extension to create high-quality multi-material meshes directly in Slicer.</p>
<aside class="quote no-group" data-username="Anis" data-post="4" data-topic="2424">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/anis/48/3547_2.png" class="avatar"> Anis:</div>
<blockquote>
<p>I don’t have dropbox to tranfer files.</p>
</blockquote>
</aside>
<p>You can use any other online storage provider.</p>

---

## Post #6 by @Saima (2019-08-13 02:22 UTC)

<p>Hi Andras,<br>
I want to use gmsh within slicer. The problem I am having is I am unable to view the vtk files generated by using gmsh and meshio.</p>
<p>Also another problem is that I create a surface model node. how can I use this surface model node as input to gmsh. any suggestions?</p>
<p>Also if I use the segment mesher I found it generates a mesh from label maps but the mesh is not refined. thats Why I now jumped to gmsh. Any suggestions?</p>
<p>So I need to now create mesh using surface model nodes generated by slicer and using these surface model nodes to generate the mesh through gmsh. Any suggestions How can I read the surface model node in gmsh</p>
<p>Thanks</p>

---

## Post #7 by @lassoan (2019-08-13 02:45 UTC)

<aside class="quote no-group" data-username="Saima" data-post="6" data-topic="2424">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/9d8465/48.png" class="avatar"> Saima:</div>
<blockquote>
<p>if I use the segment mesher I found it generates a mesh from label maps but the mesh is not refined. thats Why I now jumped to gmsh. Any suggestions?</p>
</blockquote>
</aside>
<p>What do you mean by “not refined”? By default mesh generation is set up to be very quick and generate a course mesh. You can adjust the parameters to preserve all relevant details of the surface mesh.</p>

---

## Post #8 by @Saima (2019-08-13 05:10 UTC)

<p>Sorry I mean fine mesh. How can I get a fine mesh using segment mesher with only one label map.</p>
<p>Thank you</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #9 by @lassoan (2019-08-14 05:16 UTC)

<p>See this tutorial: <a href="https://github.com/lassoan/SlicerSegmentMesher#tutorial" rel="nofollow noopener">https://github.com/lassoan/SlicerSegmentMesher#tutorial</a>. Near the end there is a step to create a finer mesh.</p>

---

## Post #10 by @Saima (2019-08-14 06:44 UTC)

<p>Hi Andras,<br>
I checked with multiple values for scale but it always give me a mesh with some external elements which are not in the label map in segmentation.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/318e5d4b06c72476e93c363eb7dd9c62687f9619.jpeg" data-download-href="/uploads/short-url/74oprGvZzBI3lEsAjQs84bcklsZ.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/318e5d4b06c72476e93c363eb7dd9c62687f9619_2_690x377.jpeg" alt="image" data-base62-sha1="74oprGvZzBI3lEsAjQs84bcklsZ" width="690" height="377" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/318e5d4b06c72476e93c363eb7dd9c62687f9619_2_690x377.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/318e5d4b06c72476e93c363eb7dd9c62687f9619_2_1035x565.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/318e5d4b06c72476e93c363eb7dd9c62687f9619_2_1380x754.jpeg 2x" data-dominant-color="A1A6A5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1051 373 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>For example see in the fig above. the label map is ok but mesh is not ok. why am i getting the mesh like this and not exactly what I needed from the label map of brain.</p>
<p>thank you</p>
<p>any suggestions please</p>

---

## Post #11 by @lassoan (2019-08-14 15:10 UTC)

<p>You can add a box-shaped segment around the brain (e.g., using Scissors effect, with appropriate masking settings). You can then extract sub-meshes by thresholding based on material ID cell scalar.</p>

---
