---
topic_id: 26903
title: "How To Conduct A 3D Cad Comparison To Obtain The Magnitude D"
date: 2022-12-24
url: https://discourse.slicer.org/t/26903
---

# How to conduct a 3D CAD comparison to obtain the magnitude deviations with a pre-alignment?

**Topic ID**: 26903
**Date**: 2022-12-24
**URL**: https://discourse.slicer.org/t/how-to-conduct-a-3d-cad-comparison-to-obtain-the-magnitude-deviations-with-a-pre-alignment/26903

---

## Post #1 by @refak_makeen (2022-12-24 04:59 UTC)

<p>I am currently working on predicting distortion of metal additive manufactured wedge structures. we have made a feasible numerical framework to fabricate components using Abaqus CAE software. In order to validate the framework we are looking into the distortion of as-built fabricated parts. An experimental specimen is as shown in the figure below.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dc5f408e1b6402fd3381d8440747e2cf9a0ace50.jpeg" data-download-href="/uploads/short-url/vrv7sxCcAHnNhOE4nfwpsLvKsA8.jpeg?dl=1" title="Screenshot 2565-12-23 at 16.49.44" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/c/dc5f408e1b6402fd3381d8440747e2cf9a0ace50_2_690x457.jpeg" alt="Screenshot 2565-12-23 at 16.49.44" data-base62-sha1="vrv7sxCcAHnNhOE4nfwpsLvKsA8" width="690" height="457" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/c/dc5f408e1b6402fd3381d8440747e2cf9a0ace50_2_690x457.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/c/dc5f408e1b6402fd3381d8440747e2cf9a0ace50_2_1035x685.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/c/dc5f408e1b6402fd3381d8440747e2cf9a0ace50_2_1380x914.jpeg 2x" data-dominant-color="CDCFD4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2565-12-23 at 16.49.44</span><span class="informations">1920×1273 84.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Using the Atos core optical camera a 3D stl file of the wedge specimen was obtained and compared using the inbuilt inspection tool. I am getting the deviation results using this software not as a magnitude but the maximum deviation is comparable with the distortion due to residual stresses during the part build.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/47aa112116b3dfc43a8a2b8795fb1381bb5023f4.jpeg" data-download-href="/uploads/short-url/adYgyEiD3JbUqzblg37ftWRGL2Y.jpeg?dl=1" title="Screenshot 2565-12-23 at 16.53.31" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/47aa112116b3dfc43a8a2b8795fb1381bb5023f4_2_690x379.jpeg" alt="Screenshot 2565-12-23 at 16.53.31" data-base62-sha1="adYgyEiD3JbUqzblg37ftWRGL2Y" width="690" height="379" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/47aa112116b3dfc43a8a2b8795fb1381bb5023f4_2_690x379.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/47aa112116b3dfc43a8a2b8795fb1381bb5023f4_2_1035x568.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/47aa112116b3dfc43a8a2b8795fb1381bb5023f4_2_1380x758.jpeg 2x" data-dominant-color="A1ADC7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2565-12-23 at 16.53.31</span><span class="informations">1920×1056 92.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I would like to know if we can find the magnitude distortion of a given surface mesh obtained from an optical camera to make a better comparison with my FEM framework results. Is there any software  package, python libraries, to get this task done. Thanks in advance!</p>

---
