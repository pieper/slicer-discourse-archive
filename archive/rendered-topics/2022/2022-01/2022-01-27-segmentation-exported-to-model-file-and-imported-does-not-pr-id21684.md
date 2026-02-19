---
topic_id: 21684
title: "Segmentation Exported To Model File And Imported Does Not Pr"
date: 2022-01-27
url: https://discourse.slicer.org/t/21684
---

# Segmentation exported to model file and imported does not preserve transparency

**Topic ID**: 21684
**Date**: 2022-01-27
**URL**: https://discourse.slicer.org/t/segmentation-exported-to-model-file-and-imported-does-not-preserve-transparency/21684

---

## Post #1 by @Young_Wang (2022-01-27 21:26 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> maybe I am not doing this right. But I found when I export the segmentation as a model and when I reload it back and visualize it with volume rendering. It doesn’t persevere the transparency</p>

---

## Post #2 by @lassoan (2022-01-28 23:48 UTC)

<p>I think this post will answer this question:</p>
<aside class="quote" data-post="2" data-topic="21625">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-can-i-export-a-brain-tumor-3d-model-with-brains-opacity/21625/2">How can I export a brain tumor 3d model with brains opacity?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    OBJ is an export format for segmentation (for exchanging data with other software), not a saving format (for saving data to be reloaded later). 
If you want to save the segmentation to disk without losing any information then save it as a .seg.nrrd (if labelmap is the master representation) or .seg.vtm (if closed surface is the master representation). 
Slicer’s OBJ reader only reads the .obj file (mesh geometry and material IDs) and not the .mat file (that contains the colors and opacities).
  </blockquote>
</aside>


---
