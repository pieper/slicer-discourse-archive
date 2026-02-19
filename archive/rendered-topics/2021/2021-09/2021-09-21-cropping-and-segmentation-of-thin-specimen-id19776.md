---
topic_id: 19776
title: "Cropping And Segmentation Of Thin Specimen"
date: 2021-09-21
url: https://discourse.slicer.org/t/19776
---

# Cropping and Segmentation of Thin Specimen

**Topic ID**: 19776
**Date**: 2021-09-21
**URL**: https://discourse.slicer.org/t/cropping-and-segmentation-of-thin-specimen/19776

---

## Post #1 by @CSULB_MammalLab (2021-09-21 05:17 UTC)

<p>Hello All,</p>
<p>I am working with pangolin study skins that were scanned as a bundle. I am looking to take thickness measurements at specific intervals of each study skin but often times I am unable to cleanly crop out each skin for observation. Since some skins have a very small gap between them and their neighbor, I am unable to crop out the skins I am not interested in without removing part of the skin that I am interested in.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e2549a359a28c6db260a344da055d3fb2cff3d07.jpeg" data-download-href="/uploads/short-url/widaq7ur2rUq5ydHJaA5RKhC88n.jpeg?dl=1" title="PangolinBundle" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e2549a359a28c6db260a344da055d3fb2cff3d07_2_690x240.jpeg" alt="PangolinBundle" data-base62-sha1="widaq7ur2rUq5ydHJaA5RKhC88n" width="690" height="240" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e2549a359a28c6db260a344da055d3fb2cff3d07_2_690x240.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e2549a359a28c6db260a344da055d3fb2cff3d07_2_1035x360.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e2549a359a28c6db260a344da055d3fb2cff3d07_2_1380x480.jpeg 2x" data-dominant-color="92898F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">PangolinBundle</span><span class="informations">1707×595 81.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6af342d08a1225d8e7fc9995a98684bc8f359b94.jpeg" data-download-href="/uploads/short-url/fg7NmnAwWllPaM14qn70L0U65XC.jpeg?dl=1" title="TopObscuringMid" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6af342d08a1225d8e7fc9995a98684bc8f359b94_2_690x361.jpeg" alt="TopObscuringMid" data-base62-sha1="fg7NmnAwWllPaM14qn70L0U65XC" width="690" height="361" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6af342d08a1225d8e7fc9995a98684bc8f359b94_2_690x361.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6af342d08a1225d8e7fc9995a98684bc8f359b94_2_1035x541.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6af342d08a1225d8e7fc9995a98684bc8f359b94_2_1380x722.jpeg 2x" data-dominant-color="B0A6A9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">TopObscuringMid</span><span class="informations">1897×994 134 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>To try to circumvent this issue I tried to use the Segment Editor and segment out the skin I am interested in utilizing the Brush and Fill Between Slices Tool. I was successful in cleaning up the scan, allowing me to use the crosshairs to find the scales I was going to measure, however I encountered an issue when it came time to measure the thickness. Due to the segmentation, when looking at the red slice view (the view that I will be using to take the thickness measurements with the Ruler tool), the scan is pixelated, making it very difficult to accurately record measurements. I am assuming that the issue either lies in my inexperience with Slicer (I am still very new to the program and working with scans in general), or with the thinness of the scales.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1d52af0f51639a826d437007288a6c4be39a9b6.jpeg" data-download-href="/uploads/short-url/tWgv4dShz10tiKmA4c6m9M9UJwO.jpeg?dl=1" title="SegmentEditor" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d1d52af0f51639a826d437007288a6c4be39a9b6_2_690x276.jpeg" alt="SegmentEditor" data-base62-sha1="tWgv4dShz10tiKmA4c6m9M9UJwO" width="690" height="276" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d1d52af0f51639a826d437007288a6c4be39a9b6_2_690x276.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d1d52af0f51639a826d437007288a6c4be39a9b6_2_1035x414.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d1d52af0f51639a826d437007288a6c4be39a9b6_2_1380x552.jpeg 2x" data-dominant-color="191B19"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SegmentEditor</span><span class="informations">1920×769 56.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Is there any way I can reduce the pixilation in the segmented volume? Or is there an alternative method I can use to crop the skins in a way that I won’t be eliminating part of my volume of interest? Is there a tool that works like the Cropping module but in reverse (create a ROI that will crop everything inside and make it not visible in the original volume rendering)?</p>
<p>Please let me know if any additional information is needed. Thank you!</p>

