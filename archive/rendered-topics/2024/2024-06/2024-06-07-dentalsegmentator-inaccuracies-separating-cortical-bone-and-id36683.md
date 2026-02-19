---
topic_id: 36683
title: "Dentalsegmentator Inaccuracies Separating Cortical Bone And"
date: 2024-06-07
url: https://discourse.slicer.org/t/36683
---

# DentalSegmentator inaccuracies separating cortical bone and teeth

**Topic ID**: 36683
**Date**: 2024-06-07
**URL**: https://discourse.slicer.org/t/dentalsegmentator-inaccuracies-separating-cortical-bone-and-teeth/36683

---

## Post #1 by @viet_duc_Vu (2024-06-07 06:32 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3bc77824b6ef28aa9c2b9c767c56563641af3274.png" alt="Untitled" data-base62-sha1="8wPwYaHs5Naw1Ou13blgqy7iQao" width="405" height="487"><br>
Hi.<br>
I really appreciate what you have done so far. The software is amazing. I have compared to between conventional segmentation ( with commercial software) and your segmentation extension. this extension helps reduce significantly the time for segmentation  compared to the conventional one. Especially, in case of CT data with artifacts.<br>
However. I still want to add some comments aiming for improving this extension. I have a concern that after trying several segmentation. Although the result is fine ( as you can see in the picture), the some part of 3D segments seem to lost quite much structure ( maybe as a default HU parameter)). You can see the red arrows pointing out losing bonny wall of maxilla and mandible.<br>
so in case, I want to improve the 3D segmentation structure, is there any way to do that ?<br>
Thank you</p>

---

## Post #2 by @Gauthier (2024-06-07 08:01 UTC)

<p>Hi,<br>
Thank you for your message. In the case of thin cortical bone (typically on the buccal/labial side of the teeth), it is often difficult (both manually and automatically!) to delineate the teeth from the bone.<br>
If there are some bony parts under-segmented when looking at the MPR slices, you can try to correct them manually using segment editor tools that are embedded on the left side of the extension.<br>
Best,<br>
Gauthier</p>

---
