---
topic_id: 28578
title: "Files Formats For Gpa"
date: 2023-03-26
url: https://discourse.slicer.org/t/28578
---

# files formats for GPA

**Topic ID**: 28578
**Date**: 2023-03-26
**URL**: https://discourse.slicer.org/t/files-formats-for-gpa/28578

---

## Post #1 by @Norbert1 (2023-03-26 02:54 UTC)

<p>As a retired physician, I am involved in maritime ethnography. One of my projects involves comparing the hull shapes of traditional Arab ships.<br>
For this I would like to perform a GPA using the Slicer Morph app. However, so far I have not been able to import my 3 D data in *.obj format into the app, I always get an error message. Which file formats can Slicer Morph work with?</p>

---

## Post #2 by @muratmaga (2023-03-26 04:58 UTC)

<p>GPA (generalized Procrustes analysis) expects landmark coordinates as input, either in fcsv or JSON format.</p>
<p>OBJ is a format for 3d surface models. You need to annotate some landmarks on these models to use GPA.</p>
<p>Please see our tutorials at:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/slicermorph/tutorials">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/slicermorph/tutorials" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/895608e967969743c7cdace52a1f3270ec1678a95eebd0d28a3a6be1f314f734/SlicerMorph/Tutorials" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/slicermorph/tutorials" target="_blank" rel="noopener">GitHub - SlicerMorph/Tutorials: SlicerMorph module tutorials</a></h3>

  <p>SlicerMorph module tutorials. Contribute to SlicerMorph/Tutorials development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Norbert1 (2023-03-27 17:36 UTC)

<p>Dear Murat,<br>
thank you very much for your reply. I will browse through the tutorials<br>
Norbert</p>

---
