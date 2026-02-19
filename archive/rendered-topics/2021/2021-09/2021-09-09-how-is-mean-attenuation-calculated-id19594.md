---
topic_id: 19594
title: "How Is Mean Attenuation Calculated"
date: 2021-09-09
url: https://discourse.slicer.org/t/19594
---

# How is mean attenuation calculated?

**Topic ID**: 19594
**Date**: 2021-09-09
**URL**: https://discourse.slicer.org/t/how-is-mean-attenuation-calculated/19594

---

## Post #1 by @Mark_Brahier (2021-09-09 12:47 UTC)

<p>How does 3D slicer calculate the output ‘mean attenuation’? For example, I select the range of -190 to -30 HU to capture adipose tissue, and I am interested in both the volume and mean attenuation. I always assumed that ‘mean’ references to the average attenuation value for each individual pixel identified within that -190 to -30 range, but I would appreciate it if someone could clarify/explain. Thanks!</p>

---

## Post #2 by @lassoan (2021-09-10 03:32 UTC)

<p>The “Mean” column of Segment statistics module output table contains the mean value of all voxel values in the segment’s region.</p>

---

## Post #3 by @Mark_Brahier (2021-09-13 12:38 UTC)

<p>Thank you. Would you be able to share the Python code for attenuation, both the code for volume within an attenuation range and for mean attenuation?</p>

---

## Post #4 by @Mark_Brahier (2021-09-16 22:37 UTC)

<p>Just following this again again… would you be able to link me to the Python code for this? Thank you!!</p>

---

## Post #5 by @lassoan (2021-09-17 13:52 UTC)

<p>Segment statistics module is implemented in Python (see <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/SegmentStatistics/SegmentStatistics.py">source code</a>). You can either use VTK or ITK filters or numpy (get the voxels as a numpy array, use masking to get the voxels in the segment’s region, and get the mean by calling the <code>mean</code> method of the masked array).</p>

---
