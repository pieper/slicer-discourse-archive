# DWIconvert error

**Topic ID**: 10561
**Date**: 2020-03-05
**URL**: https://discourse.slicer.org/t/dwiconvert-error/10561

---

## Post #1 by @nabin (2020-03-05 16:55 UTC)

<p>Operating system: macos 10.14.6<br>
Slicer version: 4.10.2</p>
<p>Dear 3Dslicer team,</p>
<p>I am trying to visualize a FSL output file in slicer. I am trying to convert the output nifti file to .nrrd format using DWIconvert but unfortunately does not work. It says the gradients does not match the volumes. I ran the whole process with FSL and there was no problem, so was wondering what could be wrong with my bvectors. Or am I missing something here. Your hint would be very much appreciated.<br>
Thank you.</p>
<p>Error message:</p>
<p><em>Diffusion-weighted DICOM Import (DWIConvert) standard error:</em></p>
<p><em>libc++abi.dylib: terminating with uncaught exception of type itk::ExceptionObject: /Volumes/Dashboards/Stable/Slicer-4102-build/BRAINSTools/DWIConvert/DWIConvertLib.cxx:108:</em></p>
<p><em>itk::ERROR: Exception creating converter</em></p>
<p><em>itk::ExceptionObject (0x7fe6b0f79f70)</em></p>
<p><em>Location: “unknown”</em></p>
<p><em>File: /Volumes/Dashboards/Stable/Slicer-4102-build/BRAINSTools/DWIConvert/DWIConverter.cxx</em></p>
<p><em>Line: 227</em></p>
<p><em>Description: itk::ERROR: number of Gradients doesn’t match number of volumes:129 != 1</em></p>

---

## Post #2 by @pieper (2020-03-05 20:26 UTC)

<p>You can try dcm2niix, which supports both nifti and nrrd.  It is available stand-alone or part of <a>SlicerDMRI</a>.<br>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicon.ico" class="site-icon" width="16" height="16">
      <a href="https://github.com/rordenlab/dcm2niix" target="_blank">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars2.githubusercontent.com/u/22748159?s=400&amp;v=4" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://github.com/rordenlab/dcm2niix" target="_blank">rordenlab/dcm2niix</a></h3>

<p>dcm2nii DICOM to NIfTI converter: compiled versions available from NITRC - rordenlab/dcm2niix</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---
