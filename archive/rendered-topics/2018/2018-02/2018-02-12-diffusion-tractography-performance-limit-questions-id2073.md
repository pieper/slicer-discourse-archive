---
topic_id: 2073
title: "Diffusion Tractography Performance Limit Questions"
date: 2018-02-12
url: https://discourse.slicer.org/t/2073
---

# Diffusion tractography performance limit questions

**Topic ID**: 2073
**Date**: 2018-02-12
**URL**: https://discourse.slicer.org/t/diffusion-tractography-performance-limit-questions/2073

---

## Post #1 by @jamesjcook (2018-02-12 18:17 UTC)

<p>I’m trying to use slicer to visualize tracks. My diffusion volumes were 275x225x450 with 0.2mm voxels.</p>
<p>Has anyone explored the limits of track visualization? Memory usage appears strangely high when I load in my tracks, the vtk fiberbundles are less than 1GiB on disk, but use 25+GiB in RAM.</p>
<p>My total number of tracks may be high, it seems to indicate I’m loading 200,000+ tracks in about 20 different vtk fiberbundle files. Some of which have 45,000, others having only 200-1000.</p>
<p>When these tracks are initially loaded the interface is frustratingly slow/laggy, even after disabling the display modules. I’ve tested in slicer 4.6, 4.8, and nightly of 2018-02-06. After saving and loading all tracks and the scene, and switching visualization to lines colored by segment, instead of tubes, the interface behaves reasonably.</p>

---

## Post #2 by @ihnorton (2018-02-13 14:46 UTC)

<p>I’m working on performance improvements for this issue. My current largest test-set is about 400MB, so if you are able to share your dataset, I would be interested in looking at it (via dropbox, gdrive, etc. – if you want to email me: <code>inorton at bwh dot harvard dot edu</code>).</p>
<blockquote>
<p>switching visualization to lines colored by segment, instead of tubes</p>
</blockquote>
<p>The performance difference between these two should go away soon, thanks to the VTK opengl2 improvements.</p>

---
