---
topic_id: 6576
title: "Importing Dwi File"
date: 2019-04-23
url: https://discourse.slicer.org/t/6576
---

# Importing DWI file 

**Topic ID**: 6576
**Date**: 2019-04-23
**URL**: https://discourse.slicer.org/t/importing-dwi-file/6576

---

## Post #1 by @amymanson (2019-04-23 13:59 UTC)

<p>Hi, I am trying to import some DWI data into Slicer.<br>
I have successfully done this in the past using .nrrd files. This new data is .nii and seems to load fine but in the Diffusion Brain Masking module it is not found as a potential Input DWI Volume, so cannot be used.<br>
Do you know why this may not be working correctly, or if I have to go through any other steps first?<br>
Thank you!</p>

---

## Post #2 by @MSpindler (2019-04-30 09:13 UTC)

<p>Hi!<br>
Is it a .nii or a .nii.gz file? (I dont think it is possible to use “.nii” files, DWI data should not be converted to a single .nii file.)<br>
For DWI data not in .nrrd format, you can use the DWIConvert module.  Here you can either use the DICOMS or FSL files (.nii.gz).</p>
<p>To get the .nii.gz file, you can convert the DICOMs using dcm2niix (<a href="https://github.com/rordenlab/dcm2niix" rel="nofollow noopener">https://github.com/rordenlab/dcm2niix</a>). But you could also directly convert to .nrrd (implemented in the newest build for dcm2niix as command-line option, not implemented in the GUI of mricrogl). Does that help?</p>

---

## Post #3 by @amymanson (2019-04-30 09:48 UTC)

<p>Thanks, I have a lot of files and not really sure which I’m supposed to be using.<br>
It’s NIH data from their online repository.<br>
I have attached some screenshots of what I have. This is all in a folder labelled “dti”. I just want some kind of DWI file that I can input into Slicer to work on.<br>
Any help would be much appreciated!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/39c1b6d31614277b36ac0f69ed34017e99841c82.png" data-download-href="/uploads/short-url/8eWfhuuDGJpmCTmVmGthZJF247w.png?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/39c1b6d31614277b36ac0f69ed34017e99841c82.png" alt="Capture" data-base62-sha1="8eWfhuuDGJpmCTmVmGthZJF247w" width="690" height="434" data-dominant-color="F7F7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">793×499 28.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @MSpindler (2019-04-30 11:07 UTC)

<p>Is the raw data format stated somewhere where you downloaded the files? I think you need to work on the raw data (either corrected or uncorrected, dont know what correction that is…).</p>

---

## Post #5 by @amymanson (2019-04-30 11:28 UTC)

<p>Thanks, I thought that but didn’t know how or which files!<br>
This is the information I have for the data:</p>
<p>DTI (3 mm resolution): 498 datasets from 274 subjects<br>
Expanded DTI (2.5 mm resolution): 193 datasets from 152 subjects<br>
Diffusion-weighted images<br>
Raw images (native resolution and orientation)<br>
Processed/corrected images (motion and distortion corrected)<br>
Reoriented to a standardized reference frame<br>
Resampled to 2mm isotropic resolution<br>
Tensor-derived quantities<br>
Diffusion tensor elements computed from corrected images<br>
Trace of diffusion tensor (equal to 3x mean<br>
diffusivity)<br>
Eigenvalues<br>
Fractional anisotropy index<br>
Lattice anisotropy index<br>
Directionally encoded color (DEC) maps</p>
<p>This Diffusion Tensor Imaging (DTI) data release contains data collected with higher resolution (2.5mm)<br>
acquisition protocol and data collected with lower resolution (3mm) or the “conventional” DTI protocol.<br>
DTI data was sometimes collected in sessions that were separated from the other measure in time.<br>
When this occurred, a visit number was assigned based on age and proximity to the other data<br>
acquisitions. In some instances, the corresponding clinical/behavioral data for that visit number may be<br>
unavailable.<br>
For the low resolution DTI data, two sets of data are available for download; DTI release 1 (REL01)<br>
contains datasets that were virtually artifact‐free and therefore did not need additional post‐processing<br>
with artifact remediation strategies (85 scans from 62 unique subjects), while DTI release 2 (REL02)<br>
contains all DTI data that passed set quality criteria (498 scans from 274 unique subjects).<br>
The higher resolution, expanded DTI (eDTI) data includes low (b=0s/mm2) and high (b=1100s/mm2)<br>
image volumes, but also includes a number of intermediate b‐values as well (b=100s/mm2, b=300s/mm2, b=500s/mm2, and b=800s/mm2). Up to nine (9) files of tensor derived quantities are included in the database: Directionally encoded color maps (DEC); Eigenvalues (EV) as 4D image file with volumes in the order of λ1, λ2, λ3; Fractional anisotropy (FA); Lattice index (LI); Relative anisotropy (RA); Trace of the diffusion tensor (TR) (equal to 3*Mean Diffusivity); Chi‐Squared map of the fitting (CS) – a measure of the goodness of fit of the tensor model; Outlier map (OUT) – indicates the percentage of data points identified as outliers and removed from the tensor fitting on a voxel‐by‐voxel basis; and Brain mask (MS).</p>

---

## Post #6 by @amymanson (2019-04-30 11:30 UTC)

<p>I think the NIH researchers used the programme TORTOISE to convert the raw (presumably DICOM) data into the files that I have. I’ve attempted to look into using TORTOISE to open or convert what I have but have not really managed to progress anywhere with that.</p>

---

## Post #7 by @MSpindler (2019-04-30 11:38 UTC)

<p>What do you want to do with the data?<br>
My guess would be that the “0001”,“0002”… files are DICOM files (or other…), but windows does not recognize the format, hence the weird datatype.<br>
Try importing these files using dcm2nii or other converter software (all files for one subject) into nii.gz.<br>
This should result in datafiles as well as bvalue and bvector files. (I cant find these in your folder structure, so you probably have to start from the raw data).</p>

---

## Post #8 by @amymanson (2019-04-30 11:48 UTC)

<p>Thank you, I’ll give that a go!<br>
I’m just wanting to look at the tractography of the brains and do some measurements of tracts. Ive done this with other data, but was just really struggling with the file structure here.</p>

---

## Post #9 by @ljod (2019-04-30 11:51 UTC)

<p>Try looking in the RAW_CPRRECTED folder. You want the raw data (DWI) with their corrections (eddy current etc.)</p>

---

## Post #10 by @MSpindler (2019-04-30 11:56 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/780cf057a7db153d3b29497c7ef8643e2828ebb3.png" data-download-href="/uploads/short-url/h8116mLnI5eqB05u0G2OSmVxxsv.png?dl=1" title="Capture5" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/780cf057a7db153d3b29497c7ef8643e2828ebb3.png" alt="Capture5" data-base62-sha1="h8116mLnI5eqB05u0G2OSmVxxsv" width="690" height="440" data-dominant-color="F7F7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture5</span><span class="informations">817×521 36.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div> yep, that’s the one.</p>

---

## Post #11 by @amymanson (2019-04-30 13:35 UTC)

<p>I have multiple folders of what I assume are DICOM files for each scan of each person. Would I be able to load these multiple folders into dcm2nii? I’ve not used this programme before</p>

---

## Post #12 by @MSpindler (2019-04-30 13:47 UTC)

<p>Maybe just try it out to see if the images are really DICOM.</p>
<p>dcm2nii searches DICOM files throughout subfolders, unless you say otherwise. So which files/folders are included depends on which folder you use as inputfolder.<br>
You can use mricrogl if you are unfamiliar with the program and want to have a GUI for dcm2nii: <a href="https://www.nitrc.org/frs/?group_id=889" rel="nofollow noopener">https://www.nitrc.org/frs/?group_id=889</a><br>
(but converting to .nrrd is not supported there yet, only .nii.gz)</p>

---

## Post #13 by @Chris_Rorden (2019-04-30 19:33 UTC)

<p>Presuming you still have the DICOMs, the easiest solution is probably to use dcm2niix to export the DICOM’s to Slicer’s preferred NRRD format (use ‘-e y’ to export to this format).</p>
<p>Option 1:<br>
install the <a>SlicerDcm2nii</a></p>
<p>Option 2:<br>
You will want to make sure you get the latest release of dcm2niix <a href="https://github.com/rordenlab/dcm2niix/releases" rel="noopener nofollow ugc">v1.0.20190410</a> as NRRD support is new. Assuming you have the latest version, you can run this command line option, which will export to NRRD and set the output filename to be the series number followed by the protocol name:</p>
<blockquote>
<p>dcm2niix -e y -f %s_%p c:\dti04\1013</p>
</blockquote>
<p>Option 3:<br>
For the upcoming releases of MRIcroGL and MRIcron, you can go to the Import/ConvertDICOMtoNIfTI menu item and select NRRD from the “Output Format” pull down menu (choose either compressed or uncompressed NRRD). The new graphical interface allows you to select the different options, includes tooltips, remembers your preferences, and your selections build a command line that is also displayed. That way you can use the graphical interface all the time if you want, or use it to design a command line for your own scripts.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78eaf268cf0a409fa6992e1f95bcc11a54f9b76e.png" alt="dcm2niix_gui" data-base62-sha1="hfGFpn4OOqADgoQwAyzQ3oxOdci" width="448" height="461"></p>

---

## Post #14 by @ljod (2019-04-30 20:58 UTC)

<p>Thanks Chris!<br>
For option <span class="hashtag">#1</span>, SlicerDCM2nii is available through the extension manager.</p>

---

## Post #15 by @amymanson (2019-05-23 12:26 UTC)

<p>Thank you all for your suggestions!<br>
I’ve only just now had a chance to actually implement your suggestions - I’m having difficulty opening DICOMs in MRIcroGL (other files that I know are definitely DICOMs). I’ve tried just dragging and dropping onto the main window and also tried using the dcm2nii converter within MRIcroGL with no success. Does anyone have any idea where I’m going wrong?<br>
Thanks again!</p>

---

## Post #16 by @ljod (2019-05-23 12:43 UTC)

<p>Hi! If you use the nightly Slicer version we have a new dcm2nii module in the extension manager. It will load DICOM DWI data directly into Slicer. We’re working on a tutorial and in the meantime if you have questions please ask here.</p>
<p>Note the module requires your DWI to be the only data in its folder. There’s a DICOM patcher Module that can help with that. See a recent post on the forum about it.</p>

---

## Post #17 by @R_Lin (2023-06-07 09:52 UTC)

<p>Hi, I wonder if it’s possible to work with nifti format in Slicer as well? I encountered the same problem, the nifti file loaded is not detected in 3D sclicer. And sadly I have only nifti files at hand, no DICOM…</p>

---

## Post #18 by @pieper (2023-06-07 14:54 UTC)

<p><a class="mention" href="/u/r_lin">@R_Lin</a> if you have a dwi file in nifti with bval and bvec files, you might be able to use this experimental loader.  You’ll need to add the module to your module path or put it in the right directory and reload Slicer.  Let us know if it works for you.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/pieper/SlicerDMRI/blob/nifiio/Modules/Scripted/NIfTIFile/NIfTIFile.py">
  <header class="source">

      <a href="https://github.com/pieper/SlicerDMRI/blob/nifiio/Modules/Scripted/NIfTIFile/NIfTIFile.py" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/pieper/SlicerDMRI/blob/nifiio/Modules/Scripted/NIfTIFile/NIfTIFile.py" target="_blank" rel="noopener">pieper/SlicerDMRI/blob/nifiio/Modules/Scripted/NIfTIFile/NIfTIFile.py</a></h4>


      <pre><code class="lang-py">import logging
import os
import unittest
import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *

class NIfTIFile(ScriptedLoadableModule):
  def __init__(self, parent):
    ScriptedLoadableModule.__init__(self, parent)
    parent.title = 'NIfTIFile'
    parent.categories = ['Testing.TestCases']
    parent.dependencies = []
    parent.contributors = ["Steve Pieper (Isomics)", ]
    parent.helpText = '''
    This module is used to implement diffusion nifti reading and writing using the conversion tool from PNL at BWH.
    '''
    parent.acknowledgementText = '''
    Thanks to:

    Billah, Tashrif; Bouix; Sylvain; Rathi, Yogesh; Various MRI Conversion Tools, https://github.com/pnlbwh/conversion, 2019, DOI: 10.5281/zenodo.2584003
</code></pre>



  This file has been truncated. <a href="https://github.com/pieper/SlicerDMRI/blob/nifiio/Modules/Scripted/NIfTIFile/NIfTIFile.py" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #19 by @R_Lin (2023-06-08 01:03 UTC)

<p>Thank you for your reply! That works! I also found there’s a DWIConvert tool in 3D slicer that does the trick too.</p>

---
