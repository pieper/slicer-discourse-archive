---
topic_id: 23587
title: "Exporting Png Files As Stacks After Registration"
date: 2022-05-25
url: https://discourse.slicer.org/t/23587
---

# Exporting png-files as stacks after registration

**Topic ID**: 23587
**Date**: 2022-05-25
**URL**: https://discourse.slicer.org/t/exporting-png-files-as-stacks-after-registration/23587

---

## Post #1 by @j.v.d (2022-05-25 15:40 UTC)

<p>Hey everyone!<br>
Lately I wanted to align two different CT-modalities with 3D Slicer so that corresponding anatomic structures are positioned exactly over each other. This worked out quite well so far with “Transforms” and “General Registration (BRAINS)” and now I wanted to create stacks (png for example) of these two CT-modalities with exact this orientation.<br>
I tried to accomplish that with the “Screen Capture”- Utility but so far I only got single pictures instead of a whole stack which I could use for further analysis. Is it possible to create these stacks I´m looking for ?</p>
<p>Best regards<br>
Jan</p>

---

## Post #2 by @muratmaga (2022-05-25 15:53 UTC)

<p>Why do you want to export stacks? YOu will loose coordinate systems, voxel spacing and possibly degrade your data.</p>

---

## Post #3 by @lassoan (2022-05-25 17:57 UTC)

<aside class="quote no-group" data-username="j.v.d" data-post="1" data-topic="23587">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/8c91f0/48.png" class="avatar"> j.v.d:</div>
<blockquote>
<p>I tried to accomplish that with the “Screen Capture”- Utility but so far I only got single pictures instead of a whole stack which I could use for further analysis.</p>
</blockquote>
</aside>
<p>Screen capture module can export image stacks (use slice sweep mode), but image stacks are for presentation purposes only, due to the issues that <a class="mention" href="/u/muratmaga">@muratmaga</a> mentioned above.</p>
<p>For further analysis, use 3D file formats, such as nrrd.</p>

---

## Post #4 by @j.v.d (2022-06-09 10:19 UTC)

<p>Thank you both for your advices ! Regarding what <a class="mention" href="/u/muratmaga">@muratmaga</a> mentioned I should rather use the single pictures instead.</p>

---
