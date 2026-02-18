# Rotating and resampling volumes with Python

**Topic ID**: 9089
**Date**: 2019-11-08
**URL**: https://discourse.slicer.org/t/rotating-and-resampling-volumes-with-python/9089

---

## Post #1 by @Prashant_Pandey (2019-11-08 17:31 UTC)

<p>I’ve written a very simple python scrited module which sums a CT image’s along one of the 3 given axes to create a DRR-like image. However I want to extend this module to sum along an abitrary axis through the image instead of only the orthogonal directions.</p>
<p>I think the best way to approach this would be to use one of the resample image modules? Is there a better way of doing this - perhaps directly in numpy instead of borrowing another module’s logic? Thanks!</p>

---

## Post #2 by @pieper (2019-11-08 18:16 UTC)

<p>Probably the easiest is to apply a transform to the volume (rotation) and then resample using <code>Resample Image (brains)</code> as a CLI from python.  Probably put it in a new volume so you can repeat with arbitrary directions.</p>

---

## Post #3 by @haruki.9direction.ne (2023-07-21 06:43 UTC)

<p>I rotated the mr image using a rotation matrix.<br>
How can the voxel resolution or size be recalculated in this process?<br>
Thank you</p>

---

## Post #4 by @lassoan (2023-07-21 14:02 UTC)

<p>This example <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#extracting-volume-patches-around-segments">script for extracting oriented boxes from a volume</a> should help (maybe it does exactly what you want).</p>

---
