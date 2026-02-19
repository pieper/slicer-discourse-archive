---
topic_id: 3247
title: "Volume Rendering From Scalars"
date: 2018-06-20
url: https://discourse.slicer.org/t/3247
---

# Volume rendering from scalars

**Topic ID**: 3247
**Date**: 2018-06-20
**URL**: https://discourse.slicer.org/t/volume-rendering-from-scalars/3247

---

## Post #1 by @cschmit3 (2018-06-20 18:52 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.8.1<br>
Expected behavior: create a model or volume from a scalar<br>
Actual behavior: no responses</p>
<p>All I am hoping to do with Slicer is to generate color coded 3D images to post in a medical article.  I have access to previously 3D rendered .pial files (left hemisphere of brain with gyri) and scalars that denote regions of interest, but not the CT dicom images.  The scalar won’t separate from the model that appears when the .pial is read in, and I’m hoping to create a volume from my scalar so that I can pick colors.  I would use the default color coding, but I can’t customize the way I want without separating the scalar from the model completely.  Any advice would be greatly appreciated.</p>

---

## Post #2 by @pieper (2018-06-20 19:15 UTC)

<p>Hi -</p>
<p>It might help if you pasted an image of what you have currently working and an example image (maybe of some other data in another system) closer to what you want to achieve.</p>
<p>It sounds like you have freesurfer data and It’s not clear to me what you mean about separating the scalar from the model.</p>

---

## Post #3 by @cschmit3 (2018-06-20 19:32 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f573b94174934695f951542d50c526e6a3e7a854.png" data-download-href="/uploads/short-url/z1mUR84T0ngBbPJep8wCfCpdCn2.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f573b94174934695f951542d50c526e6a3e7a854_2_690x356.png" alt="image" data-base62-sha1="z1mUR84T0ngBbPJep8wCfCpdCn2" width="690" height="356" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f573b94174934695f951542d50c526e6a3e7a854_2_690x356.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f573b94174934695f951542d50c526e6a3e7a854_2_1035x534.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f573b94174934695f951542d50c526e6a3e7a854.png 2x" data-dominant-color="C6C6DF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1343×693 134 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/2773047a786bcd89a05b59eab1573c6024fcdc48.png" data-download-href="/uploads/short-url/5CZ2NImYPIw844jNYL4JcHrXoF2.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/2773047a786bcd89a05b59eab1573c6024fcdc48_2_690x294.png" alt="image" data-base62-sha1="5CZ2NImYPIw844jNYL4JcHrXoF2" width="690" height="294" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/2773047a786bcd89a05b59eab1573c6024fcdc48_2_690x294.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/2773047a786bcd89a05b59eab1573c6024fcdc48_2_1035x441.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/2773047a786bcd89a05b59eab1573c6024fcdc48.png 2x" data-dominant-color="C4C4DB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1211×517 122 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The first snip shows that my scene has a model “lh” and the second one shows my applied scalar (black on the 3D).  I want to make the black labeled scalar a volume (mask?) that’s totally separate from “lh” so I can color them independently.</p>
<p>Thanks!!</p>

---

## Post #4 by @cschmit3 (2018-06-20 19:35 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/52dfbf99d1e09278684ec99c6364a48900727af4.png" data-download-href="/uploads/short-url/bP8wWHC3Zy2kKRChaoGDDeyOQ4s.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/52dfbf99d1e09278684ec99c6364a48900727af4_2_690x299.png" alt="image" data-base62-sha1="bP8wWHC3Zy2kKRChaoGDDeyOQ4s" width="690" height="299" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/52dfbf99d1e09278684ec99c6364a48900727af4_2_690x299.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/52dfbf99d1e09278684ec99c6364a48900727af4_2_1035x448.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/52dfbf99d1e09278684ec99c6364a48900727af4.png 2x" data-dominant-color="959496"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1366×592 50.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Additionally, this is what I mean when I say that I don’t have any data other than the 3D, I can’t see or edit CT dicom images.</p>

---

## Post #5 by @pieper (2018-06-20 19:58 UTC)

<p>Okay, yes, that helps explain.  Just to clarify, you scalar field of your ROI is defined on the left hemisphere surface model so it just a 2D surface and not a volumetric structure.  Often in freesurfer the surface parcellations have a corresponding aseg segmentation that is a label map of the gray matter under the ROI but I guess you don’t have that.  Or if you have the white matter model I believe they have the same vertex numbering which could allow you to extract a 3D structure (would require some work but it could be done with a little scripting).</p>
<p>Alternatively you should be able to define a color table where your ROI is visible in whatever color you want, but all other values in the scalar map to a color with a zero alpha value.  Then you would be able to see your ROI surface alone.</p>
<p>Maybe someone else who work with this data more than I do will have some ideas.</p>

---
