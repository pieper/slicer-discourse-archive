---
topic_id: 33910
title: "Segmentation Of Composite Materials From Ct Images"
date: 2024-01-22
url: https://discourse.slicer.org/t/33910
---

# Segmentation of composite materials from CT images

**Topic ID**: 33910
**Date**: 2024-01-22
**URL**: https://discourse.slicer.org/t/segmentation-of-composite-materials-from-ct-images/33910

---

## Post #1 by @tueboesen (2024-01-22 15:04 UTC)

<p>I am investigating the tools currently available to view and interactively segment 3D data (made from lots of 2D slices), specifically for material composites from CT data. (So data that typically have a lot of similar features/cells in each image, but often shifted or transformed in some small way. See <a href="https://www.ndt.net/article/ctc2018/papers/ICT2018_paper_id156.pdf" rel="noopener nofollow ugc">https://www.ndt.net/article/ctc2018/papers/ICT2018_paper_id156.pdf</a> for some examples of what materials might look like)</p>
<p>From what I can see there does not seem to be a good extension to easily segment this kind of data in slicer. (Though I could very well be wrong on this and would love to be educated on it if that is the case)</p>
<p>The best segmentation I have thus far found for this kind of job seems to be:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/vedranaa/InSegtpy">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/vedranaa/InSegtpy" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/7c66032810557d58c3f654966927a3e2b41d84376ae6156b16dca4a8dc5a568d/vedranaa/insegtpy" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/vedranaa/InSegtpy" target="_blank" rel="noopener nofollow ugc">GitHub - vedranaa/insegtpy</a></h3>

  <p>Contribute to vedranaa/insegtpy development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
though that tool is more a proof of concept than anything else. (It only runs in 1 thread and the viewer is minimal with a few bugs.)</p>
<p>I am considering taking the above code, optimizing it and turning it into a slicer extension. But before I do anything of that sort I figured I should inquire what the slicer community thinks. Have I missed any tools?, Are there better alternatives I should investigate first?</p>
<p>Disclaimer<br>
I am new to slicer, but have spent a few days playing around with it now and have tested out TomoSAM as well as a few other extensions for segmentation. TomoSAM does not seem ideal for this kind of thing, since you need to segment each individual feature it seems - though it does do a nice job of segmenting the individual feature on a pixel level.</p>
<p>I work for a non-profit called Alexandra Institute and our goal is to educate and develop tools to help danish companies with hard/interesting problems usually by bridging the gap between academia and industry.<br>
So in this particular case, the goal would be to develop an open source interactive segmentation module to make it easier for companies to segment their CT image data of materials. (The 2 example datasets I have for this task both have around 600-700 images each with a resolution of ~4k<em>4k - 5k</em>5k in grayscale, so the data is rather large)</p>

---

## Post #2 by @pieper (2024-01-22 18:09 UTC)

<p>One place to get ideas would be this project on ion-abrasion electron microscopy:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/IASEM" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/Nightly/Extensions/IASEM</a></p>
<p>It hasn’t been active in a while but it had some nice tools that may still be useful.</p>

---
