# Edit labels of DICOM images

**Topic ID**: 38213
**Date**: 2024-09-04
**URL**: https://discourse.slicer.org/t/edit-labels-of-dicom-images/38213

---

## Post #1 by @erlendAQK (2024-09-04 14:43 UTC)

<p>I haved used Monailabel to label my images. I need to edit the labeling but have problems loading the labels on top of the image. This is how it looks like when I press “Submit Label”<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/eec8c1eba5de02bb1501de5553d6f1e2135d7b3a.png" data-download-href="/uploads/short-url/y4nL3kx50lE5RUPNXg9hW1GXDB0.png?dl=1" title="Skjermbilde 2024-08-28 105654" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/eec8c1eba5de02bb1501de5553d6f1e2135d7b3a_2_690x125.png" alt="Skjermbilde 2024-08-28 105654" data-base62-sha1="y4nL3kx50lE5RUPNXg9hW1GXDB0" width="690" height="125" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/eec8c1eba5de02bb1501de5553d6f1e2135d7b3a_2_690x125.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/eec8c1eba5de02bb1501de5553d6f1e2135d7b3a_2_1035x187.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/eec8c1eba5de02bb1501de5553d6f1e2135d7b3a_2_1380x250.png 2x" data-dominant-color="A1ACA3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Skjermbilde 2024-08-28 105654</span><span class="informations">2120×387 330 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>When I load the label it looks like this. How can I edit it?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/31c3b9d817db0d892d95db6a8177d48c27482dbf.png" data-download-href="/uploads/short-url/76eJGVqM4YUbwvpTyL2H2GbFwBx.png?dl=1" title="Skjermbilde 2024-09-04 145918" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/31c3b9d817db0d892d95db6a8177d48c27482dbf.png" alt="Skjermbilde 2024-09-04 145918" data-base62-sha1="76eJGVqM4YUbwvpTyL2H2GbFwBx" width="690" height="296" data-dominant-color="4C4C4C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Skjermbilde 2024-09-04 145918</span><span class="informations">1030×443 1.27 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Background:<br>
I started out with DICOM images which I transformed into NifTi images stored as .dcm.nii.gz. I think that causes some problems. At least the “Next Sample” button does not work. I have to drag the images into 3Dslicer.</p>
<p>I have used the Segmentation configuration from the radiology app. Should I have used the deepgrow or something else?</p>

---

## Post #2 by @erlendAQK (2024-09-05 08:04 UTC)

<p>Solved!<br>
I got lost in MonaiLabel which wasn’t actually necessary for my purpose. Also, I got confused with the differences between volumes and segmentations.</p>
<p>This tutorial was helpful: <a href="https://www.youtube.com/watch?v=xIts_5fctYg" rel="noopener nofollow ugc">https://www.youtube.com/watch?v=xIts_5fctYg</a><br>
and this forum question: <a href="https://discourse.slicer.org/t/how-to-edit-nii-gz-file-that-was-created-using-another-program/6479" class="inline-onebox">How to edit nii.gz file that was created using another program?</a></p>

---
