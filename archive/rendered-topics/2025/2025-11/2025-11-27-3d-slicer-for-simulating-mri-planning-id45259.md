---
topic_id: 45259
title: "3D Slicer For Simulating Mri Planning"
date: 2025-11-27
url: https://discourse.slicer.org/t/45259
---

# 3D Slicer for simulating MRI planning

**Topic ID**: 45259
**Date**: 2025-11-27
**URL**: https://discourse.slicer.org/t/3d-slicer-for-simulating-mri-planning/45259

---

## Post #1 by @Dave (2025-11-27 19:30 UTC)

<p>Hello everyone:</p>
<p>I’m a mri teacher for technologists who would like to use this software for my lessons. I find it very useful to visualize DICOM data and navigating through organs and different planes.</p>
<p>Could it be possible, or does it even exist, some module/feature that simulates what a mri planning software performs? Some sort of ROI localized in three planes (SAG, COR, TRA) so my students could practice with the “planning box“ in order to acquire different planes of the studied organ.</p>
<p>Thanks in advance.</p>

---

## Post #2 by @Andinet_Enquobahrie (2025-11-28 13:29 UTC)

<p>Yes. Slicer can be used to simulate MRI planning. There isn’t a dedicated “MRI console” module, but the built-in tools work very well for teaching slice prescription:</p>
<ol>
<li>
<p>Reformat module: lets you rotate and translate slice planes just like prescribing oblique sagittal/axial/coronal views.</p>
</li>
<li>
<p>Markups → ROI: acts like a planning box that appears in all slice views.</p>
</li>
<li>
<p>Markups → Plane: lets you place and rotate an arbitrary plane, and you can link it to a slice view.</p>
</li>
</ol>
<p>If you want more advanced behavior (e.g., reslicing along a path, tracked planes, or custom slice stacks), the SlicerIGT extension provides these features. Tutorials are available here:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://www.slicerigt.org/wp/user-tutorial/">
  <header class="source">
      <img src="http://www.slicerigt.org/wp/wp-content/uploads/2014/04/favicon1.png" class="site-icon" alt="" width="16" height="16">

      <a href="https://www.slicerigt.org/wp/user-tutorial/" target="_blank" rel="noopener nofollow ugc">slicerigt.org</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://www.slicerigt.org/wp/user-tutorial/" target="_blank" rel="noopener nofollow ugc">User tutorial | SlicerIGT</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
