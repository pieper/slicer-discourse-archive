---
topic_id: 7227
title: "Mark Up Constraints"
date: 2019-06-19
url: https://discourse.slicer.org/t/7227
---

# Mark up constraints

**Topic ID**: 7227
**Date**: 2019-06-19
**URL**: https://discourse.slicer.org/t/mark-up-constraints/7227

---

## Post #1 by @Jainey (2019-06-19 06:39 UTC)

<p>Hi<br>
Could someone please help me to write a script to keep the distance between markups fixed, please. When I add markups on my images I want them to have the same distance between some of them when I move from frame to frame in my transform sequence.</p>
<p>Basically, I add mak ups and transform them with my transform sequence, I d like to have their distances between each other fixed.<br>
I have no software developing background. Could I do this with a python script pls. Are there anything already written so I can use.</p>
<p>Thanks</p>
<p>Tom</p>

---

## Post #2 by @lassoan (2019-06-19 15:57 UTC)

<p>You can transform the markups, harden the transform, then resample the points along the curve to be equally spaced. If you have a curve node named <code>C</code> and want control points to be at 3mm from each other then you need to type this to the Python console: <code>getNode('C').ResampleCurveWorld(3.0)</code>. Recent Slicer preview version (4.11.x) is required.</p>

---

## Post #3 by @Jainey (2019-06-20 09:17 UTC)

<p>Thanks a lot Prof.lasso <a class="mention" href="/u/lassoan">@lassoan</a><br>
I will try this</p>
<p>Tom</p>

---
