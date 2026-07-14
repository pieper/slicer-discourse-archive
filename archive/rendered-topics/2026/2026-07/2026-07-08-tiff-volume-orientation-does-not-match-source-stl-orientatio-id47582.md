---
topic_id: 47582
title: "TIFF volume orientation does not match source STL orientation"
date: 2026-07-08
url: https://discourse.slicer.org/t/47582
last_bumped: 2026-07-13T22:05:40.470Z
---

# TIFF volume orientation does not match source STL orientation

**Topic ID**: 47582
**Date**: 2026-07-08
**URL**: https://discourse.slicer.org/t/tiff-volume-orientation-does-not-match-source-stl-orientation/47582

---

## Post #1 by @tbugajski (2026-07-08 21:40 UTC)

<p>Hi SAM team,</p>
<p>We have been successfully using SAM to create partial volumes from CT segmentations, track these volumes, and apply the resulting transformations to AUT models in MATLAB to visualize motion.</p>
<p>We are now trying to repeat the same workflow using STL implant models instead of CT segmentations. Our workflow in 3D Slicer (version 5.10.0) is:</p>
<ol>
<li>Load the implant STL model into 3D Slicer.</li>
<li>Convert the model to a segmentation node.</li>
<li>Export the segmentation node as a binary labelmap volume.</li>
<li>In the SAM pre-processing module, set the <strong>Volume Node</strong> to the binary labelmap and the <strong>Segmentation Node</strong> to the STL-derived segmentation.</li>
</ol>
<p>The AUT models, volumes, and transforms are exported successfully. However, after tracking the generated TIFF volumes, applying the resulting transformation matrices to the AUT models produces an incorrect implant orientation.</p>
<p>While investigating, we noticed that the exported TIFF volumes appear to have a different orientation from the original STL model (specifically, a 180° rotation about the Y-axis). In contrast, the TIFF volumes generated from our CT segmentations retain the orientation of the source CT data. The images below show the STL (left) and CT (right) derived models and their associated TIFF volumes from the pre-processing module. Note: the TIFF volumes have been scaled back to match the same dimensions as the models.</p>
<div class="d-image-grid">
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/72d59b1e3a8902d80ace2fe406a6e5cf32535ae8.jpeg" data-download-href="/uploads/short-url/gnS4YnZYEYixHyYnkCjMB7bnEF2.jpeg?dl=1" title="STL Model" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/72d59b1e3a8902d80ace2fe406a6e5cf32535ae8.jpeg" alt="STL Model" data-base62-sha1="gnS4YnZYEYixHyYnkCjMB7bnEF2" width="420" height="485"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">STL Model</span><span class="informations">420×485 30.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5ad5b7d297d9cbd287a030f8c726834dfca735d3.jpeg" data-download-href="/uploads/short-url/cXyRojZvLg2LeuWEr4X98Oo9bpx.jpeg?dl=1" title="CT-derived bone model" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5ad5b7d297d9cbd287a030f8c726834dfca735d3.jpeg" alt="CT-derived bone model" data-base62-sha1="cXyRojZvLg2LeuWEr4X98Oo9bpx" width="512" height="478"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">CT-derived bone model</span><span class="informations">512×478 31.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</div>
<p>Could this orientation mismatch be responsible for the incorrect tracking results? If so, is there a recommended workflow for using STL models with SAM that preserves the correct orientation, or an alternative approach that would avoid this issue?</p>
<p>Any guidance would be greatly appreciated.</p>
<p>Thank you,</p>
<p>Tomasz</p>

---

## Post #2 by @John_Holtgrewe (2026-07-13 14:10 UTC)

<p>Hi Tomasz,</p>
<p>Thanks for reaching out. I do think that the orientation mismatch may be responsible for the incorrect tracking results. We have run into this before, where there was a difference in orientation between .stl bone models and the exported tiffs. In our case the tiff volume was flipped along the y and z axes relative to the .stl models. When generating the configuration file you can set a “Volume Flip,” and this can also be manually changed in the .cfg file. I would give this a try and retrack the file. Let me know if this resolves the issue.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc251a6758a51a1aa27a891aa0861b7522df543d.png" data-download-href="/uploads/short-url/zYzOzphsBHCbtOGPwIY0zfLgHlH.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc251a6758a51a1aa27a891aa0861b7522df543d.png" alt="image" data-base62-sha1="zYzOzphsBHCbtOGPwIY0zfLgHlH" width="607" height="110"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">607×110 3.35 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1196cf5890f6658adca6635ecf5a24e5dbd7cf3.png" data-download-href="/uploads/short-url/tPMgssbdyPh9tVRo9aY6iIIbklB.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1196cf5890f6658adca6635ecf5a24e5dbd7cf3.png" alt="image" data-base62-sha1="tPMgssbdyPh9tVRo9aY6iIIbklB" width="315" height="156"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">315×156 2.89 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @tbugajski (2026-07-13 16:16 UTC)

