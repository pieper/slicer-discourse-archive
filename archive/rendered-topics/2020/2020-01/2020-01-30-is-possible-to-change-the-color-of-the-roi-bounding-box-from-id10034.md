---
topic_id: 10034
title: "Is Possible To Change The Color Of The Roi Bounding Box From"
date: 2020-01-30
url: https://discourse.slicer.org/t/10034
---

# Is possible to change the color of the ROI bounding box from white to something else

**Topic ID**: 10034
**Date**: 2020-01-30
**URL**: https://discourse.slicer.org/t/is-possible-to-change-the-color-of-the-roi-bounding-box-from-white-to-something-else/10034

---

## Post #1 by @muratmaga (2020-01-30 18:59 UTC)

<p>While there seems many settings under the <strong>Modify Annotation Properties</strong> none of them seem to change the ROI bounding box color from the default white. We have images that we are trying to crop and the background is  white, making it hard to see where box is. Can this setting be modified?</p>

---

## Post #2 by @lassoan (2020-01-30 19:49 UTC)

<p>Probably it wouldn’t be too hard to propagate annotation line colors to the ROI representation, but we don’t plan to touch annotation ROIs but instead we will add a new markups ROI class instead.</p>

---

## Post #3 by @pieper (2020-01-30 21:05 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> if you are really desperate there’s probably a way to hack into it and change the color, but it wouldn’t be sustainable and probably not worth the effort.  Might be easier to change the lookup table while cropping.</p>

---

## Post #4 by @muratmaga (2020-01-30 23:03 UTC)

<p>Changing the W/L until lines are visible works.</p>

---

## Post #5 by @timeanddoctor (2020-02-08 06:28 UTC)

<p>roiNode.SetLineColor([1,0,0]), but nothing happen…</p>

---

## Post #6 by @lassoan (2020-02-08 17:46 UTC)

<p>There is no API to change ROI node color and we don’t plan to add it but instead add ROI support to markups node and implement it there (see my comment <a href="https://discourse.slicer.org/t/is-possible-to-change-the-color-of-the-roi-bounding-box-from-white-to-something-else/10034/2">above</a>).</p>

---
