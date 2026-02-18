# Error: Command 'elastix' returned non-zero exit status 3221225477

**Topic ID**: 22374
**Date**: 2022-03-08
**URL**: https://discourse.slicer.org/t/error-command-elastix-returned-non-zero-exit-status-3221225477/22374

---

## Post #1 by @Roman (2022-03-08 15:04 UTC)

<p>Operating system: win10<br>
Slicer version: 4.11.20210226 r29738 / 7a593c8<br>
Expected behavior: elastix completes the job without an error code and the result makes sense<br>
Actual behavior: Error: Command ‘elastix’ returned non-zero exit status 3221225477; entry Volume is created in the Subject hierarchy but does not save and looks like a frozen slices in 3 projections.</p>
<p>No error msgs in the log (see below). Sufficient overlap of the images at the start. The same routine worked well for about 15…20 different cases previously. Restarting Slicer does not solve the issue.</p>
<p>I’ll appreciate an advice how to solve.</p>
<p>Kind regasrd,<br>
Roman</p>
<pre><code class="lang-auto">Volume registration is started in working directory: 

C:/Users/usrv/AppData/Local/Temp/Slicer/Elastix/20220307_142012_545
Register volumes...

elastix is started at Mon Mar  7 14:20:13 2022.

which elastix:   C:\Users\usrv\AppData\Local\NA-MIC\Slicer 4.11.20210226\NA-MIC\Extensions-29738\SlicerElastix\lib\Slicer-4.11\elastix.exe
elastix runs at: win-lap-rr
  Windows  Professional (x64),  (Build 9200)
  with 16266 MB memory, and 4 cores @ 2903 MHz.
-------------------------------------------------------------------------

Running elastix with parameter file 0: "C:\Users\usrv\AppData\Local\NA-MIC\Slicer 4.11.20210226\NA-MIC\Extensions-29738\SlicerElastix\lib\Slicer-4.11\qt-scripted-modules\Resources\RegistrationParameters\Par0000affine.txt".

Current time: Mon Mar  7 14:20:13 2022.
Reading the elastix parameters from file ...

Installing all components.
InstallingComponents was successful.

ELASTIX version: 5.0.1
Command line options from ElastixBase:
-f        C:/Users/usrv/AppData/Local/Temp/Slicer/Elastix/20220307_142012_545\input\fixed.mha
-m        C:/Users/usrv/AppData/Local/Temp/Slicer/Elastix/20220307_142012_545\input\moving.mha
-fMask    unspecified, so no fixed mask used
-mMask    unspecified, so no moving mask used
-out      C:\Users\usrv\AppData\Local\Temp\Slicer\Elastix\20220307_142012_545\result-transform\
-p        C:\Users\usrv\AppData\Local\NA-MIC\Slicer 4.11.20210226\NA-MIC\Extensions-29738\SlicerElastix\lib\Slicer-4.11\qt-scripted-modules\Resources\RegistrationParameters\Par0000affine.txt
-p        C:\Users\usrv\AppData\Local\NA-MIC\Slicer 4.11.20210226\NA-MIC\Extensions-29738\SlicerElastix\lib\Slicer-4.11\qt-scripted-modules\Resources\RegistrationParameters\Par0000bspline.txt
-priority unspecified, so NORMAL process priority
-threads  unspecified, so all available threads are used
WARNING: The parameter "UseDirectionCosines", requested at entry number 0, does not exist at all.
  The default value "true" is used instead.

WARNING: The option "UseDirectionCosines" was not found in your parameter file.
  From elastix 4.8 it defaults to true!
This may change the behavior of your registrations considerably.

Command line options from TransformBase:
-t0       unspecified, so no initial transform used

Reading images...
Reading images took 189 ms.

WARNING: the fixed pyramid schedule is not fully specified!
  A default pyramid schedule is used.
WARNING: the moving pyramid schedule is not fully specified!
  A default pyramid schedule is used.
WARNING: The parameter "AutomaticTransformInitializationMethod", requested at entry number 0, does not exist at all.
  The default value "GeometricalCenter" is used instead.
