---
topic_id: 47224
title: "Decrease file sizes"
date: 2026-06-03
url: https://discourse.slicer.org/t/47224
last_bumped: 2026-06-04T00:21:52.497Z
---

# Decrease file sizes

**Topic ID**: 47224
**Date**: 2026-06-03
**URL**: https://discourse.slicer.org/t/decrease-file-sizes/47224

---

## Post #1 by @FabricioFO (2026-06-03 14:52 UTC)

<p>Hello, everyone. I’m trying to upload my ctscans, but the filles are really big, the resolution is too high. I wanna know how do you solve this kind of problem,</p>
<p><span lang="en">How do you reduce file sizes without losing quality?</span></p>

---

## Post #2 by @muratmaga (2026-06-03 15:58 UTC)

<p>Assuming you have microCT scans, read this tutorial: <a href="https://github.com/SlicerMorph/Tutorials/tree/main/ImageStacks" class="inline-onebox" rel="noopener nofollow ugc">Tutorials/ImageStacks at main · SlicerMorph/Tutorials · GitHub</a></p>

---

## Post #3 by @aiden.zhu (2026-06-04 00:21 UTC)

<p>Here are a few strategies you can try to reduce your file size:</p>
<ul>
<li>
<p><strong>A. Crop to a specific Region of Interest (ROI):</strong> Focus only on smaller sub-regions. This is the only method that reduces file size without sacrificing high-resolution image quality.</p>
</li>
<li>
<p><strong>B. Convert bit depth (e.g., 16-bit/32-bit to 8-bit):</strong> While lowering the bit depth reduces data size, it will affect image quality to some degree. Success depends heavily on the contrast of your features.</p>
</li>
<li>
<p><strong>C. Downsample the data:</strong> You can bin the data (e.g., 2x2x2 or 3x3x3). This reduces overall quality, but finding the right downsampling factor can drastically shrink file sizes while keeping the quality acceptable.</p>
</li>
<li>
<p><strong>D. Apply lossless compression:</strong> If you simply need a smaller file for storage or transfer, try compressing it into a ZIP file.</p>
</li>
</ul>

---
