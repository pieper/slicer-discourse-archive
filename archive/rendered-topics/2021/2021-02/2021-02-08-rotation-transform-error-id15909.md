---
topic_id: 15909
title: "Rotation Transform Error"
date: 2021-02-08
url: https://discourse.slicer.org/t/15909
---

# Rotation Transform Error

**Topic ID**: 15909
**Date**: 2021-02-08
**URL**: https://discourse.slicer.org/t/rotation-transform-error/15909

---

## Post #1 by @MachadoL (2021-02-08 19:10 UTC)

<p>Hello, Everyone.</p>
<p>I am performing a 3D multistage registration. 1st Stage is a Translation transform initiated with an identity transform. The second stage is a Rotation transform.</p>
<p>It is pops up the following errors right after the first iteration:</p>
<pre><code>ExceptionObject caught !

itk::ExceptionObject (0x563b1e8ede50)
Location: "void itk::MattesMutualInformationImageToImageMetricv4&lt;TFixedImage, TMovingImage, TVirtualImage, TInternalComputationValueType, TMetricTraits&gt;::ComputeResults() const [with TFixedImage = itk::Image&lt;float, 3&gt;; TMovingImage = itk::Image&lt;float, 3&gt;; TVirtualImage = itk::Image&lt;float, 3&gt;; TInternalComputationValueType = double; TMetricTraits = itk::DefaultImageToImageMetricTraitsv4&lt;itk::Image&lt;float, 3&gt;, itk::Image&lt;float, 3&gt;, itk::Image&lt;float, 3&gt;, double&gt;]" 
File: /home/9679247/Documentos/General-Sources/InsightToolkit-5.1.2/Modules/Registration/Metricsv4/include/itkMattesMutualInformationImageToImageMetricv4.hxx
Line: 312
Description: itk::ERROR: itk::ERROR: MattesMutualInformationImageToImageMetricv4(0x563b1e6a4c60): All samples map outside moving image buffer. The images do not sufficiently overlap. They need to be initialized to have more overlap before this metric will work. For instance, you can align the image centers by translation.
</code></pre>
<p>Also:</p>
<pre><code>ExceptionObject caught !

itk::ExceptionObject (0x55d97dcea7d0)
Location: "itk::Versor::Set( const VectorType )" 
Description: Trying to initialize a Versor with a vector whose magnitude is greater than 1
</code></pre>
<p>I tried varying the initial transform initialization method:</p>
<p>First I verified the way I am sing the previous stage transform into the next stage:</p>
<pre><code> registrationR-&gt;SetInitialTransform( initialTransformRotation );
          registrationR-&gt;InPlaceOn();

          // Connecting previous stage transform to the next stage;
          registrationR-&gt;SetMovingInitialTransform(
            initialTransformTranslation);
</code></pre>
<p>Then I check some possibilities for the Initial transform. I tried:<br>
Initial transform with <code>SetIdentity()</code>, to make it an Identity transfom.<br>
Also, I tried to use the <code>CenteredTransformInitializer class</code>, defining <code>MomentsOn()</code> method.<br>
None of the strategies above sounded to solve this problem.</p>
<p>Any help is very welcomed.</p>

---

## Post #2 by @lassoan (2021-02-08 19:18 UTC)

<p>Which module do you use for registration?</p>
<p>As the error message states, the registration fails because the images do not sufficiently overlap.</p>
<p>I would recommend to pre-align the images before registration as described <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html#automatic-image-registration">here</a>. If that solves your problem then you can experiment with automatic initialization methods. Note that you need to harden the transform on the image that you pass to the registration module because most (if not all) registration modules ignore parent transforms of the input volumes.</p>

---

## Post #3 by @MachadoL (2021-02-08 19:49 UTC)

<p>Ouh, Didn’t let it clear.<br>
I am WRITING a pipeline with ITK classes.</p>
<p>And I tried previous initialization methods (MomentsOn) and previous stage transform.<br>
I’ll write that post on ITK discourse.</p>
<p>Thanks anyway <a class="mention" href="/u/lassoan">@lassoan</a> .</p>

---

## Post #4 by @lassoan (2021-02-08 19:57 UTC)

<p>Note that Elastix (available in Slicer via SlicerElastix extension, but you can use it as a standalone command-line application, or as a Python package) is a nice solution for this, as you don’t need to write any code, just define each registration stage in a text file (<a href="https://simpleelastix.readthedocs.io/ParameterMaps.html">parameter map file</a>) and Elastix takes care of instantiating all the classes, setting parameters, connecting the stages. Elastix also defines a number of metrics and optimizers in addition to the stock ITK classes.</p>

---

## Post #5 by @MachadoL (2021-02-08 20:21 UTC)

<p>All right. Thanks again.</p>

---
