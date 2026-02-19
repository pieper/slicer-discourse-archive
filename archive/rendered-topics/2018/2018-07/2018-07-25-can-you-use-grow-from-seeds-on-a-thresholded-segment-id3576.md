---
topic_id: 3576
title: "Can You Use Grow From Seeds On A Thresholded Segment"
date: 2018-07-25
url: https://discourse.slicer.org/t/3576
---

# Can you use grow from seeds on a thresholded segment

**Topic ID**: 3576
**Date**: 2018-07-25
**URL**: https://discourse.slicer.org/t/can-you-use-grow-from-seeds-on-a-thresholded-segment/3576

---

## Post #1 by @Shamay_Agaron (2018-07-25 18:27 UTC)

<p>In the segment editor, is it possible to apply grow from seeds not only to the master volume, but directly onto a thresholded segment?</p>

---

## Post #2 by @lassoan (2018-07-25 18:59 UTC)

<p>You can export the segment to a labelmap volume and use that as master volume.</p>
<p>What is your use case? What problem would you like to solve?</p>

---

## Post #3 by @Shamay_Agaron (2018-07-25 19:32 UTC)

<p>I’m looking at a fractured humerus and I would like to generate a workflow that semi-automatically recognizes the different fracture pieces and separates them as distinct segments. They are visually very island-like but they still have connections to the larger bone in many cases, which makes the ‘Grow from seeds’ functionality fail for me</p>

---

## Post #4 by @lassoan (2018-07-25 20:38 UTC)

<p>That question is already discussed in <a href="https://discourse.slicer.org/t/segmenting-fractured-bone-fragments/3575/2">this topic</a>, let’s just continue the discussion there.</p>

---
