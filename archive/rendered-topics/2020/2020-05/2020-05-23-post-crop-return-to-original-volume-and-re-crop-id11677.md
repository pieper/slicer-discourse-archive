---
topic_id: 11677
title: "Post Crop Return To Original Volume And Re Crop"
date: 2020-05-23
url: https://discourse.slicer.org/t/11677
---

# Post-crop return to original volume and re-crop

**Topic ID**: 11677
**Date**: 2020-05-23
**URL**: https://discourse.slicer.org/t/post-crop-return-to-original-volume-and-re-crop/11677

---

## Post #1 by @Hannnonk (2020-05-23 18:27 UTC)

<p>Operating system:windows 10<br>
Slicer version:</p>
<ol>
<li>enter dicom</li>
<li>successfully crop and segment</li>
<li>is there any way to return to the original volume to do another crop?</li>
</ol>
<p>thx</p>

---

## Post #2 by @lassoan (2020-05-23 18:29 UTC)

<p>If you haven’t overwritten the original DICOM volume that you loaded (by default, it is not overwritten but a new cropped volume is created), then you can just modify the ROI, choose <code>Output volume</code> -&gt; <code>Create new volume</code>, and click <code>Apply</code>.</p>

---
