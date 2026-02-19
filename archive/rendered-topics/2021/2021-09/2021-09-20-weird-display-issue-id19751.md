---
topic_id: 19751
title: "Weird Display Issue"
date: 2021-09-20
url: https://discourse.slicer.org/t/19751
---

# Weird Display Issue?

**Topic ID**: 19751
**Date**: 2021-09-20
**URL**: https://discourse.slicer.org/t/weird-display-issue/19751

---

## Post #1 by @mollyselba (2021-09-20 00:01 UTC)

<p>Has anyone else had this issue with random circles appearing in their volumes? The issue only appeared when I switched to the more recent version of 3D Slicer. The size/configuration of circles does not change when I zoom in/out. Any input on how to fix it would be greatly appreciated.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/439688466b3c33516a922c80595a0123aa1a1555.jpeg" data-download-href="/uploads/short-url/9DUvhrvT9GrCNi70B05OzquXAGh.jpeg?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/439688466b3c33516a922c80595a0123aa1a1555_2_690x482.jpeg" alt="Capture" data-base62-sha1="9DUvhrvT9GrCNi70B05OzquXAGh" width="690" height="482" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/439688466b3c33516a922c80595a0123aa1a1555_2_690x482.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/439688466b3c33516a922c80595a0123aa1a1555.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/439688466b3c33516a922c80595a0123aa1a1555.jpeg 2x" data-dominant-color="494A4F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">949×664 75.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8cd647e43ac4b12ed6b011ef7036548b313bdcb.jpeg" data-download-href="/uploads/short-url/sEnxPihvSczW1AcZsEFugPtBJs7.jpeg?dl=1" title="Capture2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c8cd647e43ac4b12ed6b011ef7036548b313bdcb_2_690x478.jpeg" alt="Capture2" data-base62-sha1="sEnxPihvSczW1AcZsEFugPtBJs7" width="690" height="478" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c8cd647e43ac4b12ed6b011ef7036548b313bdcb_2_690x478.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8cd647e43ac4b12ed6b011ef7036548b313bdcb.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8cd647e43ac4b12ed6b011ef7036548b313bdcb.jpeg 2x" data-dominant-color="8E91BF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture2</span><span class="informations">968×671 54.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Operating system: Windows 10 Pro<br>
Slicer version: 4.12.0-2021-09-17<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @lassoan (2021-09-20 00:05 UTC)

<p>Those are the control points of the annotation ROI widget corrupting the alpha channel of the volume renderer.</p>
<p>You can probably make those go away by enabling/disabling depth peeling and/or using the new markups ROI widget, or just by hiding the  annotation ROI widget.</p>

---
