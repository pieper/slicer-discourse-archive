# The Problem of Communication with Unity using openIGTLink

**Topic ID**: 30345
**Date**: 2023-07-02
**URL**: https://discourse.slicer.org/t/the-problem-of-communication-with-unity-using-openigtlink/30345

---

## Post #1 by @jay1987 (2023-07-02 06:23 UTC)

<p>i want to using Slicer to communication Unity with OpenIGTLink<br>
I have read the code of ARInSlicer and learned how to transform TransformNode and 2DTexture from Slicer to Unity ,is there any way to Transform PolyData from Slicer to Unity?</p>

---

## Post #2 by @lassoan (2023-07-02 11:34 UTC)

<p>Slicer can already send polydata via OpenIGTLink, so all you need to do is to implement receiving of this message type in Unity and building of a mesh object from the received information.</p>
<p>After you implement this (maybe by extending <a href="https://github.com/BSEL-UC3M/HoloLens2and3DSlicer-PedicleScrewPlacementPlanning" class="inline-onebox">GitHub - BSEL-UC3M/HoloLens2and3DSlicer-PedicleScrewPlacementPlanning: GitHub repository for the IJCARS paper: "Real-Time open-source integration between Microsoft HoloLens 2 and 3D Slicer"</a>), please share it with the community, as probably other groups would find it useful, too.</p>

---
