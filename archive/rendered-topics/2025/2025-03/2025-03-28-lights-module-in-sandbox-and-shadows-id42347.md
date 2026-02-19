---
topic_id: 42347
title: "Lights Module In Sandbox And Shadows"
date: 2025-03-28
url: https://discourse.slicer.org/t/42347
---

# Lights module in Sandbox and Shadows

**Topic ID**: 42347
**Date**: 2025-03-28
**URL**: https://discourse.slicer.org/t/lights-module-in-sandbox-and-shadows/42347

---

## Post #1 by @muratmaga (2025-03-28 18:25 UTC)

<p>I am trying to update our short course notes for the new shadow functionality in the preview. But it is not clear to me whether this is a full replacement of the Lights module in Sandbox. I tried to use them together and it was a bit messy,</p>
<p>What is the suggestion for functionality not exposed in the Shadows popup in 3D viewer (e.g., light angles). Continue to use Lights module?</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #2 by @lassoan (2025-03-29 02:49 UTC)

<p>The Lights module mostly collects various lighting related features into one place to make it easier to experiment with different options without switcing modules. It does not add any additional features for adjusting shadows. Only the “Lighting” and “Image-based lighting” sections contain features that are not yet available properly in Slicer core.</p>
<p>The module is mostly for quick experimentation, because some essential features are missing (probably that’s why you may perceive it as messy). For example, settings in “Lighting” and “Image-based lighting” sections are not saved into the scene (nothing complicated just has not been on the critical path for any funded projects); sliders update the scene, but the sliders don’t get updated if the scene changes. Usability should probably be improved, too, as it may be confusing that you need to select what views you want the module to manage (need to click “Select all” to see any changes).</p>

---
