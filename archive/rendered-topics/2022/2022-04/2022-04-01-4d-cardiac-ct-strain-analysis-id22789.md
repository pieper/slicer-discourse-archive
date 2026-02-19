---
topic_id: 22789
title: "4D Cardiac Ct Strain Analysis"
date: 2022-04-01
url: https://discourse.slicer.org/t/22789
---

# 4D cardiac CT Strain analysis

**Topic ID**: 22789
**Date**: 2022-04-01
**URL**: https://discourse.slicer.org/t/4d-cardiac-ct-strain-analysis/22789

---

## Post #1 by @xiaolin (2022-04-01 10:59 UTC)

<p>Hi everyone,</p>
<p>I’m a medical student and doing 4D segmentation on 3D Slicer now, and the segmentation is really good.<br>
And I gonna proceed to the next step–the Strain analysis. There is a paper–CardIAc: an open-source application for myocardial strain analysis which shows the good analysis from 3D Silcer. But I cannot find “CardIAc” extension.<br>
Does anyone know this extension and please provide some information how can I find it in the Extension Manager.<br>
My system: Mac, 3D Slicer: Version 4.13.0</p>
<p>Thanks a lot and have a nice weekend in advance.</p>
<p>Xiaolin Sun</p>

---

## Post #2 by @pieper (2022-04-01 11:49 UTC)

<p>i suppose you mean this paper:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://pubmed.ncbi.nlm.nih.gov/33196972/">
  <header class="source">
      <img src="https://cdn.ncbi.nlm.nih.gov/coreutils/nwds/img/favicons/favicon.ico" class="site-icon" width="64" height="64">

      <a href="https://pubmed.ncbi.nlm.nih.gov/33196972/" target="_blank" rel="noopener">PubMed</a>
  </header>

  <article class="onebox-body">
    <img src="https://cdn.ncbi.nlm.nih.gov/pubmed/persistent/pubmed-meta-image.png" class="thumbnail onebox-avatar" width="500" height="500">

<h3><a href="https://pubmed.ncbi.nlm.nih.gov/33196972/" target="_blank" rel="noopener">CardIAc: an open-source application for myocardial strain analysis - PubMed</a></h3>

  <p>This paper introduces a new open-source application for strain analysis distributed under a BSD-style open-source license. Results demonstrate the capability and merits of the proposed application for strain analysis.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>As far as I know it hasn’t been submitted to the extension index yet.  I suggest contacting the authors to check on the status.</p>

---

## Post #3 by @lassoan (2022-04-02 01:20 UTC)

<p>If the authors don’t respond for very long time then you can do the computations with a little bit of Python scripting. You can get the displacement field from the transform node and use <a href="https://pypi.org/project/itk-strain/">ITK-strain Python package</a> to compute the strain. You can use the strain to color segmented surfaces (using <code>Probe volume with model</code> module) or compute statistics in selected image regions (using <code>Segment Statistics</code> module).</p>

---

## Post #4 by @Gening_Dong (2022-04-18 21:28 UTC)

<p>Hi, I want to calculate strain tensor as well. I found an example <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#export-the-displacement-magnitude-of-the-transform-as-a-volume" rel="noopener nofollow ugc">here</a>. However, I only want the displacement field in the segmentation/model, but not the whole volume. Can I transfer a segmentation into a new volume so that I can export the displacement magnitude of the transform as a volume and visualize it?</p>

---

## Post #5 by @lassoan (2022-04-25 13:20 UTC)

<p>I’ve replied here:</p>
<aside class="quote quote-modified" data-post="20" data-topic="22913">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gening_dong/48/14706_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/export-heart-motion-to-cfd-fsi/22913/20">Export heart motion to CFD/FSI</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi <a class="mention" href="/u/lassoan">@lassoan</a> , thanks for your help with the position extracting. However I met another problem right now: I want to calculate strain tensor of the boundary. I read your suggestion <a href="https://discourse.slicer.org/t/4d-cardiac-ct-strain-analysis/22789/3">here</a> so I’m trying to export the displacement field. 
I found an example for extracting displacement field <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#export-the-displacement-magnitude-of-the-transform-as-a-volume" rel="noopener nofollow ugc">here</a>. However, I only want the displacement field in the segmentation/model, but not the entire volume. Can I transfer a segmentation into a new volume so that I can export the displacement magnitude of the transf…
  </blockquote>
</aside>

<p>Please continue the discussion there.</p>

---

## Post #6 by @whu (2023-03-10 05:25 UTC)

<p>Is there any new words about the CardIAc according to he publication list ?<br>
thanks.</p>

---
