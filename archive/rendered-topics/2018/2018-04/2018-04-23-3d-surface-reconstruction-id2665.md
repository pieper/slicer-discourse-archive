---
topic_id: 2665
title: "3D Surface Reconstruction"
date: 2018-04-23
url: https://discourse.slicer.org/t/2665
---

# 3D surface reconstruction

**Topic ID**: 2665
**Date**: 2018-04-23
**URL**: https://discourse.slicer.org/t/3d-surface-reconstruction/2665

---

## Post #1 by @bedolancer (2018-04-23 13:25 UTC)

<p>Operating system:mac ,windows<br>
Slicer version:4.9<br>
Expected behavior:<br>
hello …id like to ask how to get the brain 3d  surface reconstruction in slicer  with blood vessels in simple way for properative planning</p>
<p>thanks alot</p>

---

## Post #2 by @lassoan (2018-04-23 13:39 UTC)

<p>Slicer tutorials should help you to get started:</p>
<ul>
<li>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Training">https://www.slicer.org/wiki/Documentation/Nightly/Training</a> - especially <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Neurosurgical_Planning_Tutorial">neurosurgical planning tutorial</a>
</li>
<li>
<a href="http://www.slicerigt.org/wp/user-tutorial/">http://www.slicerigt.org/wp/user-tutorial/</a> - U-37 tutorial</li>
</ul>

---

## Post #3 by @bedolancer (2018-04-24 13:02 UTC)

<p>thanks a lot for your reply but actually i tried with the tutorial many times so excuse my little performance …i just ask if it can be explained in simple steps to get image like that attached with the mail…i am neurosurgeon with little bet experience in software …also i hope if there will be any near educational course for 3dslicer</p>
<p>thanks</p>
<p>regards</p>
<p>Ahmed Badry</p>
<p>assistant lecturer of neurosurgery suez canal university ,Egypt</p>
<p>clinical fellow san Raffaele hospital,Milan,Italy</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/2X/4/40b87e276436ea8f8da5acc509909e56424dd638.jpg" data-download-href="/uploads/short-url/9exPAxdlWz9SSPemzRASecOIK36.jpg?dl=1" title="3D Slicer Basso-2628.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/40b87e276436ea8f8da5acc509909e56424dd638_2_690x445.jpg" alt="3D Slicer Basso-2628.png" width="690" height="445" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/40b87e276436ea8f8da5acc509909e56424dd638_2_690x445.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/40b87e276436ea8f8da5acc509909e56424dd638_2_1035x667.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/40b87e276436ea8f8da5acc509909e56424dd638.jpeg 2x" data-dominant-color="AF9480"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3D Slicer Basso-2628.png</span><span class="informations">1335×861 729 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2018-04-25 01:43 UTC)

<p>To get brain surface, you need to get a image where brain surface is clearly visible (such as a T1-weighted image), remove the skull using SwissSkullStripper extension and then extract surface using Segment Editor module’s Threshold effect. To segment vasculature, you need an MR-angio image and probably you can segment vessels by thresholding (maybe followed by Islands effect to remove small speckles in the image; and/or Smoothing effect).</p>
<p>If you can join the upcoming <a href="https://na-mic.github.io/ProjectWeek/PW28_2018_GranCanaria/">Slicer project week in Gran Canaria, Spain</a> then you can get help from a lot of Slicer experts, in person.</p>

---

## Post #5 by @ljc19800331 (2018-10-28 21:16 UTC)

<p>Hello Ahmed,</p>
<p>I am working on the same problem. Did you get this figure from other tutorial in 3D slicer? How is your current progress.</p>
<p>I am actually working on the automatic way of generating the brain cortical surface as well as the blood vessel attached on the surface, but this is a really difficult progress.</p>

---
