---
topic_id: 11190
title: "Registration Ct Mri"
date: 2020-04-19
url: https://discourse.slicer.org/t/11190
---

# Registration CT MRI

**Topic ID**: 11190
**Date**: 2020-04-19
**URL**: https://discourse.slicer.org/t/registration-ct-mri/11190

---

## Post #1 by @sfglio (2020-04-19 21:12 UTC)

<p>I want to reg CT (moving) to MRI (fixed):</p>
<ul>
<li>I have cropped the volume to the ROI in both volumes</li>
<li>I have resampled both images to the same voxel size</li>
<li>I have initially transformed the CT to MRI and provided this transform as initialization transform</li>
</ul>
<p>I tried Rigid, affine it does not matter cause I get this error:</p>
<p>General Registration (BRAINS) standard error:</p>
<p>ExceptionObject caught !</p>
<p>itk::ExceptionObject (0x7ffcf263ec00)</p>
<p>Location: “unknown”</p>
<p>File: /Volumes/Dashboards/Preview/Slicer-0-build/ITK/Modules/Registration/Metricsv4/include/itkMattesMutualInformationImageToImageMetricv4.hxx</p>
<p>Line: 312</p>
<p>Description: itk::ERROR: MattesMutualInformationImageToImageMetricv4(0x7ffcf263ddd0): Joint PDF summed to zero</p>
<p>Any idea?</p>

---

## Post #2 by @lassoan (2020-04-20 00:34 UTC)

<p>This error message means that the volumes don’t overlap enough in space.</p>
<p>Can you attach a screenshot of your initial state?</p>
<p>You may need to harden the transform after applying, otherwise it does not affect the registration.</p>
<p>You may also try “General registration (Elastix)” module (provided by SlicerElastix extension), as it tend to be less sensitive to initialization and optimization parameters.</p>

---

## Post #3 by @sfglio (2020-04-20 17:30 UTC)

<aside class="onebox googledrive">
  <header class="source">
      <a href="https://drive.google.com/file/d/1lwEo8YnIghLZoe4lF-6ppK0tcwVQAUO2/view?usp=drive_open" target="_blank" rel="nofollow noopener">drive.google.com</a>
  </header>
  <article class="onebox-body">
    
<div class="aspect-image" style="--aspect-ratio:690/362;"><img src="https://lh5.googleusercontent.com/mbiiv4dkjsdIU_LF0cn4wgsbpmsA5JYbmM-b_M5ZnaRooyML_Qssbat89bc_FvQ=w1200-h630-p" class="thumbnail" width="690" height="362"></div>

<h3><a href="https://drive.google.com/file/d/1lwEo8YnIghLZoe4lF-6ppK0tcwVQAUO2/view?usp=drive_open" target="_blank" rel="nofollow noopener">Bildschirmfoto 2020-04-20 um 18.28.10.png</a></h3>

<p>Google Drive file.</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>MRI and CT were resampled to bspline 0.2mm, however image dimensions were not the same<br>
I did harden the initial transf of the ct.<br>
as one can see there is a mismatch between ct and mri. the registration proc. could not optmize my initial transformation or provided the aforementioned error msg.<br>
elastix sometimes reported the same error msg or did not improve the results. the pity is, I already managed once a perfect registration however fail to repeat it now (same data).</p>
<p>Interestingly, fixed (ct) and moving (mri) works faster and better than the other way round. However I am looking for reg. ct (moving) on mri (fixed)</p>

---

## Post #4 by @sfglio (2020-04-20 17:45 UTC)

