# Create volume from Slices DICOM

**Topic ID**: 23649
**Date**: 2022-05-31
**URL**: https://discourse.slicer.org/t/create-volume-from-slices-dicom/23649

---

## Post #1 by @Haytham (2022-05-31 09:13 UTC)

<p>Hello,<br>
I have DICOM files that represent slices. how can get one DICOM file that represent all the volume?<br>
I need to combine all DICOM slices on a one DICOM volume.<br>
Any ideas can help me?<br>
thanks</p>

---

## Post #2 by @cpinter (2022-05-31 09:59 UTC)

<p>I’m not sure I understand correctly, but it sounds like you simply want to load a DICOM volume from a series of files. You need to use the DICOM browser for that: import folder, load series from the browser. See more <a href="https://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html#dicom-data" class="inline-onebox">Data Loading and Saving — 3D Slicer documentation</a></p>

---
