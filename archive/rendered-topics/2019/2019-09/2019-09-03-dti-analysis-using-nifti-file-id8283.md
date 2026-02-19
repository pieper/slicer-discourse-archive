---
topic_id: 8283
title: "Dti Analysis Using Nifti File"
date: 2019-09-03
url: https://discourse.slicer.org/t/8283
---

# DTI Analysis using Nifti file

**Topic ID**: 8283
**Date**: 2019-09-03
**URL**: https://discourse.slicer.org/t/dti-analysis-using-nifti-file/8283

---

## Post #1 by @nirav (2019-09-03 19:27 UTC)

<p>Hello Everyone,</p>
<p>I am working with the .nii files to perform the DTI analysis and the .nii images are converted from Bruker file using Matlab. The problem I am facing is when using the Volumes module the software is not able to detect the diffusion component to select different components (the file format used: 4D nifti with 4th dimension as the 11 images from B0 to B10). I’d really appreciate if anyone can help with the issue I am facing. I can send a link to the file if required.</p>
<p>If it is not possible to use the .nii files for DTI analysis in Slicer then is there a way to convert Bruker file to .nrrd?</p>

---

## Post #2 by @ljod (2019-09-03 20:07 UTC)

<p>You can try the SlicerDMRI DWIConvert module for nifti to nrrd. Another option is if you have bruker DICOM, the dcm2nii program can now output nrrd files.</p>

---

## Post #3 by @Chris_Rorden (2019-09-03 20:13 UTC)

<p>I think you will need to work with Bruker for a solution. Last I checked, there were two errors in the Bruker DWI DICOM files that made them <a href="https://github.com/pnlbwh/conversion" rel="nofollow noopener">unsuitable</a> for analysis.</p>
<ol>
<li>The DICOM public tags are supposed to store [xx,xy,xz,yy,yz,zz], but Bruker has saved [xx,xy,xz,yx,yy,yz]. Unfortunately, you can not reconstruct the B-matrix from this.</li>
<li>Second, they only provide the B-Matrix, not the gradient vector. While the vector [1,0,0] and [-1,0,0] generate the same B-matrix, they have different eddy currents (which tools like FSL’s Eddy leverage).</li>
</ol>
<p>If all of your scans were acquired with slice angulation orthogonal to the scanner bore, you can probably insert a single gradient table you can extract.</p>
<p>Alternatively, if you have the Bruker-format data (rather than DICOM) there may be a way to extract the gradient directions. The new <a href="https://github.com/neurolabusc/Bru2Nii/issues/24" rel="nofollow noopener">ParaVision 360</a> should allow export to NIfTI, and you could use <a class="mention" href="/u/tbillah">@tbillah</a>’s <a href="https://github.com/pnlbwh/conversion" rel="nofollow noopener">Python conversion scripts</a> to convert the NIfTI (with FSL bvec/bval) to NRRD format (with embedded gradient directions).</p>
<p>I would contact your Bruker research collaboration manager for help on this. It is a professional product and they have an obligation to stand by their DICOM conformance statement.</p>

---
