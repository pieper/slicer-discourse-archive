---
topic_id: 47420
title: "Brain MRI Gray Matter"
date: 2026-06-22
url: https://discourse.slicer.org/t/47420
last_bumped: 2026-06-22T06:10:07.981Z
---

# Brain MRI Gray Matter

**Topic ID**: 47420
**Date**: 2026-06-22
**URL**: https://discourse.slicer.org/t/brain-mri-gray-matter/47420

---

## Post #1 by @bruce2647 (2026-06-22 06:10 UTC)

<p>Continuing the discussion from <a href="https://discourse.slicer.org/t/brain-mri-gray-matter-segmentation/23718/18">Brain MRI Gray Matter Segmentation</a>:</p>
<aside class="quote no-group" data-username="drnoorfatima" data-post="18" data-topic="23718">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/drnoorfatima/48/81980_2.png" class="avatar"><a href="https://discourse.slicer.org/t/brain-mri-gray-matter-segmentation/23718/18">Brain MRI Gray Matter Segmentation</a></div>
<blockquote>
<p>Hi Kurt, what a cool project!</p>
<p>The smoothness issue you’re seeing on the sides and rear is actually a really common frustration with this workflow, thresholding alone isn’t designed to capture cortical surface detail well, especially the sulci and gyri. It’s not something you can fix just by adjusting the threshold values.</p>
<p>Getting the cortical folds to come out properly for 3D printing involves a few extra steps beyond what most tutorials cover, and the extension route you found has some compatibility nuances that trip people up.</p>
<p>I work with brain MRI segmentation and have done similar pipelines before. If you want I can take a look at what you have and point you in the right direction, feel free to DM me.</p>
</blockquote>
</aside>
<p>Fatima explained this really well. The point about thresholding not capturing cortical surface detail properly is probably the key issue here, especially around the sulci and gyri.</p>
<p>A lot of Brain MRI segmentation and 3D reconstruction workflows run into this when trying to prepare models for printing. The compatibility issues with some extensions can also make the process more frustrating than most tutorials suggest.</p>
<p>Hopefully Kurt shares an update because it would be interesting to see how the final reconstruction turns out.</p>

---

## Post #2 by @discourse_ai_spam (2026-06-22 06:10 UTC)



---

## Post #3 by @system (2026-06-22 12:41 UTC)



---
