---
topic_id: 46768
title: "Error Using Opendose 3D"
date: 2026-04-17
url: https://discourse.slicer.org/t/46768
---

# Error using OpenDose 3D 

**Topic ID**: 46768
**Date**: 2026-04-17
**URL**: https://discourse.slicer.org/t/error-using-opendose-3d/46768

---

## Post #1 by @Oscar_Azula (2026-04-17 13:51 UTC)

<p>Hello,</p>
<p>I am working with patient images from a Lu-177 therapy study in 3D Slicer. After  segmenting the organs and integrating the Absorbed dose rate, I am getting a mass of 0 for all segmented organs.<br>
I would appreciate any guidance on what might be causing this issue.<br>
Here are some additional details:<br>
Imaging modality: SPECT/CT<br>
Module used for dose calculation: OpenDose<br>
Version 5.10.0<br>
From what I understand, mass calculation depends on voxel volume and density (typically from CT Hounsfield Units), so I suspect there may be an issue with missing or incorrect intensity/density information.<br>
Has anyone encountered this problem before or knows how to fix it?<br>
Thank you in advance.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d6afd838b6e361013282c766824e5f1f54208ec.jpeg" data-download-href="/uploads/short-url/6tMI8bjvES6Ux3u8t5DkNskDL9W.jpeg?dl=1" title="1000066076" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d6afd838b6e361013282c766824e5f1f54208ec_2_690x280.jpeg" alt="1000066076" data-base62-sha1="6tMI8bjvES6Ux3u8t5DkNskDL9W" width="690" height="280" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d6afd838b6e361013282c766824e5f1f54208ec_2_690x280.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d6afd838b6e361013282c766824e5f1f54208ec_2_1035x420.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d6afd838b6e361013282c766824e5f1f54208ec_2_1380x560.jpeg 2x" data-dominant-color="625F5C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1000066076</span><span class="informations">1920×780 342 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
