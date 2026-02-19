---
topic_id: 34728
title: "Segment Endocast"
date: 2024-03-05
url: https://discourse.slicer.org/t/34728
---

# Segment endocast

**Topic ID**: 34728
**Date**: 2024-03-05
**URL**: https://discourse.slicer.org/t/segment-endocast/34728

---

## Post #1 by @ferpaiva (2024-03-05 22:58 UTC)

<p>How can I segment endocast? I’m interested to segment out the inner ear of the frog</p>

---

## Post #2 by @lassoan (2024-03-05 23:00 UTC)

<p>You can use Wrap Solidify effect in Segment Editor (provided by SurfaceWrapSolidify extension). Choose the extract cavity mode.</p>

---

## Post #3 by @ferpaiva (2024-03-05 23:06 UTC)

<p>Thank you for replying, Andras!</p>
<p>Would it work if the cavity is not fully closed?</p>

---

## Post #4 by @lassoan (2024-03-06 20:12 UTC)

<p>Yes. You can specify a size limit, and all openings below that size will be closed.</p>

---

## Post #5 by @muratmaga (2024-03-06 20:14 UTC)

<p>There is a utility module in SlicerMorph called Segment Endocast that’s based on wrap solidfy effect, if you want to give it a try.</p>
<p>You can enter the large hole size to be covered.</p>

---
