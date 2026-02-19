---
topic_id: 1022
title: "How To Align Segments To Each Other"
date: 2017-09-07
url: https://discourse.slicer.org/t/1022
---

# How to align segments to each other

**Topic ID**: 1022
**Date**: 2017-09-07
**URL**: https://discourse.slicer.org/t/how-to-align-segments-to-each-other/1022

---

## Post #1 by @Hanaana (2017-09-07 14:54 UTC)

<p>Hello everyone!!</p>
<p>Im trying to make some anatomical landmarks coordinates to my femur bone<br>
but in module registration i couldnt pick the fixed volume nor the moving<br>
volume.</p>
<p>Am i doing it wrong ?!  this is the information i found about registration<br>
while reading about the landmark registration module :<br>
<a href="https://www.slicer.org/wiki/Documentation/4.4/Modules/LandmarkRegistration" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.slicer.org/wiki/Documentation/4.4/Modules/LandmarkRegistration</a></p>
<p>Am i choosing the wrong module ?! or am i doing it wrongly ?! Please<br>
someone to help with this issue</p>
<p>Hanaa<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/07e028a022a93c115b9178952c2171cd388c411f.jpg" data-download-href="/uploads/short-url/17FBcHCFBOhfxEuMQQtQENqpXPx.jpg?dl=1" title="Screen Shot 2017-09-06 at 17.08.38 (2).jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/07e028a022a93c115b9178952c2171cd388c411f_2_625x500.jpg" width="625" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/07e028a022a93c115b9178952c2171cd388c411f_2_625x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/07e028a022a93c115b9178952c2171cd388c411f_2_937x750.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/07e028a022a93c115b9178952c2171cd388c411f_2_1250x1000.jpg 2x" data-dominant-color="B5B2C7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2017-09-06 at 17.08.38 (2).jpg</span><span class="informations">1280×1024 349 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2017-09-08 13:38 UTC)

<p>Landmark registration module in Slicer core is mainly intended for images. Install SlicerIGT extension and use <code>Fiducial Registration Wizard</code> module to align any kind of structures by dropping markup fiducials on corresponding landmarks in slice or 3D views. See U12 and U13 in <a href="http://www.slicerigt.org/wp/user-tutorial/">SlicerIGT tutorials</a>. If you need a model node instead of a segment, you can export your segmentation to model in the Segmentations module.</p>

---

## Post #3 by @Hanaana (2017-09-08 15:09 UTC)

<p>Hello Professor,</p>
<p>Thank you for the continous support . For some reasons i cannot open the<br>
link to download the SlicerIGT extension •<a href="http://192.168.1.240" rel="nofollow noopener">http://192.168.1.240</a>  Can you<br>
please help me with this issue!!</p>
<p>Hanaa</p>

---

## Post #4 by @Hanaana (2017-09-08 15:46 UTC)

<p>Hello Professor,</p>
<p>I have solved it. I could download it directly from Extension manager.</p>
<p>Thank you,</p>
<p>Hanaa</p>

---

## Post #5 by @deepmech (2017-09-09 04:04 UTC)

<p>hello hanaa , are you working on femur bone?<br>
can you send me the .stl or .iges  file of femur?(<a href="mailto:deepmech.maurya@gmail.com">deepmech.maurya@gmail.com</a>)<br>
i am working on sacrum and pelvic region to find out the high stresses area but …<br>
till now i am not able to convert .stl file to .iges file which can open in any FINITE Element software.</p>

---

## Post #6 by @lassoan (2017-09-11 02:31 UTC)

<p>STL is a surface mesh file format, so unless you use a shell model, it won’t be usable for FEA. You usually need to create a volumetric mesh. See more details in this post: <a href="https://discourse.slicer.org/t/usage-of-volumetric-meshes/620">Usage of volumetric meshes</a></p>

---
