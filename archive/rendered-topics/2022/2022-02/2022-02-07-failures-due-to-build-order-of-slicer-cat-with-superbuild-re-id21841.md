---
topic_id: 21841
title: "Failures Due To Build Order Of Slicer Cat With Superbuild Re"
date: 2022-02-07
url: https://discourse.slicer.org/t/21841
---

# Failures due to build order of Slicer CAT with superbuild remote modules

**Topic ID**: 21841
**Date**: 2022-02-07
**URL**: https://discourse.slicer.org/t/failures-due-to-build-order-of-slicer-cat-with-superbuild-remote-modules/21841

---

## Post #1 by @jamesobutler (2022-02-07 16:14 UTC)

<p>For a Slicer CAT (Custom application) that specifies additional remote extension in the main CMakeLists.txt and these remote modules are superbuild type extensions, how should I specify appropriate build dependencies for these extensions?</p>
<p>Currently some of the remote extensions I’ve been playing around with require VTK, ITK, and Python projects from the main Slicer core to be built first. This is not a problem when building the extension after the main Slicer core build finishes because all of these dependencies are already complete. However when building these superbuild remote extensions as part of a Slicer CAT with the /MP (multiple processes) flag on, these superbuild projects of these remote extensions are attempted and the build fails because it has not yet completed the Slicer core projects of VTK, ITK, and Python.  Using the /MP flag is helpful on Windows and works well with Slicer core to reduce the total build time so I would like to continue to use this build optimization.</p>
<p>One specific example of a remote superbuild extension is <a href="https://github.com/openigtlink/SlicerOpenIGTLink" rel="noopener nofollow ugc">SlicerOpenIGTLink</a>. It has superbuild projects such as OpenIGTLinkIO which depends on VTK and YASM which depends on Python. I have observed YASM starting too early in the build process and then failing.</p>
<p>Another example is remote superbuild extension <a href="https://github.com/Slicer/SlicerOpenCV" rel="noopener nofollow ugc">SlicerOpenCV</a>. It has a superbuild project of ITKVideoBridgeOpenCV which depends on the main ITK project. I have observed ITKVideoBridgeOpenCV starting too early in the build process and then failing.</p>

---

## Post #2 by @Sam_Horvath (2022-02-07 16:30 UTC)

<p>I have done this for various projects, but always in a hack/workaround fashion by adding the dependency info myself.</p>
<p>In general what is needed is that the External_Project files in the extension should be able to detect when they are being included in an application superbuild, and then add their depedencies.</p>
<p>I.e, at this line:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/SlicerOpenCV/blob/a93d759cac5cbd0aedf74e00e4a86d8cb96816b9/SuperBuild/External_ITKVideoBridgeOpenCV.cmake#L8">
  <header class="source">

      <a href="https://github.com/Slicer/SlicerOpenCV/blob/a93d759cac5cbd0aedf74e00e4a86d8cb96816b9/SuperBuild/External_ITKVideoBridgeOpenCV.cmake#L8" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/SlicerOpenCV/blob/a93d759cac5cbd0aedf74e00e4a86d8cb96816b9/SuperBuild/External_ITKVideoBridgeOpenCV.cmake#L8" target="_blank" rel="noopener">Slicer/SlicerOpenCV/blob/a93d759cac5cbd0aedf74e00e4a86d8cb96816b9/SuperBuild/External_ITKVideoBridgeOpenCV.cmake#L8</a></h4>



    <pre class="onebox">      <code class="lang-cmake">
        <ol class="start lines" start="1" style="counter-reset: li-counter 0 ;">
            <li>#-----------------------------------------------------------------------------</li>
            <li># Build the ITK OpenCV bridge, pointing it to Slicer's ITK and this build</li>
            <li># of OpenCV</li>
            <li>
            </li>
<li>set(proj ITKVideoBridgeOpenCV)</li>
            <li>
            </li>
<li># Dependencies</li>
            <li class="selected">set(${proj}_DEPENDENCIES OpenCV)</li>
            <li>ExternalProject_Include_Dependencies(${proj} PROJECT_VAR proj DEPENDS_VAR ${proj}_DEPENDENCIES)</li>
            <li>
            </li>
<li>set(ITK_SOURCE_DIR ${ITK_DIR}/../ITK)</li>
            <li>set(${proj}_SOURCE_DIR ${ITK_SOURCE_DIR}/Modules/Video/BridgeOpenCV)</li>
            <li>ExternalProject_Message(${proj} "ITK_SOURCE_DIR:${ITK_SOURCE_DIR}")</li>
            <li>ExternalProject_Message(${proj} "${proj}_SOURCE_DIR:${${proj}_SOURCE_DIR}")</li>
            <li>
            </li>
<li># don't allow using the system ITK, use the Slicer one</li>
            <li>set(${proj}_BINARY_DIR ${CMAKE_BINARY_DIR}/${proj}-build)</li>
            <li>
        </li>
