# Build error when building ITKPython

**Topic ID**: 15302
**Date**: 2021-01-01
**URL**: https://discourse.slicer.org/t/build-error-when-building-itkpython/15302

---

## Post #1 by @jamesobutler (2021-01-01 02:39 UTC)

<p>With <code>Slicer_BUILD_ITKPython</code> and <code>Slicer_INSTALL_ITKPython</code> turned on and using CMake 3.18.4 and latest Slicer master I get some errors during the wrapping process.  Has anyone successfully built ITKPython recently?</p>
<p>I was looking into turning on ITK python support as a default in Slicer since it has matured in the past year and half. This would support future python development using <code>import itk</code> instead of relying on SimpleITK when using python. This seems to be the preferred trend to support more development using Python. I considered pip installing ITK, but since Slicer at times uses a custom ITK build or at least a custom configuration it seemed necessary to build the ITK python package just like we build the SimpleITK python package for the same reason.</p>
<p>Some of my build errors (build still continuing)</p>
<pre><code class="lang-auto">33&gt;  Generating ../../itkDCMTKImageIO.xml
33&gt;C:/S5R-nightly/ITK-build/Wrapping/itkDCMTKImageIO.cxx(31,18): error GCCDED198: no type named 'DCMTKImageIOFactory' in namespace 'itk' [C:\S5R-nightly\ITK-build\Wrapping\Modules\ITKIODCMTK\ITKIODCMTKCastXML.vcxproj]
33&gt;      typedef itk::DCMTKImageIOFactory itkDCMTKImageIOFactory;
33&gt;              ~~~~~^
33&gt;C:/S5R-nightly/ITK-build/Wrapping/itkDCMTKImageIO.cxx(32,18): error G1A4676F8: no member named 'DCMTKImageIOFactory' in namespace 'itk' [C:\S5R-nightly\ITK-build\Wrapping\Modules\ITKIODCMTK\ITKIODCMTKCastXML.vcxproj]
33&gt;      typedef itk::DCMTKImageIOFactory::Pointer itkDCMTKImageIOFactory_Pointer;
33&gt;              ~~~~~^
33&gt;C:/S5R-nightly/ITK-build/Wrapping/itkDCMTKImageIO.cxx(34,18): error GCCDED198: no type named 'DCMTKSeriesFileNames' in namespace 'itk' [C:\S5R-nightly\ITK-build\Wrapping\Modules\ITKIODCMTK\ITKIODCMTKCastXML.vcxproj]
33&gt;      typedef itk::DCMTKSeriesFileNames itkDCMTKSeriesFileNames;
33&gt;              ~~~~~^
33&gt;C:/S5R-nightly/ITK-build/Wrapping/itkDCMTKImageIO.cxx(35,18): error G1A4676F8: no member named 'DCMTKSeriesFileNames' in namespace 'itk' [C:\S5R-nightly\ITK-build\Wrapping\Modules\ITKIODCMTK\ITKIODCMTKCastXML.vcxproj]
33&gt;      typedef itk::DCMTKSeriesFileNames::Pointer itkDCMTKSeriesFileNames_Pointer;
33&gt;              ~~~~~^
33&gt;  4 errors generated.
</code></pre>

---

## Post #2 by @thewtex (2021-01-06 15:34 UTC)

<p>Hi <a class="mention" href="/u/jamesobutler">@jamesobutler</a>,</p>
<p>We should be able to use the pre-built ITK Python binary packages via <code>pip install</code> – the Slicer CMake configuration could be updated to do this by default.</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="1" data-topic="15302">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>I considered pip installing ITK, but since Slicer at times uses a custom ITK build or at least a custom configuration it seemed necessary to build the ITK python package</p>
</blockquote>
</aside>
<p>This is good to consider, but the way the ITK Python binaries are built, there will not be<br>
conflicts with the Slicer ITK C++ libraries.</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="1" data-topic="15302">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<pre><code class="lang-auto">33&gt;  Generating ../../itkDCMTKImageIO.xml
33&gt;C:/S5R-nightly/ITK-build/Wrapping/itkDCMTKImageIO.cxx(31,18): error GCCDED198: no type named 'DCMTKImageIOFactory' in namespace 'itk' [C:\S5R-nightly\ITK-build\Wrapping\Modules\ITKIODCMTK\ITKIODCMTKCastXML.vcxproj]
33&gt;      typedef itk::DCMTKImageIOFactory itkDCMTKImageIOFactory;
</code></pre>
</blockquote>
</aside>
<p>This is likely related to a DCMTK CMake configuration issue, maybe there is a better hint earlier in the build log.</p>

