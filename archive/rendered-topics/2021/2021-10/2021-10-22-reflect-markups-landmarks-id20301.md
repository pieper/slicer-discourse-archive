---
topic_id: 20301
title: "Reflect Markups Landmarks"
date: 2021-10-22
url: https://discourse.slicer.org/t/20301
---

# Reflect markups (landmarks)

**Topic ID**: 20301
**Date**: 2021-10-22
**URL**: https://discourse.slicer.org/t/reflect-markups-landmarks/20301

---

## Post #1 by @Ale (2021-10-22 14:29 UTC)

<p>Dear list, I’m placing markups (landmarks) to carry out a geometric morphometric analysis in some mammals skulls. I have some cases where one of the zygomatic archs is missing (screen capture below). Is there a way to reflect one side markups  based on a defined plane to estimate landmarks of the missing structure (in this case the right zygomatic arch).<br>
Kind regards,<br>
Alej</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8cdc462baa87494b37aade3ed2f2eaf27c71c077.jpeg" alt="image" data-base62-sha1="k66MpZ8hHYPgwgzMyVyQnLKx07d" width="314" height="213"></p>

---

## Post #2 by @muratmaga (2021-10-22 15:08 UTC)

<p>Currently there is no automated (or UI driven) way of doing it. You will have to define the symmetry plane (Markups-&gt;Plane tool) and then the position of the LM can be reflected using that particular plane.<br>
<a class="mention" href="/u/smrolfe">@smrolfe</a></p>

---

## Post #3 by @smrolfe (2021-10-22 15:20 UTC)

<p>I wrote a function that does this in Python  <a href="https://github.com/SlicerMorph/SlicerMorph/blob/7cc50a5042a12692fb0624875f204a7c8ede64ad/PseudoLMGenerator/PseudoLMGenerator.py#L710" rel="noopener nofollow ugc">here</a>. It does a few extra things (merges points that are very close to the symmetry plane, creates a left, right and merged landmark set) so it would need to be altered a little bit. The plane needs to be defined or calculated before using this function, as <a class="mention" href="/u/muratmaga">@muratmaga</a> noted.</p>

---
