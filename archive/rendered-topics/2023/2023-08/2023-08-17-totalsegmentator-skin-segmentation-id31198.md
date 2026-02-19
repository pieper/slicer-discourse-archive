---
topic_id: 31198
title: "Totalsegmentator Skin Segmentation"
date: 2023-08-17
url: https://discourse.slicer.org/t/31198
---

# TotalSegmentator "skin segmentation"

**Topic ID**: 31198
**Date**: 2023-08-17
**URL**: https://discourse.slicer.org/t/totalsegmentator-skin-segmentation/31198

---

## Post #1 by @Sergio (2023-08-17 17:19 UTC)

<p>Hi,</p>
<p>I could see that TotalSegmentator has the capability of segment the “skin” using the segmentation task “Body” mode. I could see that is creating the “skin.nii.gz” file but 3D Slicer is not loading it as a segment. Only loads “Body_trunc” and “Body_extremities”.</p>
<p>Do you know any solution?</p>
<p>Thanks in advance.</p>

---

## Post #2 by @rbumm (2023-08-17 18:29 UTC)

<p>Skin is in the working pipeline.<br>
Stay tuned.</p>

---

## Post #3 by @rbumm (2023-08-17 18:33 UTC)

<aside class="quote no-group" data-username="Sergio" data-post="1" data-topic="31198">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/b77776/48.png" class="avatar"> Sergio:</div>
<blockquote>
<p>skin.nii.gz</p>
</blockquote>
</aside>
<p>Have you tried ti load that file into Slicer? Does it produce something skinny ? <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #4 by @Sergio (2023-08-17 18:44 UTC)

<p>Thanks for the information Rudolf. No, in fact I could not find the file “skin.nii.gz” but I could see that the TotalSegmentator(TS) command window indicates that TS is creating this file. However, I think the file is not being converted to segment node.</p>

---