---

## Post #2 by @muratmaga (2021-09-21 05:51 UTC)

<p>Given the shape of those individual voxels (i.e, they are rectangular), I think you have anisotropic data (e.g., Z spacing is higher than XY spacing). Prior to segmentation you can use the CropVolume module and choose the “isotropic” spacing option which will circumvent this situation.  You can even choose a value less than 1.0 to subdivide the individual voxels. (e.g., value of 0.5 will divide a single voxel 8 voxels). However, this will increase your data 8 folds, so you may want to do this in a small region of your dataset as oppose to on the entire volume.</p>

---

## Post #3 by @CSULB_MammalLab (2021-09-21 06:36 UTC)

<p>Thank you for taking the time to respond!</p>
<p>I’ve attempted to fiddle around with the resolution on the Crop Volume Module as you’ve suggested but I am unsure if I am doing it correctly.</p>
<p>I have checked the box that says “Isotropic Spacing” and went as far down as 0.3x for the spacing scale. Are these the two things you suggested?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fe86a981cf80b1683e8bc24d14b4ab701bdba767.png" data-download-href="/uploads/short-url/AjDMXXxGMD5usuJMhr4xIe37AJV.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe86a981cf80b1683e8bc24d14b4ab701bdba767_2_357x500.png" alt="image" data-base62-sha1="AjDMXXxGMD5usuJMhr4xIe37AJV" width="357" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe86a981cf80b1683e8bc24d14b4ab701bdba767_2_357x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe86a981cf80b1683e8bc24d14b4ab701bdba767_2_535x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fe86a981cf80b1683e8bc24d14b4ab701bdba767.png 2x" data-dominant-color="373737"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">539×753 25 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If I did do it correctly, it seems like it had very limited, if any, success.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a95619b21be522592aaaf4602b9ae73132613ddf.jpeg" data-download-href="/uploads/short-url/oa1a1B9HxWMx58flMkvcm5v0WK3.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a95619b21be522592aaaf4602b9ae73132613ddf_2_690x294.jpeg" alt="image" data-base62-sha1="oa1a1B9HxWMx58flMkvcm5v0WK3" width="690" height="294" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a95619b21be522592aaaf4602b9ae73132613ddf_2_690x294.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a95619b21be522592aaaf4602b9ae73132613ddf_2_1035x441.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a95619b21be522592aaaf4602b9ae73132613ddf_2_1380x588.jpeg 2x" data-dominant-color="191A19"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×820 57 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Are there any other potential alternatives? Or should I rethink the way I am taking my measurements?</p>

---

## Post #4 by @mikebind (2021-09-21 07:31 UTC)

<p>I suspect that your segmentation is still based on the lower resolution version of the volume.  Either start over with a new segmentation and select he higher resolution version as the “Master Volume”, or to change the resolution of the existing segmentation to match the higher resolution, click the “Specify Geometry”  button (looks like a cube just to the right of the “Master Volume” selector, described in a bit more detail on <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html" rel="noopener nofollow ugc">this page, also see “Segmentation is not accurate enough” section there</a>) and select the higher resolution volume there.</p>

---

## Post #5 by @muratmaga (2021-09-21 16:14 UTC)

<aside class="quote no-group" data-username="CSULB_MammalLab" data-post="3" data-topic="19776">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/f1d935/48.png" class="avatar"> CSULB_MammalLab:</div>
<blockquote>
<p>I have checked the box that says “Isotropic Spacing” and went as far down as 0.3x for the spacing scale. Are these the two things you suggested?</p>
</blockquote>
</aside>
<p>You should see a difference since you increased the volume of your data 300X (compare the Cropped Volume dimensions to that of Input volume). This might be too much for your computer to handle. So it is possible that it actually didn’t complete successfully.</p>
<p>So go a bit slow first, check only the isotropic scaling, and keep the scale at 1.0. Then as <a class="mention" href="/u/mikebind">@mikebind</a> mentioned, make sure you create new segmentation with the master volume set as <strong>18282 Second Quadrant cropped cropped</strong> (which would be the output from this operation).</p>

---
