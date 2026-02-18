# Deep Vein Segmentation And 3D Reconstruction

**Topic ID**: 14027
**Date**: 2020-10-14
**URL**: https://discourse.slicer.org/t/deep-vein-segmentation-and-3d-reconstruction/14027

---

## Post #1 by @Sedra_Mulki (2020-10-14 01:34 UTC)

<p>Hello</p>
<p>I am working on 3D slicer to extract deep vein in legs by using MRI images.</p>
<p>And I used 2 way to get the result:</p>
<p>1- First way I apply Level set segmentation from Vascular Modeling Toolkit Model, <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/4132253f54e57b0eb1706a20033c5744889aaabf.jpeg" data-download-href="/uploads/short-url/9iKtfE5BgQnR4WeMLiPPIwiZOSH.jpeg?dl=1" title="SceneView" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4132253f54e57b0eb1706a20033c5744889aaabf_2_690x468.jpeg" alt="SceneView" data-base62-sha1="9iKtfE5BgQnR4WeMLiPPIwiZOSH" width="690" height="468" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4132253f54e57b0eb1706a20033c5744889aaabf_2_690x468.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4132253f54e57b0eb1706a20033c5744889aaabf_2_1035x702.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/4132253f54e57b0eb1706a20033c5744889aaabf.jpeg 2x" data-dominant-color="4A4A55"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SceneView</span><span class="informations">1323×899 267 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>2- second way I apply Region Growing Model,<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/72fb59fd0e1fafe258318ce155fac5d9d30792dd.jpeg" data-download-href="/uploads/short-url/gpaWSVJ71eaOWGoYDaDiy4Pi5BP.jpeg?dl=1" title="2020-06-04-Scene" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/72fb59fd0e1fafe258318ce155fac5d9d30792dd_2_690x468.jpeg" alt="2020-06-04-Scene" data-base62-sha1="gpaWSVJ71eaOWGoYDaDiy4Pi5BP" width="690" height="468" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/72fb59fd0e1fafe258318ce155fac5d9d30792dd_2_690x468.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/72fb59fd0e1fafe258318ce155fac5d9d30792dd_2_1035x702.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/72fb59fd0e1fafe258318ce155fac5d9d30792dd.jpeg 2x" data-dominant-color="464850"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2020-06-04-Scene</span><span class="informations">1323×899 232 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>My first question is: this model that I applied is ok for segmentation  of deep vein.<br>
My second question is: I try to get more accuracy result, So there is model or way in 3d slicer to calculate the accuracy or (error)</p>
<p>Thank you,</p>
<p>Sidra</p>

---

## Post #2 by @lassoan (2020-10-14 02:02 UTC)

<p>There is no such thing as a perfect segmentation, only that is suitable for a specific clinical purpose. What is your goal? What information would you like to extract from the image? What are your accuracy requirements?</p>

---

## Post #3 by @Sedra_Mulki (2020-10-16 19:09 UTC)

<p>Hello,</p>
<p>Thank you for your reply.</p>
<p>My goal is to segment MRI images for deep vein in legs to get the boundary of vein in each image , after that reconstruct the vein by using boundaries in all images.<br>
I applied Level Set Segmentation from VMTK model to get the geometry of deep vein in knee.<br>
Also I applied Simple Region Growing Segmentation for same previous reason.<br>
So I need to know how I can calculate the error between real vein and vein that I extract?<br>
For example the diameter/volume of vein that I extract is equal to diameter/volume of real vein or how much the vein that I extract is match to real vein?<br>
What are the criteria to detect the error?</p>

---
