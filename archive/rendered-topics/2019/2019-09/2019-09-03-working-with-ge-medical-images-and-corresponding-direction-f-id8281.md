---
topic_id: 8281
title: "Working With Ge Medical Images And Corresponding Direction F"
date: 2019-09-03
url: https://discourse.slicer.org/t/8281
---

# Working with GE medical images and corresponding direction file

**Topic ID**: 8281
**Date**: 2019-09-03
**URL**: https://discourse.slicer.org/t/working-with-ge-medical-images-and-corresponding-direction-file/8281

---

## Post #1 by @mshah (2019-09-03 18:57 UTC)

<p>Hello,</p>
<p>I am working with a set of GE medical DTI and DWI images. It seems that the directional gradients (in 26 directions) of these images are a in a separate .txt file. If these anyway I can integrate these directions with the signal intensity per voxel within the image itself to extract the 3x3 diffusion tensor matrixes per voxel? Is there anyway I can do this in slicer?</p>
<p>Thank you!</p>

---

## Post #2 by @pieper (2019-09-03 20:02 UTC)

<p>If you are working at that level, you need to take into account the material on this page:</p>
<p><a href="https://na-mic.org/wiki/NAMIC_Wiki:DTI:Nrrd_format" class="onebox" target="_blank" rel="nofollow noopener">https://na-mic.org/wiki/NAMIC_Wiki:DTI:Nrrd_format</a></p>

---

## Post #3 by @Chris_Rorden (2019-09-03 20:03 UTC)

<p>If you have the original GE DICOM data, the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/SlicerDcm2nii" rel="nofollow noopener">SlicerDcm2nii extension</a> should be able to create NRRD files that have the diffusion gradients and b-values embedded. Alternatively, you could use <a href="https://github.com/rordenlab/dcm2niix" rel="nofollow noopener">dcm2niix</a> directly from the command line to convert GE DICOM files to either NIfTI (with FSL format *.bvec, *.bval) or NRRD (with embedded gradients).</p>
<p>If the gradients really are not included in the DICOMs (which I have not seen before), you would have to convert your text files. <a class="mention" href="/u/tbillah">@tbillah</a>’s <a href="https://github.com/pnlbwh/conversion" rel="nofollow noopener">Python conversion</a> scripts would be a good starting point. Just make sure you get the correct frame of reference for the tool you will be using.</p>

---

## Post #4 by @mshah (2019-09-03 20:35 UTC)

<p>Hi thank you for the response,</p>
<p>They are not embedded, as in slicer I am not able to attain a DWI component and the array of information from the image is a matrix of scalar values. In the Python conversion, would these commands to convert to nrrd embed the information into the image? How could I embed the directional information into the image so I can read it in slicer?</p>

---

## Post #5 by @Chris_Rorden (2019-09-03 22:34 UTC)

