---
topic_id: 4053
title: "Internal Compiler Error In Simpleitk While Building Slicer W"
date: 2018-09-10
url: https://discourse.slicer.org/t/4053
---

# Internal compiler error in SimpleITK while building Slicer with latest VS2015 compiler

**Topic ID**: 4053
**Date**: 2018-09-10
**URL**: https://discourse.slicer.org/t/internal-compiler-error-in-simpleitk-while-building-slicer-with-latest-vs2015-compiler/4053

---

## Post #1 by @lassoan (2018-09-10 19:46 UTC)

<p>I’ve recently updated my VS2015 compiler (used in VS2017 IDE) to “Microsoft ® Build Engine version 15.8.168+ga8fba1ebd7 for .NET Framework”. With this compiler, I often get compiler crash while trying to build SimpleITK’s sitkScalarConnectedComponentImageFilter:</p>
<pre><code>  sitkScalarConnectedComponentImageFilter.cxx

c:\d\s4r\itkv4\modules\segmentation\connectedcomponents\include\itkconnectedcomponentfunctorimagefilter.hxx(41): fatal error C1001: An internal error has occurred in the compiler. [C:\D\S4R\SimpleITK-build\SimpleITK-build\Code\BasicFilters\src\SimpleITK_ITKConnectedComponents.vcxproj] [C:\D\S4R\SimpleITK-build\SimpleITK.vcxproj] [C:\D\S4R\SimpleITK.vcxproj]
 
      (compiler file 'msc1.cpp', line 1518)
 
       To work around this problem, try simplifying or changing the program near the locations listed above.
</code></pre>
<p>See full logs here: <a href="https://pastebin.com/giSZD6T2">https://pastebin.com/giSZD6T2</a></p>
<p>I’ve never had this problem on other computers with VS2017 IDE / VS2015 toolset version “Microsoft ® Build Engine version 15.7.180.61344 for .NET Framework”.</p>
<p>Has anyone else come across this issue?</p>
<p><a class="mention" href="/u/blowekamp">@blowekamp</a> do you have any suggestion?</p>

---

## Post #2 by @blowekamp (2018-09-10 20:03 UTC)

<p>ITK had a report of issues with  VS 2017 15.8.0:</p><aside class="onebox discoursetopic" data-onebox-src="https://discourse.itk.org/t/visual-studio-vs-2017-15-8-0-internal-compiler-error-with-numerictraits/1205">
  <header class="source">
      <img src="https://discourse.itk.org/uploads/default/optimized/1X/71db04d41479c229accbe8bf0b99195f75f46770_2_32x32.png" class="site-icon" width="32" height="32">

      <a href="https://discourse.itk.org/t/visual-studio-vs-2017-15-8-0-internal-compiler-error-with-numerictraits/1205" target="_blank" rel="noopener nofollow ugc" title="07:57PM - 16 August 2018">ITK – 16 Aug 18</a>
  </header>

  <article class="onebox-body">
    <img src="https://discourse.itk.org/uploads/default/original/1X/8a8379ed42cbc60fb262a064faca192c7d7111e7.png" class="thumbnail onebox-avatar" width="500" height="500">

<div class="title-wrapper">
  <h3><a href="https://discourse.itk.org/t/visual-studio-vs-2017-15-8-0-internal-compiler-error-with-numerictraits/1205" target="_blank" rel="noopener nofollow ugc">Visual Studio VS 2017 15.8.0: Internal compiler error with NumericTraits</a></h3>
</div>

  <p>Just for your information: I have filed a bug report here https://developercommunity.visualstudio.com/content/problem/312703/vs-1580-internal-compiler-error.html - since itk’s NumericTraits::max() seem to cause a problem.  Best regards,   sophonet</p>

  <p>
    <span class="label1">Reading time: 1 mins 🕑</span>
      <span class="label2">Likes: 7 ❤</span>
  </p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
