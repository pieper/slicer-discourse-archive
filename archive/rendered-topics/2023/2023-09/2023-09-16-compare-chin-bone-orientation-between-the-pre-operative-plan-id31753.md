# Compare chin bone orientation between the pre-operative planning and post operative result

**Topic ID**: 31753
**Date**: 2023-09-16
**URL**: https://discourse.slicer.org/t/compare-chin-bone-orientation-between-the-pre-operative-planning-and-post-operative-result/31753

---

## Post #1 by @wael_telha (2023-09-16 19:01 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="14712">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"><a href="https://discourse.slicer.org/t/yaw-pitch-roll-measurements-with-q3dc/14712/3">Yaw, pitch, roll measurements with Q3DC</a></div>
<blockquote>
<p>f at least two of the angles have limited range (one is not more than 70-80 degrees, and one is not more than 10-15 degrees). For example, it works well for ships, because there is a practical limit on how much a ship can rotate around two of its axes.</p>
<p>For general applications, 3D rotation should not be described using roll/pitch/yaw angles, as it is</p>
</blockquote>
</aside>
<p>How can i measure the yaw, pitch and roll for bone advancement of the chin to compare between the pre-operative planning and post-operative result ( material provided is in form of STL</p>

---

## Post #2 by @lassoan (2023-09-18 02:18 UTC)

<p>You can register the bones in the two positions (using “fiducial registration”, optionally followed by surface-based automatic “Model registration”) and then you can get information about the rotation component of the transform using <a href="https://github.com/PerkLab/SlicerSandbox#characterize-transform-matrix">“Characterize transform matrix” module</a> (in Sandbox extension).</p>

---

## Post #3 by @wael_telha (2023-10-03 15:39 UTC)

<p>I am not able to find the Slicersandbox extension . how can I download it</p>

---

## Post #4 by @mikebind (2023-10-04 19:13 UTC)

<p>You can install the Slicer Sandbox extension from within Slicer using the Extensions Manager:<br>
<a href="https://slicer.readthedocs.io/en/latest/user_guide/extensions_manager.html" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/user_guide/extensions_manager.html</a></p>

---
