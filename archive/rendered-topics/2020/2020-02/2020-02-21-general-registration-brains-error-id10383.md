---
topic_id: 10383
title: "General Registration Brains Error"
date: 2020-02-21
url: https://discourse.slicer.org/t/10383
---

# General Registration (BRAINS) error

**Topic ID**: 10383
**Date**: 2020-02-21
**URL**: https://discourse.slicer.org/t/general-registration-brains-error/10383

---

## Post #1 by @Saima (2020-02-21 06:58 UTC)

<p>Hi andras,<br>
I am trying to use bspline using general registration. I am getting following error. could you please help.</p>
<p>General Registration (BRAINS) standard error:</p>
<p>WARNING: In /work/Preview/Slicer-0-build/ITK/Modules/Numerics/Optimizersv4/src/itkLBFGSBOptimizerv4.cxx, line 113</p>
<p>LBFGSBOptimizerv4 (0x1545e90): LBFGSB optimizer does not support scaling. All scales are set to one.</p>

---

## Post #2 by @lassoan (2020-02-21 15:22 UTC)

<p>This is just a warning, you don’t need to worry about it. Is there any other problem? What are you trying to do? What do you expect to happen? What happens instead?</p>

---

## Post #3 by @Saima (2020-02-26 02:57 UTC)

<p>Hi Andras,<br>
I am using general registration (brains).<br>
When I use the grid size = 14, 10,12<br>
All settings are below in screen shot.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f6bc580eb0e36293b1a87f4a10cfa3dac12a5e9.png" data-download-href="/uploads/short-url/932YL9vBAExDZ5SDClGBRX92BPr.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3f6bc580eb0e36293b1a87f4a10cfa3dac12a5e9_2_498x500.png" alt="image" data-base62-sha1="932YL9vBAExDZ5SDClGBRX92BPr" width="498" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3f6bc580eb0e36293b1a87f4a10cfa3dac12a5e9_2_498x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f6bc580eb0e36293b1a87f4a10cfa3dac12a5e9.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f6bc580eb0e36293b1a87f4a10cfa3dac12a5e9.png 2x" data-dominant-color="EDF0F2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">614×616 63.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
which is default grid size, the application give me results without error. When I use the output of bspline from this grid size and apply it on preop MRI, It is not transformed as expected. The results of transform of bspline on preop should result in close results to intraop mri, but i am not getting it.</p>
<p>Second, if I am increasing or decreasing the grid size it results into error.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d7b4912752c09856b0c65ee3406bd729ed9ebba9.png" data-download-href="/uploads/short-url/uMdwbHx5EiY27iQDaMjFymvMPBT.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d7b4912752c09856b0c65ee3406bd729ed9ebba9_2_493x500.png" alt="image" data-base62-sha1="uMdwbHx5EiY27iQDaMjFymvMPBT" width="493" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d7b4912752c09856b0c65ee3406bd729ed9ebba9_2_493x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d7b4912752c09856b0c65ee3406bd729ed9ebba9.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d7b4912752c09856b0c65ee3406bd729ed9ebba9.png 2x" data-dominant-color="EEEFF1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">622×630 69 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
General Registration (BRAINS) standard error:</p>
<p>WARNING: In /work/Preview/Slicer-0-build/ITK/Modules/Numerics/Optimizersv4/src/itkLBFGSBOptimizerv4.cxx, line 113</p>
<p>LBFGSBOptimizerv4 (0x1545e90): LBFGSB optimizer does not support scaling. All scales are set to one.</p>
<p>And if I use this bspline it does not show me any transform at all.</p>
<p>Looking forward to your reply</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #4 by @lassoan (2020-02-26 04:03 UTC)

<p>Without any images and more informative error messages, it’s hard to tell what should be changed. Typically, “General registration (BRAINS)” module is a bit hard to use because you need to manually tune its parameters. You can find description of all parameters <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/BRAINSFit">here</a> and there are many examples in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Registration/RegistrationLibrary">Registration Case Library</a>.</p>
<p>I find “General registration (Elastix)” module (provided by SlicerElastix extension) much easier to use, as the default rigid and bspline deformable presets usually work well (no manual parameter tuning is needed).</p>

---

## Post #5 by @Saima (2020-02-26 06:29 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="10383">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>neral registration (Elastix)</p>
</blockquote>
</aside>
<p>Thank you Andras.<br>
I could not find the general registration (Elastix) in the registratio section. I am using nightly version 4.11.0 2019/09/17</p>

---

## Post #6 by @lassoan (2020-02-26 12:31 UTC)

<p>Use latest stable or preview release and install SlicerElastix extension.</p>

---
