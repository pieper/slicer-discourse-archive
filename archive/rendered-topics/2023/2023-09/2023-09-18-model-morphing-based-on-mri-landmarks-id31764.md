---
topic_id: 31764
title: "Model Morphing Based On Mri Landmarks"
date: 2023-09-18
url: https://discourse.slicer.org/t/31764
---

# Model morphing based on MRI landmarks

**Topic ID**: 31764
**Date**: 2023-09-18
**URL**: https://discourse.slicer.org/t/model-morphing-based-on-mri-landmarks/31764

---

## Post #1 by @hyncik (2023-09-18 02:37 UTC)

<p>Hi,</p>
<p>I am working on a female-specific pelvic floor model development based on a template model and MRI landmarks. Currently I have programmed my extension into Slicer, which reads the template model (computational grid / surface facets as polydata) and template landmarks on the model.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c2bd41d732d25b801f17bccb37a21fe66cd5d843.png" data-download-href="/uploads/short-url/rMK6SoSAkZuNqEmkQoatpDZYIQH.png?dl=1" title="ScalingMRI" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c2bd41d732d25b801f17bccb37a21fe66cd5d843_2_650x500.png" alt="ScalingMRI" data-base62-sha1="rMK6SoSAkZuNqEmkQoatpDZYIQH" width="650" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c2bd41d732d25b801f17bccb37a21fe66cd5d843_2_650x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c2bd41d732d25b801f17bccb37a21fe66cd5d843.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c2bd41d732d25b801f17bccb37a21fe66cd5d843.png 2x" data-dominant-color="676F83"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ScalingMRI</span><span class="informations">812×624 228 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The next step is the morph / warp the template model based on alignment of template landmarks and MRI landmarks. Before programming my own script, I have an idea to employ SlicerMorph or any other already developed extension.</p>
<p>Can you advice, please?</p>
<p>Thank you, Ludek</p>

---

## Post #2 by @muratmaga (2023-09-18 04:38 UTC)

<p>if you have a population of samples, you can use the GPA module in SlicerMorph to derive PCA space of landmark variation and then deform/warp your template along PC axes.</p>
<p>If your goal is to deform a template to a specific subject using landmarks, then fiducial registration wizard in IGT extension would be more relevant. Just use the TPS warping transform. However, I am only seeing four landmarks in your screen capture. If indeed those are the landmarks you are planning to use, they may be quite insufficient for a realistic deformation of the pelvis.</p>

---

## Post #3 by @hyncik (2023-09-18 05:34 UTC)

<p>Thank you, I put here just a sample picture, I have over 30 landmarks in total. The aim of this project is also to find the sufficient number and location of landmarks.</p>

---
