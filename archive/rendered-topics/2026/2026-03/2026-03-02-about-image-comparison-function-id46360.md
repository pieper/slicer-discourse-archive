---
topic_id: 46360
title: "About Image Comparison Function"
date: 2026-03-02
url: https://discourse.slicer.org/t/46360
---

# About image comparison function

**Topic ID**: 46360
**Date**: 2026-03-02
**URL**: https://discourse.slicer.org/t/about-image-comparison-function/46360

---

## Post #1 by @ZhouMo (2026-03-02 18:34 UTC)

<p><span lang="EN-GB">Hello all,</span></p>
<p><span lang="EN-GB">I am a new user of 3D slicer. Currently, I want to achieve the image comparison function, which means I hope to be able to open two images simultaneously (such as CT images of the same patient at different time points) for comparison. However, I haven’t found a way to implement this in the software yet. Could this function be implemented? If possible, could it be achieved to align and synchronize the positions of multiple images?</span></p>
<p><span lang="EN-GB">Thank you for your help and advice.</span></p>

---

## Post #2 by @jamesobutler (2026-03-02 19:13 UTC)

<p>Slicer supports loading multiple volumes into the scene (as viewed in the Data module). You can use the Compare Volumes module to pick which volumes you want to view side-by-side and it will create a convenient layout for it.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://slicer.readthedocs.io/en/latest/user_guide/modules/comparevolumes.html">
  <header class="source">

      <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/comparevolumes.html" target="_blank" rel="noopener nofollow ugc">slicer.readthedocs.io</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/comparevolumes.html" target="_blank" rel="noopener nofollow ugc">Compare Volumes — 3D Slicer  documentation</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