<p>I would suggest running dcmdump or gdcmdump on one of your DWI images. You should inspect the DICOM tags to ensure the <a href="https://na-mic.org/wiki/NAMIC_Wiki:DTI:DICOM_for_DWI_and_DTI" rel="nofollow noopener">DWI fields</a> are indeed missing:</p>
<pre><code>Public Tags
0018,9075 : Diffusion Directionality
0018,9076 : Diffusion Gradient Direction Sequence
0018,9087 : Diffusion b-value
0018,9089 : Diffusion Gradient Orientation
0018,9117 : MR Diffusion Sequence
0018,9147 : Diffusion Anisotropy Type
Private Tags
0019,10e0 : # DTI diffusion directions (release 10.0 &amp; above)
0019,10df : # DTI diffusion directions (release 9.0 &amp; below)
0019,10d9 : Concatenated SAT {# DTI Diffusion Dir., release 9.0 &amp; below}
0021,105A : diffusion direction
0043,1039 : Slop_int_6... slop_int_9: (in the GEMS_PARM_01 block)
</code></pre>
<p>If these are really missing, I would check the providence of your images to see if you can determine when these tags were removed. Your GE Research Collaboration Manager should be able to help.</p>
<p>If these are really missing, you need to determine the frame of reference used for the text files, as <a class="mention" href="/u/pieper">@pieper</a> notes. There are no off-the shelf tools to do this, but <a class="mention" href="/u/tbillah">@tbillah</a>’s Python scripts would provide a good starting point.</p>

---

## Post #6 by @mshah (2019-09-03 22:57 UTC)

<p>Hello,</p>
<p>Again thank you for the response, I have been trying to figure out how to work with this data for quite some time now so it is very much appreciated! All tags are missing except for (0019,10d9) , (0021,105A), and (0043,1039). The thing that is confusing me most is the patients data I am working with is a stack of 26 images, therefore the directional data should be compatible with 26 directions. However tag (0021,105A) that gives the diffusion direction in the meta data says that it is in 16 directions (or 7 or simply a number that is not 26 depending on the patient and imaging sequence). Have you ever seen this before? I am working with the IvyGap glioblastoma data base, which is a common data base so I cannot figure out why these irregularities exist. I have attached the links to the dwi and dti images of patient w13 in the data base for referance.<br>
<aside class="onebox googledrive">
  <header class="source">
      <a href="https://drive.google.com/file/d/1oVaihj795rk-9Sqg7-gyuq9C5rOZTKgO/view" target="_blank" rel="nofollow noopener">drive.google.com</a>
  </header>
  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1oVaihj795rk-9Sqg7-gyuq9C5rOZTKgO/view" target="_blank" rel="nofollow noopener"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1oVaihj795rk-9Sqg7-gyuq9C5rOZTKgO/view" target="_blank" rel="nofollow noopener">4-AX EPI DWI-45431.zip</a></h3>

<p>Google Drive file.</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
<br>
<aside class="onebox googledrive">
  <header class="source">
      <a href="https://drive.google.com/file/d/1RUM-YGp01-3h2YgCBsOEEjzZRL9wNGTp/view" target="_blank" rel="nofollow noopener">drive.google.com</a>
  </header>
  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1RUM-YGp01-3h2YgCBsOEEjzZRL9wNGTp/view" target="_blank" rel="nofollow noopener"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1RUM-YGp01-3h2YgCBsOEEjzZRL9wNGTp/view" target="_blank" rel="nofollow noopener">5-AX EPI DTI-36289.zip</a></h3>

<p>Google Drive file.</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---

## Post #7 by @Rodrigo_Visconti (2019-09-04 10:35 UTC)

<p>This extension runs on ultrasound data?</p>

---

## Post #8 by @Chris_Rorden (2019-09-04 15:29 UTC)

<p>The latest version of dcm2niix (v1.0.20190902) will extract the gradient directions and amplitudes from these files - either to NIfTI (with FSL bvec/bval files) or NRRD (with Slicer-format gradients embedded in the NRRD header file).</p>
<p>You should be able to access dcm2niix by installing the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/SlicerDcm2nii" rel="nofollow noopener">SlicerDcm2nii extension</a> - creating the module Dcm2niixGUI. I am not sure if this has been updated to support the latest version of dcm2niix.</p>
<p>Alternatively, you can</p>
<ul>
<li>
<a href="https://github.com/rordenlab/dcm2niix/releases" rel="nofollow noopener">Run the latest release of dcm2niix from the command line</a>.</li>
<li>
<a href="https://github.com/rordenlab/MRIcroGL12/releases" rel="nofollow noopener">Run the latest release of dcm2niix from the MRIcroGL graphical interface (Import menu)</a>.</li>
</ul>

---

## Post #9 by @Chris_Rorden (2019-09-04 17:57 UTC)

<p>In theory, ultra-sound DICOMs should be supported. However, most development has been with MR, so CT and US may be more problematic. If you have any issues, please generate a new issue on the <a href="https://github.com/rordenlab/dcm2niix" rel="nofollow noopener">dcm2niix Github page</a>.</p>

---

## Post #10 by @lassoan (2019-09-04 20:24 UTC)

<p>Even though standard DICOM tags exist for storing 3D/4D ultrasound information, most ultrasound systems, including GE, store these images in private tags and they only give you the tag definitions if you sign a non-disclosure agreement. I don’t think dcm2niix can read ultrasound from these private tags. If you install <a href="https://github.com/SlicerHeart/SlicerHeart" rel="nofollow noopener">SlicerHeart extension</a> then you can import some of these 3D/4D ultrasound images.</p>

---
