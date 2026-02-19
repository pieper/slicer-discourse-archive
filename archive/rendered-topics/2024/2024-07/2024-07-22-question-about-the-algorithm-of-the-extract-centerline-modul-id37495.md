---
topic_id: 37495
title: "Question About The Algorithm Of The Extract Centerline Modul"
date: 2024-07-22
url: https://discourse.slicer.org/t/37495
---

# Question about the algorithm of the extract centerline module (VMTK)

**Topic ID**: 37495
**Date**: 2024-07-22
**URL**: https://discourse.slicer.org/t/question-about-the-algorithm-of-the-extract-centerline-module-vmtk/37495

---

## Post #1 by @Seokjun_Hwang (2024-07-22 06:49 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/719cb5cd6f3585541fcf05166fd00961e287afc4.png" alt="image" data-base62-sha1="gd3HEIWp3bO7EPZwKT58eCRP9ha" width="465" height="477"></p>
<p>Using the extract centerline module, I have obtained the centerline of the aorta, as shown in the picture. My research team members are interested in understanding and want to explain how this module generates the centerline.</p>
<p>For example, did it draw a line by marking the central points of cross-sectional areas? Or did it use the centroid of the aorta?</p>
<p>Can you explain in a simple way how the centerline is extracted using this algorithm? I couldn’t fully understand it even after looking at the code.</p>
<p>Thank you for implementing this module, and we would appreciate your explanation.</p>

---

## Post #2 by @lassoan (2024-07-22 22:07 UTC)

<p>The full source code of VMTK is available <a href="https://github.com/vmtk/vmtk">here</a>. Details of the algorithm is explained in Luca Antiga’s <a href="http://lantiga.github.io/media/AntigaPhDThesis.pdf">PhD thesis</a> and numerous papers.</p>

---
