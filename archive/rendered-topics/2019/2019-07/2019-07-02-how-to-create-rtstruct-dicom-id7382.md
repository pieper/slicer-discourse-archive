---
topic_id: 7382
title: "How To Create Rtstruct Dicom"
date: 2019-07-02
url: https://discourse.slicer.org/t/7382
---

# How to create RTStruct dicom  

**Topic ID**: 7382
**Date**: 2019-07-02
**URL**: https://discourse.slicer.org/t/how-to-create-rtstruct-dicom/7382

---

## Post #1 by @agatte (2019-07-02 15:26 UTC)

<p>Hello,</p>
<p>I have already created labelmap image with segmentation. I would like to export this file to RTStruct.<br>
I would like to create RTStruct image. Is this possible in Slicer ? In which module ?</p>
<p>I would be appreciate for any info.</p>
<p>Best,<br>
agatte</p>

---

## Post #2 by @cpinter (2019-07-02 15:39 UTC)

<p>Here’s information about DICOM export: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM#DICOM_export" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM#DICOM_export</a></p>
<p>You need to have a study in the Data module that contains the master volume and the segmentation.</p>
<p>If you have your segmentation as a labelmap node then first you need to convert it to a segmentation node. RIght-click labelmap, then “Convert labelmap to segmentation node”.</p>

---

## Post #3 by @agatte (2019-07-09 07:53 UTC)

<p>Hi Csaba Pinter,</p>
<p>I have already tried to follow the video youtube tutorial from wiki that you send me.</p>
<p>But it doesn’t work on  current version. I followed the tutorial and I can create a dicom series from CT but I cant save RTSTRUCT in Slicer 4.10</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/0868c4f6e0f178fc9f5fe0da0fd3eaa9b98f1226.png" data-download-href="/uploads/short-url/1cohNO5JdJdXoSCI75SV1ISY3CC.png?dl=1" title="exportSegmentationAsRTSTRUCT.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/0868c4f6e0f178fc9f5fe0da0fd3eaa9b98f1226_2_690x369.png" alt="exportSegmentationAsRTSTRUCT.png" data-base62-sha1="1cohNO5JdJdXoSCI75SV1ISY3CC" width="690" height="369" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/0868c4f6e0f178fc9f5fe0da0fd3eaa9b98f1226_2_690x369.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/0868c4f6e0f178fc9f5fe0da0fd3eaa9b98f1226_2_1035x553.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/0868c4f6e0f178fc9f5fe0da0fd3eaa9b98f1226.png 2x" data-dominant-color="AEAEB1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">exportSegmentationAsRTSTRUCT.png</span><span class="informations">1284×688 333 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>In tutorial it looked like it is possible to save RTSTRUCT and corresponding CT.</p>
<p>But here I have only one option.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8ffcd9ba853e379f121c32fdde2dacbd9bc7f3d8.png" data-download-href="/uploads/short-url/kxM0uF96TaaxqX2wpRjeWYyiYGI.png?dl=1" title="ProblemExportRTSTRUCTdicom.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8ffcd9ba853e379f121c32fdde2dacbd9bc7f3d8_2_690x386.png" alt="ProblemExportRTSTRUCTdicom.png" data-base62-sha1="kxM0uF96TaaxqX2wpRjeWYyiYGI" width="690" height="386" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8ffcd9ba853e379f121c32fdde2dacbd9bc7f3d8_2_690x386.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8ffcd9ba853e379f121c32fdde2dacbd9bc7f3d8_2_1035x579.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8ffcd9ba853e379f121c32fdde2dacbd9bc7f3d8_2_1380x772.png 2x" data-dominant-color="C7C8CE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ProblemExportRTSTRUCTdicom.png</span><span class="informations">1917×1073 317 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I would be appreciate for any help please.</p>
<p>Best regards,</p>
<p>agatte</p>

---

## Post #4 by @cpinter (2019-07-09 14:04 UTC)

<p>You need to right-click the study in order for the RT DICOM plugin to discover all the nodes.<br>
I think it should be able to find the segmentation even under the volume, but let me know otherwise.</p>

---
