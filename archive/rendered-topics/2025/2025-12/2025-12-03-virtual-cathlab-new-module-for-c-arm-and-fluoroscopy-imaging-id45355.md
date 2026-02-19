---
topic_id: 45355
title: "Virtual Cathlab New Module For C Arm And Fluoroscopy Imaging"
date: 2025-12-03
url: https://discourse.slicer.org/t/45355
---

# Virtual CathLab: new module for C-arm and fluoroscopy imaging simulation

**Topic ID**: 45355
**Date**: 2025-12-03
**URL**: https://discourse.slicer.org/t/virtual-cathlab-new-module-for-c-arm-and-fluoroscopy-imaging-simulation/45355

---

## Post #1 by @lassoan (2025-12-03 16:52 UTC)

<p>Virtual Cath Lab module has been recently added to <a href="https://slicerheart.org/">SlicerHeart extension</a>. This module simulates monoplane and biplane C-arm systems: provides 3D model of the C-arm, table, patient and generates simulated fluoroscopy images. Images can be either static (generated from 3D CT) or dynamic (generated from 4DCT). The module can also display cardiac devices (stents, occluders, clips, etc. provided by the Cardiac Device Simulator module) and virtual contrast filling (from image segmentation).</p>
<p>The module was developed for cardiac and vascular procedures, but it is well suited for simulation of any fluoroscopy guided procedures.</p>
<div class="youtube-onebox lazy-video-container" data-video-id="P8p0kaAKXuE" data-video-title="Virtual Cath Lab in 3D Slicer" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=P8p0kaAKXuE" target="_blank" class="video-thumbnail" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/P8p0kaAKXuE/maxresdefault.jpg" title="Virtual Cath Lab in 3D Slicer" width="690" height="388">
  </a>
</div>

<p>More details are provided in this paper:</p>
<p>Yuval Barak-Corren, Matthew Daemer, Mudit Gupta, Kyle Sunderland, Andras Lasso, Analise Sulentic, Trevor R. Williams, Silvani Amin, Alana Cianciulli, Michael L. O’Byrne, Matthew A. Jolley, <strong>Virtual Cath Lab: Versatile Open-Source Simulator for Education and Procedural Planning in Congenital Heart Interventions</strong>, Journal of the Society for Cardiovascular Angiography &amp; Interventions, Volume 4, Issue 11, 2025, 103937, <a href="https://doi.org/10.1016/j.jscai.2025.103937" class="inline-onebox">Redirecting</a></p>

---

## Post #2 by @chir.set (2025-12-06 15:12 UTC)

<p>I considered the VirtualCathLab with much interest.</p>
<p>It targets the cardiac cath lab by design, but may be equally helpful for pre-operative assessment in some vascular interventions too.</p>
<p>However, the default position of the C-arm in the vascular context is not always at the head of the patient (rarely actually), it is rather perpendicular to the table. The L-arm angle slider can do that but the orientation of the DRR is then rotated accordingly.</p>
<p>Would it be possible to optionally have a default position of the C-arm perpendicular to the table, on its right or on its left, with an upright DRR?</p>
<p>Thank you.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/85b0767d2fd00d0f086adc94f3752b2f4618d7de.jpeg" data-download-href="/uploads/short-url/j4FzyrGX6dHK3SduzOLJaScKU5U.jpeg?dl=1" title="CathLabSimulatorDefaultCArmPosition" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/85b0767d2fd00d0f086adc94f3752b2f4618d7de_2_690x327.jpeg" alt="CathLabSimulatorDefaultCArmPosition" data-base62-sha1="j4FzyrGX6dHK3SduzOLJaScKU5U" width="690" height="327" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/85b0767d2fd00d0f086adc94f3752b2f4618d7de_2_690x327.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/85b0767d2fd00d0f086adc94f3752b2f4618d7de_2_1035x490.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/85b0767d2fd00d0f086adc94f3752b2f4618d7de_2_1380x654.jpeg 2x" data-dominant-color="5F5F5F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">CathLabSimulatorDefaultCArmPosition</span><span class="informations">1495×710 93.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/01f561f26998bdfeaf3ef79e6460df7715306f57.jpeg" data-download-href="/uploads/short-url/hkcQM0kyalIjlAutIvhV0gSR5Z.jpeg?dl=1" title="CathLabSimulatorAlternateDefaultCArmPosition" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01f561f26998bdfeaf3ef79e6460df7715306f57_2_690x327.jpeg" alt="CathLabSimulatorAlternateDefaultCArmPosition" data-base62-sha1="hkcQM0kyalIjlAutIvhV0gSR5Z" width="690" height="327" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01f561f26998bdfeaf3ef79e6460df7715306f57_2_690x327.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01f561f26998bdfeaf3ef79e6460df7715306f57_2_1035x490.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01f561f26998bdfeaf3ef79e6460df7715306f57_2_1380x654.jpeg 2x" data-dominant-color="5A5959"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">CathLabSimulatorAlternateDefaultCArmPosition</span><span class="informations">1495×710 73.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @lassoan (2025-12-06 16:44 UTC)

