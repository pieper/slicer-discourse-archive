---
topic_id: 9940
title: "Slice Slider Step Size"
date: 2020-01-25
url: https://discourse.slicer.org/t/9940
---

# Slice slider step size

**Topic ID**: 9940
**Date**: 2020-01-25
**URL**: https://discourse.slicer.org/t/slice-slider-step-size/9940

---

## Post #1 by @jpasadena (2020-01-25 01:33 UTC)

<p>Operating system: Mac 10.14.6<br>
Slicer version: 4.10.2<br>
Expected behavior: Slide through slice 1 pixel at a time<br>
Actual behavior: Slides 10 pixels at a time</p>
<p>Total newbie here. I just would like to step through my slices one pixel at a time.<br>
My volume is 1606x1606x181 pixels. The 181 direction allows steps of one pixel,<br>
but the others only step 10 at a time, apparently with interpolation. I would like to<br>
see the original data, uninterpolated, at full resolution. There must be a simple way (?)</p>

---

## Post #2 by @Juicy (2020-01-25 04:01 UTC)

<p>First make sure that you are looking through the volume in the same direction as the original images. The colored view windows (red, yellow and green) always look through the volume normal to the primary axes (X, Y, Z) but sometimes the images may have been acquired with gantry tilt or more commonly reconstructed with a slight oblique angle from the normal primary axes.</p>
<p>To check this hover over the pin in one of the colored view ports, then click the chain icon to link all 3 views. Then click the small flyout arrows on the left hand side of the menu. Then click the icon called “Rotate to volume plane”. If you see no change then that means the images were reconstructed in the primary axial, coronal or sagittal directions but if you see a slight rotation then the images were constructed with a gantry tilt or on a oblique angle.</p>
<p>To disable interpolation go to the volumes module and make sure you have the right volume selected at the top then scroll down to the Display area and untick interpolate.</p>
<p>As for image spacing slicer should automatically skip through the images at the correct slice spacing as long as you are looking at the original image plane. If you do need to over-ride the image spacing then you can change this by again clicking the small pin icon in the view you want to change, un check the chain icon this time so the settings are not linked between views, then go to slice spacing and uncheck automatic. You can then go to the manual area and type in the desired slice spacing for the view window.</p>
<p>Hope this is what you are after.</p>

---

## Post #3 by @lassoan (2020-01-25 18:03 UTC)

<p>Can you step slice by slice if you use arrow keys or mouse scroll wheel (after you clicked in the slice viewer, not on the slider)?</p>
<p>Screen resolution is limited therefore the slider may not have as many positions as the image dimensions along that axis. Maybe Qt slider has changed during the years, so maybe it can handle more positions than pixels, so we could revisit this.</p>
<p>In Slicer, everything is 3D, so we are not constrained by the original image resolution or axes, which may be unusual first, but gives a lot of flexibility and not a problem in general. If you can describe what your goal is then we can give more specific explanation or advice, or tune the software behavior to match what to need.</p>

---

## Post #4 by @jpasadena (2020-01-25 19:43 UTC)

<p>“Can you step slice by slice if you use arrow keys or mouse scroll wheel…”</p>
<p>Yes! This is the answer! I figured it was something as simple as that.</p>
<p>On the Mac the arrow keys step 1 pixel over. As does scrolling, which<br>
on my trackpad is set as a two-finger swipe up or down.</p>
<p>So I am in business. Just FYI, this is not medical imaging, it is geophysical.<br>
I loaded the data from 181 slices as png images. The volume appears to<br>
be constructed properly. Thanks for the help and I am excited to be part<br>
of the Slicer community!</p>

---

## Post #5 by @jpasadena (2020-01-25 19:48 UTC)

<p>One more thing, in case I need it down the road:</p>
<p>Juicy said:</p>
<p>“then go to slice spacing and uncheck automatic”</p>
<p>Where is the slice spacing dialog? Which pane?<br>
Which button? And where is the “manual area”?</p>

---

## Post #6 by @Juicy (2020-01-25 20:56 UTC)

<p>See following image. In this case it is in the red pane but these options are available for all the colored panes. I have also put a yellow arrow pointing to the rotate to volume plane button I mentioned above but that may not be needed if it isn’t a medical image (not sure how geophysical images work) and I may have misinterpreted what you were after.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc66972ccf2c1fb0373976bbb829deedf42d1ab3.jpeg" alt="Slicer Forum Pic" data-base62-sha1="tadcAXrlRANGRIGbNKaFMyGy47x" width="634" height="419"></p>

---

## Post #7 by @Xiaojie_Guo (2023-11-10 02:42 UTC)

<p>Hi, is it possible to step slice by slice automatically? For example, step 10 slices in a second automatically.</p>

---
