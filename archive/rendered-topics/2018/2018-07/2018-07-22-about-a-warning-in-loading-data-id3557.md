---
topic_id: 3557
title: "About A Warning In Loading Data"
date: 2018-07-22
url: https://discourse.slicer.org/t/3557
---

# About a warning in loading data

**Topic ID**: 3557
**Date**: 2018-07-22
**URL**: https://discourse.slicer.org/t/about-a-warning-in-loading-data/3557

---

## Post #1 by @RitchieAlhpa (2018-07-22 20:16 UTC)

<p>I’d like to ask u a question about this software when  loading data and saving report.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/6971f7b65f68a4a87257b78cf68e4cfab400302e.png" data-download-href="/uploads/short-url/f2Oj9s712k9BqhNJdWFJWUF5c2q.png?dl=1" title="WechatIMG1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/6971f7b65f68a4a87257b78cf68e4cfab400302e_2_690x48.png" alt="WechatIMG1" data-base62-sha1="f2Oj9s712k9BqhNJdWFJWUF5c2q" width="690" height="48" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/6971f7b65f68a4a87257b78cf68e4cfab400302e_2_690x48.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/6971f7b65f68a4a87257b78cf68e4cfab400302e_2_1035x72.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/6971f7b65f68a4a87257b78cf68e4cfab400302e_2_1380x96.png 2x" data-dominant-color="FAE9E6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">WechatIMG1</span><span class="informations">2806×198 61.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I don’t understand why the software always output the warning?<br>
Is the warning matter?<br>
Can I  ignore it?</p>

---

## Post #3 by @lassoan (2018-07-22 20:26 UTC)

<p>This error means that loaded image series may be incorrectly scaled. If you load a complete study or patient and some of the series throw this error then you may ignore it (you may have dose report, screenshots, etc. among the series, which don’t define position, scaling, and orientation). However, if you load a single 3D series and you see such error then there is a good chance that the volume will not appear correctly.</p>

---
