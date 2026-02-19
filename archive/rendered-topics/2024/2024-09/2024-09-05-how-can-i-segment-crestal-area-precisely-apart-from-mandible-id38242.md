---
topic_id: 38242
title: "How Can I Segment Crestal Area Precisely Apart From Mandible"
date: 2024-09-05
url: https://discourse.slicer.org/t/38242
---

# How can I segment crestal area precisely apart from mandible because of its variability?

**Topic ID**: 38242
**Date**: 2024-09-05
**URL**: https://discourse.slicer.org/t/how-can-i-segment-crestal-area-precisely-apart-from-mandible-because-of-its-variability/38242

---

## Post #1 by @yijie3091 (2024-09-05 15:48 UTC)

<p>Because of the crestal area’s variability,how can I  segment it precisely apart from mandible in slicermorph?</p>

---

## Post #2 by @muratmaga (2024-09-05 19:42 UTC)

<p>Please share screenshots that are showing the types of challenges you are facing? Also segmentation is a core feature of 3D Slicer, and not part of SlicerMorph extension.</p>

---

## Post #3 by @yijie3091 (2024-09-06 10:47 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/909ea74b9bc04ead33cd4063acf577fae068b905.png" data-download-href="/uploads/short-url/kDmFuLNNdh4ZpxUUAVKiDKFglj7.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/909ea74b9bc04ead33cd4063acf577fae068b905_2_468x500.png" alt="image" data-base62-sha1="kDmFuLNNdh4ZpxUUAVKiDKFglj7" width="468" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/909ea74b9bc04ead33cd4063acf577fae068b905_2_468x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/909ea74b9bc04ead33cd4063acf577fae068b905_2_702x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/909ea74b9bc04ead33cd4063acf577fae068b905.png 2x" data-dominant-color="9592AE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">706×754 75.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8c1fb17fc563cce88a28e66e97f1faa09f2e1e31.png" data-download-href="/uploads/short-url/jZAKptVdZyMp8s4nBv1jojdjPFv.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c1fb17fc563cce88a28e66e97f1faa09f2e1e31_2_476x500.png" alt="image" data-base62-sha1="jZAKptVdZyMp8s4nBv1jojdjPFv" width="476" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c1fb17fc563cce88a28e66e97f1faa09f2e1e31_2_476x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8c1fb17fc563cce88a28e66e97f1faa09f2e1e31.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8c1fb17fc563cce88a28e66e97f1faa09f2e1e31.png 2x" data-dominant-color="9A98AC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">664×697 69.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>OK,I want to remove this red region.</p>

---

## Post #4 by @muratmaga (2024-09-06 16:35 UTC)

<p>I don’t think there is anything automatic to help you remove those regions. You can use a number of effects in the Segment Editor (paint and threshold) to delete them.</p>

---
