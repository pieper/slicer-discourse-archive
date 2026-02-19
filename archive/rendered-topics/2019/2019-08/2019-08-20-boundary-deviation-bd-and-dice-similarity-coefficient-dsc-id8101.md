---
topic_id: 8101
title: "Boundary Deviation Bd And Dice Similarity Coefficient Dsc"
date: 2019-08-20
url: https://discourse.slicer.org/t/8101
---

# Boundary deviation (BD) and Dice Similarity Coefficient (DSC)

**Topic ID**: 8101
**Date**: 2019-08-20
**URL**: https://discourse.slicer.org/t/boundary-deviation-bd-and-dice-similarity-coefficient-dsc/8101

---

## Post #1 by @MFS-YES (2019-08-20 01:44 UTC)

<p>Operating system:<br>
Slicer version: Hello!</p>
<p>I want to calculate <strong>Boundary deviations or differences (BD)</strong> and <strong>Dice Similarity Coefficient (DSC)</strong> for a 3D image on slicer and show error map (from 0 to 1). I evaluate BD by using superimposition method and display error map, am I on a good way? But I don’t know the way or module to calculate DSC via slicer. Need help. Thanks!<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @lassoan (2019-08-21 16:29 UTC)

<p>You can get Hausdorff distance and Dice similarity coefficient using “Segment Comparison” module (in SlicerRT extension). You can compute an error map by exporting segments to models and computing distances using “Model to model distance” extension.</p>

---

## Post #3 by @MFS-YES (2019-08-21 19:12 UTC)

<p>thanks!</p>
<p><a href="https://go.onelink.me/107872968?pid=InProduct&amp;c=Global_Internal_YGrowth_AndroidEmailSig__AndroidUsers&amp;af_wl=ym&amp;af_sub1=Internal&amp;af_sub2=Global_YGrowth&amp;af_sub3=EmailSignature" rel="nofollow noopener">Envoyé depuis Yahoo Mail pour Android</a></p>

---

## Post #4 by @Young_Wang (2023-12-13 21:51 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="8101">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>SlicerRT</p>
</blockquote>
</aside>
<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>, I’m using Slicer 5.6 and I have trouble of locating Hausdorff distance and Dice similarity coefficient and “Segment Comparison” module. I have installed (in SlicerRT extension. Could you please point me to where this module is? Thanks.</p>

---
