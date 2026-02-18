# Finding a DICOM series based on series description

**Topic ID**: 31726
**Date**: 2023-09-14
**URL**: https://discourse.slicer.org/t/finding-a-dicom-series-based-on-series-description/31726

---

## Post #1 by @Saima (2023-09-14 02:59 UTC)

<p>Hi Andras,<br>
I am trying to load a dicom folder. The folder contain many series/images. I am interested in loading or extracting a single series based on its series description?</p>
<p>Any help please?</p>
<p>regards,<br>
Saima</p>

---

## Post #2 by @lassoan (2023-09-14 20:06 UTC)

<p>I would recommend to import the entire folder into the database (it should take very short time, images are not loaded just the metadata is indexed). You can then use examples in the script repository to iterate through the list of series to iterate through the list of patients/studies/series to find the series with the description you are interested in.</p>
<p>You could use lower-level functions (e.g., extract data from the SQLite database directly, or iterating through all the files in the folder using pydicom), but they would require a bit more work to implement and/or would be more fragile (may stop working in future Slicer versions).</p>

---
