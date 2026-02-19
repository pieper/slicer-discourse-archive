---
topic_id: 33337
title: "Can Not Draw The Segment"
date: 2023-12-11
url: https://discourse.slicer.org/t/33337
---

# Can not draw the segment

**Topic ID**: 33337
**Date**: 2023-12-11
**URL**: https://discourse.slicer.org/t/can-not-draw-the-segment/33337

---

## Post #1 by @JamesM (2023-12-11 11:46 UTC)

<p>I am drawing tumor volumes on brain MRI, and I’m facing an issue where the drawing is not possible at the desired tumor location. It seems to be occurring only above that point, especially when dealing with tumors in the cerebellum. I’m unsure if this issue is related to the DICOM files or the settings in 3D Slicer. Is there a solution to this problem? Also, is there a way to ensure that the tumor’s position is centered on the screen?<br>
i will attach a video clip<br>
</p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/5617b10bc5353da08bfcb72cd194452be20b7675.mp4">
  </div><p></p>
<p>Thank you for your help!!</p>

---

## Post #2 by @cpinter (2023-12-11 11:53 UTC)

<p>Thanks for the video, it helps. This happens when the source volume’s extent is smaller than some other volume you are editing on. I assume that you created the segmentation using one volume but then you showed a new one and are editing on that. Is that correct? If so, then make sure that you create the segmentation with the volume you segment as source.</p>
<p>Also, the Slicer version cannot be seen in your video so I’d like to ask what version do you use? If not the latest 5.6 stable then please update.</p>

---

## Post #3 by @JamesM (2023-12-14 00:46 UTC)

<p>Thanks!. the problem has been resolved.</p>

---

## Post #4 by @cpinter (2023-12-14 10:15 UTC)

<p>Please describe how you resolved it for the benefit of forum users. Thanks</p>

---
