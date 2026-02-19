---
topic_id: 3895
title: "Diffusion Weighted Dicom Import Dwiconvert Standard Error"
date: 2018-08-26
url: https://discourse.slicer.org/t/3895
---

# Diffusion-weighted DICOM Import (DWIConvert) standard error?

**Topic ID**: 3895
**Date**: 2018-08-26
**URL**: https://discourse.slicer.org/t/diffusion-weighted-dicom-import-dwiconvert-standard-error/3895

---

## Post #1 by @cyufu (2018-08-26 04:35 UTC)

<p>Operating system：Windows 10<br>
Slicer version:4.9.0（2018-08-04）<br>
DTI data of the United Imaging 3.0T （China）</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a349fc89e920c2b34168ea8ebce5a74ef803f107.png" data-download-href="/uploads/short-url/niwlgqIR9XIwHnCuVMM3yh9pXLh.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a349fc89e920c2b34168ea8ebce5a74ef803f107_2_690x151.png" alt="image" data-base62-sha1="niwlgqIR9XIwHnCuVMM3yh9pXLh" width="690" height="151" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a349fc89e920c2b34168ea8ebce5a74ef803f107_2_690x151.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a349fc89e920c2b34168ea8ebce5a74ef803f107.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a349fc89e920c2b34168ea8ebce5a74ef803f107.png 2x" data-dominant-color="E0E1E2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">784×172 17.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/394b2ff89d559efddfd833e39c577c3c399c11c5.png" data-download-href="/uploads/short-url/8aQiQLCxrjQ7ZKpi75aJ0DRuAhn.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/394b2ff89d559efddfd833e39c577c3c399c11c5_2_545x499.png" alt="image" data-base62-sha1="8aQiQLCxrjQ7ZKpi75aJ0DRuAhn" width="545" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/394b2ff89d559efddfd833e39c577c3c399c11c5_2_545x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/394b2ff89d559efddfd833e39c577c3c399c11c5_2_817x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/394b2ff89d559efddfd833e39c577c3c399c11c5.png 2x" data-dominant-color="F6F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1022×937 42.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<pre><code class="lang-auto">Diffusion-weighted DICOM Import (DWIConvert) standard error:

Exception creating converter 
itk::ExceptionObject (0000009A0518B610)
Location: "unknown" 
File: D:\D\P\Slicer-0-build\BRAINSTools\DWIConvert\GenericDWIConverter.cxx
Line: 13
Description: itk::ERROR:  LoadFromDisk not relevant

Diffusion-weighted DICOM Import (DWIConvert) standard output:

======= DWI Convert Public Lib Ctest =========
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6ef36e32726ecb6e22b42ff8f0191f4527c024e3.png" data-download-href="/uploads/short-url/fPw4hC9YN9WbuPlRMK40RG2etvZ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6ef36e32726ecb6e22b42ff8f0191f4527c024e3.png" alt="image" data-base62-sha1="fPw4hC9YN9WbuPlRMK40RG2etvZ" width="690" height="291" data-dominant-color="EAF1F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1102×465 12.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<pre><code class="lang-auto">Found CommandLine Module, target is  C:/Program Files/Slicer 4.9.0-2018-08-04/bin/../lib/Slicer-4.9/cli-modules/DWIConvert.exe
ModuleType: CommandLineModule
Diffusion-weighted DICOM Import (DWIConvert) command line: 

C:/Program Files/Slicer 4.9.0-2018-08-04/bin/../lib/Slicer-4.9/cli-modules/DWIConvert.exe --conversionMode DicomToNrrd --outputVolume C:/Users/Cyufu/AppData/Local/Temp/Slicer/BBDCA_vtkMRMLDiffusionWeightedVolumeNodeB.nrrd --inputDicomDirectory D:/3DSlicer Data/DTI/20180826 XU Kaiyu/epi_dti_20180823 --outputDirectory . --smallGradientThreshold 0.2 --transposeInputBVectors 

</code></pre>
<p>Please let me know if you need any more information to debug this issue.<br>
Best,<br>
Caoyufu</p>

---

## Post #2 by @ihnorton (2018-08-26 18:37 UTC)

<p>The error you posted often means that DWIConvert could not find any DTI-specific information in the DICOM (unfortunately the exception path doesn’t give a helpful error message right now).</p>
<p>The most common cause is that the DICOM files were anonymized and the necessary fields are not present in the header.</p>
<p>However:</p>
<aside class="quote no-group" data-username="cyufu" data-post="1" data-topic="3895">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cyufu/48/1779_2.png" class="avatar"> cyufu:</div>
<blockquote>
<p>United Imaging 3.0T</p>
</blockquote>
</aside>
<p>I am not familiar with this scanner brand, so don’t know what fields it uses to store DTI information. If they are not using the standard DICOM tags for diffusion information, then a vendor-specific reader may need to be implemented in DWIConvert. I would suggest to contact the vendor to find out.</p>

