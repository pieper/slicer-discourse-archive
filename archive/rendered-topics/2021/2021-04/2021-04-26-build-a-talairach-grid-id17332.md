---
topic_id: 17332
title: "Build A Talairach Grid"
date: 2021-04-26
url: https://discourse.slicer.org/t/17332
---

# Build a Talairach grid

**Topic ID**: 17332
**Date**: 2021-04-26
**URL**: https://discourse.slicer.org/t/build-a-talairach-grid/17332

---

## Post #1 by @matthieufaillot (2021-04-26 14:02 UTC)

<p>Operating system:  Windows 10<br>
Slicer version: 4.10.2<br>
Expected behavior: overlay a Talairach grid system over a CT/MRI 3D volume<br>
Actual behavior: none</p>
<p>Hello,<br>
I would like to create a talairach grid model such as performed in this software ( <a href="https://support.brainvoyager.com/available-tools/49-available-plugins/166-nifti-conversion-volumetric-files.html" class="inline-onebox" rel="noopener nofollow ugc">Users Guide - Manual ACPC and Talairach Transformation - Support BrainVoyager</a>) or in this publication (<a href="https://www.researchgate.net/publication/228464568_Multimodality_image_quantification_using_Talairach_grid" rel="noopener nofollow ugc">https://www.researchgate.net/publication/228464568_Multimodality_image_quantification_using_Talairach_grid</a>).<br>
Input would be a 3D CT/MRI brain volume after aligned it to the AC/PC plane without any deformation. User would need to input specific points :  brain most anterior point, brain most posterior point, most lateral point leftward, most lateral point rightward, most superior point, and temporal most inferior point.<br>
Output : would be the same volume and overlay of a proportional talairach grid where the brain is divided in 12x8 boxes.<br>
Final goal is to be able to segment brain lesions (eg hemorrhage) on CT-scan and report results as a statistical map in a 3D Talairach grid (there was x number of lesions in a specific box of the coordinate system).</p>
<p>Although far less precise than atlas strategies based on normalization in the MNI space, this would allow to map lesions from an individual CT scan to the Talairach atlas where each box of the Talairach grid system corresponds to specific neuroanatomical structures. As a neurosurgeon,  I think this would have immediate applications in clinical practice to work with data from CT scan which remains the most used imaging modality, especially in the context of emergency</p>
<p>I think this issue is close to these ones (<span class="hashtag">#3525</span>, <span class="hashtag">#6205</span>) but I couldn’t find an answer.</p>
<p>I don’t know if this can be done using existing modules, willing to contribute to a new module if necessary but would need some guidance</p>
<p>Thank you for your help<br>
Best regards<br>
Matthieu</p>

---

## Post #2 by @lassoan (2021-04-26 21:45 UTC)

<p>Is the current can ACPC transform module sufficient or you would need something different or more?</p>
<p>Unfortunately, the ACPC module is implemented in C++, so to modify it you need to build Slicer. Alternatively, you can create a new very simple Python scripted module.</p>

---

## Post #3 by @matthieufaillot (2021-04-27 08:20 UTC)

<p>No unfortunately the ACPC module doesn’t allow to draw a grid.</p>
<p><a class="mention" href="/u/fernando">@Fernando</a>  posted a python script to perform the AC/PC alignment in this thread (<a href="https://discourse.slicer.org/t/acpc-transform-question/3525" class="inline-onebox">ACPC transform question</a>)</p>
<p>Maybe there is a possibility to build on this.</p>
<p>Best regards</p>
<p>Matthieu</p>

---

## Post #4 by @lassoan (2021-04-27 18:58 UTC)

<p>The ACPC module is slightly more sophisticated (it uses principal component analysis to get midsagittal plane, has multiple operating modes, etc.) but I agree that the Python script linked above can be a good start for the module logic.</p>
<p>I would recommend to create a simple Python scripted module by following the <a href="https://github.com/PerkLab/PerkLabBootcamp/blob/master/Doc/day3_2_SlicerProgramming.pptx">PerkLab Bootcamp Slicer programming tutorial</a>. This year we do the bootcamp online, so if you have time you can probably join in (see details <a href="https://github.com/PerkLab/PerkLabBootcamp">here</a>).</p>

---

## Post #5 by @matthieufaillot (2021-04-28 17:38 UTC)

<p>Thank you ++ I registered</p>

---

## Post #6 by @Fernando (2021-06-01 15:24 UTC)

<p><a class="mention" href="/u/matthieufaillot">@matthieufaillot</a>, let me know if you need more context about the code I shared. <a class="mention" href="/u/sarafv">@sarafv</a> could probably help as well.</p>

---

## Post #7 by @matthieufaillot (2021-12-01 04:59 UTC)

<p>Hello,<br>
I am still trying to build a tridimensional grid with unevenly spaced cells (rectilinear grid) that I want to overlay on a tridimensional medical image (eg. brain MR, brain CT scan). My ultimate goal is to be able to use this grid to compute the presence or absence of a structure/lesion in each cell of the grid ( and then be able to produce statistical maps when average the grids of multiple subjects).<br>
In order to define the coordinates of each axis, I manually created markups fiducials on one coronal slice, on one axial slice, and one sagittal slice.<br>
Then I created a vtk rectilinear grid based on the coordinates of these markups fiducials.<br>
However I cannot display the vtk rectilinear grid as a node ( I cannot use slicer.modules.models.logic().AddModel() because the vtk rectilinear grid object doesn’t have outputs).<br>
Is it possible to convert the rectilinear grid to a an unstructured grid or a polydata object and then create the node from the unstructured grid/polydata object ?<br>
Is there a better solution ?<br>
Thank you for your help</p>

---

## Post #8 by @lassoan (2021-12-19 20:16 UTC)

<p>Most likely this is very easy to do by a few line of Python script, but I’m not sure what exactly you mean by a “tridimensional grid with unevenly spaced cells”. Could you draw a sketch or add a link to publications that describe what you want to do with more details and examples?</p>

---

## Post #9 by @vandg (2025-07-11 06:56 UTC)

<p>I guess something like this..</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a8d162b0149aeb586c2ff116d138ae938ada59f8.jpeg" data-download-href="/uploads/short-url/o5qOVsiZBkvlHtGVbbO58fzzUmc.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a8d162b0149aeb586c2ff116d138ae938ada59f8_2_341x500.jpeg" alt="image" data-base62-sha1="o5qOVsiZBkvlHtGVbbO58fzzUmc" width="341" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a8d162b0149aeb586c2ff116d138ae938ada59f8_2_341x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a8d162b0149aeb586c2ff116d138ae938ada59f8_2_511x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a8d162b0149aeb586c2ff116d138ae938ada59f8_2_682x1000.jpeg 2x" data-dominant-color="949D7A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">683×1000 106 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @Fernando (2025-07-11 06:58 UTC)

<p><a class="mention" href="/u/vandg">@vandg</a>, could you please share the code for that?</p>

---

## Post #11 by @vandg (2025-07-11 07:41 UTC)

<p>Its not ready (work in progress..).<br>
Proof of concept phase <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=14" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>What’s currently missing in the SEEG community is a clear and straightforward implementation of the original Talairach framework. Many recent developments seem to drift away from its core ideas, rather than building upon them.<br>
3D Slicer is already a powerful platform for SEEG implantation planning, it just needs a few more key features to fully realize this potential.<br>
I am trying to figure out how to do it best…</p>

---
