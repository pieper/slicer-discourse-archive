---
topic_id: 36681
title: "How To Customize The Number On The Line Markups"
date: 2024-06-10
url: https://discourse.slicer.org/t/36681
---

# How to customize the number on the line markups?

**Topic ID**: 36681
**Date**: 2024-06-10
**URL**: https://discourse.slicer.org/t/how-to-customize-the-number-on-the-line-markups/36681

---

## Post #1 by @Cavers_Chen (2024-06-10 13:03 UTC)

<p>Hi!<br>
Recently, I tried to use a line to represent the relationship between segmentation pairs. However, I want to display the custom number. Is there a way to achieve this goal? Displaying the description would be great too.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5bc1ce292f616caa5ff7d8ec5e21763149f15312.png" data-download-href="/uploads/short-url/d5IFTIxWuG0okRaxMV4RIRhkzC2.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5bc1ce292f616caa5ff7d8ec5e21763149f15312_2_690x248.png" alt="image" data-base62-sha1="d5IFTIxWuG0okRaxMV4RIRhkzC2" width="690" height="248" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5bc1ce292f616caa5ff7d8ec5e21763149f15312_2_690x248.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5bc1ce292f616caa5ff7d8ec5e21763149f15312_2_1035x372.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5bc1ce292f616caa5ff7d8ec5e21763149f15312_2_1380x496.png 2x" data-dominant-color="26292A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1636×589 49.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2024-06-10 13:16 UTC)

<p>Currently, node name and measurements are displayed in the node properties label. You can disable length measurement to hide the length value. You can set a desired node name or add custom static measurements to display custom text there.</p>
<p><a href="https://github.com/Slicer/Slicer/blob/2b0853911e59203b171505ee48a6f05c8c437253/Modules/Loadable/Markups/MRML/vtkMRMLMarkupsNode.cxx#L2899">Node description is automatically updated based on measurements</a>, so we would need to change the design (for example, introduce an additional node property to store measurement results string and change the subject hierarchy tree to be able to show that). It is doable, but since there are other ways to display custom text in the markup node properties label, this design change does not seem necessary.</p>

---
