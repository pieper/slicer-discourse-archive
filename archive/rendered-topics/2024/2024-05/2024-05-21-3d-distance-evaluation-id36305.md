---
topic_id: 36305
title: "3D Distance Evaluation"
date: 2024-05-21
url: https://discourse.slicer.org/t/36305
---

# 3D Distance evaluation

**Topic ID**: 36305
**Date**: 2024-05-21
**URL**: https://discourse.slicer.org/t/3d-distance-evaluation/36305

---

## Post #1 by @Mouadh_Ben_Nasr (2024-05-21 23:55 UTC)

<p>Hello everyone,<br>
I am still working on evaluating distance between tumor and normal liver after intraarterial treatment.<br>
I managed to register the pre and post procedural imaging multimodalities.<br>
Then, I evaluated Hausdroff distance and Model to Model distance.<br>
Since we got subcapsular tumors, I used Boolean operation to substract tumor from liver and treated zone, for measuring distance between Tumor and Liver.</p>
<p>For calculating HD , I used the Tumor and the Treated volumes, and for the MtMD , tumor and normal liver.</p>
<p>Results obtained from distance are quite different  (as HD seeks for the maximum of minimums and MtMD averages all distances).</p>
<p>Since the model distance calculates the closest point between models , I assume that would correspond to the minimum distance. Using signed distances provides negative values even when substracting tumor volume from liver volume. However, I used the signed distance color map for visual assessment of distance disagreement. For distance values, I used the absolute distance calculation.<br>
I would to ask<br>
1- whether the method used for distance evaluation is correct or not?<br>
2- how to correctly interpret HD and MtMD in this case?</p>
<p>Thank you for your help<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e782ab1219aa5287c207c85064a5b4df322632dc.jpeg" data-download-href="/uploads/short-url/x22fzdx6VBPQRMXPd2Ejp37l8LO.jpeg?dl=1" title="IMG_1261" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e782ab1219aa5287c207c85064a5b4df322632dc_2_690x151.jpeg" alt="IMG_1261" data-base62-sha1="x22fzdx6VBPQRMXPd2Ejp37l8LO" width="690" height="151" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e782ab1219aa5287c207c85064a5b4df322632dc_2_690x151.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e782ab1219aa5287c207c85064a5b4df322632dc_2_1035x226.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e782ab1219aa5287c207c85064a5b4df322632dc.jpeg 2x" data-dominant-color="636E7B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_1261</span><span class="informations">1122×247 39.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
