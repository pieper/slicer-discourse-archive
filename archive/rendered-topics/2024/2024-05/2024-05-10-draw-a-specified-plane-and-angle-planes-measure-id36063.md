---
topic_id: 36063
title: "Draw A Specified Plane And Angle Planes Measure"
date: 2024-05-10
url: https://discourse.slicer.org/t/36063
---

# Draw a specified plane and Angle Planes measure

**Topic ID**: 36063
**Date**: 2024-05-10
**URL**: https://discourse.slicer.org/t/draw-a-specified-plane-and-angle-planes-measure/36063

---

## Post #1 by @YLX (2024-05-10 13:27 UTC)

<p>I want to implement in 3D slicer software, given three points to determine a plane, may I ask how this function is implemented? I also want to determine any plane given any point and find the dihedral Angle. I hope you can help me solve such problems. Thank you very much.<br>
For example, I want to identify a plane at mark F_1,F_2,F_3 in the figure below,the dihedral Angle between the plane and the midsagittal plane is found. The landmarks in the figure below are all specified.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86344b1de6246c88f5283c42144858887d145bc6.jpeg" data-download-href="/uploads/short-url/j9e1bKFBTak7G7XRQBh3oVZFnPE.jpeg?dl=1" title="G}87XXGZSK7)(ORC%5~115D" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/86344b1de6246c88f5283c42144858887d145bc6_2_549x500.jpeg" alt="G}87XXGZSK7)(ORC%5~115D" data-base62-sha1="j9e1bKFBTak7G7XRQBh3oVZFnPE" width="549" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/86344b1de6246c88f5283c42144858887d145bc6_2_549x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86344b1de6246c88f5283c42144858887d145bc6.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86344b1de6246c88f5283c42144858887d145bc6.jpeg 2x" data-dominant-color="687D7B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">G}87XXGZSK7)(ORC%5~115D</span><span class="informations">694×631 79.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Operating system:<br>
Slicer version:5.4.0<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #3 by @lassoan (2024-05-10 13:22 UTC)

<p>To place a plane by 3 points, you can go to Markups module, add a new plane, and in <code>Plane settings</code> section choose <code>Type</code> → <code>Three points</code>.</p>
<p>You can get the angle between two planes using this <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#measure-angle-between-two-markup-planes">code snippet in the script repository</a>.</p>

---
