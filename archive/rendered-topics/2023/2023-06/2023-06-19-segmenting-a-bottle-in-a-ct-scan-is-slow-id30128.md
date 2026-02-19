---
topic_id: 30128
title: "Segmenting A Bottle In A Ct Scan Is Slow"
date: 2023-06-19
url: https://discourse.slicer.org/t/30128
---

# Segmenting a bottle in a CT scan is slow

**Topic ID**: 30128
**Date**: 2023-06-19
**URL**: https://discourse.slicer.org/t/segmenting-a-bottle-in-a-ct-scan-is-slow/30128

---

## Post #1 by @Raha_Sep (2023-06-19 19:01 UTC)

<p>Hello,<br>
I would like to segment a bottle geometry from the DICOM file and save it as a vtk file. I started with “Segment Editor” and “Crop Volume” but the 3D slicer works super slow. Can you please help me to find the best way/modules for this purpose?<br>
Many thanks</p>
<p><em>(download link removed on request of the original poster)</em></p>

---

## Post #2 by @lassoan (2023-06-19 19:12 UTC)

<p>The image size is 512 x 512 x 692, so it is not very large. If you have something like 4GB free RAM then all operations should be quite fast. On my 3-year-old computer (8th-gen Intel Core i7, 32GB RAM) segmentation takes a couple of seconds in Segment Editor module.</p>
<p>Please provide detailed description of the steps you perform (include every click you make) and how long they take.</p>

---

## Post #3 by @Raha_Sep (2023-06-20 13:58 UTC)

<p>Hi Lassoan,<br>
Thank you for your prompt respond.<br>
I’ve tried to clean up my system and I believe it works faster now (3D Slicer 5.0.3). However, I like to describe the steps I did:</p>
<ul>
<li>Volumes: click on “Center Volume”/magnifying all views</li>
<li>Volume Rendering: changing the ROI/ click on “Display ROI”</li>
<li>Crop Volume: click on “Apply”</li>
<li>Segment Editor: “Add”/ on segment_1 I tring to segment the object using “Paint”/“Level Tracing”</li>
<li>click on “Show 3D”</li>
<li>since I made mistaks and the bottle should be hollow,  here I clicked on “Fill Between Slices” first that took time to act.</li>
<li>Then I clicked on “Erase” but didn’t work.</li>
<li>I tried to use undo but nothings can change anymore.</li>
</ul>
<p>Thanks in adnavce!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee67ef72632bc5eac38714301a6e289e64f81efb.jpeg" data-download-href="/uploads/short-url/y12jJWB52bfYzmQfmSQOuyznvjJ.jpeg?dl=1" title="0" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee67ef72632bc5eac38714301a6e289e64f81efb_2_690x398.jpeg" alt="0" data-base62-sha1="y12jJWB52bfYzmQfmSQOuyznvjJ" width="690" height="398" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee67ef72632bc5eac38714301a6e289e64f81efb_2_690x398.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee67ef72632bc5eac38714301a6e289e64f81efb_2_1035x597.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee67ef72632bc5eac38714301a6e289e64f81efb_2_1380x796.jpeg 2x" data-dominant-color="9C9CAC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">0</span><span class="informations">1909×1102 259 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/03fd7706b7eefafbe30c82a3540eaa164aa0762c.jpeg" data-download-href="/uploads/short-url/zitFyRX0kmwtHYYC8PK35o60Ik.jpeg?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/03fd7706b7eefafbe30c82a3540eaa164aa0762c_2_690x374.jpeg" alt="1" data-base62-sha1="zitFyRX0kmwtHYYC8PK35o60Ik" width="690" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/03fd7706b7eefafbe30c82a3540eaa164aa0762c_2_690x374.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/03fd7706b7eefafbe30c82a3540eaa164aa0762c_2_1035x561.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/03fd7706b7eefafbe30c82a3540eaa164aa0762c_2_1380x748.jpeg 2x" data-dominant-color="8F8FA2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1920×1043 112 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/667280d9d19c8797397a2fb1ef7bd31a8a5798cd.jpeg" data-download-href="/uploads/short-url/eCi1v7zlqYbY2TRkIwjACsjMqfj.jpeg?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/667280d9d19c8797397a2fb1ef7bd31a8a5798cd_2_690x375.jpeg" alt="2" data-base62-sha1="eCi1v7zlqYbY2TRkIwjACsjMqfj" width="690" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/667280d9d19c8797397a2fb1ef7bd31a8a5798cd_2_690x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/667280d9d19c8797397a2fb1ef7bd31a8a5798cd_2_1035x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/667280d9d19c8797397a2fb1ef7bd31a8a5798cd_2_1380x750.jpeg 2x" data-dominant-color="9393A6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">1920×1044 111 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d2ec17d67d77773238b39c7ae21f816b22fd201.jpeg" data-download-href="/uploads/short-url/6rHEVeTHstQT4Uo3ADEudzUXHMJ.jpeg?dl=1" title="3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d2ec17d67d77773238b39c7ae21f816b22fd201_2_690x374.jpeg" alt="3" data-base62-sha1="6rHEVeTHstQT4Uo3ADEudzUXHMJ" width="690" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d2ec17d67d77773238b39c7ae21f816b22fd201_2_690x374.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d2ec17d67d77773238b39c7ae21f816b22fd201_2_1035x561.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d2ec17d67d77773238b39c7ae21f816b22fd201_2_1380x748.jpeg 2x" data-dominant-color="8A8E9B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3</span><span class="informations">1920×1043 108 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2023-06-20 15:16 UTC)

<p>Comments on the performed steps:</p>
<ul>
<li>Volumes: click on “Center Volume”/magnifying all views → OK</li>
<li>Volume Rendering: changing the ROI/ click on “Display ROI” → do not use volume rendering, because it will occlude your segmentation; if you want to show volume rendering to get an idea of what is in the image, make sure you hide the volume rendering before you proceed with the next steps</li>
<li>Crop Volume: click on “Apply” → no need for cropping the volume; it is small enough that you should not run out ot memory if you have at least 8GB RAM in your computer</li>
<li>Segment Editor: “Add”/ on segment_1 I tring to segment the object using “Paint”/“Level Tracing” → it is easier to use Threshold effect to segment the bottle in 3D in a few seconds</li>
<li>click on “Show 3D” → OK</li>
<li>since I made mistaks and the bottle should be hollow, here I clicked on “Fill Between Slices” first that took time to act. → no need to use “Fill between slices” (Threshold effect is sufficient)</li>
<li>Then I clicked on “Erase” but didn’t work. → no need to use Erase</li>
<li>I tried to use undo but nothings can change anymore. → no need for Undo</li>
</ul>

---

## Post #5 by @Raha_Sep (2023-06-20 16:23 UTC)

<p>sounds perfect… the bottle has been segmented in a few seconds as you said byThreshold effect.<br>
I appreciate your support.</p>

---

## Post #6 by @lassoan (2023-09-08 13:03 UTC)

<p>A post was split to a new topic: <a href="/t/segmenting-3d-printed-heartseg/31617">Segmenting 3D printed heartseg</a></p>

---
