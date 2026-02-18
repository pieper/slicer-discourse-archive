# Computing DRR to a Transformed Volume

**Topic ID**: 26142
**Date**: 2022-11-08
**URL**: https://discourse.slicer.org/t/computing-drr-to-a-transformed-volume/26142

---

## Post #1 by @domP (2022-11-08 14:40 UTC)

<p>Hi everyone,<br>
is it possible to compute DRR to a transformed volume using Radiotherapy module?<br>
I have applied a “harden transform” (only a rotation) to a CT volume but when I compute DRR I don’t get the expected projection image.<br>
I have also tried to rotate the beam with the same angle using the original CT volume (not transformed) but I get a different result.</p>

---

## Post #2 by @lassoan (2022-12-01 07:39 UTC)

<p>This is a known limitation. See this topic for some more details:</p>
<aside class="quote" data-post="22" data-topic="2010">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/958977/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/generate-digitally-reconstructed-radiograph-from-3dct/2010/22">Generate digitally reconstructed radiograph from 3DCT</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Which dataset: training, validation, test?
  </blockquote>
</aside>


---
