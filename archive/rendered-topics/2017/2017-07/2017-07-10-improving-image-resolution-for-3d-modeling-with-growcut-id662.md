# Improving Image Resolution for 3D Modeling with GrowCut

**Topic ID**: 662
**Date**: 2017-07-10
**URL**: https://discourse.slicer.org/t/improving-image-resolution-for-3d-modeling-with-growcut/662

---

## Post #1 by @victoria.rose (2017-07-10 16:45 UTC)

<p>Slicer version: 4.7.0</p>
<p>I have high and low resolution images of patients and want to make 3D models of their semi-circular canals (low resolution image seen below; small bony structure consisting of three perpendicular, circular canals connected to the cochlea).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/b5299ef5ae60b161c9ea2a077c13a8606e5ef271.jpg" data-download-href="/uploads/short-url/pQDARCSOqw714V7ELJwc6OAiD7P.jpg?dl=1" title="image.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/b5299ef5ae60b161c9ea2a077c13a8606e5ef271_2_459x500.jpg" width="459" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/b5299ef5ae60b161c9ea2a077c13a8606e5ef271_2_459x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/b5299ef5ae60b161c9ea2a077c13a8606e5ef271_2_688x750.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b5299ef5ae60b161c9ea2a077c13a8606e5ef271.jpeg 2x" data-dominant-color="232323"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.jpg</span><span class="informations">788×858 87.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The low resolution files have a large pixel size (green selection = 1 pixel).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/e8437177c130da0d88ae3c6e6b44dd4345f7bdd2.jpg" data-download-href="/uploads/short-url/x8HgImA1KihB2Fg5xMpAyWyn64q.jpg?dl=1" title="image.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/e8437177c130da0d88ae3c6e6b44dd4345f7bdd2_2_651x499.jpg" width="651" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/e8437177c130da0d88ae3c6e6b44dd4345f7bdd2_2_651x499.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/e8437177c130da0d88ae3c6e6b44dd4345f7bdd2_2_976x748.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e8437177c130da0d88ae3c6e6b44dd4345f7bdd2.jpeg 2x" data-dominant-color="272727"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.jpg</span><span class="informations">1102×846 80.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The models made from the high resolution MRIs work very well with Laplacian smoothing models (grey model below) where GrowCut selected pixels based on my designated ROI. However, the low resolution images have pixel sizes that do not effectively separate the canals from the noise (as seen in the gold model that has incomplete canals below).</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fcdf24205b341db5b825c7cae7c8feaf4a51219b.png" alt="image" data-base62-sha1="A50oOlHTEHhuKgRpno30MHoMcfF" width="593" height="449"></p>
<p>I was wondering if you had any ideas on how to improve the models of the low resolution files? I have tried various thresholding and smoothing options in model maker but none of the parameters have resulted in complete canals.</p>
<p>Thank you!<br>
Victoria</p>

---

## Post #2 by @gaoyi.cn (2017-07-10 17:19 UTC)

<p>Hi,</p>
<p>This is kind of expected. With low resolution, the accuracy and topology of<br>
the segmentation may differ much from that from the high resolution…</p>
<p>Could i know the reason you would like to utilize the low resolution image<br>
instead of the high resolution one?</p>
<p>Best,<br>
yi</p>

---

## Post #3 by @victoria.rose (2017-07-10 17:36 UTC)

<p>Yi,</p>
<p>It unfortunately is what I expected, just thought I’d reach out to see ideas for improvement. For half of the patients we only have the low resolution images, not high, and I was hoping the 3D models could be salvageable given some processing.</p>
<p>Thanks!<br>
Victoria</p>

---

## Post #4 by @lassoan (2017-07-10 17:38 UTC)

<p>You can use <code>Crop volume</code> module to resample the volume to have a smaller voxel spacing. If you use that resampled volume as master volume, you will be able to segment smaller details.</p>

---

## Post #5 by @victoria.rose (2017-07-20 13:39 UTC)

<p>That worked perfectly, thank you!</p>

---
