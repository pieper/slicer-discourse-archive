# Smoothing factor always reset to 0.5 on reload

**Topic ID**: 17640
**Date**: 2021-05-16
**URL**: https://discourse.slicer.org/t/smoothing-factor-always-reset-to-0-5-on-reload/17640

---

## Post #1 by @hherhold (2021-05-16 14:08 UTC)

<p>Slicer May 9 nightly, MacOS 10.15.7.</p>
<ol>
<li>Load in a scene, any scene, with some segments.</li>
<li>Go to segment editor</li>
<li>turn on Show 3D</li>
<li>Change smoothing factor to 0.1</li>
<li>Save everything</li>
<li>Quit slicer</li>
<li>Restart slicer</li>
<li>Reload scene</li>
<li>Note that smoothing factor is set to 0.5. The segmentation, however, appears to still be the result of the 0.1 smoothing.</li>
</ol>
<p>Expected - smoothing factor value should be preserved across saves. Right now the 3D representation and the value reported do not match after a reload.</p>
<p>Thanks!</p>
<p>-Hollister</p>

---

## Post #2 by @lassoan (2021-05-17 00:48 UTC)

<p>Good catch. The correct values were used in the loaded segmentation but indeed the slider value was not initialized to show that. I’ve fixed it now, it will be available in tomorrow’s Slicer Preview Release.</p>

---

## Post #3 by @hherhold (2021-05-17 01:17 UTC)

<p>Awesome, thanks!</p>
<p>-Hollister</p>

---
