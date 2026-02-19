---
topic_id: 45058
title: "How To Merge Two Ct Series Thorax Abdopelvis Into One Contin"
date: 2025-11-12
url: https://discourse.slicer.org/t/45058
---

# How to merge two CT series (Thorax + AbdoPelvis) into one continuous volume in Slicer 5.10

**Topic ID**: 45058
**Date**: 2025-11-12
**URL**: https://discourse.slicer.org/t/how-to-merge-two-ct-series-thorax-abdopelvis-into-one-continuous-volume-in-slicer-5-10/45058

---

## Post #1 by @Julien_Ancel (2025-11-12 22:40 UTC)

<p>Hello everyone,</p>
<p>I’m working on a quantitative imaging project and I have two CT series from the same patient:</p>
<ul>
<li>
<p>one <strong>Thorax</strong> series (<code>Thorax MEDIASTIN 2.0 MPR ax</code>)</p>
</li>
<li>
<p>one <strong>AbdoPelvis</strong> series (<code>PORTAL 2.0 MPR ax</code>).</p>
</li>
</ul>
<p>Both are from the same acquisition session, with similar spacing (≈ 2 mm) and kernel, but they are stored as two separate series in DICOM.<br>
I would like to <strong>merge them into one single continuous volume (thoraco-abdominopelvic)</strong> for segmentation and radiomic analysis.</p>
<p><strong>Question:</strong><br>
What is the correct way (either via GUI or Python) to merge two contiguous CT volumes into a single continuous one in Slicer 5.10, preserving HU values and patient coordinates?<br>
Is there a recommended extension or function for this (e.g., Merge Volumes, SlicerMorph, etc.)?</p>
<p>Any example code or workflow would be greatly appreciated.</p>
<p>Thanks a lot for your help!<br>
Julien</p>

---

## Post #2 by @pieper (2025-11-12 23:43 UTC)

<p>This may be what you are looking for:</p>
<aside class="onebox githubrepo" data-onebox-src="https://github.com/mikebind/SlicerStitchImageVolumes">
  <header class="source">

      <a href="https://github.com/mikebind/SlicerStitchImageVolumes" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/d7f8b38af30b7cbbcca1e67963f0d8c4/mikebind/SlicerStitchImageVolumes" class="thumbnail">

  <h3><a href="https://github.com/mikebind/SlicerStitchImageVolumes" target="_blank" rel="noopener">GitHub - mikebind/SlicerStitchImageVolumes: A 3D Slicer (slicer.org) module for stitching...</a></h3>

    <p><span class="github-repo-description">A 3D Slicer (slicer.org) module for stitching together multiple image volumes into a single larger image volume.</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
