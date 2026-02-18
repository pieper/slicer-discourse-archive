# Pixel Spacing for volume reconstruction of ultrasound images

**Topic ID**: 33311
**Date**: 2023-12-09
**URL**: https://discourse.slicer.org/t/pixel-spacing-for-volume-reconstruction-of-ultrasound-images/33311

---

## Post #1 by @Pratima (2023-12-09 05:47 UTC)

<p>Hello I am new to 3D slicer.I have a telemed C5-2R60S-3  potable ultrasound probe and windows 11 Pro.I want to scan the abdomen and generate 3d volume.I have used plusApp &amp; Slicer openIGTlinkIF to successfully visualize real-time ultrasound image in Slicer.When I check the details of active volume in slicer,I see pixel spacing (0.2,0.2,0.2) and image size (512,512,1).I also verified same pixel spacing(0.2,0.2,0.2) by exporting image as DICOM file and reading the DICOM metadata .<br>
To check the correctness of pixel spacing:<br>
From github I came to know that we can calculate image height (in mm)=total_pixels in y-axis (512)*pixel spacing in y-axis(0.2) =102.4mm.But I have set the depth of ultrasound as 150mm in echowaveII(telemed) software and I am assuming that  image height should be near to 150 mm.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3a502d7555fb7a95712046f18809a259331898d.png" data-download-href="/uploads/short-url/ucihpPflHpF7QJXbUkfsLcV8n6J.png?dl=1" title="slicer_pixel_spac_issue" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3a502d7555fb7a95712046f18809a259331898d_2_690x304.png" alt="slicer_pixel_spac_issue" data-base62-sha1="ucihpPflHpF7QJXbUkfsLcV8n6J" width="690" height="304" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3a502d7555fb7a95712046f18809a259331898d_2_690x304.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3a502d7555fb7a95712046f18809a259331898d_2_1035x456.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3a502d7555fb7a95712046f18809a259331898d.png 2x" data-dominant-color="898784"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer_pixel_spac_issue</span><span class="informations">1121×495 153 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8b9be2b60412a282dd236626bfda2ae9db3f12c5.png" data-download-href="/uploads/short-url/jV2lO2I98ynA8pCCqbAo9gA1TCZ.png?dl=1" title="slicer_pixel_spac_issue_dicom_data" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8b9be2b60412a282dd236626bfda2ae9db3f12c5_2_478x499.png" alt="slicer_pixel_spac_issue_dicom_data" data-base62-sha1="jV2lO2I98ynA8pCCqbAo9gA1TCZ" width="478" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8b9be2b60412a282dd236626bfda2ae9db3f12c5_2_478x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8b9be2b60412a282dd236626bfda2ae9db3f12c5.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8b9be2b60412a282dd236626bfda2ae9db3f12c5.png 2x" data-dominant-color="F1F1F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer_pixel_spac_issue_dicom_data</span><span class="informations">676×706 211 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I need help to calculate(or find) right pixel spacing and generate multi-frame 3d reconstruction in slicer.<br>
Any help is really appreciated.I am not able to understand how I move forward from this point i.e. without right pixel spacing.<br>
Thank You.</p>

---

## Post #2 by @ungi (2023-12-09 16:05 UTC)

<p>Hi, to reconstruct images in 3D, you need more information about ultrasound image position and orientation, not just spacing. Are you planning to use a position tracker attached to the ultrasound? Like in this video: <a href="https://www.youtube.com/watch?v=2vXeJxYFou4&amp;ab_channel=PerkLabResearch" rel="noopener nofollow ugc">(34) Real-time 3D ultrasound reconstruction using 3D Slicer + SlicerIGT - YouTube</a></p>

---

## Post #3 by @Pratima (2023-12-09 17:06 UTC)

<p>Thank you for the reply.I am aware that calibration using position tracker provides transformation from ultrasound probe to ultrasound image frame leading to a fairly good ultrasound volume .But In my case,I only have position and orientation of ultrasound probe.<br>
So I have 2 main parameters to be found for 3D reconstruction:<br>
1)transformation from ultrasound probe to ultrasound image(or origin in ultrasound image)<br>
2)pixel spacing<br>
How can I find these parameters accurate enough in 3D slicer (or plusApp) ?</p>

---
