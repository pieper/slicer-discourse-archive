# Nvidia for liver segmentation using segment from the boundary point

**Topic ID**: 19596
**Date**: 2021-09-09
**URL**: https://discourse.slicer.org/t/nvidia-for-liver-segmentation-using-segment-from-the-boundary-point/19596

---

## Post #1 by @akmal871026 (2021-09-09 16:54 UTC)

<p>Hello,</p>
<p>before this, I used Nvidia for liver segmentation using segments from the boundary point. but this time there not have. Why?</p>

---

## Post #2 by @lassoan (2021-09-10 04:28 UTC)

<p>We use NVidia’s latest Clara version (4.0) in the AIAA demo server and made available all of their <a href="https://ngc.nvidia.com/catalog/models?orderBy=modifiedDESC&amp;pageNumber=0&amp;query=clara_pt&amp;quickFilter=&amp;filters=">models that are compatible with this version</a>. NVidia changed the internal engine and did not port all their earlier models over. Unfortunately, the model that could segment liver from boundary points was not ported. Since the engine of Clara 4.0 is MONAI, you can ask the MONAI community if there is a chance that the model will be made available, or port the model yourself to the new version or set up your own server with Clara version 2.x.</p>
<p>There is also a lot of activity around <a href="https://github.com/Project-MONAI/MONAILabel#monai-label">MONAILabel module</a>, which also has pre-trained model for liver segmentation.</p>

---

## Post #3 by @akmal871026 (2021-09-10 04:52 UTC)

<p>How to set clara 2.x?</p>

---

## Post #4 by @lassoan (2021-09-10 04:55 UTC)

<p>You need to find a Clara 2.0 server install package and instructions, install it on a Linux computer with a strong GPU, then find pre-trained models for this server version. It is not guaranteed that these packages are still available, so check that before you invest a lot of time into this.</p>

---

## Post #5 by @akmal871026 (2021-09-15 16:10 UTC)

<p>Because the problem is, when used the auto liver and tumor segmentation, does not work properly.</p>
<p>then when used deep grow, it takes a very long time to segment and not completely function.</p>

---

## Post #6 by @akmal871026 (2021-09-15 16:17 UTC)

<p>hope you can add <strong>clara for liver</strong> on segment from boundary point. thank you so much</p>

---

## Post #7 by @lassoan (2021-09-15 16:45 UTC)

<aside class="quote no-group" data-username="akmal871026" data-post="6" data-topic="19596">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/akmal871026/48/11642_2.png" class="avatar"> akmal871026:</div>
<blockquote>
<p>hope you can add <strong>clara for liver</strong> on segment from boundary point</p>
</blockquote>
</aside>
<p>That would not be us but the MONAI community. You can reach them via various channels - as described <a href="https://monai.io/community.html">here</a>. If you post a question on their forums then add a link here so that others who are interested in this can follow up.</p>

---
