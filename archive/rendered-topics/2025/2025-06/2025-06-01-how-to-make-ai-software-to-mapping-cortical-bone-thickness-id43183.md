---
topic_id: 43183
title: "How To Make Ai Software To Mapping Cortical Bone Thickness"
date: 2025-06-01
url: https://discourse.slicer.org/t/43183
---

# How to make AI software to mapping cortical bone thickness

**Topic ID**: 43183
**Date**: 2025-06-01
**URL**: https://discourse.slicer.org/t/how-to-make-ai-software-to-mapping-cortical-bone-thickness/43183

---

## Post #1 by @EsraaIsmail95 (2025-06-01 18:37 UTC)

<p>Hello, I am a dentist and new user in this amazing software<br>
I want to make a artificial intelligence for mapping of cortical bone thickness<br>
Actually it is my thesis and this will be my research work for my master degree, I am lost and I dont konw how to strat<br>
I know segmentation of bone is the first step, okay what next<br>
How to determine every single point as thickness in DICOM file , It is impossible to make all of them manually<br>
will I have to segment cortical bone only or cortical bone with spongy bone?<br>
what if I convert dicom file into jpg ?<br>
I need your help please<br>
NB the DICOM file from CBCT not CT</p>

---

## Post #2 by @lassoan (2025-06-02 00:54 UTC)

<p>To measure cortical bone thickness, first segment the cortical bone (not the spongy cancellous bone). You can then proceed with measuring the bone thickness with one of the methods described in this topic:</p>
<aside class="quote quote-modified" data-post="2" data-topic="2735">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-to-analyze-the-thickness-of-the-model/2735/2">How to analyze the thickness of the model</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    “Thickness” is not a very well defined term for models (surface meshes), but for shell-like meshes it is probably not too difficult to estimate it robustly and accurately. 
Potential approaches: 
A. Extract medial surface and estimate thickness as 2x of distance from medial surface. There are various ways of computing these in Slicer. One possible workflow: 

Compute medial surface using Simple Filters module - BinaryThinningImageFilter.
Compute distance map using Simple Filters module - Daniels…
  </blockquote>
</aside>


---
