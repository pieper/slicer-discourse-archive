---
topic_id: 23996
title: "Segment In Different Sequences"
date: 2022-06-22
url: https://discourse.slicer.org/t/23996
---

# Segment in different sequences

**Topic ID**: 23996
**Date**: 2022-06-22
**URL**: https://discourse.slicer.org/t/segment-in-different-sequences/23996

---

## Post #1 by @miuwells (2022-06-22 07:53 UTC)

<p>Hello everyone,</p>
<p>I have a question that I don’t know if it could be solved.<br>
I have two sequences, one with 0.4mm Z spacing and one with 1.25mm. I see that the size of the brush adjusts to the size of the slice of each sequence.<br>
My question is, could you paint with the 0.4mm brush size visualizing the 1.25mm sequence and then apply fill between slices to automatically complete the segmentation and get a more accurate model?<br>
Thank you very much for your help.</p>

---

## Post #2 by @lassoan (2022-06-22 13:16 UTC)

<p>Yes, you can fill between slices automatically using “Fill between slices” effect. Brush thickness is automatically set to the <em>background</em> volume spacing by default. If you want to change that then you can set the spacing manually using the <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-view">slice view controls</a>; or you can keep your <em>background</em> volume the high-resolution volume and just display the lower-resolution volume over it as <em>foreground</em> volume.</p>

---
