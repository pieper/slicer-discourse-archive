---
topic_id: 16180
title: "Dicom File Issue With Virtual Surgery Planning Software"
date: 2021-02-24
url: https://discourse.slicer.org/t/16180
---

# dicom file issue with virtual surgery planning software

**Topic ID**: 16180
**Date**: 2021-02-24
**URL**: https://discourse.slicer.org/t/dicom-file-issue-with-virtual-surgery-planning-software/16180

---

## Post #1 by @mohammed_alshakhas (2021-02-24 13:38 UTC)

<p>I use IPS case planner for facial surgery planning.</p>
<p>i have issues with uploading medical ct images .dcm , error "no valid data set is recognized "<br>
it only accepts dicom exported from Cone beam CT. which usually comes as a merged file.</p>
<p>is there anything i can do in slicer to transform or convert dicom files you think might work to solve this issue?</p>
<p>thnx</p>

---

## Post #2 by @lassoan (2021-02-25 17:01 UTC)

<p>What is “IPS case planner”? Is it a Slicer module or extension; or some third-party software?</p>
<p>Did you try to load a DICOM series exported by Slicer into it?</p>
<aside class="quote no-group" data-username="mohammed_alshakhas" data-post="1" data-topic="16180">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mohammed_alshakhas/48/10025_2.png" class="avatar"> mohammed_alshakhas:</div>
<blockquote>
<p>i have issues with uploading medical ct images .dcm , error "no valid data set is recognized "<br>
it only accepts dicom exported from Cone beam CT. which usually comes as a merged file.</p>
</blockquote>
</aside>
<p>Every DICOM compliant medical device has a publicly accessible DICOM conformance statement document, which states what kind of data it can read. You can usually find it by web search.</p>
<p>This document will tell you what kind of DICOM files the device accepts. For example, if it requires cone-beam CT, if it can accept standard CT information object (one file per slice) or requires enhanced multiframe CT information object (one file per volume).</p>

---

## Post #3 by @mohammed_alshakhas (2021-02-26 06:50 UTC)

<p>this a third party software , yet it doesn’t allow me to upload only images i obtain from medical CT from my hospital machine . other hospital don’t have the same issue . they can upload medical CT and or CBCT .</p>
<p>i hate CBCT cause the artifact level is so high you can’t segment a decent model .</p>
<p>the developer of this software is not giving me a real solution unfortunately.</p>

---

## Post #4 by @lassoan (2021-02-26 13:58 UTC)

<p>What is the exact vendor/model of the planning software? Have you found its DICOM conformance statement?</p>
<p>What is the vendor/model of the CT? If you can share a data set that the software does not load (phantom, animal, or anonymized patient data) then we can have a look if we see any obvious errors in it (missing file, missing field, unusual compression, special characters in names, etc.).</p>

---
