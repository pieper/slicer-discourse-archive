# Resolving Markup Interaction Slowdown on Model Nodes in 3D Viewer

**Topic ID**: 38010
**Date**: 2024-08-23
**URL**: https://discourse.slicer.org/t/resolving-markup-interaction-slowdown-on-model-nodes-in-3d-viewer/38010

---

## Post #1 by @park (2024-08-23 08:18 UTC)

<p>Hi all,</p>
<p>Like the video below, the interaction speed of the <code>Markups</code> slows down significantly when hovering over the <code>ModelNode</code> (in the video, it’s a  tooth scan), causing the FPS to drop to around 8. Is there a way to resolve this issue?</p>
<p>I believe the slowdown might be due to the markup performing some calculations with the model node. Is it possible to remove this from the observer using Python?"</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f5ec969ecae010c3a43e06791e50db22af32db63.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/90b11baefbf196b5921c5a72e0b475dd8e51353d.jpeg">
  </div><p></p>

---

## Post #2 by @pieper (2024-08-23 13:01 UTC)

<p>What if you change this mode:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ce5f20b04664c98a0412d27cbf59b6109d442ac9.png" alt="image" data-base62-sha1="trEatOPkGxZ0PLnKmJB1gzPFKkN" width="573" height="159"></p>
<p>If that works you should also be able to find how to do in python pretty easily.</p>

---
