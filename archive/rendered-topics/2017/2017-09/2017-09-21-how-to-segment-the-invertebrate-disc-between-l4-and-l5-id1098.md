---
topic_id: 1098
title: "How To Segment The Invertebrate Disc Between L4 And L5"
date: 2017-09-21
url: https://discourse.slicer.org/t/1098
---

# How to segment the invertebrate disc between L4 and L5?

**Topic ID**: 1098
**Date**: 2017-09-21
**URL**: https://discourse.slicer.org/t/how-to-segment-the-invertebrate-disc-between-l4-and-l5/1098

---

## Post #1 by @deepmech (2017-09-21 19:25 UTC)

<p>whether it is cartilage or meniscus ?<br>
i tried in cartilage.<br>
when we use volume rendering for bone we use CT-AAA2 format<br>
what i should use for  invertebrate disc.<br>
when we select the intensity/threshold for cartilage (or any material) in segmentation<br>
is any properties other than threshold also captured just as viscosity,semi-solid or stiffness?</p>

---

## Post #2 by @lassoan (2017-09-22 13:49 UTC)

<p>Using volume rendering, you may or may not be able to visualize a disc - depending on what imaging modality (CT/MRI) and imaging protocol you used.</p>
<p>If adjusting transfer functions in volume rendering does not give you good results or you need to quantify or 3D print the disc then you need to segment the volume using Segment editor (in latest nightly version of Slicer). Cartilage can often be segmented using “Grow from seeds effect” - or of course manually, using Paint or Draw effects.</p>

---

## Post #3 by @deepmech (2017-09-24 04:11 UTC)

<p>thank you sir<br>
but you didn’t tell whether it capture other properties or not</p>

---

## Post #4 by @deepmech (2017-09-24 04:20 UTC)

<p>good morning sir<br>
sometime when i used crop volume it does not crop it on axial,sagitial and coronal view,<br>
today it crooped but images are very small.<br>
i am attaching snapshot<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/720ca3379c0abaddd25cc2a25c6fa8738e7fb561.png" data-download-href="/uploads/short-url/ggVvsO5cql5Q3Xv0CVDiY6doEa5.png?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/720ca3379c0abaddd25cc2a25c6fa8738e7fb561_2_690x499.png" alt="Capture" data-base62-sha1="ggVvsO5cql5Q3Xv0CVDiY6doEa5" width="690" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/720ca3379c0abaddd25cc2a25c6fa8738e7fb561_2_690x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/720ca3379c0abaddd25cc2a25c6fa8738e7fb561.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/720ca3379c0abaddd25cc2a25c6fa8738e7fb561.png 2x" data-dominant-color="3C3B44"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">848×614 73.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>sometime when i restart the software it works and sometimes not.</p>

---

## Post #5 by @lassoan (2017-09-24 04:38 UTC)

<aside class="quote no-group" data-username="deepmech" data-post="4" data-topic="1098">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/e0b2c6/48.png" class="avatar"> deepmech:</div>
<blockquote>
<p>today it crooped but images are very small</p>
</blockquote>
</aside>
<p>Click <a href="http://slicer.readthedocs.io/en/latest/user_guide/user_interface.html">“Reset field of view” buttons</a> in the slice viewers to make the image fill the slice viewer (or right-click and drag up/down to zoom in/out).</p>
<p>Crop module will remove whatever is outside the cropping region of interest.</p>
<p>When you go to segmentation module, make sure you select the cropped volume as master volume. If another volume is selected already then delete the segmentation, create a new segmentation, and choose the cropped volume as master volume.</p>

---

## Post #6 by @lassoan (2017-09-24 04:44 UTC)

<aside class="quote no-group" data-username="deepmech" data-post="3" data-topic="1098">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/e0b2c6/48.png" class="avatar"> deepmech:</div>
<blockquote>
<p>but you didn’t tell whether it capture other properties or not</p>
</blockquote>
</aside>
<p>CT images capture radiographic density. Most often different structures have somewhat different radiographic density, but in general there is no direct mapping between radiographic density and mechanical properties. Most common approach is to segment structures and set mechanical properties to be uniform (or potentially somewhat modulated by the radiographic density) within.</p>

---

## Post #7 by @deepmech (2017-10-10 17:36 UTC)

<p>hello sir ,<br>
when i am using fast grow cut  segment, it is showing error.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/1357dca8a632f4bd527169d414793b7d8bc7cbf5.png" alt="Capture error" data-base62-sha1="2L7jxZzvoQh5mdoqF442B84Gwu1" width="380" height="102"></p>
<p>i noticed during first selection of region  it is same as threshold as second region in some part.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d29ff705e3d7ba473266abe9113d044b1bb4c06e.png" data-download-href="/uploads/short-url/u3gZvzo3ITQ5UOuWCZkc3wigSOq.png?dl=1" title="Capturevv" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d29ff705e3d7ba473266abe9113d044b1bb4c06e_2_690x349.png" alt="Capturevv" data-base62-sha1="u3gZvzo3ITQ5UOuWCZkc3wigSOq" width="690" height="349" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d29ff705e3d7ba473266abe9113d044b1bb4c06e_2_690x349.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d29ff705e3d7ba473266abe9113d044b1bb4c06e_2_1035x523.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d29ff705e3d7ba473266abe9113d044b1bb4c06e.png 2x" data-dominant-color="AFADA5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capturevv</span><span class="informations">1358×688 131 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>i get the intervertebrae disc by segment editor but i tried fast grow cut method.</p>

---

## Post #8 by @lassoan (2017-10-11 03:35 UTC)

<p>Use the latest nightly version of Slicer and the Segment Editor module (not the legacy Editor module).</p>

---

## Post #9 by @lassoan (2017-11-03 15:39 UTC)

<p>A post was split to a new topic: <a href="/t/crop-volume-using-ellipse-rectangle-or-freeform-shape/1363">Crop volume using ellipse, rectangle, or freeform shape</a></p>

---
