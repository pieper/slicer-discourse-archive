---
topic_id: 16480
title: "Input For New Extension For Macdonal Tumor Size Measurements"
date: 2021-03-11
url: https://discourse.slicer.org/t/16480
---

# Input for new extension for Macdonal tumor size measurements

**Topic ID**: 16480
**Date**: 2021-03-11
**URL**: https://discourse.slicer.org/t/input-for-new-extension-for-macdonal-tumor-size-measurements/16480

---

## Post #1 by @yannick_s (2021-03-11 14:43 UTC)

<p>Dear Slicer community,</p>
<p>I follow the instructions to create a Slicer extension and ask for your input to avoid overlap or missing already available work.</p>
<p><strong>Motivation</strong><br>
For the current treatment response assessment criteria, e.g., for Glioblastoma, the contrast-enhancing tumor size is assessed by radiologists by measuring the longest diameter on axial slices inside the enhancement. Subsequently, the longest perpendicular diameter to this first one is measured. The product of these two diameters is used as a surrogate for the tumor burden (Macdonald criteria). This two-dimensional metric is highly shape-dependent and sensitive to different head positions across follow-up scans. Tumor volume is currently rarely used due to the time-consuming nature of manual segmentation.</p>
<p>With the success of automated segmentation tools, we hope to move on to fully volumetric evaluation. To validate volumetry, we need to compare our response assessment to previous results obtained by the 2D method and carefully validate progression thresholds.</p>
<p>For a publication we are preparing, I wrote Python code to automate the 2D measurement based on a segmentation and visualize it. Since I used SimpleITK, I hope it would be relatively straightforward to implement a scripted module.</p>
<p><strong>Outline</strong><br>
The user loads a series of images and segmentations. The module should allow an assignment of the image/segmentation pairs to different follow-ups (e.g., similar to the ChangeTracker extension). The automated measurement is performed, changes plotted, and the two perpendicular measurements visualized.</p>
<p>Additionally, I’m thinking about implementing a tool to force perpendicular diameters for manual measurements, since in my experience, the perpendicularity strictness of radiologists’ measurements differs widely.</p>
<p>Here’s an example of how the current pipeline’s output, which I would like to extend and create a Slicer module for.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/15bcfc66905e97c6f8d08d023cbaddc7089326b1.png" alt="Urspeter_FLH_074_1947_FLH_074_1947-20130805-0_1" data-base62-sha1="36iVuSE73bMQYhFHfCvKusoEjSh" width="287" height="411"></p>
<p>Happy to get your thoughts or pointers to existing work <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @lassoan (2021-03-11 15:04 UTC)

<p>Thanks for the heads up. This sounds like a very interesting project.</p>
<p>For optimal reuse of existing features and minimize maintenance burden, I would recommend to consider the followings:</p>
<ul>
<li>Add new segmentation metrics in a new Segment Statistics plugin. Current plugins already compute principal axes, bounding box, oriented bounding box, roundness, flatness, elongation, etc. but I think none of them is exactly “longest diameter on axial slices”</li>
<li>If you implement features related to tracking tumor growth then it would be much better if you could integrate those into the existing ChangeTracker extension.</li>
<li>For implementing measurement with perpendicular axes, you could add a new “Bidimensional” markups. <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> has implemented infrastructure that makes it easy for extensions to define new markup types. We may also do this work directly in Slicer core, as bidimensional measurement is a quite common need. <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> what do you think, would it be better to create a new markup type for this or we could implement it as a new mode for ROI markups.</li>
</ul>

---
