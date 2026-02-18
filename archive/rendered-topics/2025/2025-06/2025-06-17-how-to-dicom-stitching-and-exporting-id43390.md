# How to: DICOM stitching and exporting

**Topic ID**: 43390
**Date**: 2025-06-17
**URL**: https://discourse.slicer.org/t/how-to-dicom-stitching-and-exporting/43390

---

## Post #1 by @Franchi (2025-06-17 16:36 UTC)

<p>Hello everyone, total noob on 3DSlicer here!</p>
<p>I have two partial cranial DICOM datasets of different length due to the unsufficient FOV of the CBCT used.<br>
It´s two different folders composed of 200 and 400 .dcm files each, with an overlapping segment of about 150 mm which I believe should be sufficient for proper alignment of both volumes.</p>
<p>Could I please get a step by step tutorial for importing both folders, aligning both volumes and finally exporting it all as either a single .dcm file or a dicom dataset?</p>
<p>Thanks in advance</p>

---

## Post #2 by @pieper (2025-06-17 17:54 UTC)

<p><a class="mention" href="/u/mikebind">@mikebind</a> has a module for that:</p><aside class="onebox githubrepo" data-onebox-src="https://github.com/mikebind/SlicerStitchImageVolumes">
  <header class="source">

      <a href="https://github.com/mikebind/SlicerStitchImageVolumes" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/e701f6d68cabe0419198ba40965b5015/mikebind/SlicerStitchImageVolumes" class="thumbnail">

  <h3><a href="https://github.com/mikebind/SlicerStitchImageVolumes" target="_blank" rel="noopener">GitHub - mikebind/SlicerStitchImageVolumes: A 3D Slicer (slicer.org) module for stitching...</a></h3>

    <p><span class="github-repo-description">A 3D Slicer (slicer.org) module for stitching together multiple image volumes into a single larger image volume.</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
