---
topic_id: 18906
title: "Simplefilter Image Error Type"
date: 2021-07-24
url: https://discourse.slicer.org/t/18906
---

# SimpleFilter Image Error Type

**Topic ID**: 18906
**Date**: 2021-07-24
**URL**: https://discourse.slicer.org/t/simplefilter-image-error-type/18906

---

## Post #1 by @MachadoL (2021-07-24 14:56 UTC)

<p>Hello everyone,</p>
<p>I’d like to share a problem I am recurrently facing.<br>
I load an image and try to use some simple filters inside ITKSImpleFilters modue.<br>
I try to convert, rescale and many other transformations over the image, but I still get the same error.<br>
What is worse is that the filters do not say what is the pixel type they expect.</p>
<p>Following some screenshots from an example, I try to use the gradientAnisotropicDuffusionFilter with a .tiff (0-255) image.</p>
<p>Any comments are welcomed.</p>
<p>Error:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c9af49330b0d2f1d660314688e8eacffcd1f9f25.png" data-download-href="/uploads/short-url/sMbweFgqQd8a0X1zTGPLmGmtnHD.png?dl=1" title="error" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9af49330b0d2f1d660314688e8eacffcd1f9f25_2_517x272.png" alt="error" data-base62-sha1="sMbweFgqQd8a0X1zTGPLmGmtnHD" width="517" height="272" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9af49330b0d2f1d660314688e8eacffcd1f9f25_2_517x272.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9af49330b0d2f1d660314688e8eacffcd1f9f25_2_775x408.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c9af49330b0d2f1d660314688e8eacffcd1f9f25.png 2x" data-dominant-color="B4B4B4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">error</span><span class="informations">1009×531 137 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Image Details by 3D Slicer:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/70f825704dc27cd0c9f297c8953e718386bc6f0f.png" alt="info" data-base62-sha1="g7n7Un1jzZUW7yWSKeGF7cSxwuP" width="444" height="259"></p>
<p>Image used:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e1ee4663420b542bafd766ea3f096f4ae679f7f.png" data-download-href="/uploads/short-url/b95qAFHLXLY9mXIfGiYH7NrPiVN.png?dl=1" title="cine_16" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4e1ee4663420b542bafd766ea3f096f4ae679f7f_2_250x250.png" alt="cine_16" data-base62-sha1="b95qAFHLXLY9mXIfGiYH7NrPiVN" width="250" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4e1ee4663420b542bafd766ea3f096f4ae679f7f_2_250x250.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4e1ee4663420b542bafd766ea3f096f4ae679f7f_2_375x375.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4e1ee4663420b542bafd766ea3f096f4ae679f7f_2_500x500.png 2x" data-dominant-color="4A4A4A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">cine_16</span><span class="informations">512×512 107 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @Juicy (2021-07-24 23:28 UTC)

<p>Firstly, if it is just the gradientAnisotropicDiffusionFilter you need try using the actual slicer module for this (not under the Simple Filters area). Click the Modules drop down box in the top left area of the slicer window, look under “Filtering” , then look under “Denoising”. Alternatively just search the for the module using the search function (little magnifying glass icon). This module does seem fussy about having an 8 bit integer input.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f58330f1f3babc260713cc9f7ee2f93f6a7fff9f.jpeg" data-download-href="/uploads/short-url/z1U3tCnm91zreagKY2Uvoq7LLI3.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f58330f1f3babc260713cc9f7ee2f93f6a7fff9f_2_451x500.jpeg" alt="image" data-base62-sha1="z1U3tCnm91zreagKY2Uvoq7LLI3" width="451" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f58330f1f3babc260713cc9f7ee2f93f6a7fff9f_2_451x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f58330f1f3babc260713cc9f7ee2f93f6a7fff9f_2_676x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f58330f1f3babc260713cc9f7ee2f93f6a7fff9f.jpeg 2x" data-dominant-color="4B4E50"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">751×832 170 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If you do need to use the Simple ITK filter for some reason, I think the problem is that Simple ITK filters need to do maths on the pixel values i.e. multiplication, division etc. I am not an expert in programming but I am pretty sure you can’t, for example, do division on integer numbers. For example, 3/2 = 1.5 (1.5 is no longer an integer number). So you need to convert your volume to have floating point pixel values. You can use the Cast Scalar Volume module to convert your volume to “Float” (or maybe “Double” I cant remember off the top of my head) before using other Simple ITK filters.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/18ae395ed238d751caf670b26a5f2a3b2300d707.png" alt="image" data-base62-sha1="3wkJqxlzIQS7UlyidN27PGwCmEL" width="577" height="446"></p>
<p>I am pretty sure there is a cast filter under “Simple Filters” as well</p>

