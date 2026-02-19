---
topic_id: 28924
title: "Export Segmentation As Dicom In Latest Stable Slicer"
date: 2023-04-14
url: https://discourse.slicer.org/t/28924
---

# Export segmentation as DICOM in latest stable slicer

**Topic ID**: 28924
**Date**: 2023-04-14
**URL**: https://discourse.slicer.org/t/export-segmentation-as-dicom-in-latest-stable-slicer/28924

---

## Post #1 by @Raj_Kumar_Ranabhat (2023-04-14 18:56 UTC)

<p>Hi Channel,</p>
<p>I am trying to export segmentation as a DICOM in latest stable version of 3D slicer . And it seems Quantitate reporting doesn’t work in stable version. Could you please advice ?</p>

---

## Post #2 by @pieper (2023-04-14 18:58 UTC)

<p>I thought it was working because I know a few people have been using it lately. Can you describe what you tried and what happened differently from what you expected?</p>

---

## Post #3 by @Raj_Kumar_Ranabhat (2023-04-14 19:10 UTC)

<p>One of the extension required for it is Quantitative Reporting and there is some error in this module, which can be seen in the python interactor.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fdca84b7b24dc62177b6e91d2505a8ace3d3d724.png" data-download-href="/uploads/short-url/Ad8H0N7dd1bA2RujDzjGxgmQtnu.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fdca84b7b24dc62177b6e91d2505a8ace3d3d724_2_681x499.png" alt="image" data-base62-sha1="Ad8H0N7dd1bA2RujDzjGxgmQtnu" width="681" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fdca84b7b24dc62177b6e91d2505a8ace3d3d724_2_681x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fdca84b7b24dc62177b6e91d2505a8ace3d3d724_2_1021x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fdca84b7b24dc62177b6e91d2505a8ace3d3d724.png 2x" data-dominant-color="D9D8DA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1360×998 109 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>There is no option export as  DICOMsegmentation.</p>
<p>The error seems to be in QR extension and DICOM tab is missing in this installation.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f8acf8f531dfe7db822a2fd68f0321b29e474eb1.png" data-download-href="/uploads/short-url/ztT0hoqJdORW0YiwdGu92wUINbz.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f8acf8f531dfe7db822a2fd68f0321b29e474eb1_2_578x500.png" alt="image" data-base62-sha1="ztT0hoqJdORW0YiwdGu92wUINbz" width="578" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f8acf8f531dfe7db822a2fd68f0321b29e474eb1_2_578x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f8acf8f531dfe7db822a2fd68f0321b29e474eb1_2_867x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f8acf8f531dfe7db822a2fd68f0321b29e474eb1.png 2x" data-dominant-color="B1AFAE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1110×959 194 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @pieper (2023-04-16 16:11 UTC)

<p>Pinging <a class="mention" href="/u/fedorov">@fedorov</a> in case he didn’t see this.</p>

---

## Post #5 by @lassoan (2023-04-16 18:27 UTC)

<p>It works well. What may be unexpected that you need to select the study in the subject hierarchy tree (not the segmentation node).</p>
<p>We should document this better or change the behavior (when a segmentation is selected then we could still offer exporting the segmentation, as the exporter could look up the study).</p>

---

## Post #6 by @Raj_Kumar_Ranabhat (2023-04-16 18:51 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> It seems there is a problem with Quantitative Reporting extension. See attached error in pictures above.</p>
<p>Tried with selecting the study in the subject hierarchy tree but didnot work.</p>
<p>FYI , I am using latest version of stable slicer.</p>
<p>Thanks</p>

---

## Post #7 by @lassoan (2023-04-16 19:17 UTC)

<p>DICOM Segmentation Object can only be exported along with an image (I think it is required by the DICOM standard). Therefore, you need to have the image in the study, too. Drag-and-drop the image in the same study to fix it.</p>
<p>The segmentation also need to specifically refer to an image series. If you have not the created the segmentation by importing and then segmenting a DICOM image then you may need to select the image using the “Specify Geometry” button in Segment Editor module.</p>
<p>The deprecation warnings are just warnings, they do not indicate any problem, just serve as reminders for module developers to switch to more recent API. You can ignore them.</p>

---

## Post #8 by @Raj_Kumar_Ranabhat (2023-04-17 16:13 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> , Thanks. It’s working now. Quick question does imported image, segmentation has to be specific format, say .nrrd ?<br>
I imported nii.gz but having issue with exporting the DICOM segmentation.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/278385b12f21337b7e6ca7ab63c15d691eb1eb98.png" data-download-href="/uploads/short-url/5Dypcl6QFKVfbMaKKnhgoMax3AY.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/278385b12f21337b7e6ca7ab63c15d691eb1eb98.png" alt="image" data-base62-sha1="5Dypcl6QFKVfbMaKKnhgoMax3AY" width="690" height="82" data-dominant-color="FEF0F1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1702×204 12.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Sincerely,<br>
Raj</p>

---

## Post #9 by @lassoan (2023-04-17 16:19 UTC)

<p>The image must have DICOM instance UIDs in them, so if you loaded an image from non-DICOM file then you need to export the image into DICOM format first, load it as a DICOM image, and then export the segmentation with it.</p>

---

## Post #10 by @Raj_Kumar_Ranabhat (2023-04-17 17:32 UTC)

<p>Thank You. Worked well . Please close this case.</p>

---

## Post #11 by @Raj_Kumar_Ranabhat (2023-06-07 18:46 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>, Could you please advise, why I am getting this error now ? I have selected master Volume of segmented as Dicom CT image.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ea8f9b8dcba73752d3146ab8b804ca4161dc3fcc.png" data-download-href="/uploads/short-url/xt1paJz4UlM4AGomwDzxtK7KXIU.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ea8f9b8dcba73752d3146ab8b804ca4161dc3fcc_2_690x486.png" alt="image" data-base62-sha1="xt1paJz4UlM4AGomwDzxtK7KXIU" width="690" height="486" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ea8f9b8dcba73752d3146ab8b804ca4161dc3fcc_2_690x486.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ea8f9b8dcba73752d3146ab8b804ca4161dc3fcc_2_1035x729.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ea8f9b8dcba73752d3146ab8b804ca4161dc3fcc_2_1380x972.png 2x" data-dominant-color="DCDDE4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1430×1009 186 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #12 by @lassoan (2023-06-07 20:08 UTC)

<p>Slicer 4.11 is a very old version. Please use at least the latest Slicer Stable Relase (currently Slicer-5.2.2).</p>

---
