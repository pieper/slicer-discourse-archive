---
topic_id: 14776
title: "3D View Of Vector Image"
date: 2020-11-25
url: https://discourse.slicer.org/t/14776
---

# 3D view of vector image

**Topic ID**: 14776
**Date**: 2020-11-25
**URL**: https://discourse.slicer.org/t/3d-view-of-vector-image/14776

---

## Post #1 by @Marinho95 (2020-11-25 20:56 UTC)

<p>Hi,<br>
Currently, I am reading out ultrasound image data from the Clarius ultrasound device through Plusserver. This works fine and I can see the ultrasound image on the red slice. However, when I press the eye icon on the red slice, I don’t see the image in the 3D view, but only a black square. See image:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c01aa0d96f4ef82afacfb4e76d4a499b8eac3a4f.png" data-download-href="/uploads/short-url/rpqIXNyPGk6U62XP6tn7BPw5EyX.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c01aa0d96f4ef82afacfb4e76d4a499b8eac3a4f_2_409x499.png" alt="image" data-base62-sha1="rpqIXNyPGk6U62XP6tn7BPw5EyX" width="409" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c01aa0d96f4ef82afacfb4e76d4a499b8eac3a4f_2_409x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c01aa0d96f4ef82afacfb4e76d4a499b8eac3a4f_2_613x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c01aa0d96f4ef82afacfb4e76d4a499b8eac3a4f.png 2x" data-dominant-color="4E4D60"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">744×908 74.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Is this a bug or do I have to change some settings? The image is a vector image.</p>

---

## Post #2 by @lassoan (2020-11-25 21:47 UTC)

<p>Can you save the scene as mrb, upload it somewhere and post the link here?</p>

---

## Post #3 by @Marinho95 (2020-11-26 12:38 UTC)

<p>Yes, I added the file in the following link:</p>
<p><a href="https://ufile.io/og7p8xwo" class="onebox" target="_blank" rel="noopener nofollow ugc">https://ufile.io/og7p8xwo</a></p>
<p>The ultrasound images are saved in a sequence. So you can also navigate through time to see different ultrasound images.</p>

---

## Post #4 by @lassoan (2020-11-27 02:53 UTC)

<p>Thank you for the image. You have run into this known limitation: <a href="https://github.com/Slicer/Slicer/issues/4939">RGBA images do not appear in image slices displayed in 3D views</a>. I’ve tried to fix this issue a couple of months ago, but it would requires reworking of the imaging pipeline, which would take at least several days of work, so it is not likely to happen in the next 1-2 months.</p>
<p>Since the images are grayscale, it would make more sense to send them as a single-channel image from Plus. If you want to crop display to the image fan then you can send that on a separate  channel (preferably only when the imaging geometry changes, to reduce bandwidth). You could also convert in Slicer (add an observer to the RGBA image and whenever it is updated, extract one of its components into a separate image), but it may decrease the frame rate.</p>

---
