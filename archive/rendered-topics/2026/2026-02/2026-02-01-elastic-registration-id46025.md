---
topic_id: 46025
title: "Elastic Registration"
date: 2026-02-01
url: https://discourse.slicer.org/t/46025
---

# Elastic Registration

**Topic ID**: 46025
**Date**: 2026-02-01
**URL**: https://discourse.slicer.org/t/elastic-registration/46025

---

## Post #1 by @Zah (2026-02-01 18:38 UTC)

<p><strong>Hi 3D Slicer Community,</strong></p>
<p>I’m new to 3D Slicer and still learning, and I have a few questions.</p>
<ol>
<li>
<p><strong>After performing an elastic registration, should I harden the transformed CBCT using the “Transforms” module, or should this be done from the “Data” module?</strong></p>
</li>
<li>
<p><strong>When I save my data and reopen the scene, I don’t get the same results.</strong><br>
Is there a recommended or specific way to save all transformed volumes and segmentations to ensure everything loads correctly?</p>
</li>
<li>
<p><strong>After applying an elastic transformation, how can I extract the deformation matrix or deformation field?</strong><br>
I would like to quantify the deformation if possible.</p>
</li>
<li>
<p><strong>Finally, is there any method other than “Segment Cross-Section Area” to compare bone gain before and after grafting?</strong><br>
I’m looking for reliable ways to quantify volumetric changes.</p>
</li>
</ol>
<p>Thank you very much for your help.</p>

---

## Post #2 by @muratmaga (2026-02-01 19:12 UTC)

<aside class="quote no-group" data-username="Zah" data-post="1" data-topic="46025">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/z/57b2e6/48.png" class="avatar"> Zah:</div>
<blockquote>
<p><strong>After performing an elastic registration, should I harden the transformed CBCT using the “Transforms” module, or should this be done from the “Data” module?</strong></p>
</blockquote>
</aside>
<p>These are equivalent, doesn’t matter where you it.</p>
<aside class="quote no-group" data-username="Zah" data-post="1" data-topic="46025">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/z/57b2e6/48.png" class="avatar"> Zah:</div>
<blockquote>
<p><strong>When I save my data and reopen the scene, I don’t get the same results.</strong></p>
</blockquote>
</aside>
<p>That shouldn’t be the case. Are you sure you are saving all the objects associated with the scene?</p>
<aside class="quote no-group" data-username="Zah" data-post="1" data-topic="46025">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/z/57b2e6/48.png" class="avatar"> Zah:</div>
<blockquote>
<p><strong>After applying an elastic transformation, how can I extract the deformation matrix or deformation field?</strong></p>
</blockquote>
</aside>
<p>Deformation field will be saved as a transform. You can then turn that into a grid transform or displacement field, depending on how you want to quantify the deformation. There are no specific tools to quantify deformation in Slicer, as far as I know.</p>

---
