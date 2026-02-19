---
topic_id: 4200
title: "How To Implement An Extension With One Hidden Module And One"
date: 2018-09-27
url: https://discourse.slicer.org/t/4200
---

# How to implement an extension with one hidden module and one script module 

**Topic ID**: 4200
**Date**: 2018-09-27
**URL**: https://discourse.slicer.org/t/how-to-implement-an-extension-with-one-hidden-module-and-one-script-module/4200

---

## Post #1 by @Zhiy (2018-09-27 01:31 UTC)

<p>Hi folks,</p>
<p>I am implementing an extension with one script module. But some core functions are written by C++. I plan to have one backend loadable module connect to the script module. Anyone has an idea that I can make the backend loadable module hidden in the extension? By ‘hidden’, I mean when users install my extension, can’t see anything about that module.</p>
<p>Thanks a million,</p>

---

## Post #2 by @cpinter (2018-09-27 03:25 UTC)

<p>I did the exact same thing with GelDosimetryAnalysis:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/SlicerRt/GelDosimetryAnalysis">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerRt/GelDosimetryAnalysis" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/a543d5eeb1e55cb6afc395088952d5cffde39bce9e4b2d1b01b4a6605a2755e3/SlicerRt/GelDosimetryAnalysis" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/SlicerRt/GelDosimetryAnalysis" target="_blank" rel="noopener">GitHub - SlicerRt/GelDosimetryAnalysis: 3D Slicer extension containing a...</a></h3>

  <p>3D Slicer extension containing a slicelet that covers the gel dosimetry analysis workflow used in commissioning new radiation techniques and to validate the accuracy of radiation treatment by enabl...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Zhiy (2018-09-27 13:42 UTC)

<p>Thanks <a class="mention" href="/u/cpinter">@cpinter</a>. That is what I want.</p>

---