---

## Post #3 by @pieper (2021-07-25 14:24 UTC)

<p><a class="mention" href="/u/juicy">@Juicy</a> is right, the problem is the datatype, and casting or using the alternate filter implementation are good solutions.</p>
<p>The reason for all this is that when SimpleITK classes are wrapped for python, there’s extra code size and compilation time for each pixel type so only the ones that make sense for a filter are available.</p>
<p>As a general rule for SimpleFilters, I guess the expectation was that people who understood what the filter tries to do would get the idea about what data types are needed, but if you need to know the information is admittedly pretty obscure and as far as I know it’s never been exposed in the UI (probably it should, in case anyone wants to contribute a feature to inform the user or cast automatically).</p>
<p>The info itself is in the JSON files in <a href="https://github.com/SimpleITK/SlicerSimpleFilters/tree/master/SimpleFilters/Resources/json">this directory</a>.</p>
<p>For this case it’s this line:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SimpleITK/SlicerSimpleFilters/blob/master/SimpleFilters/Resources/json/GradientAnisotropicDiffusionImageFilter.json#L7">
  <header class="source">

      <a href="https://github.com/SimpleITK/SlicerSimpleFilters/blob/master/SimpleFilters/Resources/json/GradientAnisotropicDiffusionImageFilter.json#L7" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SimpleITK/SlicerSimpleFilters/blob/master/SimpleFilters/Resources/json/GradientAnisotropicDiffusionImageFilter.json#L7" target="_blank" rel="noopener">SimpleITK/SlicerSimpleFilters/blob/master/SimpleFilters/Resources/json/GradientAnisotropicDiffusionImageFilter.json#L7</a></h4>



  <pre class="onebox">    <code class="lang-json">
      <ol class="start lines" start="1" style="counter-reset: li-counter 0 ;">
          <li>{</li>
          <li>  "name" : "GradientAnisotropicDiffusionImageFilter",</li>
          <li>  "template_code_filename" : "ImageFilter",</li>
          <li>  "template_test_filename" : "ImageFilter",</li>
          <li>  "number_of_inputs" : 1,</li>
          <li>  "doc" : "Some global documentation",</li>
          <li class="selected">  "pixel_types" : "RealPixelIDTypeList",</li>
          <li>  "include_files" : [</li>
          <li>    "algorithm"</li>
          <li>  ],</li>
          <li>  "members" : [</li>
          <li>    {</li>
          <li>      "name" : "TimeStep",</li>
          <li>      "type" : "double",</li>
          <li>      "default" : 0.125,</li>
          <li>      "doc" : "Time step for PDE solver"</li>
          <li>    },</li>
      </ol>
    </code>
  </pre>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p><code>RealPixelIDTypeList</code> and other keywords are defined here, so it’s float and double:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SimpleITK/SimpleITK/blob/master/Code/Common/include/sitkPixelIDTypeLists.h#L98-L99">
  <header class="source">

      <a href="https://github.com/SimpleITK/SimpleITK/blob/master/Code/Common/include/sitkPixelIDTypeLists.h#L98-L99" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SimpleITK/SimpleITK/blob/master/Code/Common/include/sitkPixelIDTypeLists.h#L98-L99" target="_blank" rel="noopener">SimpleITK/SimpleITK/blob/master/Code/Common/include/sitkPixelIDTypeLists.h#L98-L99</a></h4>



  <pre class="onebox">    <code class="lang-h">
      <ol class="start lines" start="98" style="counter-reset: li-counter 97 ;">
          <li>typedef typelist::MakeTypeList&lt;BasicPixelID&lt;float&gt;,</li>
          <li>                               BasicPixelID&lt;double&gt; &gt;::Type RealPixelIDTypeList;</li>
      </ol>
    </code>
  </pre>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @lassoan (2021-07-25 15:06 UTC)

<p>Conversion from input voxel type to supported voxel type should be a low-level SimpleITK feature. If automatic conversion was implemented in SimpleFilters module, users would be inconvenienced when they try to use SimpleITK filters in Python scripts.</p>
<p><a class="mention" href="/u/blowekamp">@blowekamp</a> do you plan to address this issue in SimpleITK?</p>

---
