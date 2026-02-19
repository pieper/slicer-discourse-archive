---
topic_id: 14986
title: "Problem With Paint Option And Does Not Save Segments Of Spec"
date: 2020-12-10
url: https://discourse.slicer.org/t/14986
---

# Problem with paint option and does not save segments of specific files

**Topic ID**: 14986
**Date**: 2020-12-10
**URL**: https://discourse.slicer.org/t/problem-with-paint-option-and-does-not-save-segments-of-specific-files/14986

---

## Post #1 by @einav (2020-12-10 14:08 UTC)

<p>Hello,</p>
<p>I have problems when I want to paint and save.<br>
When I use paint function on specific files it’s unresponsive. It happens in files:<br>
346_CINE.MR.PHILIP_PIG_HEART.0011.0025.2018.09.21.12.51.56.134255.48874629.IMA<br>
346_CINE.MR.PHILIP_PIG_HEART.0012.0025.2018.09.21.12.51.56.134255.48875754.IMA<br>
And it works in:346_CINE.MR.PHILIP_PIG_HEART.0010.0025.2018.09.21.12.51.56.134255.48873380.IMA</p>
<p>If I open the problematic files in new window I can paint and save it. But when I open it again the paint gone.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fba7fb6a5f59b10f6f79da02d48a174cd0518e68.png" data-download-href="/uploads/short-url/zUfKbZot45IxhKOJW59b1zAi0m4.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fba7fb6a5f59b10f6f79da02d48a174cd0518e68_2_345x178.png" alt="image" data-base62-sha1="zUfKbZot45IxhKOJW59b1zAi0m4" width="345" height="178" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fba7fb6a5f59b10f6f79da02d48a174cd0518e68_2_345x178.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fba7fb6a5f59b10f6f79da02d48a174cd0518e68_2_517x267.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fba7fb6a5f59b10f6f79da02d48a174cd0518e68_2_690x356.png 2x" data-dominant-color="595961"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1918×994 130 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The files attached.<br>
<a href="https://drive.google.com/drive/folders/1_ijHdkyheEZw_QiX2N3ev5LoGrHohNOC?usp=sharing" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/drive/folders/1_ijHdkyheEZw_QiX2N3ev5LoGrHohNOC?usp=sharing</a><br>
3DSlicer version: 4.11<br>
perating system: Windows 10</p>
<p>If there is any advice on how to edit in a better way I would love to know.</p>
<p>One more question, There is a way I can zoom in, save the file and next time it will open with the zoom in?</p>
<p>Thanks a lot,<br>
Einav.</p>

---

## Post #2 by @lassoan (2020-12-11 15:19 UTC)

<p>When you create a segmentation, the extent is determined from the master volume that you choose first. You cannot paint outside this extent. If you want to extend the segmentation region then you need to modify segmentation’s geometry (using “Specify geometry” button in Segment Editor).</p>
<p>Since you created the segmentation with a specific frame and then changed the master volume, to a different one, which was outside the extent of the first one, you were not able to paint on it.</p>
<p>You could change the segmentation’s geometry to include all frames into the extents, but since the segments actually make up a 3D volume it is easier to load the frames as a volume and do volumetric segmentation. DICOM module just does not recognize that the series make up a single 3D volume because each frame has different series instance UID.</p>
<p>I would recommend to change all the series instance UIDs in the DICOM files to the same value and then load the data as 3D volume. I’ve added a new “Force same series instance UID in each directory” option to DICOM patcher (will be available from tomorrow in Slicer Preview Release), which can do this for you automatically - you just need to place all frames of a volume into a single folder. I’ve created the volume for you, you can download it from <a href="https://1drv.ms/u/s!Arm_AFxB9yqHxM4UlI5-5E4G8y0q4g?e=y2ks3a">here</a> if you don’t want to wait until tomorrow.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/9507acc298c2f03c1be2e85f53b325863337000e.png" data-download-href="/uploads/short-url/lgnAm1A8VU280wjHiVtYdCSaZv8.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9507acc298c2f03c1be2e85f53b325863337000e_2_690x398.png" alt="image" data-base62-sha1="lgnAm1A8VU280wjHiVtYdCSaZv8" width="690" height="398" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9507acc298c2f03c1be2e85f53b325863337000e_2_690x398.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9507acc298c2f03c1be2e85f53b325863337000e_2_1035x597.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9507acc298c2f03c1be2e85f53b325863337000e_2_1380x796.png 2x" data-dominant-color="908F90"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1301 467 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @einav (2020-12-14 17:35 UTC)

<p>Hi,</p>
<p>First of all thank you.<br>
But can I get explanation how to use this function because when I used it I got the attached folder named “pa000” and not one file of volume.<br>
In addition, how can I check slice thickness in this case?</p>
<aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://ssl.gstatic.com/images/branding/product/1x/drive_2020q4_32dp.png" class="site-icon" width="16" height="16">
      <a href="https://drive.google.com/drive/folders/1u62znUWL4MgFrTTX_GSaOgDy_i5nI27q?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>
  <article class="onebox-body">
    <img src="" class="thumbnail" width="16" height="16">

<h3><a href="https://drive.google.com/drive/folders/1u62znUWL4MgFrTTX_GSaOgDy_i5nI27q?usp=sharing" target="_blank" rel="noopener nofollow ugc">pa000 - Google Drive</a></h3>



  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Thanks,<br>
Einav.</p>

---
