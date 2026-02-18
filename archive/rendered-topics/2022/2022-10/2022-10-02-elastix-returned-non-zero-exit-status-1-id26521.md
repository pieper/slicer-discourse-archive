# Elastix returned non-zero exit status 1

**Topic ID**: 26521
**Date**: 2022-10-02
**URL**: https://discourse.slicer.org/t/elastix-returned-non-zero-exit-status-1/26521

---

## Post #1 by @Kaczor69xd (2022-10-02 06:52 UTC)

<p>Hello<br>
I also have some problem with this extension. Tried it yesterday twice on different CTs. I’m pasting  whole code from python interaction. I think the problem is with elastix, it can’t get the measurements right. If you can help me I’d be grateful.</p>
<pre><code class="lang-auto">which elastix:   /Applications/Slicer.app/Contents/Extensions-30893/SlicerElastix/lib/Slicer-5.0/elastix
which elastix:   /Applications/Slicer.app/Contents/Extensions-30893/SlicerElastix/lib/Slicer-5.0/elastix
elastix runs at: Mac-mini-Micha.local
elastix runs at: Mac-mini-Micha.local
  macOS 12.6 (x64), 21G115
  macOS 12.6 (x64), 21G115
  with 8192 MB memory, and 8 cores @ 2400 MHz.
  with 8192 MB memory, and 8 cores @ 2400 MHz.
-------------------------------------------------------------------------
-------------------------------------------------------------------------


Running elastix with parameter file 0: "/Applications/Slicer.app/Contents/Extensions-30893/ABLTemporalBoneSegmentation/lib/Slicer-5.0/qt-scripted-modules/Resources/Parameters/Parameters_Rigid.txt".
Running elastix with parameter file 0: "/Applications/Slicer.app/Contents/Extensions-30893/ABLTemporalBoneSegmentation/lib/Slicer-5.0/qt-scripted-modules/Resources/Parameters/Parameters_Rigid.txt".


Current time: Sun Oct  2 08:45:18 2022.
Current time: Sun Oct  2 08:45:18 2022.
Reading the elastix parameters from file ...
Reading the elastix parameters from file ...


Installing all components.
Installing all components.
InstallingComponents was successful.
InstallingComponents was successful.


ELASTIX version: 5.0.1
ELASTIX version: 5.0.1
Command line options from ElastixBase:
Command line options from ElastixBase:
-f        /private/var/folders/l7/h7lnn18d3zdc6vc84b_yvcxc0000gn/T/Slicer-michalkaczmarczyk/Elastix/20221002_084517_248/input/fixed.mha
-f        /private/var/folders/l7/h7lnn18d3zdc6vc84b_yvcxc0000gn/T/Slicer-michalkaczmarczyk/Elastix/20221002_084517_248/input/fixed.mha
-m        /private/var/folders/l7/h7lnn18d3zdc6vc84b_yvcxc0000gn/T/Slicer-michalkaczmarczyk/Elastix/20221002_084517_248/input/moving.mha
-m        /private/var/folders/l7/h7lnn18d3zdc6vc84b_yvcxc0000gn/T/Slicer-michalkaczmarczyk/Elastix/20221002_084517_248/input/moving.mha
-fMask    /private/var/folders/l7/h7lnn18d3zdc6vc84b_yvcxc0000gn/T/Slicer-michalkaczmarczyk/Elastix/20221002_084517_248/input/fixedMask.mha
-fMask    /private/var/folders/l7/h7lnn18d3zdc6vc84b_yvcxc0000gn/T/Slicer-michalkaczmarczyk/Elastix/20221002_084517_248/input/fixedMask.mha
-mMask    /private/var/folders/l7/h7lnn18d3zdc6vc84b_yvcxc0000gn/T/Slicer-michalkaczmarczyk/Elastix/20221002_084517_248/input/movingMask.mha
-mMask    /private/var/folders/l7/h7lnn18d3zdc6vc84b_yvcxc0000gn/T/Slicer-michalkaczmarczyk/Elastix/20221002_084517_248/input/movingMask.mha
-out      /private/var/folders/l7/h7lnn18d3zdc6vc84b_yvcxc0000gn/T/Slicer-michalkaczmarczyk/Elastix/20221002_084517_248/result-transform/
-out      /private/var/folders/l7/h7lnn18d3zdc6vc84b_yvcxc0000gn/T/Slicer-michalkaczmarczyk/Elastix/20221002_084517_248/result-transform/
-p        /Applications/Slicer.app/Contents/Extensions-30893/ABLTemporalBoneSegmentation/lib/Slicer-5.0/qt-scripted-modules/Resources/Parameters/Parameters_Rigid.txt
-p        /Applications/Slicer.app/Contents/Extensions-30893/ABLTemporalBoneSegmentation/lib/Slicer-5.0/qt-scripted-modules/Resources/Parameters/Parameters_Rigid.txt
-threads  unspecified, so all available threads are used
-threads  unspecified, so all available threads are used
WARNING: The parameter "UseDirectionCosines", requested at entry number 0, does not exist at all.
WARNING: The parameter "UseDirectionCosines", requested at entry number 0, does not exist at all.
  The default value "true" is used instead.
  The default value "true" is used instead.


