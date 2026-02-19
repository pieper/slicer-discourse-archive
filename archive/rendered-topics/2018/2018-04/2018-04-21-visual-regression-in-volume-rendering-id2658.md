---
topic_id: 2658
title: "Visual Regression In Volume Rendering"
date: 2018-04-21
url: https://discourse.slicer.org/t/2658
---

# Visual regression in Volume Rendering

**Topic ID**: 2658
**Date**: 2018-04-21
**URL**: https://discourse.slicer.org/t/visual-regression-in-volume-rendering/2658

---

## Post #1 by @chir.set (2018-04-21 17:30 UTC)

<p>Today’s build has introduced a visual regression while rotating a 3D model in Volume rendering. A new VTK commit has been pulled in. It seems to request a too high frame rate. Please see two screen video shots with Slicer commit tags as suffix :</p>
<p><a href="https://mega.nz/#!BVlBwTqL!FGXzin-WlSKl6uhENQFlaw_4-PRidRL45oJb138-q_A" class="onebox" target="_blank" rel="nofollow noopener">https://mega.nz/#!BVlBwTqL!FGXzin-WlSKl6uhENQFlaw_4-PRidRL45oJb138-q_A</a></p>
<p><a href="https://mega.nz/#!NR9UAb6B!tbqFNC4ZnJtOs212JcGfU28m7rR5Pn9RkwFq0H2CUVw" class="onebox" target="_blank" rel="nofollow noopener">https://mega.nz/#!NR9UAb6B!tbqFNC4ZnJtOs212JcGfU28m7rR5Pn9RkwFq0H2CUVw</a></p>
<p>FYI.</p>

---

## Post #2 by @lassoan (2018-04-21 18:34 UTC)

<p>For a few weeks we’ve made static-quality rendering the default, a few days ago we reverted the default to the previous progressive (adaptive) option to have interactive frame rates by default for CPU volume rendering and for virtual reality viewing.</p>
<p>You still have all the options available. To prevent low-quality rendering during rotation, then go to Advanced settings / Techniques tab and either decrease “Interactive speed” or switch to “Normal quality”.</p>
<p>To reduce wood grain artifacts, I would recommend to enable “Surface smoothing” or (if rendering time is not a concern) then use “Maximum Quality” setting.</p>
<p>Let us know which settings work well for you. We may tune default values based on what we hear back from users. We also plan to make defaults adjustable in application settings.</p>

---

## Post #3 by @chir.set (2018-04-22 09:06 UTC)

<p>‘Normal quality’ renders as previously experienced. It would be great to have it adjustable in application settings, as well as ‘Surface smoothing’., for a more comfortable workflow.</p>

---

## Post #4 by @cpinter (2018-04-22 12:39 UTC)

<p>I’m planning to add this feature next week.</p>

---
