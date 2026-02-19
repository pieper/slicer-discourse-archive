---
topic_id: 11129
title: "Lofting Creating A Volume From Two Surfaces Segmentations"
date: 2020-04-15
url: https://discourse.slicer.org/t/11129
---

# Lofting - Creating a volume from two surfaces, segmentations

**Topic ID**: 11129
**Date**: 2020-04-15
**URL**: https://discourse.slicer.org/t/lofting-creating-a-volume-from-two-surfaces-segmentations/11129

---

## Post #1 by @Fluvio_Lobo (2020-04-15 18:35 UTC)

<p>Hello,</p>
<p>Is there a way to create a volume from a linear interpolation between two segmentations? This would similar to a “loft” in a CAD package. Also similar to a “sweep” but without relying on a path.</p>
<p>To be more specific:</p>
<ol>
<li>I create a segmentation by painting (segment editor) a circle on a slice</li>
<li>I scroll down a handful of slices (end-point) and paint a second circle or oval</li>
</ol>
<p>Here I would like to know if there is a tool/way to paint in between both segments (interpolate) to create a volume.</p>
<p>I know there are center-line tools, but the area of interest is not bound (i.e. is not the inside of a vessel, or airway passage).</p>
<p>Thank you!</p>

---

## Post #2 by @Sunderlandkyl (2020-04-15 18:58 UTC)

<p>Have you tried the “Fill between Slices” effect?<br>
I think that it should do what you are looking for.</p>

---

## Post #3 by @Fluvio_Lobo (2020-04-15 21:25 UTC)

<p>That worked flawlessly!</p>

---
