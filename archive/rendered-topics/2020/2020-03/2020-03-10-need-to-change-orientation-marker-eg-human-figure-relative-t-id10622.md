---
topic_id: 10622
title: "Need To Change Orientation Marker Eg Human Figure Relative T"
date: 2020-03-10
url: https://discourse.slicer.org/t/10622
---

# Need to change orientation marker (eg human figure) relative to volume

**Topic ID**: 10622
**Date**: 2020-03-10
**URL**: https://discourse.slicer.org/t/need-to-change-orientation-marker-eg-human-figure-relative-to-volume/10622

---

## Post #1 by @Joshua_Broder (2020-03-10 19:46 UTC)

<p>Operating system: Windows<br>
Slicer version: 4.11.0-2020-02-20<br>
Expected behavior: I need to rotate the human figure orientation marker to match the orientation of my image volume.<br>
Actual behavior:  Currently, the orientation of the marker is not synchronized to the volume orientation.  Can this be specified in the scene view or other default file?  My letter coordinates are correct, but I would like to use the intuitive human body image.</p>

---

## Post #2 by @Juicy (2020-03-11 07:35 UTC)

<p>The human marker should be oriented correctly in 3d space and should match the letter coordinates. If there is a mismatch then it is more likely that the volume has not loaded in the correct orientation. Has the volume been loaded from a DICOM file?</p>

---

## Post #3 by @lassoan (2020-03-11 12:03 UTC)

<aside class="quote no-group" data-username="Juicy" data-post="2" data-topic="10622">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/74df32/48.png" class="avatar"> Juicy:</div>
<blockquote>
<p>volume has not loaded in the correct orientation</p>
</blockquote>
</aside>
<p>Fully agree. You need to reorient your volume using Transforms module.</p>

---

## Post #4 by @Joshua_Broder (2020-03-11 19:57 UTC)

<p>Thanks for responses.  I was able to achieve the desired effect using the Transforms module.  The volumes we are loading are of our own making, reconstructed from 2D ultrasound images.  Perhaps you can clarify – where in the .mrml (or elsewhere) is the orientation specified?  I understand how to encode the letters for the axes, but how is the default orientation of the volume relative to the orientation graphic determined?</p>

---
