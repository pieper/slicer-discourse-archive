---
topic_id: 32869
title: "Segmentation Of Ultrasound Sequence"
date: 2023-11-17
url: https://discourse.slicer.org/t/32869
---

# Segmentation of ultrasound sequence

**Topic ID**: 32869
**Date**: 2023-11-17
**URL**: https://discourse.slicer.org/t/segmentation-of-ultrasound-sequence/32869

---

## Post #1 by @priya.vada4 (2023-11-17 03:27 UTC)

<p>Hi</p>
<p>Is it possible to segment a structure from a sequence of tracked ultrasound images and create a 3D surface model.</p>
<p>These are the steps I follow:</p>
<ol>
<li>
<p>I stream the optically-tracked ultrasound images from a third-party client using OpenIGTLink.</p>
</li>
<li>
<p>I then record a Sequence using the tracked ultrasound images.</p>
</li>
<li>
<p>Using Segment Editor, I create a Segmentation node and add it to the same sequence created above.</p>
</li>
<li>
<p>Stepping through the sequence, I segment the structure of interest on the ultrasound images. This is turning out to be painful, because I have to change the Source geometry for each ultrasound slice. Is there an easier way to segment the structure on each ultrasound slice.</p>
</li>
<li>
<p>Once I have segmented the structure on all the ultrasound slices, I would like to combine the segmentations from all the slices in the Sequence to create a 3D model of the structure. How could I do this?</p>
</li>
</ol>
<p>Regards,<br>
Priya</p>
<p>P.S: Volume rendering is not satisfactory to visualize the 3D structure.</p>

---

## Post #2 by @priya.vada4 (2023-11-21 15:19 UTC)

<p>Any suggestions to solve this issue.</p>
<p>Thanks<br>
Priya</p>

---

## Post #3 by @LeidyMoraV (2024-05-14 21:27 UTC)

<p>Maybe this video would be helpful: <a href="https://www.youtube.com/watch?v=l0BcW8c9CnI" rel="noopener nofollow ugc">Tracked ultrasound AI segmentation and 3D reconstruction tutorial (youtube.com)</a></p>

---
