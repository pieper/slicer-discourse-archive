---
topic_id: 42732
title: "Green Slice Got An Empty Green Frame"
date: 2025-04-29
url: https://discourse.slicer.org/t/42732
---

# Green slice got an empty green frame

**Topic ID**: 42732
**Date**: 2025-04-29
**URL**: https://discourse.slicer.org/t/green-slice-got-an-empty-green-frame/42732

---

## Post #1 by @Derek_Wang (2025-04-29 03:40 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/49d7033a79ef7727441087ce4587949aae00a7ca.jpeg" data-download-href="/uploads/short-url/axdw6bj7Jk6HzmmxuYNwvyepmVc.jpeg?dl=1" title="9e92b8818d2c15b0eff3803996bb6e1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/49d7033a79ef7727441087ce4587949aae00a7ca_2_690x462.jpeg" alt="9e92b8818d2c15b0eff3803996bb6e1" data-base62-sha1="axdw6bj7Jk6HzmmxuYNwvyepmVc" width="690" height="462" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/49d7033a79ef7727441087ce4587949aae00a7ca_2_690x462.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/49d7033a79ef7727441087ce4587949aae00a7ca.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/49d7033a79ef7727441087ce4587949aae00a7ca.jpeg 2x" data-dominant-color="9697BE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">9e92b8818d2c15b0eff3803996bb6e1</span><span class="informations">797×534 76.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
When I used Blender 4.4 to update the green image slice transformation matrix, it presents an empty green frame around image slice, is it possible to remove the green frame in 3D Slicer? Thanks a lot!</p>

---

## Post #2 by @Derek_Wang (2025-04-29 05:14 UTC)

<p>Got the solution as below,<br>
slice_display_node = sliceLogic.GetSliceDisplayNode()<br>
slice_display_node.SetVisibility2D(False)<br>
slice_display_node.SetSliceIntersectionOpacity(0.0)</p>

---
