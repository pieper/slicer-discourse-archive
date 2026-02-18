# Simultaneous T1 STIR eDWI segmentation

**Topic ID**: 5041
**Date**: 2018-12-11
**URL**: https://discourse.slicer.org/t/simultaneous-t1-stir-edwi-segmentation/5041

---

## Post #1 by @RuudStap (2018-12-11 14:44 UTC)

<p>Hi,</p>
<p>I have used another segmentation program: Velocity prior to 3D Slicer, where I was able to simulateously view T1, STIR and DWI (only axial views) series during segmentation. Is this a possibility in 3D Slicer?</p>
<p>Regards,</p>
<p>Ruud</p>

---

## Post #2 by @gcsharp (2018-12-11 15:01 UTC)

<p>Yes, but only two images are available in any view window.  For example, you can view T1 and STIR in the red view window, while simultaneously viewing T1 and DWI in the yellow view window.</p>

---

## Post #3 by @lassoan (2018-12-12 01:03 UTC)

<p>Slicer can synchronize multiple views by enabling “hotlink”, you also have linked cursor, and you can segment in any of the views, using any of the input volumes.</p>

---
