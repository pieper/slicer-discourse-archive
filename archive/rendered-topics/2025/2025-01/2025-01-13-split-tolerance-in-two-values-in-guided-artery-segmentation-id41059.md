---
topic_id: 41059
title: "Split Tolerance In Two Values In Guided Artery Segmentation"
date: 2025-01-13
url: https://discourse.slicer.org/t/41059
---

# Split tolerance in two values in Guided Artery Segmentation Module

**Topic ID**: 41059
**Date**: 2025-01-13
**URL**: https://discourse.slicer.org/t/split-tolerance-in-two-values-in-guided-artery-segmentation-module/41059

---

## Post #1 by @SANTIAGO_PENDON_MING (2025-01-13 14:31 UTC)

<p>Hi! I was trying some Slicer’s modules and I found the Guided Artery Segmentation Module, which is truly interesting to segment specific zone with relative precision.</p>
<p>To make it more functional, I’m thinking that split the tolerance in a lower and and a higher tolerance would be great. Sometimes you want to segment ‘more easily’ in high/low values and vice versa.</p>
<p>Also, establish a lower and a maximal value to segment is interesting. This last request could be made with filters in the segment editor module, right, but if this could be implemented directly in the module using python/C functions the usability would be better.</p>
<p>Dear <a class="mention" href="/u/lassoan">@lassoan</a>, you figure as the principal developer of the module, so, you think this is reasonable?</p>
<p>Thanks a lot <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @chir.set (2025-03-20 21:27 UTC)

<aside class="quote no-group" data-username="SANTIAGO_PENDON_MING" data-post="1" data-topic="41059">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/santiago_pendon_ming/48/66060_2.png" class="avatar"> SANTIAGO_PENDON_MING:</div>
<blockquote>
<p>split the tolerance in a lower and and a higher tolerance</p>
</blockquote>
</aside>
<p>Your request concerns more the “Flood filling” effect at <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/784997471e8e4dfede24ab9618519b95be5b4e4d/SegmentEditorFloodFilling/SegmentEditorFloodFillingLib/SegmentEditorEffect.py#L248" rel="noopener nofollow ugc">this line</a>, rather than the “Guided artery segmentation” module. The latter just makes use of the former as it is.</p>

---
