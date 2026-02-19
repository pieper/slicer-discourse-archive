---
topic_id: 10540
title: "Calculate Volumes On Ct Scans"
date: 2020-03-04
url: https://discourse.slicer.org/t/10540
---

# Calculate volumes on ct scans

**Topic ID**: 10540
**Date**: 2020-03-04
**URL**: https://discourse.slicer.org/t/calculate-volumes-on-ct-scans/10540

---

## Post #1 by @Giuseppe_Voltini (2020-03-04 13:22 UTC)

<p>Operating system:windows 10<br>
Slicer version: 4.10.2<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Is it possible to automatically calculate on a chest ct scan the  volume of a lung lesion, or multiple lung lesions ,  using  Hounsfield scale density  criteria?<br>
Thank you</p>
<p>Giuseppe</p>

---

## Post #2 by @manjula (2020-03-04 14:45 UTC)

<p>Yes if you segment it based on your intensity range then you can use segment statistics module to calculate the volume and many other parameters</p>

---

## Post #3 by @Giuseppe_Voltini (2020-03-05 10:11 UTC)

<p>THank you!  and how can I segment automatically using a density range?: I’m working on ards from coronavirus pneumonia trying to distinguish automatically the “ggo” areas from consolidation</p>

---

## Post #4 by @manjula (2020-03-05 10:58 UTC)

<p>There are many options. You can use segment editor module. Also install the segment editor extra effects. Simplest is thresholding. But there  are many other advanced methods available. You will also may need to crop or mask the region  of interest. To get rid of unnecessary regions. There are many tutorials online on this</p>
<div class="lazyYT" data-youtube-id="_7oZygGp2ds" data-youtube-title="3D Slicer Tutorial - Segmentation Wizard" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>

---

## Post #5 by @pieper (2020-03-05 13:13 UTC)

<aside class="quote no-group" data-username="Giuseppe_Voltini" data-post="3" data-topic="10540">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/giuseppe_voltini/48/5250_2.png" class="avatar"> Giuseppe_Voltini:</div>
<blockquote>
<p>I’m working on ards from coronavirus pneumonia trying to distinguish automatically the “ggo” areas from consolidation</p>
</blockquote>
</aside>
<p>I’m sure we’d all like to help you with that!</p>
<p>If you have any example data that you can share we can provide more concrete suggestions.  <a class="mention" href="/u/manjula">@manjula</a>’s suggestions are a great place to start.</p>

---
