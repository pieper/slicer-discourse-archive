---
topic_id: 35770
title: "Point On 2D Ct Slice Image To Ras Coordinate Transformation"
date: 2024-04-27
url: https://discourse.slicer.org/t/35770
---

# Point on 2D CT slice image to RAS coordinate transformation

**Topic ID**: 35770
**Date**: 2024-04-27
**URL**: https://discourse.slicer.org/t/point-on-2d-ct-slice-image-to-ras-coordinate-transformation/35770

---

## Post #1 by @joanne40226 (2024-04-27 12:57 UTC)

<p>Hi community,<br>
I encounter problems when doing point on 2D CT slice image to RAS coordinate.</p>
<p>I have screen shot an 2D CT image as shown below. i check some imformation for example the actual size of the image in mm is : 649.092624007295, 314.6698141861267(mm) and the sliceToRAS is [-1.0 0.0 0.0<br>
0.0 -0.6712189288498026 -0.7412591649036953<br>
0.0 -0.7412591649036953 0.6712189288498026 ]<br>
also, the offset of the slice is -184.6262(mm)，and the offset of the 1st image of the slice is 424.6262(mm). also the Image Origin: (204.5mm, 200mm, -361mm)<br>
now on the 2D CT image, i want to transfer the point (716, 473) in pixel to {RAS}. the answer is R=−9.352mm,A=41.234mm, 𝑆=−229.525mm bu measurement.<br>
can anyone tell me how the calculation should be when doing this kind of 2D-3D coordinate transformation?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/29de6aba2834e08a06510c4b36c359288bede7d2.jpeg" data-download-href="/uploads/short-url/5Yo6lgfzC6R0U86a5c3nB23sDXs.jpeg?dl=1" title="screenshot1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/29de6aba2834e08a06510c4b36c359288bede7d2_2_690x334.jpeg" alt="screenshot1" data-base62-sha1="5Yo6lgfzC6R0U86a5c3nB23sDXs" width="690" height="334" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/29de6aba2834e08a06510c4b36c359288bede7d2_2_690x334.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/29de6aba2834e08a06510c4b36c359288bede7d2_2_1035x501.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/29de6aba2834e08a06510c4b36c359288bede7d2_2_1380x668.jpeg 2x" data-dominant-color="3C3B3A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">screenshot1</span><span class="informations">1412×684 67 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>thank you for the time.</p>

---
