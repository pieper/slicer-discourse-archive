---
topic_id: 10189
title: "Is There An Easy Method To Calculate The Cobb Angle Using A"
date: 2020-02-10
url: https://discourse.slicer.org/t/10189
---

# Is there an easy method to calculate the Cobb Angle using a 3D Slicer module?

**Topic ID**: 10189
**Date**: 2020-02-10
**URL**: https://discourse.slicer.org/t/is-there-an-easy-method-to-calculate-the-cobb-angle-using-a-3d-slicer-module/10189

---

## Post #1 by @stevenagl12 (2020-02-10 17:08 UTC)

<p>I have CT scans that contain the spine and am trying for an easy way to get the Cobb Angle using them.</p>

---

## Post #2 by @lassoan (2020-02-10 18:18 UTC)

<p>Cobb angle is measured on 2D x-rays, which is essentially AP projection of CT image. You can create the projection image using <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Thick_slab_reconstruction_and_maximum.2Fminimum_intensity_volume_projections">this script</a> and then use angle markups angle widget (in recent Slicer Preview Release). We don’t have 4-point angle measurement yet (we’ll probably add it at some point, it would be very easy), so if angle widget is too inconvenient then you can draw 2 lines and compute the angle using a short Python script.</p>
<p>You might also find Scoliosis extension useful, which measures vertebral angles from 3D points defined directly on a volume-rendered CT.</p>

---
