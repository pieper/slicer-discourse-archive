---
topic_id: 28861
title: "Where Is Hu At Segment Statistics Module"
date: 2023-04-12
url: https://discourse.slicer.org/t/28861
---

# Where is HU at Segment Statistics module?

**Topic ID**: 28861
**Date**: 2023-04-12
**URL**: https://discourse.slicer.org/t/where-is-hu-at-segment-statistics-module/28861

---

## Post #1 by @Igor1023 (2023-04-12 11:32 UTC)

<p>Hy everyone. Im a student of Sechenov Medical University. Now im trying to manage with 3D Slicer and i want to know, where can i find Haunsfield Units here. Thank you.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/eeba81f765440ea20900d9052cc3de4e3dce1698.jpeg" data-download-href="/uploads/short-url/y3TebCPfKiJ73c9YyHi3PFoxnM4.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/eeba81f765440ea20900d9052cc3de4e3dce1698_2_689x500.jpeg" alt="image" data-base62-sha1="y3TebCPfKiJ73c9YyHi3PFoxnM4" width="689" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/eeba81f765440ea20900d9052cc3de4e3dce1698_2_689x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/eeba81f765440ea20900d9052cc3de4e3dce1698_2_1033x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/eeba81f765440ea20900d9052cc3de4e3dce1698.jpeg 2x" data-dominant-color="9A9595"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1355×983 202 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @rbumm (2023-04-12 13:23 UTC)

<p>Please select a volume in the Segment Statistics extension to get the HU.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7aa2fb982ca581d896fb2998712db8703320bc48.jpeg" data-download-href="/uploads/short-url/huTriWS77ue0WFoJmjRbCzRPnn2.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7aa2fb982ca581d896fb2998712db8703320bc48_2_690x264.jpeg" alt="image" data-base62-sha1="huTriWS77ue0WFoJmjRbCzRPnn2" width="690" height="264" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7aa2fb982ca581d896fb2998712db8703320bc48_2_690x264.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7aa2fb982ca581d896fb2998712db8703320bc48_2_1035x396.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7aa2fb982ca581d896fb2998712db8703320bc48_2_1380x528.jpeg 2x" data-dominant-color="AEADAC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1816×697 281 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @Igor1023 (2023-04-13 12:32 UTC)

<p>excuse me, are those 3 columns HU?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/562b8cf9c6b75554d4cbea63026d8f00c0924f9d.png" data-download-href="/uploads/short-url/ciimTS5cyvWWjezOHMG4CsFFzfD.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/562b8cf9c6b75554d4cbea63026d8f00c0924f9d_2_690x388.png" alt="image" data-base62-sha1="ciimTS5cyvWWjezOHMG4CsFFzfD" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/562b8cf9c6b75554d4cbea63026d8f00c0924f9d_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/562b8cf9c6b75554d4cbea63026d8f00c0924f9d_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/562b8cf9c6b75554d4cbea63026d8f00c0924f9d_2_1380x776.png 2x" data-dominant-color="B4B0AD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 343 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2023-04-13 12:53 UTC)

<p>Yes, in clinical CT images voxel values are specified in HU, therefore the intensity statistics (minimum, maximum. mean, median, standard deviation values) are all computed in HU.</p>

---

## Post #5 by @Igor1023 (2023-04-19 14:07 UTC)

<p>im sorry again. but what if i need to measure density in two or more specific areas of tumor or implant etc</p>
<p>P.S sorry for my english</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/18fcaba4c49b6387c52aca5da4670dbf3168e895.png" data-download-href="/uploads/short-url/3z2NNTMgVF1LOB2Di1hfBOJlhUp.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/18fcaba4c49b6387c52aca5da4670dbf3168e895_2_690x361.png" alt="image" data-base62-sha1="3z2NNTMgVF1LOB2Di1hfBOJlhUp" width="690" height="361" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/18fcaba4c49b6387c52aca5da4670dbf3168e895_2_690x361.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/18fcaba4c49b6387c52aca5da4670dbf3168e895_2_1035x541.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/18fcaba4c49b6387c52aca5da4670dbf3168e895_2_1380x722.png 2x" data-dominant-color="383739"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1919×1005 266 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Arrows are showing areas of interest</p>

---

## Post #6 by @pieper (2023-04-19 14:10 UTC)

