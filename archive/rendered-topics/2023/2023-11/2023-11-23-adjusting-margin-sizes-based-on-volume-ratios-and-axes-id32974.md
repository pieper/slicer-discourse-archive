---
topic_id: 32974
title: "Adjusting Margin Sizes Based On Volume Ratios And Axes"
date: 2023-11-23
url: https://discourse.slicer.org/t/32974
---

# Adjusting margin sizes based on volume ratios and axes

**Topic ID**: 32974
**Date**: 2023-11-23
**URL**: https://discourse.slicer.org/t/adjusting-margin-sizes-based-on-volume-ratios-and-axes/32974

---

## Post #1 by @ally7113 (2023-11-23 08:39 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/75862ddbdd589518b4428be94082952485bff775.png" alt="화면 캡처 2023-11-23 173352" data-base62-sha1="gLFlaMMNTmaOaEfBO20ENNHtc1v" width="621" height="266"></p>
<p>Sorry for the low-quality image…</p>
<p>I would like to expand the existing segment in three directions based on the volume ratio.<br>
For instance, I want to expand by 5% along the x-axis, 10% along the y-axis, and 10% along the z-axis. However, the margins are in millimeters, and I observed that the growth occurs uniformly in all three directions.</p>
<p>As I am not familiar with Slicer and Python, I would greatly appreciate it if you could provide detailed instructions on how to achieve this.</p>

---

## Post #2 by @muratmaga (2023-11-23 21:01 UTC)

<p>You can use PadImage filter in Simple filters which allows you to pad image in any value along 6 axis.</p>
<p>You can alternatively draw ROI and modify its extends under the ROI settings to  match dimensions you want and then use the Crop Volume module.</p>

---
