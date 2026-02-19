---
topic_id: 5013
title: "Fiducials Specify Segment In 3D View"
date: 2018-12-07
url: https://discourse.slicer.org/t/5013
---

# Fiducials - specify segment in 3D view?

**Topic ID**: 5013
**Date**: 2018-12-07
**URL**: https://discourse.slicer.org/t/fiducials-specify-segment-in-3d-view/5013

---

## Post #1 by @hherhold (2018-12-07 23:03 UTC)

<p>I am viewing 2 segments in the 3D viewer - insect exoskeleton in one segment and some internal anatomy in a 2nd segment. The exoskeleton has its opacity turned down so I can view the internal segment “in situ”. What I would like to be able to do is place a fiducial on the internal anatomy segment by clicking in the 3D viewer. What happens, though, is the intersection test hits the exoskeleton first and places the fiducial on the surface of the exoskeleton.</p>
<p>Is there a way to tell fiducial placement to ignore some segments?</p>
<p>Thanks!!!</p>
<p>-Hollister</p>

---

## Post #2 by @hherhold (2018-12-07 23:04 UTC)

<p>Oh yeah, if there’s not a way to do this and it sounds generally useful, I’m willing to take a stab at trying to implement it.</p>

---

## Post #3 by @lassoan (2018-12-07 23:44 UTC)

<p>You can only set “selectable” attribute per node. So, if you want to make the exoskeleton visible but want to prevent clicking on it then export the exoskeleton to a model and make it not selectable.</p>
<p>If you install SlicerVirtualReality extension then you get a context-menu item in Data module that allows toggle selectable state.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/698a33ae2e636ded4bd6362db1aab77c9541d4c8.png" data-download-href="/uploads/short-url/f3Eeif0MYOF9Z7beQuP1e2Xw6WQ.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/698a33ae2e636ded4bd6362db1aab77c9541d4c8_2_325x500.png" alt="image" data-base62-sha1="f3Eeif0MYOF9Z7beQuP1e2Xw6WQ" width="325" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/698a33ae2e636ded4bd6362db1aab77c9541d4c8_2_325x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/698a33ae2e636ded4bd6362db1aab77c9541d4c8_2_487x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/698a33ae2e636ded4bd6362db1aab77c9541d4c8.png 2x" data-dominant-color="ECF0F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">568×872 30.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If you don’t want or cannot install SlicerVirtualReality extension then you can make a mode node not selectable using the Python console. For example, if you exported Segment_2 to a model node, you can prevent placing markup points by typing this:</p>
<p><code>getNode('Segment_2').SetSelectable(False)</code></p>
<p>This requires recent nightly version (Slicer-4.10 does not contain this feature).</p>

---

## Post #4 by @hherhold (2018-12-07 23:53 UTC)

<p>Got it. So a Segmentation is a node in and of itself, is that correct? (And this is why exporting to a model node is the way to do this?)</p>
<p>Thanks, Andras!</p>

---

## Post #5 by @hherhold (2018-12-08 00:14 UTC)

<p>(This works great, by the way. Thanks!!!)</p>

---

## Post #6 by @lassoan (2018-12-08 02:24 UTC)

<aside class="quote no-group" data-username="hherhold" data-post="4" data-topic="5013">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar"> hherhold:</div>
<blockquote>
<p>Segmentation is a node in and of itself</p>
</blockquote>
</aside>
<p>Yes, and you specify “selectable” property for the whole segmentation node, with all segments in it. However, when you export segments to models, each segments becomes a separate model node that you can make selectable/non-selectable.</p>

---
