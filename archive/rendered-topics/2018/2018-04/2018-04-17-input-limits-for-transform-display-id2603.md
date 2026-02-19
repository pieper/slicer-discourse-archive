---
topic_id: 2603
title: "Input Limits For Transform Display"
date: 2018-04-17
url: https://discourse.slicer.org/t/2603
---

# Input limits for transform display

**Topic ID**: 2603
**Date**: 2018-04-17
**URL**: https://discourse.slicer.org/t/input-limits-for-transform-display/2603

---

## Post #1 by @david-hoffman (2018-04-17 00:46 UTC)

<p>Operating system: Windows 10 Pro 1709 build 16299.309<br>
Slicer version: 4.8.1<br>
Expected behavior: Any numerical input allowed<br>
Actual behavior: input limited to numbers greater than 0.01</p>
<p>I have transform files that are output by ANTs (<a href="https://github.com/ANTsX/ANTs" rel="nofollow noopener">https://github.com/ANTsX/ANTs</a>) and associated image data. However the voxel sizes are 0.024 or smaller and I’d like to be able to visualize the deformation field but I’m limited in how small I can make the spacing, how large I can make the scale factor, etc.</p>
<p>Is there some way to override these safeguards?</p>

---

## Post #2 by @lassoan (2018-04-17 02:16 UTC)

<p>You can set the values using the Python console, for example:</p>
<pre><code>getNode('LinearTransform_3').GetDisplayNode().SetGlyphSpacingMm(0.01)
</code></pre>
<p>I’ll have a look how the range could be made more customizable using the GUI.</p>

---
