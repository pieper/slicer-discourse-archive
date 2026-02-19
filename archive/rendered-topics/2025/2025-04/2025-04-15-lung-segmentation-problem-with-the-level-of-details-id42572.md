---
topic_id: 42572
title: "Lung Segmentation Problem With The Level Of Details"
date: 2025-04-15
url: https://discourse.slicer.org/t/42572
---

# Lung Segmentation Problem with the level of details

**Topic ID**: 42572
**Date**: 2025-04-15
**URL**: https://discourse.slicer.org/t/lung-segmentation-problem-with-the-level-of-details/42572

---

## Post #1 by @yayale (2025-04-15 10:34 UTC)

<p>I have a CT scan dataset and I am trying to segment the airways.<br>
I am using Lung CT Segmenter module, with high details I get leaks, I decreased the level of details until reaching low details, where the airways are not appearing anymore (only lungs were segmented).<br>
Anyone knowing the reason ? Even the trachea is not appearing at this level.<br>
Tried to check the documentation for this module, but unfortunately only the whole code is available.<br>
So the case is either I get leaks (high details down to medium low detail), or no airways at all (for low detail option).</p>

---

## Post #2 by @rbumm (2025-04-29 11:32 UTC)

<p>The documentation including some video links are here:  <a href="https://github.com/Slicer/SlicerLungCTAnalyzer" class="inline-onebox" rel="noopener nofollow ugc">GitHub - Slicer/SlicerLungCTAnalyzer: This is a 3D Slicer extension for segmentation and spatial reconstruction of infiltrated, collapsed, and emphysematous areas in lung CT.</a></p>
<p>A recent paper describung th methods is here<a href="https://jtd.amegroups.org/article/view/83536/html" rel="noopener nofollow ugc">https://jtd.amegroups.org/article/view/83536/html</a></p>
<p>This is what I get with airway segmentation “medium/low” details in Slicer 5.8.1</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d7433b8ec495fa53a6b6911200e297e589e80320.png" data-download-href="/uploads/short-url/uIiHui8Krug3cFIeoIL6gAgF1ok.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d7433b8ec495fa53a6b6911200e297e589e80320.png" alt="image" data-base62-sha1="uIiHui8Krug3cFIeoIL6gAgF1ok" width="590" height="124"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">590×124 3.09 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/44537b648aab5dcf7663ba0e8db687b2d615a92c.png" data-download-href="/uploads/short-url/9KrkimiKnipu2a26tV7U0DGYvZa.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/44537b648aab5dcf7663ba0e8db687b2d615a92c_2_616x499.png" alt="image" data-base62-sha1="9KrkimiKnipu2a26tV7U0DGYvZa" width="616" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/44537b648aab5dcf7663ba0e8db687b2d615a92c_2_616x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/44537b648aab5dcf7663ba0e8db687b2d615a92c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/44537b648aab5dcf7663ba0e8db687b2d615a92c.png 2x" data-dominant-color="9C9ED3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">708×574 35.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