</ol>
      </code>
    </pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>ITK etc should be included if we are doing a custom app.  As a workaround hack, you can create a fork/branch of the extension that has the additional dependency info, ex:</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/sjh26/SlicerOpenIGTLink/commit/0053222ec5da7b774320bb12e3b2a194d370c8fa">
  <header class="source">

      <a href="https://github.com/sjh26/SlicerOpenIGTLink/commit/0053222ec5da7b774320bb12e3b2a194d370c8fa" target="_blank" rel="noopener">github.com/sjh26/SlicerOpenIGTLink</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/sjh26/SlicerOpenIGTLink/commit/0053222ec5da7b774320bb12e3b2a194d370c8fa" target="_blank" rel="noopener">COMP:  Explicit VTK dependency</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2020-03-23" data-time="17:00:14" data-timezone="UTC">05:00PM - 23 Mar 20 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/sjh26" target="_blank" rel="noopener">
          <img alt="sjh26" src="https://avatars.githubusercontent.com/u/25040869?v=4" class="onebox-avatar-inline" width="20" height="20">
          sjh26
        </a>
      </div>

      <div class="lines" title="changed 1 files with 1 additions and 1 deletions">
        <a href="https://github.com/sjh26/SlicerOpenIGTLink/commit/0053222ec5da7b774320bb12e3b2a194d370c8fa" target="_blank" rel="noopener">
          <span class="added">+1</span>
          <span class="removed">-1</span>
        </a>
      </div>
    </div>
  </div>
</div>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @jamesobutler (2022-02-07 19:52 UTC)

<p>I found the following example which may be the way to update extensions source without having to maintain a fork with the hack.</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/openigtlink/SlicerOpenIGTLink/commit/05fc59ed0a20a65a012337a8ff230e0d0d532fbb">
  <header class="source">

      <a href="https://github.com/openigtlink/SlicerOpenIGTLink/commit/05fc59ed0a20a65a012337a8ff230e0d0d532fbb" target="_blank" rel="noopener nofollow ugc">github.com/openigtlink/SlicerOpenIGTLink</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/openigtlink/SlicerOpenIGTLink/commit/05fc59ed0a20a65a012337a8ff230e0d0d532fbb" target="_blank" rel="noopener nofollow ugc">COMP: Fix bundling of OpenIGTLinkIO external project adding VTK dependency</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2020-10-30" data-time="23:14:05" data-timezone="UTC">11:14PM - 30 Oct 20 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/jcfr" target="_blank" rel="noopener nofollow ugc">
          <img alt="jcfr" src="https://avatars.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
          jcfr
        </a>
      </div>

      <div class="lines" title="changed 1 files with 5 additions and 0 deletions">
        <a href="https://github.com/openigtlink/SlicerOpenIGTLink/commit/05fc59ed0a20a65a012337a8ff230e0d0d532fbb" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+5</span>
          <span class="removed">-0</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This commit adds VTK as dependency when the OpenIGTLinkIO external project
is bu<span class="show-more-container"><a href="https://github.com/openigtlink/SlicerOpenIGTLink/commit/05fc59ed0a20a65a012337a8ff230e0d0d532fbb" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">ilt in a Slicer custom application.

Co-authored-by: Sam Horvath &lt;sam.horvath@kitware.com&gt;</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Also here was my original post on this topic from a couple years back. <a href="https://discourse.slicer.org/t/sliceropenigtlink-causing-customapp-build-to-fail/7758" class="inline-onebox">SlicerOpenIGTLink causing CustomApp build to fail</a></p>

---

## Post #4 by @jcfr (2022-02-07 20:36 UTC)

<p>Exactly, extensions having external project dependencies that are required only when “bundled” should be specified using this pattern:</p>
<pre data-code-wrap="cmake"><code class="lang-cmake">if(DEFINED Slicer_SOURCE_DIR)
  list(APPEND ${proj}_DEPENDS
    NameOfExternalProject1
    NameOfExternalProject2
    ...
    )