Transform parameters are initialized as: [1, 0, 0, 0, 1, 0, 0, 0, 1, 2.1476159631866807, 11.1266446975971, 15.661047257294836]
InitializeTransform took 0.00s
Scales are estimated automatically.
Scales for transform parameters are: [5797.496715913637, 3988.8843459514082, 5436.911941693003, 5797.496715913637, 3988.8843459514082, 5436.911941693003, 5797.496715913637, 3988.8843459514082, 5436.911941693003, 1, 1, 1]
Initialization of all components (before registration) took: 7 ms.
Preparation of the image pyramids took: 2611 ms.

Resolution: 0
WARNING: The parameter "UseMultiThreadingForMetrics", requested at entry number 0, does not exist at all.
  The default value "true" is used instead.
Setting the fixed masks took: 0 ms.
Setting the moving masks took: 0 ms.
WARNING: The parameter "NumberOfFixedHistogramBins", requested at entry number 0, does not exist at all.
  The default value "32" is used instead.
WARNING: The parameter "NumberOfMovingHistogramBins", requested at entry number 0, does not exist at all.
  The default value "32" is used instead.
WARNING: The parameter "UseFastAndLowMemoryVersion", requested at entry number 0, does not exist at all.
  The default value "true" is used instead.
WARNING: The parameter "UseJacobianPreconditioning", requested at entry number 0, does not exist at all.
  The default value "false" is used instead.
WARNING: The parameter "FiniteDifferenceDerivative", requested at entry number 0, does not exist at all.
  The default value "false" is used instead.

WARNING: You have set MaximumNumberOfSamplingAttempts to 10.
  This functionality is known to cause problems (stack overflow) for large values.
  If elastix stops or segfaults for no obvious reason, reduce this value.
  You may select the RandomSparseMask image sampler to fix mask-related problems.

WARNING: The parameter "SigmoidInitialTime", requested at entry number 0, does not exist at all.
  The default value "0" is used instead.
WARNING: The parameter "MaxBandCovSize", requested at entry number 0, does not exist at all.
  The default value "192" is used instead.
WARNING: The parameter "NumberOfBandStructureSamples", requested at entry number 0, does not exist at all.
  The default value "10" is used instead.
WARNING: The parameter "UseAdaptiveStepSizes", requested at entry number 0, does not exist at all.
  The default value "true" is used instead.
WARNING: The parameter "AutomaticParameterEstimation", requested at entry number 0, does not exist at all.
  The default value "true" is used instead.
WARNING: The parameter "UseConstantStep", requested at entry number 0, does not exist at all.
  The default value "false" is used instead.
WARNING: The parameter "MaximumStepLengthRatio", requested at entry number 0, does not exist at all.
  The default value "1" is used instead.
WARNING: The parameter "MaximumStepLength", requested at entry number 0, does not exist at all.
  The default value "0.711268" is used instead.
WARNING: The parameter "NumberOfGradientMeasurements", requested at entry number 0, does not exist at all.
  The default value "0" is used instead.
WARNING: The parameter "NumberOfJacobianMeasurements", requested at entry number 0, does not exist at all.
  The default value "1000" is used instead.
WARNING: The parameter "NumberOfSamplesForExactGradient", requested at entry number 0, does not exist at all.
  The default value "100000" is used instead.
WARNING: The parameter "SigmoidScaleFactor", requested at entry number 0, does not exist at all.
  The default value "0.1" is used instead.
Elastix initialization of all components (for this resolution) took: 8 ms.
  Computing the fixed image extrema took 25 ms.
  Computing the moving image extrema took 58 ms.
Initialization of AdvancedMattesMutualInformation metric took: 921 ms.
Starting automatic parameter estimation for AdaptiveStochasticGradientDescent ...
WARNING: The parameter "ASGDParameterEstimationMethod", requested at entry number 0, does not exist at all.
  The default value "Original" is used instead.
  Computing JacobianTerms ...
  Computing the Jacobian terms took 0.001714s
  NumberOfGradientMeasurements to estimate sigma_i: 3
  Sampling gradients ...

  Progress: 100%  Sampling the gradients took 0.093331s
