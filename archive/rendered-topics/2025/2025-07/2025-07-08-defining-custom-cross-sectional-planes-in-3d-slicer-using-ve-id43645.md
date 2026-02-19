---
topic_id: 43645
title: "Defining Custom Cross Sectional Planes In 3D Slicer Using Ve"
date: 2025-07-08
url: https://discourse.slicer.org/t/43645
---

# Defining Custom Cross-Sectional Planes in 3D Slicer Using Vectors

**Topic ID**: 43645
**Date**: 2025-07-08
**URL**: https://discourse.slicer.org/t/defining-custom-cross-sectional-planes-in-3d-slicer-using-vectors/43645

---

## Post #1 by @Alex-Martin1 (2025-07-08 12:45 UTC)

<p>Hi everyone,</p>
<p>I’m writing here to ask whether something I’ve been doing in <strong>Amira</strong> can be replicated in an open-source software like <strong>3D Slicer</strong>.</p>
<p>Specifically, I need to define a <strong>cross-sectional plane</strong> with a specific orientation and position, in order to extract cross-sectional images from a defined region. In Amira, this can be done by specifying two 3D vectors (to set the plane’s orientation) and a point of origin (to set the location of the plane). This is really useful for standardizing the procedure.</p>
<p>Is there a way to do something similar in <strong>3D Slicer</strong>? Even better, is there a way to <strong>automate</strong> this through the console or scripting interface? In Amira, there’s no way to set the cross-sectional plane using commands - you have to manually copy and paste the coordinates of the vectors and origin, which is quite tedious when working with many samples.</p>
<p>I would really appreciate any help or guidance.</p>
<p>Thanks so much in advance!<br>
Alex</p>

---

## Post #2 by @pieper (2025-07-08 17:35 UTC)

<p>That all sounds quite doable.  Have a look at the example scripts and you’ll find code for making markups, working with planes, transforming images, etc.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html">
  <header class="source">

      <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html" target="_blank" rel="noopener">slicer.readthedocs.io</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html" target="_blank" rel="noopener">Script repository — 3D Slicer  documentation</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
