---
topic_id: 29594
title: "Apply Resample And Or Crop To Transformed Volume"
date: 2023-05-23
url: https://discourse.slicer.org/t/29594
---

# Apply Resample and/or Crop to transformed volume

**Topic ID**: 29594
**Date**: 2023-05-23
**URL**: https://discourse.slicer.org/t/apply-resample-and-or-crop-to-transformed-volume/29594

---

## Post #1 by @bserrano (2023-05-23 06:59 UTC)

<p>Hi all,</p>
<p>We want to reduce the spacial spacing between slices by applying Resample Scalar Volume or Crop Volume modules. When importing the volume this message appears.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/9465af4b7f1a5acaac9447f11c3a09de8f8c52a2.png" alt="imagen" data-base62-sha1="laMwuZ1mbinpiYPr5NyX850CICe" width="583" height="110"></p>
<p>After loading the volume, the application of the modules (Resample or Crop) does not work on the transformed volume, but on the original one.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a809ce80b3b369db897ea50691256a1b0a7355c.png" alt="imagen" data-base62-sha1="aD4SQQbOvvSIlHbgXSI9hvgOXpi" width="504" height="208"></p>
<p>I saw this post <a href="https://discourse.slicer.org/t/apply-reformat-reslicing/887">Apply reformat reslicing</a>, but I can’t make this solution work.</p>
<p>How can I apply the same transform to the resliced volume?</p>
<p>Thanks <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @pieper (2023-05-23 13:36 UTC)

<p>You’ll need to harden the transform first, <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html#harden-transform-on-a-node">as described here</a>.</p>

---
