# Batch Processing with SlicerLungCTAnalyzer

**Topic ID**: 42768
**Date**: 2025-05-01
**URL**: https://discourse.slicer.org/t/batch-processing-with-slicerlungctanalyzer/42768

---

## Post #1 by @omegayen (2025-05-01 22:22 UTC)

<p>Hi <a class="mention" href="/u/rbumm">@rbumm</a> thanks for your work.</p>
<p>I am working with SlicerLungCTAnalyzer and having difficulty with batch processing with both the segmenter and analyzer. I reviewed the instructions here <a href="https://github.com/Slicer/SlicerLungCTAnalyzer/wiki/Batch-processing-with-Lung-CT-Segmenter" class="inline-onebox" rel="noopener nofollow ugc">Batch processing with Lung CT Segmenter · Slicer/SlicerLungCTAnalyzer Wiki · GitHub</a> as I want to do the segmenter first before then doing the analyzer.</p>
<p>I always get this error as below</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e245fba14a26dda9602fbdf1f05830514fe8a583.png" alt="image" data-base62-sha1="whHQsf6KnHxLBSwY6agWn6QfHNN" width="502" height="92"></p>
<p>My input folder points to something like C:\input and I have folders 1, 2, 3, ..etc in it and each subfolder contains a xxx_ct.nii.gz file. Use AI is selected and checked.</p>
<p>Test mode does not work either. I am checking the box for Input is NIFTI format. Any ideas?</p>

---

## Post #2 by @Mannitol (2025-09-02 11:07 UTC)

<p>I have the same confusion. The single input and segmentation are working well, but I can’t do any batch processing. I used the 3Dslicer 5.8.1 with LungCTAnalyzer v2.69.</p>

---

## Post #3 by @Mannitol (2025-09-02 11:08 UTC)

<p>Even I tried “nrrd”, “nii.gz” and “nii”, but none of them worked.</p>

---
