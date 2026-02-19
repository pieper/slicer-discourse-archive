---
topic_id: 42452
title: "Visualization Of Lower Body Muscle Segmentation From Dafne"
date: 2025-04-06
url: https://discourse.slicer.org/t/42452
---

# Visualization of lower body muscle segmentation from Dafne

**Topic ID**: 42452
**Date**: 2025-04-06
**URL**: https://discourse.slicer.org/t/visualization-of-lower-body-muscle-segmentation-from-dafne/42452

---

## Post #1 by @trumanchiu (2025-04-06 02:10 UTC)

<p>Hello everyone, I am new to 3DSlicer and I am working on a lower body MRI study with the goal of segmenting 35 muscles and creating 3D visualizations from the segmentations. Manual muscle segmentations have been completed using <a href="https://dafne.network" rel="noopener nofollow ugc">Dafne</a>. Dafne was originally chosen over 3DSlicer as its software is designed specifically for lower body muscle segmentation.</p>
<p>I would now like to view the masks created in Dafne in 3DSlicer. After exporting the masks from Dafne as DICOM files and importing them to 3DSlicer, they do not appear to be visible.</p>
<p>Additionally, the original MR images were taken in batches, and each 111-image batch contains a 5–6 slice overlap with the adjacent batch. When I import them into Slicer, I have to view each batch separately as different image sets.</p>
<p>Therefore I have a few questions:</p>
<ol>
<li>
<p>Would it be possible to view these imported masks in 3DSlicer to create 3D models of each individual muscle?</p>
</li>
<li>
<p>Is there a way to merge the separate MRI batches into a single continuous volume so I can scroll seamlessly from the hip to the foot, rather than switching between different image sets?</p>
</li>
</ol>
<p>Thank you in advance for the help.</p>

---

## Post #2 by @pieper (2025-04-06 19:57 UTC)

<p>I don’t know if anyone here has used Dafne, but if it can put out standard DICOM Segmentation Objects, then Slicer should be able to load them if you install the Quantitative Reporting extension.</p>
<p>For the other question this module in the Sandbox extension might do what you want:</p>
<p><a href="https://github.com/PerkLab/SlicerSandbox#stitch-volumes">https://github.com/PerkLab/SlicerSandbox#stitch-volumes</a></p>

---

## Post #3 by @trumanchiu (2025-04-10 04:08 UTC)

<p>Thank you for your response, Steve. The Sandbox extension worked for the original DICOM images.</p>
<p>However, I have not been able to load the segmentation masks. If possible, could you direct me to material outlining how to import these DICOM Segmentation Objects into Quantitative Reporting? <a href="https://qiicr.gitbook.io/quantitativereporting-guide/user-guide/tutorial" rel="noopener nofollow ugc">This tutorial</a> mainly focuses on how to segment once the images are loaded. Thank you.</p>

---

## Post #4 by @pieper (2025-04-11 00:34 UTC)

<p>If the dicom segmentations are recognized by Quantitative Reporting they should just load so there’s no specific tutorial.  SEG is complex, so probably there’s something incompatible (maybe valid data that differs in details or something non-standard).</p>
<p>I see you filed an issue on github, which is good.</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/QIICR/QuantitativeReporting/issues/284">
  <header class="source">

      <a href="https://github.com/QIICR/QuantitativeReporting/issues/284" target="_blank" rel="noopener">github.com/QIICR/QuantitativeReporting</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/QIICR/QuantitativeReporting/issues/284" target="_blank" rel="noopener">Visualization of lower body muscle segmentation from Dafne</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2025-04-10" data-time="04:18:15" data-timezone="UTC">04:18AM - 10 Apr 25 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/truman-chiu" target="_blank" rel="noopener">
          <img alt="" src="https://avatars.githubusercontent.com/u/206976047?v=4" class="onebox-avatar-inline" width="20" height="20">
          truman-chiu
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Hello everyone,

I am new to 3DSlicer and I am working on a lower body MRI study<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden"> with the goal of segmenting 35 muscles and creating 3D visualizations from the segmentations. Manual muscle segmentations have been completed using [Dafne](https://dafne.network/). Dafne was originally chosen over 3DSlicer as its software is designed specifically for lower body muscle segmentation.

