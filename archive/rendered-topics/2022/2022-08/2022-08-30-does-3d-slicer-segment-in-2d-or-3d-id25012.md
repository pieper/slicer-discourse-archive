# Does 3D Slicer segment in 2D or 3D?

**Topic ID**: 25012
**Date**: 2022-08-30
**URL**: https://discourse.slicer.org/t/does-3d-slicer-segment-in-2d-or-3d/25012

---

## Post #1 by @O123456789 (2022-08-30 17:51 UTC)

<p>Hello,</p>
<p>I was asked if 3D slicer works in 2D or in 3D, but i wasn’t sure how to answer that.</p>
<p>Does the semiautomatic segmentation work on a single slice and then move to the next one or does it spread in all three dimensions evenly?</p>
<p>Thanks.</p>

---

## Post #2 by @lassoan (2022-08-30 17:59 UTC)

<p>In general, all data structures in 3D Slicer are in 3D: a “2D” image slice is just a single-slice 3D volume, a planar polygon just happens to be a 3D mesh with all of its points located in one plane, etc. This sets apart 3D Slicer from most of the medical image viewer/analysis applications, that are mostly operate on 2D image slices.</p>
<p>Not just the data structures are 3D, but all operations and their parameters are defined in 3D, in physical space. All segmentation tools operate in 3D (with the exception of “Level tracing” effect in Segment Editor, and maybe there are 1-2 more), segmenting a 3D regions instead of going slice by slice along some image axis.</p>

---
