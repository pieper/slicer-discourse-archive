# Segmentation Edit Tools Stop Working After Transforming Volume

**Topic ID**: 24039
**Date**: 2022-06-25
**URL**: https://discourse.slicer.org/t/segmentation-edit-tools-stop-working-after-transforming-volume/24039

---

## Post #1 by @chris_nik (2022-06-25 02:29 UTC)

<p>Hello,</p>
<p>I noticed that when I use the “Transforms” Module (create new linear transform → harden transform) to rotate my volume around the vertical and sagittal axes 2° each the following problem occurs: the Draw, Paint, Erase etc. functions of the “Segment Editor” Module stop working in certain small areas of the volume.</p>
<p>For now the problem occurs only when I first transform the volume first and then create a segmentation and start segmenting. However I just wanted to give feedback.</p>
<p>P.s I love 3D Slicer, thank you so much for your work!</p>
<p>Kind regards</p>

---

## Post #2 by @lassoan (2022-06-25 03:57 UTC)

<p>By applying a transform to the master volume you move the master volume but you don’t change the geometry (origin, spacing, axis directions, extents) of your segmentation. Since you can only paint within the extent of your segmentation, it is expected that you will not be able to paint in certain parts of the moved master volume.</p>
<p>If you change the segmentation geometry to match the transformed master volume (or it encompasses the transformed master volume) then you’ll be able to paint everywhere.</p>
<p>See more details in the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#panels-and-their-use">Segment Editor documentation</a>.</p>

---

## Post #3 by @chris_nik (2022-06-25 12:45 UTC)

<p>I see, thank you very much for your answer! Indeed when I first create the segmentation and then transform the volume it works fine : )</p>

---
