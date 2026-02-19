---
topic_id: 13858
title: "Edit Thick Shell"
date: 2020-10-04
url: https://discourse.slicer.org/t/13858
---

# Edit thick shell

**Topic ID**: 13858
**Date**: 2020-10-04
**URL**: https://discourse.slicer.org/t/edit-thick-shell/13858

---

## Post #1 by @Hamid (2020-10-04 22:16 UTC)

<p>I’ve made a thick shell of Aorta, I exported the shell to the model and I am able to use clipping to see inside the model. I want to edit  it e.g removing some sharp corners and etc.  Is there any way to edit the model ?</p>

---

## Post #2 by @lassoan (2020-10-04 23:26 UTC)

<p>I would recommend to smooth the segmentation and not the exported model. The best is to smooth before converting to a shell.</p>
<p>You can edit the mesh using Surface Toolbox and Dynamic Modeler modules.</p>

---

## Post #3 by @Hamid (2020-10-05 02:21 UTC)

<p>I smoothed it and then made the shell, but at some points like connections which happen after merging the sharp corners are inevitable. Your recommendation (surface toolbox and Dynamic Modeler) are very nice and helpful. I will try those.<br>
Many thanks to you Lassoan!</p>

---
