---
topic_id: 23592
title: "Dicom Sort Method"
date: 2022-05-26
url: https://discourse.slicer.org/t/23592
---

# DICOM sort method

**Topic ID**: 23592
**Date**: 2022-05-26
**URL**: https://discourse.slicer.org/t/dicom-sort-method/23592

---

## Post #1 by @Hu-nie (2022-05-26 01:34 UTC)

<p>I have a question about DICOM.</p>
<p>I am dealing with MR images. At this time, I try to use the Instance Number when aligning the DICOM. When I look at the Type of  Instance Number Tag, it says “Required, Empty if Unknown (2)”, but it sounds like there are cases where it doesn’t exist. What should I do in this case?</p>

---

## Post #2 by @lassoan (2022-05-27 03:21 UTC)

<p>Instance number must not be used for spatial sorting. Only the <code>image position patient</code> and <code>image orientation patient</code> tags are allowed for spatial positioning of the image slice. Slicer’s DICOM module uses these tags for reconstructing 3D volume from slices.</p>

---

## Post #3 by @Hu-nie (2022-05-27 04:00 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Thanks for the reply first.</p>
<p>So does this mean that I have to sort using “image position patient and image orientation patient tags” when loading DICOM?</p>
<p>If so, where is the “Instance Number” tag used?</p>

---

## Post #4 by @lassoan (2022-05-27 04:37 UTC)

<aside class="quote no-group" data-username="Hu-nie" data-post="3" data-topic="23592">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hu-nie/48/13631_2.png" class="avatar"> Hu-nie:</div>
<blockquote>
<p>So does this mean that I have to sort using “image position patient and image orientation patient tags” when loading DICOM?</p>
</blockquote>
</aside>
<p>You don’t need to, because Slicer does this for you, along with many other checks, corrections of varying spacing, etc.</p>
<aside class="quote no-group" data-username="Hu-nie" data-post="3" data-topic="23592">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hu-nie/48/13631_2.png" class="avatar"> Hu-nie:</div>
<blockquote>
<p>where is the “Instance Number” tag used?</p>
</blockquote>
</aside>
<p>It is typically displayed for the user and serves as a human-readable label for a image series or frame.</p>

---