---

## Post #3 by @jamesobutler (2021-01-06 18:25 UTC)

<p><a class="mention" href="/u/thewtex">@thewtex</a> I was considering cases where in the past Slicer has issued an ITK commit change to its Slicer ITK fork for immediate use in the Slicer preview build. Then the developer might want to use that fix from the ITK python interface.  Or maybe this is an incorrect assumption? I guess we could work around and say the fix is immediately available in C++, but must wait for a newer pre-built ITK Python package. Thoughts on this <a class="mention" href="/u/lassoan">@lassoan</a>?</p>
<p>Seems like in the past the use of the Slicer ITK fork was to wait on merge approval of a fix in ITK and also not have to update other Slicer code/dependencies due to other ITK code changes by backporting onto a known working commit.</p>
<p>I’ll try to look into the DCMTK CMake issue. I was looking how <a href="https://github.com/InsightSoftwareConsortium/ITKPythonPackage" rel="noopener nofollow ugc">https://github.com/InsightSoftwareConsortium/ITKPythonPackage</a> was creating the wheels, but was going to try the current Slicer ITKPython wrapping cmake option. Does in general this look to be correct? See the current latest code:<br>
<a href="https://github.com/Slicer/Slicer/blob/bc4a07dc408089328f359436de05c3e440f7a39e/SuperBuild/External_ITK.cmake#L153" rel="noopener nofollow ugc">https://github.com/Slicer/Slicer/blob/bc4a07dc408089328f359436de05c3e440f7a39e/SuperBuild/External_ITK.cmake#L153</a><br>
<a href="https://github.com/Slicer/Slicer/blob/bc4a07dc408089328f359436de05c3e440f7a39e/SuperBuild/External_ITK.cmake#L73-L98" rel="noopener nofollow ugc">https://github.com/Slicer/Slicer/blob/bc4a07dc408089328f359436de05c3e440f7a39e/SuperBuild/External_ITK.cmake#L73-L98</a></p>

---

## Post #4 by @jamesobutler (2021-01-06 18:30 UTC)

<p>Similarly, can ITK Python and SimpleITK (python) both be installed without conflicts if they are using different ITK versions?</p>

---

## Post #5 by @lassoan (2021-01-06 18:57 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="3" data-topic="15302">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>I was considering cases where in the past Slicer has issued an ITK commit change to its Slicer ITK fork for immediate use in the Slicer preview build. Then the developer might want to use that fix from the ITK python interface. Or maybe this is an incorrect assumption? I guess we could work around and say the fix is immediately available in C++, but must wait for a newer pre-built ITK Python package.</p>
</blockquote>
</aside>
<p>Since there is no reliable way to ensure binary compatibility between C++ libraries, we need to build Slicer’s ITK.</p>
<p>However, it is possible to create binary compatible Python packages, so for ITK Python we have the option of building and bundling it with Slicer or using a prebuilt package. While building and bundling ITK Python with Slicer has some advantages (we can choose to build it with the options we want, what data types are supported, we can apply patches immediately) there are also some disadvantages (forces us to deal with ITK Python build, makes Slicer core larger, takes longer to build, our special build might work differently from default ITK, etc.). Overall, using pre-built ITK Python looks a more favorable option to me.</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="4" data-topic="15302">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>can ITK Python and SimpleITK (python) both be installed without conflicts if they are using different ITK versions?</p>
</blockquote>
</aside>
<p>Yes. ITK Python is all statically linked, nothing is exposed from ITK.</p>
<p>What I don’t like very much about the current situation is that users may end up with having 3 copies of ITKs in Slicer: ITK C++, SimpleITK, and ITK Python. It just seems highly redundant. But maybe nowadays this is acceptable price to pay for some convenience and freedom to choice (you can use different ITK Python and SimpleITK versions).</p>
<p>Maybe we could decide to not bundle SimpleITK with Slicer and it would be downloaded/installed from PyPI when needed (e.g., when the user opens Simple Filters module). It would then somewhat reduce the redundancy.</p>