endif()
</code></pre>
<p>Then, when bundled it is sometime useful to exclude all the external projects or only consider a subset. This could be done setting variables like:<br>
<code>${extension_name}_EXTERNAL_PROJECT_EXCLUDE_ALL</code> or <code>${extension_name}_EXTERNAL_PROJECT_DEPENDENCIES</code></p>
<h3><a name="p-73663-bundling-of-superbuild-type-extension-1" class="anchor" href="#p-73663-bundling-of-superbuild-type-extension-1" aria-label="Heading link"></a>Bundling of “SuperBuild-type” extension</h3>
<p>It also sensible to read the following:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/6db0afbb7d29a9fc7e8340a862f7346241647383/CMakeLists.txt#L1103-L1126">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/6db0afbb7d29a9fc7e8340a862f7346241647383/CMakeLists.txt#L1103-L1126" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/6db0afbb7d29a9fc7e8340a862f7346241647383/CMakeLists.txt#L1103-L1126" target="_blank" rel="noopener">CMakeLists.txt</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/Slicer/Slicer/blob/6db0afbb7d29a9fc7e8340a862f7346241647383/CMakeLists.txt#L1103-L1126" rel="noopener"><code>6db0afbb7</code></a>
</div>



    <pre class="onebox"><code class="lang-txt">
      <ol class="start lines" start="1103" style="counter-reset: li-counter 1102 ;">
          <li># Support for "SuperBuild-type" extension:</li>
          <li>#</li>
          <li># * An extension is considered to be of type "SuperBuild" if a directory</li>
          <li>#   "&lt;extension_dir&gt;/SuperBuild" or "&lt;extension_dir&gt;/Superbuild" exists.</li>
          <li>#   Corresponding directory is appended to EXTERNAL_PROJECT_ADDITIONAL_DIRS.</li>
          <li>#</li>
          <li># * If variable "&lt;extension_name&gt;_EXTERNAL_PROJECT_EXCLUDE_ALL" is set to TRUE, corresponding SuperBuild directory</li>
          <li>#   is not appended to EXTERNAL_PROJECT_ADDITIONAL_DIRS.</li>
          <li>#</li>
          <li># * Associated external projects are globbed using expression of the form</li>
          <li>#   "&lt;extension_dir&gt;/(SuperBuild|Superbuild)/External_*.cmake".</li>
          <li>#</li>
          <li># * List of external project names is extracted from the "External_&lt;projectName&gt;.cmake"</li>
          <li>#   files and appended to Slicer_DEPENDENCIES. This ensures they are build before Slicer inner build.</li>
          <li>#   Setting variable "&lt;extension_name&gt;_EXTERNAL_PROJECT_DEPENDENCIES" to a list of &lt;projectName&gt; allows</li>
          <li>#   to override the list of &lt;projectName&gt; appended to Slicer_DEPENDENCIES.</li>
          <li>#</li>
          <li># * Variable Slicer_BUNDLED_EXTENSION_NAMES is updated with the names of external project</li>
          <li>#   and passed to Slicer inner build. It is then used in SlicerCPack. to package associated</li>
          <li>#   external projects if the cache variable &lt;extensionName&gt;_CPACK_INSTALL_CMAKE_PROJECTS</li>
      </ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/6db0afbb7d29a9fc7e8340a862f7346241647383/CMakeLists.txt#L1103-L1126" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<h4><a name="p-73663-example-of-use-of-extension_name_external_project_exclude_all-2" class="anchor" href="#p-73663-example-of-use-of-extension_name_external_project_exclude_all-2" aria-label="Heading link"></a>Example of use of <code>${extension_name}_EXTERNAL_PROJECT_EXCLUDE_ALL</code></h4>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Kitware/SlicerSALT/blob/7c76079d394cc036ffc704eef4ba88657607e80f/CMakeLists.txt#L338-L353">
  <header class="source">

      <a href="https://github.com/Kitware/SlicerSALT/blob/7c76079d394cc036ffc704eef4ba88657607e80f/CMakeLists.txt#L338-L353" target="_blank" rel="noopener">github.com/Kitware/SlicerSALT</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Kitware/SlicerSALT/blob/7c76079d394cc036ffc704eef4ba88657607e80f/CMakeLists.txt#L338-L353" target="_blank" rel="noopener">CMakeLists.txt</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/Kitware/SlicerSALT/blob/7c76079d394cc036ffc704eef4ba88657607e80f/CMakeLists.txt#L338-L353" rel="noopener"><code>7c76079d3</code></a>
</div>



    <pre class="onebox"><code class="lang-txt">
      <ol class="start lines" start="338" style="counter-reset: li-counter 337 ;">
          <li># ShapePopulationViewer</li>
          <li></li>
          <li>set(ShapePopulationViewer_BUILD_TESTING OFF)</li>
          <li>mark_as_superbuild(ShapePopulationViewer_BUILD_TESTING:BOOL)</li>
          <li></li>
          <li>set(extension_name "ShapePopulationViewer")</li>
          <li>set(${extension_name}_EXTERNAL_PROJECT_EXCLUDE_ALL TRUE)</li>
          <li>set(${extension_name}_SOURCE_DIR "${CMAKE_BINARY_DIR}/${extension_name}")</li>
          <li>FetchContent_Populate(${extension_name}</li>
          <li>  SOURCE_DIR     ${${extension_name}_SOURCE_DIR}</li>
          <li>  GIT_REPOSITORY ${EP_GIT_PROTOCOL}://github.com/slicersalt/${extension_name}</li>
          <li>  GIT_TAG        7414e09ba4362df058d49bcb0f5e50b388340a5b # slicersalt-2021-10-29-0836416</li>
          <li>  GIT_PROGRESS   1</li>
          <li>  QUIET</li>
          <li>  )</li>
          <li>list(APPEND Slicer_EXTENSION_SOURCE_DIRS ${${extension_name}_SOURCE_DIR})</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<h3><a name="p-73663-use-of-the-superbuildprerequisitescmake-pattern-3" class="anchor" href="#p-73663-use-of-the-superbuildprerequisitescmake-pattern-3" aria-label="Heading link"></a>Use of the <code>SuperBuildPrerequisites.cmake</code> pattern</h3>
