# Sorting images in a stack based on dicom header

**Topic ID**: 8669
**Date**: 2019-10-04
**URL**: https://discourse.slicer.org/t/sorting-images-in-a-stack-based-on-dicom-header/8669

---

## Post #1 by @mshah (2019-10-04 03:44 UTC)

<p>Hi everyone,</p>
<p>I am working with a stack of 25 DTI images taken in 26 gradient directions, this ultimately comes to 650 dicom files in each stack. In the metadata, I was moving through files from 1 to 650 and observing the b values per file. From this I found that the files in the stack are not ordered properly, is there anyway I can automatically reorder the files according to their specific header?</p>
<p>Thank you!</p>

---

## Post #2 by @lassoan (2019-10-04 04:34 UTC)

<p>All DICOM files are processed based on the file contents, not the file name or order in the database. So, there is no need to reorder the files.</p>

---

## Post #3 by @mshah (2019-10-04 06:47 UTC)

<p>The reason why I suspect they are incorrectly ordered is the b=0 occurs randomly through the 1-650 files. If they were ordered correctly, the b=0 value could correspond to every 25th .dcm file. There is no pattern in the b=0 values, have you seen this before?</p>

---

## Post #4 by @pieper (2019-10-04 13:10 UTC)

<p>You can try converting the data using <a href="https://github.com/SlicerDMRI/SlicerDcm2nii" rel="nofollow noopener">dcm2nnix</a>.  It will interpret dicom from almost any diffusion scan for processing.</p>
<p>Note that when you scan through files it may appear random because the filenames and sort-order of directories may not match the sequence parameters.  This is normal.  Once you have DWI in Slicer, you can look at the baseline and gradient volumes and it should make sense there.</p>

---
