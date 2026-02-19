---
topic_id: 25091
title: "Measurement For The Distance And Surface Area Between Joints"
date: 2022-09-05
url: https://discourse.slicer.org/t/25091
---

# Measurement for the distance and surface area between joints

**Topic ID**: 25091
**Date**: 2022-09-05
**URL**: https://discourse.slicer.org/t/measurement-for-the-distance-and-surface-area-between-joints/25091

---

## Post #1 by @yyokoyama (2022-09-05 03:53 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/0034441714f18fc9bf9c3de792da86cb2c7b7ab8.jpeg" data-download-href="/uploads/short-url/1NYIA4AYjdAg8YqzYnq4k5t7rG.jpeg?dl=1" title="2022-09-04" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/0034441714f18fc9bf9c3de792da86cb2c7b7ab8_2_348x500.jpeg" alt="2022-09-04" data-base62-sha1="1NYIA4AYjdAg8YqzYnq4k5t7rG" width="348" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/0034441714f18fc9bf9c3de792da86cb2c7b7ab8_2_348x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/0034441714f18fc9bf9c3de792da86cb2c7b7ab8_2_522x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/0034441714f18fc9bf9c3de792da86cb2c7b7ab8_2_696x1000.jpeg 2x" data-dominant-color="8D8D8C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2022-09-04</span><span class="informations">1043×1496 66.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
What would be the best way to measure the distance and surface area between sacroiliac joints (blue marked in the attached figure)?</p>

---

## Post #2 by @lassoan (2022-09-05 03:56 UTC)

<p>Since you are doing measurements in 3D, it is important to first check that the plane you are measuring the joint thickness on is orthogonal to the joint surface. You can do that by enabling slice intersection line display and translate and/or rotate the slice view if needed.</p>
<p>Then you could simply place a markup line to measure distance on the image. However, it may not be trivial to place the line endpoints in a reproducible way to the edges of the joint. To make this distance measurement more reproducible, a markup line can be placed across the joint and an intensity plot can be obtained using “Line profile” module (in Sandbox extension). The cortical bone surface shows up as a two strong peaks on the profile, which can be used to measure the joint thickness.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c5fb8156da0a58b42424f8e43925848573669fdc.jpeg" data-download-href="/uploads/short-url/sfqUmMkKqjDSVphpfrhfzfOB3uQ.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c5fb8156da0a58b42424f8e43925848573669fdc_2_690x420.jpeg" alt="image" data-base62-sha1="sfqUmMkKqjDSVphpfrhfzfOB3uQ" width="690" height="420" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c5fb8156da0a58b42424f8e43925848573669fdc_2_690x420.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c5fb8156da0a58b42424f8e43925848573669fdc_2_1035x630.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c5fb8156da0a58b42424f8e43925848573669fdc_2_1380x840.jpeg 2x" data-dominant-color="49565A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1170 196 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>If thickness measurement is needed along the entire joint space (and users are confident placing curves on the edges of the joint) then two markup curves can be placed on the image and distance between the curves can be obtained by copy-pasting this code snippet into the Python console:</p>
<pre><code class="lang-python"># distance between curves
curve1 = getNode('C1')
curve2 = getNode('C2')

import numpy as np
curve1points = arrayFromMarkupsCurvePoints(curve1)
curveDistances = np.zeros(len(curve1points))
for pointIndex, curve1point in enumerate(curve1points):
    curve2closestPoint = np.zeros(3)
    curve2.GetClosestPointPositionAlongCurveWorld(curve1point, curve2closestPoint)
    curveDistances[pointIndex] = np.linalg.norm(curve1point-curve2closestPoint)

plt = plot(curveDistances)
print(f"Average distance: {np.mean(curveDistances)}")
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4c24d0afe59c5bc850bfeac7b2b6e00193e163b8.jpeg" data-download-href="/uploads/short-url/aRBaa7cPHPnBCtQpD3R4BCGd43S.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4c24d0afe59c5bc850bfeac7b2b6e00193e163b8_2_690x419.jpeg" alt="image" data-base62-sha1="aRBaa7cPHPnBCtQpD3R4BCGd43S" width="690" height="419" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4c24d0afe59c5bc850bfeac7b2b6e00193e163b8_2_690x419.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4c24d0afe59c5bc850bfeac7b2b6e00193e163b8_2_1035x628.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4c24d0afe59c5bc850bfeac7b2b6e00193e163b8_2_1380x838.jpeg 2x" data-dominant-color="4F514F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1168 176 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>If you are interested in the area then you can add a closed curve (you can create the closed curve automatically from the two open curves that were created for the distance measurement) and enable “area” measurement:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d189291c92264ded4244f56fa4e188f8cdc80e44.jpeg" data-download-href="/uploads/short-url/tTDEHJeGUCyUGc2QW6MNLB1uxZW.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d189291c92264ded4244f56fa4e188f8cdc80e44.jpeg" alt="image" data-base62-sha1="tTDEHJeGUCyUGc2QW6MNLB1uxZW" width="690" height="469" data-dominant-color="423938"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">696×474 73.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>If you need joint thickness measurement in the entire joint space, not just in a selected plane then you can segment the sacrum and iliac bone using “Segment Editor” module and compute distances using “Model to model distance” extension. Manual segmentation may be time-consuming but there are some semi-automatic segmentation tools that may reduce this time or you can train an AI models to fully automate the segmentation (e.g., using <a href="https://docs.monai.io/projects/label/en/latest/index.html">MONAILabel</a>)</p>

---

## Post #3 by @yyokoyama (2022-09-06 04:12 UTC)

<p>Dear lassoan<br>
Thank you for your detailed response.<br>
I have some questions about the “line profile” module you mentioned.<br>
I understood the “line profile” module exists in <a href="https://github.com/PerkLab/SlicerSandbox/tree/master/LineProfile" class="inline-onebox" rel="noopener nofollow ugc">SlicerSandbox/LineProfile at master · PerkLab/SlicerSandbox · GitHub</a>, but don’t know how to install it. I would appreciate it if you could tell me.</p>
<p>Sincerely</p>

---

## Post #4 by @lassoan (2022-09-06 11:24 UTC)

<p>You can install the Sandbox extension in the Extensions Manager in Slicer.</p>

---
