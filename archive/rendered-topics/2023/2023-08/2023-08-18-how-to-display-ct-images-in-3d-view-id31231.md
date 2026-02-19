---
topic_id: 31231
title: "How To Display Ct Images In 3D View"
date: 2023-08-18
url: https://discourse.slicer.org/t/31231
---

# How to display CT images in 3D view

**Topic ID**: 31231
**Date**: 2023-08-18
**URL**: https://discourse.slicer.org/t/how-to-display-ct-images-in-3d-view/31231

---

## Post #1 by @miragevideo (2023-08-18 20:00 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1dc393f08c0cb49e116786d856da3de3d27880a0.jpeg" data-download-href="/uploads/short-url/4fiRXzWFCE2moB8XlcHRii0ePHq.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1dc393f08c0cb49e116786d856da3de3d27880a0_2_690x448.jpeg" alt="image" data-base62-sha1="4fiRXzWFCE2moB8XlcHRii0ePHq" width="690" height="448" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1dc393f08c0cb49e116786d856da3de3d27880a0_2_690x448.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1dc393f08c0cb49e116786d856da3de3d27880a0_2_1035x672.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1dc393f08c0cb49e116786d856da3de3d27880a0_2_1380x896.jpeg 2x" data-dominant-color="686874"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1247 155 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I don’t get anything in the 3D window. What do I need to do?</p>

---

## Post #2 by @lassoan (2023-08-18 20:10 UTC)

<p>You can show slice views in 3D by clicking the <a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#view-data">eye icon in the slice view controller</a>.</p>
<p>You can show CT images using volume rendering by drag-and-dropping the image from the data tree into the 3D view.</p>
<p>You can display specific structures in 3D by segmenting them. For example, you can use <a href="https://github.com/lassoan/SlicerTotalSegmentator#totalsegmentator">TotalSegmentator extension</a> to segment 100+ structures (all major bones, organs, larger vessels, etc.) fully automatically.</p>

---
