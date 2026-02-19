---
topic_id: 14187
title: "Building 3D Slicer On Mac Os Catalina"
date: 2020-10-21
url: https://discourse.slicer.org/t/14187
---

# building 3D Slicer on Mac OS Catalina 

**Topic ID**: 14187
**Date**: 2020-10-21
**URL**: https://discourse.slicer.org/t/building-3d-slicer-on-mac-os-catalina/14187

---

## Post #1 by @zolfagha (2020-10-21 14:01 UTC)

<p>Hi there,</p>
<p>I am missing some segmentation effects such as “Local Threshold” when I install 3D Slicer via .dmg on my Mac OS Catalina 10.15.5.</p>
<p>How can I add the full range of segmentation effects to my local installation?</p>
<p>Thank you,<br>
Hadi.</p>

---

## Post #2 by @jamesobutler (2020-10-21 14:27 UTC)

<aside class="quote quote-modified" data-post="1" data-topic="9233">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sunderlandkyl/48/79987_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/new-segment-editor-effect-local-threshold/9233">New Segment Editor effect: Local threshold</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Local threshold, a new semi-automatic segmentation method, has been added to the Segment Editor. It is available in both the 4.11.0 and 4.10.2 releases through the SegmentEditorExtraEffects extension. This effect adds connected voxels to segments that are within a specified threshold, and attempts to prevent leaks into other structures through small connecting regions. The result is similar to that of the “Level trace” effect in that it delineates a region within a certain threshold value, howev…
  </blockquote>
</aside>

<p>As indicated in the above linked post, the “Local Threshold” Segment Editor effect is available through the SegmentEditorExtraEffects extension. For info about installing extensions see <a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#extensions" class="inline-onebox" rel="noopener nofollow ugc">Getting Started — 3D Slicer documentation</a></p>

---
