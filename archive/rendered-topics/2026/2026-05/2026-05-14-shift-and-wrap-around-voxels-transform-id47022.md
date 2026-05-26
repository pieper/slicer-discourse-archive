---
topic_id: 47022
title: "Shift and wrap-around voxels transform"
date: 2026-05-14
url: https://discourse.slicer.org/t/47022
last_bumped: 2026-05-18T21:55:33.203Z
---

# Shift and wrap-around voxels transform

**Topic ID**: 47022
**Date**: 2026-05-14
**URL**: https://discourse.slicer.org/t/shift-and-wrap-around-voxels-transform/47022

---

## Post #1 by @brizolara.lt (2026-05-14 06:43 UTC)

<p>Hi all,</p>
<p>I would like to apply a shift in a definite direction (in my case, X) to the voxel values (not the coordinates) of a volume - keeping, thus, origin, spacing and dimensions intact.</p>
<p>Also, I would like to wrap around the voxels that were shifted outside of the region - i.e., if I’m shifting the voxels to the right, the ones that would fall outside of the region start to appear at the other side.</p>
<p>I am trying to use a GridTransform, but I know I’ll have a problem at the wrap around border. Also, it’s a dense transform and what I need is really a manipulation of voxels.</p>
<p>Maybe a custom transform in C++ is the way? Or is there any solution at the Python level?</p>
<p>I would love to know your thought on this. Thanks in advance,</p>
<p>Tiago</p>

---

## Post #2 by @pieper (2026-05-14 13:24 UTC)

<p>You can do almost anything with fancy numpy indexing.  It can be a challenge to find the right recipe, but you should be able to easily iterate and inspect the results until you get what you want.  Look in the script repository for examples and use LLMs to help with the syntax.</p>

---

## Post #3 by @brizolara.lt (2026-05-18 18:04 UTC)

<p>Hi, Steve, thanks for the answer.</p>
<p>Yes, I implemented the algorithm in Python, but - now I noticed I didn’t specify here -, I would like this to be a MRMLTransform to take advantage of Slicer’s infrastructure.</p>
<p>I tried a GridTransform, but the wrap around seems problematic. Then, I have to implement a custom transform. Is it possible to implement a custom MRMLTransform in Python (I’m afraid it’s not)?</p>

---

## Post #4 by @brizolara.lt (2026-05-18 18:11 UTC)

<p>Just to clarify the specific use case a bit further: the goal is actually to perform this circular shift (conceptually similar to numpy.roll) strictly on the view, while keeping the underlying data of the original volume completely intact and unmodified.</p>
<p>Ideally, we would like the user to be able to apply standard segmentation tools directly onto this visually shifted view, but have the resulting segmentation automatically map back to the unshifted, original volume coordinates.</p>
<p>Since using numpy indexing to roll the array would actually alter the underlying volume data (or create a new volume entirely), we are trying to find a way to make this purely a display/transform level operation…</p>

---

## Post #5 by @mikebind (2026-05-18 21:55 UTC)

<p>I’m not sure a custom transform will give you what you want either; I don’t think you can use segment editor tools on a nonlinearly transformed source image, which means you would need to harden the transform, which is, if I understand correctly, exactly what you are trying to avoid.</p>
<p>What about just duplicating your image in the desired direction? For example, if your image is X by Y by Z and you want to be able to roll over the edge in the X direction, just concatenate 3 copies of your image to make a new version which is 3X by Y by Z. Then, you could just have an update function which runs on a QTimer and periodically gets the union of the 3 segmentation regions, and copies that union back to each of the 3 regions (thereby transferring any newly added segmented areas to the other two copies. Then, when the user is done, you can just grab one of the sections, and that would be an appropriate segmentation of the original volume. In this scheme, you could start from the center section and roll off either X edge without interruption.  You wouldn’t be able to go indefinitely in either direction, but it’s hard for me to imagine why it would be helpful or necessary to loop around multiple times.</p>

---
