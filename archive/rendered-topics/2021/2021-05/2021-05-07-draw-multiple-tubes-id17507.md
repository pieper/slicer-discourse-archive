---
topic_id: 17507
title: "Draw Multiple Tubes"
date: 2021-05-07
url: https://discourse.slicer.org/t/17507
---

# Draw multiple tubes

**Topic ID**: 17507
**Date**: 2021-05-07
**URL**: https://discourse.slicer.org/t/draw-multiple-tubes/17507

---

## Post #1 by @Luca (2021-05-07 13:36 UTC)

<p>Hi,</p>
<p>I am using Slicer 4.11.20210226 on Windows 10.<br>
Is it possible to use the “Draw tube” tool to define more than one tube on the same mask? As far as I tested, once seeds have been placed, the “apply” button creates a tube on the current segmentation but also erase the previous content. Is there any shortcut I miss?</p>
<p>Thank you in advance,<br>
Luca</p>

---

## Post #2 by @lassoan (2021-05-13 04:56 UTC)

<p>You can draw any number of tubes, each in a new segment. In the end you can combine them, for example by using Logical operators effect:</p>
<ul>
<li>set Operation → Fill</li>
<li>set Bypass masking → disabled</li>
<li>set Masking (at the bottom) / Editable area → Inside all segments</li>
<li>click Apply</li>
</ul>

---
