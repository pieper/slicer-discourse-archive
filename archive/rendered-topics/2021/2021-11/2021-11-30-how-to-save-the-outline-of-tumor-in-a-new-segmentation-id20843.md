---
topic_id: 20843
title: "How To Save The Outline Of Tumor In A New Segmentation"
date: 2021-11-30
url: https://discourse.slicer.org/t/20843
---

# how to save the outline of tumor in a new segmentation

**Topic ID**: 20843
**Date**: 2021-11-30
**URL**: https://discourse.slicer.org/t/how-to-save-the-outline-of-tumor-in-a-new-segmentation/20843

---

## Post #1 by @LIE_CAI (2021-11-30 13:45 UTC)

<p>I know that using the function “hollow” could create the outline of the targeted objects.<br>
I don’t want to delete the object’s segmentation but want to save the outline and the objects in different segmentations separately. How to operate it?<br>
Thanks a lot!</p>

---

## Post #2 by @pieper (2021-11-30 13:53 UTC)

<p>I’d suggest making a copy of the segment and doing the Hollow operation on that.</p>

---

## Post #3 by @LIE_CAI (2021-11-30 14:41 UTC)

<p>Thanks, I wonder if there’s a solution that could show the outline and the targeted subject at the same time.</p>

---

## Post #4 by @pieper (2021-11-30 14:43 UTC)

<p>They will show at the same time.  Typically Slicer highlights the outline as part of the rendering process, which you control with the display options.  But if you make a new segment or segmentation by copying they should show at the same time and you can operate on them independently.</p>

---

## Post #5 by @LIE_CAI (2021-11-30 14:51 UTC)

<p>ha, I see, it works!<br>
Many thanks for your explanation! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=10" title=":slight_smile:" class="emoji" alt=":slight_smile:"> <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=10" title=":smiley:" class="emoji" alt=":smiley:"></p>

---