<p>Volume registration is started in working directory: /var/folders/lv/f_t6f0ys1x34xd03xcdprbym0000gq/T/Slicer/Elastix/20200420_194355_170<br>
Register volumes…</p>
<p>elastix is started at Mon Apr 20 19:43:55 2020.</p>
<h2>which elastix:   /Applications/Slicer.app/Contents/Extensions-28989/SlicerElastix/lib/Slicer-4.11/elastix<br>
elastix runs at: Fs-MacBook-Pro.local<br>
Mac OS X 10.14.6 (x64), 18G3020<br>
with 8192 MB memory, and 2 cores @ 2900 MHz.</h2>
<p>Running elastix with parameter file 0: “/Applications/Slicer.app/Contents/Extensions-28989/SlicerElastix/lib/Slicer-4.11/qt-scripted-modules/Resources/RegistrationParameters/Parameters_Rigid.txt”.</p>
<p>Current time: Mon Apr 20 19:43:55 2020.<br>
Reading the elastix parameters from file …</p>
<p>Installing all components.<br>
InstallingComponents was successful.</p>
<p>ELASTIX version: 5.000<br>
Command line options from ElastixBase:<br>
-f        /var/folders/lv/f_t6f0ys1x34xd03xcdprbym0000gq/T/Slicer/Elastix/20200420_194355_170/input/fixed.mha<br>
-m        /var/folders/lv/f_t6f0ys1x34xd03xcdprbym0000gq/T/Slicer/Elastix/20200420_194355_170/input/moving.mha<br>
-fMask    unspecified, so no fixed mask used<br>
-mMask    unspecified, so no moving mask used<br>
-out      /var/folders/lv/f_t6f0ys1x34xd03xcdprbym0000gq/T/Slicer/Elastix/20200420_194355_170/result-transform/<br>
-p        /Applications/Slicer.app/Contents/Extensions-28989/SlicerElastix/lib/Slicer-4.11/qt-scripted-modules/Resources/RegistrationParameters/Parameters_Rigid.txt<br>
-p        /Applications/Slicer.app/Contents/Extensions-28989/SlicerElastix/lib/Slicer-4.11/qt-scripted-modules/Resources/RegistrationParameters/Parameters_BSpline.txt<br>
-threads  unspecified, so all available threads are used<br>
WARNING: The parameter “UseDirectionCosines”, requested at entry number 0, does not exist at all.<br>
The default value “true” is used instead.</p>
<p>WARNING: The option “UseDirectionCosines” was not found in your parameter file.<br>
From elastix 4.8 it defaults to true!<br>
This may change the behavior of your registrations considerably.</p>
<p>Command line options from TransformBase:<br>
-t0       unspecified, so no initial transform used</p>
<p>Reading images…<br>
Reading images took 150 ms.</p>
<p>WARNING: the fixed pyramid schedule is not fully specified!<br>
A default pyramid schedule is used.<br>
WARNING: the moving pyramid schedule is not fully specified!<br>
A default pyramid schedule is used.<br>
WARNING: The parameter “AutomaticTransformInitializationMethod”, requested at entry number 0, does not exist at all.<br>
The default value “GeometricalCenter” is used instead.<br>
Transform parameters are initialized as: [0, 0, 0, -1.5244374302985904, -24.311078731531566, -14.602596841435947]<br>
Scales are estimated automatically.<br>
Scales for transform parameters are: [3772.2559831259255, 3825.3517771192674, 5551.213166583119, 1, 1, 1]<br>
Initialization of all components (before registration) took: 19 ms.<br>
Preparation of the image pyramids took: 1777 ms.</p>
<p>Resolution: 0<br>
WARNING: The parameter “ShowExactMetricValue”, requested at entry number 0, does not exist at all.<br>
The default value “false” is used instead.<br>
WARNING: The parameter “CheckNumberOfSamples”, requested at entry number 0, does not exist at all.<br>
The default value “true” is used instead.<br>
WARNING: The parameter “UseMultiThreadingForMetrics”, requested at entry number 0, does not exist at all.<br>
The default value “true” is used instead.<br>
Setting the fixed masks took: 0 ms.<br>
Setting the moving masks took: 0 ms.<br>
WARNING: The parameter “NumberOfFixedHistogramBins”, requested at entry number 0, does not exist at all.<br>
The default value “32” is used instead.<br>
WARNING: The parameter “NumberOfMovingHistogramBins”, requested at entry number 0, does not exist at all.<br>
The default value “32” is used instead.<br>
WARNING: The parameter “FixedLimitRangeRatio”, requested at entry number 0, does not exist at all.<br>
The default value “0.01” is used instead.<br>
WARNING: The parameter “MovingLimitRangeRatio”, requested at entry number 0, does not exist at all.<br>
The default value “0.01” is used instead.<br>
WARNING: The parameter “FixedKernelBSplineOrder”, requested at entry number 0, does not exist at all.<br>
The default value “0” is used instead.<br>
WARNING: The parameter “MovingKernelBSplineOrder”, requested at entry number 0, does not exist at all.<br>
The default value “3” is used instead.<br>
WARNING: The parameter “UseFastAndLowMemoryVersion”, requested at entry number 0, does not exist at all.<br>
The default value “true” is used instead.<br>
WARNING: The parameter “UseJacobianPreconditioning”, requested at entry number 0, does not exist at all.<br>
The default value “false” is used instead.<br>
WARNING: The parameter “FiniteDifferenceDerivative”, requested at entry number 0, does not exist at all.<br>
The default value “false” is used instead.<br>
WARNING: The parameter “SP_A”, requested at entry number 0, does not exist at all.<br>
The default value “20” is used instead.<br>
WARNING: The parameter “MaximumNumberOfSamplingAttempts”, requested at entry number 0, does not exist at all.<br>
The default value “0” is used instead.<br>
WARNING: The parameter “SigmoidInitialTime”, requested at entry number 0, does not exist at all.<br>
The default value “0” is used instead.<br>
WARNING: The parameter “MaxBandCovSize”, requested at entry number 0, does not exist at all.<br>
The default value “192” is used instead.<br>
WARNING: The parameter “NumberOfBandStructureSamples”, requested at entry number 0, does not exist at all.<br>
The default value “10” is used instead.<br>
WARNING: The parameter “UseAdaptiveStepSizes”, requested at entry number 0, does not exist at all.<br>
The default value “true” is used instead.<br>
WARNING: The parameter “AutomaticParameterEstimation”, requested at entry number 0, does not exist at all.<br>
The default value “true” is used instead.<br>
WARNING: The parameter “UseConstantStep”, requested at entry number 0, does not exist at all.<br>
The default value “false” is used instead.<br>
WARNING: The parameter “MaximumStepLengthRatio”, requested at entry number 0, does not exist at all.<br>
The default value “1” is used instead.<br>
WARNING: The parameter “MaximumStepLength”, requested at entry number 0, does not exist at all.<br>
The default value “0.449219” is used instead.<br>
WARNING: The parameter “NumberOfGradientMeasurements”, requested at entry number 0, does not exist at all.<br>
The default value “0” is used instead.<br>
WARNING: The parameter “NumberOfJacobianMeasurements”, requested at entry number 0, does not exist at all.<br>
The default value “1000” is used instead.<br>
WARNING: The parameter “NumberOfSamplesForExactGradient”, requested at entry number 0, does not exist at all.<br>
The default value “100000” is used instead.<br>
WARNING: The parameter “SigmoidScaleFactor”, requested at entry number 0, does not exist at all.<br>
The default value “0.1” is used instead.<br>
Elastix initialization of all components (for this resolution) took: 2 ms.<br>
Computing the fixed image extrema took 1 ms.<br>
Computing the moving image extrema took 0 ms.<br>
Initialization of AdvancedMattesMutualInformation metric took: 5 ms.<br>
Starting automatic parameter estimation for AdaptiveStochasticGradientDescent …<br>
WARNING: The parameter “ASGDParameterEstimationMethod”, requested at entry number 0, does not exist at all.<br>
The default value “Original” is used instead.<br>
Computing JacobianTerms …<br>
Computing the Jacobian terms took 0.004218s<br>
NumberOfGradientMeasurements to estimate sigma_i: 6<br>
Sampling gradients …</p>
<p>Progress: 0%Time spent in resolution 0 (ITK initialization and iterating): 0.017 s.<br>
Stopping condition: Error in metric.<br>
Settings of AdaptiveStochasticGradientDescent in resolution 0:<br>
( SP_a 1.000000 )<br>
( SP_A 20.000000 )<br>
( SP_alpha 0.602000 )<br>
( SigmoidMax 1.000000 )<br>
( SigmoidMin -0.800000 )<br>
( SigmoidScale 0.000000 )</p>
<p>itk::ExceptionObject (0x7fa16184a1d0)<br>
Location: “ElastixTemplate - Run()”<br>
File: /Volumes/Dashboards/Preview/S-0-E-b/SlicerElastix-build/elastix/Common/CostFunctions/itkAdvancedImageToImageMetric.hxx<br>
Line: 1007<br>
Description: itk::ERROR: itk::ERROR: AdvancedMattesMutualInformationMetric(0x7fa160840800): Too many samples map outside moving image buffer: 2203 / 16384</p>
<p>Error occurred during actual registration.</p>
<p>Errors occurred!<br>
vtkDebugLeaks has found no leaks.</p>
<p>Error: Command ‘elastix’ returned non-zero exit status 1.</p>

