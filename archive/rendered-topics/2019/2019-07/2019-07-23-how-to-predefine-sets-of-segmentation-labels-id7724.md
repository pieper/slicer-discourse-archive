---
topic_id: 7724
title: "How To Predefine Sets Of Segmentation Labels"
date: 2019-07-23
url: https://discourse.slicer.org/t/7724
---

# How to predefine sets of segmentation labels?

**Topic ID**: 7724
**Date**: 2019-07-23
**URL**: https://discourse.slicer.org/t/how-to-predefine-sets-of-segmentation-labels/7724

---

## Post #1 by @storno (2019-07-23 12:32 UTC)

<p>Hi there</p>
<p>For a segmentation task in with MRI data I would like to predefine a set of segmentation labels, e.g. T1_segmentations with segments T1_Liver and T1_spleen and the same for T2. Is there a button in the GUI I am missing that provides this functionality or can it be implemented any other way?</p>
<p>Thanks, Steph</p>

---

## Post #2 by @cpinter (2019-07-23 14:00 UTC)

<p>Hi Steph,</p>
<p>Do you need a pre-populated segmentation, or a reduced set of items in the terminology selector (that opens when you double-click color)?</p>
<p>If the former, then you can create a segmentation where you add segments with the proper terminology, color, name, etc. and then you can reuse it. For example you can save it as a scene and load that when you start a new segmentation. If you need to start multiple segmentations in the same session, keep the template and clone it every time you need to start a new one (right-click menu in Data module).</p>
<p>If the latter, you need to create a json file that contains only the terminology items you need. Just copy one of the presets that come with Slicer and remove what you don’t need.</p>

---

## Post #3 by @lassoan (2019-07-23 18:15 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="2" data-topic="7724">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>If the former, then you can create a segmentation where you add segments with the proper terminology, color, name, etc. and then you can reuse it. For example you can save it as a scene and load that when you start a new segmentation.</p>
</blockquote>
</aside>
<p>Just this week we added new filter and search tools to the segment list to facilitate this use case. You can find segments in the segmentation by using the filter and then set its state to “in progress” (or “flagged”) and use filter buttons to show only those selected segments.</p>
<p><img src="https://user-images.githubusercontent.com/9222709/61647000-6317c300-ac7a-11e9-9c30-1d17f0a08539.png" alt="" role="presentation" width="" height=""></p>

---
