---
topic_id: 45963
title: "Alpaca Template Selection K Means"
date: 2026-01-28
url: https://discourse.slicer.org/t/45963
---

# Alpaca template selection K-means

**Topic ID**: 45963
**Date**: 2026-01-28
**URL**: https://discourse.slicer.org/t/alpaca-template-selection-k-means/45963

---

## Post #1 by @Stephan_Collins (2026-01-28 08:50 UTC)

<p>Dear all, there’s something I did not understand in the ALPACA workflow.<br>
The plos one paper clearly explains the benefits of doing K means clustering and choosing templates that best match subgroups of data relative to a completely blind approach using multiple source models.<br>
But once you have identified the groups and which samples you should use for malpaca, malpaca will figure out wich samples to choose for both source and target automatically or are you supposed to create folders and run malpaca manually for each subgroup (I suppose so) ?</p>
<p>And again, well done to all for an amazing software (slicer) and module (slicermorph) !</p>

---

## Post #2 by @muratmaga (2026-01-28 15:52 UTC)

<aside class="quote no-group" data-username="Stephan_Collins" data-post="1" data-topic="45963">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/stephan_collins/48/81446_2.png" class="avatar"> Stephan_Collins:</div>
<blockquote>
<p>you supposed to create folders and run malpaca manually for each subgroup (I suppose so) ?</p>
</blockquote>
</aside>
<p>Yes, You need to copy and paste those models and corresponding set of landmarks into appropriate folder structure (Source_LMs, and Source_Models) and set MALPACA that way.</p>

---
