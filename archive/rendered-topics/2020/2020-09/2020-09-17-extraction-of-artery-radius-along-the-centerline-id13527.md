# Extraction of artery radius along the centerline 

**Topic ID**: 13527
**Date**: 2020-09-17
**URL**: https://discourse.slicer.org/t/extraction-of-artery-radius-along-the-centerline/13527

---

## Post #1 by @irnjsn (2020-09-17 12:39 UTC)

<p>Hi everyone,</p>
<p>I realized a segmentation of the femoral artery and used Extract Centerline to obtain the coordinates of the centerline. The data extracted from this centerline gives a radius (I guess an average one) of the complete artery.<br>
I would like to be able to know the radius of the arteries at any point of my centerline, how can I do that?<br>
I extracted the position of each point defining the centerline but cannot find how to obtain the radius for each of this point.</p>
<p>Thank you !</p>

---

## Post #2 by @lassoan (2020-09-17 12:41 UTC)

<p>If you output the extracted centerline as a model then radius is available as point data. See <a href="https://github.com/vmtk/SlicerExtension-VMTK#examples">Examples section of VMTK extension documentation</a> for details.</p>

---
