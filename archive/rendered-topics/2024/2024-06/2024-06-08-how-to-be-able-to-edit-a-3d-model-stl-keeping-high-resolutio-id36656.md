---
topic_id: 36656
title: "How To Be Able To Edit A 3D Model Stl Keeping High Resolutio"
date: 2024-06-08
url: https://discourse.slicer.org/t/36656
---

# How to be able to edit a 3D Model (.stl) keeping high resolution of the output

**Topic ID**: 36656
**Date**: 2024-06-08
**URL**: https://discourse.slicer.org/t/how-to-be-able-to-edit-a-3d-model-stl-keeping-high-resolution-of-the-output/36656

---

## Post #1 by @MAXFAXSURGEON (2024-06-08 14:21 UTC)

<p>Hi everyone in this great forum,<br>
I need to modify an .stl file in form of 3D model to be used in another software for orthognathic virtual planning. When I loaded the 3D model to generate a master volume to be then opened in segment editor and when using the erase option the model lost its resolution as You can see this on the image below:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/2994ad8e2df19def73e3c61eb29703ce77fbd991.jpeg" data-download-href="/uploads/short-url/5VQ7h0Jj5336HvTWMNPk1k6TrMt.jpeg?dl=1" title="090560e0c23eb4ddf4d966273ce2866" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/2994ad8e2df19def73e3c61eb29703ce77fbd991_2_519x500.jpeg" alt="090560e0c23eb4ddf4d966273ce2866" data-base62-sha1="5VQ7h0Jj5336HvTWMNPk1k6TrMt" width="519" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/2994ad8e2df19def73e3c61eb29703ce77fbd991_2_519x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/2994ad8e2df19def73e3c61eb29703ce77fbd991_2_778x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/2994ad8e2df19def73e3c61eb29703ce77fbd991.jpeg 2x" data-dominant-color="BEC2CF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">090560e0c23eb4ddf4d966273ce2866</span><span class="informations">973×936 82.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
So, is there any option to be able to modify the 3D Model (cutting unneeded parts) having the output 3D .STL Model with high resolution? Would highly appreciate any support.<br>
Thank you so much in advance.<br>
I tried also to use the Dynamic Modeler  but I do not know how to apply the cutting tools in this module.</p>

---

## Post #2 by @lassoan (2024-06-09 03:57 UTC)

<p>You can edit STL files without losing any relevant details (memory usage and computation time depends on the size of the smallest details need to be preserved). See step-by-step instructions for <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#import-an-existing-segmentation-from-model-surface-mesh-file">importing</a> and <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#editing-a-segmentation-imported-from-model-surface-mesh-file">editing</a>.</p>

---
