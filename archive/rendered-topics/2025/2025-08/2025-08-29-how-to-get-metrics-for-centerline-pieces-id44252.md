---
topic_id: 44252
title: "How To Get Metrics For Centerline Pieces"
date: 2025-08-29
url: https://discourse.slicer.org/t/44252
---

# How to get metrics for centerline pieces?

**Topic ID**: 44252
**Date**: 2025-08-29
**URL**: https://discourse.slicer.org/t/how-to-get-metrics-for-centerline-pieces/44252

---

## Post #1 by @abitrolly (2025-08-29 14:34 UTC)

<p>How to split <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/Docs/ExtractCenterline.md" rel="noopener nofollow ugc">extracted centerline</a> into pieces to get curvature, torsion and tortuosity for each piece?</p>
<p>I feel like I miss something obvious, but after hours of trying I haven’t found how to do this through UI. If it is impossible, maybe somebody can point me to the right Python calls? I have coordinates of points where to split the centerlines written down manually from CT scan.</p>

---

## Post #2 by @chir.set (2025-08-29 15:04 UTC)

<p>To split a <em>bifurcated</em> centerline <em>model</em>, you can consider the <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/Docs/CenterlineDisassembly.md" rel="noopener nofollow ugc">Centerline disassembly</a> module.</p>
<p>The <code>ExtractCenterline</code> module provides metrics also.</p>
<p>You can get an overview <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/7708b85902571082ab813bf0833e13ed85e84d09/ExtractCenterline/ExtractCenterline.py#L619" rel="noopener nofollow ugc">here</a> to calculate metrics in Python.</p>

---

## Post #3 by @abitrolly (2025-08-29 17:05 UTC)

<p>Thanks for the pointers. There is a need to split <em>centerline</em> that is <em>not bifurcated</em> into subsequent pieces. On the CT scan there are places where the vein goes through different bones, and I’d like to manually split the <em>centerline</em> into pieces that correspond to these bones to measure the parameters.</p>
<p>The <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/Docs/CenterlineDisassembly.md" rel="noopener nofollow ugc">centerline disassembly</a> module mentions branches as “<em>centerline</em> parts that exclude the bifurcations”, but how to I place a point to split one continuous <em>centerline</em> into these branches?</p>

---

## Post #4 by @mikebind (2025-08-29 18:17 UTC)

<p>You can manually place the endpoints for each section and run extract centerline for each section.  Then you will have separate centerlines to take the measurements from.  If you are concerned about exactly placing the endpoint in each section in the center of the vessel, you can first extract the centerline for the whole vessel, then place your segment endpoints along the extracted full centerline.</p>

---

## Post #5 by @chir.set (2025-08-29 18:31 UTC)

<p>Ok, so it’s not splitting at bifurcations.</p>
<p><a class="mention" href="/u/mikebind">@mikebind</a> 's suggestion is probably the best thing to do.</p>
<p>If you really need to cut your centerline, the <code>Dynamic modeler</code> module allows to cut any model with a plane or a ROI for example.</p>

---

## Post #6 by @abitrolly (2025-08-31 13:56 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="4" data-topic="44252">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>extract the centerline for the whole vessel, then place your segment endpoints along the extracted full centerline</p>
</blockquote>
</aside>
<p>Thanks. I will try to find out how to place endpoints there, which view and buttons I need to press.</p>
<aside class="quote no-group" data-username="chir.set" data-post="5" data-topic="44252">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>the <code>Dynamic modeler</code> module allows to cut any model with a plane or a ROI for example</p>
</blockquote>
</aside>
<p>I am going to try this as well. Thanks.</p>

---
