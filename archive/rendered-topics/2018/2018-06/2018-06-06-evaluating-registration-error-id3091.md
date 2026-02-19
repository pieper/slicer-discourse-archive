---
topic_id: 3091
title: "Evaluating Registration Error"
date: 2018-06-06
url: https://discourse.slicer.org/t/3091
---

# Evaluating registration error

**Topic ID**: 3091
**Date**: 2018-06-06
**URL**: https://discourse.slicer.org/t/evaluating-registration-error/3091

---

## Post #1 by @DavideBassano (2018-06-06 15:53 UTC)

<p>Hello,</p>
<p>I have to do <strong>registration</strong> of 2 similar volumes: one from a CT (dicom file) and one is a .stl file I created.<br>
I did the manual registration overlapping them.<br>
I need to know if the .stl volume I created is similar to the real volume from CT.<br>
Does exist a way to calculate an <strong>error after the registration</strong> ? So I could understand if the volume I created is realistic compared to the real volume. Maybe I could try another type of registration instead of the manual one, which would give me back also a registration error (I don’t know).</p>
<p>Thanks,</p>
<p>Davide</p>

---

## Post #2 by @lassoan (2018-06-06 21:58 UTC)

<p>For qualitative assessment, you can show the segmentation performed on the moving volume transformed to the fixed volume and overlaid on the fixed volume. You can supplement that with <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Transforms#Transform_display_options">Transforms module’s visualization options</a>:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a19db221f97564ea5fedb882d94e47d296a822f.jpeg" alt="image" data-base62-sha1="azwJckI6TMnVSpd0UX9rC1idRMz" width="280" height="239"></p>
<p>For quantitative assessment, you can evaluate registration result by comparing segmentation that was transformed from the moving volume to the fixed volume, to segmentation that was done directly on the fixed volume.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/SegmentComparison">Segment comparison module</a> (in SlicerRT extension) can give you quantitative metrics about segment similarity (Hausdorff and Dice metrics).</p>

---

## Post #3 by @DavideBassano (2018-06-07 08:17 UTC)

<p>Dear Andras,</p>
<p>thanks for your answer.<br>
I can’t understand why I have to do the segmentation: my volumes are already defined and overlapped (see picture attached). I just need to assess the registration and understand if the trasnformed volume is fitting well with the fixed volume from CT.<br>
How can I do it?</p>
<p>Thanks,<br>
Davide<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/dde54af788698523cb64b07b85314365e1e51dac.jpeg" data-download-href="/uploads/short-url/vEYMgZ7jEBCc7PJhZS211YezspC.jpg?dl=1" title="IMG_20180607_101757__01" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dde54af788698523cb64b07b85314365e1e51dac_2_265x500.jpg" alt="IMG_20180607_101757__01" data-base62-sha1="vEYMgZ7jEBCc7PJhZS211YezspC" width="265" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dde54af788698523cb64b07b85314365e1e51dac_2_265x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dde54af788698523cb64b07b85314365e1e51dac_2_397x750.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dde54af788698523cb64b07b85314365e1e51dac_2_530x1000.jpg 2x" data-dominant-color="A89AAC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_20180607_101757__01</span><span class="informations">1727×3258 2.18 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
In this picture you can see CT volume in red and the volume I created (grey), overlapped.</p>

---

## Post #4 by @lassoan (2018-06-07 15:45 UTC)

<p>You only need to do segmentation if you want to get quantitative results using Hausdorff or Dice metrics.</p>
<p>It is also useful to do a very simple, threshold-based segmentation if you want to compare two images in a slice view, as it is difficult to see misalignment on two images that are blended together (especially when you want to see small differences), while misalignment is very clearly visible if you overlay extracted contours on an image.</p>
<p>Example 1: perfectly aligned images (left: blending two images; right: overlaying thresholding result on the other image)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cf21b2f76f112beb0b9684a971351fbe5c8aab94.jpeg" data-download-href="/uploads/short-url/tyn2fIiaKuWAFkEyHSK0FCZ5FUU.jpg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cf21b2f76f112beb0b9684a971351fbe5c8aab94_2_690x330.jpg" alt="image" data-base62-sha1="tyn2fIiaKuWAFkEyHSK0FCZ5FUU" width="690" height="330" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cf21b2f76f112beb0b9684a971351fbe5c8aab94_2_690x330.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cf21b2f76f112beb0b9684a971351fbe5c8aab94.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cf21b2f76f112beb0b9684a971351fbe5c8aab94.jpeg 2x" data-dominant-color="8E8F8D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">908×435 77.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Example 2: slightly misaligned images (left: blending two images; right: overlaying thresholding result on the other image). Misalignment appears as slight blurring on the left, and it is clearly visible on the right.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/54e53284d2e27a7f55160b29842bb527fa83869d.jpeg" data-download-href="/uploads/short-url/c719Xa6QJluvfa2cJFXrtjyCxfD.jpg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/54e53284d2e27a7f55160b29842bb527fa83869d_2_690x329.jpg" alt="image" data-base62-sha1="c719Xa6QJluvfa2cJFXrtjyCxfD" width="690" height="329" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/54e53284d2e27a7f55160b29842bb527fa83869d_2_690x329.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/54e53284d2e27a7f55160b29842bb527fa83869d.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/54e53284d2e27a7f55160b29842bb527fa83869d.jpeg 2x" data-dominant-color="8E8E8C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">913×436 76.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Another common method for quantitative assessment of registration result is to define corresponding anatomical landmarks on the moving and fixed image and compare the position difference between the fixed image landmarks and the transformed moving image landmarks (they should be exactly the same if the registration is perfect). Fiducial registration wizard module (in SlicerIGT extension) can compute this error (and also a transformation) from such anatomical landmarks.</p>

---

## Post #5 by @Saima (2020-12-16 14:06 UTC)

<p>how to check rigid registration between ct and mri. Ct being registered to mri using rigid registration. is there any other way to register ct to mri</p>
<p>regards,<br>
Saima safdar</p>

---
