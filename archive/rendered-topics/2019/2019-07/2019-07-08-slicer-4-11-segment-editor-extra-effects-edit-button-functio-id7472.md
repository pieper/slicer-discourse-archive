---
topic_id: 7472
title: "Slicer 4 11 Segment Editor Extra Effects Edit Button Functio"
date: 2019-07-08
url: https://discourse.slicer.org/t/7472
---

# Slicer 4.11 Segment Editor extra effects edit button functionality error

**Topic ID**: 7472
**Date**: 2019-07-08
**URL**: https://discourse.slicer.org/t/slicer-4-11-segment-editor-extra-effects-edit-button-functionality-error/7472

---

## Post #1 by @RMR54 (2019-07-08 20:13 UTC)

<p>In Slicer 4.10.2, after a segmentation is added to 3D volume, and then adding a segment, say using Draw tube effect, then when clicking on "Edit’ button, the delete button besides “Fiducial Placement:” label (which allows removal of last placed point, or removal of all markups), becomes enabled. In Slicer 4.11, the delete button however doesn’t become enabled until one of the following actions take place:</p>
<ul>
<li>cursor is moved towards proximity of a markup</li>
<li>another markup is added to the segment</li>
<li>position of existing markup is modified</li>
</ul>

---

## Post #2 by @lassoan (2019-07-09 05:02 UTC)

<p>Good catch. I’ve fixed the issue. Button states should be updated correctly in Slicer Preview Releases r28365 or later.</p>

---

## Post #3 by @RMR54 (2019-07-09 21:58 UTC)

<p>Thanks for the fix and update <a class="mention" href="/u/lassoan">@lassoan</a>!</p>

---
