---
topic_id: 24962
title: "Suv Conversion Error Cant Find Tag 18 1072 But Tag 18 1078 A"
date: 2022-08-28
url: https://discourse.slicer.org/t/24962
---

# SUV conversion error - Can't find tag 18 1072 - but tag 18 1078 available

**Topic ID**: 24962
**Date**: 2022-08-28
**URL**: https://discourse.slicer.org/t/suv-conversion-error-cant-find-tag-18-1072-but-tag-18-1078-available/24962

---

## Post #1 by @samcyc (2022-08-28 10:04 UTC)

<p>Hello everybody,</p>
<p>I can’t convert my DICOM files in Bq/mL into SUV.<br>
I think the problem comes from the metadata of my data which do not contain the tag (0018,1072) RadiopharmaceuticalStartTime, as the error message of the “SUV Factor Calculator” module tells me:<br>
itk::ExceptionObject (0000005A9AB9D0D0)<br>
Location: “unknown”<br>
File: D:\D\S\S-0-E-b\PETDICOMExtension\SUVFactorCalculatorCLI\itkDCMTKFileReader.cxx<br>
Line: 89<br>
Description: ITK ERROR: Can’t find tag 18 1072</p>
<p>However, in the documentation of this module, they mention that the tag (0018,1078) RadiopharmaceuticalStartDateTime​ can be interchangeable with the tag (0018,1072) RadiopharmaceuticalStartTime, and my metadata contains this tag.</p>
<p>How can I overcome this error message?</p>
<p>Thank you very much !</p>

---

## Post #2 by @pieper (2022-08-28 19:49 UTC)

<p>You could try filing an issue and contacting the developers here: <a href="https://github.com/QIICR/Slicer-PETDICOMExtension" class="inline-onebox">GitHub - QIICR/Slicer-PETDICOMExtension: 3D Slicer extension containing tools for importing DICOM PET series</a></p>

---
