---
topic_id: 47021
title: "Error In Total Segmentor Macos"
date: 2026-05-14
url: https://discourse.slicer.org/t/47021
---

# Error In total Segmentor macOS 

**Topic ID**: 47021
**Date**: 2026-05-14
**URL**: https://discourse.slicer.org/t/error-in-total-segmentor-macos/47021

---

## Post #1 by @Gabriel.LA (2026-05-14 06:26 UTC)

<p>Command ‘[’/Applications/Slicer.app/Contents/bin/../bin/PythonSlicer’, ‘/Applications/Slicer.app/Contents/lib/Python/bin/TotalSegmentator’, ‘-i’, ‘/private/var/folders/3n/nb74wlx17txbbdx1b3cjlwym0000gn/T/Slicer-gabriellunardiaranha/__SlicerTemp__2026-05-13_20+07+54.798/total-segmentator-input.nii’, ‘-o’, ‘/private/var/folders/3n/nb74wlx17txbbdx1b3cjlwym0000gn/T/Slicer-gabriellunardiaranha/__SlicerTemp__2026-05-13_20+07+54.798/segmentation’, ‘–device’, ‘cpu’, ‘–ml’, ‘–task’, ‘total’]’ returned non-zero exit status 1.</p>
<pre><code class="lang-auto">
</code></pre>
<p><span lang="en">I’m trying to use Total Segmentor 3D Slicer 10.0 without success. I’ve already updated Python, NuNet, and everything else available in other topics. Thanks.</span></p>

---

## Post #2 by @lassoan (2026-05-14 06:41 UTC)

<p>The problem was fixed recently. You need to install Slicer from scratch (remove or rename your current Slicer and install Slicer again) to start from a clean, tested state. Once you installed Slicer, you only need to install TotalSegmentator, then load an image (e.g., CTChest sample data) and it will all work (first time it takes about 5-10 minutes to install all required Python packages).</p>

---