<p>You can use the Segment Editor to define the regions over which you want to measure the HU values.</p>

---

## Post #7 by @Igor1023 (2023-04-19 14:27 UTC)

<p>Thank you. in the right corner there is a result of segmentation. H I J K columns shows density of all CT images or only of my region?</p>

---

## Post #8 by @pieper (2023-04-19 14:31 UTC)

<p>From the screenshot the values in the H I J columns of the segment statistics are for the segment named ‘bone’, not the full volume.  Make additional segments in the segment editor and you will get additional rows with the per-segment HU values.</p>

---

## Post #9 by @Igor1023 (2023-04-19 14:49 UTC)

<p>ok thank you. so if i want to measure specific points i need to define smaller region including those points, right?</p>

---

## Post #10 by @pieper (2023-04-19 14:52 UTC)

<p>Correct.  Use segments if you want to calculate statistics over multiple voxels, or use the DataProbe to look at the values at specific points.</p>

---

## Post #11 by @Igor1023 (2023-04-19 15:00 UTC)

<p>thank you. is 3982 dencity on HU?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cdba9049b95bdb29613499b9ce99567c1b3fc78b.png" data-download-href="/uploads/short-url/tlXAIhvEd76hd5mNnheBvBK3Zd9.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cdba9049b95bdb29613499b9ce99567c1b3fc78b_2_592x499.png" alt="image" data-base62-sha1="tlXAIhvEd76hd5mNnheBvBK3Zd9" width="592" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cdba9049b95bdb29613499b9ce99567c1b3fc78b_2_592x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cdba9049b95bdb29613499b9ce99567c1b3fc78b_2_888x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cdba9049b95bdb29613499b9ce99567c1b3fc78b.png 2x" data-dominant-color="363533"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1178×994 188 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #12 by @pieper (2023-04-19 15:03 UTC)

<p>That depends on the calibration of your scan.  Clinical CTs are generally good, but cone-beam CTs are often not calibrated.  You can search for information on this.  Slicer just reports what’s in the images.</p>

---

## Post #13 by @Igor1023 (2023-04-19 15:09 UTC)

<p>no i mean in what units of measurement is this number?</p>

---

## Post #14 by @pieper (2023-04-19 15:23 UTC)

<p>The units are whatever is in your file.</p>

---

## Post #15 by @Igor1023 (2023-04-19 16:09 UTC)

<p>can you please say where i can find average value of density at my segmet?</p>

---

## Post #16 by @Igor1023 (2023-04-19 16:30 UTC)

<p>hi, can you please tell how to measure average density of my segmentation?</p>

---

## Post #17 by @pieper (2023-04-19 16:34 UTC)

<p>Sorry if it’s not coming through but I believe we have already told you exactly what you are asking.  Were you able to create multiple structures and get the statistics for each segment?</p>

---

## Post #18 by @Igor1023 (2023-04-19 16:37 UTC)

<p>im sorry. im asking not about it. i have my segmentation and i wnat to know average density of it, not for another segemts. just of segment that i already have. i suugest that it is mean column. but i cant say exactly, so im asking you about it</p>

---

## Post #19 by @Igor1023 (2023-04-19 16:39 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8e50a32ebc183586bbb00a621a7b3e174fd11ff5.png" alt="image" data-base62-sha1="kiYz4zhwIGpKWX6tiOYW41YvFzL" width="386" height="233"><br>
average density of this one, who named as bone</p>

---

## Post #20 by @pieper (2023-04-19 16:53 UTC)

<p>Yes, in this case average density (x-ray absorption) is the mean column of the segment statistics when the CT is selected as the scalar volume.</p>

---

## Post #21 by @Igor1023 (2023-04-19 16:54 UTC)

<p>thank you very much. and to be 100% sure mean column is in HU right?</p>

---

## Post #22 by @pieper (2023-04-19 17:01 UTC)

<p>Yes, CT scans come in units of HU.  What we don’t always know is how accurately the HU is measured by the device, so there may be some amount of error due to the scanner and/or discretization of the pixels and segmentation so you should keep that in mind when interpreting the numbers for any specific task.</p>

---

## Post #23 by @Igor1023 (2023-04-19 17:03 UTC)

<p>thanks you made my day.</p>

---
