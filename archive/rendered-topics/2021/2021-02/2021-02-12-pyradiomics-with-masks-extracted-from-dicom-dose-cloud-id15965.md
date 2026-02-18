# Pyradiomics with masks extracted from DICOM dose cloud

**Topic ID**: 15965
**Date**: 2021-02-12
**URL**: https://discourse.slicer.org/t/pyradiomics-with-masks-extracted-from-dicom-dose-cloud/15965

---

## Post #1 by @Adam (2021-02-12 03:49 UTC)

<p>Operating system:Windows 10<br>
Slicer version: 4.10.1</p>
<p>Hi,</p>
<p>I have masks stored in numpy ndarray, and I am using pynrrd to write them to .nrrd format for use in pyradiomics. When I check the nrrd masks against the dicom image in Slicer, the image origin and voxel size do not align. It’s easy enough to correct manually in slicer by changing the ‘Image Spacing:’, and ‘Image Origin:’, but I need to do this for thousands of DICOM files.Pixel spacing is available in the DICOM header, but the slice thickness seems difficult to get.</p>
<p>What is the best way to approach this problem? Do I try to convert all the DICOM to nrrd first? How can I do that in a python script? Saving as nrrd in Slicer works well but is too slow for many files.</p>
<p>Thank you for your help</p>

---

## Post #2 by @pieper (2021-02-12 15:54 UTC)

<p>You can probably use DWIConvert or dcm2niix that come with SlicerDMRI.  They are meant for diffusion scans, but will also convert scalar volumes if they don’t find diffusion info in the headers.  Both are simple executables so they are super fast compared to starting Slicer.</p>

---

## Post #3 by @Adam (2021-02-17 17:34 UTC)

<p>Thank you, I will have a look at that.</p>

---

## Post #4 by @JoostJM (2021-03-09 12:18 UTC)

<p>Alternatively, I built a python package that can analyze DICOM scalar volumes and convert them to nrrd.<br>
See <a href="https://github.com/JoostJM/nrrdify.git">https://github.com/JoostJM/nrrdify.git</a>. The trick is that DICOM files are generally a file per slice, and you need to order them correctly before converting the to nrrd using something like SimpleITK image series reader. Nrrdify handles this by looking at ImagePositionPatient tag.<br>
It also operates in batch mode, allowing you to convert your entire dataset in one go.</p>

---
