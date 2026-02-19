---
topic_id: 40086
title: "Registration Of Anisotropic Whole Body Cts On Isotropic Femu"
date: 2024-11-09
url: https://discourse.slicer.org/t/40086
---

# Registration of anisotropic whole-body CTs on isotropic femur CTs

**Topic ID**: 40086
**Date**: 2024-11-09
**URL**: https://discourse.slicer.org/t/registration-of-anisotropic-whole-body-cts-on-isotropic-femur-cts/40086

---

## Post #1 by @nikkos (2024-11-09 04:23 UTC)

<p>The following data are available:</p>
<ul>
<li>Low-resolution, anisotropic whole-body CTs (1 x 1 x 0.7 mm)</li>
<li>High-resolution, isotropic CTs of the femur (0.08 x 0.08 x 0.08 mm)</li>
</ul>
<p>We want to register the whole-body CT to the femur CT and crop the volume of interest from the whole-body CT. The result should be the same volume with the same isotropic grid (0.08 x 0.08 x 0.08 mm) in low and high res (related to the content) without losing much information through processing.<br>
The question is how we should ideally carry out the <strong>process steps</strong> (registration, cropping) and which <strong>settings</strong> (including resampling, interpolation, and others) are important in order to <strong>minimize the loss of information.</strong></p>
<p>Our current process is as follows:</p>
<ol>
<li>Center align both volumes (and harden the transformation)</li>
<li>Rough alignment of the volumes (Create new linear transform → use translation sliders and transformation matrix to move/flip CT and overlay them manually → harden transform)</li>
<li>Registration (General Registration (BRAINS) → Fixed Volume: High Res CT; Moving Volume: Low Res CT → Create new linear transform Rigid (6 DOF) → Apply)</li>
<li>Crop (Select ROI of High Res CT → Output volume: Create new volume; Interpolator: B-spline → Fit to volume → Apply on low res CT)</li>
</ol>

---

## Post #2 by @lassoan (2024-11-10 14:25 UTC)

<aside class="quote no-group" data-username="nikkos" data-post="1" data-topic="40086">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/f0a364/48.png" class="avatar"> nikkos:</div>
<blockquote>
<p>Center align both volumes (and harden the transformation)</p>
</blockquote>
</aside>
<p>Since the region that the two images cover are very different, centering will provide very bad results, so I would recommend skipping this step.</p>
<aside class="quote no-group" data-username="nikkos" data-post="1" data-topic="40086">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/f0a364/48.png" class="avatar"> nikkos:</div>
<blockquote>
<p>Rough alignment of the volumes (Create new linear transform → use translation sliders and transformation matrix to move/flip CT and overlay them manually → harden transform)</p>
</blockquote>
</aside>
<p>Yes, you can do the initial alignment fully manually. Instead of the sliders, you may find <a href="https://discourse.slicer.org/t/new-feature-interactive-transformation-adjustable-center-of-rotation/36974">interactive transform widgets</a> much more convenient to use.</p>
<p>For even better and faster results, you can use Fiducial Registration Wizard module (in SlicerIGT extension). You can place 3 corresponding landmarks on volume-rendered images in 1-2 minutes, which should give you a registration with less than 5mm error.</p>
<aside class="quote no-group" data-username="nikkos" data-post="1" data-topic="40086">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/f0a364/48.png" class="avatar"> nikkos:</div>
<blockquote>
<p>Registration (General Registration (BRAINS)</p>
</blockquote>
</aside>
<p>Before this, crop both images to approximately the common region.</p>
<p>Instead of BRAINS, I would recommend to try Elastix or ANTs, which are typically much more robust (you get good results without having to tune any parameters).</p>
<aside class="quote no-group" data-username="nikkos" data-post="1" data-topic="40086">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/f0a364/48.png" class="avatar"> nikkos:</div>
<blockquote>
<p>Crop (Select ROI of High Res CT → Output volume: Create new volume; Interpolator: B-spline → Fit to volume → Apply on low res CT)</p>
</blockquote>
</aside>
<p>I’m not sure what your end goal is. Just cropping an image does not sound very useful. If you want to stitch the volumes then you can use the <a href="https://github.com/PerkLab/SlicerSandbox?tab=readme-ov-file#stitch-volumes">Stitch Volumes module</a> (in Sandbox extension).</p>

---

## Post #3 by @nikkos (2024-11-14 15:27 UTC)

<p>Thank you very much for the quick reply.</p>
<p>The first two steps of our pipeline are basically there to place the CTs roughly on top of each other and thus prepare them for registration without any further crop. This step is necessary because the low-resolution CT of a patient shows the whole body and the high-resolution CT only shows a section of an anatomy (femur).</p>
<p>The registration using BRAINS works well so far (both volumes are visually perfectly registered to each other). However, we are unsure whether we are already losing information from the low-resolution CT (moving volume) in this step and how this could possibly be minimised.</p>
<p>If the two volumes are perfectly aligned with each other, we still have to select the same section in the mm space. We therefore crop the low-resolution CT to the ROI of the high-resolution CT. Here we are also not sure whether we lose information through cropping and the associated interpolation/resampling operation.</p>
<p>The final goal should be two volumes (high res and low res) which show the same anatomy and have an identical grid (isotropic spacing) and associated cropping.</p>
<p>Best regards</p>

---

## Post #4 by @nikkos (2024-12-09 15:49 UTC)

<p>Hi,</p>
<p>I wanted to let you know that I have now built my own slicer module that works very well. Thanks again for your help.</p>
<p>Best regards<br>
Niklas</p>

---

## Post #5 by @muratmaga (2024-12-09 17:08 UTC)

<p>That’s great to here. If possible, please share it (e.g., like gist) so that others on the forum can benefit from it as well…</p>

---

## Post #6 by @nikkos (2024-12-11 16:58 UTC)

<p>Hi,</p>
<p>I’m happy to do that, but I still have to rework the code a bit and restructure the GUI so that it can be used by everyone. I’ll get to work on it as soon as I have time.</p>

---
