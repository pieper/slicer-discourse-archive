---
topic_id: 29147
title: "Segmenting In A Rotated Volume"
date: 2023-04-26
url: https://discourse.slicer.org/t/29147
---

# Segmenting in a rotated volume

**Topic ID**: 29147
**Date**: 2023-04-26
**URL**: https://discourse.slicer.org/t/segmenting-in-a-rotated-volume/29147

---

## Post #1 by @chris_nik (2023-04-26 17:23 UTC)

<p>Hello dear community, it is me again. I made the following observation which induced a question:</p>
<p>Goal: to segment a rotated volume</p>
<p>Observation: if I create a new segment first and then rotate the volume in the ‘Transforms’ module, the segmentation tools work properly (s. Fig.1). However, if I rotate the volume first and then create a new segment, the area I mark with the segmentation tools gets distorted or is not completely filled (s. Fig.2). I then also get a notification that slice views orientation is not aligned with segmentation (s. Fig.3). I suppose this means that the orientation of the volume does not match the orientation of the segmentation. If I click on the latter notification button the volume gets rotated back to its original position, the segmentation tools work properly again, but my goal to segment in a rotated volume is not met anymore.</p>
<p>For this reason I normally create the segment first, then rotate the volume and it works fine for the most part. Sometimes the markup I create in one slice gets transferred to the adjacent one, however this behaviour is seldom. I also don’t get a notification that the slice orientation does not match the segmentation orientation. I still wanted to ask if I am doing it right and if there is an explanation for the behaviour in case of volume rotation and then segment creation.</p>
<p>Cheers</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/679b1295727d8d99aefb63e09b3586d42ecd11cc.png" data-download-href="/uploads/short-url/eMxq69b3PuNIppsBVIYOKMfgoiw.png?dl=1" title="Upload5" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/679b1295727d8d99aefb63e09b3586d42ecd11cc_2_690x491.png" alt="Upload5" data-base62-sha1="eMxq69b3PuNIppsBVIYOKMfgoiw" width="690" height="491" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/679b1295727d8d99aefb63e09b3586d42ecd11cc_2_690x491.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/679b1295727d8d99aefb63e09b3586d42ecd11cc.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/679b1295727d8d99aefb63e09b3586d42ecd11cc.png 2x" data-dominant-color="383632"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Upload5</span><span class="informations">790×563 101 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Fig.1: Segment created, then volume rotated; proper fill of marked area</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/dbb41d6d48ab687e29a499b911fc0d7bc6389074.jpeg" data-download-href="/uploads/short-url/vlAsygkMTbWB5YhdJwxTx0vg9pi.jpeg?dl=1" title="Upload1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/dbb41d6d48ab687e29a499b911fc0d7bc6389074_2_690x487.jpeg" alt="Upload1" data-base62-sha1="vlAsygkMTbWB5YhdJwxTx0vg9pi" width="690" height="487" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/dbb41d6d48ab687e29a499b911fc0d7bc6389074_2_690x487.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/dbb41d6d48ab687e29a499b911fc0d7bc6389074.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/dbb41d6d48ab687e29a499b911fc0d7bc6389074.jpeg 2x" data-dominant-color="4F4D49"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Upload1</span><span class="informations">793×560 76.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b817ee79d9f9189ed742e79e93049c6dc336c1f4.jpeg" data-download-href="/uploads/short-url/qgz7UKbI7UIrdlV235yFRdmzRUE.jpeg?dl=1" title="Upload2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b817ee79d9f9189ed742e79e93049c6dc336c1f4_2_690x489.jpeg" alt="Upload2" data-base62-sha1="qgz7UKbI7UIrdlV235yFRdmzRUE" width="690" height="489" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b817ee79d9f9189ed742e79e93049c6dc336c1f4_2_690x489.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b817ee79d9f9189ed742e79e93049c6dc336c1f4.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b817ee79d9f9189ed742e79e93049c6dc336c1f4.jpeg 2x" data-dominant-color="4F4D49"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Upload2</span><span class="informations">795×564 81.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/628fcbc58f20ba40206f893b07291c2d4c2972b1.jpeg" data-download-href="/uploads/short-url/e3USa1VzfmS42svIu5zpZUjhGeZ.jpeg?dl=1" title="Upload3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/628fcbc58f20ba40206f893b07291c2d4c2972b1_2_368x500.jpeg" alt="Upload3" data-base62-sha1="e3USa1VzfmS42svIu5zpZUjhGeZ" width="368" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/628fcbc58f20ba40206f893b07291c2d4c2972b1_2_368x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/628fcbc58f20ba40206f893b07291c2d4c2972b1_2_552x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/628fcbc58f20ba40206f893b07291c2d4c2972b1_2_736x1000.jpeg 2x" data-dominant-color="585855"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Upload3</span><span class="informations">795×1079 117 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Fig.2: Volume rotated, then segment created; distortion and unproper fill of marked area, in the frontal view the brush tool seems to be unaligned with the marked area</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/1268b57a0a00a7712155ce05b21b203e1221ba65.jpeg" data-download-href="/uploads/short-url/2CQVNwjY88QaXpggXA4rIuNZ4ih.jpeg?dl=1" title="Upload4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/1268b57a0a00a7712155ce05b21b203e1221ba65_2_690x317.jpeg" alt="Upload4" data-base62-sha1="2CQVNwjY88QaXpggXA4rIuNZ4ih" width="690" height="317" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/1268b57a0a00a7712155ce05b21b203e1221ba65_2_690x317.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/1268b57a0a00a7712155ce05b21b203e1221ba65_2_1035x475.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/1268b57a0a00a7712155ce05b21b203e1221ba65_2_1380x634.jpeg 2x" data-dominant-color="4B4E4E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Upload4</span><span class="informations">1592×732 177 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Fig.3: Notification that slice orientation is not aligned with segmentation in case of volume rotation and then segment creation</p>

---

## Post #2 by @pieper (2023-04-26 17:40 UTC)

<p>Interestingly, this topic <a href="https://discourse.slicer.org/t/segmentation-using-paint-the-bulb-of-paint-disappears-after-the-image-is-oriented-in-accordance-with-the-anatomical-axes/29128">just came up</a> yesterday.  There’s a <a href="https://lassoan.github.io/SlicerSegmentationRecipes/ObliqueSliceSegmentation/">great description here</a>.  Maybe we can do something to make the behavior more intuitive.</p>

---

## Post #3 by @chris_nik (2023-04-26 20:27 UTC)

<p>Thank you very much, I will try both methods : )</p>

---