<p>More recently, we introduced a new pattern consisting in adding a file called <code>SuperBuildPrerequisites.cmake</code> in the extension, and including it in custom application  at configuration  time.</p>
<p>This is useful to avoid duplicating requirements.</p>
<h4><a name="p-73663-slicersmtk-4" class="anchor" href="#p-73663-slicersmtk-4" aria-label="Heading link"></a>SlicerSMTK</h4>
<p>_while bundling case has been tested <img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=15" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"> , the standalone build is still a work in progress <img src="https://emoji.discourse-cdn.com/twitter/hourglass.png?v=15" title=":hourglass:" class="emoji" alt=":hourglass:" loading="lazy" width="20" height="20"> _</p>
<p>The <code>SlicerMSTK/SuperBuildPrerequisites.cmake</code> file:</p>
<ul>
<li><a href="https://gitlab.kitware.com/aeva/slicersmtk/-/blob/feat-create-minimum-viable-plugin/SuperBuildPrerequisites.cmake" class="inline-onebox">Verifying connection...</a></li>
</ul>
<p>… and how it is integrated in the custom application:</p>
<ul>
<li><a href="https://gitlab.kitware.com/shreeraj.jadhav/aevaslicer/-/blob/a3cb6208059ce3a4d8dec1bbf26b714f2590afc1/CMakeLists.txt#L209-221" class="inline-onebox">Verifying connection...</a></li>
</ul>
<h4><a name="p-73663-slicerimstk-5" class="anchor" href="#p-73663-slicerimstk-5" aria-label="Heading link"></a>SlicerIMSTK</h4>
<p>References:</p>
<ul>
<li><a href="https://github.com/jcfr/SlicerIMSTK/tree/support-custom-app-bundling-and-standalone-extension-build#readme">https://github.com/jcfr/SlicerIMSTK/tree/support-custom-app-bundling-and-standalone-extension-build#readme</a></li>
<li><a href="https://github.com/jcfr/SlicerIMSTK/blob/support-custom-app-bundling-and-standalone-extension-build/SuperBuildPrerequisites.cmake">https://github.com/jcfr/SlicerIMSTK/blob/support-custom-app-bundling-and-standalone-extension-build/SuperBuildPrerequisites.cmake</a></li>
</ul>
<p>Worth noting that <code>SuperBuildPrerequisites.cmake</code> defines <code>SlicerIMSTK_EXTERNAL_PROJECT_DEPENDENCIES</code></p>

---

## Post #5 by @lassoan (2022-02-07 21:45 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="4" data-topic="21841">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>Exactly, extensions having external project dependencies that are required only when “bundled” should be specified using this pattern:</p>
<pre><code class="lang-auto">if(DEFINED Slicer_SOURCE_DIR)
  list(APPEND ${proj}_DEPENDS
    NameOfExternalProject1
    NameOfExternalProject2
    ...
    )
endif()
</code></pre>
</blockquote>
</aside>
<p>Could we put this pattern inside <code>ExternalProject_Include_Dependencies</code>? To me it looks like a bug in <code>ExternalProject_Include_Dependencies</code> that it always enforces existence of <code>External_ITK.cmake</code> even if it is not needed. I think we could solve the issues by adding a check in <code>ExternalProject_Include_Dependencies</code> that would prevent the function from looking for <code>External_ITK.cmake</code> if <code>ITK_FOUND</code> is already set, similarly how it is done here:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/lassoan/SlicerSegmentMesher/blob/4315b7b5ab34a6464bbf3c53fac0e9862fa6be55/SuperBuild/External_cleaver.cmake#L5-L9">
  <header class="source">

      <a href="https://github.com/lassoan/SlicerSegmentMesher/blob/4315b7b5ab34a6464bbf3c53fac0e9862fa6be55/SuperBuild/External_cleaver.cmake#L5-L9" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/lassoan/SlicerSegmentMesher/blob/4315b7b5ab34a6464bbf3c53fac0e9862fa6be55/SuperBuild/External_cleaver.cmake#L5-L9" target="_blank" rel="noopener">lassoan/SlicerSegmentMesher/blob/4315b7b5ab34a6464bbf3c53fac0e9862fa6be55/SuperBuild/External_cleaver.cmake#L5-L9</a></h4>



    <pre class="onebox"><code class="lang-cmake">
      <ol class="start lines" start="5" style="counter-reset: li-counter 4 ;">
          <li>if (NOT ITK_FOUND)</li>
          <li>  # Cleaver is bundled with Slicer in a custom application.</li>
          <li>  # In this case ITK dependency must be added.</li>
          <li>  set(${proj}_DEPENDS ITK)</li>
          <li>endif()</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I guess by introducing a new <code>SuperBuildPrerequisites.cmake</code> file we could do more, but things are already so complex that we should really try to avoid adding a new mechanism to make things any more powerful, nicer, and generic and instead we should striving to make this simpler, less flexible, less configurable if at all possible.</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="1" data-topic="21841">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Using the /MP flag is helpful on Windows and works well with Slicer core to reduce the total build time</p>
