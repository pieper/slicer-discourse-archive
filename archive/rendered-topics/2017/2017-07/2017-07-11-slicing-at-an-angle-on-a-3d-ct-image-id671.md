# Slicing at an angle on a 3D CT image

**Topic ID**: 671
**Date**: 2017-07-11
**URL**: https://discourse.slicer.org/t/slicing-at-an-angle-on-a-3d-ct-image/671

---

## Post #1 by @Ivan_Hidrovo (2017-07-11 20:38 UTC)

<p>Hello guys,</p>
<p>I have a 3D CT image of a tumor that I want to slice at an incline (angle) with respect to the x,y,z grid, and I want to be able to extract that plane. I am basically trying to crop at a certain angle. My goal is to have that plane be parallel to the flank of the mouse on which the tumor is located. Does the latest version of slicer have some module that could allow me to do this?</p>
<p>Thank you,<br>
Ivan</p>

---

## Post #2 by @lassoan (2017-07-11 21:32 UTC)

<p>If you want to crop a segmented tumor at a certain angle, use Segment editor (in latest nightly version) module’s Scissors tool:</p>
<div class="lazyYT" data-youtube-id="m4zTj8i4tCA" data-youtube-title='New "scissors" editing tool in 3D Slicer for 3D cropping' data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<p>If you want to crop the entire volume then use <code>Crop volume</code> module. To clip at an oblique angle, create a new region of interest (ROI), go to Transforms module, create a new Linear transform, apply it to the ROI, and rotate it (either using the sliders or by activating the Interaction widget in the Display section).</p>
<p>If you just want to view your tumor at arbitrarily oriented slice planes then use the <code>Reformat</code> module.</p>

---
