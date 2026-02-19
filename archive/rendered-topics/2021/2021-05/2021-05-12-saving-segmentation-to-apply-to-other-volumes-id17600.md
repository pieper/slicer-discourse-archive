---
topic_id: 17600
title: "Saving Segmentation To Apply To Other Volumes"
date: 2021-05-12
url: https://discourse.slicer.org/t/17600
---

# Saving segmentation to apply to other volumes

**Topic ID**: 17600
**Date**: 2021-05-12
**URL**: https://discourse.slicer.org/t/saving-segmentation-to-apply-to-other-volumes/17600

---

## Post #1 by @sravan953 (2021-05-12 17:40 UTC)

<p>Hello,</p>
<p>I have 2 registered NIFTI brain images. I performed skull stripping using the Swiss Skull Stripper extension, and converted the resulting binary label mask into a segmentation node. I saved this segmentation as a .seg.nrrd file.</p>
<p>Now, how do I apply this segment a new volume with this saved segmentation? By apply, I mean apply the skull stripping binary label mask to the new volume.</p>

---

## Post #2 by @lassoan (2021-05-13 05:04 UTC)

<p>You can use Mask volume effect in Segment Editor module to blank out region inside or outside a segment of any volume.</p>

---

## Post #3 by @sravan953 (2021-05-13 13:28 UTC)

<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a>, that worked!</p>

---
