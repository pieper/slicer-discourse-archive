---
topic_id: 21184
title: "Segmentation Creation"
date: 2021-12-22
url: https://discourse.slicer.org/t/21184
---

# Segmentation creation

**Topic ID**: 21184
**Date**: 2021-12-22
**URL**: https://discourse.slicer.org/t/segmentation-creation/21184

---

## Post #1 by @19lollo95 (2021-12-22 15:54 UTC)

<p>Hi everyone,<br>
I have to segment the MRBrain considering white matter, gray matter, CFS, skull etc. How can I create an mhd file consisting of some of these objects? (e.g. how can I get one file / segment which contains only white and gray matter, another which contains CFS of the skull and the last which contains only a tumor)<br>
Thanks in advance</p>

---

## Post #2 by @lassoan (2021-12-23 16:02 UTC)

<p>See the answer in this post:</p>
<aside class="quote" data-post="2" data-topic="21183">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/segmentation-saving-support/21183/2">Segmentation saving support</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    When you export a segmentation to a labelmap then by default only the visible segments are exported. So, you can have two labelmap volumes, each containing one segment by showing one segment, export, showing the other segment, export. 
For volumetric mesh generation I would recommend to use SegmentMesher extension, which can generate multimaterial tetrahedral mesh directly from segmentation.
  </blockquote>
</aside>


---
