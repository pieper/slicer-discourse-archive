---
topic_id: 12961
title: "Create More Than One Conversion Rule In Developped Module"
date: 2020-08-12
url: https://discourse.slicer.org/t/12961
---

# Create more than one conversion rule in developped module

**Topic ID**: 12961
**Date**: 2020-08-12
**URL**: https://discourse.slicer.org/t/create-more-than-one-conversion-rule-in-developped-module/12961

---

## Post #1 by @loubna (2020-08-12 08:37 UTC)

<p>Hi;<br>
I have developed a new reconstruction module in slicerRT.</p>
<p>I have created new conversion rule (planar Contours-&gt;Closed surface) in which I have implemented a contours based reconstruction method. In fact it works fine if segmentations have high quality, but it fails with intricate objects.</p>
<p>My question how can I create many conversions rules in my module? for exemple like planarContours-&gt;RibbonModel-&gt;BinaryLabelMap-&lt;Closedsurface?</p>
<p>If I create two conversion rules (for exemple PlanarContours-&gt;RibbonModel) and (Ribbon Model-&gt;BinaryLabelMap). They are separated and dont appear in the same line when I click on closed surface update Botton.</p>
<p>It may be there is Something to do when registering rules in logic Module?</p>
<p>I would like to get planarContours-&gt;RibbonModel-&gt;BinaryLabelMap-&lt;Closedsurface?</p>
<p>Thank’s in advance</p>

---

## Post #2 by @lassoan (2020-08-13 13:20 UTC)

<p>You can register any number of conversion rules. By default, Slicer will choose the combination of rules that can accomplish a conversion with the minimum cost, but you can choose a different path manually.</p>

---
