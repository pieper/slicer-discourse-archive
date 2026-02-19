---
topic_id: 46113
title: "Regarding Radius Of Centerline Curve"
date: 2026-02-10
url: https://discourse.slicer.org/t/46113
---

# Regarding radius of centerline curve

**Topic ID**: 46113
**Date**: 2026-02-10
**URL**: https://discourse.slicer.org/t/regarding-radius-of-centerline-curve/46113

---

## Post #1 by @Mudrika (2026-02-10 16:59 UTC)

<p>Hello everyone!</p>
<p>I am extracting centerline curves from a 3D model of coronary arteries and further through centerline quantiifcation, radius of the arteries is calculated. Can someone please tell, is it the average radius along teh centerline segment? As the arteries are non-circular in nature, what value of radius is reported?</p>
<p>Thank you in advance!</p>

---

## Post #2 by @chir.set (2026-02-10 18:16 UTC)

<aside class="quote no-group" data-username="Mudrika" data-post="1" data-topic="46113">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/c57346/48.png" class="avatar"> Mudrika:</div>
<blockquote>
<p>Can someone please tell, is it the average radius along teh centerline segment?</p>
</blockquote>
</aside>
<p>Yes, it’s the <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/3f95934e30284ad2f882d21813beb365cbd87de6/ExtractCenterline/ExtractCenterline.py#L871" rel="noopener nofollow ugc">average</a> of all the radii measured at each point of the centerline curve.</p>
<p>If you need details, consider using the <code>Cross-section analysis</code> module. It can show the</p>
<ul>
<li>maximum inscribed sphere diameter (MIS), which is the largest sphere that could fit at a given point of the centerline by the VMTK libraries,</li>
<li>circular equivalent diameter (CE), which is derived from the cross-section area of the lumen at a given point.</li>
</ul>
<p>The average radius mentioned above is calculated from the MIS radii.</p>
<p>As for ‘<em>Which one should I use?</em>’, your research purposes have the answer.</p>

---

## Post #3 by @Mudrika (2026-02-11 12:09 UTC)

<p>Thank you so much for the clarification!</p>

---
