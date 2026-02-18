# What interpolation does Slicer use for visualisation

**Topic ID**: 35382
**Date**: 2024-04-09
**URL**: https://discourse.slicer.org/t/what-interpolation-does-slicer-use-for-visualisation/35382

---

## Post #1 by @koeglfryderyk (2024-04-09 08:16 UTC)

<p>What kind of interpolation does Slicer use for visualization of slices?</p>
<p>E.g. I have a linear transformation and apply it to a volume - what interpolation method is used for the displayed voxels in the RGY views?</p>

---

## Post #2 by @rfenioux (2024-04-09 15:36 UTC)

<p>By default, the views apply a linear interpolation.<br>
It can be disabled using this button (a nearest neighbor interpolation is then used), but this can result in aliasing artifacts when rotating the slices or the volume :</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0bb2d1a8f025c0202782abb84f9e582ed177a3c6.png" alt="Screenshot 2024-04-09 173229" data-base62-sha1="1FumWAK0Lks3Vty82DbZR4AEukS" width="250" height="138"></p>

---

## Post #3 by @lassoan (2024-04-10 04:01 UTC)

<p>You can find some more details on interpolation in slice views in <a href="https://discourse.slicer.org/t/volume-display-interpolate-turned-off-by-default-in-newest-stable/13918/17">this topic</a>. There is also a code snippet to enable higher-order interpolation if that is of interest. Interpolation should not be disabled (you would then see the signal sampling points, not the signal itself).</p>

---
