# Save segmented images

**Topic ID**: 18523
**Date**: 2021-07-05
**URL**: https://discourse.slicer.org/t/save-segmented-images/18523

---

## Post #1 by @refrangioni (2021-07-05 21:45 UTC)

<p>I need to use segmented images in a program that uses segmented slices in .bmp format<br>
I can also use segmented images in DICOM format and then transform them to .bmp<br>
what is the best way. and how to save segmented ​​slices images in DICOM in 3d slicer. I tried but I could not.</p>

---

## Post #2 by @Gowtham_P (2021-07-06 10:27 UTC)

<p>I also had a similar problem, Currently, I am using a workaround to export the Segmentation node as DICOM series by using the Binary Labelmap option. I am not sure it’s the proper solution, but it works for me.</p>
<p>Solution:<br>
Right Click the segmentation node on Data Manager → Export visible segments to Binary Labelmap<br>
A new segmentation label will be created, if you right-click that you will get the option to export to DICOM, where you can add details and export your segment as a DICOM series.</p>
<p>Hope this Helps!!</p>

---

## Post #3 by @refrangioni (2021-07-07 12:56 UTC)

<p>Thanks for your help !<br>
I tried this but it looks like the generated images don’t contain the segmentation.<br>
I think I’m doing something wrong when I get to stage of export.<br>
In “select export type” (iten 2) has “scalar volume”, “RT” and “slicer data bundle”.<br>
The first 2  (scalar volume and RT) generated files without segmentation and the third one did not complete.</p>

---

## Post #4 by @Gowtham_P (2021-07-08 14:56 UTC)

<p>Hi,</p>
<p>I think there is a small misunderstanding, probably due to my lazy short explanation.</p>
<p>you understood the concept of the export option which I mentioned as saving the data. Pls, see the attached images for reference. It’s actually exporting the same data inside the slicer to a different format.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/21d73d8a80dd7b5168bb8040b99585394a2c198b.jpeg" data-download-href="/uploads/short-url/4PmUei2u1ZLqHWGWwQbUezOFrlh.jpeg?dl=1" title="S1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/21d73d8a80dd7b5168bb8040b99585394a2c198b_2_690x388.jpeg" alt="S1" data-base62-sha1="4PmUei2u1ZLqHWGWwQbUezOFrlh" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/21d73d8a80dd7b5168bb8040b99585394a2c198b_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/21d73d8a80dd7b5168bb8040b99585394a2c198b_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/21d73d8a80dd7b5168bb8040b99585394a2c198b_2_1380x776.jpeg 2x" data-dominant-color="393B42"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">S1</span><span class="informations">1920×1080 279 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7dc13565a685c1149845f57465653845b025faed.jpeg" data-download-href="/uploads/short-url/hWtD8ENQ3oeQhjK0qyEIfYZf4hD.jpeg?dl=1" title="S2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7dc13565a685c1149845f57465653845b025faed_2_690x388.jpeg" alt="S2" data-base62-sha1="hWtD8ENQ3oeQhjK0qyEIfYZf4hD" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7dc13565a685c1149845f57465653845b025faed_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7dc13565a685c1149845f57465653845b025faed_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7dc13565a685c1149845f57465653845b025faed_2_1380x776.jpeg 2x" data-dominant-color="3A3B42"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">S2</span><span class="informations">1920×1080 282 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d852c4fcb32f6d69782eb7464d06ec5e30f16ad4.jpeg" data-download-href="/uploads/short-url/uRGsUT1SFd5CTbm4bzMw80qHg5m.jpeg?dl=1" title="S3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d852c4fcb32f6d69782eb7464d06ec5e30f16ad4_2_690x388.jpeg" alt="S3" data-base62-sha1="uRGsUT1SFd5CTbm4bzMw80qHg5m" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d852c4fcb32f6d69782eb7464d06ec5e30f16ad4_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d852c4fcb32f6d69782eb7464d06ec5e30f16ad4_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d852c4fcb32f6d69782eb7464d06ec5e30f16ad4_2_1380x776.jpeg 2x" data-dominant-color="3F3F46"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">S3</span><span class="informations">1920×1080 311 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @refrangioni (2021-07-10 01:56 UTC)

<p>Hi,<br>
I managed to save the segmented images in dicom format using the SlicerRT extension.<br>
I followed as recommended by you<br>
Right Click the segmentation node on Data Manager → Export visible segments to Binary Labelmap<br>
right-click  to export to DICOM, where you can add details and export your segment as a DICOM series.<br>
Need to choose RT in “select export type” item.<br>
But this RT only apear if SlicerRT extension is able.<br>
Thanks for your tips!!!<br>
Great and good explanations !!!</p>

---
