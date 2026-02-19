---
topic_id: 19309
title: "How To Make A Tumor Model In A 3D Ct Data"
date: 2021-08-23
url: https://discourse.slicer.org/t/19309
---

# How to make a tumor model in a 3D CT data?

**Topic ID**: 19309
**Date**: 2021-08-23
**URL**: https://discourse.slicer.org/t/how-to-make-a-tumor-model-in-a-3d-ct-data/19309

---

## Post #1 by @slicexray (2021-08-23 09:08 UTC)

<p>Hi, I am trying a CT imaging simulation project. And I want to use 3Dslicer to build up a tumor model. The conception is inserting a small ball as the tumor model into the current brain model. And export it as a voxelized phantom. Could anyone help me or give some hints?<br>
Best/Johan</p>

---

## Post #2 by @lassoan (2021-08-23 13:59 UTC)

<p>You can paint a tumor using Paint effect in Segment Editor module. If you enable “sphere brush” option then you can create a tumor model by a single click. Then you can paint that segment into the CT using Mask volume effect.</p>
<p>If you want to simulate a more realistic shape or texture then it should be easy to do, too. You can get the image and mask of a segmented tumor as numpy arrays and combine them with voxels of another volume using standard numpy operations. See useful examples in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#combine-multiple-volumes-into-one">script repository</a>.</p>

---

## Post #3 by @slicexray (2021-08-25 02:23 UTC)

<p>Hi, Andras, Thank you for the great advices!<br>
I tried to use the Paint effect with “sphere brush” in the Digimouse model, as the red ball bellow, and click Mask volume.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d301ec37c04ea4b852039f059ede4f4c6cbee790.jpeg" alt="123" data-base62-sha1="u6ERFH6CYGwGutM3BgGjiBK2eOc" width="413" height="358"><br>
Then I add the skin segment and adjust the skin opacity in Segmentations, to make the organ visible. But the red ball is invisible. Could you tell me why?<br>
Best/Johan</p>

---

## Post #4 by @lassoan (2021-08-25 05:32 UTC)

<p>Mask volume modifies the chosen input volume and generates an output volume where the region inside (or outside) of the segment is set to a specific intensity. This can be used to simulate a tumor that looks more dense or contrast-enhanced on the image.</p>
<p>If you successfully add a sphere-shaped segment then it will be displayed in views and adjusting opacity should not affect its visibility. Depending on the opacity value, you may need to <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#d-view">enable depth peeling</a> to ensure transparent segments embedded into each other are displayed correctly.</p>

---

## Post #5 by @slicexray (2021-08-26 15:19 UTC)

<p>I found the solution to this problem. The sphere segment shoud be done after adding the skin segment. To my understanding, mask volume is Blank out the selected skin segment.</p>

---
