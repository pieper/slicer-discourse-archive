---
topic_id: 19535
title: "The Result Of Segmentation Looks Flat"
date: 2021-09-07
url: https://discourse.slicer.org/t/19535
---

# The result of segmentation looks flat

**Topic ID**: 19535
**Date**: 2021-09-07
**URL**: https://discourse.slicer.org/t/the-result-of-segmentation-looks-flat/19535

---

## Post #1 by @Damir_G (2021-09-07 01:35 UTC)

<p>Hello,<br>
I am working with CT scan images of a permafrost core. I am using 3D Slicer to get a 3D model of constituents. I.e. I have a stack of images and certain threshold values and I use “Segment Editor” in 3D Slicer.</p>
<p>On the first attached image, you see a same CT image in Fiji, left is the original, and right with a certain threshold range chosen. The second image is the result I get in 3D slicer. I would like to get some advice regarding the interpretation of the result. Namely, with a flat area in the middle. Should it be so perfectly flat or am I missing something? Is there any way to make that flat area look less artificial?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/904d8cc24f553abfeb5c5c78a62fea27417e1085.jpeg" data-download-href="/uploads/short-url/kAyU8MuCfTCYMYBZMdnIVxV7Ndz.jpeg?dl=1" title="2021-09-07 01_24_47-nlm_1398x1416,1566_POS2-1.tif (50%)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/904d8cc24f553abfeb5c5c78a62fea27417e1085_2_690x348.jpeg" alt="2021-09-07 01_24_47-nlm_1398x1416,1566_POS2-1.tif (50%)" data-base62-sha1="kAyU8MuCfTCYMYBZMdnIVxV7Ndz" width="690" height="348" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/904d8cc24f553abfeb5c5c78a62fea27417e1085_2_690x348.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/904d8cc24f553abfeb5c5c78a62fea27417e1085_2_1035x522.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/904d8cc24f553abfeb5c5c78a62fea27417e1085_2_1380x696.jpeg 2x" data-dominant-color="826767"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2021-09-07 01_24_47-nlm_1398x1416,1566_POS2-1.tif (50%)</span><span class="informations">1418×716 129 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a7793324b675480822ff9af6c904ed6b5561bf9.jpeg" data-download-href="/uploads/short-url/aCLwiSkdCKVuyD2fMxFjmj7ezwd.jpeg?dl=1" title="2021-09-07 01_25_05-3D Slicer 4.11.20210226" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4a7793324b675480822ff9af6c904ed6b5561bf9_2_479x500.jpeg" alt="2021-09-07 01_25_05-3D Slicer 4.11.20210226" data-base62-sha1="aCLwiSkdCKVuyD2fMxFjmj7ezwd" width="479" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4a7793324b675480822ff9af6c904ed6b5561bf9_2_479x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4a7793324b675480822ff9af6c904ed6b5561bf9_2_718x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a7793324b675480822ff9af6c904ed6b5561bf9.jpeg 2x" data-dominant-color="88899F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2021-09-07 01_25_05-3D Slicer 4.11.20210226</span><span class="informations">833×869 118 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thank you.</p>

---

## Post #2 by @muratmaga (2021-09-07 01:44 UTC)

<p>The images you show in FiJi are cross-sectional slices, and whereas the image from Slicer is the 3D rendering of the segmentation. So they are not totally equal.</p>
<p>If this is the very first/last slice in the stack, 3D rendering will appear flat on those ends, because it is like you put through your core through a microtome and cut it right there. You can play with shading and material settings a bit to make it less shiny, but ultimately it is flat because your data ends there.</p>

---

## Post #3 by @Damir_G (2021-09-08 11:29 UTC)

<p>Dear <a class="mention" href="/u/muratmaga">@muratmaga</a>, thank you for the clarification.<br>
Images I used for the 3D model, are not first nor last in the image stack, however, I think it wouldn’t change the outcome.</p>
<p>if you don’t mind, I would like to ask a couple more questions. Is it possible in 3D slicer somehow to remove 10 slices from the beginning and end? And if so, will there be any change regarding that flat area?</p>
<p>Thank you.</p>

---

## Post #4 by @lassoan (2021-09-09 12:05 UTC)

<p>You can adjust the displayed region of interest (ROI) in the Volume Rendering module. You can also use Crop volume module to persistently cut off parts of a volume. If the ROI box is aligned with the volume axes (that is probably the default) then the appearance will be a similar very straight cut. If you rotate the view then the cut will be jagged, but most likely this will not be visually more appealing.</p>
<p>You can adjust material properties in Volume Rendering module to make the material more or less shiny, shift the transfer functions or move points of the opacity transfer function to make parts of the volume more or less transparent. You can also adjust the lighting in Lights module (in Sandbox extension).</p>

---
