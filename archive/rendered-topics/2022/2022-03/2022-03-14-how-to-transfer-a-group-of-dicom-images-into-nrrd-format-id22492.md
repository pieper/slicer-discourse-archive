# How to transfer a group of DICOM images into NRRD format

**Topic ID**: 22492
**Date**: 2022-03-14
**URL**: https://discourse.slicer.org/t/how-to-transfer-a-group-of-dicom-images-into-nrrd-format/22492

---

## Post #1 by @LIE_CAI (2022-03-14 12:50 UTC)

<p>For example, I have a group of files,<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8ba75818022c333913b9f74164881c293a69f894.png" alt="1647261723(1)" data-base62-sha1="jVqTToDc3zP9zGhUXDpoDNqZSi8" width="477" height="378"><br>
Each file has a series of DICOM images,<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a57e4b6467426bee0fc0dbc928f9287346e3c10a.png" alt="1647261780(1)" data-base62-sha1="nC1mM4nQ3L2XZ1aop3lJcl7KXCa" width="468" height="364"><br>
I’d like to tranfer them into NRRD format,<br>
Is it possible to achieve it automatically in 3D slicers?<br>
Thanks a lot !</p>

---

## Post #2 by @pieper (2022-03-14 15:47 UTC)

<p>Assuming the dicom data is essentially volumetric then you just need to combine these two snippets into a small script:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#load-dicom-files-into-the-scene-from-a-folder" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#load-dicom-files-into-the-scene-from-a-folder</a></p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#save-volume-to-file" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#save-volume-to-file</a></p>

---

## Post #3 by @hina-shah (2022-03-15 02:30 UTC)

<p>We have a small extension called <a href="https://github.com/hina-shah/SlicerBatchAnonymize">SlicerBatchAnonymize</a> that does exactly this. It should be available in the nightly Slicer’s extension index. Hope this helps.</p>

---