---

## Post #3 by @ihnorton (2018-08-26 18:49 UTC)

<aside class="quote no-group" data-username="ihnorton" data-post="2" data-topic="3895">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ihnorton/48/9_2.png" class="avatar"> ihnorton:</div>
<blockquote>
<p>I would suggest to contact the vendor to find out.</p>
</blockquote>
</aside>
<p>Specifically, DWIConvert needs to know the DICOM tags which store b-value and gradient information. For example, you can find some discussion/notes about the tags of existing supported vendors on this page:</p>
<p><a href="https://na-mic.org/wiki/NAMIC_Wiki:DTI:DICOM_for_DWI_and_DTI" class="onebox" target="_blank" rel="noopener">https://na-mic.org/wiki/NAMIC_Wiki:DTI:DICOM_for_DWI_and_DTI</a></p>

---

## Post #4 by @ihnorton (2018-10-17 14:13 UTC)

<p><a class="mention" href="/u/cyufu">@cyufu</a> dcm2niix now has preliminary support for UIH scanner diffusion images, please see:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/rordenlab/dcm2niix/issues/225#issuecomment-426377407">
  <header class="source">

      <a href="https://github.com/rordenlab/dcm2niix/issues/225#issuecomment-426377407" target="_blank" rel="noopener">github.com/rordenlab/dcm2niix</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/rordenlab/dcm2niix/issues/225#issuecomment-426377407" target="_blank" rel="noopener">dcm2niix does not support data from United Imaging Healthcare(UIH), China</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2018-09-14" data-time="02:56:39" data-timezone="UTC">02:56AM - 14 Sep 18 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2018-10-03" data-time="14:58:07" data-timezone="UTC">02:58PM - 03 Oct 18 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/chunshan" target="_blank" rel="noopener">
          <img alt="chunshan" src="https://avatars.githubusercontent.com/u/1472108?v=4" class="onebox-avatar-inline" width="20" height="20">
          chunshan
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">UIH is a noted MR manufacturer from China which is currently exploring the world<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">wide markets. By now many institutes over the world have been using UIH　ＭＲscanners to acquire DWI/DTI and fMRI data. The users also want to convert their dicom data to NIfTI format using dcm2niix which is very popular in the brain and neurology research community. But the dcm2niix currently does not recognize the UIH data format correctly. As an example, We tried to convert the fMRI data using dcm2niix and got the following result of improper format conversion.
![](http://7xps0u.com1.z0.glb.clouddn.com/dcm2niix_uih_wrong_conversion.jpg)

UIH supports two ways of archiving the DWI/DTI and fMRI data. One way is one dicom file per slice and the other is one dicom file per volume (We call it GRID format). The private tags used in the images are shown in the following table. 


Tag ID | Tag Name | VR | VM | Description | Sample
-- | -- | -- | -- | -- | --
0061,1002 | Generate Private | US | 1 | Flag to generate private format file | 1
**0061,4002** | **FOV** | SH | 1 | FOV(mm) | 224*224
0065,1000 | MeasurmentUID | UL | 1 | Measurement UID of Protocol | 12547865
0065,1002 | ImageOrientationDisplayed | SH | 1 | Image Orientation Displayed | Sag or Sag&gt;Cor
0065,1003 | ReceiveCoil | LO | 1 | Receive Coil Information | H 8
0065,1004 | Interpolation | SH | 1 | Interpolation | I
0065,1005 | PE Direction Displayed | SH | 1 | Phase encoding diretion displayed | A-&gt;P or H-&gt;F
0065,1006 | Slice Group ID | IS | 1 | Slice Group ID | 1
0065,1007 | Uprotocol | OB | 1 | Uprotocol value |  
0065,1009 | BActualValue | FD | 1 | Actual B-Value from sequence | 1000.0
**0065,100A** | **BUserValue** | FD | 1 | User Choose B-Value from UI | 1000.0
**0065,100B** | **Block Size** | DS | 1 | Size of the paradigm/block | 10
**0065,100C** | **Experimental status** | SH | 1 | fMRI | rest/active
0065,100D | Parallel Information | SH | 1 | ratio of parallel acquisition and acceleration |  
0065,100F | Slice Position | SH | 1 | Slice location displayed on the screen | H23.4
0065,1011 | Sections | SH | 1 |   |  
0065,1013 | InPlaneRotAngle | FD（°） | 1 | Rotation angle in the plane | -0.5936
0065,1014 | SliceNormalVector | DS | 3 | Normal vector of the slice | 0\0\1
0065,1015 | SliceCenterPosition | DS | 3 | Center position of the   slice | 0\0\0
0065,1016 | PixelRotateModel | UL | 1 | Pixel Rotation Model | 4
0065,1017 | SAR Model | LO | 1 | Calculation model of SAR   value | Normal:WHBST
0065,1018 | dB/dt Model | LO | 1 | Calculation model of dB/dt | Normal
0065,1023 | TablePosition | LO | 1 | Table Position | 0
0065,1025 | Slice Gap | DS | 1 | Slice Gap | 0.0
0065,1029 | AcquisitionDuration | SH | 1 | Acquisition Duration | 0.03
0065,102B | ApplicationCategory | LT | 1 | Application names available | DTI\Func
0065,102C | RepeatitionIndex | IS | 1 |   | 0
**0065,102D** | **SequenceDisplayName** | ST | 1 | Sequence display name | Epi_dti_b0
0065,102E | NoiseDecovarFlag | LO | 1 | Noise decorrelation flag | PreWhite
0065,102F | ScaleFactor | FL | 1 | scale factor | 2.125
0065,1031 | MRSequenceVariant | SH | 1 | SequenceVariant |  
0065,1032 | MRKSpaceFilter | SH | 1 | K space filter |  
0065,1033 | MRTableMode | SH | 1 | Table mode | Fix
0065,1036 | MRDiscoParameter | OB | 1 |   |  
**0065,1037** | **MRDiffusionGradOrientation** | FD | 3 | Diffusion gradient   orientation | 0\0\0
0065,1038 | MRPerfusionNoiseLevel | FD | 1 | epi_dwi/perfusion noise   level | 40
0065,1039 | MRGradRange | SH | 6 | linear range of gradient | 0.0\157\0.0\157\0.0\125
**0065,1050** | **MR Number Of Slice In   Volume** | DS | 1 | Number Of Frames In a   Volume，Columns of each frame: cols =ceil(sqrt(total)) ; Rows of   each frame: rows =ceil(total/cols) ;   appeared when image type   (00080008) has VFRAME | 27
0065,1051 | MR VFrame Sequence | SQ | 1 | 1 |  
 -&gt;0008,0022 | Acquisition Date | DA | 1 |   |  
 -&gt;0008,0032 | Acquisition Time | TM | 1 |   |  
 -&gt;0008,002A | Acquisition DateTime | DT | 1 |   |  
 -&gt;0020,0032 | ImagePosition(Patient) | DS | 3 |   |  
 -&gt;00201041 | Slice Location | DS | 1 |   |  
 -&gt;0018,9073 | Acquisition Duration | FD | 1 |   |  
 -&gt;0065,100C | MRExperimental Status | SH | 1 |   | rest/active

The example data can be downloaded from https://1drv.ms/f/s!Avf7THyflzj1gnO37GL2I8Hk-0MV . The gradient table for the DTI data is also provided.

If any questions, please give me a reply or contact me via email  chunshan.yang@united-imaging.com</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I don’t think we (me or <a class="mention" href="/u/hjmjohnson">@hjmjohnson</a>) have the bandwidth to implement this format natively in DWIConvert in the near future, so I would suggest to use dcm2niix, and then import the nifti files using DWIConvert.</p>

---

## Post #5 by @Ekaterina (2019-02-18 17:49 UTC)

<p>Good day!<br>
Please help me!<br>
3D-slicer incorrectly reads images from a Toshiba tomograph. I do not understand how to transpose the matrix, I can ask you to write me the steps. I will be very grateful to you.</p>
<p>Do you have the opportunity to see my pictures? I can send them to you by mail (pictures are already anonymized).</p>

---

## Post #6 by @ljod (2019-02-18 20:30 UTC)

<p>Hello. Have you tried the program dcm2niix to convert to nrrd, then read it into Slicer? This should work.</p>
<p>Alternatively we have a new import module under testing now. To try it, download the Nightly Build from <a href="http://slicer.org" rel="nofollow noopener">slicer.org</a>, then use the Extension Manager to install the Dcm2niix module. It seems to be available for Mac and Linux currently. It is under construction so please let us know if it works for you.</p>

---

## Post #7 by @Alex_Donabedian (2023-11-29 18:50 UTC)

<p>Hello, are you aware if DWIConvert is compatible with scans from a Bruker 7T?</p>

---
