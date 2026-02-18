# New to Slicer: Overlaying a .mrml file on a DICOM image

**Topic ID**: 34545
**Date**: 2024-02-26
**URL**: https://discourse.slicer.org/t/new-to-slicer-overlaying-a-mrml-file-on-a-dicom-image/34545

---

## Post #1 by @Arjun_Moorthy (2024-02-26 15:49 UTC)

<p>I’m new to slicer, and I’m working with a prostate cancer dataset (<a href="https://www.cancerimagingarchive.net/collection/prostate-mri-us-biopsy/" class="inline-onebox" rel="noopener nofollow ugc">PROSTATE-MRI-US-BIOPSY - The Cancer Imaging Archive (TCIA)</a>) and I have patient MRI/US DICOM data and .mrml file biopsy vectors and I’d like to overlay .mrml files (there are multiple folders each with one .mrml file and corresponding fiducials (.fcsv files per patient)) onto the DICOM images and then save that .mrml file onto the DICOM image so I can go back through and use screen capture to export specific slices (with annotated biopsy points).</p>
<p>Is the only way to do this with the python interpreter, and if so, how should I go about this?</p>

---

## Post #2 by @pieper (2024-02-26 23:18 UTC)

<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/mrml_overview.html#:~:text=MRML%20file%3A%20When,with%20.mrb%20extension">MRML files</a> are scene files that would load images plus overlays, they are not overlays themselves.  I haven’t looked at this data but I see that on the TCIA page there are instructions about how to load this data in Slicer.  You should refer to those and then let us know if you are still having trouble.  There should be no need to write python code unless you want to automate the process.</p>

---

## Post #3 by @Arjun_Moorthy (2024-02-27 03:00 UTC)

<p>Sounds good, but this is a large dataset (1151 patients) and I was not able to find another method of manually uploading all .mrml’s to slicer besides adding each to the scene and saving. I was looking at the TCIA extension, but it doesn’t seem like that can automatically load in the .mrml’s either. So, do you think the python script is the best way to go?</p>

---

## Post #4 by @pieper (2024-02-27 19:51 UTC)

<p>If you want to apply the same method to all the data in the collection then a python script is a great way to do it.</p>

---
