# DWIConvert is not working to convert DICOM to NRRD

**Topic ID**: 9717
**Date**: 2020-01-06
**URL**: https://discourse.slicer.org/t/dwiconvert-is-not-working-to-convert-dicom-to-nrrd/9717

---

## Post #1 by @Nguyen_Cuong (2020-01-06 15:56 UTC)

<p>Operating system: MacOS<br>
Slicer version:4.10.2<br>
Expected behavior:NRRD file<br>
Actual behavior: I had a problem when I try to convert DICOM file to NRRD with DWIConvert library.<br>
Everything is OK when I used Slicer tool with UI to load and save DICOM file as NRRD.<br>
However, I have multiple DICOM files and want to convert automatically.<br>
I use a command<br>
/Applications/Slicer.app/Contents/lib/Slicer-4.10/cli-modules/DWIConvert  -i /Users/aaa/Desktop/dicom/1.3.6.1.4.1.14519.5.2.1.6279.6001.975254950136384517744116790879 -o /Users/aaa/Desktop/dicom/a.nrrd</p>
<p>I got a error<br>
Dicom images are ordered in a volume interleaving way.</p>
<p>ImageOrientationPatient (0020:0037): LPS Orientation Matrix</p>
<p>1 0 0</p>
<p>0 1 0</p>
<p>0 0 1</p>
<p>this-&gt;m_SpacingMatrix</p>
<p>0.599609 0 0</p>
<p>0 0.599609 0</p>
<p>0 0 2.5</p>
<p>NRRDSpaceDirection</p>
<p>0.599609 0 0</p>
<p>0 0.599609 0</p>
<p>0 0 2.5</p>
<p>Slice 0: -171.7 -153.5 -8.09</p>
<p>Slice 1: -171.7 -153.5 -10.59</p>
<p>Slice order is SI</p>
<p>Number of Slices: 124</p>
<p>Number of Volume: 1</p>
<p>Number of Slices in each volume: 124</p>
<p>WARNING: Missing B Value</p>
<p>Exception extracting gradient vectors</p>
<p>itk::ExceptionObject (0x7fb09d9a7610)</p>
<p>Location: “unknown”</p>
<p>File: /Volumes/Dashboards/Stable/Slicer-4102-build/ITK/Modules/IO/DCMTK/src/itkDCMTKFileReader.cxx</p>
<p>Line: 963</p>
<p>Description: itk::ERROR: Cant find tag 19 10bb</p>
<p>I found the reason is my DICOM file were removed some private tags, right?<br>
But it is still converted by Slicer tool<br>
Could you give me some solution.<br>
Thank you very much.</p>

---

## Post #2 by @pieper (2020-01-06 16:18 UTC)

<p>Slicer’s dicom reader doesn’t always use DWIConvert, so it’s probably going through a different path when you use the UI.</p>
<p>For batch converting dicom to nrrd, there are many possible options depending on the exact data, but typically we find dcm2niix to be the best option.  You can get it via slicerdmri or directly from the source (linked in thes readme).</p>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicon.ico" class="site-icon" width="16" height="16">
      <a href="https://github.com/SlicerDMRI/SlicerDcm2nii" target="_blank">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars0.githubusercontent.com/u/15898279?s=400&amp;v=4" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://github.com/SlicerDMRI/SlicerDcm2nii" target="_blank">SlicerDMRI/SlicerDcm2nii</a></h3>

<p>Support loading DICOM data in Slicer using the functionality of the dcm2niix program. - SlicerDMRI/SlicerDcm2nii</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Nguyen_Cuong (2020-01-06 16:40 UTC)

<p>Dear Pieper,<br>
Thanks for your suggestion, I have tried to use dcm2niix to convert into NRRD but I have some problems:</p>
<ol>
<li>The nrrd file converted from dcm2niix has more size than 3D slicer 65MB compared with 42MB for same DICOM</li>
<li>I have further task like create a segmentation file using MITK Phenotyping library. When I load generated .nrrd file, something is different in bordered</li>
</ol>
<p>The output of nrrd file of <strong>dcm2niix</strong>, and it could not be done<br>
0.489] loading /storage/cuongnc/LIDC-IDRI-processing/new_nrrd/0873a/0873a_ct_scan.nrrd via itk::ImageIOFactory…<br>
[0.489] ioRegion: ImageIORegion (0x7fff3cf6df20)<br>
Dimension: 3<br>
Index: 0 0 0<br>
Size: 512 512 124<br>
[0.533] [135, <strong>-153.8,</strong> -6.84]<br>
[0.533] [-172, <strong>153.2</strong>, -316.84]</p>
<p>The output of nrrd file of <strong>Slicer</strong> , it works successful<br>
0.486] loading /storage/cuongnc/LIDC-IDRI-processing/new_nrrd/0873a/0873a_ct_scan.nrrd via itk::ImageIOFactory…<br>
[0.487] ioRegion: ImageIORegion (0x7ffc39afae40)<br>
Dimension: 3<br>
Index: 0 0 0<br>
Size: 512 512 124<br>
[1.158] [135, <strong>153.2,</strong> -6.84]<br>
[1.158] [-172, <strong>-153.8,</strong> -316.84]</p>
<p>In addition, I also use MITK Phenotyping  to convert into NRRD file, but it doesnt work with some DICOM file. The NRRD files are not merged into one file, such as 0873a_ct_scan_1.nrrd, 0873a_ct_scan_2.nrrd 0873a_ct_scan_3.nrrd …</p>

