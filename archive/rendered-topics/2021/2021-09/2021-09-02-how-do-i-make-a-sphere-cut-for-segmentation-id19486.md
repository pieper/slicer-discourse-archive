---
topic_id: 19486
title: "How Do I Make A Sphere Cut For Segmentation"
date: 2021-09-02
url: https://discourse.slicer.org/t/19486
---

# How do I make a sphere cut for segmentation?

**Topic ID**: 19486
**Date**: 2021-09-02
**URL**: https://discourse.slicer.org/t/how-do-i-make-a-sphere-cut-for-segmentation/19486

---

## Post #1 by @akshay_pillai (2021-09-02 16:39 UTC)

<p>I want to create a sphere segment. I try to use scissors and circle effect but that doesn’t result in a good sphere. I am looking to obtain something like this : <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/71f8b10f1e74da2f78f17ea2e8ba6bbf705cd8e2.png" alt="MicrosoftTeams-image" data-base62-sha1="ggeLXtbqtOVBCfododecXmcHA7U" width="312" height="304"></p>
<p>How can I obtain this? just the sphere part.</p>

---

## Post #2 by @lassoan (2021-09-02 17:50 UTC)

<p>What you show should be easily achievable with the Scissors effect. You can also use the Paint effect, with “sphere brush” option enabled. You may also use markups to let the user specify a sphere, for example, <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#specify-a-sphere-by-multiple-of-markups-points">using markups fiducials</a>.</p>

---
