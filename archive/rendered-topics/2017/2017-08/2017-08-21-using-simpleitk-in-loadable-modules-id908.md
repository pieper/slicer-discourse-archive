# Using SimpleItk in loadable modules

**Topic ID**: 908
**Date**: 2017-08-21
**URL**: https://discourse.slicer.org/t/using-simpleitk-in-loadable-modules/908

---

## Post #1 by @sandra (2017-08-21 08:21 UTC)

<p>Hi everyone,</p>
<p>I would like to use SimpleItk while writting a loadable module.<br>
My problem is about including the necessary files:<br>
<span class="hashtag">#include</span> &lt;sitkCenteredTransformInitializerFilter.h&gt; for example doesn’t work, I get the error “file not found”</p>
<p>I know that Slicer’s architecture is complex and I’m not sure how to include SimpleItk/the necessary files in a loadable module. I tried the different ways I could find in SimpleItk examples (in the official documentation, so not using Slicer) but I didn’t succeed.</p>
<p>(I did build Slicer with SimpleItk).</p>
<p>Thanks for your help,</p>
<p>Sandra.</p>

---

## Post #2 by @Fernando (2017-08-21 12:13 UTC)

<p>Hi Sandra,</p>
<p>I think SimpleITK has wrappers for Python, C#, Java and R, but for C++ you should use ITK directly.</p>

---

## Post #3 by @sandra (2017-08-21 12:35 UTC)

<p>You mean that in general it isn’t possible to use simpleItk with C++ or it isn’t possible in Slicer particularly ?</p>

---

## Post #4 by @Fernando (2017-08-21 12:59 UTC)

<p>In general:</p>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">
      <a href="https://github.com/SimpleITK/SimpleITK#simpleitk" target="_blank" rel="nofollow noopener">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars1.githubusercontent.com/u/476215?s=400&amp;v=4" class="thumbnail onebox-avatar" width="337" height="337">

<h3><a href="https://github.com/SimpleITK/SimpleITK#simpleitk" target="_blank" rel="nofollow noopener">SimpleITK/SimpleITK</a></h3>

<p>SimpleITK: a layer built on top of the Insight Toolkit (ITK), intended to simplify and facilitate ITK's use in rapid prototyping, education and interpreted languages. - SimpleITK/SimpleITK</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #5 by @sandra (2017-08-21 13:02 UTC)

<p>I saw this page where there are examples of simpleItk used in C++</p>
<p><a href="https://itk.org/SimpleITKDoxygen/html/examples.html" class="onebox" target="_blank" rel="nofollow noopener">https://itk.org/SimpleITKDoxygen/html/examples.html</a></p>

---

## Post #6 by @Fernando (2017-08-21 13:13 UTC)

<aside class="quote no-group" data-username="sandra" data-post="5" data-topic="908">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/4491bb/48.png" class="avatar"> sandra:</div>
<blockquote>
<p>I saw this page where there are examples of simpleItk used in C++</p>
</blockquote>
</aside>
<p>I didn’t know about those, sorry.</p>

---

## Post #7 by @fedorov (2017-08-21 20:03 UTC)

<p>In general, it is indeed possible to use SimpleITK from C++, but I don’t know of any examples in Slicer. <a class="mention" href="/u/blowekamp">@blowekamp</a> would know for sure!</p>

---

## Post #8 by @jcfr (2017-08-21 20:27 UTC)

<p>While possible, the build system currently do not enable this.</p>
<p>In a nutshell, the SimpleITK targets (available through <code>SimpleITKConfig.cmake</code>) are not exposed to extensions.  Only ITK is.</p>
<p>To keep things simple, I suggest we stick to ITK when dealing with C++ and image processing.</p>

---

## Post #9 by @blowekamp (2017-08-22 01:25 UTC)

<p>I have a module, which is still compiling, that uses SimpleITK in this way. The NucleusClosing module uses the c++ interface for SimpleITK. It still seems to work.</p>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">
      <a href="https://github.com/blowekamp/Slicer-IASEM?files=1" target="_blank" rel="nofollow noopener">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars1.githubusercontent.com/u/321061?s=400&amp;v=4" class="thumbnail onebox-avatar" width="420" height="420">

<h3><a href="https://github.com/blowekamp/Slicer-IASEM?files=1" target="_blank" rel="nofollow noopener">blowekamp/Slicer-IASEM</a></h3>

<p>Slicer3D IASEM Microscopy Extension. Contribute to blowekamp/Slicer-IASEM development by creating an account on GitHub.</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>HTH<br>
Brad</p>

---

## Post #10 by @jcfr (2017-08-22 03:59 UTC)

