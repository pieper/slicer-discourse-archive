---
topic_id: 2033
title: "Regarding Distorted Sagittal And Coronal Image"
date: 2018-02-06
url: https://discourse.slicer.org/t/2033
---

# Regarding distorted sagittal and coronal image

**Topic ID**: 2033
**Date**: 2018-02-06
**URL**: https://discourse.slicer.org/t/regarding-distorted-sagittal-and-coronal-image/2033

---

## Post #1 by @Joanna (2018-02-06 14:16 UTC)

<h2><a name="p-8329-operating-system-windows-10-slicer-version-481-expected-behaviornormal-sagittal-and-coronal-image-actual-behaviordistorted-sagittal-and-coronal-image-1" class="anchor" href="#p-8329-operating-system-windows-10-slicer-version-481-expected-behaviornormal-sagittal-and-coronal-image-actual-behaviordistorted-sagittal-and-coronal-image-1" aria-label="Heading link"></a>Operating system: Windows 10<br>
Slicer version: 4.8.1<br>
Expected behavior:normal sagittal and coronal image<br>
Actual behavior:distorted sagittal and coronal image</h2>
<p>Dear Sir,</p>
<p>I’ m intrested in the medical imaging. I’m trying to use the 3DSlicer to segment images for 3D printing. But I faced one issue ahter loading the images. The images (sagittal and coronal view) were distorted (z direction). The screenshots were attached below. Can you please help me to solve it?</p>
<p>Thanks.</p>
<p>Joanna</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ecdd57197e5303fcaff1754c28ec34396b0a0cd9.png" data-download-href="/uploads/short-url/xNoTWoof4ZTr1RhhrpwVGQLuaBX.png?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ecdd57197e5303fcaff1754c28ec34396b0a0cd9_2_690x388.png" alt="1" data-base62-sha1="xNoTWoof4ZTr1RhhrpwVGQLuaBX" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ecdd57197e5303fcaff1754c28ec34396b0a0cd9_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ecdd57197e5303fcaff1754c28ec34396b0a0cd9_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ecdd57197e5303fcaff1754c28ec34396b0a0cd9_2_1380x776.png 2x" data-dominant-color="5E5E66"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1920×1080 296 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @cpinter (2018-02-06 15:49 UTC)

<p>Probably the DICOM tags specifying the image spacing are incorrect, and so the Z (IS) spacing is much larger than it is supposed to be. You can manually change spacing in the Volumes module. Open Volume Information panel, and change the third Image Spacing value.</p>

---

## Post #3 by @Joanna (2018-02-07 05:55 UTC)

<p>Thank you <a class="mention" href="/u/cpinter">@cpinter</a>, this is helpful.</p>

---
