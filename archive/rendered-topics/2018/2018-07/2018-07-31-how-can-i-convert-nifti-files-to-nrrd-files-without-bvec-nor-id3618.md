# How can I convert NIFTI files to NRRD files without .bvec nor .bval files?

**Topic ID**: 3618
**Date**: 2018-07-31
**URL**: https://discourse.slicer.org/t/how-can-i-convert-nifti-files-to-nrrd-files-without-bvec-nor-bval-files/3618

---

## Post #1 by @Kyu_Sung_Choi (2018-07-31 13:39 UTC)

<p>Hello,</p>
<p>I am working with DSC NIFTI files, however I need to convert these into NRRD files.<br>
I know that there’s a module named DWIConvert, but I think you need .bvec or .bval files to use it.<br>
(Actually I have DSC dicom files, but after dcm2niix, no .bvec or .bval files are produced for my datasets.)<br>
So my question is,</p>
<ol>
<li>Is it possible to convert NIFTI files to NRRD files without .bvec nor .bval files?</li>
<li>If possible, then how can I do this?</li>
</ol>
<p>Thank you in advance!</p>

---

## Post #2 by @ihnorton (2018-07-31 14:40 UTC)

<aside class="quote no-group" data-username="Kyu_Sung_Choi" data-post="1" data-topic="3618">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/b77776/48.png" class="avatar"> Kyu_Sung_Choi:</div>
<blockquote>
<p>Is it possible to convert NIFTI files to NRRD files without .bvec nor .bval files?</p>
</blockquote>
</aside>
<p>For non-diffusion MR images, yes. You can also load those .nii file directly in Slicer without an intermediate NRRD conversion step.</p>
<p>(the nii/bvec/bval file set is for diffusion weighted imaging, and bvec/bval is necessary to convert a nifti-DWI volume to a nrrd-DWI volume; they store the gradient and b value information)</p>
<aside class="quote no-group" data-username="Kyu_Sung_Choi" data-post="1" data-topic="3618">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/b77776/48.png" class="avatar"> Kyu_Sung_Choi:</div>
<blockquote>
<p>Actually I have DSC dicom files, but after dcm2niix, no .bvec or .bval files are produced for my datasets.</p>
</blockquote>
</aside>
<p>dcm2niix will only create bvec/bval pairs for diffusion weighted MR images.</p>

---

## Post #3 by @Kyu_Sung_Choi (2018-08-01 00:45 UTC)

<p>Thank you for your answer, Isaiah.<br>
I misunderstood that DSC images are diffusion weighted images, which is totally not.</p>
<p>Actually I have hundreds of nifti files to convert.<br>
Could you please let me know how to save nifti files into nrrd files <strong>in command lines?</strong><br>
Thank you in advance!</p>

---
