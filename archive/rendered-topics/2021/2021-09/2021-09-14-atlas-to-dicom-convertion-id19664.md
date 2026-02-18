# Atlas to DICOM convertion

**Topic ID**: 19664
**Date**: 2021-09-14
**URL**: https://discourse.slicer.org/t/atlas-to-dicom-convertion/19664

---

## Post #1 by @R_Rodriguez (2021-09-14 12:58 UTC)

<p>Hi all<br>
I am trying to convert an atlas (binary 0/1 file, originally nifti format) into DICOM. Using “Create DICOM Series” I obtained completely white slices.<br>
Some help?<br>
Thank you in advance</p>
<p>Operating system: Windows<br>
Slicer version: 4.11</p>

---

## Post #2 by @pieper (2021-09-14 13:10 UTC)

<p>Can you post an example file?</p>

---

## Post #3 by @lassoan (2021-09-14 13:47 UTC)

<p>The file is actually not all white, but intensity difference of 1 is so small that in many viewers will not see that subtle change with the default window/level settings.</p>
<p>“Atlas” is not a kind of image, but it refers to how you use that image, so there is no <em>atlas</em> information object in DICOM. Instead, a binary (0/1) image is a <em>segmentation</em>, which can be <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#dicom-export">saved into DICOM as Segmentation Object or RT Structure Set information object</a>.</p>
<p>If the external viewer does not support these information objects then you can make your binary file appear as a fake CT image by rescaling its intensity range. For example, you can keep the 0 HU (=water) as background, but change 1 to 1000 HU (=bone) for the foreground, using RescaleIntensityImageFilter in Simple Filters module.</p>

---
