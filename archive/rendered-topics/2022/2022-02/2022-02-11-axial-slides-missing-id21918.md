# Axial slides missing

**Topic ID**: 21918
**Date**: 2022-02-11
**URL**: https://discourse.slicer.org/t/axial-slides-missing/21918

---

## Post #1 by @HodaGH (2022-02-11 15:01 UTC)

<p>Hi,</p>
<p>I have .AIM files of murine caudal vasculature from Scanco micro-CT which I opened with imagej , changed it to .NRRD and was able to open it in Slicer based on <a href="https://discourse.slicer.org/t/support-for-aim-isq-files-generated-on-scanco-microct/6261">this</a> discussion. The image looks ok in imagej and also opened it with python scripts so no problem with my image but when I load it in Slicer some of the axial slides are missing. Is there any way to solve this? If not is there any way to connect the pieces in my segmentation?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c9864da484089a5f998c6c0ff9dc29e0282b0eff.jpeg" data-download-href="/uploads/short-url/sKLIkAWTiMBbsdwUkyWPZcV5899.jpeg?dl=1" title="Screen Shot 2022-02-11 at 9.45.38 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c9864da484089a5f998c6c0ff9dc29e0282b0eff_2_565x500.jpeg" alt="Screen Shot 2022-02-11 at 9.45.38 AM" data-base62-sha1="sKLIkAWTiMBbsdwUkyWPZcV5899" width="565" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c9864da484089a5f998c6c0ff9dc29e0282b0eff_2_565x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c9864da484089a5f998c6c0ff9dc29e0282b0eff_2_847x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c9864da484089a5f998c6c0ff9dc29e0282b0eff_2_1130x1000.jpeg 2x" data-dominant-color="3C2B29"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2022-02-11 at 9.45.38 AM</span><span class="informations">1364×1206 150 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thank you,<br>
Hoda</p>

---

## Post #2 by @lassoan (2022-02-11 15:58 UTC)

<p>Could you share the files (upload the files to dropbox, onedrive, google drive, etc. and post the link) so that we can have a look?</p>

---

## Post #3 by @HodaGH (2022-02-11 16:58 UTC)

<p>here you go <a href="https://drive.google.com/file/d/1KPvXHoVtLgjGGCIGDfTRnVDIneYlxlmB/view?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">vasculature.nrrd - Google Drive</a></p>

---

## Post #4 by @lassoan (2022-02-11 19:27 UTC)

<p>Thank you, in this reconstructed file there are indeed two dark regions. Could you please upload the input files (before reconstruction) so that we can see why the gaps are there?</p>

---

## Post #5 by @HodaGH (2022-02-13 04:13 UTC)

<p>Thank you I see them now. I’ll ask if I can have them but is it possible to have a connected segmentation with these missing slides?<br>
I followed the vesselness instructions, created a seed fiducial then preview and start. then used thresholding in segment editor (also adjusted window level in the volume module )  but the three major vessels got segmented like this<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3d30c4c4cbf1a8c2c48c2f38628eae70b4ff3049.png" data-download-href="/uploads/short-url/8JjBWwUw0HIcRMWDFb7RwSZiMat.png?dl=1" title="Screen Shot 2022-02-12 at 11.02.25 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3d30c4c4cbf1a8c2c48c2f38628eae70b4ff3049_2_572x500.png" alt="Screen Shot 2022-02-12 at 11.02.25 PM" data-base62-sha1="8JjBWwUw0HIcRMWDFb7RwSZiMat" width="572" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3d30c4c4cbf1a8c2c48c2f38628eae70b4ff3049_2_572x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3d30c4c4cbf1a8c2c48c2f38628eae70b4ff3049_2_858x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3d30c4c4cbf1a8c2c48c2f38628eae70b4ff3049_2_1144x1000.png 2x" data-dominant-color="30323A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2022-02-12 at 11.02.25 PM</span><span class="informations">1172×1024 30.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
how can I improve?</p>

---

## Post #6 by @lassoan (2022-03-13 05:00 UTC)

<p>This looks quite good. You can remove the noise using “Islands” effect and may further improve results using “Smoothing” effect.</p>
<p>You can also try using “Grow from seeds”, “Local threshold”, and “Fast marching” effects (in SegmentEditorExtraEffects extension) instead of simple “Threshold” effect for higher quality segmentation.</p>

---
