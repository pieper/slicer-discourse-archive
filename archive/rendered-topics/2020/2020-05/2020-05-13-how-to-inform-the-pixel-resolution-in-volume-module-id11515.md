# How to inform the pixel resolution in Volume module?

**Topic ID**: 11515
**Date**: 2020-05-13
**URL**: https://discourse.slicer.org/t/how-to-inform-the-pixel-resolution-in-volume-module/11515

---

## Post #1 by @Acantharia (2020-05-13 09:01 UTC)

<p>Dear all,<br>
I have a stack of TIFF images with a pixel resolution of 8nmx8nmx8nm. In order to calculate the volume of different segments in nm3 (and so making the conversion between voxel numbers and nm3) using segment statistics, Do i need to provide the resolution info in the “pixel spacing”???. it is not 1mm by default but 0.000008?<br>
Thank you<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/dab45c39ee9f56479473f1e53bce9582e3088803.jpeg" data-download-href="/uploads/short-url/vcKvxaUzsM0f9qqXVrXtd3T1tjJ.jpeg?dl=1" title="Help-Slicer-volume" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dab45c39ee9f56479473f1e53bce9582e3088803_2_305x500.jpeg" alt="Help-Slicer-volume" data-base62-sha1="vcKvxaUzsM0f9qqXVrXtd3T1tjJ" width="305" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dab45c39ee9f56479473f1e53bce9582e3088803_2_305x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dab45c39ee9f56479473f1e53bce9582e3088803_2_457x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/dab45c39ee9f56479473f1e53bce9582e3088803.jpeg 2x" data-dominant-color="F0F0F0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Help-Slicer-volume</span><span class="informations">588×963 89.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @muratmaga (2020-05-13 15:06 UTC)

<p>Yes, you can correct the image spacing in volumes module.</p>
<p>But that given that extremely small value of voxel size, you might be better off setting the default length unit to nanometer. Edit-&gt;Application Settings-&gt;Units and expand the advanced option. Should work, but this is not a heavily tested feature.</p>

---

## Post #3 by @Acantharia (2020-05-14 06:41 UTC)

<p>Thank you muratmaga for your response and information. I changed the unit in nm but it did not change in the volume information panel (still in mm). I am not sure I understand the meaning of “image spacing”.  sorry<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/1316ac4c78ef20adbe8b6cf5249d3df5cadcbf21.jpeg" data-download-href="/uploads/short-url/2IREdCYqNZcOmLjFh6bLhyrzqM1.jpeg?dl=1" title="unit change" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1316ac4c78ef20adbe8b6cf5249d3df5cadcbf21_2_447x500.jpeg" alt="unit change" data-base62-sha1="2IREdCYqNZcOmLjFh6bLhyrzqM1" width="447" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1316ac4c78ef20adbe8b6cf5249d3df5cadcbf21_2_447x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1316ac4c78ef20adbe8b6cf5249d3df5cadcbf21_2_670x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/1316ac4c78ef20adbe8b6cf5249d3df5cadcbf21.jpeg 2x" data-dominant-color="F5F5F5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">unit change</span><span class="informations">715×799 80.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Best,</p>

---

## Post #4 by @muratmaga (2020-05-14 07:01 UTC)

<p>You may have to restart Slicer for changes to take place. In the version I use (5/12, it shows units as nm in the volume module after applying this setting and restarting. After this change has taken place, edit the <code>Image Spacing</code> tab of the volume module to be 8x8x8 (There is no setting called pixel spacing).</p>

---

## Post #5 by @Acantharia (2020-05-14 07:10 UTC)

<p>I restarted and indeed “nm” scale is now there. It is now 10000nm<em>10000nm</em>10000nm. But when I change to 8nm 8nm 8nm, I lost my “images” from the different views. my image dimensions are 1071<em>1152</em>927…<br>
Thanks</p>

---

## Post #6 by @muratmaga (2020-05-14 19:21 UTC)

<p>Hit the center field of view button</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/01dc85c4d7a8468f7f8d4bf10004f91e6b3bc1a8.png" alt="image" data-base62-sha1="gsWzTC3iPoSIAwCCJ1xqYhUAyc" width="211" height="69"></p>

---
