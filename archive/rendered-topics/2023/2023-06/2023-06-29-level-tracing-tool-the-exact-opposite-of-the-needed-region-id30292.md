---
topic_id: 30292
title: "Level Tracing Tool The Exact Opposite Of The Needed Region"
date: 2023-06-29
url: https://discourse.slicer.org/t/30292
---

# Level tracing tool; the exact opposite of the needed region

**Topic ID**: 30292
**Date**: 2023-06-29
**URL**: https://discourse.slicer.org/t/level-tracing-tool-the-exact-opposite-of-the-needed-region/30292

---

## Post #1 by @Dima_Harba (2023-06-29 02:39 UTC)

<p>Hello!<br>
I am using the level tracing tool to segment brain tumors but it keeps selecting the exact opposite of the desired region. Is there any way to make the “mouse move " select my deisred region instead? i;e: " 1- the current selection by the level tracing tool”</p>
<p>Thank you for your help!</p>

---

## Post #2 by @pieper (2023-06-29 09:29 UTC)

<p>You can use the Invert operation in the Logical Operators tool of the Segment Editor, but it applies to the whole volume and not just a slice.  Change Island in the Islands effect might be easier.  But in general the Level Tracing tool is hard to use for volume segmentation.  Better to try Grow from Seeds or Watershed.</p>

---

## Post #3 by @Dima_Harba (2023-07-01 18:17 UTC)

<p>Yes thank you, The grow from seeds option was best!</p>

---
