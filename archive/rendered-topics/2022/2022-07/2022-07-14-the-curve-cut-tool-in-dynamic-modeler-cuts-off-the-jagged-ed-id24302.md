---
topic_id: 24302
title: "The Curve Cut Tool In Dynamic Modeler Cuts Off The Jagged Ed"
date: 2022-07-14
url: https://discourse.slicer.org/t/24302
---

# The curve cut tool in dynamic modeler cuts off the jagged edges of the model

**Topic ID**: 24302
**Date**: 2022-07-14
**URL**: https://discourse.slicer.org/t/the-curve-cut-tool-in-dynamic-modeler-cuts-off-the-jagged-edges-of-the-model/24302

---

## Post #1 by @janus_zhu (2022-07-14 05:14 UTC)

<p>1、The first step is to place curves on the surface of the model<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a049dfcda74ccbb0e7b5c6d24606c9a73209e09.png" alt="curve cut model" data-base62-sha1="jGXMye6FvZoGz0xGyeJC1rZIO81" width="555" height="407"><br>
2、Use the cueve cut tool in dynamic model to cut<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e13785fbe5112907e3a0cbf2f1df7094e184d96.png" alt="curve cut model 1" data-base62-sha1="b8GXmmgNj9mJ2fnORCD1qlvbEgu" width="384" height="266"><br>
3、Result : the edges of the model are jagged<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/dbbc7ccf1392c196ac1204db77182230d7933dda.png" data-download-href="/uploads/short-url/vlSoIDx0xVgF091R1vVsizr9LaG.png?dl=1" title="curve cut model 2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/dbbc7ccf1392c196ac1204db77182230d7933dda_2_628x500.png" alt="curve cut model 2" data-base62-sha1="vlSoIDx0xVgF091R1vVsizr9LaG" width="628" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/dbbc7ccf1392c196ac1204db77182230d7933dda_2_628x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/dbbc7ccf1392c196ac1204db77182230d7933dda.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/dbbc7ccf1392c196ac1204db77182230d7933dda.png 2x" data-dominant-color="808F9C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">curve cut model 2</span><span class="informations">700×557 121 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2022-07-14 16:52 UTC)

<p>Increase the number of points on the curve using resampling (and make sure you enable the constrain to surface). Here is a cut with three point CC originally (green), and another one using the resampling on that curve to increase the number of points to 53. They are cut from the same sphere.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/6273481e890ee319f0cbf22d44fb975de4e26385.png" alt="image" data-base62-sha1="e2VMuakQ6QmpG1xCbnZoO1x1mQJ" width="674" height="448"></p>

---
