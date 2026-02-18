# Resampling using linear Transform

**Topic ID**: 40087
**Date**: 2024-11-09
**URL**: https://discourse.slicer.org/t/resampling-using-linear-transform/40087

---

## Post #1 by @racctor (2024-11-09 04:24 UTC)

<p>Hello,</p>
<p>I tried a few variations now, but nothing seems to work. I have multiple series loaded. One of those is my Series “10”. Loading it, I see that the skull is not properly rotated. The right side is more forward and to high.</p>
<p>I created a new linear Transform in the Data Module and linked it to Series 10. Then i went to the Transforms Module and selected the new LinearTransform. There I tried two variations:</p>
<ol>
<li>Rotation PA 0.3°, Harden Transform, Rotation IS -0,7°, Harden Transform</li>
<li>Rotation PA 0.3°, Rotation IS -0,7° (the PA rotation automatically showed 0° after entering a value into IS rotation), Harden Transform</li>
</ol>
<p>In both cases I went to the Resample Scalar Volume afterwards and chose my Input Volume (“Series 10”) while creating a new Output volume. Interpolation lanczos was used. Once the Resampling is done, I get the new volume.</p>
<p>My problem is that the new volume is again orientated like the original, so that e.g. the right side is still more forward.</p>
<p>What am I doing wrong?</p>

---

## Post #2 by @lassoan (2024-11-09 15:49 UTC)

<p>There are several image resampling modules in Slicer. If you want to apply a transform during resampling then you need to choose a module that allows you to select a transform (such as <code>Resample scalar/vector/DWI volume</code>) or a region of interest (such as <code>Crop volume</code>).</p>

---
