# Mask volume multilabel

**Topic ID**: 23910
**Date**: 2022-06-17
**URL**: https://discourse.slicer.org/t/mask-volume-multilabel/23910

---

## Post #1 by @bserrano (2022-06-17 12:08 UTC)

<p>Hi all,</p>
<p>I’ve working recently with Mask Volume from Segment Editor, is a very usefull tool in terms of image segmentation. However, it only works with binary labels. It would be possible to add a multilabel option?</p>
<p>I mean, if we have 2 segments and I want pixels of segment 1 to have value 5 and pixels of segment 2 to have value 10 and create a new volume with that information.</p>

---

## Post #2 by @mau_igna_06 (2022-06-17 12:31 UTC)

<p>Maybe export the sehmentation as a labelmap and edit the numpy array affter</p>

---

## Post #3 by @bserrano (2022-06-17 13:21 UTC)

<p>Thanks, it works! Now I have pixel_value = 1 for segment_1 and pixel_value = 2 for segment_2. Are these values always generated depending on the order of the segments in the segmentation?</p>
<p>Do you know if I can choose the pixel value in advance?</p>

---

## Post #4 by @mau_igna_06 (2022-06-17 13:23 UTC)

<p>I believe you can.</p>
<p>Please explore the segmenetations module</p>

---

## Post #5 by @lassoan (2022-06-17 19:36 UTC)

<p>You can specify what label value you want to use for each segment by using a color table.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/dee3fbd571a4f6237173215e8bbb921938e7e12a.png" data-download-href="/uploads/short-url/vNMrYRZD6flyin96TePOj6Cbwvw.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/dee3fbd571a4f6237173215e8bbb921938e7e12a_2_396x500.png" alt="image" data-base62-sha1="vNMrYRZD6flyin96TePOj6Cbwvw" width="396" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/dee3fbd571a4f6237173215e8bbb921938e7e12a_2_396x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/dee3fbd571a4f6237173215e8bbb921938e7e12a_2_594x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/dee3fbd571a4f6237173215e8bbb921938e7e12a_2_792x1000.png 2x" data-dominant-color="41403F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">874×1101 66.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Color is found by matching the segment name to the color name. The assigned label value is the color’s index in the table.</p>

---
