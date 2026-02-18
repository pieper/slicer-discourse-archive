# fMRI work in 3D Slicer 4.11

**Topic ID**: 17525
**Date**: 2021-05-08
**URL**: https://discourse.slicer.org/t/fmri-work-in-3d-slicer-4-11/17525

---

## Post #1 by @Andrii_Bachun (2021-05-08 14:30 UTC)

<p>How can I analyze FMRI in 3d sliser 4.11?<br>
FMRI engine was super. maybe someone have older sliser with fmri engine?</p>

---

## Post #2 by @pieper (2021-05-08 15:03 UTC)

<p>We don’t have an integrated fMRI tool in Slicer right now.  I agree, the fRMIEngine was a really nice implementation (here are <a href="https://www.slicer.org/w/img_auth.php/3/31/SlicerTraining5_fMRI.ppt">some slides</a> for anyone interested.  We stopped developing it because there were so many other options (fsl, afni, etc) and also we ran into problems working with large acquisitions using the 32bit CPUs common at that time.</p>
<p>Many of the core C++ classes could probably be ported but the interface and probably much of the glue logic would need to be redone.</p>
<p>Currently people do their fMRI in one of the other packages and load the statistical results into Slicer for visualization with other acquisitions.</p>

---
