---
topic_id: 83
title: "Adc Map Registration From Slicer Users"
date: 2017-04-12
url: https://discourse.slicer.org/t/83
---

# "ADC map registration" (from slicer-users)

**Topic ID**: 83
**Date**: 2017-04-12
**URL**: https://discourse.slicer.org/t/adc-map-registration-from-slicer-users/83

---

## Post #1 by @ihnorton (2017-04-12 13:50 UTC)

<p><a href="http://slicer-users.65878.n3.nabble.com/ADC-map-registration-td4032173.html">From slicer-users</a></p>
<pre><code class="lang-auto">Dear Slicer users,

I'm using Brainsfit to register ADC maps. I scanned 5 times to the same
volunteer in order to obtain the repatability of these maps.

Even using immobilizer small movements and rotations appear so I need to
register all the images. Since the slice thickness is 5 mm for those ADC
maps I suppose that I cannot expect very good results from the registering
process.

A T1 weighted image with 1 mm3  per voxel was scanned in the same session
(to be used for freesurfer) so I tried to use it as fixed image in my second
attempt instead of the first ADC map.

I used rigid rotations but the results that I obtained seemed like needing
an additional BSpline non rigid registration. I used MSE for the first
attemp and MMI for the second one with the structural image as fixed one.

Since the results do no seem to be as good as I expected, do any of you have
experience enough to tell me if these parameters are correct?

                 '--maskProcessingMode ROI',
                 '--fixedBinaryVolume mask.nii.gz --movingBinaryVolume
mask.nii.gz',
                 '--useRigid --use BSpline',
                 '--samplingPercentage 0.05 --initializeTransformMode Off',
                 '--splineGridSize 4,4,4 --maxBSplineDisplacement 10',
                 '--medianFilterSize 0,0,0 --removeIntensityOutliers 0
--outputVolumePixelType int',
                 '--backgroundFillValue 0 --interpolationMode WindowedSinc',
                 '--numberOfIterations 1500 --maximumStepLength 0.5
--minimumStepLength 0.001',
                 '--relaxationFactor 0.5 --translationScale 1000',
                 ' --reproportionScale 1 --skewScale 1',
                 '--numberOfHistogramBins 50 --numberOfMatchPoints 10',
                 '--costMetric MMI',  #MSE for ADC/ADC
                 '--ROIAutoDilateSize 0 --ROIAutoClosingSize 9',
                 '--costFunctionConvergenceFactor 1000
--projectedGradientTolerance 0.0001',
                 '--maximumNumberOfEvaluations 900
--maximumNumberOfCorrections 25',
                 '--metricSamplingStrategy Random',
                 '--fixedVolumeTimeIndex 0 --movingVolumeTimeIndex 0',
                 '--maskInferiorCutOffFromCenter 1000  --numberOfSamples 0
--failureExitCode -1 --numberOfThreads -1',
                 '--debugLevel 0 --echo'

Rigid registration finished after 35-40 iterations and non-rigid
registration used around 25 iterations.

Do any of you have any suggestion about these parameters?

Thank you in advance.

Félix.
</code></pre>

---

## Post #2 by @ihnorton (2017-04-12 13:53 UTC)

<p>Hi Felix,</p>
<p>A couple questions/suggestions:</p>
<ul>
<li>does it work better without ROI/mask? I’ve never had to use those, at least for MR.</li>
<li>increase the <code>--samplingPercentage</code>
</li>
<li>how are you evaluating the registration? Do you have a side-by-side comparison that you consider to be bad?</li>
</ul>

---

## Post #3 by @fedorov (2017-04-12 14:01 UTC)

<p>Felix,</p>
<p>what is the organ being imaged?</p>
<p>A challenge with applying deformable registration, particularly in the context of evaluating repeatability, is that you will not be able to separate the inherent measurement differences from those caused by the imperfect registration (and your registration will never be perfect).</p>
<p>If I were you, I would start with evaluation of repeatability of the mean signal over a region that can be more or less reliably identified in each of these scans, and also consider what is the clinical problem these images are intended to address.</p>
<p>AF</p>

---

## Post #4 by @Felix_Navarro_Guirad (2017-04-17 19:54 UTC)

<p>Dear Andrey and Isaiah, thank you very much for your replies.</p>
<p>I’m trying to evaluate the registration of the ADC maps of the brain. I’m evaluating the result sliding the alpha blend slider on slicer GUI. As far as I’ve seen in the examples, somewhere in the wiki, I expected better results.</p>
<p>If I don’t use ROI mask  the B-Spline registration seems to work worse. Increasing the sampling percentage does not seem to improve the result, thanks for the tip.</p>
<p>I think that the registration process is needed because regions where repeatability is evaluated are the results of freesurfer segmentation of T1 weighted image. It seems to me that I need to register the ADC maps (1x1x5 mm3) over T1 weighted image (1x1x1 mm3) source of those regions.</p>
<p>If I move the T1w to ADC maps I could not evaluate if the result of the registration moves the regions to the same place in the ADC maps, but if I do the opposite I can compare all the registered ADC maps. Maybe, finally I can apply the inverse transformation to the regions so they move to the original ADC maps, but first I need to evaluate the result of the registration.</p>
<p>Would you change any other parameter ? I.e. I’m not sure if 4,4,4 is a good value for the spline grid size.</p>

---

## Post #5 by @fedorov (2017-04-19 03:48 UTC)

<aside class="quote no-group" data-username="Felix_Navarro_Guirad" data-post="4" data-topic="83">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/4491bb/48.png" class="avatar"> Felix_Navarro_Guirad:</div>
<blockquote>
<p>If I move the T1w to ADC maps I could not evaluate if the result of the registration moves the regions to the same place in the ADC maps, but if I do the opposite I can compare all the registered ADC maps.</p>
</blockquote>
</aside>
<p>Felix, I do not understand what you are trying to say here. Considering the differences in resolution, it makes sense to have T1 as moving image.</p>
<p>You could also consider registering b0 image instead of the ADC map (usually, you have the diffusion images as a separate series alongside the ADC series), and then apply the transformation to ADC. Do you have the diffusion b0 image, did you try this?</p>
<aside class="quote no-group" data-username="Felix_Navarro_Guirad" data-post="4" data-topic="83">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/4491bb/48.png" class="avatar"> Felix_Navarro_Guirad:</div>
<blockquote>
<p>Would you change any other parameter ? I.e. I’m not sure if 4,4,4 is a good value for the spline grid size.</p>
</blockquote>
</aside>
<p>You can definitely experiment with the grid size. It depends on the nature of deformation you observe. If you include a screenshot illustrating the problem, it might help.</p>

---

## Post #6 by @Felix_Navarro_Guirad (2017-04-19 14:55 UTC)

<p>Thank you Andrey for your support.</p>
<p>Finally I took your advice and registered T1w to b0 image, this didn’t corrected Eddy distortion but since I’m computing statistic for regions this procedure should be good enough .</p>
<p>As you suggested the result for the initial procedure was better if 7x7x4 was used for the spline grid size since voxels are not isotropic.</p>
<p>Thank you very much for your advices.</p>

---
