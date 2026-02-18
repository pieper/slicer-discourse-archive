# Failure to load rodent DWI data

**Topic ID**: 14719
**Date**: 2020-11-20
**URL**: https://discourse.slicer.org/t/failure-to-load-rodent-dwi-data/14719

---

## Post #1 by @rcknickmeyer (2020-11-20 22:25 UTC)

<p>I am trying to load diffusion weighted images into Slicer. These are mouse images acquired on a Bruker 7T. When I try to load the DICOM images using the “import DICOM files” function this is what happens:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a6198fedd4ae0f9b6470fabd64f7e52cb7670725.jpeg" data-download-href="/uploads/short-url/nHo1Fq1QBXo8GfrsWbFbOrWov0F.jpeg?dl=1" title="Screenshot_DTI_loading_issue" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a6198fedd4ae0f9b6470fabd64f7e52cb7670725_2_664x500.jpeg" alt="Screenshot_DTI_loading_issue" data-base62-sha1="nHo1Fq1QBXo8GfrsWbFbOrWov0F" width="664" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a6198fedd4ae0f9b6470fabd64f7e52cb7670725_2_664x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a6198fedd4ae0f9b6470fabd64f7e52cb7670725_2_996x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a6198fedd4ae0f9b6470fabd64f7e52cb7670725_2_1328x1000.jpeg 2x" data-dominant-color="4A4A57"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_DTI_loading_issue</span><span class="informations">3572×2688 693 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I tried using the DWI converter and received the following error:</p>
<p>Diffusion-weighted DICOM Import (DWIConvert) standard error:</p>
<p>Exception creating converter</p>
<p>itk::ExceptionObject (00000003AFAFD9A0)</p>
<p>Location: “unknown”</p>
<p>File: D:\D\S\Slicer-0-build\BRAINSTools\DWIConvert\GenericDWIConverter.cxx</p>
<p>Line: 13</p>
<p>Description: itk::ERROR: LoadFromDisk not relevant</p>
<p>I also asked the MRI technician to provide the files in NIfTI format.</p>
<p>She provided one version where the data was represented by a single file: this is what I get when I try to load it:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6fff592327d729f44774f8a3fa23ac53da3d7ab8.png" data-download-href="/uploads/short-url/fYM4YhNACE4Bc6wqCUSzAhuR8Ny.png?dl=1" title="Screenshot_NII_LOADING_ISSUE" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6fff592327d729f44774f8a3fa23ac53da3d7ab8_2_664x500.png" alt="Screenshot_NII_LOADING_ISSUE" data-base62-sha1="fYM4YhNACE4Bc6wqCUSzAhuR8Ny" width="664" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6fff592327d729f44774f8a3fa23ac53da3d7ab8_2_664x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6fff592327d729f44774f8a3fa23ac53da3d7ab8_2_996x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6fff592327d729f44774f8a3fa23ac53da3d7ab8_2_1328x1000.png 2x" data-dominant-color="6E2B37"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_NII_LOADING_ISSUE</span><span class="informations">3572×2688 85 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Another version included many different .nii files; when I try to load these as a batch nothing happens.</p>

---

## Post #2 by @pieper (2020-11-24 18:27 UTC)

<p>As you probably know DWI data formats, particularly from research scanners, are complex and highly variable.  Probably your best bet is to try <a href="https://github.com/rordenlab/dcm2niix">dcm2nii</a> either directly or with <a href="https://dmri.slicer.org">SlicerDMRI</a> (<a href="https://github.com/SlicerDMRI/SlicerDcm2nii">SlicerDcm2nii</a>)</p>

---
