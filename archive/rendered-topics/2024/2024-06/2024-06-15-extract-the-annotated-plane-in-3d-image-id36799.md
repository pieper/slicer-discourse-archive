# Extract the annotated plane in 3D image

**Topic ID**: 36799
**Date**: 2024-06-15
**URL**: https://discourse.slicer.org/t/extract-the-annotated-plane-in-3d-image/36799

---

## Post #1 by @musheng0624 (2024-06-15 03:55 UTC)

<p>I am doing a view plane localization research. First I need to annotate the plane as the ground-truth. I use the “Markups” module of 3D Slicer to annotate the plane. But after i annotated the plane and export the json file. I used the “baseToNode” as the rotation matrix to extract the annotated plane, but i can not get the annotated plane. How can i get the annotated plane using python? Should I using the key “center” and “normal” in the json file?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/114ba23ab019467b2d4e784a94d2c921bea2919f.jpeg" data-download-href="/uploads/short-url/2t0a0GKtHVXw0JPEBE3y6S7zYeP.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/114ba23ab019467b2d4e784a94d2c921bea2919f_2_690x408.jpeg" alt="image" data-base62-sha1="2t0a0GKtHVXw0JPEBE3y6S7zYeP" width="690" height="408" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/114ba23ab019467b2d4e784a94d2c921bea2919f_2_690x408.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/114ba23ab019467b2d4e784a94d2c921bea2919f_2_1035x612.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/114ba23ab019467b2d4e784a94d2c921bea2919f_2_1380x816.jpeg 2x" data-dominant-color="A2969D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1137 155 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This is my annotate plane!</p>

---

## Post #2 by @lassoan (2024-06-15 05:12 UTC)

<p>Yes, you can use <code>center</code> and <code>normal</code> properties in the json file. If you want to create a markup plane JSON file then you can follow this <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#create-markup-plane-json-file-outside-slicer">example in the script repository</a>.</p>

---