WARNING: The option "UseDirectionCosines" was not found in your parameter file.
WARNING: The option "UseDirectionCosines" was not found in your parameter file.
  From elastix 4.8 it defaults to true!
  From elastix 4.8 it defaults to true!
This may change the behavior of your registrations considerably.
This may change the behavior of your registrations considerably.


Command line options from TransformBase:
Command line options from TransformBase:
-t0       unspecified, so no initial transform used
-t0       unspecified, so no initial transform used


Reading images...
Reading images...
Reading images took 477 ms.
Reading images took 477 ms.


WARNING: the fixed pyramid schedule is not fully specified!
WARNING: the fixed pyramid schedule is not fully specified!
  A default pyramid schedule is used.
  A default pyramid schedule is used.
WARNING: the moving pyramid schedule is not fully specified!
WARNING: the moving pyramid schedule is not fully specified!
  A default pyramid schedule is used.
  A default pyramid schedule is used.
WARNING: The parameter "AutomaticTransformInitializationMethod", requested at entry number 0, does not exist at all.
WARNING: The parameter "AutomaticTransformInitializationMethod", requested at entry number 0, does not exist at all.
  The default value "GeometricalCenter" is used instead.
  The default value "GeometricalCenter" is used instead.
Transform parameters are initialized as: [0, 0, 0, -25.126531652343715, -31.40466437890626, -40.37869225390621]
Transform parameters are initialized as: [0, 0, 0, -25.126531652343715, -31.40466437890626, -40.37869225390621]
Scales are estimated automatically.
Scales are estimated automatically.
Scales for transform parameters are: [3401.561698635128, 3491.2521564018725, 2502.4099204386434, 1, 1, 1]
Scales for transform parameters are: [3401.561698635128, 3491.2521564018725, 2502.4099204386434, 1, 1, 1]
Initialization of all components (before registration) took: 9 ms.
Initialization of all components (before registration) took: 9 ms.
Preparation of the image pyramids took: 2600 ms.
Preparation of the image pyramids took: 2600 ms.


Resolution: 0
Resolution: 0
WARNING: The parameter "ShowExactMetricValue", requested at entry number 0, does not exist at all.
WARNING: The parameter "ShowExactMetricValue", requested at entry number 0, does not exist at all.
  The default value "false" is used instead.
  The default value "false" is used instead.
WARNING: The parameter "CheckNumberOfSamples", requested at entry number 0, does not exist at all.
WARNING: The parameter "CheckNumberOfSamples", requested at entry number 0, does not exist at all.
  The default value "true" is used instead.
  The default value "true" is used instead.
WARNING: The parameter "UseMultiThreadingForMetrics", requested at entry number 0, does not exist at all.
WARNING: The parameter "UseMultiThreadingForMetrics", requested at entry number 0, does not exist at all.
  The default value "true" is used instead.
  The default value "true" is used instead.
WARNING: The parameter "ErodeFixedMask", requested at entry number 0, does not exist at all.
WARNING: The parameter "ErodeFixedMask", requested at entry number 0, does not exist at all.
  The default value "false" is used instead.
  The default value "false" is used instead.
WARNING: The parameter "ErodeMovingMask", requested at entry number 0, does not exist at all.
WARNING: The parameter "ErodeMovingMask", requested at entry number 0, does not exist at all.
  The default value "false" is used instead.
  The default value "false" is used instead.
Setting the fixed masks took: 1 ms.
Setting the fixed masks took: 1 ms.
Setting the moving masks took: 0 ms.
Setting the moving masks took: 0 ms.
WARNING: The parameter "NumberOfFixedHistogramBins", requested at entry number 0, does not exist at all.
WARNING: The parameter "NumberOfFixedHistogramBins", requested at entry number 0, does not exist at all.
  The default value "32" is used instead.
  The default value "32" is used instead.
