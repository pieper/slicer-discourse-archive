---
topic_id: 5876
title: "Error User Can Only Specify One Output Transform Type"
date: 2019-02-21
url: https://discourse.slicer.org/t/5876
---

# Error: user can only specify one output transform type

**Topic ID**: 5876
**Date**: 2019-02-21
**URL**: https://discourse.slicer.org/t/error-user-can-only-specify-one-output-transform-type/5876

---

## Post #1 by @coolsocks (2019-02-21 20:40 UTC)

<p>Hi,</p>
<p>I am using Slicer 4.10.1.<br>
Whenever I try to run Brainfit General registration for Rigid registration, I always get this error:</p>
<p>Error:  user can only specify one output transform type</p>
<p>However, I only selected Slicer Linear Transform as the output Type. Why does this occur?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/5496bcac6f94fc01d7f1e2bbb4ca39869ce78093.png" data-download-href="/uploads/short-url/c4j3ISVAnihmB5AZS9AZtb41enN.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/5496bcac6f94fc01d7f1e2bbb4ca39869ce78093.png" alt="image" data-base62-sha1="c4j3ISVAnihmB5AZS9AZtb41enN" width="690" height="123" data-dominant-color="F0F0F0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1116×199 6.92 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The program will only work if I set an Output Image Volume but No Linear/BSpline Transform.</p>

---

## Post #2 by @coolsocks (2019-02-21 20:56 UTC)

<p>Solved the issue. It was because I never clicked on “reset to default” after I performed a registration beforehand.</p>

---