I would now like to view the masks created in Dafne in 3DSlicer. After exporting the masks from Dafne as DICOM files and importing them to 3DSlicer, they do not appear to be visible. I was recommended to install the images into the Quantitative Reporting extension but I am unsure how to load theDICOM files into this extension. I looked through the tutorial documentation but it seemed to have a greater focus on segmenting the DICOM images. 

Any help would be appreciated, thank you.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Probably you’ll need to post example data.  Also it could help you to try this tool: <a href="https://www.dclunie.com/dicom3tools/dciodvfy.html" class="inline-onebox">DICOM Validator - dciodvfy</a></p>

---

## Post #5 by @trumanchiu (2025-04-11 23:53 UTC)

<p>Thank you for the information, Steve. I have been in contact with Andriy and he provided me with a solution. He suggested I download the masks from Dafne in NIfTI format and import the data as a segmentation. It has worked and I can now view the masks in 3D! Thank you for your help and I may have more questions as I continue learning the intricacies of 3DSlicer!</p>

---

## Post #6 by @fedorov (2025-04-12 02:19 UTC)

<p>To add to that, I suggested trying NIfTI because that option was shown in the screenshot shared by <a class="mention" href="/u/trumanchiu">@trumanchiu</a>, and I didn’t want to risk the exposure of patient information in the DICOM files that the system was exporting, since the user did not have experience with de-identification. It would still be interesting to see what was the issue in the DICOM that Dafne is exporting, but not some other time.</p>

---

## Post #7 by @trumanchiu (2025-04-18 01:29 UTC)

<p>Hello everyone,</p>
<p>I have a few questions regarding refining individual muscle/bone segmentations and also exporting to 3D viewers.</p>
<p>In terms of muscle segmentations, unfortunately due to a glitch in Dafne, the software we used to create the segmentation masks, we had an issue with our interpolating which created extra masks that you can see in the images below on the left. <strong>Is there a way to quickly remove these masks?</strong> I tried using the “Islands” function but when I am not able to use a minimum size that preserves the smaller segmentations done while removing the strips on the left.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ce0d7207a5b0767a237a90e184c57959b1e5b4db.png" data-download-href="/uploads/short-url/toPagBTSREooP9YXFuXLEcp1KDF.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ce0d7207a5b0767a237a90e184c57959b1e5b4db.png" alt="image" data-base62-sha1="toPagBTSREooP9YXFuXLEcp1KDF" width="95" height="206"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">191×413 52.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
^ All thigh muscles with extra masks on the left</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7ebd0abc5d2691d3f2d88ddbab98f8f7dd023cce.jpeg" data-download-href="/uploads/short-url/i5bbgG1O2iaEe6QcI0RSKkuoeXI.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7ebd0abc5d2691d3f2d88ddbab98f8f7dd023cce_2_344x217.jpeg" alt="image" data-base62-sha1="i5bbgG1O2iaEe6QcI0RSKkuoeXI" width="344" height="217" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7ebd0abc5d2691d3f2d88ddbab98f8f7dd023cce_2_344x217.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7ebd0abc5d2691d3f2d88ddbab98f8f7dd023cce_2_516x325.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7ebd0abc5d2691d3f2d88ddbab98f8f7dd023cce_2_688x434.jpeg 2x" data-dominant-color="9993C3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1148×725 88.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
^ Just the vasti muscles with the extra masks on the left</p>
<p>In addition to removing the extra masks, I have been using the “Segment Editor” function, particularly the “Fill between slices” function. I’ve shown an example below. <strong>Is there a way to edit the results of the interpolation?</strong></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a02d12d14474ae0cd05332774831ba78ff842972.jpeg" data-download-href="/uploads/short-url/mQYXOJNHEHLt2VLhFn2bRt6Xjiy.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a02d12d14474ae0cd05332774831ba78ff842972_2_689x435.jpeg" alt="image" data-base62-sha1="mQYXOJNHEHLt2VLhFn2bRt6Xjiy" width="689" height="435" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a02d12d14474ae0cd05332774831ba78ff842972_2_689x435.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a02d12d14474ae0cd05332774831ba78ff842972_2_1033x652.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a02d12d14474ae0cd05332774831ba78ff842972.jpeg 2x" data-dominant-color="454242"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1148×725 74 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
^ VI “fill between slices” function segmenting over the femur</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6aecb53bc9d4a8516dcb34f490cee061e6cdf831.jpeg" data-download-href="/uploads/short-url/ffTKTcVkTZmPeXnEkhle7Pph5UB.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6aecb53bc9d4a8516dcb34f490cee061e6cdf831_2_344x217.jpeg" alt="image" data-base62-sha1="ffTKTcVkTZmPeXnEkhle7Pph5UB" width="344" height="217" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6aecb53bc9d4a8516dcb34f490cee061e6cdf831_2_344x217.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6aecb53bc9d4a8516dcb34f490cee061e6cdf831_2_516x325.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6aecb53bc9d4a8516dcb34f490cee061e6cdf831_2_688x434.jpeg 2x" data-dominant-color="5B5850"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1148×725 62.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
^ For example, in this axial segmentation of the proximal femur, I am unable to edit the “results”. Instead, I would have to segment over top of it and the auto-update feature removes that initial mask.</p>
<p>In terms of 3D visualization, I have exported individual muscle in .stl format. I have viewed them on 3D Viewer. However, we are looking for a way to export all 35 muscles together, and be able to select which muscles you want to view in a common, user-friendly platform. The goal is for participants of the study to view their segmented muscles without having to use a platform like 3D Slicer. <strong>Is there a platform that this is able to be done in?</strong> <strong>In addition to this, is there a way to compress these files?</strong> One model (VMO) is already ~11 MB.</p>
<p>Thank you in advance.</p>

