---
topic_id: 47604
title: "How to implement real-time surgical navigation by mapping Intel RealSense D405 RGB-D camera with pre-operative CT/CBCT in 3D Slicer?"
date: 2026-07-13
url: https://discourse.slicer.org/t/47604
last_bumped: 2026-07-13T04:38:11.993Z
---

# How to implement real-time surgical navigation by mapping Intel RealSense D405 RGB-D camera with pre-operative CT/CBCT in 3D Slicer?

**Topic ID**: 47604
**Date**: 2026-07-13
**URL**: https://discourse.slicer.org/t/how-to-implement-real-time-surgical-navigation-by-mapping-intel-realsense-d405-rgb-d-camera-with-pre-operative-ct-cbct-in-3d-slicer/47604

---

## Post #1 by @abhijeet2410 (2026-07-13 04:38 UTC)

<p>Hello everyone,</p>
<p>Thank you for your kind attention.</p>
<p>We are developing a <strong>real-time intraoral surgical navigation system</strong> using <strong>3D Slicer</strong> and would appreciate guidance on the recommended workflow.</p>
<h3><a name="p-134845-objective-1" class="anchor" href="#p-134845-objective-1" aria-label="Heading link"></a>Objective</h3>
<p>Our goal is to overlay a <strong>live RGB-D camera view (Intel RealSense D405)</strong> onto a <strong>pre-operative CT/CBCT scan</strong> so that the live surgical scene is accurately mapped into the CT coordinate system.</p>
<p>The final system should provide:</p>
<ul>
<li>Live RGB image</li>
<li>Live depth image</li>
<li>Real-time point cloud</li>
<li>CT/CBCT volume</li>
<li>Live camera pose relative to CT</li>
<li>Continuous visualization during surgery</li>
</ul>
<h3><a name="p-134845-current-hardware-2" class="anchor" href="#p-134845-current-hardware-2" aria-label="Heading link"></a>Current Hardware</h3>
<ul>
<li>Intel RealSense D405</li>
</ul>
<p>For example <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=15" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>We don’t have a sensor at the end of the suction tip. We want to visualize the live 2D operation view together with the CT image in 3D Slicer. Should we purchase a specific camera for this purpose, or do we need an additional sensor? If we use a sensor, the suction tip position and operation should be highlighted in both the live 2D view and the corresponding CT image. Thank you.</p>

---
