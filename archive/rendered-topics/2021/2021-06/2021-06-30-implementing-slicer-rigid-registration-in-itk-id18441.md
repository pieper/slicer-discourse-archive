# Implementing Slicer rigid registration in ITK

**Topic ID**: 18441
**Date**: 2021-06-30
**URL**: https://discourse.slicer.org/t/implementing-slicer-rigid-registration-in-itk/18441

---

## Post #1 by @rz93 (2021-06-30 20:26 UTC)

<p>I am trying to register two CT head images from the same subjects. There exists significant rotations and one image is significantly cropped than the other.<br>
I used the General Registration (BRAINS) rigid registration with MSE metric and default parameters and it worked out pretty well. Now I’m trying to duplicate the result using SimpleITK in python, but it fails to produce the same result as Slicer. Can anyone point out where my SimpleITK implementation is not right?</p>
<p>My code is below:</p>
<pre><code class="lang-auto">initial_transform = sitk.CenteredTransformInitializer(fixed_image,  moving_image, 
                                                      sitk.Euler3DTransform(), sitk.CenteredTransformInitializerFilter.GEOMETRY)
registration_method = sitk.ImageRegistrationMethod()

# Similarity metric settings.
registration_method.SetMetricAsMeanSquares()
registration_method.SetMetricSamplingStrategy(registration_method.RANDOM)
registration_method.SetMetricSamplingPercentage(0.002)
registration_method.SetInterpolator(sitk.sitkLinear)

# Optimizer settings.
registration_method.SetOptimizerAsRegularStepGradientDescent(learningRate=0.05, 
                                                              minStep=0.001, numberOfIterations=1500)
registration_method.SetOptimizerScalesFromPhysicalShift()
registration_method.SetOptimizerWeights([1,1,1,1000,1000,1000])
registration_method.SetInitialTransform(initial_transform, inPlace=False)
egistration_method.Execute(fixed_image, moving_image)

</code></pre>

---

## Post #2 by @lassoan (2021-07-02 04:23 UTC)

<p>ITK (SimpleITK) registration provides solid basic infrastructure for registration but it typically requires careful initialization and extensive parameter tuning to be used in practice.</p>
<p>That’s why higher level toolkits, such as BRAINS, Elastix, and ANTs have been developed on top of ITK and you would normally use one of these higher-level toolkits. BRAINS is bundled with the Slicer installer, and you can get the other two by installing SlicerElastix and SlicerANTs extensions.</p>
<p>If you must use plain ITK/SimpleITK then you can ask for advice for that on the <a href="https://discourse.itk.org">ITK forum</a>.</p>

---