---

## Post #4 by @lassoan (2020-01-06 18:33 UTC)

<aside class="quote no-group" data-username="Nguyen_Cuong" data-post="3" data-topic="9717">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/nguyen_cuong/48/5606_2.png" class="avatar"> Nguyen_Cuong:</div>
<blockquote>
<p>I also use MITK Phenotyping to convert into NRRD file, but it doesnt work</p>
</blockquote>
</aside>
<p>Is there a reason you are trying to use MITK Phenotyping instead of 3D Slicer? Slicer, along with extensions such as SlicerRadiomics should be able to do everything that MITK Phenotyping offers and much more.</p>

---

## Post #5 by @Nguyen_Cuong (2020-01-06 19:00 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="9717">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>SlicerRadiomics</p>
</blockquote>
</aside>
<p>Yeah, I agree with you, Slice is amazing tool for medical image processing with multiple extensions. But I my working environment is on the remote server and do not family with UI application along with a huge of data.<br>
I am trying to build Slicer app and use its library to convert DICOM to NRRD file but it still do not work.<br>
Do you have any advise for me ?<br>
Thank you very much.</p>

---

## Post #6 by @pieper (2020-01-06 19:20 UTC)

<p>You can use pyradiomics outside of slicer.</p>
<p>For format conversion, it really depends on your data.  Here’s some background that may help:</p>
<p><a href="https://projectweek.na-mic.org/PW27_2018_Boston/Projects/DICOMVolumeReconstruction/">Volume reconstruction project</a></p>
<p><a href="https://discourse.slicer.org/t/how-to-convert-dicom-files-to-nrrd/540/13">A previous thread</a> about conversion.</p>

---

## Post #7 by @Chris_Rorden (2020-01-07 14:10 UTC)

<p><a class="mention" href="/u/nguyen_cuong">@Nguyen_Cuong</a></p>
<blockquote>
<ol>
<li>The nrrd file converted from dcm2niix has more size than 3D slicer 65MB compared with 42MB for same DICOM</li>
</ol>
</blockquote>
<p>I am very surprised by this, the NRRD header is far more concise than the DICOM header. dcm2niix will strive to losslessly convert your data. Therefore, dcm2niix files are virtually always smaller than the incoming DICOMs. The typical situation where this is not the case is where the distance between slices varies, since NRRD and NIfTI require equidistant slices. This is sometimes seen in CT scans (e.g. for CT scans of brain, more slices near brain stem, fewer slices for superior cortex), but never (to my knowledge) seen in DWI scans (where you typically desire both equidistant slices and isotropic voxels).</p>
<p>I also note “CT” in the file name (<code>0873a_ct_scan</code>) and a spatial resolution that does not look like DWI (0.6x0.6x2.5, the voxels are not isotropic, and such a high in-plane resolution would result in low SNR, strong eddy currents, huge EPI artifacts, long readout times).</p>
<p>Can I suggest you run <a href="https://github.com/rordenlab/dcm2niix/releases" rel="noopener nofollow ugc">dcm2niix</a> from the command line and see what messages it gives. If this is a CT scan, interpolated slice gaps is appropriate, but if this is really a DWI scan it suggests that not all of the data was transferred.</p>

---

## Post #8 by @Nguyen_Cuong (2020-01-07 14:44 UTC)

