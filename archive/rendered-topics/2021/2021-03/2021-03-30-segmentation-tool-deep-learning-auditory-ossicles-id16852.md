---
topic_id: 16852
title: "Segmentation Tool Deep Learning Auditory Ossicles"
date: 2021-03-30
url: https://discourse.slicer.org/t/16852
---

# Segmentation tool, Deep learning, Auditory ossicles

**Topic ID**: 16852
**Date**: 2021-03-30
**URL**: https://discourse.slicer.org/t/segmentation-tool-deep-learning-auditory-ossicles/16852

---

## Post #1 by @j.v.d (2021-03-30 15:28 UTC)

<p>Operating system: macOS Big Sur 11.2.1<br>
Slicer version: 4.11.20210226<br>
Expected behavior: Automatic segmentation of the auditory ossicles<br>
Actual behavior: Segmentation via thresholding and no segmentation for the stapes</p>
<p>Hey everyone!<br>
I´m working on a project about the 3D-segmentation of the middle ear with different CT modalities.<br>
I already segmented some of the auditory ossicles but until now I didn’t achieve a segmentation of the stapes and the tympanic membrane with the thresholding tool even with very high resolution images.<br>
Is there already a special tool for the segmentation of these anatomic structures ?<br>
And further I wanted to ask, if there is already a tool for the automatic segmentation of the auditory ossicles via deep learning ?</p>
<p>Thanks a lot in advance!<br>
Kind regards<br>
Jan</p>

---

## Post #2 by @lassoan (2021-04-03 03:14 UTC)

<p>You may find that representation of very thin membranes and curves requires very high resolution segmentation. If your computer cannot handle sufficiently high-resolution segmentations (it runs out of physical memory and starts swapping memory to disk, making everything extremely slow) then you can model them using curves and curved surfaces.</p>
<p>You can use Markups Curves to “segment” stapes and the newly added <a href="https://discourse.slicer.org/t/new-module-baffle-planner-for-designing-surface-patches/16799">Baffle planner module</a> to create a model of the membrane.</p>
<aside class="quote no-group" data-username="j.v.d" data-post="1" data-topic="16852">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/8c91f0/48.png" class="avatar"> j.v.d:</div>
<blockquote>
<p>And further I wanted to ask, if there is already a tool for the automatic segmentation of the auditory ossicles via deep learning ?</p>
</blockquote>
</aside>
<p>I would think so. You may contact members of the <a href="https://github.com/Auditory-Biophysics-Lab/Slicer-ABLTemporalBoneSegmentation"> Auditory Medical Biophysics Lab at Western University</a> to get more information.</p>

---
