---
topic_id: 5761
title: "Transform Extract Translation Only"
date: 2019-02-13
url: https://discourse.slicer.org/t/5761
---

# Transform: Extract translation only

**Topic ID**: 5761
**Date**: 2019-02-13
**URL**: https://discourse.slicer.org/t/transform-extract-translation-only/5761

---

## Post #1 by @miniBin (2019-02-13 17:40 UTC)

<p>Hello is there a way to extract the translation data only from a transform matrix. I have a transform between two scans but I only need to see the translation. How do I do this? Thank you.</p>

---

## Post #2 by @pieper (2019-02-13 19:49 UTC)

<p>The translation is just the first three rows of the last column of the 4x4 matrix.</p>

---

## Post #3 by @miniBin (2019-02-14 19:26 UTC)

<p>I cannot find the transformation matrix. I used ElastiX to register two different frames.</p>
<p>Usually the matrix just shows up in the transforms module but it is not there?</p>

---

## Post #4 by @lassoan (2019-02-14 20:56 UTC)

<p>Unfortunately, from Elastix we can only get a displacement field from Elastix. Either Elastix would need to be improved to save transform in standard ITK file format (<a href="https://github.com/SuperElastix/elastix/issues/18" rel="nofollow noopener">https://github.com/SuperElastix/elastix/issues/18</a>) or SlicerElastix module would need to be improved to be able to parse Elastix proprietary transform file format.</p>

---

## Post #5 by @miniBin (2019-02-14 21:15 UTC)

<p>No problem and thank you for the clarification! I can still play around with the displacement field for my purposes.</p>
<p>Many thanks.</p>

---
