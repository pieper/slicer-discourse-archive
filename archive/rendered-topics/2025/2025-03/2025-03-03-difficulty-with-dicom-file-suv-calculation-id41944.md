# Difficulty with Dicom file SUV calculation

**Topic ID**: 41944
**Date**: 2025-03-03
**URL**: https://discourse.slicer.org/t/difficulty-with-dicom-file-suv-calculation/41944

---

## Post #1 by @Aurorasp (2025-03-03 18:16 UTC)

<p>Hello all<br>
Beginner to 3d Slicer. A bit of background. I recorded PET CT on 8 mice in Mediso, and we reconstructed the files, entering info about route time of injection and F18 radiotracer and average of activity injected (I can’t add info for all 8 mice one by one). Also, I didn’t enter weight information as far as I remember. In the 3d slicer, after creating an overlap of CT PET, selecting PET, and cropping my interest brain area, I create a segment on the Brain(interest area) and obtain segment statistics. However, opening this dicom file in Slicer doesn’t allow any SUV or standard SUV calculation; it gives the error of WARNING: In D:\D\S\S-0-build\ITK\Modules\IO\GDCM\src\itkGDCMSeriesFileNames.cxx, line 100<br>
GDCMSeriesFileNames (0000018CE071A840): No Series were found<br>
the thing is, checking the file information, it doesn’t seem that I am handling an already calibrated file (the scalar range is very big), so the mean obtained in segment statistics, to my understanding, can’t be used for SUV uptake calculation.  any more insight or step-by-step guide to share, please, will be really appreciated.</p>

---

## Post #2 by @pieper (2025-03-03 23:22 UTC)

<p>As far as I know the PET tools were all developed for human scans and the metadata extraction has some special cases for different scanners.  You would probably need to dig into the code to make sure you are getting the right parameters for the mouse scans.  Since it sounds like you know the needed parameters it should be possible for you to make it work.</p>

---
