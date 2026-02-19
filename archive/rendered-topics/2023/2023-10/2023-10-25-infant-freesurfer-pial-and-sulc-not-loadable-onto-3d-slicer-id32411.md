---
topic_id: 32411
title: "Infant Freesurfer Pial And Sulc Not Loadable Onto 3D Slicer"
date: 2023-10-25
url: https://discourse.slicer.org/t/32411
---

# Infant Freesurfer .pial and .sulc not loadable onto 3d Slicer 5.3.0

**Topic ID**: 32411
**Date**: 2023-10-25
**URL**: https://discourse.slicer.org/t/infant-freesurfer-pial-and-sulc-not-loadable-onto-3d-slicer-5-3-0/32411

---

## Post #1 by @orocchio-giordano (2023-10-25 16:21 UTC)

<p>Hello!</p>
<p>I am using clinical data processed through the infant_recon_pipeline in Freesurfer and I am receiving error messages when I try to load the pial surfaces and sulc scalar overlays into 3d Slicer.</p>
<p>With previous datasets, freesurferimporter extension has worked beautifully and allows me to import lh.pial with lh.sulc scalar overlay and corresponding “brain.mgz” reference volume. I repeat that process with rh.pial, lh.white, and rh.white (***Note, due to a bug, loading all of these at once does not work and so I’ve found that I have to load each model individally with it’s own individual scalar overlay)</p>
<p>As of now, the only difference between the new dataset (let’s call it A) and the one I was previously using (B) is the fact that the outputs are for a younger subject. Dataset A actually has two sets of data; all are young children, however, only 1/3 of all subjects were processed with the infant pipeline. The remaining subjects were above the 4.5 year threshold to use adult freesurfer pipeline, but I noticed that the individual pial files were only 1 KB compared to those in Dataset B, which were roughly 4.5 KB.</p>
<p>I’ve tried redownloading and deleting, as well as individually loading data without the freesurfer importer module section, but no pial surfaces load, and only a handful of the white surfaces load.</p>
<p>I welcome any and all feedback that you may have in resolving this issue. Please let me know how I can help, I appreciate your feedback!</p>
<p>Sincerely,<br>
Olivia</p>

---

## Post #2 by @Sunderlandkyl (2023-10-25 16:26 UTC)

<p>Could you send me a link to the datasets?</p>

---
