# Hi dears, regarding zygomatic complex segmentation

**Topic ID**: 20748
**Date**: 2021-11-23
**URL**: https://discourse.slicer.org/t/hi-dears-regarding-zygomatic-complex-segmentation/20748

---

## Post #1 by @MAXFAXSURGEON (2021-11-23 13:36 UTC)

<p>I am doing a research related to zygomatic bone complex and I need to know how to:</p>
<ol>
<li>how to segment the zygomatic bone from the model of both T1 and T2?</li>
<li>how to save the superimposed model as a moving 3D model?<br>
please if there are tutorial clips regarding these two issues would be nice to share with me… Thank you in advance.</li>
</ol>

---

## Post #2 by @lassoan (2021-11-23 18:27 UTC)

<p>This is not a trivial task, because bones are typically not well visible in MRI images. The optimal answer depends on how many cases you need to segment, with what accuracy, what are the time constraints, etc.</p>
<p>To get started, you can read the <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html">image segmentation overview</a> page and then try “Grow from seeds” and “Fill between slices” effects.</p>

---

## Post #3 by @MAXFAXSURGEON (2021-12-04 02:37 UTC)

<p>thank you so much for your reply.</p>

---
