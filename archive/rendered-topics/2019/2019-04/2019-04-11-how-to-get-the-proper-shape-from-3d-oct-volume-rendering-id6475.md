# How to get the proper shape from 3d OCT volume rendering

**Topic ID**: 6475
**Date**: 2019-04-11
**URL**: https://discourse.slicer.org/t/how-to-get-the-proper-shape-from-3d-oct-volume-rendering/6475

---

## Post #1 by @sreyankar (2019-04-11 20:53 UTC)

<p>Operating system: Mac OS X<br>
Slicer version: 4.10.1<br>
Expected behavior: Trying to interactively build a 3d model from a stack of circular OCT images from an airway. The boundaries are not very well defined.<br>
Actual behavior: In the 3d volume it shows up as a volumetric cylinder, how to make it in the shape I want, i.e. an actual airway?</p>

---

## Post #2 by @lassoan (2022-04-04 15:17 UTC)

<p>You can reconstruct Cartesian volume from circular OCT images (see discussion <a href="https://discourse.slicer.org/t/3d-reconstruction-of-radial-oct-slices/20734/5">here</a>) and then you can use Segment Editor to create a 3D model.</p>

---
