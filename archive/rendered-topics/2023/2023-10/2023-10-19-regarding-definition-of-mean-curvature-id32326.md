# Regarding definition of mean curvature

**Topic ID**: 32326
**Date**: 2023-10-19
**URL**: https://discourse.slicer.org/t/regarding-definition-of-mean-curvature/32326

---

## Post #1 by @Mudrika (2023-10-19 13:36 UTC)

<p>Hello everyone!</p>
<p>I am extracting a centerline model for a geometry. By using the ‘markups’, I am drawing curves on the selected arteries and calculating geometric parameters like length and mean curvature. As we know, the curvature changes at every point and for drawing a curve, few control points are defined. So, for the calculation of the mean curvature, is it the mean curvature of the defined control points or is it something else?</p>
<p>Thank you!</p>

---

## Post #2 by @Slogish (2024-03-31 16:10 UTC)

<p>I have the same question,and i also would like to know how to define the maximum curvature?What is the radius of the Osculating circle?</p>

---

## Post #3 by @lassoan (2024-03-31 19:22 UTC)

<p>The control points are only used for computing the curve. Radius is computed on the curve that you see, which has many more (by default 10x more) points than control points. Mean curvature is the average curvature value along the entire curve that you see (not just at the control points).</p>

---

## Post #4 by @Mudrika (2024-04-03 05:50 UTC)

<p>Thanks a lot for the clarification!</p>

---

## Post #5 by @Slogish (2024-04-03 22:35 UTC)

<p>Thanks！！！！</p>
<p>---- Replied Message ----</p>
<blockquote>
<p>From | <a href="mailto:notifications@slicer.discoursemail.com">Andras Lasso via 3D Slicer Community</a><a href="mailto:notifications@slicer.discoursemail.com">notifications@slicer.discoursemail.com</a> |</p>
<ul>
<li>| - |<br>
Date | 04/01/2024 03:22 |<br>
To | <a href="mailto:up_wyp@163.com">up_wyp</a><a href="mailto:up_wyp@163.com">up_wyp@163.com</a> |<br>
Subject | [Slicer] Regarding definition of mean curvature |</li>
</ul>
</blockquote>
<p>The control points are only used for computing the curve. Radius is computed on the curve that you see, which has many more (by default 10x more) points than control points. Mean curvature is the average curvature value along the entire curve that you see (not just at the control points).</p>
<p>–<br>
<em>Previous Replies</em><br>
I have the same question,and i also would like to know how to define the maximum curvature?What is the radius of the Osculating circle?</p>

---