Automatic parameter estimation took 0.10s
1:ItNr	2:Metric	3a:Time	3b:StepSize	4:||Gradient||	Time[ms]
0	-0.406891	0.000000	9.324989	0.021714	1018.3
499	-0.905263	77.574939	1.986557	0.007577	1.2
Time spent in resolution 0 (ITK initialization and iterating): 1.668 s.
Stopping condition: Maximum number of iterations has been reached.
Settings of AdaptiveStochasticGradientDescent in resolution 0:
( SP_a 195.824766 )
( SP_A 20.000000 )
( SP_alpha 1.000000 )
( SigmoidMax 1.000000 )
( SigmoidMin -0.425486 )
( SigmoidScale 0.000006 )


Resolution: 1
WARNING: The parameter "UseMultiThreadingForMetrics", requested at entry number 1, does not exist at all.
  The default value "true" is used instead.
Setting the fixed masks took: 0 ms.
Setting the moving masks took: 0 ms.
WARNING: The parameter "NumberOfFixedHistogramBins", requested at entry number 1, does not exist at all.
  The default value "32" is used instead.
WARNING: The parameter "NumberOfMovingHistogramBins", requested at entry number 1, does not exist at all.
  The default value "32" is used instead.
WARNING: The parameter "UseFastAndLowMemoryVersion", requested at entry number 1, does not exist at all.
  The default value "true" is used instead.
WARNING: The parameter "UseJacobianPreconditioning", requested at entry number 1, does not exist at all.
  The default value "false" is used instead.
WARNING: The parameter "FiniteDifferenceDerivative", requested at entry number 1, does not exist at all.
  The default value "false" is used instead.

WARNING: You have set MaximumNumberOfSamplingAttempts to 10.
  This functionality is known to cause problems (stack overflow) for large values.
  If elastix stops or segfaults for no obvious reason, reduce this value.
  You may select the RandomSparseMask image sampler to fix mask-related problems.

WARNING: The parameter "SigmoidInitialTime", requested at entry number 1, does not exist at all.
  The default value "0" is used instead.
WARNING: The parameter "MaxBandCovSize", requested at entry number 1, does not exist at all.
  The default value "192" is used instead.
WARNING: The parameter "NumberOfBandStructureSamples", requested at entry number 1, does not exist at all.
  The default value "10" is used instead.
WARNING: The parameter "UseAdaptiveStepSizes", requested at entry number 1, does not exist at all.
  The default value "true" is used instead.
WARNING: The parameter "AutomaticParameterEstimation", requested at entry number 1, does not exist at all.
  The default value "true" is used instead.
WARNING: The parameter "UseConstantStep", requested at entry number 1, does not exist at all.
  The default value "false" is used instead.
WARNING: The parameter "MaximumStepLengthRatio", requested at entry number 1, does not exist at all.
  The default value "1" is used instead.
WARNING: The parameter "MaximumStepLength", requested at entry number 1, does not exist at all.
  The default value "0.711268" is used instead.
WARNING: The parameter "NumberOfGradientMeasurements", requested at entry number 1, does not exist at all.
  The default value "0" is used instead.
WARNING: The parameter "NumberOfJacobianMeasurements", requested at entry number 1, does not exist at all.
  The default value "1000" is used instead.
WARNING: The parameter "NumberOfSamplesForExactGradient", requested at entry number 1, does not exist at all.
  The default value "100000" is used instead.
WARNING: The parameter "SigmoidScaleFactor", requested at entry number 1, does not exist at all.
  The default value "0.1" is used instead.
Elastix initialization of all components (for this resolution) took: 5 ms.
  Computing the fixed image extrema took 28 ms.
  Computing the moving image extrema took 57 ms.
