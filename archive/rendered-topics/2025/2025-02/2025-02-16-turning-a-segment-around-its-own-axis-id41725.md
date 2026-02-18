# Turning a segment around it's own axis

**Topic ID**: 41725
**Date**: 2025-02-16
**URL**: https://discourse.slicer.org/t/turning-a-segment-around-its-own-axis/41725

---

## Post #1 by @Nastia_Kfir (2025-02-16 17:37 UTC)

<p>Hi! i’ve been trying unsucsessfully to understand how can i turn a segment around it’s own axis, but all iv’e managed to find is rotating the segment around the axis of the slice in the transformation module.<br>
GPT and gemini weren’t helpful, all i got from them is how to find the central coordinateds of my segment.<br>
is there a way to turn a segment around it’s own axis and not the axis of the slice?</p>

---

## Post #2 by @lassoan (2025-02-16 17:38 UTC)

<p>In latest Slicer version (5.8 and later) you can specify any point as center of rotation in Transforms module.</p>

---

## Post #3 by @Nastia_Kfir (2025-02-19 08:53 UTC)

<p>thank you very much!</p>

---

## Post #4 by @philippepellerin (2025-02-20 16:33 UTC)

<p>But if you aim to rotate an isolated segment, you can’t. You must move the whole segmentation at the same time.<br>
If you want to move an isolated segment, then you need to export it first to a model, and you will be able to move the model isolated.</p>

---
