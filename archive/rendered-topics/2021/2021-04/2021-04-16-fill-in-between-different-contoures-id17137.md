---
topic_id: 17137
title: "Fill In Between Different Contoures"
date: 2021-04-16
url: https://discourse.slicer.org/t/17137
---

# Fill in between different contoures

**Topic ID**: 17137
**Date**: 2021-04-16
**URL**: https://discourse.slicer.org/t/fill-in-between-different-contoures/17137

---

## Post #1 by @aseman (2021-04-16 18:21 UTC)

<p>Slicer version: 4.10.1<br>
Hi 3D slicer experts and all<br>
I have a number of contours that are in separate segments(like Fig A). I want to make a model of all of them (like Fig B). How can I fill in between them to finally have a contour and make  an integrated model(Fig B)?<br>
Thanks a lot</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d56ccac419fe33f36046a9ad13ed0e642247a3ab.png" data-download-href="/uploads/short-url/us2MNDSwhfRyeqjwgFNN5qY1aGv.png?dl=1" title="picture1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d56ccac419fe33f36046a9ad13ed0e642247a3ab_2_354x375.png" alt="picture1" data-base62-sha1="us2MNDSwhfRyeqjwgFNN5qY1aGv" width="354" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d56ccac419fe33f36046a9ad13ed0e642247a3ab_2_354x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d56ccac419fe33f36046a9ad13ed0e642247a3ab.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d56ccac419fe33f36046a9ad13ed0e642247a3ab.png 2x" data-dominant-color="8B91A9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">picture1</span><span class="informations">509×539 71.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2021-04-18 05:42 UTC)

<p>You can use Segment editor for this: choose Scissors effect, Operation → Fill inside; Masking / Editable area → Inside all segments, and trace a large circle around the object. For automated processing the easiest is to threshold the labelmap.</p>

---
