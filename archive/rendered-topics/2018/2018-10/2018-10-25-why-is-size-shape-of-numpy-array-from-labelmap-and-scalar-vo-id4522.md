---
topic_id: 4522
title: "Why Is Size Shape Of Numpy Array From Labelmap And Scalar Vo"
date: 2018-10-25
url: https://discourse.slicer.org/t/4522
---

# Why is size/shape of numpy array from labelmap and scalar volume not the same?

**Topic ID**: 4522
**Date**: 2018-10-25
**URL**: https://discourse.slicer.org/t/why-is-size-shape-of-numpy-array-from-labelmap-and-scalar-volume-not-the-same/4522

---

## Post #1 by @mag (2018-10-25 00:04 UTC)

<p>Hi,</p>
<p>I want to export my volume and segmentation into numpy arrays so that I can use them for further analysis. I did as explained in this <a href="https://discourse.slicer.org/t/segment-binarylabelmap-to-numpy-array/778">post</a> and it seems to work but I don’t quite understand why the arrays I obtain do not have the same shape and size. I thought the labelmap would have the same geometry of my volume, just with the scalar units replaced by binary labels where I have placed a segment and some null-value elsewhere. Can somebody clarify?</p>
<p>Thank you</p>

---

## Post #2 by @lassoan (2018-10-25 02:42 UTC)

<p>Size of voxel array is always the minimum necessary size to store that segment. You can convert between physical position and array index as shown in this example in the script repository: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_centroid_of_a_segment_in_world_.28RAS.29_coordinates">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_centroid_of_a_segment_in_world_.28RAS.29_coordinates</a></p>

---
