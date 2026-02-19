---
topic_id: 19235
title: "Craniofacial Voxel Analysis"
date: 2021-08-17
url: https://discourse.slicer.org/t/19235
---

# Craniofacial Voxel Analysis

**Topic ID**: 19235
**Date**: 2021-08-17
**URL**: https://discourse.slicer.org/t/craniofacial-voxel-analysis/19235

---

## Post #1 by @Jose_Tomas_Ahumada_S (2021-08-17 15:43 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.11.2021</p>
<p>Hello, I’m a relative new user of Slicer and I need to do a Cranio-facial voxel analysis, but I really don’t know how to do it (until the moment I know how to load the DICOM or TIFF data, do the segmentation and create the 3D model).</p>
<p>I explain myself, I want to compare two different skulls (WT vs Mutant) doing a voxel comparition analysis of the skulls, so I can see what are the differences between them (form, shape, what zone is bigger or smaller, etc).</p>
<p>Is this possible with Slicer??</p>
<p>Thank you so much for your help,<br>
I hope someone can help me</p>

---

## Post #2 by @muratmaga (2021-08-17 16:53 UTC)

<p>To use voxel based analyses, you need to normalize and register your images into a common reference frame (usually a template), obtain deformation fields from registration, calculate the jacobian determinants of deformation fields and apply T-test (with permutation) to calculate the significance of results, which you can present as a heatmap of voxel shrinkage/expansion.</p>
<p>All the raw components to do this in Slicer is available, but you will have to write your own functions for statistical analyses. Instead, I would suggest you use ANTsX platform [1] (either in R as ANTsR, or in Python as AntsPy) and do all your stats, and then bring the results to Slicer for visualization.</p>
<p>Note that results of this approach is highly dependent on the template and the registration parameters you choose. If you want to start small and if you can rely on landmarks, you can do a landmark-based shape analysis of data in SlicerMorph [2]. While we do not support groupwise analysis, it is fairly easy to do so in R (or even SlicerSalt [3] I would imagine), once you have your landmarks.</p>
<p>[1] <a href="https://www.nature.com/articles/s41598-021-87564-6" class="inline-onebox" rel="noopener nofollow ugc">The ANTsX ecosystem for quantitative biological and medical imaging | Scientific Reports</a><br>
[2] <a href="https://github.com/SlicerMorph/SlicerMorph/" class="inline-onebox" rel="noopener nofollow ugc">GitHub - SlicerMorph/SlicerMorph: Extensions to conduct 3D morphometrics in Slicer</a><br>
[3] <a href="http://salt.slicer.org/" rel="noopener nofollow ugc">http://salt.slicer.org/</a></p>

---

## Post #3 by @lassoan (2021-08-17 20:31 UTC)

<p>ANTs has been also added recently to Slicer as an extension: <a href="https://github.com/simonoxen/SlicerANTs">SlicerANTs</a>.</p>
<p>You probably want to align the images rigidly first (using simple landmark registration or automated image registration), harden the transform, and then compute a displacement field using a warping transform.</p>

---

## Post #4 by @Jose_Tomas_Ahumada_S (2021-08-23 09:01 UTC)

<p>Thank you so much for your help, I will try to follow your advice</p>
<p>Regards</p>

---

## Post #5 by @Jose_Tomas_Ahumada_S (2021-08-24 12:59 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="19235">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>rden the transform, an</p>
</blockquote>
</aside>
<p>Hello again, I can’t found the extension SlicerANTs in the extension manager, is not longer available?<br>
Thanks</p>

---

## Post #6 by @jamesobutler (2021-08-24 13:29 UTC)

<p>SlicerAnts is currently only available for the latest Slicer Preview and is not available for latest Slicer Stable.</p>

---
