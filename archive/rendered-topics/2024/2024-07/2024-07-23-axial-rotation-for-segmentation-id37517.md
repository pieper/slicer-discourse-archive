---
topic_id: 37517
title: "Axial Rotation For Segmentation"
date: 2024-07-23
url: https://discourse.slicer.org/t/37517
---

# Axial rotation for segmentation

**Topic ID**: 37517
**Date**: 2024-07-23
**URL**: https://discourse.slicer.org/t/axial-rotation-for-segmentation/37517

---

## Post #1 by @Noa (2024-07-23 12:24 UTC)

<p>Hello,<br>
I’m trying to flip a 180° segmentation around its Y axis. However, the transform module doesn’t seem to allow me to do this. Does anyone know what command I can use to flip my segment?<br>
Thank you in advance.</p>

---

## Post #2 by @lassoan (2024-07-23 17:59 UTC)

<p>Would you like to actually change the physical location of the segmentation (for example, to spatially align with another image or segmentation)? You can then apply a transform. Note that applying a simple transform for rotating a segmentation will not change the voxel data, just update the orientation in the image header.</p>
<p>If you just want to modify how the image appears in a slice view (flip/rotate) then you can use flip and rotate buttons in the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/reformat.html#panels-and-their-use">Reformat module</a>.</p>

---

## Post #3 by @Noa (2024-07-24 07:00 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/69c0391338a91fd0c1c0636633fd559cb7834314.png" alt="image" data-base62-sha1="f5vY9k0gL8fzle47LXQxyw0H1Xu" width="564" height="321"><br>
Well I try to flip arround the yellow segmentation so it aligns with the blue one.<br>
Thank you for your quick answer!</p>

---

## Post #4 by @Noa (2024-07-24 09:23 UTC)

<p>by the way I try to do this with Python <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---
