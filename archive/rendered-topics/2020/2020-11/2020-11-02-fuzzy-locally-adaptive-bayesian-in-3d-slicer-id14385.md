---
topic_id: 14385
title: "Fuzzy Locally Adaptive Bayesian In 3D Slicer"
date: 2020-11-02
url: https://discourse.slicer.org/t/14385
---

# Fuzzy Locally Adaptive Bayesian in 3D Slicer

**Topic ID**: 14385
**Date**: 2020-11-02
**URL**: https://discourse.slicer.org/t/fuzzy-locally-adaptive-bayesian-in-3d-slicer/14385

---

## Post #1 by @Nora (2020-11-02 15:22 UTC)

<p>Hi all,</p>
<p>I’ve been trying to use different segmentation methods to study the reproducibility of Radiomics in PET data.</p>
<p>I was able to do the manual and the GrowCut algorithm for segmentation. Yet, I want to try to more methods like the fuzzy locally adaptive Bayesian. Is it possible to do it on Slicer?</p>
<p>Regards,</p>
<p>Nora</p>

---

## Post #2 by @lassoan (2020-11-02 16:57 UTC)

<p>If you have any segmentation method that is implemented in any Python package, ITK, etc. then it is easy to try it in Slicer. If you find an implementation and need help with using it in Slicer then let us know.</p>
<p>If no implementation is available then it usually means that the authors were not confident enough to provide an implementation and nobody else considered the method promising enough to reimplement it from specification, or someone implemented and it did not work well enough to worth share it publicly. You can try to contact authors of papers that used the method and ask for their implementation, but (if they respond at all) then most likely they will say that they don’t have the source code anymore, or they are not allowed to share it, or they would need to find the source code or “clean it up” before they can send it to you but they don’t have time for it right now.</p>
<p>Majority of publications in medical image computing exist mainly because the first author had to graduate and the funding project required publication of the results, regardless of the developed new techniques were any good or better than other existing methods. There are of course truly good, new methods emerge as a result of various research efforts, but it is not easy to find them among all the noise, because in case of software algorithms, you would need source code and data to reproduce results, and most journals don’t require authors to provide these. More and more research communities are pushing for more open software (Slicer has been a strong proponent of this from its inception), so things are slowly getting better.</p>

---
