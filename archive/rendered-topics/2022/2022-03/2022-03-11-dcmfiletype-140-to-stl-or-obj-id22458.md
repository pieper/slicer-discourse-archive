---
topic_id: 22458
title: "Dcmfiletype 140 To Stl Or Obj"
date: 2022-03-11
url: https://discourse.slicer.org/t/22458
---

# Dcmfiletype.140 to stl or obj

**Topic ID**: 22458
**Date**: 2022-03-11
**URL**: https://discourse.slicer.org/t/dcmfiletype-140-to-stl-or-obj/22458

---

## Post #1 by @R_Mutt (2022-03-11 16:33 UTC)

<p>Hello, I am writing from Turkey. First of all, I apologize for my English, I’m translating from google translate. I am a university student and I need to convert baby ultrasound images to stl. Unfortunately, I couldn’t find the source online. I have files named DCMfileType.140, is it possible to convert them to stl?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e40b2d5d8dd79134dfac2c1c03658913a34c84e.jpeg" data-download-href="/uploads/short-url/bafRf35oB1npJBCKxDLfDfnAoGi.jpeg?dl=1" title="Ekran görüntüsü 2022-03-10 221335" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4e40b2d5d8dd79134dfac2c1c03658913a34c84e_2_690x23.jpeg" alt="Ekran görüntüsü 2022-03-10 221335" data-base62-sha1="bafRf35oB1npJBCKxDLfDfnAoGi" width="690" height="23" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4e40b2d5d8dd79134dfac2c1c03658913a34c84e_2_690x23.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e40b2d5d8dd79134dfac2c1c03658913a34c84e.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e40b2d5d8dd79134dfac2c1c03658913a34c84e.jpeg 2x" data-dominant-color="F5F5F5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Ekran görüntüsü 2022-03-10 221335</span><span class="informations">810×27 5.89 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Can you give me a source for this? Or is it possible to convert this file to stl?</p>

---

## Post #2 by @R_Mutt (2022-03-11 12:32 UTC)

<p>Hello, I am writing from Turkey. First of all, I apologize for my English, I’m translating from google translate. I am a university student and I need to convert baby ultrasound images to stl. Unfortunately, I couldn’t find the source online. I have files named DCMfileType.140, is it possible to convert them to stl?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e40b2d5d8dd79134dfac2c1c03658913a34c84e.jpeg" data-download-href="/uploads/short-url/bafRf35oB1npJBCKxDLfDfnAoGi.jpeg?dl=1" title="Ekran görüntüsü 2022-03-10 221335" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4e40b2d5d8dd79134dfac2c1c03658913a34c84e_2_690x23.jpeg" alt="Ekran görüntüsü 2022-03-10 221335" data-base62-sha1="bafRf35oB1npJBCKxDLfDfnAoGi" width="690" height="23" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4e40b2d5d8dd79134dfac2c1c03658913a34c84e_2_690x23.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e40b2d5d8dd79134dfac2c1c03658913a34c84e.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e40b2d5d8dd79134dfac2c1c03658913a34c84e.jpeg 2x" data-dominant-color="F5F5F5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Ekran görüntüsü 2022-03-10 221335</span><span class="informations">810×27 5.89 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Can you give me a source for this? Or is it possible to convert this file to stl?</p>

---

## Post #3 by @lassoan (2022-03-12 18:47 UTC)

<p>“Type” column in File explorer does not show the actual file type, but description of the file type according to some software that you installed on your computer. In this case, you have configured Adobe Photoshop to be associated with DICOM files, that’s why you see <code>Adobe Photoshop DCMfileType.140</code> as file type. So, all we know is that the file looks like a DICOM file.</p>
<p>Baby ultrasound image files given to parents are typically contain a screen capture movie, so you cannot get a 3D image out of it. If the 3D volumes are acquired for research purposes then there is a higher chance that they actually contain 3D/4D volume. Even if the images contain 3D information, ultrasound imaging vendors are trying to make it difficult to extract that information.</p>
<p>If your files actually contain 3D data, in one of the few formats that have publicly available decoders then you can read them using SlicerHeart extension as described <a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/Docs/ImageImportExport.md">here</a>.</p>

---
