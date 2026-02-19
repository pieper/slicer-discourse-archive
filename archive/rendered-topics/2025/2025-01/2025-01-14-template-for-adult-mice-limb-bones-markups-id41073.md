---
topic_id: 41073
title: "Template For Adult Mice Limb Bones Markups"
date: 2025-01-14
url: https://discourse.slicer.org/t/41073
---

# Template for adult mice limb bones markups

**Topic ID**: 41073
**Date**: 2025-01-14
**URL**: https://discourse.slicer.org/t/template-for-adult-mice-limb-bones-markups/41073

---

## Post #1 by @coco (2025-01-14 07:57 UTC)

<p>Dear all,<br>
I wondered if anyone has a set of landmarked limb bones (zeugopode/stylopode) in adult mice ? I have seen a video using a couple of hundred markups on a gorilla femur and some other published works with about a hundred markups in mice for a single bone. If someone can help and share a template for those long bones, it would save us some work (acknowledgement agreed!)<br>
Many thanks</p>

---

## Post #2 by @muratmaga (2025-01-14 16:55 UTC)

<p>I don’t think anything exists. But others can chime in. It is also fairly straightforward to do with PseudoLMGenerator. Please check out these two tutorials (you will need the second to fill the cavities inside the bone so that no internal LMs are generated):</p>
<ol>
<li><a href="https://github.com/SlicerMorph/Tutorials/tree/main/PseudoLMGenerator#readme" class="inline-onebox" rel="noopener nofollow ugc">Tutorials/PseudoLMGenerator at main · SlicerMorph/Tutorials · GitHub</a></li>
<li><a href="https://github.com/SlicerMorph/Tutorials/blob/main/WaterTightModels/Readme.MD" class="inline-onebox" rel="noopener nofollow ugc">Tutorials/WaterTightModels/Readme.MD at main · SlicerMorph/Tutorials · GitHub</a></li>
</ol>
<p>In the upcoming project week we will be discussing some kind of an infrastructure to share user-generated, custom settings such as color tables, volume rendering presets, etc. This type of templates can potentially be part of that as well (though it will also require for the reference model to be shared as well).</p>

---