---

## Post #5 by @lassoan (2020-04-20 17:47 UTC)

<aside class="quote no-group" data-username="sfglio" data-post="3" data-topic="11190">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sfglio/48/3346_2.png" class="avatar"> sfglio:</div>
<blockquote>
<p>Interestingly, fixed (ct) and moving (mri) works faster and better than the other way round. However I am looking for reg. ct (moving) on mri (fixed)</p>
</blockquote>
</aside>
<p>That’s not a problem at all. You can swap fixed/moving images and invert the final transform by a single click (“Invert” button in Transforms module).</p>

---

## Post #6 by @sfglio (2020-04-20 17:48 UTC)

<p>OK, thanks a lot!</p>
<p>And what means “Command ‘elastix’ returned non-zero exit status 1.”?</p>

---

## Post #7 by @lassoan (2020-04-20 18:25 UTC)

<aside class="quote no-group" data-username="sfglio" data-post="6" data-topic="11190">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sfglio/48/3346_2.png" class="avatar"> sfglio:</div>
<blockquote>
<p>what means “Command ‘elastix’ returned non-zero exit status 1.”?</p>
</blockquote>
</aside>
<p>It means Elastix encountered an error. Details of the error are described in the Elastix output log.</p>

---

## Post #8 by @sfglio (2020-08-12 09:57 UTC)

