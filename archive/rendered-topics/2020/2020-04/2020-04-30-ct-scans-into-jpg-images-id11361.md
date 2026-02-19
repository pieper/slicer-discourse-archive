---
topic_id: 11361
title: "Ct Scans Into Jpg Images"
date: 2020-04-30
url: https://discourse.slicer.org/t/11361
---

# CT scans into jpg images

**Topic ID**: 11361
**Date**: 2020-04-30
**URL**: https://discourse.slicer.org/t/ct-scans-into-jpg-images/11361

---

## Post #1 by @anitakh1 (2020-04-30 09:26 UTC)

<p>hello. can you please guide me how to convert CT volume scans (.raw files) into axial, saggital and coronal jpg or ong images?</p>

---

## Post #2 by @pieper (2020-04-30 11:53 UTC)

<p>You can use ScreenCapture for that: <a href="https://www.slicer.org/wiki/Documentation/4.10/Modules/ScreenCapture">https://www.slicer.org/wiki/Documentation/4.10/Modules/ScreenCapture</a></p>

---

## Post #3 by @anitakh1 (2020-04-30 14:05 UTC)

<p>thank you so much. it works. and now after doing some work, if i want to combine the 3 view to get back the volume, what do i have to do?</p>

---

## Post #4 by @pieper (2020-04-30 14:30 UTC)

<p>Don’t use the jpegs to store volumes.  Best to use nrrd instead.</p>

---

## Post #5 by @anitakh1 (2020-04-30 16:13 UTC)

<p>but i will be working on 2D slices of the 3 views so result will also be 2D images. then i need to combine the results of the 3 views (which are in 2D form) to get the final output.</p>

---

## Post #6 by @muratmaga (2020-04-30 16:39 UTC)

<p>What are you trying to do?</p>

---

## Post #7 by @anitakh1 (2020-05-01 05:41 UTC)

<p>hello. i am working on airway segmentation from CT lung volume. so will use 2D images and segmented ground truth in all 3 views to train CNN then will segment airways of new CT volumes. lastly will try to put them in volume again to see the airway segmented tree and calculate airway length and volume etc. hope i sound clear. thanks</p>

---

## Post #8 by @muratmaga (2020-05-01 14:44 UTC)

<p>Yes, that part I understand. What I am not following is why you need the segmented slices in 2D? There are 3D resnet and unet…</p>

---

## Post #9 by @JanWitowski (2020-05-03 09:00 UTC)

<p>You can easily change 3D matrices in NRRD files into a stack of 2D NRRD arrays for each slice. Then  save them in separate files, e.g. using pynrrd library. Jpegs are worst possible format for this, you lose a lot of information from the CT by limiting the pixel range and compressing data.</p>

---

## Post #10 by @anitakh1 (2020-05-05 14:05 UTC)

<p>thanks for the suggestions. i will try</p>

---

## Post #11 by @anitakh1 (2020-05-07 06:28 UTC)

<p>Screen capture captures the screen but what to do if i want to capture each slice of 512X512 size?? kindly guide</p>

---

## Post #12 by @anitakh1 (2020-05-15 11:03 UTC)

<p>i downloaded preview version of 3D slicer 4.11.0 but fast marching effect is not there in segment editor while i can see in one of the videos. how can i get fast marching effect?</p>

---

## Post #13 by @anitakh1 (2020-05-17 12:49 UTC)

<p>actually i am preparing some ground truth of segmented airway and segment lung airway is giving lot of leakages. i followed some slicer videos and i think fast marching module can help. pl suggest</p>

---