Initialization of AdvancedMattesMutualInformation metric took: 796 ms.
Starting automatic parameter estimation for AdaptiveStochasticGradientDescent ...
WARNING: The parameter "ASGDParameterEstimationMethod", requested at entry number 0, does not exist at all.
  The default value "Original" is used instead.
  Computing JacobianTerms ...
  Computing the Jacobian terms took 0.001510s
  NumberOfGradientMeasurements to estimate sigma_i: 3
  Sampling gradients ...

  Progress: 100%  Sampling the gradients took 0.094170s
Automatic parameter estimation took 0.10s
1:ItNr	2:Metric	3a:Time	3b:StepSize	4:||Gradient||	Time[ms]
0	-0.819623	0.000000	5.730569	0.016572	893.8
1	-0.817330	0.000000	5.730569	0.026268	1.3
499	-0.775099	170.116731	0.629678	0.027961	1.2
Time spent in resolution 1 (ITK initialization and iterating): 1.533 s.
Stopping condition: Maximum number of iterations has been reached.
Settings of AdaptiveStochasticGradientDescent in resolution 1:
( SP_a 120.341959 )
( SP_A 20.000000 )
( SP_alpha 1.000000 )
( SigmoidMax 1.000000 )
( SigmoidMin -0.348804 )
( SigmoidScale 0.000014 )


Resolution: 2
WARNING: The parameter "UseMultiThreadingForMetrics", requested at entry number 2, does not exist at all.
  The default value "true" is used instead.
Setting the fixed masks took: 0 ms.
Setting the moving masks took: 0 ms.
WARNING: The parameter "NumberOfFixedHistogramBins", requested at entry number 2, does not exist at all.
  The default value "32" is used instead.
WARNING: The parameter "NumberOfMovingHistogramBins", requested at entry number 2, does not exist at all.
  The default value "32" is used instead.
WARNING: The parameter "UseFastAndLowMemoryVersion", requested at entry number 2, does not exist at all.
  The default value "true" is used instead.
WARNING: The parameter "UseJacobianPreconditioning", requested at entry number 2, does not exist at all.
  The default value "false" is used instead.
WARNING: The parameter "FiniteDifferenceDerivative", requested at entry number 2, does not exist at all.
  The default value "false" is used instead.

WARNING: You have set MaximumNumberOfSamplingAttempts to 10.
  This functionality is known to cause problems (stack overflow) for large values.
  If elastix stops or segfaults for no obvious reason, reduce this value.
  You may select the RandomSparseMask image sampler to fix mask-related problems.

WARNING: The parameter "SigmoidInitialTime", requested at entry number 2, does not exist at all.
  The default value "0" is used instead.
WARNING: The parameter "MaxBandCovSize", requested at entry number 2, does not exist at all.
  The default value "192" is used instead.
WARNING: The parameter "NumberOfBandStructureSamples", requested at entry number 2, does not exist at all.
  The default value "10" is used instead.
WARNING: The parameter "UseAdaptiveStepSizes", requested at entry number 2, does not exist at all.
  The default value "true" is used instead.
WARNING: The parameter "AutomaticParameterEstimation", requested at entry number 2, does not exist at all.
  The default value "true" is used instead.
WARNING: The parameter "UseConstantStep", requested at entry number 2, does not exist at all.
  The default value "false" is used instead.
WARNING: The parameter "MaximumStepLengthRatio", requested at entry number 2, does not exist at all.
  The default value "1" is used instead.
WARNING: The parameter "MaximumStepLength", requested at entry number 2, does not exist at all.
  The default value "0.711268" is used instead.
WARNING: The parameter "NumberOfGradientMeasurements", requested at entry number 2, does not exist at all.
  The default value "0" is used instead.
WARNING: The parameter "NumberOfJacobianMeasurements", requested at entry number 2, does not exist at all.
  The default value "1000" is used instead.
WARNING: The parameter "NumberOfSamplesForExactGradient", requested at entry number 2, does not exist at all.
  The default value "100000" is used instead.
WARNING: The parameter "SigmoidScaleFactor", requested at entry number 2, does not exist at all.
  The default value "0.1" is used instead.
