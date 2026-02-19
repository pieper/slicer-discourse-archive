---
topic_id: 1865
title: "Extraction Of The Centerlines"
date: 2018-01-18
url: https://discourse.slicer.org/t/1865
---

# Extraction of the centerlines

**Topic ID**: 1865
**Date**: 2018-01-18
**URL**: https://discourse.slicer.org/t/extraction-of-the-centerlines/1865

---

## Post #1 by @giuseppe.cardone (2018-01-18 08:43 UTC)

<p>Hi,<br>
I would like to extract the centerlines of a vein model that I obtained from the segmentation. When I fix the fiducial points the model of the centerline is empty, in fact if I see the information there is written that the centerline has 0 points. I use the version 4.8.1 of 3D slicer so the vmtk module change from the previous versions and I can’t find tutorial about this topic.<br>
Second question: If I want to import the centerline like a curve in Solidworks, Can I do it? If not, There is a way to record the coordinate x, y, z of the centerline?</p>
<p>Thank you.</p>

---

## Post #2 by @giuseppe.cardone (2018-01-18 09:23 UTC)

<p>PS<br>
I want to use the points in solidworks to recreate a sketch of the curve.</p>

---

## Post #3 by @lassoan (2018-01-18 21:54 UTC)

<p>You can use <code>Extract skeleton</code> module to create a text file (id, x, y, z) file directly from a binary labelmap.</p>
<p>You can use VMTK extension’s Centerline Computation module for more complex shapes (for example for extracting complete vessel trees) or if you prefer to get output as a VTK polydata file.</p>

---

## Post #4 by @lassoan (2018-01-19 06:07 UTC)

<p>A post was split to a new topic: <a href="/t/dbs-electrode-reconstruction/1872">DBS electrode reconstruction</a></p>

---

## Post #5 by @giuseppe.cardone (2018-01-19 06:58 UTC)

<p>I will try with extract skeleton!<br>
Thank you!</p>

---
