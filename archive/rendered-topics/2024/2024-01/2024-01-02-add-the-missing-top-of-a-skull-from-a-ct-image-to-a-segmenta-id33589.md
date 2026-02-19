---
topic_id: 33589
title: "Add The Missing Top Of A Skull From A Ct Image To A Segmenta"
date: 2024-01-02
url: https://discourse.slicer.org/t/33589
---

# Add the missing top of a skull from a CT image to a segmentation for 3D model

**Topic ID**: 33589
**Date**: 2024-01-02
**URL**: https://discourse.slicer.org/t/add-the-missing-top-of-a-skull-from-a-ct-image-to-a-segmentation-for-3d-model/33589

---

## Post #1 by @MaikeRos (2024-01-02 17:11 UTC)

<p>Hello there,</p>
<p>I extracted CBCT images of a patient with RTStruct files and loaded them into Slicer. The problem with my CBCT image is, that the top of the skull is missing. I tried manually to add it to the corresponding segmentations of the body and the skull. But drawing it by hand over about 200 slices and no possibilty of copying the shape of one slice, I didn’t manage it. Is there maybe some extension or something, I can do, that Slicer recognizes the skull and the shape of the head and adds the missing slices, so that I have the whole head?</p>
<p>Would be so glad, if anyone has an idea <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>Kind regards,<br>
Maike</p>

---

## Post #2 by @lassoan (2024-01-02 17:14 UTC)

<p>You can do much better than copying segmentation from previous slice: you can use “Fill between slices” effect to interpolate between slices. It is enough to segment every 5th or 10th slice and the effect can fill in the blanks.</p>
<p>However, instead of inventing a skull shape, it is probably better to register a CT image that contains the full skull and bring over that skull segmentation from there.</p>

---
