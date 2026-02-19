---
topic_id: 1340
title: "Transfer Segmentation To Same But Differently Cropped Volume"
date: 2017-11-01
url: https://discourse.slicer.org/t/1340
---

# Transfer segmentation to same but differently cropped volume

**Topic ID**: 1340
**Date**: 2017-11-01
**URL**: https://discourse.slicer.org/t/transfer-segmentation-to-same-but-differently-cropped-volume/1340

---

## Post #1 by @Clara_Korting (2017-11-01 10:43 UTC)

<p>Hi,</p>
<p>I just started using 3D Slicer and have encountered a problem now that I couldn’t find an answer to yet. It would be great if someone has an idea how to solve it and help me.</p>
<p>I started segmenting the muscles of the lower leg of a patient just to notice when almost done that the image I was using was not cropped correctly and I was missing about 5 slices that I wanted to segment as well. I cropped my nifti-image again and was able to show the same segmentation on my new volume however I cannot continue with the segmentation here outside of borders of the old volume. My question is now is there a way to transfer my old segmentation to the new volume and continue there or would I have to segment everything again?</p>
<p>Thank you very much in advance and for taking the time!</p>
<p>Best,<br>
Clara</p>

---

## Post #2 by @lassoan (2017-11-01 11:40 UTC)

<p>This has come up a few times and we already have a ticket for this: <a href="https://issues.slicer.org/view.php?id=4308">https://issues.slicer.org/view.php?id=4308</a></p>
<p>Until a convenient user interface is implemented, you need to do the following steps manually:</p>
<ul>
<li>Switch to Segment Editor module</li>
<li>Create a new segmentation</li>
<li>Set Master volume (the new, larger volume)</li>
<li>Switch to Segmentations module</li>
<li>Import all segments from the other segmentation using Copy/Move section</li>
</ul>

---

## Post #3 by @Clara_Korting (2017-11-01 15:52 UTC)

<p>Thank you very much that’s exactly what I was hoping for!</p>

---

## Post #4 by @lassoan (2023-03-21 02:51 UTC)



---
