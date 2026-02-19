---
topic_id: 502
title: "Tractography Through Rois From Tms Dicom Data Anyone Experie"
date: 2017-06-14
url: https://discourse.slicer.org/t/502
---

# Tractography through ROIs from TMS-DICOM-Data - anyone experience?

**Topic ID**: 502
**Date**: 2017-06-14
**URL**: https://discourse.slicer.org/t/tractography-through-rois-from-tms-dicom-data-anyone-experience/502

---

## Post #1 by @LGG (2017-06-14 15:43 UTC)

<p>Hi everyone,</p>
<p>I would like to create ROIs out of DICOM-Data that has been acquired through TMS (with Slicer 4.6). The aim is to run tractography through these ROIs. I tried to do full brain tractography and use the TMS-Data as labelmaps, but so far I haven’t been able to produce a labelmap out of the TMS-Data. Does anyone have experience with that or an idea how to approach this? It would be a great help!</p>

---

## Post #2 by @ihnorton (2017-06-14 16:00 UTC)

<p>Hi Lioba,</p>
<p>Can you please describe in more detail the data, what you tried, and what the issue was? One or two screenshots might help. I have used TMS in the past, but it was a proprietary system and we only received lists of coordinates and amplitudes (not DICOM). If you receive a DICOM heatmap image of stimulation, for example, you will likely need to threshold it  (using one of the editor tools) to produce a binary labelmap which could then be used as an input ROI.</p>

---

## Post #3 by @ihnorton (2017-06-14 16:01 UTC)

<p>(also, if you send screenshots or share data, <strong>please make sure to crop any patient data!</strong>)</p>

---

## Post #4 by @LGG (2017-06-14 18:13 UTC)

<p>Hi Isaiah!</p>
<p>Thank you so much for that quick reply! Well my thought was to create a labelmap in the Editor, putting the TMS-points (its just several mapping-locations without any brain tissue underneath - I took a screenshot of it) as a Master Volume to create a labelmap of it. But that didn’t work (screenshot No. 2). I actually don’t really understand what the software does when it creates a merge label map. I actually want it to accept all the TMS-points as ROIs, or all of them together as one ROI (which seems to be more probable to implement).</p>
<p>I would be so glad if there’s a solution for that!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba038cdd4fcb37443d2a8b7e4781e8b87a9992b9.png" data-download-href="/uploads/short-url/qxypMECxlwXdSBDNWESSQ2oujJT.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba038cdd4fcb37443d2a8b7e4781e8b87a9992b9_2_690x361.png" alt="image" data-base62-sha1="qxypMECxlwXdSBDNWESSQ2oujJT" width="690" height="361" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba038cdd4fcb37443d2a8b7e4781e8b87a9992b9_2_690x361.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba038cdd4fcb37443d2a8b7e4781e8b87a9992b9_2_1035x541.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba038cdd4fcb37443d2a8b7e4781e8b87a9992b9_2_1380x722.png 2x" data-dominant-color="868697"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1666×872 85.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @ihnorton (2017-06-14 19:37 UTC)

<p>It looks like the threshold is too low. Move the mouse cursor over the dots, then look at the value in the “Data Probe” area in the bottom-left side of the window. Then set the threshold to only include that value – the dots should be highlighted as the threshold is changed. Here is a video demonstrating usage of the threshold tool:</p>
<div class="lazyYT" data-youtube-id="-IZV-rG9C7Q" data-youtube-title="3D Slicer: Threshold Effect and Robust Statistics Segmenter" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>

---
