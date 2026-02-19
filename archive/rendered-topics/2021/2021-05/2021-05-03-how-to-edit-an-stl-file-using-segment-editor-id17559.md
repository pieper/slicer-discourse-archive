---
topic_id: 17559
title: "How To Edit An Stl File Using Segment Editor"
date: 2021-05-03
url: https://discourse.slicer.org/t/17559
---

# How to edit an STL file using Segment Editor

**Topic ID**: 17559
**Date**: 2021-05-03
**URL**: https://discourse.slicer.org/t/how-to-edit-an-stl-file-using-segment-editor/17559

---

## Post #1 by @Hamid (2021-05-03 20:20 UTC)

<p>I want to do some modifications on my stl file. when I open it from file as a data the “Segment Editor” is NOT active. How may I do that?</p>

---

## Post #2 by @lassoan (2021-05-11 04:54 UTC)

<p>See step-by-step instructions in <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#import-an-existing-segmentation-from-model-surface-mesh-file">Segmentations module documentation</a> (see the tip at the end of the section on how to create a master volume if you don’t have one).</p>

---

## Post #3 by @Hamid (2021-05-12 03:40 UTC)

<p>Great! It works now. Thanks a lot.</p>

---

## Post #4 by @Hamid (2021-05-14 17:54 UTC)

<p>I load the stl file and after specifying the geometry I tried to modify the stl file using Draw tube effect. when I click on Draw tube effect a message shows up that says:“<strong>change master representation to binary labelmap</strong>”. if say YES,the files quality changes like<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/cad3c1d617397271054887cb18ae92358be103a5.jpeg" data-download-href="/uploads/short-url/sWi8tp1TA3COwLPR06pkzpYGuO1.jpeg?dl=1" title="before-after" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cad3c1d617397271054887cb18ae92358be103a5_2_690x332.jpeg" alt="before-after" data-base62-sha1="sWi8tp1TA3COwLPR06pkzpYGuO1" width="690" height="332" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cad3c1d617397271054887cb18ae92358be103a5_2_690x332.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cad3c1d617397271054887cb18ae92358be103a5_2_1035x498.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/cad3c1d617397271054887cb18ae92358be103a5.jpeg 2x" data-dominant-color="828EAA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">before-after</span><span class="informations">1352×652 76.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
attached screenshot. what would be the solution for this?<br>
The barbed fitting beforehand  is added to the stl file in solidworks.(FYI)<br>
Many thanks</p>

---

## Post #5 by @lassoan (2021-05-14 18:01 UTC)

<p>This is looks good. The resolution you choose determines what details are preserved. If it is not feasible to use a resolution that preserves all the details you need (e.g., because your segmentation is large and your computer could not handle a very fine resolution labelmap of that size) then you can combine image-derived meshes with CAD parts by Boolean mesh operations, using Combine Models module (in Sandbox extension).</p>

---

## Post #6 by @Hamid (2021-05-14 19:54 UTC)

<p>Thanks for quick reply. This quality does not work for my case because the tube should be fitted to the fitting barbed that you see in the screen shot and this one will end up with a leakage.<br>
How may I change the resolution?<br>
Does the image spacing change the mentioned quality? for my case the image spacing is 1mm along each axes. What happened if I change it e.g to 0.1mm?</p>

---

## Post #7 by @lassoan (2021-05-14 20:49 UTC)

<p>Spacing of the binary labelmap representation of the segmentation directly determines “quality”, i.e., size of the smallest details that can be preserved. Typical spacing is between few tenths of a millimeter to a few millimeters - consistent with spacing of the input images. However, if you need fitting between mechanical parts then you would need to work with 1-2 magnitudes smaller spacing along each axis, which would mean that you would have 3-6 magnitudes more voxels in the labelmap. Working with such large labelmaps (tens of GBs in size) is often not practically feasible, so if you need to combine pieces from image-driven segmentations with CAD parts, I would recommend to export the segmentation to models and then combine them with CAD-designed meshes using Combine models module.</p>

---

## Post #8 by @Hamid (2021-12-08 18:07 UTC)

<p>When I load data (.stl model) into Slicer there are three options(segmentation-model-volume). If I choose model and load it, is there any way to modify the model? e.g cutting a part of it?<br>
Thanks</p>

---

## Post #9 by @mikebind (2021-12-08 18:23 UTC)

<p>Look at the Dynamic Modeler module, which provides tools for manipulation of surface models, including cutting.</p>

---

## Post #10 by @Hamid (2021-12-10 23:11 UTC)

<p>Thank you Mike. it works for cutting. Is there any option to fill holes ,…etc there?</p>

---

## Post #11 by @mikebind (2021-12-10 23:34 UTC)

<p>The Surface Toolbox module has a variety of processing options oriented towards cleaning up and optimizing model meshes.  One of the options there is “Fill Holes”, which might accomplish what you want (I don’t have experience with using that tool, so I’m not sure how it goes about filling holes).</p>
<p>Depending on what manipulations you want to do, you might have an easier time loading your stl as a segmentation and editing it using the Segment Editor tools.  Then you can convert back to a surface representation after editing.</p>

---

## Post #12 by @Hamid (2022-10-31 20:19 UTC)

<p>Hello,<br>
How can I use painting option with stl file?segment editor is inactive when open a stl file</p>

---

## Post #13 by @muratmaga (2022-10-31 23:37 UTC)

<p>Right click on the stl object in the Data module and choose “convert model to Segmentation node”</p>

---

## Post #14 by @Hamid (2022-11-01 03:32 UTC)

<p>Perfect! Thank you so much Muratmaga</p>

---