<aside class="quote no-group" data-username="Chris_Rorden" data-post="7" data-topic="9717">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chris_rorden/48/4073_2.png" class="avatar"> Chris_Rorden:</div>
<blockquote>
<p>I also note “CT” in the file name ( <code>0873a_ct_scan</code> ) and a spatial resolution that does not look like DWI (0.6x0.6x2.5, the voxels are not isotropic, and such a high in-plane resolution would result in low SNR, strong eddy currents, huge EPI artifacts, long readout times).</p>
<p>Can I suggest you run <a href="https://github.com/rordenlab/dcm2niix/releases" rel="noopener nofollow ugc">dcm2niix</a> from the command line and see what messages it gives. If this is a CT scan, interpolated slice gaps is appropriate, but if this is really a DWI scan it suggests that not all of the data was transferred.</p>
</blockquote>
</aside>
<p>Dear Chris_Rorden,<br>
Thank you very much for deep knowledges about medical image. I’am just starting to work with these image types.</p>
<blockquote>
<p>Blockquote<br>
Therefore, dcm2niix files are virtually always smaller than the incoming DICOMs.</p>
</blockquote>
<p>My DICOM is 65.5 MB and the output NRRD file of dcm2niix have equal size. Weird<br>
The DICOM dataset I got from <a href="https://wiki.cancerimagingarchive.net/display/Public/LIDC-IDRI" rel="noopener nofollow ugc">LIDC</a><br>
As your proposing, I run the command line to convert DICOM to NRRD</p>
<pre><code class="lang-plaintext">/Applications/MRIcroGL.app/Contents/Resources/dcm2niix -f "%f_%p_%t_%s" -p n -z n -e y -b n -o "/Users/cuongnc/Desktop/dicom" "/Users/cuongnc/Desktop/dicom/1.3.6.1.4.1.14519.5.2.1.6279.6001.975254950136384517744116790879"

Compression will be faster with 'pigz' installed http://macappstore.org/pigz/

Chris Rorden's dcm2niiX version v1.0.20190902 (JP2:OpenJPEG) (JP-LS:CharLS) Clang10.0.1 (64-bit MacOS)

Found 124 DICOM file(s)

Warning: Unable to append protocol name (0018,1030) to filename (it is empty).

Convert 124 DICOM as /Users/cuongnc/Desktop/dicom/1.3.6.1.4.1.14519.5.2.1.6279.6001.975254950136384517744116790879__20000101170254_4034901608a (512x512x124x1)

NRRD writer is experimental

Conversion required 0.327573 seconds (0.320474 for core code).
</code></pre>

---

## Post #9 by @Nguyen_Cuong (2020-01-07 14:49 UTC)

<p>Thank you very much for your solutions.<br>
I have tried many approaches but it do not work for me <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=9" title=":frowning:" class="emoji" alt=":frowning:"><br>
The last way is using 3D slicer tool to convert DICOM image manually</p>

---

## Post #10 by @Chris_Rorden (2020-01-07 17:19 UTC)

<p>Can you view the converted NRRD file with <a href="https://www.nitrc.org/projects/mricrogl" rel="nofollow noopener">MRIcroGL</a>? More details regarding MRIcroGL are <a href="https://www.nitrc.org/plugins/mwiki/index.php/mricrogl:MainPage" rel="nofollow noopener">here</a>. You could also try using dcm2niix to convert to NIfTI (remove <code>-e y</code> from the call) instead of NRRD and see if that helps. In theory they should be the same, but NRRD is a very new feature for dcm2niix.</p>

---

## Post #11 by @Nguyen_Cuong (2020-01-07 17:37 UTC)

<aside class="quote no-group quote-modified" data-username="Nguyen_Cuong" data-post="8" data-topic="9717">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/nguyen_cuong/48/5606_2.png" class="avatar"> Nguyen_Cuong:</div>
<blockquote>
<p>/Applications/MRIcroGL.app/Contents/Resources/dcm2niix -f “%f_%p_%t_%s” -p n -z n -e y -b n -o “/Users/cuongnc/Desktop/dicom” “/Users/cuongnc/Desktop/dicom/1.3.6.1.4.1.14519.5.2.1.6279.6001.975254950136384517744116790879”</p>
</blockquote>
</aside>
<p>Yeah, it can be shown normally. The .nii generated file . as you say have the same size and can be displayed<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4c1536bf5d9686ec7600ab7a5ac85e8f20dba727.jpeg" data-download-href="/uploads/short-url/aR3JLLSTUvK0udc0XUAS02Bu4Jh.jpeg?dl=1" title="Screen Shot 2020-01-08 at 12.35.01 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4c1536bf5d9686ec7600ab7a5ac85e8f20dba727_2_690x448.jpeg" alt="Screen Shot 2020-01-08 at 12.35.01 AM" data-base62-sha1="aR3JLLSTUvK0udc0XUAS02Bu4Jh" width="690" height="448" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4c1536bf5d9686ec7600ab7a5ac85e8f20dba727_2_690x448.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4c1536bf5d9686ec7600ab7a5ac85e8f20dba727_2_1035x672.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4c1536bf5d9686ec7600ab7a5ac85e8f20dba727_2_1380x896.jpeg 2x" data-dominant-color="888888"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-01-08 at 12.35.01 AM</span><span class="informations">2406×1564 590 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
