---
topic_id: 46803
title: "Cta Vessel Segmentation Petrous Ica Vs Bone Overlap Problem"
date: 2026-04-21
url: https://discourse.slicer.org/t/46803
---

# CTA vessel segmentation: petrous ICA vs bone overlap problem

**Topic ID**: 46803
**Date**: 2026-04-21
**URL**: https://discourse.slicer.org/t/cta-vessel-segmentation-petrous-ica-vs-bone-overlap-problem/46803

---

## Post #1 by @sandcastle (2026-04-21 20:49 UTC)

<p>Hi all,</p>
<p>I’ve been working on segmenting the circle of Willis and proximal carotids from CTA data. This has been straightforward with 3DRA and TOF-MRA, but I’m running into difficulty with the petrous ICA being inseparable from adjacent bone on CTA.</p>
<p>The main issue seems to be that contrast-enhanced vessels and cortical bone have overlapping intensities, so:</p>
<ul>
<li>
<p>manual thresholding fails</p>
</li>
<li>
<p>Grow from Seeds leaks into bone</p>
</li>
<li>
<p>pre-processing with Swiss Skull Stripper has not helped</p>
</li>
</ul>
<p>Does anyone have recommendations for separating vessels from bone in this region? For example:</p>
<ul>
<li>
<p>specific Slicer workflows or modules</p>
</li>
<li>
<p>preprocessing techniques</p>
</li>
<li>
<p>or alternative segmentation strategies beyond intensity-based methods</p>
</li>
</ul>
<p>I’m relatively new to 3D Slicer, so any guidance on specific workflows or modules would be especially helpful. Thanks in advance!</p>

---