<p>I have registered many CTs (fixed) and MRIs (moving), however I forgot to set the option “Slicer Linear Transform” in the General Registration modul. Is there retrospectively the option to get the transf. matrix from 2 registered volumes, as I want to invert now the registration (MRI &lt;- CT)???</p>

---

## Post #9 by @lassoan (2020-08-12 15:12 UTC)

<p>If you haven’t saved the linear transform node, only the resampled moving image, then there is no way to recover that information. Of course, you could re-register the transformed moving image to the moving image to compute a transformation, but then you could just as well re-run the registration.</p>
<p>I assume you have done it using a batch file anyway, so re-running the registration should not take too much effort. If the time required to redo the registrations is a concern then you can virtual machines from a google/microsoft/amazon to distribute the work and speed things up as much as you need.</p>

---

## Post #10 by @sfglio (2020-08-13 21:34 UTC)

<p>Thank you once again for your fast reply and help!</p>
<p>However re-thinking the workflow, I rendered one logical problem:</p>
<p>If I wanna know if MRI is suitable for a spec. surgery planning which was accomplished by CT up to now, I thought I have to do the planning first in MRI and then check it in CT (after registration).</p>
<p>However, as I necessarily have to pre-align the CT and MRI data sets to perform the registration process successfully, I have my FIRST transformation<br>
and<br>
after using General Registration (BRAINS) I get my SECOND transformation.</p>
<p>So could I deduce from these transformations what my surgical planning would like to be in CT?<br>
Do I have to put these two transformations together? Or do I just need the second one in order to answer whether my planning in MRI would be the same in CT???</p>
<p>Kind regards</p>

---

## Post #11 by @lassoan (2020-08-14 00:21 UTC)

<p>Using Slicer, you can transform the surgical plan (points, directions, etc.) and images in any directions, using one combined transform or in multiple steps. So, most likely this will not be a limitation in any way.</p>
<aside class="quote no-group" data-username="sfglio" data-post="10" data-topic="11190">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sfglio/48/3346_2.png" class="avatar"> sfglio:</div>
<blockquote>
<p>do I just need the second one in order to answer whether my planning in MRI would be the same in CT???</p>
</blockquote>
</aside>
<p>We don’t have enough information to make any particular recommendation. Usually you choose a hypothesis, design a study to test it, and perform the study. If you have a high-level idea about what you want to do, we can then help with the technical details.</p>

---
