---
topic_id: 21729
title: "Trouble Building Itk Python Wrapping"
date: 2022-02-01
url: https://discourse.slicer.org/t/21729
---

# Trouble building ITK python wrapping

**Topic ID**: 21729
**Date**: 2022-02-01
**URL**: https://discourse.slicer.org/t/trouble-building-itk-python-wrapping/21729

---

## Post #1 by @ebrahim (2022-02-01 11:43 UTC)

<p>I want to include ITK python wrapping in my Slicer build, but building fails when I turn on <code>Slicer_BUILD_ITKPython</code>, with the following error in the make output</p>
<pre><code class="lang-nohighlight">...
-- ITKPyUtils: Creating itkPyCommand submodule.
-- ITKPyUtils: Creating itkPyImageFilter submodule.
CMake Error: The following variables are used in this project, but they are set to NOTFOUND.
Please set them or make sure they are set and tested correctly in the CMake files:
_vtk_lib_include_dirs
   used as include directory in directory /home/ebrahim/Slicer-SuperBuild-Debug/ITK/Modules/Bridge/VtkGlue/wrapping
   used as include directory in directory /home/ebrahim/Slicer-SuperBuild-Debug/ITK/Modules/Bridge/VtkGlue/wrapping
  ... &lt;more of the same message&gt;
   used as include directory in directory /home/ebrahim/Slicer-SuperBuild-Debug/ITK/Modules/Bridge/VtkGlue/wrapping
-- Configuring incomplete, errors occurred!
</code></pre>
<p>I see the variable <code>_vtk_lib_include_dirs</code> getting assigned <a href="https://github.com/InsightSoftwareConsortium/ITK/blob/master/Modules/Bridge/VtkGlue/wrapping/CMakeLists.txt" rel="noopener nofollow ugc">here in ITK</a>, but I don’t really know what’s going on. Not sure if this is a Slicer issue or an ITK issue. Any ideas?</p>

---

## Post #2 by @lassoan (2022-02-02 02:56 UTC)

<p>Slicer passes VTK_DIR to ITK <a href="https://github.com/Slicer/Slicer/blob/1513644e124f19d128d49e98d7e7d979f5b905f1/SuperBuild/External_ITK.cmake#L160">here</a>, which should be sufficient for ITK to configure ITKVTKGlue.</p>
<p><a class="mention" href="/u/thewtex">@thewtex</a> do you have any idea what can go wrong?</p>

---

## Post #3 by @jcfr (2022-02-02 03:43 UTC)

<p>Thanks for the report. I will have a look and report back shortly.</p>

---

## Post #4 by @thewtex (2022-02-02 15:35 UTC)

<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/1513644e124f19d128d49e98d7e7d979f5b905f1/SuperBuild/External_ITK.cmake#L39">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/1513644e124f19d128d49e98d7e7d979f5b905f1/SuperBuild/External_ITK.cmake#L39" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/1513644e124f19d128d49e98d7e7d979f5b905f1/SuperBuild/External_ITK.cmake#L39" target="_blank" rel="noopener nofollow ugc">Slicer/Slicer/blob/1513644e124f19d128d49e98d7e7d979f5b905f1/SuperBuild/External_ITK.cmake#L39</a></h4>



    <pre class="onebox">      <code class="lang-cmake">
        <ol class="start lines" start="29" style="counter-reset: li-counter 28 ;">
            <li>if(NOT DEFINED ITK_DIR AND NOT Slicer_USE_SYSTEM_${proj})</li>
            <li>
            </li>
<li>  ExternalProject_SetIfNotDefined(</li>
            <li>    Slicer_${proj}_GIT_REPOSITORY</li>
            <li>    "${EP_GIT_PROTOCOL}://github.com/InsightSoftwareConsortium/ITK"</li>
            <li>    QUIET</li>
            <li>    )</li>
            <li>
            </li>
<li>  ExternalProject_SetIfNotDefined(</li>
            <li>    Slicer_${proj}_GIT_TAG</li>
            <li class="selected">    "v5.2.1"</li>
            <li>    QUIET</li>
            <li>    )</li>
            <li>
            </li>
<li>  set(EXTERNAL_PROJECT_OPTIONAL_CMAKE_CACHE_ARGS)</li>
            <li>
            </li>
<li>  if(Slicer_USE_TBB)</li>
            <li>    list(APPEND EXTERNAL_PROJECT_OPTIONAL_CMAKE_CACHE_ARGS</li>
            <li>      -DModule_ITKTBB:BOOL=ON</li>
            <li>      -DTBB_DIR:PATH=${TBB_DIR}</li>
            <li>      )</li>
        </ol>
      </code>
    </pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I would recommend updating to ITK <code>v5.3rc03</code>. VTK changes its CMake configuration often. There have been updates.</p>