<p>Indeed <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=5" title=":smile:" class="emoji" alt=":smile:"> , we are marking <code>SimpleITK</code>  as <code>FIND_PACKAGE</code> … and the targets end up being exposed.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/ead66c24da4cc499981b09e05ea79c82815ce2db/SuperBuild/External_SimpleITK.cmake#L127-L130" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/ead66c24da4cc499981b09e05ea79c82815ce2db/SuperBuild/External_SimpleITK.cmake#L127-L130" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/ead66c24da4cc499981b09e05ea79c82815ce2db/SuperBuild/External_SimpleITK.cmake#L127-L130</a></h4>
<pre class="onebox"><code class="lang-cmake"><ol class="start lines" start="127" style="counter-reset: li-counter 126 ;">
<li>mark_as_superbuild(</li>
<li>VARS SimpleITK_DIR:PATH</li>
<li>LABELS "FIND_PACKAGE"</li>
<li>)</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #11 by @sandra (2017-08-22 08:16 UTC)

<p>So <a class="mention" href="/u/blowekamp">@blowekamp</a> what did you do to have simpleItk working in your loadable module ?</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> : do I have to write these 4 lines somewhere or are they already present in the slicer’s architecture ?</p>

---

## Post #12 by @jcfr (2017-08-22 13:08 UTC)

<p>Hi <a class="mention" href="/u/sandra">@sandra</a>,</p>
<p>You only need to “link” against the <code>SimpleITK</code> targets as it is done here:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/blowekamp/Slicer-IASEM/blob/f3895471dd01d0340cbed5178dfe7ac27b745090/NucleusClosing/CMakeLists.txt#L31-L33" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/blowekamp/Slicer-IASEM/blob/f3895471dd01d0340cbed5178dfe7ac27b745090/NucleusClosing/CMakeLists.txt#L31-L33" target="_blank" rel="nofollow noopener">blowekamp/Slicer-IASEM/blob/f3895471dd01d0340cbed5178dfe7ac27b745090/NucleusClosing/CMakeLists.txt#L31-L33</a></h4>
<pre class="onebox"><code class="lang-txt"><ol class="start lines" start="31" style="counter-reset: li-counter 30 ;">
<li>set(MODULE_TARGET_LIBRARIES</li>
<li>${ITK_LIBRARIES} ${SimpleITK_LIBRARIES}</li>
<li>)</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>In the case of loadable modules, you would add <code>${SimpleITK_LIBRARIES}</code> to the <code>TARGET_LIBRARIES</code> parameter of the logic:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/ead66c24da4cc499981b09e05ea79c82815ce2db/Utilities/Templates/Modules/Loadable/Logic/CMakeLists.txt#L20-L26" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/ead66c24da4cc499981b09e05ea79c82815ce2db/Utilities/Templates/Modules/Loadable/Logic/CMakeLists.txt#L20-L26" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/ead66c24da4cc499981b09e05ea79c82815ce2db/Utilities/Templates/Modules/Loadable/Logic/CMakeLists.txt#L20-L26</a></h4>
<pre class="onebox"><code class="lang-txt"><ol class="start lines" start="20" style="counter-reset: li-counter 19 ;">
<li>SlicerMacroBuildModuleLogic(</li>
<li>NAME ${KIT}</li>
<li>EXPORT_DIRECTIVE ${${KIT}_EXPORT_DIRECTIVE}</li>
<li>INCLUDE_DIRECTORIES ${${KIT}_INCLUDE_DIRECTORIES}</li>
<li>SRCS ${${KIT}_SRCS}</li>
<li>TARGET_LIBRARIES ${${KIT}_TARGET_LIBRARIES}</li>
<li>)</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #13 by @blowekamp (2017-08-22 13:19 UTC)

<p>The first step is to find the SimpleITK package in CMake:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/blowekamp/Slicer-IASEM/blob/f3895471dd01d0340cbed5178dfe7ac27b745090/CMakeLists.txt#L45-L52" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/blowekamp/Slicer-IASEM/blob/f3895471dd01d0340cbed5178dfe7ac27b745090/CMakeLists.txt#L45-L52" target="_blank" rel="nofollow noopener">blowekamp/Slicer-IASEM/blob/f3895471dd01d0340cbed5178dfe7ac27b745090/CMakeLists.txt#L45-L52</a></h4>
<pre class="onebox"><code class="lang-txt"><ol class="start lines" start="45" style="counter-reset: li-counter 44 ;">
<li>if(Slicer_USE_SimpleITK)</li>
<li># this find is needed to define SimpleITK_USE_FILE</li>
<li>find_package(SimpleITK REQUIRED)</li>
<li>
</li>
<li>include(${SimpleITK_USE_FILE})</li>
<li>else()</li>
<li>message(FATAL_ERROR "Slicer is not configured for SimpleITK.\nSome modules will be disabled.")</li>
<li>endif()</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Then as JC said you need to link against the SimpleITK libraries.</p>

---

## Post #14 by @sandra (2017-08-22 13:20 UTC)

<p>Ok and those lines about find the SimpleITK package, where should I write them (for a loadable module) ? (In which CMakeLists.txt)</p>

---
