# Problem with DICOM Dental files

**Topic ID**: 1193
**Date**: 2017-10-07
**URL**: https://discourse.slicer.org/t/problem-with-dicom-dental-files/1193

---

## Post #1 by @Jonathan_Dmello (2017-10-07 04:51 UTC)

<p>Need some help with a dicom dental file. The 3D image loads in a elongated view. by which i mean the image is stretched vertically. Can anyone help with this. i am  adding a link to the file. I think its a problem with the file or i have messed up the settings. Anyways please let me know whats wrong and how do i correct it.</p>
<p>Thank you<br>
Jonathan</p>

---

## Post #2 by @lassoan (2017-10-07 05:17 UTC)

<p>Some Dental CBCT scanners create invalid DICOM files: they incorrectly store slice spacing in slice thickness tag and slice position information is missing.</p>
<p>Fortunately, the <code>DICOM patcher</code> (in Utilities category) module can fix this issue. Delete the already imported series from Slicer’s DICOM browser, then go to DICOM patcher module, set up input and output directories, then click Patch, click Import, then click Go to DICOM module to load the data.</p>
<p>Note: make sure to always anonymize data before sharing.</p>

---

## Post #3 by @Jonathan_Dmello (2017-10-07 05:27 UTC)

<p>Hi Andras Lasso,<br>
Thanks for the quick reply. Will definitely remember to anonymize the data in future. Still a newbie at this.</p>

---

## Post #4 by @zel (2023-01-24 03:14 UTC)

<p>where is patcher, please</p>

---

## Post #5 by @cpinter (2023-01-24 11:13 UTC)

<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicompatcher.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/dicompatcher.html</a></p>

---

## Post #6 by @lassoan (2023-01-24 12:21 UTC)

<p>The DICOM Patcher module is included in Slicer core (no need to install any extensions). You can use the <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#toolbar">Module selection toolbar</a> to switch to the module. It is in the “Utilities” category.</p>

---