Elastix initialization of all components (for this resolution) took: 4 ms.
  Computing the fixed image extrema took 39 ms.
  Computing the moving image extrema took 83 ms.
Initialization of AdvancedMattesMutualInformation metric took: 829 ms.
Starting automatic parameter estimation for AdaptiveStochasticGradientDescent ...
WARNING: The parameter "ASGDParameterEstimationMethod", requested at entry number 0, does not exist at all.
  The default value "Original" is used instead.
  Computing JacobianTerms ...
  Computing the Jacobian terms took 0.001470s
  NumberOfGradientMeasurements to estimate sigma_i: 3
  Sampling gradients ...

  Progress: 100%  Sampling the gradients took 0.103908s
Automatic parameter estimation took 0.11s
1:ItNr	2:Metric	3a:Time	3b:StepSize	4:||Gradient||	Time[ms]
0	-0.784162	0.000000	3.981186	0.044915	936.4
1	-0.795454	0.000000	3.981186	0.032977	1.2
499	-0.815347	154.061447	0.477575	0.041381	1.1
Time spent in resolution 2 (ITK initialization and iterating): 1.590 s.
Stopping condition: Maximum number of iterations has been reached.
Settings of AdaptiveStochasticGradientDescent in resolution 2:
( SP_a 83.604913 )
( SP_A 20.000000 )
( SP_alpha 1.000000 )
( SigmoidMax 1.000000 )
( SigmoidMin -0.467668 )
( SigmoidScale 0.000031 )


Resolution: 3
WARNING: The parameter "UseMultiThreadingForMetrics", requested at entry number 3, does not exist at all.
  The default value "true" is used instead.
Setting the fixed masks took: 0 ms.
Setting the moving masks took: 0 ms.
WARNING: The parameter "NumberOfFixedHistogramBins", requested at entry number 3, does not exist at all.
  The default value "32" is used instead.
WARNING: The parameter "NumberOfMovingHistogramBins", requested at entry number 3, does not exist at all.
  The default value "32" is used instead.
WARNING: The parameter "UseFastAndLowMemoryVersion", requested at entry number 3, does not exist at all.
  The default value "true" is used instead.
WARNING: The parameter "UseJacobianPreconditioning", requested at entry number 3, does not exist at all.
  The default value "false" is used instead.
WARNING: The parameter "FiniteDifferenceDerivative", requested at entry number 3, does not exist at all.
  The default value "false" is used instead.

WARNING: You have set MaximumNumberOfSamplingAttempts to 10.
  This functionality is known to cause problems (stack overflow) for large values.
  If elastix stops or segfaults for no obvious reason, reduce this value.
  You may select the RandomSparseMask image sampler to fix mask-related problems.

WARNING: The parameter "SigmoidInitialTime", requested at entry number 3, does not exist at all.
  The default value "0" is used instead.
WARNING: The parameter "MaxBandCovSize", requested at entry number 3, does not exist at all.
  The default value "192" is used instead.
WARNING: The parameter "NumberOfBandStructureSamples", requested at entry number 3, does not exist at all.
  The default value "10" is used instead.
WARNING: The parameter "UseAdaptiveStepSizes", requested at entry number 3, does not exist at all.
  The default value "true" is used instead.
WARNING: The parameter "AutomaticParameterEstimation", requested at entry number 3, does not exist at all.
  The default value "true" is used instead.
WARNING: The parameter "UseConstantStep", requested at entry number 3, does not exist at all.
  The default value "false" is used instead.
WARNING: The parameter "MaximumStepLengthRatio", requested at entry number 3, does not exist at all.
  The default value "1" is used instead.
WARNING: The parameter "MaximumStepLength", requested at entry number 3, does not exist at all.
  The default value "0.711268" is used instead.
WARNING: The parameter "NumberOfGradientMeasurements", requested at entry number 3, does not exist at all.
  The default value "0" is used instead.
WARNING: The parameter "NumberOfJacobianMeasurements", requested at entry number 3, does not exist at all.
  The default value "1000" is used instead.
