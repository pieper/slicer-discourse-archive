---
topic_id: 14588
title: "A Challenge Named Diaphragm"
date: 2020-11-13
url: https://discourse.slicer.org/t/14588
---

# A challenge named diaphragm

**Topic ID**: 14588
**Date**: 2020-11-13
**URL**: https://discourse.slicer.org/t/a-challenge-named-diaphragm/14588

---

## Post #1 by @luigi_m (2020-11-13 17:03 UTC)

<p>Dear all, I am trying to segment the diaphragm anatomical model from TC files.<br>
As you know, diaphragm is a very complex structure due to its muscular and fibrotic nature, its small thickness and the personal variations.</p>
<p>Moreover, as you can see in the photo attached, in some areas, it is very difficult to distinguish between diaphragm and other structures, such as liver and spleen.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c32414ab108354a3dce547b640937e26a690b85b.jpeg" alt="immagine" data-base62-sha1="rQipnz49WvnGhzeRXcR1h6VqYYz" width="591" height="439"></p>
<p>I have found no topics about diaphragm. Has anyone already tried to segment it, if so how? The radiologist and I are looking for suggestions.</p>
<p>Thank you for your attention,<br>
Luigi</p>

---

## Post #2 by @lassoan (2020-11-13 17:13 UTC)

<p>There have been a few projects that used Slicer for diaphragm segmentation. One of them is nicely written up in this paper:</p>
<aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://www.ncbi.nlm.nih.gov/favicon.ico" class="site-icon" width="16" height="16">
      <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5118562/" target="_blank" rel="noopener">PubMed Central (PMC)</a>
  </header>
  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:128/67;"><img src="https://www.ncbi.nlm.nih.gov/corehtml/pmc/pmcgifs/pmc-logo-share.png" class="thumbnail" width="128" height="67"></div>

<h3><a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5118562/" target="_blank" rel="noopener">Anatomy-based algorithm for automatic segmentation of human diaphragm in...</a></h3>

<p>In-depth understanding of the diaphragm’s anatomy and physiology has been of great interest to the medical community, as it is the most important muscle of the respiratory system. While noncontrast four-dimensional (4-D) computed tomography (CT) ...</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Segmentation and modeling tools have been greatly improved in Slicer since then, so probably many steps are now easier to perform.</p>
<p>What is the goal of the diaphragm segmentation? What kind of analysis you plan to perform? Do you need a volumetric representation (closed surface or labelmap volume) or a thin surface representation (open surface mesh)?</p>

---

## Post #4 by @luigi_m (2020-11-13 17:39 UTC)

<p>Dear Andras,<br>
First of all, thank you for your answer and the paper you linked me, I will read it as soon as possible.</p>
<p>The aim of this work is to study the hiatal hernia, so we are focusing on the area around the esophageal hiatus.</p>
<p>We would like to obtain a volumetric representation, that could be 3D printed, but, if a surface representation would be a lot easier to be done, we could even start with that one and then, maybe, we can try to make a solid using Meshmixer (hoping and checking that the result would not be altered too much).</p>
<p>PS. sorry for the double answer</p>

---

## Post #5 by @lassoan (2020-11-13 18:46 UTC)

<p>Is thickness of the structure is important? If yes, then you need to segment it as a volume. This might be challenging, as the structure is large, thin, and hardly visible. If you are interested only in the shape (and print it with a constant thickness) then you have the option of segmenting surrounding structures and extract their common interface (using Margin effect and Logical operations effect) or defining the diaphragm surface with points and curves.</p>

---

## Post #6 by @luigi_m (2020-11-14 09:57 UTC)

<p>Andras, thanks for your suggestions,<br>
I am afraid that segmenting the diaphragm as a volume for several cases could be a too much time-consuming activity.</p>
<p>I will try to segment its shape. Is there a tool for points and curves? Because i have never used such approach.</p>
<p>It would have been amazing if the algorithm developed by the research you linked me would have been integrated in 3D Slicer… I am thinking to send an email asking for any development.</p>
<p>I will keep you update about this segmentation.<br>
Have a nice weekend!</p>

---
