# Any help to do simple tractography by simple easy steps?@

**Topic ID**: 44036
**Date**: 2025-08-09
**URL**: https://discourse.slicer.org/t/any-help-to-do-simple-tractography-by-simple-easy-steps/44036

---

## Post #1 by @ahmad_elgamal (2025-08-09 21:31 UTC)

<p>Any help to do simple tractography by simple easy steps?@</p>

---

## Post #2 by @pieper (2025-08-10 17:30 UTC)

<p>You need to install SlicerDMRI, then you can get a tensor image from SampleData.  Then place a fiducial on something like the corpus callosum and go into the interactive seeding module and enable seeding with the selected fiducial.  Then you can more the fiducial around, adjust parameters, etc.</p>

---

## Post #3 by @ahmad_elgamal (2025-08-10 21:30 UTC)

<p>I already have a SlicerDMRI, also installed the all related extensions, but when I start to follow tutorial every time I found an error at any step, or a step I can’t apply it on my version 5.8</p>
<p>I have a DICOM  volumes of complete DTI examinations , and I’m wondering to do tractography</p>

---

## Post #4 by @pieper (2025-08-10 21:39 UTC)

<p>What is in the error log?</p>

---

## Post #5 by @ahmad_elgamal (2025-08-10 21:50 UTC)

<p>According to the tutorial, first step to convert DWI to DWI.nhdr , some times I find difficulties to choose which DWI I have to choose to complete conversion without errors,(DWI, B0, B1000, Iso DWI, Reg DWI, DTI, RegDTI…ect), but now I tried many types and finally one can be converted without problems</p>
<p>Then I found problem to open the new dwi.nhdr and to activate it at volume step</p>
<p>Sometimes I can pass it, then I found a problem to complete steps of Diffusion Tensor estimation, as I can set all parameters, except one related to (input mask), I can’t found any choices to complete this step, so it finished by fault</p>
<p>I need a simple video or tutorial to latest version 5.8, to can deal with these issues please</p>

---

## Post #6 by @pieper (2025-08-11 19:23 UTC)

<p>Diffusion imaging is still pretty much a specialist’s field, especially when you are working with new acquisitions since the dicom formats can vary widely.  There may not be any good tutorials beyond what you have already found (assuming you are looking in <a href="http://dmri.slicer.org">dmri.slicer.org</a>).  If you find specific things that are not working you can file issues on the github page.</p>

---