---

## Post #5 by @jamesobutler (2022-02-02 15:53 UTC)

<p>Here is work already in progress to use most recent ITK. This branch could be used for testing the ITK python wrapping</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/5954">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/5954" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/pull/5954" target="_blank" rel="noopener nofollow ugc">Update ITK to post-5.3rc03 including requiring at least C++14</a>
    </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>jamesobutler:c++14</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-10-19" data-time="20:25:52" data-timezone="UTC">08:25PM - 19 Oct 21 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/jamesobutler" target="_blank" rel="noopener nofollow ugc">
          <img alt="jamesobutler" src="https://avatars.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
          jamesobutler
        </a>
      </div>

      <div class="lines" title="4 commits changed 42 files with 56 additions and 60 deletions">
        <a href="https://github.com/Slicer/Slicer/pull/5954/files" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+56</span>
          <span class="removed">-60</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This is part of work for #5673.

C++14 is the new minimum with CMake 3.16.3 as<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/5954" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden"> set by ITK 5.3 requirements (https://github.com/InsightSoftwareConsortium/ITK/blob/v5.3rc01/Documentation/SupportedCompilers.md).

This will enable future GrowCut remote ITK module work as @dzenanz was beginning in #5807.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #6 by @jamesobutler (2022-02-02 16:34 UTC)

<p>Note this previous attempt linked below of me trying to build ITK python. Some discussion was about <code>pip install itk</code> as an easier option for Slicer instead of changing Slicer to build ITK python wrapping as part of the nightly build process.</p>
<aside class="quote quote-modified" data-post="1" data-topic="15302">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/build-error-when-building-itkpython/15302">Build error when building ITKPython</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    With Slicer_BUILD_ITKPython and Slicer_INSTALL_ITKPython turned on and using CMake 3.18.4 and latest Slicer master I get some errors during the wrapping process.  Has anyone successfully built ITKPython recently? 
I was looking into turning on ITK python support as a default in Slicer since it has matured in the past year and half. This would support future python development using import itk instead of relying on SimpleITK when using python. This seems to be the preferred trend to support more …
  </blockquote>
</aside>


---

## Post #7 by @jcfr (2022-02-02 19:21 UTC)

<p>A post was split to a new topic: <a href="/t/addressing-issue-with-pip-install-itk/21763">Addressing issue with “pip install itk”</a></p>

---

## Post #8 by @ebrahim (2022-02-02 16:47 UTC)

<p>Thanks for pointing me to this PR!<br>
I will try building off this branch and report back.</p>

---

## Post #9 by @ebrahim (2022-02-02 21:50 UTC)

<p>With that branch I ended up with the following error during build on linux:</p>
<pre><code class="lang-nohighlight">[100%] Generating ../../itkImageToVTKImageFilter.xml
In file included from /path/to/superbuild/ITK-build/Wrapping/itkImageToVTKImageFilter.cxx:16:
/path/to/superbuild/ITK/Modules/Bridge/VtkGlue/include/itkImageToVTKImageFilter.h:22:10: fatal error: 'vtkImageImport.h' file not found
#include "vtkImageImport.h"
         ^~~~~~~~~~~~~~~~~~
1 error generated.
make[5]: *** [Wrapping/Modules/ITKVtkGlue/CMakeFiles/ITKVtkGlueCastXML.dir/build.make:65: Wrapping/itkImageToVTKImageFilter.xml] Error 1
make[4]: *** [CMakeFiles/Makefile2:36492: Wrapping/Modules/ITKVtkGlue/CMakeFiles/ITKVtkGlueCastXML.dir/all] Error 2
make[3]: *** [Makefile:152: all] Error 2
make[2]: *** [slicersources-build/CMakeFiles/ITK.dir/build.make:118: slicersources-build/ITK-prefix/src/ITK-stamp/ITK-build] Error 2
make[1]: *** [CMakeFiles/Makefile2:877: slicersources-build/CMakeFiles/ITK.dir/all] Error 2
make: *** [Makefile:84: all] Error 2
</code></pre>
<p>EDIT: I should add that I was trying this with a Slicer Custom App, not with vanilla Slicer. So the issue may be related to the way in which I included the new branch. Perhaps I omitted a needed change in my top level cmake file.</p>
<p>I’ll continue digging into this.</p>

---

## Post #10 by @ebrahim (2022-02-03 23:44 UTC)

<p>Update: Same error with vanilla Slicer.</p>

---
