# Importing several single DICOM files as a merged and stacked DICOM file

**Topic ID**: 15381
**Date**: 2021-01-07
**URL**: https://discourse.slicer.org/t/importing-several-single-dicom-files-as-a-merged-and-stacked-dicom-file/15381

---

## Post #1 by @Ata_Naghavi (2021-01-07 01:21 UTC)

<p><strong>Operating system:</strong> Windows 10</p>
<p><strong>Slicer version:</strong> 4.13.0</p>
<p><strong>Expected behavior:</strong> To be able to view and segment my imported DICOM files as a merged file and can go through them slice by slice.</p>
<p><strong>Actual behavior:</strong> After importing my DICOM files, I can only see a single slice on the 4 screen viewer. I cannot drag the arrow and see several slice in series but only see one slice. If I want to see my other slices, I need to make them visible individually which means the previous view will be disabled to be looked at.</p>
<p>Any suggestions on how to import/merge the separated DICOM files into 3D Slicer?</p>
<p>Thank you.</p>

---

## Post #2 by @lassoan (2021-01-07 01:23 UTC)

<p>Read the files using DICOM module as described here: <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#read-dicom-files-into-the-scene" class="inline-onebox">DICOM — 3D Slicer documentation</a></p>

---
