# Slicer.exe file shuts down when setting the marker

**Topic ID**: 3931
**Date**: 2018-08-28
**URL**: https://discourse.slicer.org/t/slicer-exe-file-shuts-down-when-setting-the-marker/3931

---

## Post #1 by @kamrul079 (2018-08-28 19:22 UTC)

<p>I had built a module for tracking purpose. it successfully calibrate camera. But when I set the marker setting for the probe tracking, suddenly slicer stops and shuts down with the following error as shown in the image.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e268a337c7651b55765bbd4b6ba4296238d53c4.png" data-download-href="/uploads/short-url/b9lOsMpdzwCVEDYSb538YjiQNZq.png?dl=1" title="errors" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4e268a337c7651b55765bbd4b6ba4296238d53c4_2_690x401.png" alt="errors" data-base62-sha1="b9lOsMpdzwCVEDYSb538YjiQNZq" width="690" height="401" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4e268a337c7651b55765bbd4b6ba4296238d53c4_2_690x401.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4e268a337c7651b55765bbd4b6ba4296238d53c4_2_1035x601.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4e268a337c7651b55765bbd4b6ba4296238d53c4_2_1380x802.png 2x" data-dominant-color="C8C8CC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">errors</span><span class="informations">1923×1120 98.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @cpinter (2018-08-28 19:34 UTC)

<p>Your module probably has a bug that makes Slicer crash. If you included logging statements in your code then looking at the log could help (About / Report a problem), but the proper course of action would be debugging: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Debugging">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Debugging</a></p>

---

## Post #3 by @kamrul079 (2018-08-28 21:16 UTC)

<p>Can you suggest me a “videotracking” module for slicer?</p>

---

## Post #4 by @lassoan (2018-08-28 21:47 UTC)

<p>What do you mean by “videotracking”? Position tracking of 2D barcodes is available through Plus toolkit.</p>

---

## Post #5 by @kamrul079 (2018-08-28 21:48 UTC)

<p>Webcam based tracking of phantom for augmented reality application</p>

---

## Post #6 by @lassoan (2018-08-28 22:02 UTC)

<p>Plus toolkit can do such tracking - see <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/DeviceOpticalMarkerTracker.html">OpticalMarkerTracker device documentation</a> for details.</p>

---