</blockquote>
</aside>
<p>If we want to make the Windows build faster I would not bother with the mere 20-30% speedup that <code>/MP</code> can do, because it rarely, if ever makes a difference - build takes hours either way. However, if we can reach the 30-minute full build from scratch (as on Linux) then it would worth investing time into developing and supporting that build option. Making Windows builds significantly faster using Ninja <a href="https://discourse.slicer.org/t/msvc-cmake-cxx-mp-flag-default-value/1786/5">came up a few years ago</a>, and interestingly nested external project builds caused the problems with that, too. If making things more complicated is inevitable then at least we should check if we can get other benefits out of it, such as faster builds.</p>

---

## Post #6 by @jamesobutler (2022-02-08 14:05 UTC)

<p>I have had some success upon using the following changes in these PRs. I’m still having issues with SlicerOpenCV in the ITKVideoBridgeOpenCV project.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/openigtlink/SlicerOpenIGTLink/pull/118">
  <header class="source">

      <a href="https://github.com/openigtlink/SlicerOpenIGTLink/pull/118" target="_blank" rel="noopener nofollow ugc">github.com/openigtlink/SlicerOpenIGTLink</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/openigtlink/SlicerOpenIGTLink/pull/118" target="_blank" rel="noopener nofollow ugc">COMP: Add explicit dependencies</a>
    </h4>

    <div class="branches">
      <code>openigtlink:master</code> ← <code>jamesobutler:custom-app-depends</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-02-08" data-time="14:02:40" data-timezone="UTC">02:02PM - 08 Feb 22 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/jamesobutler" target="_blank" rel="noopener nofollow ugc">
          <img alt="jamesobutler" src="https://avatars.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
          jamesobutler
        </a>
      </div>

      <div class="lines" title="1 commits changed 2 files with 12 additions and 2 deletions">
        <a href="https://github.com/openigtlink/SlicerOpenIGTLink/pull/118/files" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+12</span>
          <span class="removed">-2</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This adds some explicit dependencies to superbuild projects so that these projec<span class="show-more-container"><a href="https://github.com/openigtlink/SlicerOpenIGTLink/pull/118" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">ts build successfully when part of a Slicer custom app build process with the /MP (multiple processes) build flag enabled. Without these changes, these projects would fail early as their dependent external projects from Slicer core had not finished yet.

Changes based on discussion at https://discourse.slicer.org/t/failures-due-to-build-order-of-slicer-cat-with-superbuild-remote-modules/21841

This supersedes https://github.com/openigtlink/SlicerOpenIGTLink/pull/94</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/IGSIO/SlicerIGSIO/pull/16">
  <header class="source">

      <a href="https://github.com/IGSIO/SlicerIGSIO/pull/16" target="_blank" rel="noopener nofollow ugc">github.com/IGSIO/SlicerIGSIO</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/IGSIO/SlicerIGSIO/pull/16" target="_blank" rel="noopener nofollow ugc">COMP: Add explicit dependencies</a>
    </h4>

    <div class="branches">
      <code>IGSIO:master</code> ← <code>jamesobutler:custom-app-depends</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-02-08" data-time="14:02:58" data-timezone="UTC">02:02PM - 08 Feb 22 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/jamesobutler" target="_blank" rel="noopener nofollow ugc">
          <img alt="jamesobutler" src="https://avatars.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
          jamesobutler
        </a>
      </div>

      <div class="lines" title="1 commits changed 1 files with 7 additions and 2 deletions">
        <a href="https://github.com/IGSIO/SlicerIGSIO/pull/16/files" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+7</span>
          <span class="removed">-2</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This adds some explicit dependencies to superbuild projects so that these projec<span class="show-more-container"><a href="https://github.com/IGSIO/SlicerIGSIO/pull/16" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">ts build successfully when part of a Slicer custom app build process with the /MP (multiple processes) build flag enabled. Without these changes, these projects would fail early as their dependent external projects from Slicer core had not finished yet.

Changes based on discussion at https://discourse.slicer.org/t/failures-due-to-build-order-of-slicer-cat-with-superbuild-remote-modules/21841</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #7 by @lassoan (2022-02-08 14:31 UTC)

<p>Yes, it seems that the same check is needed in every superbuild-type extensions.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> is there a specific reason that you recommended changing every <code>External_*.cmake</code> in every superbuild-type extension instead of fixing <code>SuperBuildPrerequisites.cmake</code>?</p>

---

## Post #8 by @jcfr (2022-02-08 17:49 UTC)

<p>Following <a href="https://discourse.slicer.org/t/2022-02-08-weekly-meeting/21843" class="inline-onebox">2022.02.08 Weekly Meeting</a> discussion, we considered the following options:</p>
<ol>
<li>
<p>Add a “virtual” project called <code>Slicer Dependencies</code> that would depend on all Slicer external project and ensure external projects from bundled SuperBuild extensions systematically depend on it.</p>
</li>
<li>
<p>Update <code>ExternalProjectDependency.cmake</code> to support customizing dependency of any external  project.</p>
</li>
</ol>
<p>We will  move forward with approach (2)</p>
<h3><a name="p-73687-externalproject_add_dependencies-1" class="anchor" href="#p-73687-externalproject_add_dependencies-1" aria-label="Heading link"></a>ExternalProject_Add_Dependencies</h3>
<p>The good news is that the <code>ExternalProjectDependency</code> API already provide a function to do so:</p>
<p><a href="https://cmake-artichoke.readthedocs.io/en/latest/ExternalProjectDependency.html#function:ExternalProject_Add_Dependencies">ExternalProject_Add_Dependencies</a></p>
<p>This means that custom application integrator should be able to address the integration of  the issue specfic to <code>SlicerOpenCV</code> by adding:</p>
<pre><code class="lang-auto">ExternalProject_Add_Dependencies(ITKVideoBridgeOpenCV
  DEPENDS
    ITK
  )
