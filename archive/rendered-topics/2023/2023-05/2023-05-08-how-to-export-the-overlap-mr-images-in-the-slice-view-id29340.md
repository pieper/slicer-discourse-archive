# How to export the overlap MR images in the slice view

**Topic ID**: 29340
**Date**: 2023-05-08
**URL**: https://discourse.slicer.org/t/how-to-export-the-overlap-mr-images-in-the-slice-view/29340

---

## Post #1 by @Eugene_Zh (2023-05-08 05:06 UTC)

<p>Operating system: Windows 11<br>
Slicer version: 5.2.2</p>
<p>Dear All,<br>
I have two different MR Sequences that is already registered, but not the same FOV. I can overlap them in the slice view by using the foreground-background tool. But I want to fuse them and export to one nii file. I have read some QA in the forum like use the stitch volume in Sandbox （the output is concatenate but not overlap and adjust opacity）or Mask volume（I don‘t know how to turn a raw nii MR image to a mask）.  I want to find a method to export the overlapped image and can adjust the cover order and opacity just like the slice view shows. Could you please help to find a way to do this?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/704aa877fca674a7ecae3461b4ed0cebb50007a0.jpeg" data-download-href="/uploads/short-url/g1nqIllBKraFYkCBBxuXkAikBiM.jpeg?dl=1" title="图片" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/704aa877fca674a7ecae3461b4ed0cebb50007a0_2_690x497.jpeg" alt="图片" data-base62-sha1="g1nqIllBKraFYkCBBxuXkAikBiM" width="690" height="497" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/704aa877fca674a7ecae3461b4ed0cebb50007a0_2_690x497.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/704aa877fca674a7ecae3461b4ed0cebb50007a0_2_1035x745.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/704aa877fca674a7ecae3461b4ed0cebb50007a0.jpeg 2x" data-dominant-color="343134"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">图片</span><span class="informations">1274×919 131 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<em>overlapped slice view</em><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6add138ca7f4bc6e16cfc4e309f605714c10a459.png" alt="图片" data-base62-sha1="ffmgtIq4Q49I97Y8eNxaBc5NIO5" width="225" height="435"><br>
<em>the output of the Stitch volume</em><br>
Thank you so much！</p>
<p>Best regards,<br>
Eugene</p>

---

## Post #2 by @Sam_Horvath (2023-05-08 14:51 UTC)

<p>You could look at the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/addscalarvolumes.html">Add Scalar Volumes</a> module.</p>
<p>Also you can try the <a href="https://slicer.readthedocs.io/en/5.2/user_guide/modules/simplefilters.html">Simple Filters</a> module to put together a pipeline to create the blended image, using the Multiply and Add filters.</p>

---
