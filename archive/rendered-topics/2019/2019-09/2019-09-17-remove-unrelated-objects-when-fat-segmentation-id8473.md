---
topic_id: 8473
title: "Remove Unrelated Objects When Fat Segmentation"
date: 2019-09-17
url: https://discourse.slicer.org/t/8473
---

# Remove unrelated objects when fat segmentation

**Topic ID**: 8473
**Date**: 2019-09-17
**URL**: https://discourse.slicer.org/t/remove-unrelated-objects-when-fat-segmentation/8473

---

## Post #1 by @hu_shuang (2019-09-17 22:59 UTC)

<p>Is there a function that can remove unrelated objects such as blanket, clothing, and scanning couch when segment fat by thresholding on CT?</p>

---

## Post #2 by @lassoan (2019-09-17 23:20 UTC)

<p>Probably the easiest is to threshold everything and then cut off irrelevant regions using Scissors tool.</p>
<p>You may also use masking settings: create a segment that only covers the body and then use that as editable region.</p>

---

## Post #3 by @hu_shuang (2019-09-17 23:41 UTC)

<p>Hi Iassoan,<br>
Thank you for your reply. I have around 70 whole body CTs to be processed, It’s not realistic for me to cut off irrelevant regions one section by section manually and there also would be bias when the pixels are close to fat. Is there an automatic way?<br>
Shuang</p>

---

## Post #4 by @lassoan (2019-09-17 23:51 UTC)

<p>70 images are not too many. If you can cut off the table with 1 minute of extra work for each then most likely that will be the fastest solution.</p>

---

## Post #5 by @hu_shuang (2019-09-17 23:59 UTC)

<p>Actually it’s around 70 patients and each of them have more than 240 images, I see a thin open circle just outside of the skin almost in every slice if using thresholding which is very annoying. there is also unwanted pixels in the sharp decreasing area, ie. pixels right next to air.</p>

---

## Post #6 by @hu_shuang (2019-09-18 00:09 UTC)

<p>one article described that they removed those using morphologic opening operations and then denoised the images using standard median filtering and then did the threshold to get fat. However, I don’t know how to do it in 3d slicer and wonder if there is some other methods to segment fat.</p>

---

## Post #7 by @Juicy (2019-09-18 03:32 UTC)

<p>If the other parts are unconnected islands you could try the island effect in segment editor. I find keep largest island pretty useful. Otherwise ‘remove selected island’ deletes any islands which you click on in the 2D views. There are also other options in there.</p>

---
