---
topic_id: 19569
title: "Segment Statistics From Each Slice"
date: 2021-09-08
url: https://discourse.slicer.org/t/19569
---

# Segment statistics from each slice

**Topic ID**: 19569
**Date**: 2021-09-08
**URL**: https://discourse.slicer.org/t/segment-statistics-from-each-slice/19569

---

## Post #1 by @melindamareesmith (2021-09-08 13:02 UTC)

<p>Hello,<br>
I can see how to extract mean scalar value for a segment from the segment statistics, but what I would like to do is extract this for each MRI slice- in a similar way to how the segment cross-sectional area outputs area for each slice. Is it possible?<br>
Thank you</p>

---

## Post #2 by @lassoan (2021-09-08 15:10 UTC)

<p>Can you write a bit about your use case? What is the clinical application?</p>
<p>You can implement this either in a short Python script or enhance the Segment cross-sectional area module to take an additional input volume and get the mean value for each slice (it is a single line of Python code to get average intensity of a masked volume at a specific slice, you just need to propagate the selected volume to the <code>run</code> method and save the result in an additional table in the column).</p>

---

## Post #3 by @melindamareesmith (2021-09-08 21:04 UTC)

<p>Thank you for your reply. I am wanting to use the mean intensity from fat/water MRI to calculate muscle fat infiltration. I can see this is possible from the segment statistics output, however I want to examine this slice-by-slice in addition to whole segment (muscle) that the segment statistics allows.</p>

---
