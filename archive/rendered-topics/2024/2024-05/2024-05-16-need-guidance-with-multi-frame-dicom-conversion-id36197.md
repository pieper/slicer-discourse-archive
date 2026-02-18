# Need guidance with multi-frame dicom conversion

**Topic ID**: 36197
**Date**: 2024-05-16
**URL**: https://discourse.slicer.org/t/need-guidance-with-multi-frame-dicom-conversion/36197

---

## Post #1 by @GONZALOU (2024-05-16 05:30 UTC)

<p>I’ve been attempting to convert a multi-frame DICOM file into single-frame DICOM files using SANTE DICOM Editor. Despite the conversion seeming successful, I suspect there’s an issue with the header information of the single-frame files. When I try to import these converted files into another software app, they’re not recognized as single-frame files, causing the data not to be imported at all. Interestingly, when I use single-frame files that haven’t been converted, everything works fine. Currently, I’m investigating this issue and searching for solutions to ensure compatibility between the generated DICOM files and the target software. Given my positive experience with 3D Slicer in the past and its versatility, I’m considering whether it could offer a solution by effectively “splitting” the multi-frame without losing any crucial data that might render them unreadable.</p>

---

## Post #2 by @pieper (2024-05-16 20:59 UTC)

<p>You might be able to.  Try loading the multiframe instance and the re-export and you should get singleframe instances.</p>
<p>If that doesn’t work your best bet would be to write a custom pydicom script.</p>

---
