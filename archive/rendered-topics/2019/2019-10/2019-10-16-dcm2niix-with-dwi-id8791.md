---
topic_id: 8791
title: "Dcm2Niix With Dwi"
date: 2019-10-16
url: https://discourse.slicer.org/t/8791
---

# Dcm2niix with DWI

**Topic ID**: 8791
**Date**: 2019-10-16
**URL**: https://discourse.slicer.org/t/dcm2niix-with-dwi/8791

---

## Post #1 by @JohnK (2019-10-16 00:40 UTC)

<p>Hi all,<br>
Hope it is ok to start a new topic on dcm2niix. I think I did my homework by looking at others discussions and attempts on DWI images<br>
{ i.e.,</p><aside class="quote" data-post="1" data-topic="6576">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/13edae/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/importing-dwi-file/6576">Importing DWI file </a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi, I am trying to import some DWI data into Slicer. 
I have successfully done this in the past using .nrrd files. This new data is .nii and seems to load fine but in the Diffusion Brain Masking module it is not found as a potential Input DWI Volume, so cannot be used. 
Do you know why this may not be working correctly, or if I have to go through any other steps first? 
Thank you!
  </blockquote>
</aside>
<aside class="quote quote-modified" data-post="3" data-topic="8639">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/59ef9b/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/dti-averaging-of-b0-images/8639/3">DTI, averaging of b0 images</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Thanks for the quick reply. 
b-value is 1000 and 30 directions. Unfortunately Other scans will be at 10 directions, but still appears to have good results 
The details of the study are complex, but the simple story is that we suspect there is near anatomical absence vs complete dysfunction of superior fasciculus pathways from the occipital lobe (based on volume loss in anatomical T1 /t2 imaging with additional evoked potential recordings). So the issue is providing evidence that the pathway is p…
  </blockquote>
</aside>
<aside class="quote" data-post="4" data-topic="5407">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/frederic/48/4907_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/convert-single-files-into-one-nii/5407/4">Convert single files into one .nii</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Not directly, but yest it’s possible, for example by a thing like that: 
After that you load MRIcroGL (dcm2niix) 

import os 
command1 = “dcm2nix /YourDirectory/data.IMA” 
os.system(command1)
  </blockquote>
</aside>
<p>
}</p>
<p>Using 3DSlicer 4.10.2 / Windows 64</p>
<p>My problem:<br>
Reading of raw DCM files from a DWI scan from viewer NilRead.<br>
“Diffusion-weighted DICOM Import (DWIConvert) standard error:<br>
…<br>
…<br>
E: can’t change to unencapsulated representation for pixel data<br>
E: can’t determine ‘PhotometricInterpretation’ of decompressed image<br>
E: mandatory attribute ‘PhotometricInterpretation’ is missing or can’t be determined<br>
Error: no DICOMfiles found in inputDirectory: C:/Users/jkelly/AppData/Local/Temp/Slicer/<strong>SlicerTemp</strong><br>
Unable to create converter”</p>
<p>As expected, this method didn’t work either:<br>
3D slicer → DICOM import → Advanced → examine → load as Diffusion volume<br>
Error “Could not load: axDTI_30_64ch - as DWI Volume as a Diffusion Volume”</p>
<p>So I tried dcm2niix version v1.0.20190902 in MRIcron using these options<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/64acfbae64f811846425fe2e11bd57a43ebd73d8.png" alt="image" data-base62-sha1="emCmql9i4ogabykwWlfEsinITxK" width="448" height="461"></p>
<p>It loads the nrrd output as a diffusion weighted file but scrambles the image</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/23212c44d415d058eae3c5998965ca69def5c038.jpeg" data-download-href="/uploads/short-url/50LMCcc9zD3kiMxKQo9zv1dzyVa.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/23212c44d415d058eae3c5998965ca69def5c038_2_690x323.jpeg" alt="image" data-base62-sha1="50LMCcc9zD3kiMxKQo9zv1dzyVa" width="690" height="323" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/23212c44d415d058eae3c5998965ca69def5c038_2_690x323.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/23212c44d415d058eae3c5998965ca69def5c038_2_1035x484.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/23212c44d415d058eae3c5998965ca69def5c038_2_1380x646.jpeg 2x" data-dominant-color="9998A5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1651×773 313 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If instead I use  dcm2niix to output NIFTI with default parameters (using command line)<br>
I get a coherent image but 3Dslicker thinks it is a scalar volume, and I cannot process the data.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/885e93db3a9d192a9af9b88db52586130920fe48.jpeg" data-download-href="/uploads/short-url/jsnzbnIn0OXJdwsh8VTCtd3JsyQ.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/885e93db3a9d192a9af9b88db52586130920fe48_2_690x357.jpeg" alt="image" data-base62-sha1="jsnzbnIn0OXJdwsh8VTCtd3JsyQ" width="690" height="357" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/885e93db3a9d192a9af9b88db52586130920fe48_2_690x357.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/885e93db3a9d192a9af9b88db52586130920fe48_2_1035x535.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/885e93db3a9d192a9af9b88db52586130920fe48_2_1380x714.jpeg 2x" data-dominant-color="9897A4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1474×764 185 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I see the json file spits out important information of which here are a sample:<br>
“ImagingFrequency”: 123.23,<br>
“Manufacturer”: “Siemens”,<br>
“ManufacturersModelName”: “Prisma_fit”,<br>
“InPlanePhaseEncodingDirectionDICOM”: “COL”,<br>
“ConversionSoftware”: “dcm2niix”,<br>
“ConversionSoftwareVersion”: “v1.0.20190902”<br>
“InPlanePhaseEncodingDirectionDICOM”: “COL”,<br>
“ConversionSoftware”: “dcm2niix”,<br>
“ConversionSoftwareVersion”: “v1.0.20190902”</p>
<p>Any suggestions?<br>
Thanks!</p>

