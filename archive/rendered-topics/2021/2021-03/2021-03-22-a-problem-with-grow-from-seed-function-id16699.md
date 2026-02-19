---
topic_id: 16699
title: "A Problem With Grow From Seed Function"
date: 2021-03-22
url: https://discourse.slicer.org/t/16699
---

# A problem with "Grow from seed function"

**Topic ID**: 16699
**Date**: 2021-03-22
**URL**: https://discourse.slicer.org/t/a-problem-with-grow-from-seed-function/16699

---

## Post #1 by @YOZ (2021-03-22 19:35 UTC)

<p>Hello!</p>
<p>Can you guys help me with “Grow from seed function”. When I draw my seeds, and press initialize in the grow from seed function it show a square instead of tracking along the artery.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc75e9c83fd33778f3fc450b880c95e43da711be.jpeg" data-download-href="/uploads/short-url/qTcok8yYthZkjPIONZQNCnod3iu.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bc75e9c83fd33778f3fc450b880c95e43da711be_2_690x441.jpeg" alt="image" data-base62-sha1="qTcok8yYthZkjPIONZQNCnod3iu" width="690" height="441" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bc75e9c83fd33778f3fc450b880c95e43da711be_2_690x441.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bc75e9c83fd33778f3fc450b880c95e43da711be_2_1035x661.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bc75e9c83fd33778f3fc450b880c95e43da711be_2_1380x882.jpeg 2x" data-dominant-color="B6B6BB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2734×1749 472 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thank you for your hard work!</p>

---

## Post #2 by @pieper (2021-03-22 20:09 UTC)

<p>Hi - you need to add a background segment too (basically anything that is “not artery”) and add enough so that only your artery is left.</p>

---

## Post #3 by @lassoan (2021-03-24 17:28 UTC)

<p>Check out <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html#segment-editor-module-overview">segmentation tutorials</a> to learn how to segment and the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#grow-from-seeds">Grow from seeds effect documentation</a> get to know more about the Grow from seeds effect specifically.</p>

---

## Post #4 by @YOZ (2021-03-24 23:16 UTC)

<p>Thanks guys. That helped</p>

---
