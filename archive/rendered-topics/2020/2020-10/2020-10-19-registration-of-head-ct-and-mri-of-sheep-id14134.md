---
topic_id: 14134
title: "Registration Of Head Ct And Mri Of Sheep"
date: 2020-10-19
url: https://discourse.slicer.org/t/14134
---

# Registration of head CT and MRI of sheep

**Topic ID**: 14134
**Date**: 2020-10-19
**URL**: https://discourse.slicer.org/t/registration-of-head-ct-and-mri-of-sheep/14134

---

## Post #1 by @ADeane (2020-10-19 12:17 UTC)

<p>Hi all,</p>
<p>Goal: accurately registering head CT (bone) and T1 MRI from ovine subject - to be used for surgical planning.</p>
<p>Problem:  unable to apply general registration (BRAINS)</p>
<p>I am new to using 3D slicer for registration. I am currently attempting to register CT bone and T1 weighted MRI scans (head). The resulting registration will be used to plan neurosurgeries.</p>
<p>So far, I have manually transformed the CT scan to align with the MRI (both have been centred). I have attempted to then use general registration (BRAINS), however the resulting output is grey squares.</p>
<p>See google drive link for the DICOM images being used.</p>
<aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://ssl.gstatic.com/images/branding/product/1x/drive_2020q4_32dp.png" class="site-icon" width="32" height="32">
      <a href="https://drive.google.com/drive/folders/1KQdATjr6bvReNBIXqQa6QRO-NH9x3m0n?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>
  <article class="onebox-body">
    <img src="" class="thumbnail" width="" height="">

<h3><a href="https://drive.google.com/drive/folders/1KQdATjr6bvReNBIXqQa6QRO-NH9x3m0n?usp=sharing" target="_blank" rel="noopener nofollow ugc">Ovine CT-MRI - Google Drive</a></h3>



  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Any help or guidance would be greatly appreciated!</p>
<p>Ashley</p>

---

## Post #2 by @lassoan (2020-10-20 04:33 UTC)

<p>Default parameters of “General registration (BRAINS)” module work for human brain registration but you need to tune the parameters to work for other cases.</p>
<p>“General registration (Elastix”) module (provided by SlicerElastix extension) is much more robust. Its default parameter set works well for most registration tasks, as long as the two images approximately contain the same region.</p>
<p>Fully automatic registration of your data set took 2 minutes on my laptop using Elastix, using default parameter set, and the result looks almost perfect:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/70630cd799df9c01be990709bf3810d75cfd299e.jpeg" data-download-href="/uploads/short-url/g2dGP0GNWL64hAfVTY0REyUBur4.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/70630cd799df9c01be990709bf3810d75cfd299e_2_690x420.jpeg" alt="image" data-base62-sha1="g2dGP0GNWL64hAfVTY0REyUBur4" width="690" height="420" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/70630cd799df9c01be990709bf3810d75cfd299e_2_690x420.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/70630cd799df9c01be990709bf3810d75cfd299e_2_1035x630.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/70630cd799df9c01be990709bf3810d75cfd299e_2_1380x840.jpeg 2x" data-dominant-color="454444"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1375 837 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/2561cc893ce870edaafb0504b6d33fe4de711c66.gif" alt="SlicerCapture" data-base62-sha1="5kHcnLC489DwtrbSm8wRil77KBw" width="445" height="500" class="animated"></p>

---

## Post #3 by @CASmith (2022-01-10 00:33 UTC)

<p>Hi Ashley,</p>
<p>I am working on a similar project as you were, where a regisetered CT/MRI image of a sheep head would be amazingly useful for device design and surgical planning,</p>
<p>Is there any chance you would be able to post an updated link to you dicom files (or the registered image)?</p>
<p>Best regards,<br>
Chris S</p>

---

## Post #4 by @ADeane (2022-01-11 00:34 UTC)

<p>Hi Chris,</p>
<p>Unfortunately I have changed jobs and therefore no longer have access to these images.</p>
<p>Best of luck,<br>
Ashley</p>

---

## Post #5 by @CASmith (2022-01-11 00:56 UTC)

<p>Fair enough.</p>
<p>Thanks Ashley</p>
<p>Chris</p>

---

## Post #6 by @Matteo_Donega (2022-10-21 12:03 UTC)

<p>Hi Chris <a class="mention" href="/u/casmith">@CASmith</a> did you have any luck in finding an MRI/CT of a sheep? I have the same interested and would benefit from this too. Many thanks</p>

---
