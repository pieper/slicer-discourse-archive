# Enhancing rendered volume

**Topic ID**: 29487
**Date**: 2023-05-16
**URL**: https://discourse.slicer.org/t/enhancing-rendered-volume/29487

---

## Post #1 by @KSL (2023-05-16 07:15 UTC)

<p>Hello friends, I came across a video on Youtube by Amira Software that rendered the spine with fine details of the vertebrae (labelleb 1, in the image). When I try to obtain the fine details (labelled 2, in the image) using slicer 5.3, I could not obtain the same. Is there any technique/setting to obtain such detailed rendered image using 3d slicer<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c427b2a1ba940e810a4f20e3db36d5a79390e10e.jpeg" data-download-href="/uploads/short-url/rZgDrYuFxYzAOCA6MclfZXL6crQ.jpeg?dl=1" title="SP" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c427b2a1ba940e810a4f20e3db36d5a79390e10e_2_605x499.jpeg" alt="SP" data-base62-sha1="rZgDrYuFxYzAOCA6MclfZXL6crQ" width="605" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c427b2a1ba940e810a4f20e3db36d5a79390e10e_2_605x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c427b2a1ba940e810a4f20e3db36d5a79390e10e_2_907x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c427b2a1ba940e810a4f20e3db36d5a79390e10e.jpeg 2x" data-dominant-color="A6A097"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SP</span><span class="informations">1192×985 86 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
. Thank you.</p>

---

## Post #2 by @rbumm (2023-05-16 08:04 UTC)

<p>Are you using the same data in 3d Slicer?</p>

---

## Post #3 by @RafaelPalomar (2023-05-16 17:36 UTC)

<p>(1) looks to me like a 3D surface model from a segmentation, while (2) looks like a volume rendering. If this is true, the rendering technique wouldn’t be the same. Secondly, with volume rendering you might not have the fine control to capture small features as you would if you segment your model. You may want to obtain the segmentation and do surface rendering, instead of volume rendering.</p>

---

## Post #4 by @lassoan (2023-05-16 18:59 UTC)

<p>Yes, it looks like the left may be surface rendering; or volume rendering with a steep (step-like) Scalar Opacity Mapping function. If you loaded the same data set in Slicer and in the other software then you can adjust the shape of Scalar Opacity Mapping function (in Volume rendering module / Advanced section) to get the same kind of appearance.</p>
<p>Shape of the vertebrae look different in the left and right images, so if you loaded the same data set then there might be something wrong with how you exported the data set or imported it to Slicer. What is the image spacing (voxel size) of your image? What is the image spacing displayed in Volumes module / Volume information section?</p>

---

## Post #5 by @KSL (2023-05-19 09:19 UTC)

<p>Sir, the image, “labelled 1”, is a screenshot from Youtube channel by Thermo Fisher Scientific. The image, “labelled 2”, is my own data that I processed with Volume rendering on 3d slicer 5.3. using the preset uCT Bone 8 bit . I have no idea how the image is processed in Thermo Fisher Scientific but I am pretty sure the morphological details shown in images 1 and 2 are same. I want to know if there is any method to enhance the volume rendering in 3d slicer to obtain the same details like the image from Thermo Fisher Scientific. Thank you.</p>

---

## Post #6 by @KSL (2023-05-19 10:20 UTC)

<p>Sir, I do not know how to get information on the Voxel size and image spacing. However, after doing few changes in the advanced setting under Volume rendering, I obtain the following image.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e543be96405b20a138d118ad0f28fec80a5b3c4f.png" data-download-href="/uploads/short-url/wIatV9ZFZn4WKEGLBlqwB7OAeMn.png?dl=1" title="S3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e543be96405b20a138d118ad0f28fec80a5b3c4f_2_396x500.png" alt="S3" data-base62-sha1="wIatV9ZFZn4WKEGLBlqwB7OAeMn" width="396" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e543be96405b20a138d118ad0f28fec80a5b3c4f_2_396x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e543be96405b20a138d118ad0f28fec80a5b3c4f_2_594x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e543be96405b20a138d118ad0f28fec80a5b3c4f_2_792x1000.png 2x" data-dominant-color="CACCDD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">S3</span><span class="informations">798×1006 268 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #7 by @KSL (2023-05-19 10:41 UTC)

<p>Sir, I did segmentation using Total Segmentator module. How do I execute surface rendering on the segmented vertebrae?</p>

---
