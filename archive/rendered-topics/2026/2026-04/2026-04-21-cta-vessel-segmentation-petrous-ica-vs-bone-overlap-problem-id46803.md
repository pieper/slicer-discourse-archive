---
topic_id: 46803
title: "CTA vessel segmentation: petrous ICA vs bone overlap problem"
date: 2026-04-21
url: https://discourse.slicer.org/t/46803
last_bumped: 2026-04-22T19:26:03.840Z
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

## Post #2 by @pieper (2026-04-22 13:19 UTC)

<p>A lot depends on the quality of your CTA.  I had some luck on exactly this problem using nnInteractive.</p>

---

## Post #3 by @chir.set (2026-04-22 19:26 UTC)

<p>You can use the <code>Guided artery segmentation</code> and the <code>Guided vein segmentation</code> modules in the <a href="https://github.com/vmtk/SlicerExtension-VMTK" rel="noopener nofollow ugc">SlicerVMTK</a> extension. A sample result is below.</p>
<p>It’s indeed not straightforward inside a bone. Segmenting the carotids at the neck level is done in a breeze (except in very very tight stenosis). Segmenting the circle of Willis is even more tricky.</p>
<p>Since you are a beginner, I would advise to crop your volume to the target region of study to save time. Resampling to isotropic voxel size gives better results that are more good looking in addition.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/704dc6ea353b6e3670cd0ddbfb832921c042d634.jpeg" data-download-href="/uploads/short-url/g1u711bkj4TpPgVqgj37Fhamqy0.jpeg?dl=1" title="IntraPetrousICAGAS" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/704dc6ea353b6e3670cd0ddbfb832921c042d634_2_641x500.jpeg" alt="IntraPetrousICAGAS" data-base62-sha1="g1u711bkj4TpPgVqgj37Fhamqy0" width="641" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/704dc6ea353b6e3670cd0ddbfb832921c042d634_2_641x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/704dc6ea353b6e3670cd0ddbfb832921c042d634_2_961x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/704dc6ea353b6e3670cd0ddbfb832921c042d634_2_1282x1000.jpeg 2x" data-dominant-color="252623"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IntraPetrousICAGAS</span><span class="informations">1497×1167 174 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6d007df61d0a95a7876ee9b766c46ade8b6503c7.jpeg" data-download-href="/uploads/short-url/fyh66uolY3f0Tvu4M58oS1rqcm3.jpeg?dl=1" title="IntraPetrousICAGVS" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6d007df61d0a95a7876ee9b766c46ade8b6503c7_2_641x500.jpeg" alt="IntraPetrousICAGVS" data-base62-sha1="fyh66uolY3f0Tvu4M58oS1rqcm3" width="641" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6d007df61d0a95a7876ee9b766c46ade8b6503c7_2_641x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6d007df61d0a95a7876ee9b766c46ade8b6503c7_2_961x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6d007df61d0a95a7876ee9b766c46ade8b6503c7_2_1282x1000.jpeg 2x" data-dominant-color="272721"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IntraPetrousICAGVS</span><span class="informations">1497×1167 181 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
