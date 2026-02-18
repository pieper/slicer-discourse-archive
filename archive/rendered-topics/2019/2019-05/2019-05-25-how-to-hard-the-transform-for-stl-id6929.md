# How to hard the transform for stl?

**Topic ID**: 6929
**Date**: 2019-05-25
**URL**: https://discourse.slicer.org/t/how-to-hard-the-transform-for-stl/6929

---

## Post #1 by @timeanddoctor (2019-05-25 16:41 UTC)

<p>[1, 0, 0, 2],<br>
[0, 1, 0, 2],<br>
[0, 0, 1, 2],<br>
[0, 0, 0, 0.01]</p>
<p>the “0.01” seems not work in slicer and cannot save as well as.</p>

---

## Post #2 by @lassoan (2019-05-25 17:08 UTC)

<p>You must not change the last row of the transform (it would create transforms that violate assumptions in VTK and ITK filters). There is a ticket for making the last row read-only but we have not come around to implement it yet.</p>
<p>What would you like to achieve by modifying the last row?</p>

---

## Post #3 by @timeanddoctor (2019-05-26 04:12 UTC)

<p>I want to scale the group stl file, but never change the relationship location and then display it in the 3d slicer</p>

---

## Post #4 by @lassoan (2019-05-26 11:49 UTC)

<p>Scaling transform is:</p>
<pre><code class="lang-auto">ScaleX 0 0 0
0 ScaleY 0 0
0 0 ScaleZ 0
0 0 0      1
</code></pre>

---
