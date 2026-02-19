---
topic_id: 28273
title: "The Voxel Size In Igt Volume Reconstruction"
date: 2023-03-10
url: https://discourse.slicer.org/t/28273
---

# The voxel size in IGT Volume Reconstruction

**Topic ID**: 28273
**Date**: 2023-03-10
**URL**: https://discourse.slicer.org/t/the-voxel-size-in-igt-volume-reconstruction/28273

---

## Post #1 by @LV52 (2023-03-10 08:49 UTC)

<p>I have used the openigtlink to transmit the ultrasound image and 3d position into 3d slicer.<br>
Then I uesd IGT Volume Reconstruction to reconstruct the 3d ultrasound volume.</p>
<p>In the Image volume the voxel size(image spacing) is 0.1244x0.1244x0.1mm, which is consistent with my original ultrasound images and physical size.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ffba9705f4048189c13eb8ffcc698c111b5af09f.png" alt="微信截图_20230310155646" data-base62-sha1="AuhwmMtOKUU7YEQSbG1I662DTtl" width="553" height="318"><br>
<br><br>
When I switch to “Volume Reconstruction” model, there also has another “output spacing” parameter, with the defalut 1x1x1.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/63b931d0a5f14f034e98c733c0eefa334e1e4c11.png" data-download-href="/uploads/short-url/eec2Vg0E1jUzhAlo2fUFPmX9RGF.png?dl=1" title="微信截图_20230310155731" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/63b931d0a5f14f034e98c733c0eefa334e1e4c11.png" alt="微信截图_20230310155731" data-base62-sha1="eec2Vg0E1jUzhAlo2fUFPmX9RGF" width="511" height="500" data-dominant-color="F4F1F1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">微信截图_20230310155731</span><span class="informations">557×544 11.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<br></p>
<p>If I used the defalut parameter to reconstruct the 3d ultrasound volume, the voxel size of volume will change to 1x1x1mm, which is not consistent with my original ultrasound images and physical size.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3f4ae30aa6c26abcc9c224b9178af46614095aa.png" alt="微信截图_20230310155839" data-base62-sha1="uf2Yf5O9JcKxtJlt1eeopYnZ8WS" width="541" height="294"><br>
<br></p>
<p>So, I decided to change the “output spacing” parameter in “Volume Reconstruction” model again.<br>
But the “output spacing” parameter seems like only support to two decimal places.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dcc56ae18e5e67499fd00c33266ba895b24e1599.png" data-download-href="/uploads/short-url/vv20wRUBfaSW2fo7625GRkrAPPz.png?dl=1" title="微信截图_20230310155803" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dcc56ae18e5e67499fd00c33266ba895b24e1599.png" alt="微信截图_20230310155803" data-base62-sha1="vv20wRUBfaSW2fo7625GRkrAPPz" width="502" height="500" data-dominant-color="F4F1F1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">微信截图_20230310155803</span><span class="informations">558×555 11.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/72a4b60bed1de59bd252a3a8bd054735c656040b.png" alt="微信截图_20230310155907" data-base62-sha1="gmbk3PuNLXoMF9H5rNErHdnlhdV" width="543" height="286"><br>
<br><br>
Is there has any method to reconstruct the 3d ultrasound volume with correct voxel size?<br>
Thanks!</p>

---
