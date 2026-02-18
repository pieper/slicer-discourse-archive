# creating single nrrd file

**Topic ID**: 8812
**Date**: 2019-10-17
**URL**: https://discourse.slicer.org/t/creating-single-nrrd-file/8812

---

## Post #1 by @HariES (2019-10-17 11:17 UTC)

<p>When I am saving loaded dicom files slicer saved as .nhdr and raw data files instead single .nrrd. I am not able to import this detached files in metric test. How to make single .nrrd file</p>

---

## Post #2 by @lassoan (2019-10-17 11:19 UTC)

<p>Nhdr format uses two separate files for header and pixel data. Choose nrrd format in Save data window to store image in a single file.</p>

---
