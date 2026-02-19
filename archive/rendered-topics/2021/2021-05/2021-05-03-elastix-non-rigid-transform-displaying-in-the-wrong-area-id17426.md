---
topic_id: 17426
title: "Elastix Non Rigid Transform Displaying In The Wrong Area"
date: 2021-05-03
url: https://discourse.slicer.org/t/17426
---

# Elastix non-rigid transform displaying in the wrong area?

**Topic ID**: 17426
**Date**: 2021-05-03
**URL**: https://discourse.slicer.org/t/elastix-non-rigid-transform-displaying-in-the-wrong-area/17426

---

## Post #1 by @Teresa_Gadda (2021-05-03 22:40 UTC)

<p>Hello Slicer team -</p>
<p>I have performed a rigid registration using elastix of two spine images and thought I would try doing a non-rigid registration on the same images to see if it improves my result further.  I hardened the rigid registration transforms and then performed a non-rigid registration.  The registration completed successfully but when I ask to see the results, the deformed grid does not overlap the registration images.  The output volume, however, <em>does</em> appear to be deformed as I expected.  So I’m beginning to suspect that the transform just isn’t displaying in the correct location?  But I wanted to run it by this group and see if there’s something I’m not thinking of.  Let me show you some images.</p>
<p>Here is the fixed image (with the non-rigid transformation grid):<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a83c4377cf679ef2b539deb6362f47de37fbdc02.png" alt="image" data-base62-sha1="o0hkp1aWNOZe8uSy3e7zP1pbm5s" width="559" height="457"></p>
<p>Here is the moving image (note, it’s basically in the same location as the fixed image already because they were registered to each other previously):<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/15e8b8aff72acc66abb25c7feb6707467728deeb.png" alt="image" data-base62-sha1="37OD4Hhbig19f3ty5vRkKz0fz2X" width="579" height="469"></p>
<p>Here is the output image from elastix (the outputVolumeNode):<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/573ece4e3a8356d618d5ccb2da6cf1cac175d82c.png" alt="image" data-base62-sha1="crO6fTpHxLRNZGSVJG7Ksty13ru" width="573" height="442"></p>
<p>So what I’m wondering is, <strong>why isn’t the visualization of the transform on top of the images that are transformed?</strong></p>
<p>Let me know if more data would help.  I can send the images, elastix parameters, elastix log files/results, etc.</p>

---

## Post #2 by @lassoan (2021-05-21 18:42 UTC)

<p>Does the transform appear in correct location if you enable Advanced / Force grid output transform option?</p>

---
