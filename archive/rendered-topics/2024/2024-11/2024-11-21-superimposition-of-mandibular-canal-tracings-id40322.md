# Superimposition of mandibular canal tracings 

**Topic ID**: 40322
**Date**: 2024-11-21
**URL**: https://discourse.slicer.org/t/superimposition-of-mandibular-canal-tracings/40322

---

## Post #1 by @Swarna_Yerebairapura (2024-11-21 22:20 UTC)

<p>This pertains to the superimposition of mandibular canal tracings performed in three different CBCT software programs. I aim to import DICOM files with mandibular canal tracings into 3D Slicer. However, in all the CBCT software these tracings are only visible in the panoramic reconstruction (2D) view and not in the MPR planes. Is it possible to superimpose these mandibular canal tracings in 3D Slicer even though they appear only in panoramic reconstruction (2D) view ?</p>

---

## Post #2 by @lassoan (2024-11-21 22:23 UTC)

<p>Yes! The amazing and unique property of Slicer’s Curved Planar Reformat feature that it is implemented via an invertible spatial transform. It means that if you draw anything in the straightened space you can bring it back into the original space by a few clicks (applying the inverse if the straightening transform to the object that you defined in the straightened space).</p>

---
