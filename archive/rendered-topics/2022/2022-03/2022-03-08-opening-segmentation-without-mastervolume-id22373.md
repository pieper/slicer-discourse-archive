---
topic_id: 22373
title: "Opening Segmentation Without Mastervolume"
date: 2022-03-08
url: https://discourse.slicer.org/t/22373
---

# Opening segmentation without mastervolume

**Topic ID**: 22373
**Date**: 2022-03-08
**URL**: https://discourse.slicer.org/t/opening-segmentation-without-mastervolume/22373

---

## Post #1 by @laura.h (2022-03-08 15:03 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.11.20210226</p>
<p>Hello, I am new to slicer and have a problem with opening my finished segmentation without a mastervolume.</p>
<p>I use a dummyFile (.nhdr), generated with my original binary data (CT), as the mastervolume for the segmentation.<br>
When I open the finished segmenation and the dummyFile, I am able to view all slices.</p>
<p>But when I try to open the finished segmentation (.seg.nrrd) without the mastervolume, only three of the 512 slices (that I can usually choose with the scroll bar) are shown. The scrollbar directly jumps from one end to the middle to the other end.</p>
<p>Is there a specific way to save/export the segmentation (should still be .seg.nrrd or .nrrd), so that I can open it without the mastervolume and still be able to view all slices?</p>
<p>Thank you in advance!<br>
Laura</p>

---

## Post #2 by @laura.h (2022-03-11 12:13 UTC)

<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cb832617a16928f1ae31fe57e1431989f7875c26.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cb832617a16928f1ae31fe57e1431989f7875c26.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cb832617a16928f1ae31fe57e1431989f7875c26.mp4</a>
    </source></video>
  </div><p></p>
<p>Additional video:</p>
<p>First you can see the segmentation with the master volume (dummyFile) and then without the mastervolume.</p>
<p>Without the mastervolume the red scrollbar jumps from -1.0000 to 0.0000 to 1.0000, whereas with the mastervolume it ranges from 0.0000 to 255.0000.</p>

---
