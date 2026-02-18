# Exception during execution of SimpleFilter filters

**Topic ID**: 2442
**Date**: 2018-03-27
**URL**: https://discourse.slicer.org/t/exception-during-execution-of-simplefilter-filters/2442

---

## Post #1 by @EricWilson (2018-03-27 18:59 UTC)

<p>I am currently trying to test different filtering methods in the UI which will later be automated through python. I am using a volume of DICOM images and I am getting an error on several different SimpleFilter filters. If i try to filter using the LaplacianImageFilter for example, using the default parameters and using my volume as input, I will get the following exception when running the filter:</p>
<p>Exception thrown in SimpleITK LaplacianImageFilter_Execute: d:\d\p\slicer-481-package\simpleitk\code\common\include\sitkMemberFunctionFactory.hxx:196:<br>
sitk::ERROR: Pixel type: 16-bit signed integer is not supported in 3D byclass itk::simple::LaplacianImageFilter</p>
<p>I can’t find much about the error, does anyone know  how to fix it?</p>

---

## Post #2 by @lassoan (2018-03-27 19:11 UTC)

<p>You need to cast the input images to a supported pixel type using “Cast Scalar Volume” module.</p>

---

## Post #3 by @EricWilson (2018-03-27 20:42 UTC)

<p>ok, that seems to have fixed the issue. however, the information on what the supported pixel types are for a given filter aren’t easy to find. I was able to use trial and error for the LaplacianImageFilter and found that it only takes in float and double, and after looking in the header file for the declaration <a href="https://itk.org/Doxygen/html/itkLaplacianImageFilter_8h_source.html" rel="nofollow noopener">here</a>, I can see that there is a check for floating point here:</p>
<pre><code>itkConceptMacro( InputPixelTypeIsFloatingPointCheck,
     ( Concept::IsFloatingPoint&lt; InputPixelType &gt; ) );
</code></pre>
<p>however, this isn’t listed anywhere else that i can see on the main file, and the input parameter only says that both input and output need to be of the same dimensionality.</p>
<p>thanks for the response.</p>

---

## Post #4 by @lassoan (2018-03-27 20:53 UTC)

<aside class="quote no-group" data-username="EricWilson" data-post="3" data-topic="2442">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ericwilson/48/1513_2.png" class="avatar"> EricWilson:</div>
<blockquote>
<p>that seems to have fixed the issue. however, the information on what the supported pixel types are for a given filter aren’t easy to find</p>
</blockquote>
</aside>
<p>Yes, I sometimes find this difficult, too.</p>
<p><a class="mention" href="/u/blowekamp">@blowekamp</a> Do you have a suggestion how to address this?</p>

---

## Post #5 by @blowekamp (2018-03-28 13:14 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="2442">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Yes, I sometimes find this difficult, too.</p>
<p><a class="mention" href="/u/blowekamp">@blowekamp</a> Do you have a suggestion how to address this?</p>
</blockquote>
</aside>
<p>For filters which just take one input, it is quite easy to know what is accepted. If you look at the SimpleITK Doxygen e.g. <a href="https://itk.org/SimpleITKDoxygen110/html/classitk_1_1simple_1_1LaplacianImageFilter.html" rel="noopener nofollow ugc">LaplacianImageFilter</a>, they have a member typedef called <a href="https://itk.org/SimpleITKDoxygen110/html/classitk_1_1simple_1_1LaplacianImageFilter.html#a9af38cbfce40eafe5015775d1ccfaba8" rel="noopener nofollow ugc">PixelIDTypeList</a> which is the input pixels types supported by the filter defined by a “typelist”.</p>
<p>For multi-input filters the image types are generally expected to be the same dimension and pixel type. However “Mask” images are expected to be of pixel type uint8_t. There are a handful of filters which are “dual dispatch”, meaning the support different image types for their inputs. This include the <a href="https://itk.org/SimpleITKDoxygen/html/classitk_1_1simple_1_1LabelStatisticsImageFilter.html" rel="noopener nofollow ugc">LabelStatisticsImageFilter</a>, <a href="https://itk.org/SimpleITKDoxygen/html/classitk_1_1simple_1_1MaskImageFilter.html" rel="noopener nofollow ugc">MaskImageFilter</a>, <a href="https://itk.org/SimpleITKDoxygen/html/classitk_1_1simple_1_1LabelIntensityStatisticsImageFilter.html" rel="noopener nofollow ugc">LabelIntensityStatisticsImageFilter</a> etc. These conventions are documented <a href="https://itk.org/SimpleITKDoxygen/html/ConventionsPage.html" rel="noopener nofollow ugc">here</a>.</p>
<p>Determining the output image type is admittedly difficult. It can be dependent on the input image type(s). Even looking at the instantiated ITK filter’s template arguments does not always show the output image type. You need to look at the ImageToImageFilter ancestor of the instantiated ITK type.</p>
<p>Yes this situation should be improved. I am open to suggestions and a discussion on what should be done to improve it. Documentation in the SimpleITK class description? Runtime access?</p>

---

## Post #6 by @lassoan (2018-03-28 13:25 UTC)

<p>Thank you Brad. I think the main pain point is that the error message is <code>Exception ... Pixel type: 16-bit signed integer is not supported in 3D byclass itk::simple::LaplacianImageFilter</code> - it does not give a clue about what pixel type is supported.</p>
<p>It should not be too difficult to generate a link to the doxygen page of the filter. This could be useful for other purposes anyway, to learn what is the meaning of different parameters, etc.</p>
<p>However, for me it is not obvious how PixelIDTypeList tells what the accepted input pixel types are.</p>
<blockquote>
<p>typedef RealPixelIDTypeList itk::simple::LaplacianImageFilter::PixelIDTypeList<br>
Define the pixels types supported by this filter<br>
Definition at line 78 of file sitkLaplacianImageFilter.h.</p>
</blockquote>
<p>Is it the <code>Real</code> word that indicates that it requires floating-point input?</p>

---

## Post #7 by @blowekamp (2018-03-28 13:45 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="2442">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Is it the Real word that indicates that it requires floating-point input?</p>
</blockquote>
</aside>
<p>Yes. As is frequent in Doxygen, and C++ conventions there are nested types that need to be clicked through. You can find this definition:</p>
<pre><code class="lang-auto">typedef typelist::MakeTypeList&lt;BasicPixelID&lt;float&gt;, BasicPixelID&lt;double&gt; &gt;::Type itk::simple::RealPixelIDTypeList
</code></pre>
<p>Although that still may not be clear to many…</p>
<p>So you suggestion is to improve the error message when the image types are not supported. Either by listing what is supported, or linking on where to get more information?</p>

---

## Post #8 by @lassoan (2018-03-28 13:50 UTC)

<aside class="quote no-group" data-username="blowekamp" data-post="7" data-topic="2442">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/blowekamp/48/1386_2.png" class="avatar"> blowekamp:</div>
<blockquote>
<p>So you suggestion is to improve the error message when the image types are not supported.</p>
</blockquote>
</aside>
<p>Yes. Since currently it is a bit difficult to decipher pixel type info from doxygen, either doxygen page generation should be tuned or somehow SimpleFilters should figure out what the pixel type is and display that to the user.</p>

---

## Post #9 by @manjula (2019-12-22 21:11 UTC)

<p>Is the finding of the input pixel type for the simple-filters been simplified yet or still we need to do trial and error  with Cast Scalar volume ?</p>

---
