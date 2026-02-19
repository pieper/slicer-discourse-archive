---
topic_id: 28808
title: "Kidney Tumor Segmentation"
date: 2023-04-07
url: https://discourse.slicer.org/t/28808
---

# Kidney tumor segmentation

**Topic ID**: 28808
**Date**: 2023-04-07
**URL**: https://discourse.slicer.org/t/kidney-tumor-segmentation/28808

---

## Post #1 by @zaher_bahouth (2023-04-07 22:30 UTC)

<p>I’m a kidney surgeon, trying to find the best way to do segmentation for kidney and kidney tumors on DICOM ct scans<br>
Is there any extension that could be helpful?</p>

---

## Post #2 by @lassoan (2023-04-07 22:35 UTC)

<p>You can segment kidneys on CT images fully automatically using <a href="https://github.com/lassoan/SlicerTotalSegmentator#totalsegmentator">TotalSegmentator</a>.</p>
<p>You can segment tumors in them using Segment Editor’s Grow from seeds tool as shown here:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="cybL5A0w3hw" data-video-title="Brain tumor segmentation on MRI in 1 minute" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=cybL5A0w3hw" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/cybL5A0w3hw/maxresdefault.jpg" title="Brain tumor segmentation on MRI in 1 minute" width="" height="">
  </a>
</div>

<p>After some practice, it should not take more than 1-2 minutes, so it is probably not worth investing too much time into automating it. However, if you want to automate it and you have lots of CT scans with kidney tumors (probably a hundred or so would suffice) then you can train an AI model using <a href="https://github.com/Project-MONAI/MONAILabel/tree/main/plugins/slicer#monai-label-plugin-for-3d-slicer">MONAILabel extension</a> to automatically segment the tumors, too.</p>

---

## Post #3 by @zaher_bahouth (2023-04-08 06:35 UTC)

<p>Thank you so much for the reply. That’s extremely helpful…<br>
I’ll give it a try and write back if i still need any help…</p>

---
