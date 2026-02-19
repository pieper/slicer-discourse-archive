---
topic_id: 10026
title: "Error With Elastix Registration"
date: 2020-01-30
url: https://discourse.slicer.org/t/10026
---

# Error with elastix registration

**Topic ID**: 10026
**Date**: 2020-01-30
**URL**: https://discourse.slicer.org/t/error-with-elastix-registration/10026

---

## Post #1 by @RadioQuest (2020-01-30 13:55 UTC)

<p>Running elastix with parameter file 0: “/Users/…/Downloads/Slicer.app/Contents/Extensions-27970/SlicerElastix/lib/Slicer-4.11/qt-scripted-modules/Resources/RegistrationParameters/Parameters_Rigid.txt”.</p>
<p>Current time: Thu Jan 30 13:52:42 2020.<br>
Reading the elastix parameters from file …</p>
<p>Installing all components.<br>
InstallingComponents was successful.</p>
<p>ELASTIX version: 4.900<br>
Command line options from ElastixBase:<br>
-f        /var/folders/rm/z7mv0dx968j37d7g4ywm43b80000gn/T/Slicer-drpree/Elastix/20200130_135241_078/input/fixed.mha<br>
-m        /var/folders/rm/z7mv0dx968j37d7g4ywm43b80000gn/T/Slicer-drpree/Elastix/20200130_135241_078/input/moving.mha<br>
-fMask    unspecified, so no fixed mask used<br>
-mMask    unspecified, so no moving mask used<br>
-out      /var/folders/rm/z7mv0dx968j37d7g4ywm43b80000gn/T/Slicer-drpree/Elastix/20200130_135241_078/result-transform/<br>
-p        /Users/drpree/Downloads/Slicer.app/Contents/Extensions-27970/SlicerElastix/lib/Slicer-4.11/qt-scripted-modules/Resources/RegistrationParameters/Parameters_Rigid.txt<br>
-p        /Users/drpree/Downloads/Slicer.app/Contents/Extensions-27970/SlicerElastix/lib/Slicer-4.11/qt-scripted-modules/Resources/RegistrationParameters/Parameters_BSpline.txt<br>
-threads  unspecified, so all available threads are used<br>
WARNING: The parameter “UseDirectionCosines”, requested at entry number 0, does not exist at all.<br>
The default value “true” is used instead.</p>
<p>WARNING: The option “UseDirectionCosines” was not found in your parameter file.<br>
From elastix 4.8 it defaults to true!<br>
This may change the behavior of your registrations considerably.</p>
<p>Command line options from TransformBase:<br>
-t0       unspecified, so no initial transform used</p>
<p>Reading images…<br>
Reading images took 230 ms.</p>
<p>WARNING: the fixed pyramid schedule is not fully specified!<br>
A default pyramid schedule is used.<br>
WARNING: the moving pyramid schedule is not fully specified!<br>
A default pyramid schedule is used.<br>
WARNING: The parameter “AutomaticTransformInitializationMethod”, requested at entry number 0, does not exist at all.<br>
The default value “GeometricalCenter” is used instead.<br>
Transform parameters are initialized as: [0, 0, 0, 0.3627215474843979, -104.6372784525156, -27.999998092651353]<br>
Scales are estimated automatically.<br>
Scales for transform parameters are: [38942.372131347656, 38942.372131347656, 63034.744262695305, 1, 1, 1]<br>
Initialization of all components (before registration) took: 7 ms.<br>
Preparation of the image pyramids took: 1344 ms.</p>
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
The default value “0.809152” is used instead.<br>
WARNING: The parameter “NumberOfGradientMeasurements”, requested at entry number 0, does not exist at all.<br>
The default value “0” is used instead.<br>
WARNING: The parameter “NumberOfJacobianMeasurements”, requested at entry number 0, does not exist at all.<br>
The default value “1000” is used instead.<br>
WARNING: The parameter “NumberOfSamplesForExactGradient”, requested at entry number 0, does not exist at all.<br>
The default value “100000” is used instead.<br>
WARNING: The parameter “SigmoidScaleFactor”, requested at entry number 0, does not exist at all.<br>
The default value “0.1” is used instead.<br>
Elastix initialization of all components (for this resolution) took: 30 ms.<br>
Computing the fixed image extrema took 0 ms.<br>
Computing the moving image extrema took 0 ms.<br>
Initialization of AdvancedMattesMutualInformation metric took: 57 ms.<br>
Starting automatic parameter estimation for AdaptiveStochasticGradientDescent …<br>
WARNING: The parameter “ASGDParameterEstimationMethod”, requested at entry number 0, does not exist at all.<br>
The default value “Original” is used instead.<br>
Computing JacobianTerms …<br>
Computing the Jacobian terms took 0.001056s<br>
NumberOfGradientMeasurements to estimate sigma_i: 6<br>
Sampling gradients …</p>
<p>Progress: 0%Time spent in resolution 0 (ITK initialization and iterating): 0.174 s.<br>
Stopping condition: Error in metric.<br>
Settings of AdaptiveStochasticGradientDescent in resolution 0:<br>
( SP_a 1.000000 )<br>
( SP_A 20.000000 )<br>
( SP_alpha 0.602000 )<br>
( SigmoidMax 1.000000 )<br>
( SigmoidMin -0.800000 )<br>
( SigmoidScale 0.000000 )</p>
<p>itk::ExceptionObject (0x7fb824102cc0)<br>
Location: “ElastixTemplate - Run()”<br>
File: /Volumes/Dashboards/Preview/S-0-E-b/SlicerElastix-build/elastix/Common/CostFunctions/itkAdvancedImageToImageMetric.hxx<br>
Line: 1018<br>
Description: itk::ERROR: AdvancedMattesMutualInformationMetric(0x7fb824842e00): Too many samples map outside moving image buffer: 10108 / 69632</p>
<p>Error occurred during actual registration.</p>
<p>Errors occurred!<br>
vtkDebugLeaks has found no leaks.</p>
<p>Error:</p>

---

## Post #2 by @lassoan (2020-01-30 14:43 UTC)

<aside class="quote no-group" data-username="RadioQuest" data-post="1" data-topic="10026">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/85f322/48.png" class="avatar"> RadioQuest:</div>
<blockquote>
<p>Too many samples map outside moving image buffer: 10108 / 69632</p>
</blockquote>
</aside>
<p>This happens when the two input volumes don’t overlap enough.</p>
<p>I would recommend doing an approximate landmark registration with 3-4 landmarks points to somewhat align the images before fully automatic registration.</p>
<p>If your images have approximately the same orientation and only their position differs significantly then you may enable Elastix’ builtin transform initialization by editing the parameter files (see section “5.5.2 Bad initial alignment” in <a href="http://elastix.isi.uu.nl/doxygen/index.html">Elastix manual</a>).</p>

---
