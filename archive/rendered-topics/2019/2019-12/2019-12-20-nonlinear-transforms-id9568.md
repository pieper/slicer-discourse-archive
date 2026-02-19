---
topic_id: 9568
title: "Nonlinear Transforms"
date: 2019-12-20
url: https://discourse.slicer.org/t/9568
---

# Nonlinear transforms

**Topic ID**: 9568
**Date**: 2019-12-20
**URL**: https://discourse.slicer.org/t/nonlinear-transforms/9568

---

## Post #1 by @rprueckl (2019-12-20 09:48 UTC)

<p>Our use-case is that we want to manually adjust a part of a brain atlas to the physiology of an individual subject. Therefore, besides rotation, translation, scaling, we want to transform the part of the atlas also nonlinearly to adjust for specialties of the subject.</p>
<p>3D Slicer seems to support what we try to achieve with the general transforms, however, we do not know how to edit a nonlinear transform. So the question is if anybody knows how to edit nonlinear transforms.<br>
I known from blender the lattice modifier, which would fulfill our needs:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b85cfd45deb148ec7a905f3288f01e889e94e250.gif" alt="ezgif-3-db915a63db94" data-base62-sha1="qiX5ahCvceuKjsWPUfJ3s7is0qA" width="600" height="338"></p>
<p>Has there anything been used in 3D Slicer which goes into this direction? If not, what would be an approach to implement functionality like this?</p>
<p>Many thanks!</p>

---

## Post #2 by @pieper (2019-12-20 14:22 UTC)

<p>Hi <a class="mention" href="/u/rprueckl">@rprueckl</a> - In the current release, 4.10, the LandmarkRegistration module lets you interactively control a thin plate spline nonlinear transform with realtime preview.  Unfortunately it hasn’t been ported to 4.11 (the markups API changed).</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.10/Modules/LandmarkRegistration" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/4.10/Modules/LandmarkRegistration</a></p>
<div class="lazyYT" data-youtube-id="SL5i50M_V5Y" data-youtube-title="Landmark registration Using Slicer for Multimodal Images" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>

---

## Post #3 by @lassoan (2019-12-20 15:35 UTC)

<p>You can use “Fiducial registration wizard” module in SlicerIGT extension, with warping transform option.</p>
<p>“Landmark Registration” module is more optimized for slight adjustment of volumes, while “Fiducial registration wizard” is a more general landmark registration module that is applicable to any kind of nodes, supports automatic point matching (for rigid transforms), sampling from real-time position trackers, transform preview, etc.</p>
<p>You can also compute non-linear transforms fully automatically. You can use SlicerElastix or Brains to automatically register volumes. You can use Segment Registration to non-automaticall register segments (or models, binary labelmaps) to each other.</p>

---
