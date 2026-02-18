# Rigid landmark registration for models

**Topic ID**: 23075
**Date**: 2022-04-21
**URL**: https://discourse.slicer.org/t/rigid-landmark-registration-for-models/23075

---

## Post #1 by @stevenagl12 (2022-04-21 16:44 UTC)

<p>I forget, is there a module for using landmarks to rigidly align models and images together in 3D space? I am hoping to be able to do principal component analysis from the SLicerMorph module while retaining the size dimension as a feature for GMM and shape analysis…? In addition, if we can register the shapes rigidly, we can take those registered shapes into programs like scalismo and have one less thing to do in that programming environment.</p>

---

## Post #2 by @lassoan (2022-04-23 05:04 UTC)

<p>Probably the most convenient module for <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html#semi-automatic-registration">landmark-based image-to-model registration</a> is <code>Fiducial registration wizard</code> module in SlicerIGT extension.</p>

---