---

## Post #6 by @thewtex (2021-01-07 13:52 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="3" data-topic="15302">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p><a class="mention" href="/u/thewtex">@thewtex</a> I was considering cases where in the past Slicer has issued an ITK commit change to its Slicer ITK fork for immediate use in the Slicer preview build</p>
</blockquote>
</aside>
<p>For quite some time, there were two commits added on top of ITK that were specific to Slicer’s build configuration, but all substantial changes were integrated into the upstream ITK repository. However, currently, Slicer is using upstream ITK:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/88a4b7d84f0186becbadb8aac4f976ff89288e3a/SuperBuild/External_ITK.cmake#L33">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/88a4b7d84f0186becbadb8aac4f976ff89288e3a/SuperBuild/External_ITK.cmake#L33" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/88a4b7d84f0186becbadb8aac4f976ff89288e3a/SuperBuild/External_ITK.cmake#L33" target="_blank" rel="noopener nofollow ugc">Slicer/Slicer/blob/88a4b7d84f0186becbadb8aac4f976ff89288e3a/SuperBuild/External_ITK.cmake#L33</a></h4>



    <pre class="onebox"><code class="lang-cmake">
      <ol class="start lines" start="23" style="counter-reset: li-counter 22 ;">
          <li></li>
          <li># Sanity checks</li>
          <li>if(DEFINED ITK_DIR AND NOT EXISTS ${ITK_DIR})</li>
          <li>  message(FATAL_ERROR "ITK_DIR variable is defined but corresponds to nonexistent directory")</li>
          <li>endif()</li>
          <li></li>
          <li>if(NOT DEFINED ITK_DIR AND NOT Slicer_USE_SYSTEM_${proj})</li>
          <li></li>
          <li>  ExternalProject_SetIfNotDefined(</li>
          <li>    Slicer_${proj}_GIT_REPOSITORY</li>
          <li class="selected">    "${EP_GIT_PROTOCOL}://github.com/InsightSoftwareConsortium/ITK"</li>
          <li>    QUIET</li>
          <li>    )</li>
          <li></li>
          <li>  ExternalProject_SetIfNotDefined(</li>
          <li>    Slicer_${proj}_GIT_TAG</li>
          <li>    "v5.1.2"</li>
          <li>    QUIET</li>
          <li>    )</li>
          <li></li>
          <li>  set(EXTERNAL_PROJECT_OPTIONAL_CMAKE_CACHE_ARGS)</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<blockquote>
<p><a href="https://github.com/Slicer/Slicer/blob/bc4a07dc408089328f359436de05c3e440f7a39e/SuperBuild/External_ITK.cmake#L73-L98" class="inline-onebox" rel="noopener nofollow ugc">Slicer/SuperBuild/External_ITK.cmake at bc4a07dc408089328f359436de05c3e440f7a39e · Slicer/Slicer · GitHub</a></p>
</blockquote>
<p>Overall, it looks OK. However, I agree with <a class="mention" href="/u/lassoan">@lassoan</a>: in practice, using pre-built binaries is practically a good, workable approach to pursue.</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="3" data-topic="15302">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>I’ll try to look into the DCMTK CMake issue.</p>
</blockquote>
</aside>
<p>Thanks, <a class="mention" href="/u/jamesobutler">@jamesobutler</a>. We may want to create an <code>itk-iodcmtk</code> binary Python package similar to the many other ITK module Python packages.</p>

---

## Post #7 by @jcrudy (2021-09-29 19:25 UTC)

<p>I hit the same problem: <a href="https://github.com/InsightSoftwareConsortium/ITK/issues/2762" class="inline-onebox" rel="noopener nofollow ugc">Building v5.2.1 fails on itkDCMTKImageIO.cxx · Issue #2762 · InsightSoftwareConsortium/ITK · GitHub</a><br>
I did find a potential solution, which I mentioned in the thread on the github issue.</p>

---