</code></pre>
<h3><a name="p-73687-path-forward-2" class="anchor" href="#p-73687-path-forward-2" aria-label="Heading link"></a>Path forward</h3>
<p>This means that for now we have the flexibility of either updating extension or customizing the external project dependency graph when bundling extension in custom application.</p>

---

## Post #9 by @lassoan (2022-02-08 19:55 UTC)

<p>Thank you <a class="mention" href="/u/jcfr">@jcfr</a> for working on this. Just one question:</p>
<p>If there is a project has dependencies that are provided in the Slicer core (ITK, VTK, DCMTK, etc.) then we need to add them using <code>ExternalProject_Add_Dependencies(${proj} DEPENDS ...)</code>; and add other libraries (zmq, pybind11, xeus, etc.) using <code>SET(${proj}_DEPENDS ...)</code>?</p>

---

## Post #10 by @jamesobutler (2022-02-08 21:07 UTC)

<p>Adding lines like the following appear to work to avoid having to update my custom application to now use the latest versions of extensions with my recently pushed updates.</p>
<pre><code class="lang-auto">ExternalProject_Add_Dependencies(OpenIGTLink
  DEPENDS
    ITK
  )
</code></pre>
<p>The ITKVideoBridgeOpenCV project is still failing for me because of a <code>numpy</code> location check that is in the initial configuration. I observed the CMake message <code>numpy package not found in python distribution. OpenCV python bindings won't be generated.</code> at time of configuring my custom application. Since this check for <code>numpy</code> location is done at time of configure rather than at time of the project beginning after ITK/python/python-numpy projects have finished, then it fails to appropriately build OpenCV as ITKVideoBridgeOpenCV needs.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/SlicerOpenCV/blob/a93d759cac5cbd0aedf74e00e4a86d8cb96816b9/SuperBuild/External_OpenCV.cmake#L50-L62">
  <header class="source">

      <a href="https://github.com/Slicer/SlicerOpenCV/blob/a93d759cac5cbd0aedf74e00e4a86d8cb96816b9/SuperBuild/External_OpenCV.cmake#L50-L62" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/SlicerOpenCV/blob/a93d759cac5cbd0aedf74e00e4a86d8cb96816b9/SuperBuild/External_OpenCV.cmake#L50-L62" target="_blank" rel="noopener nofollow ugc">Slicer/SlicerOpenCV/blob/a93d759cac5cbd0aedf74e00e4a86d8cb96816b9/SuperBuild/External_OpenCV.cmake#L50-L62</a></h4>



    <pre class="onebox">      <code class="lang-cmake">
        <ol class="start lines" start="50" style="counter-reset: li-counter 49 ;">
            <li># Determine numpy include folder (if exists)</li>
            <li>execute_process(COMMAND ${PYTHON_EXECUTABLE} -c "import pkg_resources;pkg=pkg_resources.get_distribution('numpy');print(pkg.location)" </li>
            <li>  OUTPUT_VARIABLE _numpy_location</li>
            <li>  ERROR_VARIABLE _numpy_error)</li>
            <li>if(NOT _numpy_location)</li>
            <li>  message("numpy package not found in python distribution. OpenCV python bindings won't be generated.")</li>
            <li>else()</li>
            <li>  file(TO_CMAKE_PATH ${_numpy_location} _numpy_location)</li>
            <li>  string(STRIP ${_numpy_location} _numpy_location)</li>
            <li>  list(APPEND ADDITIONAL_OPENCV_ARGS</li>
            <li>        -DPYTHON3_NUMPY_INCLUDE_DIRS:PATH=${_numpy_location}/numpy/core/include</li>
            <li>        )</li>
            <li>endif()</li>
        </ol>
      </code>
    </pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<pre><code class="lang-auto">46&gt;CMake Warning at C:/SApp/OpenCV-install/OpenCVConfig.cmake:166 (message):
