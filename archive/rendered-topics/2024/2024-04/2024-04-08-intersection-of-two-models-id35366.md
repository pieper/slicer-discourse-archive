---
topic_id: 35366
title: "Intersection Of Two Models"
date: 2024-04-08
url: https://discourse.slicer.org/t/35366
---

# Intersection of two models

**Topic ID**: 35366
**Date**: 2024-04-08
**URL**: https://discourse.slicer.org/t/intersection-of-two-models/35366

---

## Post #1 by @Noa (2024-04-08 21:13 UTC)

<p>Hello,<br>
I would like to model in 3D the intersection of my two contours: “scinti” and “tep”. I’ve tried to do this with the “segment editor” module and the intersect option, but when I press apply, nothing happens. What should I do?<br>
thanks in advance<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/886dcdbf847c99cf380e791ce818241ba85fd245.png" alt="image" data-base62-sha1="jsUbJMSxLrIYWBJz06RzfWuEQAt" width="614" height="438"></p>

---

## Post #2 by @lassoan (2024-04-08 21:18 UTC)

<p>There is no need to create a new “intersection” segment. Intersection result will be stored in the current segment (that is selected at the segment list at the top).</p>

---

## Post #3 by @Noa (2024-04-09 08:43 UTC)

<p>Thank you for your answer. But how do I visualize in 3D this intersection?</p>

---

## Post #4 by @cpinter (2024-04-09 12:47 UTC)

<p>I’ve made a short video about using the intersection tool. I hope this answers your questions. If you want the intersection to be in a new segment then you can first use the <code>Copy</code> mode of the <code>Logical operators</code> effect to copy one of the segments and do the intersection using that as current segment.</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78cd81cf255813832a5f6ca6727f741401ad15c4.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/68773fd5b938f44af1e254fb94187344fbcae866.jpeg">
  </div><p></p>

---
