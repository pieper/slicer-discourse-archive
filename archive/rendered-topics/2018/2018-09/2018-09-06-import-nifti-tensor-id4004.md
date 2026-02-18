# Import NIFTI tensor

**Topic ID**: 4004
**Date**: 2018-09-06
**URL**: https://discourse.slicer.org/t/import-nifti-tensor/4004

---

## Post #1 by @AKKnutsen (2018-09-06 15:55 UTC)

<p>Operating system: Windows 64-bit<br>
Slicer version: 4.8.1</p>
<p>I’m interested in loading a tensor saved as a 4D NIFTI for visualization, but am unsure of how to do so. This does not appear to be an option in DWIConvert.</p>
<p>Is anyone familiar with how to do this? Thanks in advance.</p>

---

## Post #2 by @ihnorton (2018-09-07 14:06 UTC)

<p>I’m not aware of any tool to do this right now. What software is the Nifti matrix file coming from? My limited (possibly outdated) understanding is that interpretation of the Nifti matrix format tends to be very application-specific.</p>

---

## Post #3 by @AKKnutsen (2018-09-07 16:44 UTC)

<p>Thanks for your reply. Much appreciated.</p>
<p>The software varies. I use different software for DTI processing (e.g., TORTOISE, FDT, etc). TORTOISE actually offers an option to output the processed DTI data to NRRD that can be input into Slicer (I have used this).</p>
<p>My research is in biomechanics, so I also work with tensors related to deformation.I have written code for tensor visualization in Matlab, but Slicer has better surface visualization and built-in tensor glyphs + tractography.</p>
<p>I generally write the tensors as NIFTis in Matlab or Python.</p>
<p>I’m not sure that I follow your comment that the “interpretation of the Nifti matrix format tends to be very application-specific.” Are you referring to the organization of the fourth dimension (describing the tensor components)?</p>
<p>Thanks again.</p>

---
