# Mask Shifting in Segment Editor

**Topic ID**: 18850
**Date**: 2021-07-21
**URL**: https://discourse.slicer.org/t/mask-shifting-in-segment-editor/18850

---

## Post #1 by @Esteban_Barreiro (2021-07-21 11:36 UTC)

<p>Hi everybody! hope you are ok.<br>
I found that sometimes masks from the Segment Editor shift before zoom in or out in Axial, Sagital and Coronal views. Center the views (even with axial,sagital and coronal views linked) does not help at all… Maybe a bug?<br>
Im on Windows 10, Slicer 4.11.20210226 stable version r29738 / 7a59c8.<br>
The steps I do:<br>
Import DICOM file, Link views, go to Segment Editor, Create mask, active Threshold effect, zoom in with interpolation off so I can see the exact pixel value of the pixels I need to segment what I want, zoom out, and bang! mask shift. I attach an image.<br>
Sorry if I creat a topic that was already in disscusion, Icouldnt find anything about it.<br>
Thanks for the great work, love you all guys!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78d5ffeeb0149c15308c35ef53dd658d7d8264a5.png" data-download-href="/uploads/short-url/heXMU2MoftUMSSTZA3vfoVR7wvH.png?dl=1" title="Bug Mascara Segment Editor" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/78d5ffeeb0149c15308c35ef53dd658d7d8264a5_2_690x388.png" alt="Bug Mascara Segment Editor" data-base62-sha1="heXMU2MoftUMSSTZA3vfoVR7wvH" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/78d5ffeeb0149c15308c35ef53dd658d7d8264a5_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/78d5ffeeb0149c15308c35ef53dd658d7d8264a5_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78d5ffeeb0149c15308c35ef53dd658d7d8264a5.png 2x" data-dominant-color="3B3841"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Bug Mascara Segment Editor</span><span class="informations">1364×768 158 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2021-07-21 11:56 UTC)

<p>Thank you for reporting this. I don’t recall anyone having this issue, so there might be something special in your data or software/hardware configuration.</p>
<p>What is the spacing, origin, and axis directions of the input CT image (Volumes module → Volume Information) and the segmentation (Segment Editor module → Specify geometry)?</p>
<p>Does the misalignment get fixed if you hover the mouse over the view?<br>
Does the issue occur if the Data Probe (in the bottom-left corner) is collapsed?</p>
<p>Do you have Intel Graphics card? Is the driver up-to-date?</p>
<p>Is the issue reproducible using the latest Slicer Preview Release?</p>
<p>Can you take a screen capture video?</p>

---
