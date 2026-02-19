---
topic_id: 4963
title: "Re Sampling Vs Harden Transform For A Dose Volume"
date: 2018-12-04
url: https://discourse.slicer.org/t/4963
---

# Re-sampling vs Harden Transform for a dose volume

**Topic ID**: 4963
**Date**: 2018-12-04
**URL**: https://discourse.slicer.org/t/re-sampling-vs-harden-transform-for-a-dose-volume/4963

---

## Post #1 by @Lowey (2018-12-04 20:35 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.8.1 Stable</p>
<p>Hi there,</p>
<p>I have a general question about how Slicer handles and applies deformable registration files that are exported from TPS software with respect to grids.</p>
<p>I would like to apply a deformation vector field (DVF) to a dose volume. My question is,</p>
<p>If I apply the DVF to a dose volume within Slicer’s Transform module (i.e., Apply Transform → Harden Transform) what happens to the grid spacing of the warped dose volume?<br>
Is it still uniform (through some internal re-sampling?) or is the grid of the dose volume ‘smeared’ out in a warped non-uniform fashion?</p>
<p>For reference, here is the transform information of my Deformable Registration Grid<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf76a6f0de32835851e73dab45734a34701c0aa9.png" alt="image" data-base62-sha1="rjLphIxc1wEeNCcUxwzEzWs7RMJ" width="433" height="238"></p>
<p>As an extra question 1)<br>
What is the difference between using the Transforms module or a Re-sampling module when applying a DVF to a dose volume?</p>
<p>Extra question 2)<br>
What is the difference between applying a ‘Displacement field’ transform and a ‘b-Spline’ transform to a dose volume?</p>
<p>Many thanks!</p>

---

## Post #2 by @lassoan (2018-12-04 23:49 UTC)

<p>Transforms module’s harden function only resamples the volume if necessary (if a Non-linear transform is applied). If resampling is needed then the resulting grid has the same spacing and orientation as the original grid and linear interpolation is used.</p>
<p>If you use resampling modules then you have complete control over the output grid and interpolation method.</p>

---

## Post #3 by @Lowey (2018-12-04 23:52 UTC)

<p>Thank you Andras, very helpful</p>

---
