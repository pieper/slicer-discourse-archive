---
topic_id: 24589
title: "Hollow Sphere Dynamic Modeler"
date: 2022-08-01
url: https://discourse.slicer.org/t/24589
---

# Hollow sphere: Dynamic modeler

**Topic ID**: 24589
**Date**: 2022-08-01
**URL**: https://discourse.slicer.org/t/hollow-sphere-dynamic-modeler/24589

---

## Post #1 by @AMK (2022-08-01 10:51 UTC)

<p>Hi,</p>
<p>I am trying to create a hollow sphere. For this I was trying to use the dynamic modeler tools option of ‘hollow’. I had expected that it would create a shell of the specified thickness. Instead it creates another model which just gets shifted by the specified thickness. I have attached the screenshot. Incase there is another option for creating a hollow sphere, please let me know.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/71f5f43d5f73a65d92e6c3451a2f3f9b284a18f2.png" data-download-href="/uploads/short-url/gg8Ujx1TXda03J0pApMdQJj7AeC.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/71f5f43d5f73a65d92e6c3451a2f3f9b284a18f2_2_690x300.png" alt="image" data-base62-sha1="gg8Ujx1TXda03J0pApMdQJj7AeC" width="690" height="300" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/71f5f43d5f73a65d92e6c3451a2f3f9b284a18f2_2_690x300.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/71f5f43d5f73a65d92e6c3451a2f3f9b284a18f2_2_1035x450.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/71f5f43d5f73a65d92e6c3451a2f3f9b284a18f2_2_1380x600.png 2x" data-dominant-color="858384"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">3840×1670 402 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thanks</p>

---

## Post #2 by @AMK (2022-08-01 11:17 UTC)

<p>I found the problem. It was an ordering error. I need to first make a hollow and then a plane cut.</p>

---
