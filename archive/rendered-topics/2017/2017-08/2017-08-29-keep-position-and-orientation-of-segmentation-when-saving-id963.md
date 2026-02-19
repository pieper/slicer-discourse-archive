---
topic_id: 963
title: "Keep Position And Orientation Of Segmentation When Saving"
date: 2017-08-29
url: https://discourse.slicer.org/t/963
---

# Keep position and orientation of segmentation when saving

**Topic ID**: 963
**Date**: 2017-08-29
**URL**: https://discourse.slicer.org/t/keep-position-and-orientation-of-segmentation-when-saving/963

---

## Post #1 by @amewes (2017-08-29 13:36 UTC)

<p>Operating system: Win 10<br>
Slicer version: Current Nightly<br>
Expected behavior: surface model from segmentation should be in correct position with respect to volume<br>
Actual behavior: surface model from segmentation is shifted somewhere</p>
<p>I want to segment a rib from a dataset and save it as a ply file. However, the exported model is not at the correct position but shifted somewhere. How do I keep the transform of the anatomical dataset so that the segmented model remains at the correct position? I would expect this to be the default behaviour.</p>

---

## Post #2 by @lassoan (2017-08-29 13:42 UTC)

<p>Does the exported model appear in the correct position in Slicer?<br>
If you save the model to file and load it back to Slicer, does the exported model appear in the correct position?<br>
Have you applied a transform on your Segmentation node?<br>
Do you have this alignment problem when you load the surface mesh and volume in some other software?</p>

---

## Post #3 by @amewes (2017-08-30 09:21 UTC)

<p>It appears at the correct position in slicer, but not in external programs (Meshlab).<br>
I did not apply any transform to it.</p>
<p>When I export the segmented model as a labelmap, import the label map in an other program (MeVisLab), and export it as ply, then it has the correct position.</p>
<p>It seems that I cannot choose a reference volume in model export in slicer; this is possible only for labelmap export. Maybe that’s why it is positioned at origin coordinates?</p>

---

## Post #4 by @lassoan (2017-08-30 11:23 UTC)

<p>STL files cannot store in a standard way what unit and coordinate system is used and each software use different conventions. Following the solution described in this topic will most likely resolve the inconsistency for you:</p>
<p><a href="https://discourse.slicer.org/t/misalignment-visualization-problem/821/2" class="onebox" target="_blank">https://discourse.slicer.org/t/misalignment-visualization-problem/821/2</a></p>

---
