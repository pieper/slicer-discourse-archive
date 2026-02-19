---
topic_id: 35946
title: "Discrepancy In Image Origin Values Between 3D Slicer And Sim"
date: 2024-05-06
url: https://discourse.slicer.org/t/35946
---

# Discrepancy in Image Origin Values between 3D Slicer and SimpleITK

**Topic ID**: 35946
**Date**: 2024-05-06
**URL**: https://discourse.slicer.org/t/discrepancy-in-image-origin-values-between-3d-slicer-and-simpleitk/35946

---

## Post #1 by @ibrahim_ciftci (2024-05-06 15:56 UTC)

<p>Hi all,</p>
<p>I’m encountering an issue when loading a label in 3D Slicer. The image origin is displayed as follows: -8.7478mm, -66.3176mm, -70.4628mm. However, when I read the same label using SimpleITK, I get an output of (8.74779987335205, 66.31759643554688, -70.46279907226562). Additionally, I’m experiencing a similar problem with the IJK TO RAS DIRECTION MATRIX; in 3D Slicer, values that are +1 appear as -1 in SimpleITK.</p>
<p>Could someone please shed light on why this might be happening?</p>
<p>Thanks in advance!</p>

---

## Post #2 by @pieper (2024-05-06 16:24 UTC)

<p>This info should help: <a href="https://slicer.readthedocs.io/en/latest/user_guide/coordinate_systems.html" class="inline-onebox">Coordinate systems — 3D Slicer documentation</a></p>

---

## Post #3 by @ibrahim_ciftci (2024-05-07 06:00 UTC)

<p>Thanks for your prompt response. I think I may not have explained what I need properly. When I load the same Nifti file in both 3D Slicer and SimpleITK, the origins appear differently as shown in the screenshots I provided. In 3D Slicer, it’s one value, while in SimpleITK, it’s another.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e5c4f266a6c2709fd4f675d70474861e9261160.png" data-download-href="/uploads/short-url/232shdx7YseW7u4Jj9FWLI0Mj5u.png?dl=1" title="3dslicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e5c4f266a6c2709fd4f675d70474861e9261160.png" alt="3dslicer" data-base62-sha1="232shdx7YseW7u4Jj9FWLI0Mj5u" width="690" height="175" data-dominant-color="F4F4F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3dslicer</span><span class="informations">746×190 4.43 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0d00224e4a374b0174757dc0ba243f30ba1bdc73.png" data-download-href="/uploads/short-url/1R0uDNATe2f6KFxeAJ1XN0nEa1t.png?dl=1" title="komut" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0d00224e4a374b0174757dc0ba243f30ba1bdc73.png" alt="komut" data-base62-sha1="1R0uDNATe2f6KFxeAJ1XN0nEa1t" width="690" height="75" data-dominant-color="1B1B1B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">komut</span><span class="informations">1101×121 4.73 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @muratmaga (2024-05-07 06:07 UTC)

<p>Values are the same, but the signs of the first two axis are different. That because Slicer uses a RAS coordinate system and ITK uses LPS. Please read the coordinate system documentation that was shared.</p>

---

## Post #5 by @ibrahim_ciftci (2024-05-08 10:16 UTC)

<p>I am encountering an issue while trying to align DICOM images converted to NIfTI format with their corresponding labels. Despite my attempts to match the spacing direction and origin values, I am facing the following error. I believe the issue may be related to the 4th dimension, but I’m uncertain how to address it. Could someone please provide guidance on how to properly align the image and label in NIfTI format? Additionally, I’m unclear about the significance of the 4th dimension and how to ensure compatibility between the image and label.</p>
<p>Thank you for your assistance.</p>
<p>I apologize for any grammatical or syntactical errors due to my limited proficiency in English.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c89aa41c331461eea65e79ac9246a8607ed78f25.png" data-download-href="/uploads/short-url/sCCOhzqI1Bo1HixRAOYrHLIMJs9.png?dl=1" title="err" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c89aa41c331461eea65e79ac9246a8607ed78f25.png" alt="err" data-base62-sha1="sCCOhzqI1Bo1HixRAOYrHLIMJs9" width="690" height="167" data-dominant-color="262726"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">err</span><span class="informations">1081×262 12.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/337b9c2a5b6a6e25998fa2701af3603f210725ca.png" alt="slc" data-base62-sha1="7lrbqe4jTsB8DvZV1VtPaESaASm" width="428" height="404"></p>

---

