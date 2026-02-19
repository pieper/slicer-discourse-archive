---
topic_id: 9621
title: "Limitation In Increasing The Resolution In Crop Volume Modul"
date: 2019-12-26
url: https://discourse.slicer.org/t/9621
---

# Limitation in increasing the resolution in Crop Volume module

**Topic ID**: 9621
**Date**: 2019-12-26
**URL**: https://discourse.slicer.org/t/limitation-in-increasing-the-resolution-in-crop-volume-module/9621

---

## Post #1 by @Tekk_ya (2019-12-26 13:13 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.10.1 and 4.10.2</p>
<p>Hi all,</p>
<p>I want to increase the resolution of CT scans in the crop volume module. I have cropped the original scan with my selected ROI and I haven’t applied any interpolation (let’s call this volume as the “cropped scan”). I am trying to increase the resolution of the cropped scan. So, I have the cropped scan as input and I use the “Spacing scale” of 0.25. The problem is that after pressing “apply” everything seems normal but when I checked the scan’s resolution in the “Data” module, I realized that the output scan has exactly the same dimension and spacing as the cropped scan. I have checked the spacing scale of 0.5  and it works fine. This means that I cannot increase the resolution with a spacing scale of less than 0.5. Would you please let me know why I face such a problem and how I can fix it? I have tried the same procedure on two different PCs and I see the same behavior on both.</p>

---

## Post #2 by @lassoan (2019-12-26 16:11 UTC)

<aside class="quote no-group" data-username="Tekk_ya" data-post="1" data-topic="9621">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tekk_ya/48/3548_2.png" class="avatar"> Tekk_ya:</div>
<blockquote>
<p>“Spacing scale” of 0.25.</p>
</blockquote>
</aside>
<p>This increases memory usage by 4x4x4 = by a factor of 64x. If you started out with a 200MB volume, the required amount of RAM was 2GB. To be able to resample with spacing scale of 0.25, you would need 128GB of RAM. So, most likely you have run out of memory.</p>
<p>There are several solutions:</p>
<ul>
<li>not just resample but also crop the volume to a smaller region</li>
<li>increase virtual memory/swap size in system settings</li>
<li>add more physical RAM to your computer</li>
<li>choose a larger spacing scale</li>
</ul>

---
