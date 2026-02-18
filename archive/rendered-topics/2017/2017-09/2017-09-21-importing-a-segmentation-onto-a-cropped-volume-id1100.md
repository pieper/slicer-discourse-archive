# Importing a segmentation onto a cropped volume

**Topic ID**: 1100
**Date**: 2017-09-21
**URL**: https://discourse.slicer.org/t/importing-a-segmentation-onto-a-cropped-volume/1100

---

## Post #1 by @stevenagl12 (2017-09-21 19:55 UTC)

<p>I have a cropped volume that I am trying to import the segmentation I performed on the main volume to. Is there an easy way to do this without registration?</p>

---

## Post #2 by @stevenagl12 (2017-09-21 20:16 UTC)

<p>Never mind, I figured out a way.</p>

---

## Post #3 by @Wayne (2023-02-05 14:07 UTC)

<p>Is any one can tell me how to do this import? I have the same problem, but I don’t know how to do. Thanks a lot.</p>

---

## Post #4 by @Wayne (2023-02-05 14:13 UTC)

<p>Or is there any way to corp a segmentation with a ROI?</p>

---

## Post #5 by @muratmaga (2023-02-05 15:28 UTC)

<p>Sure you can crop a segmentation. Just load it as a volume instead of segmentation and use the Crop Volume module.</p>
<p>However, I am not sure why you need to crop it? If you cropped your original volume within Slicer things should still continue to line up correctly…</p>

---

## Post #7 by @Wayne (2023-02-06 04:14 UTC)

<p>I used your method to crop the volume and the segmentation with one ROI. But, the cropped segmentation cannot fit the cropped volume. Do you have another method to resolve my problem?</p>

---

## Post #8 by @Wayne (2023-02-06 13:34 UTC)

<p>I have a volume of about 1.8 GB. I have creat a segmentation on it (about 900 MB), it cost me about one week. Now, I want to modify part of the segmentation. However, I found in the Segmentation Editor, each paint cost about 5 seconds. If I corp the volume that I interested in. The cropped volume will be 400 MB, and the new segmentation created on it will be 200 MB. Each paint will cost only 1 second. However, I must spend one more week to recreate all segmentations on the new segmentation. So, I want to know if there is a way to corp both the volume and old segmentation. And modify all segmentations based on the cropped volume and cropped segmentation.</p>

---
