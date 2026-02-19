---
topic_id: 15999
title: "Registration With Bspline Method Itkv4 Registration"
date: 2021-02-15
url: https://discourse.slicer.org/t/15999
---

# Registration with BSpline method, ITKv4 registration

**Topic ID**: 15999
**Date**: 2021-02-15
**URL**: https://discourse.slicer.org/t/registration-with-bspline-method-itkv4-registration/15999

---

## Post #1 by @hao (2021-02-15 16:10 UTC)

<p>Hi,<br>
I have a regestration problem with Bspline transform.<br>
I want to do the registration beween CT and MRI. I use the same precedure: manuel tranform for align the two series at the first time, Linear Transform for the second time and the BSpline transform for the thrid time.<br>
I have tried in 3 PC (win 7, win 10 et ubuntu 18), work perfectly. But the 4th PC (ubuntu 18, AMD 5700, 32G memory, Nvidia GTV 1660) always give the same errer (LBFGSB optimizer …). I have tried with 4.13.0 et 4.11 version, the same results.<br>
Could anyone give me some advise? thank you.</p>
<pre><code class="lang-plaintext">General Registration (BRAINS) standard error:

WARNING: In /work/Preview/Slicer-0-build/ITK/Modules/Numerics/Optimizersv4/src/itkLBFGSBOptimizerv4.cxx, line 99
LBFGSBOptimizerv4 (0x14ef8c0): LBFGSB optimizer does not support scaling. All scales are set to one.


General Registration (BRAINS) standard output:

Original Fixed image origin[-125, -102.2, -11.25, 0]
Read ITK transform from file: /tmp/Slicer-hao/BJIGG_vtkMRMLLinearTransformNodeF.h5
HACK: 0  AffineTransform
TransformTypes: BSpline(1 of 1).




=============================== ITKv4 Registration: Starting Transform Estimations for BSpline(1 of 1).===============================

Initialized BSpline transform is set to be an identity transform.
  - Number of parameters = 9945
-- WARNING: Only one in every 663 parameters is printed on screen.

LBFGSB optimizer is used for BSpline registration using following parameters set:
-----------------------------------------------------------------------------------
NOTICE: You can use commandline options to adjust these parameters to find a
         probable better compromise between running time and registration precision.
-----------------------------------------------------------------------------------
 - Cost Function Convergence Factor : 2e+13
 - Projected Gradient Tolerance     : 1e-05
 - Maximum Number of Corrections    : 25
 - Maximum Number of Evaluations    : 900
 - Maximum Number of Iterations     : 1500
</code></pre>
<p>Moving image is warped by initial transform, before it is passed to the BSpline registration.</p>
<p>*** Running bspline registration (meshSizeAtBaseLevel = [14, 10, 12]) ***</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/552759278935b062c11eb1afffe37149dfab7fa0.jpeg" data-download-href="/uploads/short-url/c9iT4pKlArWPEl9fs48OcIkzXgI.jpeg?dl=1" title="fusion_problem.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/552759278935b062c11eb1afffe37149dfab7fa0_2_690x386.jpeg" alt="fusion_problem.PNG" data-base62-sha1="c9iT4pKlArWPEl9fs48OcIkzXgI" width="690" height="386" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/552759278935b062c11eb1afffe37149dfab7fa0_2_690x386.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/552759278935b062c11eb1afffe37149dfab7fa0_2_1035x579.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/552759278935b062c11eb1afffe37149dfab7fa0_2_1380x772.jpeg 2x" data-dominant-color="8C8C94"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">fusion_problem.PNG</span><span class="informations">1846×1033 365 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-02-15 16:53 UTC)

<p>“General registration (BRAINS)” module requires experimentation with registration parameters (percentage of samples, minimum and maximum step length, and relaxation factor).</p>
<p>I would suggest to try <a href="https://github.com/lassoan/SlicerElastix">SlicerElastix extension</a>, because its default registration preset gives good results for all reasonable inputs. The only requirement is to crop the images to approximately the same anatomical region (e.g., if one image only contains the brain then crop the other image similarly).</p>

---

## Post #3 by @hao (2021-02-15 18:19 UTC)

<p>thanks, I will try it.</p>

---

## Post #4 by @hao (2021-02-15 18:37 UTC)

<p>It work perfectly with Elastix.<br>
otherwise, a little long but acceptable.</p>
<p>thanks Iassoan.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b7f2590ab44517df0d2b81739cf114e8ce0aa673.jpeg" data-download-href="/uploads/short-url/qfgBveQ7N6QcIy7zohJQNE4h9OX.jpeg?dl=1" title="fusion_problem02.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b7f2590ab44517df0d2b81739cf114e8ce0aa673_2_690x378.jpeg" alt="fusion_problem02.PNG" data-base62-sha1="qfgBveQ7N6QcIy7zohJQNE4h9OX" width="690" height="378" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b7f2590ab44517df0d2b81739cf114e8ce0aa673_2_690x378.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b7f2590ab44517df0d2b81739cf114e8ce0aa673_2_1035x567.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b7f2590ab44517df0d2b81739cf114e8ce0aa673_2_1380x756.jpeg 2x" data-dominant-color="75827D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">fusion_problem02.PNG</span><span class="informations">1852×1015 345 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @lassoan (2021-02-15 18:42 UTC)

