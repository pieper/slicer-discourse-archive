# General registration not importing dicom or nrrd file

**Topic ID**: 14993
**Date**: 2020-12-10
**URL**: https://discourse.slicer.org/t/general-registration-not-importing-dicom-or-nrrd-file/14993

---

## Post #1 by @reem_alzafiri (2020-12-10 19:32 UTC)

<p>Hi all,</p>
<p>Im using the latest version 4.11 and have downloaded slicerRT(latest version). I have practiced with the sample data working on general registration(brains), however, when i tried to use my own ultrasound images, it won’t let me import my dicom files. When i exported those files into .nrrd, and it still wouldnt allow me to import it for general registration despite it being loaded and I can see all my images(both dicom and nrrd).  Please let me know if there is something I’m missing or doing wrong. Thanks !</p>

---

## Post #2 by @reem_alzafiri (2020-12-10 19:32 UTC)

<p>Hi everyone,</p>
<p>I need help registering my ultrasound images. I used the sample data to practice registration, but when I try to do the same with my imported dicom files it wouldn’t allow me to import any of the images. I also exported my dicom files to nrrd and imported it again but when going to the registration tab, it would not let me import any of those files either.</p>

---

## Post #3 by @lassoan (2020-12-10 19:34 UTC)

<p>Your ultrasound images are most likely vector volumes (RGB or RGBA). You need to convert them to scalar volumes for registration. You can convert by using “Vector to Scalar volume” module.</p>

---

## Post #4 by @reem_alzafiri (2020-12-14 16:44 UTC)

<p>Thank you ! It works now !</p>
<p>best,</p>
<p>Reem Alzafiri</p>

---
