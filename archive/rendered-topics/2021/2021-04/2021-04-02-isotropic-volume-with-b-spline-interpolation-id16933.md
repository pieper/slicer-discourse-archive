# Isotropic Volume with B-Spline Interpolation

**Topic ID**: 16933
**Date**: 2021-04-02
**URL**: https://discourse.slicer.org/t/isotropic-volume-with-b-spline-interpolation/16933

---

## Post #1 by @Fluvio_Lobo (2021-04-02 20:27 UTC)

<p>Hello,</p>
<p>I am trying to understand what is exactly happening when I use the <strong>crop volume</strong> function with the <strong>isotropic spacing</strong> and <strong>B-spline interpolation</strong> flags on. This is mostly for a discussion section on a publication and my own sanity <img src="https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=9" title=":sweat_smile:" class="emoji" alt=":sweat_smile:"></p>
<p>The <strong>isotropic spacing</strong> is ensuring that the shape of the voxels of the new volume are almost identical in size (say +/- 5-10%). And, in the directions in which the difference is greater than a set limit, say  this 5-10%, a <strong>B-Spline</strong> interpolation is used to approximate the voxels in between???</p>
<p>Is this correct? <img src="https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=9" title=":sweat_smile:" class="emoji" alt=":sweat_smile:"> close?</p>

---

## Post #2 by @lassoan (2021-04-02 20:30 UTC)

<p>If you set “isotropic spacing” then the voxel spacing of the output volume will be exactly the same along all 3 axes. B-spline interpolation is used to get voxel values of the new volume.</p>

---
