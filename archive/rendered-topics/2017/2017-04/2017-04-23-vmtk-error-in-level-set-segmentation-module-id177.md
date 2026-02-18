# VMTK: Error in Level Set Segmentation module

**Topic ID**: 177
**Date**: 2017-04-23
**URL**: https://discourse.slicer.org/t/vmtk-error-in-level-set-segmentation-module/177

---

## Post #1 by @lassoan (2017-04-23 11:31 UTC)

<p>(question moded from slicer-users)</p>
<p>We are using Slicer 4.6.2 in Cent OS 7 and Windows 8. We have installed Vmtk Slicer Module using the 3D Slicer extension wizard.</p>
<p>We have tried with</p>
<ol>
<li>CT cardiac angiogram dataset from Slicer</li>
<li>MR angiogram of the brain. (our dataset)</li>
</ol>
<p>The vesselness enhancement module processed the CT cardiac angiogram dataset appropriately during few attempts. But the next step ( Level Set Segmentation module) forced Slicer to shut down. This happens in Cent OS and Windows.<br>
Kindly advice</p>

---

## Post #2 by @lassoan (2017-04-23 12:10 UTC)

<p>If using latest Slicer version and cropping the volume to much smaller does not solve the problem then you can use the Segment editor module to segment vasculature manually, by thresholding and other editing operations (use vesselness filtered volume as master volume).</p>

---
