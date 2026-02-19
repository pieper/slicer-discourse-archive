---
topic_id: 41553
title: "Detect Closed Polydata Line"
date: 2025-02-07
url: https://discourse.slicer.org/t/41553
---

# Detect closed polydata line

**Topic ID**: 41553
**Date**: 2025-02-07
**URL**: https://discourse.slicer.org/t/detect-closed-polydata-line/41553

---

## Post #1 by @darabi (2025-02-07 13:39 UTC)

<p>Hello,</p>
<p>I have a model which has a rim which is detectable with vtkFeatureEdges by using SetFeatureEdges(True) and SetFeatureAngle to a value between 35 and 45.</p>
<p>Decreasing the feature angle incrementally and selecting the largest segment with SurfaceToolbox.extractLargestConnectedComponent leads to a more and more complete recognition of the rim, until the rim is visually closed.</p>
<p>surface:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/8016a0c4b8dec6be8c6fcee0ab42157f1058e452.png" data-download-href="/uploads/short-url/ih7AYTHwkbSzuRkTk4IQ7gcs8r8.png?dl=1" title="surface" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/8016a0c4b8dec6be8c6fcee0ab42157f1058e452.png" alt="surface" data-base62-sha1="ih7AYTHwkbSzuRkTk4IQ7gcs8r8" width="623" height="371"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">surface</span><span class="informations">623×371 44.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>feature angle 48°:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a31131d25b6a07220de6bf611328b72690af5dfa.png" data-download-href="/uploads/short-url/ngyFlRzxy0G02f12B8mmCjyiLay.png?dl=1" title="rim-48-deg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a31131d25b6a07220de6bf611328b72690af5dfa.png" alt="rim-48-deg" data-base62-sha1="ngyFlRzxy0G02f12B8mmCjyiLay" width="623" height="371"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">rim-48-deg</span><span class="informations">623×371 4.65 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>feature angle 45°:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e1b4b78db1a368af2c2a414044d79e37cd363123.png" data-download-href="/uploads/short-url/wcGC91nQt6XnyDrmEll2WvBGKs3.png?dl=1" title="rim-45-deg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e1b4b78db1a368af2c2a414044d79e37cd363123.png" alt="rim-45-deg" data-base62-sha1="wcGC91nQt6XnyDrmEll2WvBGKs3" width="623" height="371"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">rim-45-deg</span><span class="informations">623×371 5.36 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>feature angle 39°:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/eb425c15c722b0961c495f677e7e52d5dbc2b667.png" data-download-href="/uploads/short-url/xzcnAV8pCDjLp4RD4Tu0Xu8LvVl.png?dl=1" title="rim-39-deg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/eb425c15c722b0961c495f677e7e52d5dbc2b667.png" alt="rim-39-deg" data-base62-sha1="xzcnAV8pCDjLp4RD4Tu0Xu8LvVl" width="623" height="371"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">rim-39-deg</span><span class="informations">623×371 5.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The resulting polydata consists of cells which are all of type vtkLine with two points.</p>
<p>Q1: What is the most straightforward way of identifying, if the line is closed?</p>
<p>Q2: Is there is a better strategy for extracting the rim?</p>
<p>Thank you</p>
<p>Kambiz</p>

---

## Post #2 by @darabi (2025-02-08 14:28 UTC)

<p>Forgot to mention: my ultimate goal is to cut the mesh in two parts at the position of the rim. So any hints on how to achieve this are also highly appreciated.</p>

---