<p>You are absolutely right. To get a monoplane model, we removed the ceiling-mounted C-arm of the biplane model, but of course you would not normally use it at that angle, and we haven’t implemented auto-rotate.</p>
<p>If you have a chance then feel free to add this feature (e.g., add a +/-90deg rotation to the <code>updateCameraPosition</code> method to keep the detector “view’s up” direction approximately aligned to “patient’s head” direction), but if you are not sure how to do it then I’ll try to get to it in the next few days.</p>

---

## Post #4 by @chir.set (2025-12-06 18:22 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="45355">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>feel free to add this feature</p>
</blockquote>
</aside>
<p>A few tries have not been convincing, I don’t really grab the logic of this module.</p>
<p>But the position of the C-arm in the module is not a fundamental issue because we can still determine angles as it is and map these relative to the table and the C-arm in the OR. If it implies too much work, you may drop the request. Thanks for having considered.</p>

---

## Post #5 by @lassoan (2025-12-07 14:42 UTC)

<p>I’ve updated the module with the followings:</p>
<ul>
<li>Added detector rotation angle (no auto-rotation is available, but the rotation can be easily manually adjusted on the GUI)</li>
<li>Default L arm angle is set the C-arm to be at the side of the table</li>
<li>Projection beam is displayed (to make it easier to see the field of view in 3D)</li>
<li>Detector size is configurable in the preset .csv files</li>
</ul>
<p>It would be great if you could test it and give feedback. If you have a few vascular systems that you want to add to the parameter sets (with SOD, detector size, default angles) then feel free to send a pull request with additional csv file entries.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/5825bd29f99a24c8ebfd978e916c74d52118f6c0.jpeg" data-download-href="/uploads/short-url/czMS6wQwvO9Y1BXsC9h3nPjbdAs.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/5825bd29f99a24c8ebfd978e916c74d52118f6c0_2_690x357.jpeg" alt="image" data-base62-sha1="czMS6wQwvO9Y1BXsC9h3nPjbdAs" width="690" height="357" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/5825bd29f99a24c8ebfd978e916c74d52118f6c0_2_690x357.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/5825bd29f99a24c8ebfd978e916c74d52118f6c0_2_1035x535.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/5825bd29f99a24c8ebfd978e916c74d52118f6c0_2_1380x714.jpeg 2x" data-dominant-color="57575F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1919×993 286 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @chir.set (2025-12-07 17:12 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="45355">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It would be great if you could test it and give feedback.</p>
</blockquote>
</aside>
<p>It is indeed much better and more realistic to OR situations. I’ll give more feedback<br>
later on cumulating experiences on more cases. Thank you very much.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d45c426c99d3472362bae04d29b7132193ade19.jpeg" data-download-href="/uploads/short-url/6suXuHECX67xJEKReh4XvRHb5W1.jpeg?dl=1" title="VirtualCathLabEasier" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d45c426c99d3472362bae04d29b7132193ade19_2_690x215.jpeg" alt="VirtualCathLabEasier" data-base62-sha1="6suXuHECX67xJEKReh4XvRHb5W1" width="690" height="215" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d45c426c99d3472362bae04d29b7132193ade19_2_690x215.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d45c426c99d3472362bae04d29b7132193ade19_2_1035x322.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d45c426c99d3472362bae04d29b7132193ade19_2_1380x430.jpeg 2x" data-dominant-color="595857"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">VirtualCathLabEasier</span><span class="informations">1920×600 164 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @lassoan (2025-12-07 18:12 UTC)

<p>Nice image! You show the vessel in the simulated fluoro image as a surface rendering now. You can try to use the “Virtual contrast filling” section to make the appearance more realistic (the module fills the CT image uniformly inside the segment/model with the density you specify).</p>

---

## Post #8 by @chir.set (2025-12-07 19:58 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="45355">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>fills the CT image uniformly</p>
</blockquote>
</aside>
<p>Yep, that purpose was what I did not understand yet.</p>

---

## Post #9 by @lassoan (2025-12-08 03:18 UTC)

<p>Virtual contrast filling can be useful to simulate stronger contrast filling (e.g., you have a CT with IV contrast injection and you want to simulate local contrast injection) or you want to add anything to the CT that was originally not there (e.g., a stent or device).</p>

---

## Post #10 by @chir.set (2025-12-08 15:03 UTC)

<p>Here is the procedural image with the C-arm oriented as simulated. I find it a faithful reproduction for a first try, and remain confident for subsequent ones.</p>
<p>Here it means less radio emission and less contrast medium injection.</p>
<p>This module should be viewed as a wonderful add-on to anyone working with a C-arm, beyond the cardio-vascular realm, orthopedists for example.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/60aea8e1be85b82122935da82eda0a185fc243a2.jpeg" data-download-href="/uploads/short-url/dNi2IuC7R1gjs3SQBhNUUVbsjzI.jpeg?dl=1" title="VirtualCathLabProcedural" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/60aea8e1be85b82122935da82eda0a185fc243a2_2_282x500.jpeg" alt="VirtualCathLabProcedural" data-base62-sha1="dNi2IuC7R1gjs3SQBhNUUVbsjzI" width="282" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/60aea8e1be85b82122935da82eda0a185fc243a2_2_282x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/60aea8e1be85b82122935da82eda0a185fc243a2.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/60aea8e1be85b82122935da82eda0a185fc243a2.jpeg 2x" data-dominant-color="A4A4A4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">VirtualCathLabProcedural</span><span class="informations">405×718 50.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
