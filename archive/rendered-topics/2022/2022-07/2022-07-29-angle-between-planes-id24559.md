---
topic_id: 24559
title: "Angle Between Planes"
date: 2022-07-29
url: https://discourse.slicer.org/t/24559
---

# Angle between planes

**Topic ID**: 24559
**Date**: 2022-07-29
**URL**: https://discourse.slicer.org/t/angle-between-planes/24559

---

## Post #1 by @PaoloZaffino (2022-07-29 10:48 UTC)

<p>Hi all,<br>
I would like to quantify an angle between 2 planes.<br>
Q3DC allows drawing lines, not planes.<br>
Do you know how to get this parameter?</p>
<p>Thanks a lot,<br>
Paolo</p>

---

## Post #2 by @lassoan (2022-07-29 13:39 UTC)

<p>You can use <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#measure-angle-between-two-markup-planes">this code snippet</a> to get angle between two planes. You can put it into a scripted module if you want to avoid copy-pasting code, but often what happens is that you add markups to your scene (mark points, lines, planes, etc.) and then run a script that computes all metrics (angles, distances, etc.) that you need by a single click.</p>

---

## Post #3 by @PaoloZaffino (2022-08-02 18:15 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a> .<br>
So the first plane in the list is the “reference”?<br>
I would avoid computing the complementary angle (or at least I would know if I’m doing it).</p>
<p>Paolo</p>

---