## Post #6 by @Davide_Scorza (2024-05-08 11:54 UTC)

<p>The direction should be only the rotation component of the transform matrix (3x3).<br>
The Direction you are showing in the prompt is a 4x4, as an homogeneous transform matrix (even if translations are set to zero).</p>
<p>I guess that passing only the rotational component should fix the problem.</p>

---

## Post #7 by @ibrahim_ciftci (2024-05-08 13:03 UTC)

<p>Thank you for the response, but I didn’t quite understand the solution you mentioned. I’m using SimpleITK to convert DICOM to NIfTI, and I’m still unclear on how to implement the solution you suggested. Could you please provide a more detailed explanation on how to apply it in the context of SimpleITK or a DICOM to NIfTI library?</p>

---

## Post #8 by @muratmaga (2024-05-08 17:46 UTC)

<aside class="quote no-group" data-username="ibrahim_ciftci" data-post="1" data-topic="35946">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ibrahim_ciftci/48/70309_2.png" class="avatar"> ibrahim_ciftci:</div>
<blockquote>
<p>Could someone please shed light on why this might be happening?</p>
</blockquote>
</aside>
<p>This is already answered here:</p>
<aside class="quote no-group" data-username="muratmaga" data-post="4" data-topic="35946">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>hat because Slicer uses a RAS coordinate system and ITK uses LPS. P</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="ibrahim_ciftci" data-post="5" data-topic="35946">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ibrahim_ciftci/48/70309_2.png" class="avatar"> ibrahim_ciftci:</div>
<blockquote>
<p>I am encountering an issue while trying to align DICOM images converted to NIfTI format with their corresponding labels.</p>
</blockquote>
</aside>
<p>Where are you having these issues? Is this in Slicer? How are these files generated? I see one is DICOM, but where is the labelmap coming from?</p>
<p>In any event,  if you create a lineaer transformation with first two diagonal values are -1, and everythig left as unchanged and put the labelmap under this transform you should be able to line up your two dataset.</p>

---

## Post #9 by @ibrahim_ciftci (2024-05-09 12:34 UTC)

<p>In the dataset I’m working on related to breast cancer, the label file is in .dcm format, while the images are in a series of .dcm files. To be able to train them in an nnU-Net model, I’ve used a Python script with libraries like SimpleITK or DICOM to NIfTI to convert both files’ formats from DICOM to NIfTI. However, when I reload them into the 3D Slicer program, I encounter discrepancies between the images and the labels. These issues were not present when the files were in DICOM format.</p>
<p>I suspect these discrepancies arise from the images being in 4D format and the inadequacy of the libraries I’m using for this conversion process. I sought assistance regarding these transformations, aiming to preserve values like spacing, direction, origin, etc., without distortion.</p>

---

## Post #10 by @muratmaga (2024-05-09 13:23 UTC)

<p>What happens when you create a transform like this, and assign your segmentation to it?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b4c169f97368cff3db43bc2ef5b397c0c069e20.png" data-download-href="/uploads/short-url/1BWgMO3magctU6B4SlM62qT3Zn2.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b4c169f97368cff3db43bc2ef5b397c0c069e20_2_517x322.png" alt="image" data-base62-sha1="1BWgMO3magctU6B4SlM62qT3Zn2" width="517" height="322" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b4c169f97368cff3db43bc2ef5b397c0c069e20_2_517x322.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b4c169f97368cff3db43bc2ef5b397c0c069e20_2_775x483.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b4c169f97368cff3db43bc2ef5b397c0c069e20.png 2x" data-dominant-color="EAEBEB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1006×628 28 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #11 by @AlfredoMoralesPinzon (2024-05-09 14:49 UTC)

<p>Did you use dcm2niix?</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/rordenlab/dcm2niix">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/rordenlab/dcm2niix" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/d109a732f334c8b741b6193ea60439fad5f4831cb935c2aa68c03cb31c5e7611/rordenlab/dcm2niix" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/rordenlab/dcm2niix" target="_blank" rel="noopener nofollow ugc">GitHub - rordenlab/dcm2niix: dcm2nii DICOM to NIfTI converter: compiled...</a></h3>

  <p>dcm2nii DICOM to NIfTI converter: compiled versions available from NITRC - rordenlab/dcm2niix</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>You can also load you DICOM images in Slicer and save them as nifti. This would allow you to double check the issues after converting DICOM to nifti when using your scripts.</p>
<p>I hope this could help.</p>

---
