# Mismatch of image view and its actual dimensions

**Topic ID**: 13337
**Date**: 2020-09-04
**URL**: https://discourse.slicer.org/t/mismatch-of-image-view-and-its-actual-dimensions/13337

---

## Post #1 by @a10227 (2020-09-04 13:18 UTC)

<p>Good day,<br>
I noticed a mismatch between the image dimensions and its view in Slicer (the view is the same in other viewers as in Slicer). The dimension of the image is 512<em>233. On the left side is the image view in Slicer, on the right side is its view after I read it in python, converted it into an array and displayed it. It can be seen that the dimensions on the left side don’t correspond to 512</em>233 (the width should be &gt; 2 times bigger than height but it is not), on the other hand, on the right image the image seems to have the correct dimensions but it seems to be distorted also (I am not sure if it’s really distorted or not)<br>
Could you please tell me, why the image is displayed in slicer in such a way and what parameters are responsible for the mismatch between the actual dimensions and the dimensions of the view in Slicer?<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f5b3400347f75faadf83bfe80b4b7176d42f346.jpeg" data-download-href="/uploads/short-url/92ttUuKAvyD1kND0aMFganTtyYe.jpeg?dl=1" title="photo_2020-09-04_13-11-46" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3f5b3400347f75faadf83bfe80b4b7176d42f346_2_690x187.jpeg" alt="photo_2020-09-04_13-11-46" data-base62-sha1="92ttUuKAvyD1kND0aMFganTtyYe" width="690" height="187" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3f5b3400347f75faadf83bfe80b4b7176d42f346_2_690x187.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f5b3400347f75faadf83bfe80b4b7176d42f346.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f5b3400347f75faadf83bfe80b4b7176d42f346.jpeg 2x" data-dominant-color="505560"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">photo_2020-09-04_13-11-46</span><span class="informations">1032×281 30.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2020-09-04 13:23 UTC)

<p>Hi -</p>
<p>Pixel dimensions are not the same as world space, and the spacing between pixel center can be different in different directions.</p>
<p>See this page for more info:</p>
<p><a href="https://www.slicer.org/wiki/Coordinate_systems" class="onebox" target="_blank">https://www.slicer.org/wiki/Coordinate_systems</a></p>

---

## Post #3 by @a10227 (2020-09-04 14:29 UTC)

<p>thank you, the problem is solved by using make_isotropic function from <a href="https://github.com/InsightSoftwareConsortium/SimpleITK-Notebooks/blob/master/Python/05_Results_Visualization.ipynb" rel="nofollow noopener">sitk notebook</a>, but your answer is also helpful.<br>
<a href="https://discourse.itk.org/t/mismatch-of-image-view-and-its-actual-dimensions/3433/2?u=a10227" rel="nofollow noopener">Here is the link to another helpful answer</a></p>

---
