---
topic_id: 7814
title: "Error With Flood Fill In The Nightly"
date: 2019-07-30
url: https://discourse.slicer.org/t/7814
---

# Error with flood fill in the nightly

**Topic ID**: 7814
**Date**: 2019-07-30
**URL**: https://discourse.slicer.org/t/error-with-flood-fill-in-the-nightly/7814

---

## Post #1 by @muratmaga (2019-07-30 13:58 UTC)

<p>I am getting this error when I try to use the flood fill with the editable intensity range option enabled with the MRHead.nrrd. Things work fine when the editable intensity range is unchecked.</p>
<p>Switch to module:  “SegmentEditor”<br>
Execute: image ScalarType (4) must match out ScalarType (4), and mask scalar type (4) must be unsigned char.</p>

---

## Post #2 by @lassoan (2019-07-30 16:13 UTC)

<p>Masking was not implemented for Flood fill effect. I’ve added it and will be available in releases downloaded tomorrow or later.</p>

---

## Post #3 by @muratmaga (2019-07-30 17:03 UTC)

<p>Thanks Andras!!!</p>

---

## Post #4 by @muratmaga (2019-08-02 21:34 UTC)

<p>Hi Andras,<br>
I just tried with today’s preview (on Linux), and I am still getting this error message.</p>
<p><strong>Execute: image ScalarType (4) must match out ScalarType (4), and mask scalar type (4) must be unsigned char.</strong></p>

---

## Post #5 by @lassoan (2019-08-02 23:18 UTC)

<p>I could reproduce and fix the problem in the Preview Release (r28426).</p>

---
