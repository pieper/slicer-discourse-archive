---
topic_id: 26864
title: "Whats Wrong With My Dwi Failed To Convert From Dwi To Tensor"
date: 2022-12-21
url: https://discourse.slicer.org/t/26864
---

# What's wrong with my DWI? Failed to convert from DWI to tensors

**Topic ID**: 26864
**Date**: 2022-12-21
**URL**: https://discourse.slicer.org/t/whats-wrong-with-my-dwi-failed-to-convert-from-dwi-to-tensors/26864

---

## Post #1 by @peter_adidharma (2022-12-21 01:49 UTC)

<p>Hi all,</p>
<p>I’ve been working to do some tractography using slicerDMRI, but seems to encounter the same problem with all DWI files that i have as i failed to convert it to tensors. Here, I attached the .nrrd file of our DWI.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://www.dropbox.com/s/5uk42u9c3itt8ls/dwi.nrrd?dl=0">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/metaserver/static/images/favicon-vfl8lUR9B.ico" class="site-icon" width="32" height="32">

      <a href="https://www.dropbox.com/s/5uk42u9c3itt8ls/dwi.nrrd?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>

  <article class="onebox-body">
    <img src="https://www.dropbox.com/static/metaserver/static/images/spectrum-icons/generated/content/content-unknown-large.png" class="thumbnail onebox-avatar" width="160" height="160">

<h3><a href="https://www.dropbox.com/s/5uk42u9c3itt8ls/dwi.nrrd?dl=0" target="_blank" rel="noopener nofollow ugc">dwi.nrrd</a></h3>

  <p>Shared with Dropbox</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Can anyone point out whats wrong with my DWI?</p>
<p>Really appreciate your help.</p>
<p>Regards,<br>
Peter</p>

---

## Post #2 by @pieper (2022-12-21 16:53 UTC)

<p>If you look at the header you can see that there’s only one volume (a baseline, with gradient 0,0,0).  For tractography you typically need dozens of gradients at different angles.</p>
<pre data-code-wrap="NRRD0005"><code class="lang-plaintext"># Complete NRRD file format specification at:
# http://teem.sourceforge.net/nrrd/format.html
type: short
dimension: 3
space: right-anterior-superior
sizes: 160 160 25
space directions: (-1.3536703538588315,-0.23908993262719125,0.032211445171427509) (0.24112542786612504,-1.3467566568679989,0.13685771888390255) (0.029318512241917394,0.53090466025518757,5.1727440171111505)
kinds: domain domain domain
endian: little
encoding: gzip
space origin: (99.988388696114995,105.71384036457,-55.297402783850025)
measurement frame: (-1,0,0) (0,-1,0) (0,0,1)
DICOM_0008_0060_Modality:=MR
DICOM_0008_0070_Manufacturer:=SIEMENS
DICOM_0008_1090_ManufacturerModelName:=Skyra
DICOM_0018_0022_ScanOptions:=FS
DICOM_0018_0023_MRAcquisitionType:=2D
DICOM_0018_0080_RepetitionTime:=5500
DICOM_0018_0081_EchoTime:=64
DICOM_0018_0083_NumberOfAverages:=1
DICOM_0018_0087_MagneticFieldStrength:=3
DICOM_0018_1020_SoftwareVersions:=syngo MR E11
DICOM_0018_1314_FlipAngle:=180
DWMRI_b-value:=0
DWMRI_gradient_0000:=0   0   0
modality:=DWMRI


</code></pre>

---

## Post #3 by @peter_adidharma (2022-12-22 04:38 UTC)

<p>Thank you for the reply. Do you have any suggestion on what to change in the process of doing the MRI?</p>

---

## Post #4 by @pieper (2022-12-22 13:40 UTC)

<p>Acquiring diffusion MRI in a form compatible with tractography is a complex process, and the detail vary a lot by scanner type.  Generally speaking you would want dozens of gradient directions and usually there will be a standard sequence from the scanner vendor the provides good results.</p>

---
