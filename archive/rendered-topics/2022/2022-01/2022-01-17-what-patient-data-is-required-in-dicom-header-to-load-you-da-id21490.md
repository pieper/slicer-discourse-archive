# What patient data is required in DICOM header to load you data with "Load DICOM Data"?

**Topic ID**: 21490
**Date**: 2022-01-17
**URL**: https://discourse.slicer.org/t/what-patient-data-is-required-in-dicom-header-to-load-you-data-with-load-dicom-data/21490

---

## Post #1 by @Luna (2022-01-17 10:09 UTC)

<p>I am currently creating a DICOM file of images without a SOP class. If I would load my dicom file slicer would say that some patient data is missing. Which attributes should I add to load it?</p>

---

## Post #2 by @pieper (2022-01-17 15:05 UTC)

<p>DICOM is such a complex standard that it’s hard to say exactly what is required for various image types.  You can read the standard of course, or you can look at the source code.  But the easiest is probably to look at examples of data that works and try to replicate the structure for your data while referring to the standard to see what values are valid.  This site can help: <a href="https://dicom.innolitics.com/ciods" class="inline-onebox">All CIODs – DICOM Standard Browser</a></p>

---
