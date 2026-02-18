# Yaw, pitch, roll measurements with Q3DC

**Topic ID**: 14712
**Date**: 2020-11-20
**URL**: https://discourse.slicer.org/t/yaw-pitch-roll-measurements-with-q3dc/14712

---

## Post #1 by @mccarthyvetsurg (2020-11-20 16:55 UTC)

<p>Trying to figure out which directions roll, yaw, and pitch are correlating to using Q3DC.</p>
<p>I know if I google yaw, pitch, roll that yaw correlates with Z, pitch correlates with y and roll with x.  Can someone please translate these to medical terminology used anterior/posterior, superior/inferior, right and left directions in the segmentation view?</p>
<p>I am not sure if roll is inferior, posterior etc.  Thank you.</p>

---

## Post #2 by @pll_llq (2020-11-22 19:12 UTC)

<p>Roll will be rotation around Anterior-Posterior axis<br>
Pitch will be the rotation around Right-Left axis<br>
Yaw will be the rotation around Superior-Inferior axis</p>
<p>Here’s a nice picture from the Wikipedia that explains directional references<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7fa648d7055e90ba635749c52118ac66fad503c3.jpeg" data-download-href="/uploads/short-url/ideTUb6KajpNpk0fdLFUwqkKVGz.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7fa648d7055e90ba635749c52118ac66fad503c3_2_555x500.jpeg" alt="image" data-base62-sha1="ideTUb6KajpNpk0fdLFUwqkKVGz" width="555" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7fa648d7055e90ba635749c52118ac66fad503c3_2_555x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7fa648d7055e90ba635749c52118ac66fad503c3_2_832x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7fa648d7055e90ba635749c52118ac66fad503c3_2_1110x1000.jpeg 2x" data-dominant-color="F3EBEA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1500×1350 193 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @lassoan (2020-11-22 20:31 UTC)

<p>Roll/pitch/yaw parameterization is only meaningful if at least two of the angles have limited range (one is not more than 70-80 degrees, and one is not more than 10-15 degrees). For example, it works well for ships, because there is a practical limit on how much a ship can rotate around two of its axes.</p>
<p>For general applications, 3D rotation should not be described using roll/pitch/yaw angles, as it is ambiguous (same orientation can be described by different angle combinations, therefore the conversion between RPY and orientation is not invertible; angle values are not meaningful as soon as more than one angle is more more than a few ten degrees - big numbers don’t mean big rotation, the angle do not represent rotation axis orientation, larger difference in RPY values of two orientations does not mean larger difference between the orientations; suffers from gimbal lock; and basic operations on them can be numerically unstable).</p>
<p>You can use RPY parameterization for medical applications by carefully choosing reference coordinate system, which is aligned with the anatomy so that two of the RPY angles will have limited range. These reference coordinate system is often not the patient coordinate system (RAS - right/anterior/superior) but one that is aligned to the joint and reference coordinate system axis directions may be different on the two sides of the body. So, there is no generally applicable mapping between RPY orientation in RAS coordinate systems.</p>

---
