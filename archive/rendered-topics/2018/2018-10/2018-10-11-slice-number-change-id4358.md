---
topic_id: 4358
title: "Slice Number Change"
date: 2018-10-11
url: https://discourse.slicer.org/t/4358
---

# Slice number change

**Topic ID**: 4358
**Date**: 2018-10-11
**URL**: https://discourse.slicer.org/t/slice-number-change/4358

---

## Post #1 by @Ash_Alarfaj (2018-10-11 12:00 UTC)

<p>Problem report for Slicer 4.8.1 macosx-amd64: [please describe expected and actual behavior]</p>
<p>expected: in the axial image (red viewer) when I’ve moved the mouse from up to down the image the slice number should be same eg. slice 44.</p>
<p>actual behavior: the slice number changes in the same image see red box slice 44 the number change from 44-43 in the same image when I move a mouse from up to down. it is really confusing. how can I know which slice I’ve analyzed.</p>

---

## Post #2 by @lassoan (2018-10-11 12:16 UTC)

<p>Slicer does not display slice number but anatomical position and voxel position in the volume.</p>
<p>As you move your mouse:</p>
<ul>
<li>you should see 2 anatomical coordinates changing (if slice orientation is set to axial, sagittal, or coronal) or 3 coordinates changing (for oblique views)</li>
<li>you should see 2 voxel coordinates changing (if slice view is rotated to volume plane - you can enforce this by clicking “rotate to volume plane” button in the slice view controller) or 3 coordinates changing (is slice view is not aligned to volume axes)</li>
</ul>

---

## Post #3 by @Ash_Alarfaj (2018-10-11 13:27 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="4358" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Slicer does not display slice number but anatomical position and voxel position in the volume.</p>
<p>As you move your mouse:</p>
<ul>
<li>you should see 2 anatomical coordinates changing (if slice orientation is set to axial, sagittal, or coronal) or 3 coordinates changing (for oblique views)</li>
<li>you should see 2 voxel coordinates changing (if slice view is rotated to volume plane - you can enforce this by clicking “rotate to volume plane” button in the slice view controller) or 3 coordinates changing (is slice view is not aligned to volume axes)</li>
</ul>
</blockquote>
</aside>
<p>thanks a lot this really helps. done the problem is fixed.<br>
all the best</p>

---
