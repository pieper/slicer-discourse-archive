# Unable to load DICOM files

**Topic ID**: 38443
**Date**: 2024-09-19
**URL**: https://discourse.slicer.org/t/unable-to-load-dicom-files/38443

---

## Post #1 by @michael_henderson (2024-09-19 11:57 UTC)

<p>I’ve Googled and Youtubed this but can’t come up with anything other than tutorials on how to load dicom files into the slicer. I have 2 zip files, one containing about 2900 dicom files and the other about 1400. I’ve unzipped the files and put them into separate folders, I’ve tried loading the entire unzipped file, and nothing works. When I select “add dicom data” and the window opens to select the files to download from, nothing shows up, either the zip or the individual files. I’m using windows 10 and Slicer v5.6.2. Thanks in advance! I’m trying to 3D print my brain and my sons, we both had brain surgery due to brain cancer.</p>

---

## Post #2 by @pieper (2024-09-19 20:03 UTC)

<p>There’s a lot of information in this portion of the documentation.  Did you find it?</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#troubleshooting">https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#troubleshooting</a></p>
<p>Especially this part sounds like it should help with what you describe:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#i-try-to-import-a-directory-of-dicom-files-but-nothing-shows-up-in-the-browser">https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#i-try-to-import-a-directory-of-dicom-files-but-nothing-shows-up-in-the-browser</a></p>
<p><a class="mention" href="/u/michael_henderson">@michael_henderson</a> please give these a try and let us know how it goes.</p>
<p>As an aside I’m wondering if we should detect the case where adding files/directories results in no new database entries and direct users to one of these links.</p>

---
