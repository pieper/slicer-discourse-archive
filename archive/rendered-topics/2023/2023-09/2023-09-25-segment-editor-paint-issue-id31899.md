---
topic_id: 31899
title: "Segment Editor Paint Issue"
date: 2023-09-25
url: https://discourse.slicer.org/t/31899
---

# Segment Editor Paint Issue

**Topic ID**: 31899
**Date**: 2023-09-25
**URL**: https://discourse.slicer.org/t/segment-editor-paint-issue/31899

---

## Post #1 by @Hannah_Osland (2023-09-25 22:53 UTC)

<p>I am trying to use the segment editor feature to isolate an organ in my animal scans. When I attempt to paint using the segment editor tool, it doesn’t persist. Here were my steps</p>
<ol>
<li>Load .tiff files using ImageStacks on the SlicerMorph extension</li>
<li>Volume render into 3D</li>
<li>Go to segment editor, create new volume, paint tool</li>
</ol>
<p>When I attempt to paint, the paint does not seem to be going onto the 3D volume projection, so maybe it is something wrong with how I am loading my files?</p>

---

## Post #2 by @muratmaga (2023-09-25 23:04 UTC)

<p>Volume rendering and segmentation serve different purposes. If you want to see the 3D of your segmentation, then skip step 2 and click the Show 3D button in segment editor.</p>

---

## Post #3 by @muratmaga (2023-09-26 01:18 UTC)

<aside class="quote no-group" data-username="Hannah_Osland" data-post="1" data-topic="31899">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hannah_osland/48/65515_2.png" class="avatar"> Hannah_Osland:</div>
<blockquote>
<p>When I attempt to paint, the paint does not seem to be going onto the 3D volume projection, so maybe it is something wrong with how I am loading my files?</p>
</blockquote>
</aside>
<p>You may want to read this section before going any further on your project: <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html" class="inline-onebox">Image Segmentation — 3D Slicer documentation</a></p>

---
