# Measure tumor and edema volume

**Topic ID**: 2290
**Date**: 2018-03-11
**URL**: https://discourse.slicer.org/t/measure-tumor-and-edema-volume/2290

---

## Post #1 by @joaomarto (2018-03-11 23:53 UTC)

<p>Hello,</p>
<p>I am using for the first time the 3D slicer software and I am having difficulty in calculating cerebral tumors volumes. Also I would link to measure the surrounding edema volume.</p>
<p>What is the best way to do it?</p>
<p>Thank you in advance.</p>
<p>Kind Regards,</p>
<p>João Marto</p>

---

## Post #2 by @lassoan (2018-03-12 05:42 UTC)

<p>You can segment the tumor and edema using Segment editor module (I would recommend trying Grow from seeds effect), then compute volume using Segment statistics module.</p>

---
