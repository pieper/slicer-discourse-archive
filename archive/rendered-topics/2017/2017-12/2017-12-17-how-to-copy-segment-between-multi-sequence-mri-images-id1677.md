---
topic_id: 1677
title: "How To Copy Segment Between Multi Sequence Mri Images"
date: 2017-12-17
url: https://discourse.slicer.org/t/1677
---

# How to copy segment between multi-Sequence MRI images

**Topic ID**: 1677
**Date**: 2017-12-17
**URL**: https://discourse.slicer.org/t/how-to-copy-segment-between-multi-sequence-mri-images/1677

---

## Post #1 by @1111 (2017-12-17 23:21 UTC)

<p>Operating system: mac<br>
Slicer version: 4.8</p>
<p>Dear all，<br>
i have constructed some segments in T1+contrast axial images, but i also want to construct same  segments in T1 and T2 axial images，then export all segments as RT structures based on this three different images，but i don‘t know how to deal with it. Does any body can help me？<br>
Thanks<br>
Zilong</p>

---

## Post #2 by @lassoan (2017-12-18 00:10 UTC)

<p>This all sounds feasible. How far have you got? Do you have any specific question?</p>

---

## Post #3 by @1111 (2017-12-18 00:16 UTC)

<p>Thanks for your help！<br>
Now i know how to construct segment，and how to export as RT structure！but i don‘t  know how to construct  same segment in other MRI sequence，then export as RT structure！any suggestion？thanks<br>
zilong</p>

---

## Post #4 by @lassoan (2017-12-18 05:45 UTC)

<aside class="quote no-group" data-username="1111" data-post="3" data-topic="1677">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/1/71e660/48.png" class="avatar"> 1111:</div>
<blockquote>
<p>how to construct  same segment in other MRI sequence</p>
</blockquote>
</aside>
<p>Add new segments, select the other MRI image as master volume, and segment structures using that volume.</p>
<aside class="quote no-group" data-username="1111" data-post="3" data-topic="1677">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/1/71e660/48.png" class="avatar"> 1111:</div>
<blockquote>
<p>export as RT structure</p>
</blockquote>
</aside>
<p>Install SlicerRT extension and follow instructions in <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM#DICOM_export">DICOM module documentation</a>.</p>

---

## Post #5 by @1111 (2017-12-18 06:01 UTC)

<p>yes, i know this step, but i want to know how to link the fist construct segment with  other master volume, i need to make sure the segment in all MRI sequences are the same。<br>
thanks for your reply！</p>

---

## Post #6 by @doc-xie (2017-12-18 07:54 UTC)

<p>Hello,Professor Lassoan!<br>
How to estimate the data notes are in a DICOM-compliant hierarchy and can be exported to DICOM files?<br>
Best wishes!<br>
doc-xie</p>

---

## Post #7 by @lassoan (2017-12-18 14:15 UTC)

<p>When you export an RT structure set, it is always associated with the volume that is in the same DICOM study. To export the same structure set for different volumes, copy or move the segmentation node into each study and then export the study.</p>

---

## Post #8 by @1111 (2017-12-18 17:32 UTC)

<p>ok, got it. I will try! thanks</p>

---