WARNING: The parameter "NumberOfMovingHistogramBins", requested at entry number 0, does not exist at all.
WARNING: The parameter "NumberOfMovingHistogramBins", requested at entry number 0, does not exist at all.
  The default value "32" is used instead.
  The default value "32" is used instead.
WARNING: The parameter "FixedLimitRangeRatio", requested at entry number 0, does not exist at all.
WARNING: The parameter "FixedLimitRangeRatio", requested at entry number 0, does not exist at all.
  The default value "0.01" is used instead.
  The default value "0.01" is used instead.
WARNING: The parameter "MovingLimitRangeRatio", requested at entry number 0, does not exist at all.
WARNING: The parameter "MovingLimitRangeRatio", requested at entry number 0, does not exist at all.
  The default value "0.01" is used instead.
  The default value "0.01" is used instead.
WARNING: The parameter "FixedKernelBSplineOrder", requested at entry number 0, does not exist at all.
WARNING: The parameter "FixedKernelBSplineOrder", requested at entry number 0, does not exist at all.
  The default value "0" is used instead.
  The default value "0" is used instead.
WARNING: The parameter "MovingKernelBSplineOrder", requested at entry number 0, does not exist at all.
WARNING: The parameter "MovingKernelBSplineOrder", requested at entry number 0, does not exist at all.
  The default value "3" is used instead.
  The default value "3" is used instead.
WARNING: The parameter "UseFastAndLowMemoryVersion", requested at entry number 0, does not exist at all.
WARNING: The parameter "UseFastAndLowMemoryVersion", requested at entry number 0, does not exist at all.
  The default value "true" is used instead.
  The default value "true" is used instead.
WARNING: The parameter "UseJacobianPreconditioning", requested at entry number 0, does not exist at all.
WARNING: The parameter "UseJacobianPreconditioning", requested at entry number 0, does not exist at all.
  The default value "false" is used instead.
  The default value "false" is used instead.
WARNING: The parameter "FiniteDifferenceDerivative", requested at entry number 0, does not exist at all.
WARNING: The parameter "FiniteDifferenceDerivative", requested at entry number 0, does not exist at all.
  The default value "false" is used instead.
  The default value "false" is used instead.
WARNING: The parameter "SP_A", requested at entry number 0, does not exist at all.
WARNING: The parameter "SP_A", requested at entry number 0, does not exist at all.
  The default value "20" is used instead.
  The default value "20" is used instead.
WARNING: The parameter "MaximumNumberOfSamplingAttempts", requested at entry number 0, does not exist at all.
WARNING: The parameter "MaximumNumberOfSamplingAttempts", requested at entry number 0, does not exist at all.
  The default value "0" is used instead.
  The default value "0" is used instead.
WARNING: The parameter "SigmoidInitialTime", requested at entry number 0, does not exist at all.
WARNING: The parameter "SigmoidInitialTime", requested at entry number 0, does not exist at all.
  The default value "0" is used instead.
  The default value "0" is used instead.
WARNING: The parameter "MaxBandCovSize", requested at entry number 0, does not exist at all.
WARNING: The parameter "MaxBandCovSize", requested at entry number 0, does not exist at all.
  The default value "192" is used instead.
  The default value "192" is used instead.
WARNING: The parameter "NumberOfBandStructureSamples", requested at entry number 0, does not exist at all.
WARNING: The parameter "NumberOfBandStructureSamples", requested at entry number 0, does not exist at all.
  The default value "10" is used instead.
  The default value "10" is used instead.
WARNING: The parameter "UseAdaptiveStepSizes", requested at entry number 0, does not exist at all.
WARNING: The parameter "UseAdaptiveStepSizes", requested at entry number 0, does not exist at all.
  The default value "true" is used instead.
  The default value "true" is used instead.
WARNING: The parameter "AutomaticParameterEstimation", requested at entry number 0, does not exist at all.
WARNING: The parameter "AutomaticParameterEstimation", requested at entry number 0, does not exist at all.
  The default value "true" is used instead.
  The default value "true" is used instead.
WARNING: The parameter "UseConstantStep", requested at entry number 0, does not exist at all.
WARNING: The parameter "UseConstantStep", requested at entry number 0, does not exist at all.
  The default value "false" is used instead.
  The default value "false" is used instead.
