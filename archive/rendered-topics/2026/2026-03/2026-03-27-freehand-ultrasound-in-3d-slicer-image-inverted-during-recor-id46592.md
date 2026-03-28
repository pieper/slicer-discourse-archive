---
topic_id: 46592
title: "Freehand Ultrasound In 3D Slicer Image Inverted During Recor"
date: 2026-03-27
url: https://discourse.slicer.org/t/46592
---

# Freehand ultrasound in 3D Slicer: image inverted during recording

**Topic ID**: 46592
**Date**: 2026-03-27
**URL**: https://discourse.slicer.org/t/freehand-ultrasound-in-3d-slicer-image-inverted-during-recording/46592

---

## Post #1 by @daandevlieger2-alt (2026-03-27 09:10 UTC)

<p>Hi everyone,</p>
<p>I’m using 3D Slicer (version 5.8.1) together with an OptiTrack V120 Trio and the PLUS/ArtUS setup for 3D freehand ultrasound.</p>
<p>I’m encountering an issue where, during acquisition, the ultrasound image is streamed upside down in Slicer. I tried correcting the orientation in the Reformat module, but every time I restart the recording, the image flips upside down again.</p>
<p>I also experimented with changing <code>PortUsImageOrientation="UN"</code> to <code>"UF"</code> in the acquisition XML file. While this corrected the image orientation visually, it negatively affected my calibration, resulting in multiple sweeps that were not well aligned.</p>
<p>During calibration, the image appears correctly oriented (skin surface superior) when using <code>PortUsImageOrientation="UN"</code> in the XML file. So both the calibratio and acquisition XML files have the same <code>PortUsImageOrientation</code> setting.</p>
<p>Does anyone know how to resolve this issue? It’s quite confusing to perform ultrasound acquisitions with the image upside down.</p>
<p>Thanks in advance!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/41e7ad604eb9305a7837c99b0c34efdbdf16417c.png" data-download-href="/uploads/short-url/9p1oUw8zjYKa5WTsRW9evyVcFSk.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/41e7ad604eb9305a7837c99b0c34efdbdf16417c_2_690x397.png" alt="image" data-base62-sha1="9p1oUw8zjYKa5WTsRW9evyVcFSk" width="690" height="397" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/41e7ad604eb9305a7837c99b0c34efdbdf16417c_2_690x397.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/41e7ad604eb9305a7837c99b0c34efdbdf16417c_2_1035x595.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/41e7ad604eb9305a7837c99b0c34efdbdf16417c_2_1380x794.png 2x" data-dominant-color="3C3C42"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1919×1105 294 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/88690ddd88a599a795b494709e42d6cf5a370a81.png" data-download-href="/uploads/short-url/jsK0PPFrBkBHvgc6ei5E87JO3NT.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/88690ddd88a599a795b494709e42d6cf5a370a81_2_690x397.png" alt="image" data-base62-sha1="jsK0PPFrBkBHvgc6ei5E87JO3NT" width="690" height="397" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/88690ddd88a599a795b494709e42d6cf5a370a81_2_690x397.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/88690ddd88a599a795b494709e42d6cf5a370a81_2_1035x595.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/88690ddd88a599a795b494709e42d6cf5a370a81_2_1380x794.png 2x" data-dominant-color="3D3C43"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1916×1104 307 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @Sunderlandkyl (2026-03-27 14:15 UTC)

<p>Try using the Volume Reslice Driver module in SlicerIGT.</p>

---

## Post #3 by @lassoan (2026-03-28 00:36 UTC)

<p>See more details and step-by-step instructions in <a href="https://www.slicerigt.org/wp/user-tutorials/" class="inline-onebox">User tutorials | SlicerIGT</a>.</p>

---
