# seperating a femur from the plevis

**Topic ID**: 1891
**Date**: 2018-01-22
**URL**: https://discourse.slicer.org/t/seperating-a-femur-from-the-plevis/1891

---

## Post #1 by @MSilent (2018-01-22 00:19 UTC)

<p>Operating system: Windos<br>
Slicer version:latest<br>
Expected behavior: segmentation of 2 bones<br>
Actual behavior: segmentation colour crosses to both bones</p>
<p>I am trying to 3d print a pelvis and a femur from a CT.  They have to be separate for the print so they will articulate for presurgical planning.  When I cut it down to size it works perfectly.  However when I try to use the editor to colour the femur and the pelvis two different colours the colour bleeds through to the other bone.  Until I can use separate colours for the two bones I will not be able to remove one and print it and then remove the first and print the second.</p>
<p>Thanks for any help.</p>
<p>MSilent</p>

---

## Post #2 by @pieper (2018-01-22 13:24 UTC)

<p>Probably your best option is to manually separate the two parts.  Using a sphere brush to paint the femoral head may be the easiest.  The Segment Editor with the scissors in 3D could also be very helpful.</p>

---

## Post #3 by @MRI23D (2018-01-22 13:41 UTC)

<p>Two MRI coordinations arent the same either. Patient head was slanted.</p>

---

## Post #4 by @lassoan (2018-01-22 16:57 UTC)

<p>I’ve tried semi-automatic method in the past, but due to pelvis and femur head have the same intensity in the image and they appear to be touching each other (unless image has very high resolution), they did not work well. So, Steve’s suggestion of using sphere brush will most likely the easiest method.</p>
<p>This has come up a few times, so I’ve recorded a video that shows the exact steps that you can follow:</p>
<div class="lazyYT" data-youtube-id="0at15gjk-Ns" data-youtube-title="Creating femur model from CT volume using 3D Slicer" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>

---

## Post #5 by @MSilent (2018-01-25 20:00 UTC)

<p>I watched your video but was busy and now I am working on the hip today.<br>
The video is no longer up.  Can you repost it so I can go step by step?</p>
<p>Thank you,<br>
Pat</p>

---
