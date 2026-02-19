---
topic_id: 1032
title: "How To Output The Dti Volume Into Dicom Datas"
date: 2017-09-11
url: https://discourse.slicer.org/t/1032
---

# How to output the DTI volume into DICOM datas?

**Topic ID**: 1032
**Date**: 2017-09-11
**URL**: https://discourse.slicer.org/t/how-to-output-the-dti-volume-into-dicom-datas/1032

---

## Post #1 by @Jin (2017-09-11 03:51 UTC)

<p>How to output the DTI volume into DICOM datas?<br>
I use the Create a DICOM Series module, but I can’t find the DTI volume in the Input Volume.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/662f4592dacdff80258004fc756004a8274f89c1.jpeg" data-download-href="/uploads/short-url/ezXYQ4YlPqzIujO4d3UPQZyvUR3.JPG?dl=1" title="11" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/662f4592dacdff80258004fc756004a8274f89c1_2_690x161.JPG" alt="11" data-base62-sha1="ezXYQ4YlPqzIujO4d3UPQZyvUR3" width="690" height="161" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/662f4592dacdff80258004fc756004a8274f89c1_2_690x161.JPG, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/662f4592dacdff80258004fc756004a8274f89c1.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/662f4592dacdff80258004fc756004a8274f89c1.jpeg 2x" data-dominant-color="E7E9EC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">11</span><span class="informations">769×180 19.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/1426de40b6d188a854cb5416816a58a5b15ac1ca.jpeg" data-download-href="/uploads/short-url/2SgP5NFniL4T3Me37E5UUZgZNiO.JPG?dl=1" title="12" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/1426de40b6d188a854cb5416816a58a5b15ac1ca_2_550x500.JPG" alt="12" data-base62-sha1="2SgP5NFniL4T3Me37E5UUZgZNiO" width="550" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/1426de40b6d188a854cb5416816a58a5b15ac1ca_2_550x500.JPG, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/1426de40b6d188a854cb5416816a58a5b15ac1ca.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/1426de40b6d188a854cb5416816a58a5b15ac1ca.jpeg 2x" data-dominant-color="353440"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">12</span><span class="informations">704×640 40 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @ljod (2017-09-12 13:48 UTC)

<p>Hello Jin. I believe DICOM export of DTI is not supported. What is the use case?</p>

---

## Post #3 by @Jin (2017-12-05 13:39 UTC)

<p>I want to put the DTI data into navigation system, and reconstruct the 3 dimensional image, but all most navigation system can not support the vtk data.</p>

---

## Post #4 by @ihnorton (2017-12-05 14:45 UTC)

<p>If you want to process diffusion-weighted acquisitions into diffusion tensor volumes on a commercial system, you need to use the original DWI DICOM data. Slicer does not support writing DWI DICOM from NRRD files (nor does any other software I know about).</p>

---

## Post #5 by @lassoan (2017-12-05 18:00 UTC)

<p>You have the option to use Slicer with your commercial navigation system.The idea is that you use Slicer to display additional, experimental information during surgeries, without impacting the current workflow. Demo of StealthStation and Slicer showing real-time instrument position:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="UHmv5u-sB5g" data-video-title="Integration of 3D Slicer with Medtronic StealthStation navigation system" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=UHmv5u-sB5g" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/UHmv5u-sB5g/hqdefault.jpg" title="Integration of 3D Slicer with Medtronic StealthStation navigation system" width="" height="">
  </a>
</div>

<p>For your specific use case, you may find <code>U-37 Brain surgery navigation</code> tutorial on <a href="http://www.slicerigt.org/wp/user-tutorial/">SlicerIGT tutorial page</a> useful. It provides step-by-step instructions for setting up brain surgery navigation in Slicer. There is also test data (images and recorded tracking information) that you can use for testing everything without having access to a surgical navigation system or position trackers.</p>
<p><a href="https://1drv.ms/p/s!AhiABcbe1DBygeVDvZ-mv20dBMRY0A"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b1763b80b28e008e86d4c253f361c93ea621d06a.jpeg" alt="2017-12-05_12-54-04" data-base62-sha1="pjTP5NdyqjfI9x3p4Iu2xCEvU26" width="690" height="465"></a></p>
<p>Through SlicerIGT extension and PLUS toolkit, you can connect to BrainLab or Medtronic StealthStation and get patient images and real-time instrument positions. Unfortunately, Stryker don’t have a research interface that Slicer could connect to. In your lab, you can use equivalent but lower-cost tracking systems (such as OptiTrack, cameras starting from $2500 or so). See here an <a href="https://plustoolkit.github.io/features">overview of supported imaging and tracking devices in PLUS</a>.</p>

---