WARNING: The parameter "MaximumStepLengthRatio", requested at entry number 0, does not exist at all.
WARNING: The parameter "MaximumStepLengthRatio", requested at entry number 0, does not exist at all.
  The default value "1" is used instead.
  The default value "1" is used instead.
WARNING: The parameter "MaximumStepLength", requested at entry number 0, does not exist at all.
WARNING: The parameter "MaximumStepLength", requested at entry number 0, does not exist at all.
  The default value "0.190429" is used instead.
  The default value "0.190429" is used instead.
WARNING: The parameter "NumberOfGradientMeasurements", requested at entry number 0, does not exist at all.
WARNING: The parameter "NumberOfGradientMeasurements", requested at entry number 0, does not exist at all.
  The default value "0" is used instead.
  The default value "0" is used instead.
WARNING: The parameter "NumberOfJacobianMeasurements", requested at entry number 0, does not exist at all.
WARNING: The parameter "NumberOfJacobianMeasurements", requested at entry number 0, does not exist at all.
  The default value "1000" is used instead.
  The default value "1000" is used instead.
WARNING: The parameter "NumberOfSamplesForExactGradient", requested at entry number 0, does not exist at all.
WARNING: The parameter "NumberOfSamplesForExactGradient", requested at entry number 0, does not exist at all.
  The default value "100000" is used instead.
  The default value "100000" is used instead.
WARNING: The parameter "SigmoidScaleFactor", requested at entry number 0, does not exist at all.
WARNING: The parameter "SigmoidScaleFactor", requested at entry number 0, does not exist at all.
  The default value "0.1" is used instead.
  The default value "0.1" is used instead.
Elastix initialization of all components (for this resolution) took: 2 ms.
Elastix initialization of all components (for this resolution) took: 2 ms.
  Computing the fixed image extrema took 1 ms.
  Computing the fixed image extrema took 1 ms.
  Computing the moving image extrema took 1 ms.
  Computing the moving image extrema took 1 ms.
Initialization of AdvancedMattesMutualInformation metric took: 5 ms.
Initialization of AdvancedMattesMutualInformation metric took: 5 ms.
Starting automatic parameter estimation for AdaptiveStochasticGradientDescent ...
Starting automatic parameter estimation for AdaptiveStochasticGradientDescent ...
WARNING: The parameter "ASGDParameterEstimationMethod", requested at entry number 0, does not exist at all.
WARNING: The parameter "ASGDParameterEstimationMethod", requested at entry number 0, does not exist at all.
  The default value "Original" is used instead.
  The default value "Original" is used instead.
  Computing JacobianTerms ...
  Computing JacobianTerms ...
  Computing the Jacobian terms took 0.001969s
  Computing the Jacobian terms took 0.001969s
  NumberOfGradientMeasurements to estimate sigma_i: 10
  NumberOfGradientMeasurements to estimate sigma_i: 10
  Sampling gradients ...
  Sampling gradients ...


  Progress: 0%Time spent in resolution 0 (ITK initialization and iterating): 0.010 s.
  Progress: 0%Time spent in resolution 0 (ITK initialization and iterating): 0.010 s.
Stopping condition: Error in metric.
Stopping condition: Error in metric.
Settings of AdaptiveStochasticGradientDescent in resolution 0:
Settings of AdaptiveStochasticGradientDescent in resolution 0:
( SP_a 1.000000 )
( SP_a 1.000000 )
( SP_A 20.000000 )
( SP_A 20.000000 )
( SP_alpha 0.602000 )
( SP_alpha 0.602000 )
( SigmoidMax 1.000000 )
( SigmoidMax 1.000000 )
( SigmoidMin -0.800000 )
( SigmoidMin -0.800000 )
( SigmoidScale 0.000000 )
( SigmoidScale 0.000000 )




itk::ExceptionObject (0x7f8ed8009e70)
itk::ExceptionObject (0x7f8ed8009e70)
Location: "ElastixTemplate - Run()"
Location: "ElastixTemplate - Run()"
File: /Volumes/D/S/S-0-E-b/SlicerElastix-build/elastix/Common/CostFunctions/itkAdvancedImageToImageMetric.hxx
File: /Volumes/D/S/S-0-E-b/SlicerElastix-build/elastix/Common/CostFunctions/itkAdvancedImageToImageMetric.hxx
Line: 916
Line: 916
Description: ITK ERROR: AdvancedMattesMutualInformationMetric(0x7f8ecf813a00): Too many samples map outside moving image buffer: 0 / 1119
Description: ITK ERROR: AdvancedMattesMutualInformationMetric(0x7f8ecf813a00): Too many samples map outside moving image buffer: 0 / 1119