WARNING: The parameter "NumberOfSamplesForExactGradient", requested at entry number 3, does not exist at all.
  The default value "100000" is used instead.
WARNING: The parameter "SigmoidScaleFactor", requested at entry number 3, does not exist at all.
  The default value "0.1" is used instead.
Elastix initialization of all components (for this resolution) took: 5 ms.
  Computing the fixed image extrema took 39 ms.
  Computing the moving image extrema took 81 ms.
Initialization of AdvancedMattesMutualInformation metric took: 822 ms.
Starting automatic parameter estimation for AdaptiveStochasticGradientDescent ...
WARNING: The parameter "ASGDParameterEstimationMethod", requested at entry number 0, does not exist at all.
  The default value "Original" is used instead.
  Computing JacobianTerms ...
  Computing the Jacobian terms took 0.001645s
  NumberOfGradientMeasurements to estimate sigma_i: 3
  Sampling gradients ...

  Progress: 100%  Sampling the gradients took 0.104218s
Automatic parameter estimation took 0.11s
1:ItNr	2:Metric	3a:Time	3b:StepSize	4:||Gradient||	Time[ms]
0	-0.724236	0.000000	2.499108	0.050914	929.5
1	-0.713829	0.000000	2.499108	0.052878	1.2
2	-0.776407	1.000000	2.385512	0.039460	1.3
3	-0.686208	1.947181	2.287046	0.061353	1.2
499	-0.682485	99.771879	0.434549	0.047134	1.3
Time spent in resolution 3 (ITK initialization and iterating): 1.574 s.
Stopping condition: Maximum number of iterations has been reached.
Settings of AdaptiveStochasticGradientDescent in resolution 3:
( SP_a 52.481268 )
( SP_A 20.000000 )
( SP_alpha 1.000000 )
( SigmoidMax 1.000000 )
( SigmoidMin -0.687876 )
( SigmoidScale 0.000068 )



Creating the TransformParameterFile took 0.01s

Registration result checksum: 3184531648

Skipping applying final transform, no resulting output image generated.

Final metric value  = -0.682485
Settings of AdaptiveStochasticGradientDescent for all resolutions:
( SP_a 195.824766 120.341959 83.604913 52.481268 )
( SP_A 20.000000 20.000000 20.000000 20.000000 )
( SP_alpha 1.000000 1.000000 1.000000 1.000000 )
( SigmoidMax 1.000000 1.000000 1.000000 1.000000 )
( SigmoidMin -0.425486 -0.348804 -0.467668 -0.687876 )
( SigmoidScale 0.000006 0.000014 0.000031 0.000068 )

Time spent on saving the results, applying the final transform etc.: 6 ms.
Running elastix with parameter file 0: "C:\Users\usrv\AppData\Local\NA-MIC\Slicer 4.11.20210226\NA-MIC\Extensions-29738\SlicerElastix\lib\Slicer-4.11\qt-scripted-modules\Resources\RegistrationParameters\Par0000affine.txt", has finished.


Current time: Mon Mar  7 14:20:22 2022.
Time used for running elastix with this parameter file:
  9.2s.

-------------------------------------------------------------------------

Running elastix with parameter file 1: "C:\Users\usrv\AppData\Local\NA-MIC\Slicer 4.11.20210226\NA-MIC\Extensions-29738\SlicerElastix\lib\Slicer-4.11\qt-scripted-modules\Resources\RegistrationParameters\Par0000bspline.txt".

Current time: Mon Mar  7 14:20:22 2022.
Reading the elastix parameters from file ...

