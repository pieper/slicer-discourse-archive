# Question in general registration(BRAINS)

**Topic ID**: 23106
**Date**: 2022-04-24
**URL**: https://discourse.slicer.org/t/question-in-general-registration-brains/23106

---

## Post #1 by @Rui_Zhuang (2022-04-24 13:10 UTC)

<p>when I use general registration(BRAINS) to compare two ct volume, in the fixed image volume and moving image volume is the same ct volume. However, I have imported the two CT volumes, the Beforeopration and the Afteropration. How could I solve the problem?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0a0b0801cea57b88b9bf3e2b25699827429aca77.jpeg" data-download-href="/uploads/short-url/1qQpmBOMgbr9WT0e9mmJfL44szd.jpeg?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0a0b0801cea57b88b9bf3e2b25699827429aca77_2_690x351.jpeg" alt="1" data-base62-sha1="1qQpmBOMgbr9WT0e9mmJfL44szd" width="690" height="351" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0a0b0801cea57b88b9bf3e2b25699827429aca77_2_690x351.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0a0b0801cea57b88b9bf3e2b25699827429aca77_2_1035x526.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0a0b0801cea57b88b9bf3e2b25699827429aca77_2_1380x702.jpeg 2x" data-dominant-color="DBE7F1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1608×818 126 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f91346421c3d15e1eb4f2681d6933db8444515f8.jpeg" data-download-href="/uploads/short-url/zxqbuSwaO5v6yGTVKPtamepgKPm.jpeg?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f91346421c3d15e1eb4f2681d6933db8444515f8_2_690x364.jpeg" alt="2" data-base62-sha1="zxqbuSwaO5v6yGTVKPtamepgKPm" width="690" height="364" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f91346421c3d15e1eb4f2681d6933db8444515f8_2_690x364.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f91346421c3d15e1eb4f2681d6933db8444515f8_2_1035x546.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f91346421c3d15e1eb4f2681d6933db8444515f8_2_1380x728.jpeg 2x" data-dominant-color="8A8989"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">2564×1354 195 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1bf6ba9df4c9c5445e0b894dfb483c22ae889253.jpeg" data-download-href="/uploads/short-url/3ZnvnoZNva4xN26veS5O17v58oX.jpeg?dl=1" title="3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1bf6ba9df4c9c5445e0b894dfb483c22ae889253_2_690x371.jpeg" alt="3" data-base62-sha1="3ZnvnoZNva4xN26veS5O17v58oX" width="690" height="371" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1bf6ba9df4c9c5445e0b894dfb483c22ae889253_2_690x371.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1bf6ba9df4c9c5445e0b894dfb483c22ae889253_2_1035x556.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1bf6ba9df4c9c5445e0b894dfb483c22ae889253_2_1380x742.jpeg 2x" data-dominant-color="858484"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3</span><span class="informations">2538×1365 372 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2022-04-24 19:54 UTC)

<p>The images detected as a time sequence and got loaded as a MultiVolume. MultiVolume nodes don’t show up in scalar volume selectors, so you cannot select it as input in the registration module.</p>
<p>I would recommend to enable “Advanced” option in the DICOM module and load the images as separate scalar volumes.</p>

---
