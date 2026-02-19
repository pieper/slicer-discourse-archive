---
topic_id: 35143
title: "Aspect Ratio Error When Loading Dicom"
date: 2024-03-27
url: https://discourse.slicer.org/t/35143
---

# Aspect ratio error when loading dicom

**Topic ID**: 35143
**Date**: 2024-03-27
**URL**: https://discourse.slicer.org/t/aspect-ratio-error-when-loading-dicom/35143

---

## Post #1 by @juanslo (2024-03-27 22:36 UTC)

<p>I’ve recently had problems loading a .DCM file into 3D Slicer. The problem appears when viewing the file since two of the three planes appear outside their aspect ratio. These planes appear “clumped” or “crushed.” I have attached an image.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1c8e651a8b0ec20792e465c6e15e405261bed55e.jpeg" data-download-href="/uploads/short-url/44CrPDnef0qSCL2K3hsuLf2UBr0.jpeg?dl=1" title="Captura de pantalla 2024-03-27 102400" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c8e651a8b0ec20792e465c6e15e405261bed55e_2_690x395.jpeg" alt="Captura de pantalla 2024-03-27 102400" data-base62-sha1="44CrPDnef0qSCL2K3hsuLf2UBr0" width="690" height="395" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c8e651a8b0ec20792e465c6e15e405261bed55e_2_690x395.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c8e651a8b0ec20792e465c6e15e405261bed55e_2_1035x592.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c8e651a8b0ec20792e465c6e15e405261bed55e_2_1380x790.jpeg 2x" data-dominant-color="575873"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla 2024-03-27 102400</span><span class="informations">1426×817 62.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2024-03-27 22:43 UTC)

<p>Slicer uses the information reported in the dicom file to set the correct image spacing values. Your dicom has incorrect Z axis value (probably showing it as 1).</p>
<p>You can confirm this by going to the volumes module and checking the image spacing for this dataset.</p>
<p>Where is this dicom originated forum? This is almost never an issue with properly constructed DICOMs.</p>

---
