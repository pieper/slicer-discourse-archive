---
topic_id: 14154
title: "Elastix Registration Incorporating Contour Information"
date: 2020-10-20
url: https://discourse.slicer.org/t/14154
---

# Elastix registration incorporating contour information

**Topic ID**: 14154
**Date**: 2020-10-20
**URL**: https://discourse.slicer.org/t/elastix-registration-incorporating-contour-information/14154

---

## Post #1 by @labixin (2020-10-20 08:20 UTC)

<p>Hi all,</p>
<p>I want to incorporate contour information with intensity-based registration in Elastix (“MultiMetricMultiResolutionRegistration”). I have one corresponding segments (breast gland) both in pre-operative and post-operative CT images. And my goal is to register two CT data sets with MI, while simultaneously registering the corresponding segments (binary images) with the kappa statistic (mentioned as <a href="https://elastix.lumc.nl/doxygen/parameter.html" rel="noopener nofollow ugc">Metric “AdvancedKappaStatistic”</a> in Elastix, and the explanation is attached below). However, there is little information on how to implement this.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b7ecb2832a340043426032d79906d99d28eab015.jpeg" data-download-href="/uploads/short-url/qf4uVbIhKW1Ked1g3gx0iP1RnG5.jpeg?dl=1" title="01" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b7ecb2832a340043426032d79906d99d28eab015_2_690x124.jpeg" alt="01" data-base62-sha1="qf4uVbIhKW1Ked1g3gx0iP1RnG5" width="690" height="124" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b7ecb2832a340043426032d79906d99d28eab015_2_690x124.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b7ecb2832a340043426032d79906d99d28eab015.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b7ecb2832a340043426032d79906d99d28eab015.jpeg 2x" data-dominant-color="F4F4F4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">01</span><span class="informations">740×133 14.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Could you give some suggestions? Or is there any other way to better use the additional contour information. Thanks a lot!</p>
<p>Sincerely,</p>
<p>Crayon</p>

---
