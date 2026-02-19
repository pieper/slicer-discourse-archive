---
topic_id: 8361
title: "Petctfusion Dealing With Pet And Ct Dicom Images"
date: 2019-09-10
url: https://discourse.slicer.org/t/8361
---

# PETCTfusion (dealing with PET and CT DICOM images)

**Topic ID**: 8361
**Date**: 2019-09-10
**URL**: https://discourse.slicer.org/t/petctfusion-dealing-with-pet-and-ct-dicom-images/8361

---

## Post #1 by @Nora (2019-09-10 12:18 UTC)

<p>Hi,</p>
<p>I’m trying to put my head around 3D slicer.<br>
I’ve downloaded version 4.10.2 and 4.11.0. I’ll be working with PET/CT images.</p>
<p>I’m trying to find PETCTfusion module but I couldn’t find it on the list, not even on the extension manger.<br>
I have bunch of CT and PET DICOM images and I want to segment tumours and calculate some features.</p>
<p>Appreciate your help.</p>

---

## Post #2 by @lassoan (2019-09-11 18:53 UTC)

<p>PETCTFusion module was developed for Slicer-3.x. In current Slicer-4.x version it is replaced by other modules. See details here: <a href="https://www.slicer.org/wiki/Documentation/4.10/Modules/PETStandardUptakeValueComputation" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/4.10/Modules/PETStandardUptakeValueComputation</a>.</p>

---

## Post #3 by @mlewis1973 (2021-12-17 19:27 UTC)

<p>I believe the PETCTfusion module made the process of fusing PET and CT volumes easier than doing it manually.  PETStandardUptakeValueComputation is based on PETCTFusion, but it doesn’t have the fusion tools, just the metric extraction tools.  Anyone seen a nice PET-CT automatic fusion tool that<br>
requires minimal mouse clicks?</p>

---

## Post #4 by @mikbuch (2023-02-16 14:32 UTC)

<p>Hi <a class="mention" href="/u/mlewis1973">@mlewis1973</a> , did you by any chance find a way (a module) to perform PET/CT fusion in Slicer?</p>

---

## Post #5 by @mikbuch (2023-02-18 23:37 UTC)

<p>A quick workaround to achieve PET-CT fusion would be to overlay PET scan over CT image using standard Slicer 3D visualization functionalities. The result is presented below:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1e6165a5ca62ec9ca3cb09da94fa2120d1ee06f5.jpeg" data-download-href="/uploads/short-url/4kKZLZ80El3xxQNLJwGjJcVoKK9.jpeg?dl=1" title="PET-CT_Fusion_PETish-colormap" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1e6165a5ca62ec9ca3cb09da94fa2120d1ee06f5_2_690x435.jpeg" alt="PET-CT_Fusion_PETish-colormap" data-base62-sha1="4kKZLZ80El3xxQNLJwGjJcVoKK9" width="690" height="435" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1e6165a5ca62ec9ca3cb09da94fa2120d1ee06f5_2_690x435.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1e6165a5ca62ec9ca3cb09da94fa2120d1ee06f5_2_1035x652.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1e6165a5ca62ec9ca3cb09da94fa2120d1ee06f5_2_1380x870.jpeg 2x" data-dominant-color="51565D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">PET-CT_Fusion_PETish-colormap</span><span class="informations">3906×2464 913 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Here I explain how to overlay the images: <a href="https://discourse.slicer.org/t/show-two-volumes-overlaid/2626/5" class="inline-onebox">Show two volumes overlaid - #5 by mikbuch</a></p>

---
