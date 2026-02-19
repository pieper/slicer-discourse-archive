---
topic_id: 36552
title: "Quantitative Rotation Scaling Translation"
date: 2024-06-02
url: https://discourse.slicer.org/t/36552
---

# Quantitative Rotation, Scaling, Translation

**Topic ID**: 36552
**Date**: 2024-06-02
**URL**: https://discourse.slicer.org/t/quantitative-rotation-scaling-translation/36552

---

## Post #1 by @yeong9316 (2024-06-02 11:08 UTC)

<p>When using the Markup function in 3D Slicer, something I always wonder about is quantitative manipulation.<br>
For example, in the case of Blender, when moving a specific object to the</p>
<p>For example, if you want to rotate the angle of Plane P created in the screen below by exactly 47 degrees by manipulating the green Rotation Bar, is there a way to rotate it by quantitatively entering this value?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aa8a350b49192646b1f905f4483c066b907f8053.png" alt="image" data-base62-sha1="okFhcSwWX1Q9jrf8HlOkp8V4PMT" width="457" height="343"></p>
<p>Also, I am curious about how to measure the degree of rotation during MPR through Slice intersection - Interaction, which is used when manipulating DICOM files, and how to initialize it to the MPR point of view that was first loaded.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/87c03a01e222b998bda91aa31d8e2ae97859a25f.jpeg" alt="image" data-base62-sha1="jmUiJcP797fn7ZlvzpZc88ecTFl" width="690" height="408"></p>

---

## Post #2 by @chir.set (2024-06-03 06:59 UTC)

<aside class="quote no-group" data-username="yeong9316" data-post="1" data-topic="36552">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/yeong9316/48/67308_2.png" class="avatar"> yeong9316:</div>
<blockquote>
<p>is there a way to rotate it by quantitatively entering this value</p>
</blockquote>
</aside>
<p>You may create a MRML transform for the plane from the Data module, then edit the transform in the ‘Transform’ module. The handles you are showing are those of an UI-only interaction transform, which is not editable otherwise.</p>

---
