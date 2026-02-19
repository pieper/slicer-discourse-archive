---
topic_id: 39481
title: "Intracranial 4D Flow Mri Getting Unknown Error"
date: 2024-10-01
url: https://discourse.slicer.org/t/39481
---

# Intracranial 4D Flow MRI...Getting unknown error

**Topic ID**: 39481
**Date**: 2024-10-01
**URL**: https://discourse.slicer.org/t/intracranial-4d-flow-mri-getting-unknown-error/39481

---

## Post #1 by @sannpeterson (2024-10-01 22:32 UTC)

<p>I’ve been using Siemens’ WIP (work-in-progress) 4D Flow MRI sequence for the past few months, and I’ve encountered an occasional issue. In 3 out of 20 cardiac phases, there is a complete reversal of flow in all vessels across the image, in every direction. Left-to-right flow appears as right-to-left, anterior-to-posterior shows as posterior-to-anterior, and so on. I haven’t been able to identify the cause of this anomaly. I’ve been scanning both the brain and chest, but this problem only occurs in some of the brain scans, despite using an adequate venc setting. Both Siemens and our techs suspect aliasing, but the issue seems different from typical aliasing artifacts. I’ve also attempted phase unwrapping with various commercial software, but it hasn’t resolved the problem.</p>
<p>Hoping for some insight as well as possible fixes. Tysm!</p>
<p><a href="https://we.tl/t-ZWak9F2eU1" rel="noopener nofollow ugc">link to dicom</a></p>

---

## Post #2 by @pieper (2024-10-04 18:12 UTC)

<p>How are you loading this data?  It’s not loading as a sequence for me (maybe due to anonymization).</p>

---

## Post #3 by @sannpeterson (2024-10-18 18:27 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="39481">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>? It’s not loading as a sequence for me (maybe due to an</p>
</blockquote>
</aside>
<p>I’m using a 4d flow analysis software. I normally don’t anonymize it before importing into the software but I did to share the dataset.</p>

---
