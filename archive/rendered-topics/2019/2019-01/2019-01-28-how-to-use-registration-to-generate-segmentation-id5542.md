# How to Use Registration to Generate Segmentation

**Topic ID**: 5542
**Date**: 2019-01-28
**URL**: https://discourse.slicer.org/t/how-to-use-registration-to-generate-segmentation/5542

---

## Post #1 by @miniBin (2019-01-28 15:39 UTC)

<p>Hello, I have several volumes in a sequence that I would like to segment. If I segment the first volume, how do I use registration to segment the rest of them with the same number of nodes and mesh elements?</p>
<p>What I tried:</p>
<ul>
<li>
<p>Import two separate volumes Frame 0 and Frame 8.</p>
</li>
<li>
<p>Use Elastix to find transform.</p>
</li>
<li>
<p>Go to transform and apply to masked Frame 0.</p>
</li>
</ul>
<p>It seems to change but I do not know if it is correct. I want to keep number of points between each frame the same but idk if this is happening?</p>
<p>Thank you for any answers.</p>

---

## Post #2 by @lassoan (2019-01-29 01:08 UTC)

<p>What you describe sounds correct. You need to pay attention to trivial details, such as computing the transform in the correct direction and test if the registration is robust and accurate enough (based on qualitative assessment using transform visualization, and quantitative assessment by comparing computed landmark or segmentation displacement to ground truth).</p>
<p>If you transform models (surface meshes) then transformations preserve all the points and connectivity (only the point coordinates are updated).</p>

---

## Post #3 by @miniBin (2019-02-02 03:24 UTC)

<p>thank you for this detailed answer!</p>

---
