# 3D reconstruction fluoroscopic cholangiogram images

**Topic ID**: 34905
**Date**: 2024-03-15
**URL**: https://discourse.slicer.org/t/3d-reconstruction-fluoroscopic-cholangiogram-images/34905

---

## Post #1 by @Marc_eL (2024-03-15 06:27 UTC)

<p>Dear experts,</p>
<p>For my project, I aim to perform a 3D reconstruction of liver ducts obtained through fluoroscopic images during retrograde endoscopic cholangiography. In most cases, both apiko-posterior and lateral images are available. What would be the best method to perform a 3D reconstruction with sufficient quality, for example, to measure duct changes in a volume range of 1-3 mm? I have read some previous posts on this topic, where the RTK Tool was recommended for reconstructing a 3D volume. I managed to import the tool via the Python console, but I don’t know how to apply it. Could someone advise me on the “how-to” step by step, or refer me to literature where I could learn more about it? Is there other more simple solution? I would appreciate any help.</p>
<p>Best regards</p>

---

## Post #2 by @lassoan (2024-03-17 02:08 UTC)

<p>You cannot get a full 3D volumetric reconstruction of a tubular structures from just two projections. However, you can approximate the centerline and some diameter changes. These approximations are not done commonly, so most likely you need to find some promising methods in the literature and implement them.</p>
<p>RTK is mostly used for reconstructing a 3D volume from projection images acquired and hundreds of different angles, so probably it cannot do anything with just two projections - but you can ask its developers to confirm.</p>

---
