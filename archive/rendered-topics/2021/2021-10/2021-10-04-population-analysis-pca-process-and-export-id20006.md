---
topic_id: 20006
title: "Population Analysis Pca Process And Export"
date: 2021-10-04
url: https://discourse.slicer.org/t/20006
---

# Population Analysis PCA Process and Export

**Topic ID**: 20006
**Date**: 2021-10-04
**URL**: https://discourse.slicer.org/t/population-analysis-pca-process-and-export/20006

---

## Post #1 by @mhertz (2021-10-04 22:47 UTC)

<p>Hello everyone, I have been having some trouble using the Population Analysis function in SlicerSALT. I have been following <a href="https://docs.google.com/presentation/d/1CfFPKFMA3KtlOJY5hpdZ_HACavoSIsVxpnThNIuYhZE/present?slide=id.p1" rel="noopener nofollow ugc">this</a> tutorial, but am stuck at Step 3, generating the PCA model. I’ve uploaded the VTK files and generated the CSV describing the groups, but when I go to select the CSV under “selection of groups” in the PCA section and press “Process and Export”, nothing happens. Any help in resolving this issue would be much appreciated.</p>
<p>I’m primarily using this tool to superimpose my 3D data to create a mean shape model for morphometric analysis. If anyone knows another way to create a mean shape model from multiple surface scans that alternative would also be great! Thanks very much.</p>

---

## Post #2 by @muratmaga (2021-10-04 22:51 UTC)

<p>If you have fixed/anatomical landmarks, you can create a mean shape model in SlicerMorph. (<a href="https://github.com/SlicerMorph/SlicerMorph" class="inline-onebox" rel="noopener nofollow ugc">GitHub - SlicerMorph/SlicerMorph: Extensions to conduct 3D morphometrics in Slicer</a>)</p>

---

## Post #3 by @mhertz (2021-10-04 23:01 UTC)

<p>Hi, thanks <a class="mention" href="/u/muratmaga">@muratmaga</a> for the idea. My issue is that I’m trying to do morphometrics on 3d surface scans of humans, focusing on the arms and legs, where there are not established and well-defined anatomical landmarks. I found a few interesting articles about landmarkless approaches of analysis, but the first step was creating a prototype (mean/average) model to then sequentially compare the dataset to.</p>
<p>These are what I’ve been drawing inspiration from:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0150368">
  <header class="source">
      <img src="https://journals.plos.org/resource/img/favicon.ico" class="site-icon" width="48" height="48">

      <a href="https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0150368" target="_blank" rel="noopener nofollow ugc">journals.plos.org</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:320/261;"><img src="https://journals.plos.org/plosone/article/figure/image?id=10.1371/journal.pone.0150368.g011&amp;size=inline" class="thumbnail" width="320" height="261"></div>

<h3><a href="https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0150368" target="_blank" rel="noopener nofollow ugc">A Landmark-Free Method for Three-Dimensional Shape Analysis</a></h3>

  <p>Background The tools and techniques used in morphometrics have always aimed to transform the physical shape of an object into a concise set of numerical data for mathematical analysis. The advent of landmark-based morphometrics opened new avenues of...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://www.sciencedirect.com/science/article/abs/pii/S1077314205000858">
  <header class="source">
      <img src="https://sdfestaticassets-us-east-1.sciencedirectassets.com/shared-assets/13/images/favSD.ico" class="site-icon" width="16" height="16">

      <a href="https://www.sciencedirect.com/science/article/abs/pii/S1077314205000858" target="_blank" rel="noopener nofollow ugc">sciencedirect.com</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:112/150;"><img src="https://ars.els-cdn.com/content/image/1-s2.0-S1077314205X01254-cov150h.gif" class="thumbnail" width="112" height="150"></div>

<h3><a href="https://www.sciencedirect.com/science/article/abs/pii/S1077314205000858" target="_blank" rel="noopener nofollow ugc">Joint registration and averaging of multiple 3D anatomical surface models</a></h3>

  <p>In biological imaging, three-dimensional (3D) reconstruction from serial sections is a powerful technique that produces graphical surface models of an…</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Would you happen to know anything about that?</p>

---

## Post #4 by @muratmaga (2021-10-04 23:20 UTC)

<p>There is a method we are working on, which as a by-product can facilitate generation of such population averages. But that’s unfortunately couple months away.</p>
<p>Meanwhile, you can take one representative sample, run it through PseudoLMGenerator in SlicerMorph, and then use ALPACA to transfer points to other samples. If the resultant transfer is sufficiently good, you can take those points and run through GPA module to obtain a mean shape model.</p>
<p>This is all available through SLicerMorph.</p>

---