46&gt;  Found OpenCV Windows Pack but it has no binaries compatible with your
46&gt;  configuration.
46&gt;
46&gt;  You should manually point CMake variable OpenCV_DIR to your build of OpenCV
46&gt;  library.
46&gt;Call Stack (most recent call first):
46&gt;  itk-module-init.cmake:4 (find_package)
46&gt;  CMakeLists.txt:14 (include)
46&gt;
46&gt;
46&gt;CMake Error at itk-module-init.cmake:4 (find_package):
46&gt;  Found package configuration file:
46&gt;
46&gt;    C:/SApp/OpenCV-install/OpenCVConfig.cmake
46&gt;
46&gt;  but it set OpenCV_FOUND to FALSE so package "OpenCV" is considered to be
46&gt;  NOT FOUND.
46&gt;Call Stack (most recent call first):
46&gt;  CMakeLists.txt:14 (include)
46&gt;
46&gt;
46&gt;-- Configuring incomplete, errors occurred!
46&gt;See also "C:/SApp/ITKVideoBridgeOpenCV-build/CMakeFiles/CMakeOutput.log".
46&gt;C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets(241,5): error MSB8066: Custom build for 'C:\SApp\CMakeFiles\320ab9882e45cf6a908302c3985d3202\ITKVideoBridgeOpenCV-mkdir.rule;C:\SApp\CMakeFiles\320ab9882e45cf6a908302c3985d3202\ITKVideoBridgeOpenCV-download.rule;C:\SApp\CMakeFiles\320ab9882e45cf6a908302c3985d3202\ITKVideoBridgeOpenCV-update.rule;C:\SApp\CMakeFiles\320ab9882e45cf6a908302c3985d3202\ITKVideoBridgeOpenCV-patch.rule;C:\SApp\CMakeFiles\320ab9882e45cf6a908302c3985d3202\ITKVideoBridgeOpenCV-configure.rule;C:\SApp\CMakeFiles\320ab9882e45cf6a908302c3985d3202\ITKVideoBridgeOpenCV-build.rule;C:\SApp\CMakeFiles\320ab9882e45cf6a908302c3985d3202\ITKVideoBridgeOpenCV-install.rule;C:\SApp\CMakeFiles\d0f4a9b23d08a9ea69be4fa4694697b0\ITKVideoBridgeOpenCV-complete.rule;C:\SApp\CMakeFiles\daf1effa4b5847d53d90fb6a3d2334b3\ITKVideoBridgeOpenCV.rule;C:\SApp\slicersources-src\CMakeLists.txt' exited with code 1.
46&gt;Done building project "ITKVideoBridgeOpenCV.vcxproj" -- FAILED.
</code></pre>

---

## Post #11 by @jcfr (2022-02-08 22:03 UTC)

<h3><a name="p-73703-slicerjupyter-use-case-custom-application-bundling-use-case-1" class="anchor" href="#p-73703-slicerjupyter-use-case-custom-application-bundling-use-case-1" aria-label="Heading link"></a>SlicerJupyter use-case custom application bundling use-case</h3>
<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="21841">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If there is a project has dependencies that are provided in the Slicer core (ITK, VTK, DCMTK, etc.) then we need to add them using <code>ExternalProject_Add_Dependencies(${proj} DEPENDS ...)</code> ; and add other libraries (zmq, pybind11, xeus, etc.) using <code>SET(${proj}_DEPENDS ...)</code> ?</p>
</blockquote>
</aside>
<p>There is no need to specify additional <code>set(${proj}_DEPENDS ..)</code></p>
<p>To make things concrete, bundling <code>SlicerJupyter</code> would only require the following in the custom application top-level <code>CMakeLists.txt</code>:</p>
<pre data-code-wrap="cmake"><code class="lang-cmake"># SlicerJupyter
set(extension_name "SlicerJupyter")
set(${extension_name}_SOURCE_DIR "${CMAKE_BINARY_DIR}/${extension_name}")
FetchContent_Populate(${extension_name}
  SOURCE_DIR     ${${extension_name}_SOURCE_DIR}
  GIT_REPOSITORY ${EP_GIT_PROTOCOL}://github.com/Slicer/SlicerJupyter.git
  GIT_TAG        b282a2c819da1e3e4fe1ab6c419e2299f976720d
  GIT_PROGRESS   1
  QUIET
  )
list(APPEND Slicer_EXTENSION_SOURCE_DIRS ${${extension_name}_SOURCE_DIR})

ExternalProject_Add_Dependencies(pybind11
  DEPENDS
    python
  )

ExternalProject_Add_Dependencies(python-packages
  DEPENDS
    python
    python-pip
    python-setuptools
  )
</code></pre>
<p>The configuration output effectively indicates the dependencies are considered:</p>
<pre data-code-wrap="bash"><code class="lang-bash">$  cmake   -DCMAKE_BUILD_TYPE:STRING=Release   -DQt5_DIR:PATH=$Qt5_DIR  ../SlicerGalaxy
[...]
-- SuperBuild -   python-packages =&gt; Requires python[INCLUDED], python-pip[INCLUDED], python-setuptools[INCLUDED], 
-- SuperBuild -   python-packages[OK]
[...]
-- SuperBuild -   pybind11 =&gt; Requires python[INCLUDED], 
-- SuperBuild -   pybind11[OK]
[...]

