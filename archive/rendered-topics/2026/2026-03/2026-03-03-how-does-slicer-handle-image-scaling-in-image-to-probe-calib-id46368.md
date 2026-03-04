---
topic_id: 46368
title: "How Does Slicer Handle Image Scaling In Image To Probe Calib"
date: 2026-03-03
url: https://discourse.slicer.org/t/46368
---

# How Does Slicer Handle Image Scaling in Image-to-probe Calibration?

**Topic ID**: 46368
**Date**: 2026-03-03
**URL**: https://discourse.slicer.org/t/how-does-slicer-handle-image-scaling-in-image-to-probe-calibration/46368

---

## Post #1 by @daandevlieger2-alt (2026-03-03 11:01 UTC)

<p>Hi everyone,</p>
<p>We are working with 3D Slicer (version 5.8.1), an OptiTrack V120:Trio, and an Telemed ArtUs for 3D freehand ultrasound acquisition.</p>
<p>We have repeatedly attempted probe calibration using a stylus-based approach as described in this repository:<br>
<a href="https://github.com/AurelieSar/3Dultrasound" rel="noopener nofollow ugc">https://github.com/AurelieSar/3Dultrasound</a></p>
<p>However, we have not been able to obtain a stable calibration file that supports multiple (rotated) sweeps. As an alternative, we are considering a CAD-based calibration approach and generating the probe rotation/translation matrix manually.</p>
<p>From our understanding, the probe-to-image transform matrix contains a scaling component (mm/pixel), which can be estimated by computing the norm of each column of the 3×3 submatrix. When we inspect scaling factors derived from calibration matrices generated directly in Slicer, we observe values in the range of approximately 0.11–0.15 mm/pixel.</p>
<p>However, when calculating the mm/pixel ratio directly in EchoWave (with our current acquisition settings), we obtain a value of 0.093 mm/pixel.</p>
<p>Our questions are:</p>
<ol>
<li>
<p>How can we determine with certainty what the correct scaling factor should be?</p>
</li>
<li>
<p>How does Slicer internally handle pixel spacing and scaling during ultrasound calibration?</p>
</li>
<li>
<p>Is the scaling factor expected to come purely from the ultrasound image spacing metadata, or can it be modified implicitly during the calibration optimization process?</p>
</li>
</ol>
<p>Any clarification on how Slicer manages image spacing and scaling in the probe-to-image transform would be greatly appreciated.</p>
<p>Thank you in advance for your help.</p>

---
