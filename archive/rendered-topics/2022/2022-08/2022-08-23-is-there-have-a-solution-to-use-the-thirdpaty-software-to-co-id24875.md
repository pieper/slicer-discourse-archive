---
topic_id: 24875
title: "Is There Have A Solution To Use The Thirdpaty Software To Co"
date: 2022-08-23
url: https://discourse.slicer.org/t/24875
---

# Is there have a solution to use the thirdpaty software to convert dicom files to nifti files?

**Topic ID**: 24875
**Date**: 2022-08-23
**URL**: https://discourse.slicer.org/t/is-there-have-a-solution-to-use-the-thirdpaty-software-to-convert-dicom-files-to-nifti-files/24875

---

## Post #1 by @jay1987 (2022-08-23 02:47 UTC)

<p>I have tryed to use slicer it self to convert dicom files to nifti files,but it seems to have problems.<br>
is there have a thirty party software to use subprocess to convert dicom files to nifti files?</p>

---

## Post #2 by @pieper (2022-08-23 13:47 UTC)

<p>There is a <a href="https://github.com/SlicerDMRI/SlicerDcm2nii">dcm2nii</a> extension that is meant for diffusion MRI but it may also work for other acquisitions.  Note that it’s not always possible to convert dicom to nifti and if dicom files don’t load as scalar volumes in Slicer they may not be compatible with nifti.</p>

---

## Post #3 by @PaoloZaffino (2022-08-23 14:28 UTC)

<p>Plastimatch is a good solution: <a href="http://plastimatch.org/" rel="noopener nofollow ugc">http://plastimatch.org/</a></p>

---

## Post #4 by @dave3d (2022-08-23 15:55 UTC)

<p>You could use SimpleITK to convert DICOM to Nifti.  Here’s an example showing how:</p>
<p><a href="https://simpleitk.readthedocs.io/en/master/link_DicomSeriesReader_docs.html" class="onebox" target="_blank" rel="noopener nofollow ugc">https://simpleitk.readthedocs.io/en/master/link_DicomSeriesReader_docs.html</a></p>
<p>If you give an output file name with the “.nii” or “.nii.gz” it will write Nifti.</p>

---
