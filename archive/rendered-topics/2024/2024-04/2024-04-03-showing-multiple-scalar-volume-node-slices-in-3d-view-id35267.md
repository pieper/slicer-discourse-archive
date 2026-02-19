---
topic_id: 35267
title: "Showing Multiple Scalar Volume Node Slices In 3D View"
date: 2024-04-03
url: https://discourse.slicer.org/t/35267
---

# Showing Multiple Scalar Volume Node Slices in 3D View 

**Topic ID**: 35267
**Date**: 2024-04-03
**URL**: https://discourse.slicer.org/t/showing-multiple-scalar-volume-node-slices-in-3d-view/35267

---

## Post #1 by @adavis (2024-04-03 22:26 UTC)

<p>Hello,</p>
<p>I am relatively new to Slicer and am trying to implement code that will display multiple scalar volume nodes’ slices in the 3D view. My initial thought was to replicate what clicking the eye icon in the Data Module subject hierarchy does; however, even this only allows one vtkMRMLScalarVolumeNode’s slices to be shown at a time in the 3D view. I think this has something to do with the slice views as when I change the layout to more windows and set particular volumes to particular slice views, I can achieve the effect I want as pictured below (i.e. I can see axial slices from both the MRI head sample volume and the added volume at the same time in the 3D view).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e3b8e980edb4fe713b1e23ef21a948b1d01a95b6.jpeg" data-download-href="/uploads/short-url/wuwyBGbAOGgE6p2IRhv79Qf8eDs.jpeg?dl=1" title="Screenshot 2024-04-03 at 2.30.34 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e3b8e980edb4fe713b1e23ef21a948b1d01a95b6_2_690x383.jpeg" alt="Screenshot 2024-04-03 at 2.30.34 PM" data-base62-sha1="wuwyBGbAOGgE6p2IRhv79Qf8eDs" width="690" height="383" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e3b8e980edb4fe713b1e23ef21a948b1d01a95b6_2_690x383.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e3b8e980edb4fe713b1e23ef21a948b1d01a95b6_2_1035x574.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e3b8e980edb4fe713b1e23ef21a948b1d01a95b6_2_1380x766.jpeg 2x" data-dominant-color="3C3A41"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-04-03 at 2.30.34 PM</span><span class="informations">1920×1066 100 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>How can I achieve this through Python? Do I need to make 2D slice views of both volumes and then display those rather than trying to display the volume in its entirety? If so, how can I do this?</p>

---