---

## Post #2 by @Chris_Rorden (2019-10-16 02:28 UTC)

<p>Can I suggestion you run dcm2niix from the command line with logorrheic verbosity <code>-v 2</code> and ignoring derived images <code>-i y</code>, e.g.  <code>dcm2niix -v 2 ~/DICOMS/</code>. It would also help to see the fslhd output of the NIfTI file created or more details from the BIDS header, in particular the <code>ImageType</code> tag. My first guess is that you are having problems with a derived image, e.g. the color FA map. Slicer wants scalar images and tends to handle derived color images oddly. I would suggest that you adjust your sequence to not save derived images (e.g. on the Prisma "Diffusion’ tab, uncheck any derived images (FA, ADC, Trace, etc). You can always create better derived images after post-processing (de-Gibbs, de-noise, Eddy, TOPUP). If you still have issues, feel free to post an issue on the dcm2niix Github web page.</p>
<p>For settings up DWI scans on a Prisma, you may want to look at <a href="https://osf.io/brvak/wiki/home/" rel="nofollow noopener">this page</a>, albeit your 64 channel head(40)/neck(24) coil will allow more aggressive multi-band. I would recommend the CMRR diffusion sequences - be aware that the Siemens Product diffusion sequences have a bug in such that if you copy references between a A-P and a P-A scan the second series will be rotated 90-degrees (e.g. R-L) nor 180 degrees (P-A). With the CMRR sequences, you will be able to set “reversed RO/PE” to reverse phase encoding for proper phase encoding reversal (for TOPUP/Eddy). Also be aware that the default diffusion schemes for Siemens are half-sphere, so if you have a research license you will want to insert your own whole-sphere schemes for optimal use of Eddy.</p>
<p>If you have the 32-channel head-only coil, I would suggest you test it to see if it provides better performance than the 64-channel head/neck coil. The page I list above describes how to compute SNR. The 64-channel has some inherent limitations: the integrated neck coil forces a rotation to the head such that the cheek bones hit the coil and the frontal lobes are pushed away from the small coils. I would also check if the smaller coils had sufficient SNR in deep regions of the brain (e.g. main white matter tracts). I believe the 64-channels also required bandwidth compression at one stage, and I am not sure if this was resolved. You may want to check if de-selecting the neck channels (from the System tab) improves SNR. When we purchased our Prisma, we did not get this coil, as we believed that the problems were inherent to the design. You may want to contact other teams that have both this and the 32-channel to see if they have any advice.</p>

---

## Post #3 by @Chris_Rorden (2019-10-17 15:37 UTC)

<p><a class="mention" href="/u/johnk">@JohnK</a> thanks for sharing a sample dataset.</p>
<ol>
<li>Your images use Transfer Syntax (0002,0010) JPEG2000Lossless. The version of dcm2niix included with the slicer extension does not support this, while the version included with MRIcroGL does. Be aware that the DICOM standard only requires DICOM-compliant tools to support uncompressed images. Therefore, using a compressed transfer syntax can prevent you from using many popular DICOM tools. Furthermore, be aware that the JPEG2000 standard was not heavily used. In particular I believe OpenJPEG is the only open source (albeit unwieldy) <a href="https://en.wikipedia.org/wiki/JPEG_2000#Libraries" rel="nofollow noopener">library</a> to support the 16-bit precision used in medical images. Therefore, for both short term and archival purposes, I would suggest using lossless transfer syntaxes and use conventional file or disk based compression if file size is an issue.</li>
<li>Your anonymization scripts removed the <a href="https://nipy.org/nibabel/dicom/siemens_csa.html" rel="nofollow noopener">Siemens CSA headers</a> from your images. These are crucial for Siemens EPI images, specifically to determine number of images in the mosaic, slice times, gradient directions, phase encoding polarity, etc. Without these details your images will be underspecified for diffusion analyses. I would check the providence of your images and convert a copy of your images before these details were stripped out. Alternatively, you will need to acquire a new dataset with these sequences, export the data directly from the console and extract the CSA information.</li>
</ol>
<p><a class="mention" href="/u/ihnorton">@ihnorton</a> it might be worth updating the Slicer dcm2niix extension to include a version of dcm2niix compiled to handle compressed transfer syntaxes (using OpenJPEG for JPEG2000 and CharLS for loco JPEG-LS):</p>
<pre><code>git clone https://github.com/rordenlab/dcm2niix.git
cd dcm2niix
mkdir build &amp;&amp; cd build
cmake -DZLIB_IMPLEMENTATION=Cloudflare -DUSE_JPEGLS=ON -DUSE_OPENJPEG=ON ..
make</code></pre>

---

## Post #4 by @JohnK (2019-10-18 16:54 UTC)

<p>Just a note to conclude my part of the discussion -<br>
I am certain this is a vendor specific issue for downloading DWI data sets (scalar volume export of T1, T2, etc is fine). I have raised this issue with the NilRead (Hyland is company name) but I have no idea if it will be addressed in the future.</p>
<p>I suspect these enterprise level cloud-based PACS systems will become more popular in the future. Indeed for our organization, end-users outside of Radiology have to use this system (I am in Ophthalmology analyzing visual cortex, so I need to use it).</p>

---

## Post #5 by @lassoan (2019-10-18 17:28 UTC)

<aside class="quote no-group" data-username="Chris_Rorden" data-post="3" data-topic="8791">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chris_rorden/48/4073_2.png" class="avatar"> Chris_Rorden:</div>
<blockquote>
<p>it might be worth updating the Slicer dcm2niix extension to include a version of dcm2niix compiled to handle compressed transfer syntaxes (using OpenJPEG for JPEG2000 and CharLS for loco JPEG-LS)</p>
</blockquote>
</aside>
<p>JPEG options are already enabled in Slicer Preview Releases:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerDMRI/SlicerDcm2nii/blob/2368ebfdccc82b721960206d4e269a9ea3222071/SuperBuild/External_dcm2niix.cmake#L45-L46">
  <header class="source">

      <a href="https://github.com/SlicerDMRI/SlicerDcm2nii/blob/2368ebfdccc82b721960206d4e269a9ea3222071/SuperBuild/External_dcm2niix.cmake#L45-L46" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerDMRI/SlicerDcm2nii/blob/2368ebfdccc82b721960206d4e269a9ea3222071/SuperBuild/External_dcm2niix.cmake#L45-L46" target="_blank" rel="noopener">SlicerDMRI/SlicerDcm2nii/blob/2368ebfdccc82b721960206d4e269a9ea3222071/SuperBuild/External_dcm2niix.cmake#L45-L46</a></h4>



    <pre class="onebox"><code class="lang-cmake">
      <ol class="start lines" start="45" style="counter-reset: li-counter 44 ;">
          <li>-DUSE_OPENJPEG:BOOL=ON</li>
          <li>-DUSE_JPEGLS:BOOL=ON</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>However, Slicer-4.10.x extension index still referred to an older version of the extension.   I’ve updated it now to use the latest version of SlicerDcm2niix, too.</p>

---

## Post #6 by @JohnK (2019-10-28 19:32 UTC)

<p>I figured out a work around to my problem with inadequate DICOM export for DWI files. I will post my approach in case someone else comes along with a similar problem (windows 10 64-bit)</p>
<ol>
<li>
<p>store the DWI DICOM series to a folder</p>
</li>
<li>
<p>get the latest release version of MRIcron or dcm2niix (<a href="https://github.com/rordenlab/dcm2niix/releases" rel="nofollow noopener">https://github.com/rordenlab/dcm2niix/releases</a>)</p>
</li>
<li>
<p>create a batch file in the folder with the DICOMs that runs dcm2niix on the folder (no switches needed)<br>
e.g., C:\MRIcron\Resources\dcm2niix C:\myFolder_with_DICOM\</p>
</li>
<li>
<p>IF it ran correctly, then you will have an output of 4 files<br>
[series namexxxx].nii<br>
[series namexxxx].bval<br>
[series namexxxx].bvec<br>
[series namexxxx].json</p>
</li>
<li>
<p>open the nii file with DSI-Studio (<a href="http://dsi-studio.labsolver.org/dsi-studio-download" rel="nofollow noopener">http://dsi-studio.labsolver.org/dsi-studio-download</a>)<br>
If it worked, you will see a correct table of b-values and b-vectors for each image (click ok) and it will create a file [series namexxxx].nii.src.gz</p>
</li>
<li>
<p>In DSI-Studio click reconstruction, which shows the brain mask. Do File -&gt; Save 4DNifti file will now be<br>
[series namexxxx].nii.src.gz.nii.gz with associated .bvec and .bval files</p>
</li>
<li>
<p>in Slicer, open Diffusion -&gt; import export -&gt;DWIconvert<br>
-Pick FSLtoNRRD<br>
-Create new diffusion weighted volume as …<br>
-In NIFTI to NRRD conversion parameters pick the  NIFTI file [series namexxxx].nii.src.gz.nii.gz<br>
-pick the corresponding .bvec and .bval files for the other two choices<br>
-Click apply and hopefully you have yourself a DWI series in 3D Slicer.</p>
</li>
</ol>
<p>Good luck Agent 007</p>

---

## Post #7 by @JohnK (2019-10-28 23:19 UTC)

<p>Forgot to mention, you can try skipping steps 5 and 6 and using the 3 files (.nii, .bval, .bvec) from dcm2niix and see if that works as well.</p>

---
