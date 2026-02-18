# Surface Dice similarity coefficient

**Topic ID**: 29514
**Date**: 2023-05-17
**URL**: https://discourse.slicer.org/t/surface-dice-similarity-coefficient/29514

---

## Post #1 by @Rukhsora (2023-05-17 16:02 UTC)

<p>How can I obtain Surface Dice Coefficient in 3D Slicer 5.3.0. ?</p>

---

## Post #2 by @cpinter (2023-05-22 08:59 UTC)

<p>Dice coefficient is for volumes not surfaces. For surfaces you can calculate Hausdorff distance. Both are available in the Segment Comparison module in the SlicerRT extension.</p>
<p>FYI the forum has a search function, which is useful, as most basic questions have been already answered at least once, for example</p><aside class="quote" data-post="2" data-topic="19755">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/dice-similarity-coefficient/19755/2">Dice similarity coefficient</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    You can use Segment Comparison module (in SlicerRT extension).
  </blockquote>
</aside>


---