Error occurred during actual registration.
Error occurred during actual registration.




Errors occurred!
Errors occurred!
Error: Command 'elastix' returned non-zero exit status 1.
Traceback (most recent call last):
  File "/Applications/Slicer.app/Contents/Extensions-30893/ABLTemporalBoneSegmentation/lib/Slicer-5.0/qt-scripted-modules/ABLTemporalBoneSegmentationModule.py", line 635, in process_transform
    output = function()
  File "/Applications/Slicer.app/Contents/Extensions-30893/ABLTemporalBoneSegmentation/lib/Slicer-5.0/qt-scripted-modules/ABLTemporalBoneSegmentationModule.py", line 808, in transform
    return ABLTemporalBoneSegmentationModuleLogic().apply_elastix_rigid_registration(elastix=self.elastixLogic,
  File "/Applications/Slicer.app/Contents/Extensions-30893/ABLTemporalBoneSegmentation/lib/Slicer-5.0/qt-scripted-modules/ABLTemporalBoneSegmentationModule.py", line 1311, in apply_elastix_rigid_registration
    elastix.registerVolumes(
  File "/Applications/Slicer.app/Contents/Extensions-30893/SlicerElastix/lib/Slicer-5.0/qt-scripted-modules/Elastix.py", line 818, in registerVolumes
    self.logProcessOutput(ep)
  File "/Applications/Slicer.app/Contents/Extensions-30893/SlicerElastix/lib/Slicer-5.0/qt-scripted-modules/Elastix.py", line 739, in logProcessOutput
    raise subprocess.CalledProcessError(return_code, "elastix")
subprocess.CalledProcessError: Command 'elastix' returned non-zero exit status 1.
</code></pre>

---

## Post #2 by @Young_Wang (2022-11-30 18:21 UTC)

<p><a class="mention" href="/u/fufu">@FUFU</a> <a class="mention" href="/u/dat_minh">@DAT_Minh</a> I’m working on a similar project using this module and experiencing the same command elsatix return to non-zern exit status 1 error.<br>
Could you please elaborate on how to solve this?</p>

---

## Post #3 by @lassoan (2022-11-30 20:52 UTC)

<aside class="quote no-group quote-modified" data-username="Kaczor69xd" data-post="1" data-topic="26521">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/b487fb/48.png" class="avatar"> Kaczor69xd:</div>
<blockquote>
<pre><code class="lang-auto">AdvancedMattesMutualInformationMetric(0x7f8ecf813a00): Too many samples map outside moving image buffer:l
</code></pre>
</blockquote>
</aside>
<p>This is a very common error, it simply means that the input images must be better aligned. Make sure that you crop any non-overlapping regions from the input images and all transforms are hardened on the input images.</p>

---

## Post #4 by @lassoan (2022-11-30 20:54 UTC)



---

## Post #5 by @Young_Wang (2022-12-01 13:45 UTC)

<p>hey <a class="mention" href="/u/lassoan">@lassoan</a> , i followed your advice that cropped the excessive volumes before registration using the ABL module but I still experience the same error. One interesting thing, I am using the <a href="https://www.nature.com/articles/sdata2018297" rel="noopener nofollow ugc">open-ear</a> dataset. I found slicer behaves differently between mac and windows with the same steps on the same data.</p>

---

## Post #6 by @lassoan (2022-12-01 14:07 UTC)

<p>Please upload the scene somewhere and post the link here and I can have a look.</p>
<aside class="quote no-group" data-username="Young_Wang" data-post="5" data-topic="26521">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/young_wang/48/13926_2.png" class="avatar"> Young_Wang:</div>
<blockquote>
<p>I found slicer behaves differently between mac and windows with the same steps on the same data.</p>
</blockquote>
</aside>
<p>If the registration with the same input images and registration parameters consistently converges on one platform then it should converge on all platforms.</p>
<p>If the registration does not converge to a global optimum then even the slightest numerical differences can lead to very different end results, so in these cases it may be normal that you end up getting different results on different platforms.</p>

---

## Post #7 by @Young_Wang (2022-12-01 14:41 UTC)

<p>Thank you for your prompt reply. I uploaded the scene into <a href="https://dalu-my.sharepoint.com/:u:/g/personal/jn511893_dal_ca/EYuu9zbW4IpGgbsORrBFx7IBfkqB8rIdMNAAMJrfes8s2A?e=g0GFhk" rel="noopener nofollow ugc">this one drive</a>. Please let me know if you have any difficulties accessing it.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b091691ff3bf50af162546ee3b132816e683406.jpeg" data-download-href="/uploads/short-url/aHNhsqhq2WCuYawtr7CRzNRU3SS.jpeg?dl=1" title="error message" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b091691ff3bf50af162546ee3b132816e683406_2_690x394.jpeg" alt="error message" data-base62-sha1="aHNhsqhq2WCuYawtr7CRzNRU3SS" width="690" height="394" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b091691ff3bf50af162546ee3b132816e683406_2_690x394.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b091691ff3bf50af162546ee3b132816e683406_2_1035x591.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b091691ff3bf50af162546ee3b132816e683406_2_1380x788.jpeg 2x" data-dominant-color="767574"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">error message</span><span class="informations">1920×1098 175 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I also noticed that somehow in the sample data module the text is cutoff<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3d397d69a322a969c701a308fa2c5117d82af3c6.jpeg" data-download-href="/uploads/short-url/8JCiqx8ldehbIc9T5DoaMXB4rr0.jpeg?dl=1" title="title cutoff" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3d397d69a322a969c701a308fa2c5117d82af3c6_2_690x396.jpeg" alt="title cutoff" data-base62-sha1="8JCiqx8ldehbIc9T5DoaMXB4rr0" width="690" height="396" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3d397d69a322a969c701a308fa2c5117d82af3c6_2_690x396.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3d397d69a322a969c701a308fa2c5117d82af3c6_2_1035x594.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3d397d69a322a969c701a308fa2c5117d82af3c6_2_1380x792.jpeg 2x" data-dominant-color="3F3E3C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">title cutoff</span><span class="informations">1920×1102 119 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @lassoan (2022-12-01 17:34 UTC)

<p>In the scene I only see one volume (PostDentalSurgery) in 3 versions (original, cropped, transformed). Can you share a scene where you have two volumes that you want to register (a moving and a fixed)?</p>
<p>I also noticed that you have a CochleaRegistrationMask. Masking is only intented for specifying a non-rectangular ROI that is only slightly smaller than the image (e.g., to exclude a surgical tool or excised tissue region from the registration). Instead, the mask is much, much smaller than the cropped image:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/29277a3136716a7c389f4f5886c5eaeff0f9ba19.jpeg" data-download-href="/uploads/short-url/5S49FPgajfGCh8mKee1wr55dPpT.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/29277a3136716a7c389f4f5886c5eaeff0f9ba19_2_690x497.jpeg" alt="image" data-base62-sha1="5S49FPgajfGCh8mKee1wr55dPpT" width="690" height="497" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/29277a3136716a7c389f4f5886c5eaeff0f9ba19_2_690x497.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/29277a3136716a7c389f4f5886c5eaeff0f9ba19_2_1035x745.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/29277a3136716a7c389f4f5886c5eaeff0f9ba19.jpeg 2x" data-dominant-color="1C1D1C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1254×904 65.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>The area on this slice is 10-20x smaller, so the volume is about 100x smaller. This means that random volumetric sampling will fail 99% of the time, which will cause the registration to fail with “too many samples map outside moving image” error. Instead of using such tiny mask, crop the volume to the size of the mask.</p>

---

## Post #9 by @Young_Wang (2022-12-02 00:49 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>, thanks for looking into this for me. I was following the tutorial list <a href="https://github.com/Auditory-Biophysics-Lab/Slicer-ABLTemporalBoneSegmentation" rel="noopener nofollow ugc">here</a>. Using the cropped PostDentalSurgery volume as the input volume in the ABL extension.</p>

---

## Post #10 by @lassoan (2022-12-03 13:54 UTC)

<p>Probably cropping the image to the green ROI (instead of using that ROI as mask) would fix the sampling error.</p>
<p>The registration metric is computed by generating random samples. Samples that fall outside the mask are discarded. If the mask is small (volume of mask is smaller than maybe 50% of the image volume) then many samples are discarded. If too many sanples are discarded then you get the sampling error message.</p>

---

## Post #11 by @Young_Wang (2022-12-05 02:33 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> thanks, I will give this a try</p>

---
