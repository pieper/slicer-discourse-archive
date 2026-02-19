---
topic_id: 28143
title: "Pet Spect Maximum Intensity Projection"
date: 2023-03-02
url: https://discourse.slicer.org/t/28143
---

# PET / SPECT Maximum Intensity Projection

**Topic ID**: 28143
**Date**: 2023-03-02
**URL**: https://discourse.slicer.org/t/pet-spect-maximum-intensity-projection/28143

---

## Post #1 by @Jan_Lennart (2023-03-02 16:03 UTC)

<p>Hi Slicer Community,</p>
<p>Can someone guide me to a tutorial or the appropriate manual on creating a 2d MIP of SPECT or PET scans?</p>
<aside class="onebox wikipedia" data-onebox-src="https://en.wikipedia.org/wiki/Maximum_intensity_projection">
  <header class="source">

      <a href="https://en.wikipedia.org/wiki/Maximum_intensity_projection" target="_blank" rel="noopener nofollow ugc">en.wikipedia.org</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:100/354;"><img src="//upload.wikimedia.org/wikipedia/commons/f/fe/Mouse02-spect.gif" class="thumbnail" width="100" height="354"></div>

<h3><a href="https://en.wikipedia.org/wiki/Maximum_intensity_projection" target="_blank" rel="noopener nofollow ugc">Maximum intensity projection</a></h3>

<p>In scientific visualization, a maximum intensity projection (MIP) is a method for 3D data that projects in the visualization plane the voxels with maximum intensity that fall in the way of parallel rays traced from the viewpoint to the plane of projection.  This implies that two MIP renderings from opposite viewpoints are symmetrical images if they are rendered using orthographic projection.
 MIP is used for the detection of lung nodules in lung cancer screening programs which use computed tomogr...</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Thanks,<br>
Jan</p>

---

## Post #2 by @3sa5c64x (2023-04-20 06:29 UTC)

<p>Hi,</p>
<ol>
<li>import DICOM files</li>
<li>go to Volume Rendering module</li>
<li>select volume and enable 3D view</li>
<li>open Advanced - Techniques tab and select MIP technique, adjust scalar opacity mapping</li>
<li>center 3D view</li>
</ol>

---
