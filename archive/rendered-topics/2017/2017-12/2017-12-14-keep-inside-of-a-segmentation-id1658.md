# Keep Inside of a segmentation

**Topic ID**: 1658
**Date**: 2017-12-14
**URL**: https://discourse.slicer.org/t/keep-inside-of-a-segmentation/1658

---

## Post #1 by @LESAUNIER_Thibault (2017-12-14 10:34 UTC)

<p>Hello,</p>
<p>I have a medical model. I know how to make a 3D model from it but the segmentation give me only the surface of my model. It’s possible to keep the inside of a segmentation in Slicer ?</p>
<p>Thanks</p>

---

## Post #2 by @cpinter (2017-12-14 14:43 UTC)

<p>It’s not clear to me what would you like to do. Crop the anatomical volume based on a segment (i.e. use it as a mask)? Or save the segmentation as a labelmap volume?</p>

---

## Post #3 by @LESAUNIER_Thibault (2017-12-14 14:59 UTC)

<p>I’m sorry. It’s difficult for me to explain my problem.</p>
<p>So, I use slicer to save a labelmap volume using Segmentation tool. Then, I use this volume in Unity. And I did it.</p>
<p>The problem is that the segmentation give me only the contour of my volume. If I apply a cut plane on my object, it is hollow (for example)<br>
My question is :<br>
-Is it possible to export a full 3D volume from Slicer ?</p>
<p>Thanks</p>

---

## Post #4 by @lassoan (2017-12-14 15:19 UTC)

<p>Labelmaps and surface meshes are uniform/hollow inside. If you want to cut into the labelmap/mesh and see volume intensities (not just a plain cross-section) then you need to blank out areas of the volume that are outside your segment and visualize this grayscale volume in Unity using volume rendering. You can buy volume renderer for Unity in the asset store for a few 10$.</p>
<p>If you need something else then please give a bit more information about your project, what is the end goal and what is the specific goal that you would like to achieve (what exactly you would like to see when you cut into the object).</p>

---
