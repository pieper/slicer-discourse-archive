---
topic_id: 11902
title: "Problem With Nrrd File"
date: 2020-06-06
url: https://discourse.slicer.org/t/11902
---

# Problem with nrrd file

**Topic ID**: 11902
**Date**: 2020-06-06
**URL**: https://discourse.slicer.org/t/problem-with-nrrd-file/11902

---

## Post #1 by @Adrian_Izaguirre (2020-06-06 14:15 UTC)

<p>Hi I’am a student new both to the forum and the software, for a project i hadto find a baby ultrasound and make a 3d model of it, but when i try to upload the data to 3DSlicer the images are show in just one axis instead of the three so I can’t use it but is the only one i found. Can some one help me with this please.</p>
<p>Sorry in advace if the message is not write correctly English is not my native language</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4c73d0dcbf49d00a8fa849d0dd6688f7f27e0c75.png" data-download-href="/uploads/short-url/aUkqaA4vwst7LCD1Ya8Mxz1xuNT.png?dl=1" title="Capture3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4c73d0dcbf49d00a8fa849d0dd6688f7f27e0c75_2_690x449.png" alt="Capture3" data-base62-sha1="aUkqaA4vwst7LCD1Ya8Mxz1xuNT" width="690" height="449" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4c73d0dcbf49d00a8fa849d0dd6688f7f27e0c75_2_690x449.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4c73d0dcbf49d00a8fa849d0dd6688f7f27e0c75_2_1035x673.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4c73d0dcbf49d00a8fa849d0dd6688f7f27e0c75_2_1380x898.png 2x" data-dominant-color="334D59"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture3</span><span class="informations">1432×932 113 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><a href="https://www.embodi3d.com/files/file/35592-baby/" rel="noopener nofollow ugc">Nrrd download link</a></p>

---

## Post #2 by @lassoan (2020-06-06 19:42 UTC)

<p>Unfortunately, ITK’s DICOM reader (that Slicer uses for DICOM image reading) does not convert all color images to the correct color space. Since you only need the image intensity anyway, this should not be a problem (unless you work with Doppler images). Go to “Vector to scalar volume” to convert the color volume to a grayscale volume.</p>
<p>Can you tell a bit about your project? How do you plan to use these images in 3D Slicer?</p>

---

## Post #3 by @Adrian_Izaguirre (2020-06-12 13:51 UTC)

<p>For the project I had to construct a printable 3D model of the baby from the 2D images of the ultrasound, the objective is to be able to see the face of the baby.</p>

---

## Post #4 by @lassoan (2020-06-12 16:05 UTC)

<p>Most vendors do not let you export 3D/4D ultrasound image to external applications, but we managed to implement a few importers for selected devices - see more information <a href="https://github.com/SlicerHeart/SlicerHeart">here</a>.</p>

---
