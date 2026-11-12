---
topic_id: 48853
title: "How to Create a 3D Cuboid ROI ?(3D-Slicer Version 5.12.4)"
date: 2026-11-11
url: https://discourse.slicer.org/t/48853
last_bumped: 2026-11-11T16:06:31.328Z
---

# How to Create a 3D Cuboid ROI ?(3D-Slicer Version 5.12.4)

**Topic ID**: 48853
**Date**: 2026-11-11
**URL**: https://discourse.slicer.org/t/how-to-create-a-3d-cuboid-roi-3d-slicer-version-5-12-4/48853

---

## Post #1 by @zahra_jbz (2026-11-11 16:06 UTC)

<p>Hello everyone,</p>
<p>I would like to create a 3D cuboid (rectangular prism) ROI in 3D Slicer with the following boundaries:</p>
<ul>
<li>
<p><strong>Superior and inferior boundaries:</strong> Defined by two specific axial slices.</p>
</li>
<li>
<p><strong>Medial boundary:</strong> The patient’s midline.</p>
</li>
<li>
<p><strong>Lateral boundary:</strong> The midaxillary line.</p>
</li>
</ul>
<p>My goal is to calculate the volume of the intersection between this 3D region and an existing heart segmentation.</p>
<p>Could anyone guide me on how to create this 3D ROI and calculate the overlapping volume with the heart segmentation in 3D Slicer?</p>
<p>I would appreciate any suggestions, recommended modules, or Python-based solutions.</p>
<p>Thank you!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/75d05fbf49e05fdff5c1ccde98be9de145cd1d82.png" data-download-href="/uploads/short-url/gOeiNUczO3S2uOaBSZJUOyIG8YG.png?dl=1" title="Screenshot 2026-11-11 112009" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/75d05fbf49e05fdff5c1ccde98be9de145cd1d82_2_607x500.png" alt="Screenshot 2026-11-11 112009" data-base62-sha1="gOeiNUczO3S2uOaBSZJUOyIG8YG" width="607" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/75d05fbf49e05fdff5c1ccde98be9de145cd1d82_2_607x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/75d05fbf49e05fdff5c1ccde98be9de145cd1d82_2_910x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/75d05fbf49e05fdff5c1ccde98be9de145cd1d82.png 2x" data-dominant-color="71677E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2026-11-11 112009</span><span class="informations">1047×862 305 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
