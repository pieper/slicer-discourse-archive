---
topic_id: 36487
title: "Volume In Quantification Module"
date: 2024-05-30
url: https://discourse.slicer.org/t/36487
---

# Volume in Quantification Module

**Topic ID**: 36487
**Date**: 2024-05-30
**URL**: https://discourse.slicer.org/t/volume-in-quantification-module/36487

---

## Post #1 by @mira_mira (2024-05-30 04:01 UTC)

<p>Hi Everyone,</p>
<p>I am new user in 3D slicer and currently working on metal foam. My difficulty is to compare the quantification data of solid matrix Volume with the data that I obtained using CTan, microCT.</p>
<p>My question is, can I use straight away the Volume that I obtained in quantification-statistics module as my volume solid matrix after the segmentation process? If yes, Why the volume is too large compare to the physical volume (total volume) which is only 700mm3?</p>
<p>I need to find the void volume, so it is easier to use formula of<br>
Total volume minus Volume of solid matrix. But the total volume is much smaller than volume of solid matrix which I cannot calculate.</p>
<p>Attach the segmentation metal foam and statistic data.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/739180eb94b7aee4f91000fd0afddbab95070a7e.png" data-download-href="/uploads/short-url/gumEfcoV1zkPJlRgdXfMXMCm1Fs.png?dl=1" title="3Dmodel" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/739180eb94b7aee4f91000fd0afddbab95070a7e_2_690x442.png" alt="3Dmodel" data-base62-sha1="gumEfcoV1zkPJlRgdXfMXMCm1Fs" width="690" height="442" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/739180eb94b7aee4f91000fd0afddbab95070a7e_2_690x442.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/739180eb94b7aee4f91000fd0afddbab95070a7e.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/739180eb94b7aee4f91000fd0afddbab95070a7e.png 2x" data-dominant-color="8B94B6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3Dmodel</span><span class="informations">906×581 172 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c9d311eeaeb68084b7d72d03fa265ed5db0de99e.png" data-download-href="/uploads/short-url/sNqbB1YJR8pIPf5FkgisahXiOCy.png?dl=1" title="15 PPI" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c9d311eeaeb68084b7d72d03fa265ed5db0de99e.png" alt="15 PPI" data-base62-sha1="sNqbB1YJR8pIPf5FkgisahXiOCy" width="690" height="67" data-dominant-color="E5D6AB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">15 PPI</span><span class="informations">845×83 3.64 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks a lot for help.<br>
-Amirah-</p>

---

## Post #2 by @rfenioux (2024-05-30 11:31 UTC)

<p>It could be a problem with units. The first thing you should check is if the spacing of the voxels is correct. You can specify it in the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/volumes.html#panels-and-their-use" rel="noopener nofollow ugc">volume information panel</a> of the volume module.</p>
<p><a href="https://discourse.slicer.org/t/setting-up-units-in-slicer/34861">This post</a> might also be relevant if it is indeed a units problem.</p>

---

## Post #3 by @mira_mira (2024-05-30 23:47 UTC)

<p>Hi Roman,</p>
<p>Thanks for reply. The spacing of voxel has been set as 1mm but the output voxel is automatically been set as 2mm. Is there any relevant to this issue?<br>
-Amirah-</p>

---

## Post #4 by @lassoan (2024-05-31 00:31 UTC)

<p>You will get correct volume and surface measurement values if you see correct spacing values in Volumes module. You can easily change spacing values in a volume (just type the correct value in the inputbox). However, if you already created a segmentation then you need to apply a transformation that scales the segmentation to the correct size.</p>
<p>The correct voxel spacing must be much smaller than 1mm, because 700mm3 total volume means that your scanned object size is approximately 10 x 10 x 10 mm and there are hundreds of voxels along each axis, so probably the correct magnitude of the spacing is around 0.01mm.</p>
<p>For the future, it would make everything simpler if you ask the CT acquisition technician to acquire the image in standard DICOM format, or if you get in images in a format that does not store 3D image geometry properly (such as TIFF) then carefully set the correct image spacing manually before you start segmenting the image. <a class="mention" href="/u/muratmaga">@muratmaga</a> may have more specific advice, depending on what microCT manufacturer/model you use.</p>

---

## Post #5 by @muratmaga (2024-05-31 01:47 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="36487">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> may have more specific advice, depending on what microCT manufacturer/model you use.</p>
</blockquote>
</aside>
<p>SlicerMorph has two import utilities one for Bruker instruments and the other for GE (phoenix). As far as I know Scanco format (aim) is directly supported in Slicer.</p>
<p>Depending on how the data is provided to you, you can use the ImageStacks in SlicerMorph extension to import them, and during the import time you can enter the correct image spacing information.</p>

---

## Post #6 by @mira_mira (2024-05-31 02:53 UTC)

<p>Thank you for the feedbacks.</p>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> I have the BMP images from CT scan by Bruker and have use the image stacks function. The statistics data were wrong probably due to spacing information.</p>
<p>I will retry again by inserting spacing of 0.01mm as suggested by <a class="mention" href="/u/lassoan">@lassoan</a>. If there are any way to know the correct magnitude for the sample, please let me know.</p>
<p>-amirah-</p>

---

## Post #7 by @muratmaga (2024-05-31 03:50 UTC)

<p>Use the skyscanreconImport. Just point out to the reconstruction log file and spacing information should be entered automatically.</p>

---
