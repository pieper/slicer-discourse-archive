# Why  the module Cardiacagatston cannot be used in the slicer 5.2.2?

**Topic ID**: 30498
**Date**: 2023-07-10
**URL**: https://discourse.slicer.org/t/why-the-module-cardiacagatston-cannot-be-used-in-the-slicer-5-2-2/30498

---

## Post #1 by @SYL (2023-07-10 12:55 UTC)

<p>why  the module Cardiacagatston cannot be used in the slicer 5.2.2</p>

---

## Post #2 by @lassoan (2023-07-10 12:56 UTC)

<p><a class="mention" href="/u/curtislisle">@curtislisle</a> is working on making a new version of the module available for Slicer-5.2.2. See more details in this topic:</p>
<aside class="quote" data-post="1" data-topic="1544">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/e/439d5e/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/cardiac-agatston-scoring-module/1544/">Cardiac Agatston Scoring module</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    I require help regarding use of 3d slicer module “CardiacAgatstonScoring”.This module isnt showing in any version except 4.4 but in 4.4 when i click Apply(for calculating calcium score)it doesnt work 
Operating system: 
Slicer version: 
Expected behavior: 
Actual behavior:
  </blockquote>
</aside>


---

## Post #3 by @SYL (2023-07-10 13:18 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/76657cc5ded509e9b08f258c478601ab541e781b.png" alt="image" data-base62-sha1="gTnMbL0xiBbB0E1vUhOL37AlxLZ" width="150" height="108"></p>
<p>another question ，How to divide a model in the coronal position into eight equally large parts (based on the center of the circle)</p>

---

## Post #4 by @lassoan (2023-07-10 13:34 UTC)

<p>When you segment the calcifications in Segment Editor module, you can split it to multiple regions (for example, using Scissors module). The score can be computed for each segment.</p>

---

## Post #5 by @SYL (2023-07-11 02:04 UTC)

<p>not the calcification, i just need to divide it to 8 parts 。 but i cant find the center of this circle.</p>

---

## Post #6 by @lassoan (2023-07-15 15:00 UTC)

<p>You can create a segmentation manually (e.g., using Scissors tool) that has these 8 sectors, save it, and reuse it for any patient cases. You can transform this segmentation to each patient case, harden the transform, add to your calcification segmentation, and use “Logical operators” effect to use it to subdivide your segmentation. Once you have a good workflow that you perform manually, you can automate it using Python scripting.</p>

---
