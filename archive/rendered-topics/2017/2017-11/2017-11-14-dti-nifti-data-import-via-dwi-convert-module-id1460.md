# DTI Nifti data import via DWI Convert Module

**Topic ID**: 1460
**Date**: 2017-11-14
**URL**: https://discourse.slicer.org/t/dti-nifti-data-import-via-dwi-convert-module/1460

---

## Post #1 by @DTI (2017-11-14 23:48 UTC)

<p>Hi</p>
<p>I am trying to import DTI data (connectome nifti format) into slicer with the DWI NiftiFSL to Nrrd Converter (Mac OS X 10.12.6, Slicer 4.9). It runs for 120s, but completes with errors*.</p>
<hr>
<p>*Diffusion-weighted DICOM Import (DWIConvert) standard error:</p>
<p>libc++abi.dylib: terminating with uncaught exception of type itk::ExceptionObject: /Users/kitware/Dashboards/Nightly/Slicer-0-build/BRAINSTools/DWIConvert/DWIConvertLib.cxx:108:<br>
itk::ERROR: Exception creating converter<br>
itk::ExceptionObject (0x103e03ae8)<br>
Location: "unknown"<br>
File: /Users/kitware/Dashboards/Nightly/Slicer-0-build/BRAINSTools/DWIConvert/DWIConverter.cxx<br>
Line: 220<br>
Description: itk::ERROR: Mismatch between count of B Vectors (1) and B Values (143)</p>
<hr>
<p>I already tried to reformat the bval and bvec files into columns (delimiter ‘,’ or ’ '), but it still doesn’t work.</p>
<p>Can you tell me, in what format the bval and bvec files have to be to work?</p>
<p>Thank you very much,<br>
Best regards,</p>
<p>Lorenz</p>

---

## Post #2 by @ihnorton (2017-11-15 03:07 UTC)

<p>What tool did you use to create your NIfTI file(s)? There are several flavors of NIfTI-dwi.</p>
<p>The format supported by DWIConvert is FSL-style, which is also the default output style of dcm2nii. Space-delimited columns, newline-delimited rows; bvec rows correspond to x/y/z column components respectively.</p>
<p>e.g.:</p>
<p>file.bval</p>
<pre><code class="lang-auto">0 1000 1000 1000 ...
</code></pre>
<p>file.bvec</p>
<pre><code class="lang-auto">x1 x2 x3 x4 ...
y1 y2 y3 y4 ...
z1 z2 z3 z4 ...
</code></pre>
<p>(there is also a transpose vectors option available for compatibility with some similar software, which will have one b-value per row in file.bval, and one vector per row in file.bvec)</p>

---

## Post #3 by @DTI (2017-11-15 15:48 UTC)

<p>Thank you! That worked. I was able to load the images.<br>
Unfortunately, I have one further question: The now imported images appear side by side when I scroll through them instead of one after the other (see video <a href="https://www.dropbox.com/s/jn6s11njj9c3w5s/nifti.mov?dl=0" rel="nofollow noopener">https://www.dropbox.com/s/jn6s11njj9c3w5s/nifti.mov?dl=0</a>). How can I fix this?<br>
Thank you again, Lorenz</p>

---

## Post #4 by @ihnorton (2017-11-15 16:39 UTC)

<p>I’ve seen something similar when DWIConvert loaded a NIfTI with the wrong ITK reader. It could also happen if the strides are wrong because the expected image/slice count doesn’t match the predicted image count based on the header, for some reason.</p>
<p>However, I’m surprised to see a coronal view in the “red” slice viewer, because that is axial by default. Did you change it to coronal? If not, perhaps that is an indication that the orientations are not being interpreted correctly. Was your data acquired as coronal slices?</p>
<p>I can take a look if you are able to share some (anonymized) data. If you prefer to share directly rather than publicly, please share to <code>inorton at partners dot org</code> from dropbox/onedrive/etc.</p>
<p><strong>EDIT: also, if you share data, <em>please indicate what software was used to convert it</em></strong></p>

---
