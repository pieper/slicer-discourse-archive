---
topic_id: 27312
title: "Hide 2D Segment From Showing In Certain Slice Views"
date: 2023-01-17
url: https://discourse.slicer.org/t/27312
---

# Hide 2D Segment from Showing in Certain Slice Views

**Topic ID**: 27312
**Date**: 2023-01-17
**URL**: https://discourse.slicer.org/t/hide-2d-segment-from-showing-in-certain-slice-views/27312

---

## Post #1 by @xerox (2023-01-17 21:53 UTC)

<p>Hi,</p>
<p>I currently have created a 2D segmentation algorithm in Python and have set my segmentations similar to how it is done in <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#read-and-write-a-segment-as-a-numpy-array" rel="noopener nofollow ugc">this code</a>. Because my code is in 2D however and only segments based on the axial view, I want to hide any segment markups from the sagittal and coronal view as those segments don’t have any meaning. Is there a way to do this perhaps by modifying the voxel array or something similar? Thanks for the help in advance!</p>

---

## Post #2 by @Sunderlandkyl (2023-01-18 01:39 UTC)

<p>You can make nodes visible only in specific views using  <a href="https://apidocs.slicer.org/master/classvtkMRMLDisplayNode.html#a8fd9a8d62109f08b3720edc8e174a546" rel="noopener nofollow ugc"><code>displayNode.SetViewNodeIDs</code></a>.</p>
<p>See an example here using Markups:<br>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#change-markup-point-list-display-properties" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#change-markup-point-list-display-properties</a></p>

---
