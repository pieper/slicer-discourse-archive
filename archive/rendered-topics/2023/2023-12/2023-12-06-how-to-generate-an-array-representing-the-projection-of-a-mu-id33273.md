---
topic_id: 33273
title: "How To Generate An Array Representing The Projection Of A Mu"
date: 2023-12-06
url: https://discourse.slicer.org/t/33273
---

# how to generate an array representing the projection of a multileaf collimator (MLC) field onto a CT slice in 3D Slicer?

**Topic ID**: 33273
**Date**: 2023-12-06
**URL**: https://discourse.slicer.org/t/how-to-generate-an-array-representing-the-projection-of-a-multileaf-collimator-mlc-field-onto-a-ct-slice-in-3d-slicer/33273

---

## Post #1 by @Meryeme_Bellahsaouia (2023-12-06 23:27 UTC)

<p>I am trying to create an array with the same dimensions as a CT slice. Within this array, each voxel will have a value of 1 if it falls inside the MLC field and 0 if it falls outside.</p>
<p>Is this achievable using 3D Slicer?</p>

---

## Post #2 by @lassoan (2023-12-06 23:33 UTC)

<p>I think we are already beyond this. <a class="mention" href="/u/mik">@Mik</a> has implemented support for beams with MLC in SlicerRT extension. I would recommend you to check out SlicerRT extension and come back here with any questions that yo may have.</p>

---