ELASTIX version: 5.0.1
Command line options from ElastixBase:
-f        C:/Users/usrv/AppData/Local/Temp/Slicer/Elastix/20220307_142012_545\input\fixed.mha
-m        C:/Users/usrv/AppData/Local/Temp/Slicer/Elastix/20220307_142012_545\input\moving.mha
-fMask    unspecified, so no fixed mask used
-mMask    unspecified, so no moving mask used
-out      C:\Users\usrv\AppData\Local\Temp\Slicer\Elastix\20220307_142012_545\result-transform\
-p        C:\Users\usrv\AppData\Local\NA-MIC\Slicer 4.11.20210226\NA-MIC\Extensions-29738\SlicerElastix\lib\Slicer-4.11\qt-scripted-modules\Resources\RegistrationParameters\Par0000affine.txt
-p        C:\Users\usrv\AppData\Local\NA-MIC\Slicer 4.11.20210226\NA-MIC\Extensions-29738\SlicerElastix\lib\Slicer-4.11\qt-scripted-modules\Resources\RegistrationParameters\Par0000bspline.txt
-priority unspecified, so NORMAL process priority
-threads  unspecified, so all available threads are used
WARNING: The parameter "UseDirectionCosines", requested at entry number 0, does not exist at all.
  The default value "true" is used instead.

WARNING: The option "UseDirectionCosines" was not found in your parameter file.
  From elastix 4.8 it defaults to true!
This may change the behavior of your registrations considerably.

Command line options from TransformBase:
-t0       unspecified, so no initial transform used
WARNING: The parameter "BSplineTransformSplineOrder", requested at entry number 0, does not exist at all.
  The default value "3" is used instead.
WARNING: The parameter "UseCyclicTransform", requested at entry number 0, does not exist at all.
  The default value "false" is used instead.

Reading images...
Reading images took 0 ms.

WARNING: the fixed pyramid schedule is not fully specified!
  A default pyramid schedule is used.
WARNING: the moving pyramid schedule is not fully specified!
  A default pyramid schedule is used.
Initialization of all components (before registration) took: 14 ms.
Preparation of the image pyramids took: 3251 ms.

Resolution: 0
WARNING: The parameter "UseMultiThreadingForMetrics", requested at entry number 0, does not exist at all.
  The default value "true" is used instead.
Setting the fixed masks took: 0 ms.
Setting the moving masks took: 0 ms.
WARNING: The parameter "NumberOfFixedHistogramBins", requested at entry number 0, does not exist at all.
  The default value "32" is used instead.
WARNING: The parameter "NumberOfMovingHistogramBins", requested at entry number 0, does not exist at all.
  The default value "32" is used instead.
WARNING: The parameter "UseJacobianPreconditioning", requested at entry number 0, does not exist at all.
  The default value "false" is used instead.
WARNING: The parameter "FiniteDifferenceDerivative", requested at entry number 0, does not exist at all.
  The default value "false" is used instead.

WARNING: You have set MaximumNumberOfSamplingAttempts to 10.
  This functionality is known to cause problems (stack overflow) for large values.
  If elastix stops or segfaults for no obvious reason, reduce this value.
  You may select the RandomSparseMask image sampler to fix mask-related problems.

Elastix initialization of all components (for this resolution) took: 6 ms.
  Computing the fixed image extrema took 53 ms.
  Computing the moving image extrema took 90 ms.
Initialization of AdvancedMattesMutualInformation metric took: 930 ms.
1:ItNr	2:Metric	3:StepSize	4:||Gradient||	Time[ms]
0	-0.000000	627.201626	0.000000	935.9
1	-1.404256	623.504937	0.012287	9.1
263	-1.223687	290.629149	0.024444	3.4

Error: Command 'elastix' returned non-zero exit status 3221225477.
</code></pre>

---

## Post #2 by @lassoan (2022-03-08 18:57 UTC)

<aside class="quote no-group" data-username="Roman" data-post="1" data-topic="22374">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/roman/48/14584_2.png" class="avatar"> Roman:</div>
<blockquote>
<p><code>3221225477</code></p>
</blockquote>
</aside>
<p>This error code (in hex: 0xC0000005) means memory access violation. If the same Slicer version + SlicerElastix worked on the same data before then one potential root cause of the problem is that you installed another Elastix or any other software that uses ITK and that placed files in folders that are in your PATH.</p>
<p>If the registration works for many other cases and only fails for this data set then check what is different compared to the others. Is the data set significantly larger, uses a different voxel type, etc. compared to the others?</p>

---
