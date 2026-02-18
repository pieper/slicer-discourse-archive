# Boundary point of a cross-section 

**Topic ID**: 22719
**Date**: 2022-03-28
**URL**: https://discourse.slicer.org/t/boundary-point-of-a-cross-section/22719

---

## Post #1 by @Dongwei1 (2022-03-28 11:17 UTC)

<p>Hi all,</p>
<p>I am currently using vmtk to compute the centerline and cross-section of the vessel. I do aware that vmtkcenterlinesections can help me calculate the area of the cross-section perpendicular to the centerline, but is there a way to fetch the coordinates of boundary points of the cross-section?</p>
<p>Thank you in advance!</p>
<p>Bests,<br>
Dongwei</p>

---

## Post #2 by @chir.set (2022-03-28 15:32 UTC)

<aside class="quote no-group" data-username="Dongwei1" data-post="1" data-topic="22719">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dongwei1/48/14027_2.png" class="avatar"> Dongwei1:</div>
<blockquote>
<p>s there a way to fetch the coordinates of boundary points of the cross-section</p>
</blockquote>
</aside>
<p>If you use SlicerVMTK extension, you may hack the module ‘Cross-section analysis’ to get the surface points a cross-section from <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/b280bd8471e4036282be3c7402c37e7d099d0d3e/CrossSectionAnalysis/CrossSectionAnalysis.py#L1131" rel="noopener nofollow ugc">here</a>. Unless I misunderstood your workflow and your need.</p>

---

## Post #3 by @Dongwei1 (2022-03-31 11:32 UTC)

<p>Thank you! I will try it out!</p>

---
