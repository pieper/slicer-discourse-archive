---
topic_id: 46368
title: "How Does Slicer Handle Image Scaling in Image-to-probe Calibration?"
date: 2026-03-03
url: https://discourse.slicer.org/t/46368
last_bumped: 2026-03-05T13:09:19.219Z
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

## Post #2 by @ungi (2026-03-04 19:39 UTC)

<p>Hi, have you seen this tutorial for the SlicerIGT extension?<br>
<a href="https://1drv.ms/p/c/7230d4dec6058018/IQAYgAXG3tQwIIBygA4AAAAAAVTQnqD1wox1oBIRD7WJfiE?e=ec9ayt" rel="noopener nofollow ugc">SlicerIGT-U31_TrackedUSCal.pptx</a></p>
<p>The mm/pixel spacing will be included in the output linear transformation matrix, just make sure you set similarity (not rigid) during fiducial point registration.</p>
<p>This is a very manual method, but eliminates other sources of errors (e.g. from phantom manufacturing or automatic image processing) and works for all ultrasound shapes and sizes with the same stylus. I think this is a good method to start ultrasound tracker calibration.</p>

---

## Post #3 by @daandevlieger2-alt (2026-03-05 09:26 UTC)

<p>Hi! Thank you for your reply. So far, I have always used this calibration method, which works well for single sweeps. However, since I would like to use 3DUS for muscle imaging, I need to perform multiple sweeps. In that case, this calibration method does not seem to map the point correctly in space, which results in poor reconstructions when combining multiple sweeps. We’ve tried different styluses, different software versions of plus 2.9.0 and performed the calibration many many times but nothings seems to resolve our calibration problem.</p>
<p>For that reason, I was considering trying the CAD-based calibration (recommended by Francesco Cenni), since we have CAD models of both the probe and the probe holder. However, from your message I understand that you would not recommend this approach due to other potential sources of error. Is that correct?</p>

---

## Post #4 by @ungi (2026-03-05 13:09 UTC)

<p>If executed correctly, all calibrations methods can be accurate, in theory. I have found the stylus-based method easy to control, modify, and repeat. I personally had most success with that. I find it important to rotate the stylus and the ultrasound (independently) and recollect the calibration points in various poses. So I use about 16 calibration points rather than 3-4 to eliminate any orientation-based bias.</p>

---
