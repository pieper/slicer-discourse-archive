---
topic_id: 632
title: "Could Not Load 1 Ultrasound For Fetal Growth Meas As A Scala"
date: 2017-07-05
url: https://discourse.slicer.org/t/632
---

# Could not load: 1: Ultrasound for Fetal Growth Meas as a Scalar Volume

**Topic ID**: 632
**Date**: 2017-07-05
**URL**: https://discourse.slicer.org/t/could-not-load-1-ultrasound-for-fetal-growth-meas-as-a-scalar-volume/632

---

## Post #1 by @Nano_Alabbadi (2017-07-05 19:38 UTC)

<p>hey there thanx  for ur helpful program i had this massage (Could not load: 1: Ultrasound for Fetal Growth Meas as a Scalar Volume)</p>
<p>can u help me to fix it .</p>
<p>thanx a lot</p>

---

## Post #2 by @pieper (2017-07-05 20:22 UTC)

<p>Hi -</p>
<p>The data may be in a proprietary format that Slicer cannot read.</p>
<p>This page has some suggestions for debugging:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM</a></p>
<p>If the data happens to be from a Philips scanner this extension might help:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/SlicerHeart" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Extensions/SlicerHeart</a></p>
<p>Hope that helps,<br>
Steve</p>

---

## Post #4 by @lassoan (2017-07-06 18:21 UTC)

<p>Could you put all files in a zip folder and send a link to that? Or could you send the link to the folder that contains all the files?</p>

---

## Post #6 by @lassoan (2017-07-06 19:20 UTC)

<p>The data set might have contained patient-identifiable information, so I’ve removed the post. I’ll investigate the files and give you an update soon.</p>

---

## Post #7 by @lassoan (2017-07-06 19:31 UTC)

<p>The images are screen captures from the ultrasound machine. The easiest way to load them is to just drag-and-drop each file to the Slicer application window and click OK in the Add data dialog.</p>
<p>However, you cannot do much with these images: they are only 2D image slices (so you cannot do any 3d visualization or measurement). To make measurements you need to scale them by applying a transform (you can get the scale by measuring the distance between the white dots along the vertical ruler on the right side of the images, divide that by the real distance - 10mm between each dot, enter them into the first two diagonal values in the transform, inverting the transform, and applying it to the image).</p>

---

## Post #8 by @Nano_Alabbadi (2017-07-06 19:41 UTC)

<p>Thanx a lot <img src="https://emoji.discourse-cdn.com/twitter/pray/3.png?v=5" title=":pray:t3:" class="emoji" alt=":pray:t3:"></p>

---

## Post #9 by @Nano_Alabbadi (2017-07-06 19:45 UTC)

<p>Thanx a lot for ur help <img src="https://emoji.discourse-cdn.com/twitter/pray/3.png?v=5" title=":pray:t3:" class="emoji" alt=":pray:t3:"><img src="https://emoji.discourse-cdn.com/twitter/pray/3.png?v=5" title=":pray:t3:" class="emoji" alt=":pray:t3:"></p>

---
