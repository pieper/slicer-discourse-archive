---
topic_id: 15796
title: "Comparing Dose Accumulation From Tps Varian Eclipse And 3D S"
date: 2021-02-02
url: https://discourse.slicer.org/t/15796
---

# Comparing Dose accumulation from TPS Varian Eclipse and 3D Slicer

**Topic ID**: 15796
**Date**: 2021-02-02
**URL**: https://discourse.slicer.org/t/comparing-dose-accumulation-from-tps-varian-eclipse-and-3d-slicer/15796

---

## Post #1 by @jannah_fj (2021-02-02 13:58 UTC)

<p>Hello there, I tried to do the accumulation of doses with 3D Slicer, then I compared with the accumulated doses from the TPS simulation results of the varian eclipse manually (neither use the dose comparison nor the DVH comparison from 3D slicer). Both of them show almost the same value but not exactly the same, for example:<br>
The Body, from TPS varian eclipse show the volume 24897,1 cm3 but from slicer i got 24898,5 cm3. The mean dose of the body from TPS varian eclipse show 3,67 Gy but from slicer i got 3,64018 Gy. The maximum dose from TPS varian eclipse show 52,93 Gy but from slicer i got 52,7287 Gy. And so on.</p>
<p>I wonder if this due to the different algorithms used by 3D Slicer or anything else?  I tried this for at least 6 data but the results are always almost the same and never exactly the same.</p>

---

## Post #2 by @lassoan (2021-02-05 04:31 UTC)

<p>These differences are expected. Radiation therapy applications use RT structure set DICOM information object for specifying regions of interest by a set of 2D planar contours. The DICOM standard does not specify how a 3D region can be reconstructed from these 2D contours, therefore each software implementation provides slightly different results.</p>
<p>See some more information in these papers:</p>
<ul>
<li><a href="http://perk.cs.queensu.ca/sites/perk.cs.queensu.ca/files/Pinter2012_0.pdf">http://perk.cs.queensu.ca/sites/perk.cs.queensu.ca/files/Pinter2012_0.pdf</a></li>
<li><a href="http://perk.cs.queensu.ca/sites/perkd7.cs.queensu.ca/files/Sunderland2015-manuscript.pdf">http://perk.cs.queensu.ca/sites/perkd7.cs.queensu.ca/files/Sunderland2015-manuscript.pdf</a></li>
</ul>

---