<p>Hi John,</p>
<p>Thanks for the reply.</p>
<p>I failed to mention this in my previous post, but I had initially tried a [1 0 1] flip since the TIFF seemed to be flipped about the Y-axis, but I had no success. I tried your suggestion of a [0 1 1] flip but the tracking is still off.</p>
<p>After further investigation, I managed to create a transform in Slicer that flips the TIFF to match the orientation of the STL. My initial statement that the TIFF is flipped about the Y-axis was incorrect, and the TIFF model is actually flipped about the Z-axis, requiring a [1 1 0] flip.</p>
<p>I retracked the first frame with this flip, and it seems the AUT models are in the correct orientation now, but still not properly translated. I have tried to apply some of the transforms the partial volume generator provides, but I have had no success there either.</p>
<div class="d-image-grid">
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8e790b9c6602760afa11e8c0f6283322c1146127.png" data-download-href="/uploads/short-url/kkn8DoCdZGGLYUEzJOeUxHhB8Cb.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8e790b9c6602760afa11e8c0f6283322c1146127.png" alt="image" data-base62-sha1="kkn8DoCdZGGLYUEzJOeUxHhB8Cb" width="519" height="365"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">519×365 38.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/92c37f28560dbde80741d4c02ba9af731888d7f8.png" data-download-href="/uploads/short-url/kWkyKnJmVRo663zXDYYQj76EQpq.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/92c37f28560dbde80741d4c02ba9af731888d7f8.png" alt="image" data-base62-sha1="kWkyKnJmVRo663zXDYYQj76EQpq" width="690" height="465" data-dominant-color="333333"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">874×589 32.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</div>

---

## Post #4 by @tbugajski (2026-07-13 20:45 UTC)

<p>Hi again John,</p>
<p>I wanted to provide some more information for you to help us pinpoint the issue.</p>
<p>In Slicer, I uploaded the AUT model and the associated TIFF volume. After applying the PVOL2AUT transform, the TIFF and AUT model do not align (I can confirm this transform works with CT model datasets).</p>
<p>The image of the TIFF in AUT space is below, and you can see that it is still a reflection of the AUT model. Applying a 180-degree rotation about the Z-axis (which I believe would be a [1 1 0] flip in the cfg file) would get the TIFF in the correct orientation. However, I would still need to translate the TIFF along the Y-axis by some arbitrary value of ~-85 mm? Not sure where this 85 would come from.</p>
<p>I tried to apply this transform to the AUT models in MATLAB, and then apply the tracking, but still no success. Perhaps I am thinking of these transformations incorrectly.</p>
<p>I appreciate the help thus far.</p>
<p>UPDATE: After posting this, I quickly swapped the -85 mm translation to be positive. The models seem to align perfectly now. However, I am still not sure where this 85 mm originates from. I am trying to check the volume dimensions, transforms, etc. but this value is nowhere to be found.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/94d4359dba4ea26f80a8adcc7ed9aaf7b4285dd0.jpeg" data-download-href="/uploads/short-url/leBjYJjuh974LDeoFiYDfm5i7mw.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/94d4359dba4ea26f80a8adcc7ed9aaf7b4285dd0_2_690x399.jpeg" alt="image" data-base62-sha1="leBjYJjuh974LDeoFiYDfm5i7mw" width="690" height="399" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/94d4359dba4ea26f80a8adcc7ed9aaf7b4285dd0_2_690x399.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/94d4359dba4ea26f80a8adcc7ed9aaf7b4285dd0.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/94d4359dba4ea26f80a8adcc7ed9aaf7b4285dd0.jpeg 2x" data-dominant-color="88869F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">798×462 59 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @John_Holtgrewe (2026-07-13 20:49 UTC)

<p>We have not used SAM to process and track implants before, so my experience here is limited. I haven’t run into this issue before with our human data. We did just collect some implant data, so I will try to track it and see if we have a similar issue.</p>

---

## Post #6 by @tbugajski (2026-07-13 20:52 UTC)

<p>Sounds good, thanks. I did provide an update in my last post in which I solved the issue. However, my solution required me to manually translate the model 85 mm until it matched closely. So, to acquire a more accurate solution is still required. I will keep looking into this and provide the solution if I find it.</p>

---

## Post #7 by @tbugajski (2026-07-13 22:05 UTC)

<p>Good news: I have found the solution with my STL models in case you (or anyone else) run into the same issue. Briefly, the PVOL2AUTO transform that was exported did not compensate for the additional Z-axis rotation that needed to occur.</p>
<p>The original PVOL2AUTO transform provided a 180-degree rotation about the X-axis and an additional translation about the Y-axis of -42.79 mm:</p>
<p>PVOL2AUT =</p>
<p>1	0	0	0<br>
0	-1	0	-42.79<br>
0	0	-1	0<br>
0	0	0	1</p>
<p>However, this transformation failed to account for the additional Z-axis rotation and translation about the Y-axis of about -85 mm (which I realized is actually just double the original Y-axis translation in PVOL2AUT):</p>
<p>Tz =</p>
<p>-1	0	0	0<br>
0	-1	0	-42.79*2<br>
0	0	1	0<br>
0	0	0	1</p>
<p>By combining the two transforms, you essentially form a rotation matrix representing a 180-degree rotation about the Y-axis with a Y-axis translation of the original magnitude:</p>
<p>Ty =</p>
<p>-1	0	0	0<br>
0	1	0	-42.79<br>
0	0	-1	0<br>
0	0	0	1</p>
<p>Therefore, in MATLAB I simply applied Tz to the AUT models to ensure that they are in the same space as the TIFF when imported into SAM. The tracking is then bringing the new models into the correct position.</p>

---