<p>Great, thanks for the update!</p>
<aside class="quote no-group" data-username="hao" data-post="4" data-topic="15999">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/ea5d25/48.png" class="avatar"> hao:</div>
<blockquote>
<p>a little long but acceptable.</p>
</blockquote>
</aside>
<p>With tuning of registration parameters (cropping, resampling of inputs, good initialization, reduced number of samples, etc.) you should be able to get rigid registration in 10-20 seconds and bspline in about a minute.</p>

---

## Post #6 by @hao (2021-02-15 18:54 UTC)

<p>realy? it is good news. could you give me some articles ?<br>
thanks</p>

---

## Post #7 by @lassoan (2021-02-15 19:09 UTC)

<p>The <a href="https://itk.org/ItkSoftwareGuide.pdf">ITK Software Guide</a> is a good introduction to mechanics of intensity-based medical image registration. They should give you an idea how to choose number of samples, step size/relaxation factor, optimizer stopping conditions, etc. to reduce registration time.</p>

---

## Post #8 by @hao (2021-02-15 19:22 UTC)

<p>I will try to read it, likely not easy to understand all of the mechanics of ITK. I am a medical doctor… <img src="https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=9" title=":sweat_smile:" class="emoji" alt=":sweat_smile:"></p>

---

## Post #9 by @hao (2021-02-16 09:37 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="15999" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>With tuning of registration parameters (cropping, resampling of inputs, good initialization, reduced number of samples, etc.) you should be able to get rigid registration in 10-20 seconds and bspline in about a minute.</p>
</blockquote>
</aside>
<p>I have read some ITK, Elastix and SimpleElastix documents and begin to understand some mecanisme in the processus. but in pratice, I have still some questions:</p>
<ol>
<li>tuning of registration parameters, do you means that tuning this parameters in the General Registration (brain) module? because I see that in the Elastix module the paramers are in the database folder, and the items are differents with which you have mentioned (cropping, resampling, intitialiation, et al). In the Elastix parametermap, there are such as "ImagePyramidSchedule, Number of Iterations, Number of spatial samples, et al), which may be modified to optimise the proecssus, could we research the same resultes?</li>
<li>resampling of inputs: do you means to down-sampling the moving images, ex from 512x512x200 to 256x256X100</li>
<li>good initialization: do you means to do the manuel registration and harden the transform?</li>
<li>reduced number of samples: I see that in the tuto, 100 000 to 200 000 are oftens used. We can reduce to which niveau? 10 000. how about B spline grid size.</li>
</ol>

---

## Post #10 by @lassoan (2021-02-16 15:37 UTC)

<aside class="quote no-group" data-username="hao" data-post="9" data-topic="15999">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/ea5d25/48.png" class="avatar"> hao:</div>
<blockquote>
<p>tuning of registration parameters, do you means that tuning this parameters in the General Registration (brain) module?</p>
</blockquote>
</aside>
<ul>
<li>General registration (BRAINS): parameters can be changed in the module user interface</li>
<li>General registration (Elastix): parameters can be changed by editing parameter files</li>
</ul>
<aside class="quote no-group" data-username="hao" data-post="9" data-topic="15999">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/ea5d25/48.png" class="avatar"> hao:</div>
<blockquote>
<p>resampling of inputs: do you means to down-sampling the moving images, ex from 512x512x200 to 256x256X100</p>
</blockquote>
</aside>
<p>Yes. Downsampling will not affect the registration time fundamentally (as registration is sample-based) but there are a few places where a smaller image reduces processing time.</p>
<aside class="quote no-group" data-username="hao" data-post="9" data-topic="15999">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/ea5d25/48.png" class="avatar"> hao:</div>
<blockquote>
<p>good initialization: do you means to do the manuel registration and harden the transform?</p>
</blockquote>
</aside>
<p>Convergence is usually faster if you start closer to the optimal solution. You can either turn of automatic initialization and manually register and harden transform on the input; or experiment with different automatic initialization options.</p>
<aside class="quote no-group" data-username="hao" data-post="9" data-topic="15999">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/ea5d25/48.png" class="avatar"> hao:</div>
<blockquote>
<p>reduced number of samples: I see that in the tuto, 100 000 to 200 000 are oftens used. We can reduce to which niveau?</p>
</blockquote>
</aside>
<p>It depends on the size and complexity of your images. A typical 3D volume size is 256x256x256 = 16 million voxels. If on average you take 1 sample out of each 5x5x5 cube then you will end up with 134 000 samples. This sampling density is typically sufficient for rigid registration and often you can get acceptable results with even less samples (about 10 000). If you do bspline registration with many grid points then you might want to use a bit more samples.</p>

---

## Post #11 by @hao (2021-02-16 20:51 UTC)

<p>thanks Iassoan, your advise is very useful.</p>

---
