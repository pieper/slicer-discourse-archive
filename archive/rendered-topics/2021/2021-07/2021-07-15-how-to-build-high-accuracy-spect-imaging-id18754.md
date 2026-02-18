# How to build high accuracy SPECT Imaging

**Topic ID**: 18754
**Date**: 2021-07-15
**URL**: https://discourse.slicer.org/t/how-to-build-high-accuracy-spect-imaging/18754

---

## Post #1 by @akmal871026 (2021-07-15 15:09 UTC)

<p>Hi All,</p>
<p>I did the SPECT image segmentation using the PETTumorSegmentation extension.</p>
<p>But there is low accuracy.</p>
<p>Let say, my dummy sphere volume phantom is 27 ml, using PETTumorSegmenation I got 44ml.</p>
<p>Does anyone know is it there is the best method for SPECT segmentation using 3D Slicer??</p>
<p>Thank you.</p>

---

## Post #2 by @lassoan (2021-07-15 16:17 UTC)

<p>You can use finer resolution for the segmentation than the input image. See detailed instructions <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#segmentation-is-not-accurate-enough">here</a>.</p>
<p>Do you also have a CT image corresponding to the SPECT image? If yes, then it would make sense to choose that as a master volume for the segmentation, as most likely it has sufficiently fine resolution.</p>

---

## Post #3 by @akmal871026 (2021-07-15 17:32 UTC)

<p>Hi Sir,</p>
<p>I’m not find <em>Specify geometry</em> button in Segment Editor</p>

---

## Post #4 by @lassoan (2021-07-15 17:35 UTC)

<p>The button is here, as described in the documentation:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1ce70d1b4679d9af8a65a0dab5c93dfd709f5115.jpeg" data-download-href="/uploads/short-url/47GoqQjhVu7nwJGydU1FazV1PFP.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1ce70d1b4679d9af8a65a0dab5c93dfd709f5115_2_690x407.jpeg" alt="image" data-base62-sha1="47GoqQjhVu7nwJGydU1FazV1PFP" width="690" height="407" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1ce70d1b4679d9af8a65a0dab5c93dfd709f5115_2_690x407.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1ce70d1b4679d9af8a65a0dab5c93dfd709f5115.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1ce70d1b4679d9af8a65a0dab5c93dfd709f5115.jpeg 2x" data-dominant-color="E0E1E3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">881×520 76.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>If the button is not there then you are using a very old Slicer version and you need to update to the current version.</p>

---

## Post #5 by @akmal871026 (2021-07-15 17:44 UTC)

<p>i got that. this is my geometry. then how to do?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2f07f80d8d93431396b1da126e07a669258a7beb.jpeg" data-download-href="/uploads/short-url/6I3vTP4AqxIGIW3bmpnM2CqlVdF.jpeg?dl=1" title="geometry" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2f07f80d8d93431396b1da126e07a669258a7beb_2_690x468.jpeg" alt="geometry" data-base62-sha1="6I3vTP4AqxIGIW3bmpnM2CqlVdF" width="690" height="468" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2f07f80d8d93431396b1da126e07a669258a7beb_2_690x468.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2f07f80d8d93431396b1da126e07a669258a7beb_2_1035x702.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2f07f80d8d93431396b1da126e07a669258a7beb_2_1380x936.jpeg 2x" data-dominant-color="FFFFFF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">geometry</span><span class="informations">2640×1792 84 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @lassoan (2021-07-15 19:40 UTC)

<p>You have two options, as described <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#segmentation-is-not-accurate-enough">here</a>.</p>
<p>I would recommend option A (crop volume), because you can crop away a large part of your volume and so you can have a high-resolution volume, without increased memory usage.</p>
<p>Option B. (use specify geometry button) would work, too, just would make things slower. For your data, you would need to use an oversampling factor of about 4.0, and since the physical extent of the volume will remains the same, the memory usage (and computation time for most operations) will be 64x more.</p>

---

## Post #7 by @akmal871026 (2021-07-16 03:52 UTC)

<p>But sir, where is button crop located?? I also not found</p>

---

## Post #8 by @lassoan (2021-07-16 13:03 UTC)

<p>You can switch to Crop volume module using the module finder (Ctrl-F).</p>

---

## Post #9 by @akmal871026 (2021-07-17 14:20 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e6c080b3463d789e335a4cfc9fcb732a792d5cd1.png" alt="image.png" data-base62-sha1="wVkfI7aA5YwP5NuPA4TuIv8c0U1" width="517" height="346"></p>
<p><strong>Which one? Crop Volume or Crop Volume Sequence?</strong></p>

---

## Post #10 by @lassoan (2021-07-17 16:17 UTC)

<p>You can read a short summary of the module on the right side. In short, “Crop volume” module is for cropping volumes (3D), while “Crop volume sequence” module is for cropping sequence of volumes (4D data sets). Therefore, as I wrote in my last post, you will need to use “Crop volume” module.</p>

---
