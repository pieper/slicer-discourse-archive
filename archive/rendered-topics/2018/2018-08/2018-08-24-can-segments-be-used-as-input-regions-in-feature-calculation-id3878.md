---
topic_id: 3878
title: "Can Segments Be Used As Input Regions In Feature Calculation"
date: 2018-08-24
url: https://discourse.slicer.org/t/3878
---

# Can segments be used as input regions in feature calculation?

**Topic ID**: 3878
**Date**: 2018-08-24
**URL**: https://discourse.slicer.org/t/can-segments-be-used-as-input-regions-in-feature-calculation/3878

---

## Post #1 by @TingtingYu (2018-08-24 11:53 UTC)

<p>Hi,</p>
<p>I loaded DICOM-RT using DICOM module. When I turned to Data Module, the RT structure was shown as a segment. Can this segment used as input region in radiomics calculation? I am a little confused about that. RT-Struct are planar contour, it is not a volume. But when I use it to do the radiomics calculation, I get the same answer as I use the labelmap (I use the segmentation module to export the labelmap from segment) as input region. Many thanks.</p>
<p>Best,<br>
Tingting</p>

---

## Post #2 by @lassoan (2018-08-24 12:30 UTC)

<aside class="quote no-group" data-username="TingtingYu" data-post="1" data-topic="3878">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/b38774/48.png" class="avatar"> TingtingYu:</div>
<blockquote>
<p>Can this segment used as input region in radiomics calculation?</p>
</blockquote>
</aside>
<p>Yes. Segmentation nodes dynamically convert between different representations (planar contour, binary labelmap, closed surface, etc.) as needed.</p>

---

## Post #3 by @fedorov (2018-08-24 17:59 UTC)

<p>There are at least 2 extensions in Slicer that calculate radiomics features.</p>
<ul>
<li>If you use the <a href="https://github.com/Radiomics/SlicerRadiomics">SlicerRadiomics</a> extension, you can use Segmentation segments directly.</li>
<li>If you use <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/HeterogeneityCAD">HeterogeneityCAD</a> extension, I think you will first need to convert segmentation into binary labelmap.</li>
</ul>

---

## Post #4 by @TingtingYu (2018-08-25 10:44 UTC)

<p>Hi Andras,</p>
<p>Got it. Thank you.</p>
<p>Best,<br>
Tingting</p>

---

## Post #5 by @TingtingYu (2018-08-25 10:54 UTC)

<p>Hi Andrey,</p>
<p>Thank you for your detailed suggestions. Really appreciated that. I actually have tried both of them. Quick questions, do CT images can also be used in heterogeneityCAD or this module can only use DCE-MRI images?</p>
<p>Best,<br>
Tingting</p>

---

## Post #6 by @fedorov (2018-08-26 20:56 UTC)

<p>I’ve heard people using heterogeneityCAD for CT, but I have not developed that module, and I have not used it myself. <a class="mention" href="/u/jayender">@jayender</a> should be able to give the authoritative answer.</p>

---

## Post #7 by @TingtingYu (2018-08-27 02:17 UTC)

<p>Hi Andrey,</p>
<p>Thank you. I will go to his website and then read the related topics to see whether I can dig something.</p>
<p>Best,<br>
Tingting</p>

---
