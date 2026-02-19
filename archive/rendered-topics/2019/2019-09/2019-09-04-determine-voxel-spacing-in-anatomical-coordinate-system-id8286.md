---
topic_id: 8286
title: "Determine Voxel Spacing In Anatomical Coordinate System"
date: 2019-09-04
url: https://discourse.slicer.org/t/8286
---

# Determine voxel spacing in anatomical coordinate system

**Topic ID**: 8286
**Date**: 2019-09-04
**URL**: https://discourse.slicer.org/t/determine-voxel-spacing-in-anatomical-coordinate-system/8286

---

## Post #1 by @Leon (2019-09-04 09:15 UTC)

<p>Who can explain this to me?</p>
<p>In the ‘Volumes’ module, the dimensions are displayed in three columns. If I understand it correctly (but correct me if I’m wrong), then the order from left to right is axial - coronal - sagital, or should I use the IJK space?</p>
<p>However, when I do a resampling using ‘Resample Scalar Volume’, then the spacing parameters are in a different order! They even differ depending on the type of scan!</p>
<p>I’ve tested this using the ’CTChest’ and the ‘MRHead’ sample.<br>
With CTChest the effect from left to right is: sagital - coronal - axial.<br>
With MRHead the effect from left to right is: coronal - axial - sagital.</p>
<p>Or do I have to use the IJK space, because this is not clear to me? It’s not displayed above the columns in the ‘Volumes’ module and also not mentioned in the ‘Resample Scalar Volume’ module. The manual also doesn’t give a definite, clear answer about this.</p>
<p>Btw, I find the manuals generally difficult to understand. But perhaps that’s because  I may not be smart enough. <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=9" title=":wink:" class="emoji" alt=":wink:"></p>
<p>Greeting,<br>
Léon</p>

---

## Post #2 by @Leon (2019-09-04 11:35 UTC)

<p>I thought I had figured it out that the (default) spacing parameters 0,0,0 in the ‘resample Scalar Volume’ stand for the axial view, sagital view and coronal view, but I was wrong. Apparently that also depends on the scanning direction. Does it?</p>
<p>Why isn’t that mentioned somewhere in the manual or help?</p>

---

## Post #3 by @lassoan (2019-09-04 13:15 UTC)

<p>Spacing of a volume typically refers to column norms of the IJKToRAS transformation matrix (or IJKToLPS, or IJK to any physical coordinate system - the column norm value is always the same). This convention is followed in all basic libraries 3D Slicer is based on, most notably ITK and VTK.</p>
<p>In short, spacing specifies the volume voxel size along the volume’s I, J, K axes.</p>
<p>Since these axes can be defined in arbitrary directions in space, spacing along a physical axis (such as axial, coronal, sagittal) may not be even clearly defined.</p>
<p>If your volume axes are aligned with anatomical axes then you can find the closest voxel axis by transforming the anatomical direction by RASToIJK and get the norm of that axis. For the general case, when volume axes can be arbitrarily rotated in physical space, then you may use the radius of an ellipsoid that is fit inside the volume voxel.</p>

---