</code></pre>
<h4><a name="p-73703-suggested-slicerjupyter-updates-2" class="anchor" href="#p-73703-suggested-slicerjupyter-updates-2" aria-label="Heading link"></a>Suggested SlicerJupyter updates</h4>
<ul>
<li>
<p>There are some hard-coded instance of the string <code>lib/python3.6/site-packages</code> that should be removed. Instead the variable <code>PYTHON_SITE_PACKAGES_SUBDIR</code>should be used. This pull request should take care of this: <a href="https://github.com/Slicer/SlicerJupyter/pull/67" class="inline-onebox">COMP: Fix python-packages external project removing hard-coded site-packages path by jcfr · Pull Request #67 · Slicer/SlicerJupyter · GitHub</a></p>
</li>
<li>
<p>Considering <code>python-packages</code> project name is fairly generic and could conflict with other extension install python packages, we should rename it to <code>python-slicerjupyter-requirements</code>. This will be done after the previous pull-request has been integrated. It is tracked by this issue: <a href="https://github.com/Slicer/SlicerJupyter/issues/68" class="inline-onebox">GitHub · Where software is built</a></p>
</li>
<li>
<p>To provide some more flexibility, we should also look into adding<br>
<code>Slicer_REQUIRED_PYTHON_VERSION_DOT</code> recently introduced in <a href="https://github.com/Slicer/Slicer/commit/e32fa814fecdc73cf817141ce0d36d0a088e3881">Slicer@e32fa814f</a> to <code>SlicerConfig.cmake.in</code>. This pull request  takes care of this: <a href="https://github.com/Slicer/Slicer/pull/6169" class="inline-onebox">COMP: Add Slicer_REQUIRED_PYTHON_VERSION_* variables to SlicerConfig by jcfr · Pull Request #6169 · Slicer/Slicer · GitHub</a></p>
</li>
</ul>

---

## Post #12 by @jcfr (2022-02-09 02:07 UTC)

<h3><a name="p-73712-sliceropencv-custom-application-bundling-use-case-1" class="anchor" href="#p-73712-sliceropencv-custom-application-bundling-use-case-1" aria-label="Heading link"></a>SlicerOpenCV custom application bundling use-case</h3>
<aside class="quote no-group" data-username="jamesobutler" data-post="10" data-topic="21841">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>The ITKVideoBridgeOpenCV project is still failing for me because of a <code>numpy</code> location check that is in the initial configuration. I observed the CMake message <code>numpy package not found in python distribution. OpenCV python bindings won't be generated.</code> at time of configuring my custom application</p>
</blockquote>
</aside>
<p>The following pull-request simplify and fix the support for custom application bundling: <a href="https://github.com/Slicer/SlicerOpenCV/pull/69" class="inline-onebox">Simplify buildsystem by jcfr · Pull Request #69 · Slicer/SlicerOpenCV · GitHub</a></p>
<p>In a nutshell, the introspection leading to the error you experienced should be done at build time. And it turns out this was already the case. An additional OpenCV patch was needed to make sure no attempt at finding Python2 was done (see ).</p>
<p>To illustrate the following should allows to bundle <code>SlicerOpenCV</code>:</p>
<p><em><img src="https://emoji.discourse-cdn.com/twitter/warning.png?v=15" title=":warning:" class="emoji" alt=":warning:" loading="lazy" width="20" height="20">  The example below currently references a fork because the pull request referenced above has not yet been integrated. Please, do not implement any production code relying a personal fork.</em></p>
<pre data-code-wrap="cmake"><code class="lang-cmake">
# SlicerOpenCV
set(extension_name "SlicerOpenCV")
set(${extension_name}_SOURCE_DIR "${CMAKE_BINARY_DIR}/${extension_name}")
FetchContent_Populate(${extension_name}
  SOURCE_DIR     ${${extension_name}_SOURCE_DIR}
  GIT_REPOSITORY ${EP_GIT_PROTOCOL}://github.com/jcfr/SlicerOpenCV.git
  GIT_TAG        e2a86986482ba0da4f7b5ca2abe8e158a0f2a991
  GIT_PROGRESS   1
  QUIET
  )
list(APPEND Slicer_EXTENSION_SOURCE_DIRS ${${extension_name}_SOURCE_DIR})

# SlicerOpenCV: Add OpenCV dependencies specific to Slicer
ExternalProject_Add_Dependencies(OpenCV
  DEPENDS
    python-numpy
  )

# SlicerOpenCV: Overide list of dependencies to avoid attempt to build ITKVideoBridgeOpenCV
set(${extension_name}_EXTERNAL_PROJECT_DEPENDENCIES
  OpenCV
  )

# SlicerOpenCV: Enable ITKVideoBridgeOpenCV module
set(Module_ITKVideoBridgeOpenCV ON)
mark_as_superbuild(
  VARS
    Module_ITKVideoBridgeOpenCV:BOOL
    OpenCV_DIR:PATH # Set in External_OpenCV.cmake
  PROJECTS
    ITK
  )
ExternalProject_Add_Dependencies(ITK
  DEPENDS
    OpenCV
  )
</code></pre>

---

## Post #13 by @jcfr (2022-02-09 02:18 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="12" data-topic="21841">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>SlicerOpenCV custom application bundling use-case</p>
</blockquote>
</aside>
<p>You may also want to specify <code>VTK</code> since OpenCV is built with the option:</p>
<pre data-code-wrap="diff"><code class="lang-diff">ExternalProject_Add_Dependencies(OpenCV
  DEPENDS
    python-numpy
+   VTK
  )
</code></pre>

---
