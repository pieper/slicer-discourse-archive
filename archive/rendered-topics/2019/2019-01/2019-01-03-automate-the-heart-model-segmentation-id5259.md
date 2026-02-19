---
topic_id: 5259
title: "Automate The Heart Model Segmentation"
date: 2019-01-03
url: https://discourse.slicer.org/t/5259
---

# Automate the heart model segmentation

**Topic ID**: 5259
**Date**: 2019-01-03
**URL**: https://discourse.slicer.org/t/automate-the-heart-model-segmentation/5259

---

## Post #1 by @anandmulay3 (2019-01-03 08:11 UTC)

<p>I want to automate the segmentation process to create a heart model , i have already created one which creates nice models for bone,skin and external objects. now i want to move further to create a scriptable module which can generate a heart model from given MR,CT data.<br>
I need a guidance to achieve this,</p>

---

## Post #2 by @lassoan (2019-01-03 15:53 UTC)

<p>A good approach can be to use registration (image based maybe initialized with some landmarks) to transfer seeds from an atlas to the current patient image; then use “Grow from seeds” effect (probably with masking) to get the final segmentation.</p>

---

## Post #3 by @anandmulay3 (2019-01-04 14:26 UTC)

<p>Yeah i’m thinking in same direction , your tumor script will be helpful in this.<br>
i have tried the seed grow effect which you shown in your video, its great i think i just need to use both this together to achieve this.<br>
i just want to know…</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="5259">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>probably with masking</p>
</blockquote>
</aside>
<p>how to do this? and how it will be helpful?</p>

---

## Post #4 by @lassoan (2019-01-04 15:20 UTC)

<p>Masking is useful because you can exclude irrelevant areas by defining a hard constraint by specifying image intensity range (or a specific segment). The masked area is excluded from the region growing: it is not grown and it is not overwritten by other segments. On the other hand, if you used “background” seeds to exclude irrelevant areas, this background segment is grown as well, therefore it would compete with other seeds, which may lead to incomplete segmentation.</p>
<p>For contrast-enhanced acquisitions, you may use an intensity-based mask, by setting intensity range for the segmentation that only includes contrasted vessels (bones have similar intensity, but by adding separate seeds in bone regions, you can easily separate them).</p>

---

## Post #5 by @anandmulay3 (2019-02-14 07:33 UTC)

<p>Can masking be implemented in my automated script , you have any link or example scriptable module?</p>

---
