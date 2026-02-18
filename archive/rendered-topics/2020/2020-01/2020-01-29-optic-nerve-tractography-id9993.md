# Optic Nerve tractography

**Topic ID**: 9993
**Date**: 2020-01-29
**URL**: https://discourse.slicer.org/t/optic-nerve-tractography/9993

---

## Post #1 by @HariES (2020-01-29 10:33 UTC)

<p>Dear Sir,</p>
<p>Optic nerve is mixing with noise of image in the mask. So tensor is not estimated in dti estimation for the optic nerve. How to do optic nerve tracts after installing fiducial in optic nerve.</p>

---

## Post #2 by @pieper (2020-01-29 21:55 UTC)

<p><a class="mention" href="/u/zhangfanmark">@zhangfanmark</a> may have other suggestions, but I would say that it’s probably hard to track the optic nerve, particularly if your image is noisy.</p>

---

## Post #3 by @zhangfanmark (2020-01-29 23:37 UTC)

<p>Other than potential issue from image quality, DTI tractography can be insufficient to track through the crossing fiber region. You can try our UKF tractography using a two tensor model, which should give better tracking performance of the optic nerve.</p>
<p>You can find UKF tutorial here: <a href="http://dmri.slicer.org/docs/" rel="nofollow noopener">http://dmri.slicer.org/docs/</a></p>
<p>Regards,<br>
Fan</p>

---