---

## Post #8 by @pieper (2025-04-18 20:11 UTC)

<p>You can probably fix all the segmentation errors with tools like scissors.  For the fill between slices you may need to segment the femur first and then nave it not overwrite that segment.</p>
<p>For easy web viewer software you can export to gltf using the OpenAntatomy extension.  There are lots of viewers on the web to pick from.</p>

---

## Post #9 by @trumanchiu (2025-04-19 04:19 UTC)

<p>Thanks for your response Steve.</p>
<p>Do you know how I would be able to categorize my segmentations like the first photo below? The second photo is what is looks like when I put all of the segmentations in 1 folder as it would not let me import different 3D models at the same time in 3D Viewer. Thanks.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c6d9f5de8e84792064eed747a8c44d4f8b10f837.jpeg" data-download-href="/uploads/short-url/sn7w49K824CSbO94JOIYbAZpb39.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c6d9f5de8e84792064eed747a8c44d4f8b10f837_2_345x223.jpeg" alt="image" data-base62-sha1="sn7w49K824CSbO94JOIYbAZpb39" width="345" height="223" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c6d9f5de8e84792064eed747a8c44d4f8b10f837_2_345x223.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c6d9f5de8e84792064eed747a8c44d4f8b10f837_2_517x334.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c6d9f5de8e84792064eed747a8c44d4f8b10f837_2_690x446.jpeg 2x" data-dominant-color="DDD8D5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1278×827 134 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a51422c487202846fce9742b790f8169a9777a4c.jpeg" data-download-href="/uploads/short-url/nylVfyglNyDE5ugAhev9kLOYelu.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a51422c487202846fce9742b790f8169a9777a4c_2_477x375.jpeg" alt="image" data-base62-sha1="nylVfyglNyDE5ugAhev9kLOYelu" width="477" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a51422c487202846fce9742b790f8169a9777a4c_2_477x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a51422c487202846fce9742b790f8169a9777a4c_2_715x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a51422c487202846fce9742b790f8169a9777a4c_2_954x750.jpeg 2x" data-dominant-color="F7F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1136×893 128 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @pieper (2025-04-19 17:05 UTC)

<p>I don’t know off the top of my head, no.</p>

---

## Post #11 by @trumanchiu (2025-04-29 19:15 UTC)

<p>Hello everyone, thank you for your help.</p>
<p>I have a follow up question: is there a way to view the cross-sectional images as well as the 3D models similar to the Four-Up view in 3DSlicer but in a publicly available viewer similar to <a href="http://3dviewer.net" rel="noopener nofollow ugc">3dviewer.net</a>?</p>
<p>We are trying to develop this for a teaching tool to have these images and models side by side for students studying lower body musculoskeletal anatomy. Thank you.</p>

---

## Post #12 by @pieper (2025-04-30 00:45 UTC)

<p>Not sure, but maybe with volview: <a href="https://volview.kitware.com/">https://volview.kitware.com/</a></p>

---
