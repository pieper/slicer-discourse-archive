---
topic_id: 1115
title: "Failing Slicer Extension Test Itk Cannot Load Test Image"
date: 2017-09-25
url: https://discourse.slicer.org/t/1115
---

# Failing Slicer Extension Test - ITK cannot load test image

**Topic ID**: 1115
**Date**: 2017-09-25
**URL**: https://discourse.slicer.org/t/failing-slicer-extension-test-itk-cannot-load-test-image/1115

---

## Post #1 by @mschwier (2017-09-25 15:11 UTC)

<p>System: Win 10 64 Bit Visual Studio 2013</p>
<p>Dear all,</p>
<p>I’m trying to debug a test executable of a Slicer Extension (PkModeling). The problem is that running the test, which processes an image, fails in itkImageFileReader.hxx with this error:</p>
<pre><code>File: d:\sd\itkv4\modules\io\imagebase\include\itkImageFileReader.hxx
Line: 143
Description:  Could not create IO object for reading file 
D:/Dev/Repos/PkModeling/CLI/Testing/Cxx/../../../Data/SampledPhantoms/QINProstate001/Input/QINProstate001-phantom.nrrd
  Tried to create one of the following:
    MRMLIDImageIO
  You probably failed to set a file suffix, or
    set the suffix to an unsupported type.
</code></pre>
<p>The project is set up as superbuild and can be build Standalone and as Slicer Extension. The test works fine in standalone but fails when build as extension (build against the ITK in Slicer). I have no idea what’s going on, and why ITK thinks it cannot load a nrrd file.</p>
<p>Debugging into it confirmed that in <em>ImageIOFactory::CreateImageIO</em> the call to <em>ObjectFactoryBase::CreateAllInstance(“itkImageIOBase”)</em> doesn’t return any ImageIOBase object that could handle an “nrrd” file.</p>
<p>I’m suspecting I am missing smth in my cmake configuration, since other extensions (e.g. DCMQI) built as Slicer Extension against the same ITK doesn’t have this problem <img src="https://emoji.discourse-cdn.com/twitter/confused.png?v=5" title=":confused:" class="emoji" alt=":confused:"></p>

---

## Post #2 by @lassoan (2017-09-25 16:09 UTC)

<p>MRMLIDImageIO is a special IO class that allows passing images between Slicer and CLI modules without writing them to file. One way of disabling it is to only create executable CLI by adding <code>EXECUTABLE_ONLY</code> in your CMakeLists.txt file:</p>
<pre><code>SEMMacroBuildCLI(
  NAME ${MODULE_NAME}
  LOGO_HEADER ${Slicer_SOURCE_DIR}/Resources/NAMICLogo.h
  TARGET_LIBRARIES ${${MODULE_NAME}_TARGET_LIBRARIES}
  INCLUDE_DIRECTORIES
    ${vtkITK_INCLUDE_DIRS}
    ${MRMLCore_INCLUDE_DIRS}
  EXECUTABLE_ONLY
  )
</code></pre>
<p>You may also temporarily disable the mechanism by enabling <code>Prefer executable CLIs</code> option in Application settings / Modules.</p>

---

## Post #3 by @mschwier (2017-09-25 16:16 UTC)

<p>Hi Andras,</p>
<p>Both options are already active (EXECUTABLE_ONLY in SEMMacroBuildCLI and “Prefer executable CLIs” in Slicer itslef).</p>

---

## Post #4 by @lassoan (2017-09-25 19:42 UTC)

<p>If you don’t use MRMLIDImageIO then it means that standard ITK image IO factory classes are not registered. Compare CMakeLists.txt and source code of your CLI to other CLIs that can read images, there are probably 1-2 lines missing from your code.</p>

---

## Post #5 by @mschwier (2017-09-25 22:01 UTC)

<p>Thx, I think  I found it Apparently these lines in the cmake for the test did the trick:</p>
<pre><code>if(TARGET ITKFactoryRegistration)
  target_compile_definitions(${CLP}Test PUBLIC HAS_ITK_FACTORY_REGISTRATION)
endif()
</code></pre>
<p>However I don’t completely understand why this didn’t cause an issue for the standalone build (i.e. not as slicer extension)?</p>

---

## Post #6 by @jcfr (2017-09-25 22:21 UTC)

<p>Hi <a class="mention" href="/u/mschwier">@mschwier</a>,</p>
<p>The <code>ITKFactoryRegistration</code> is a library specific to Slicer that was used to workaround a limitation of ITK. For some background info, read <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=21592">here</a></p>
<p>That said, when building Slicer against Slicer, these extra lines should not be needed. The variable <code>ITK_LIBRARIES</code>  is automatically updated …</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/1cc0d9405f282bea47f932b0c58a288608ba014b/CMake/UseSlicer.cmake.in#L117-L121" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/1cc0d9405f282bea47f932b0c58a288608ba014b/CMake/UseSlicer.cmake.in#L117-L121" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/1cc0d9405f282bea47f932b0c58a288608ba014b/CMake/UseSlicer.cmake.in#L117-L121</a></h4>
<pre class="onebox"><code class="lang-in"><ol class="start lines" start="117" style="counter-reset: li-counter 116 ;">
<li># Expose mechanism allowing extensions to register ITK IOFactories.</li>
<li># For details: http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=21592</li>
<li>set(ITK_NO_IO_FACTORY_REGISTER_MANAGER 1) # See Libs/ITKFactoryRegistration/CMakeLists.txt</li>
<li>list(APPEND ITK_LIBRARIES ITKFactoryRegistration)</li>
<li>list(APPEND ITK_INCLUDE_DIRS ${ITKFactoryRegistration_INCLUDE_DIRS})</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Also, a specific command line wrapper is used:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/eefeac9286f48552e8418a11f412b2823a09b407/Base/CLI/CMakeLists.txt#L47-L50" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/eefeac9286f48552e8418a11f412b2823a09b407/Base/CLI/CMakeLists.txt#L47-L50" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/eefeac9286f48552e8418a11f412b2823a09b407/Base/CLI/CMakeLists.txt#L47-L50</a></h4>
<pre class="onebox"><code class="lang-txt"><ol class="start lines" start="47" style="counter-reset: li-counter 46 ;">
<li>configure_file(</li>
<li>SEMCommandLineLibraryWrapper.cxx.in</li>
<li>${SlicerExecutionModel_CLI_LIBRARY_WRAPPER_CXX}</li>
<li>)</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/1cc0d9405f282bea47f932b0c58a288608ba014b/CMake/SlicerConfig.cmake.in#L403" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/1cc0d9405f282bea47f932b0c58a288608ba014b/CMake/SlicerConfig.cmake.in#L403" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/1cc0d9405f282bea47f932b0c58a288608ba014b/CMake/SlicerConfig.cmake.in#L403</a></h4>
<pre class="onebox"><code class="lang-in"><ol class="start lines" start="393" style="counter-reset: li-counter 392 ;">
<li>                          "${var} has been used to configure this project and Slicer.\n"</li>
<li>                          "${var}=${${var}}\n"</li>
<li>                          "Slicer_${var}=${value}")</li>
<li>    endif()</li>
<li>  endif()</li>
<li>  set(${var} "${value}" ${ARGN})</li>
<li>endif()</li>
<li>endmacro()</li>
<li>
</li>
<li># SlicerExecutionModel settings</li>
<li class="selected">set(SlicerExecutionModel_CLI_LIBRARY_WRAPPER_CXX "@SlicerExecutionModel_CLI_LIBRARY_WRAPPER_CXX_CONFIG@")</li>
<li>set(SlicerExecutionModel_EXTRA_INCLUDE_DIRECTORIES "@SlicerExecutionModel_EXTRA_INCLUDE_DIRECTORIES_CONFIG@")</li>
<li>set(SlicerExecutionModel_EXTRA_EXECUTABLE_TARGET_LIBRARIES "@SlicerExecutionModel_EXTRA_EXECUTABLE_TARGET_LIBRARIES_CONFIG@")</li>
<li>
</li>
<li># Slicer external projects variables</li>
<li>@Slicer_SUPERBUILD_EP_VARS_CONFIG@</li>
<li>
</li>
<li># --------------------------------------------------------------------------</li>
<li># Consistent Compiler Selections</li>
<li># --------------------------------------------------------------------------</li>
<li># Compilation Commands</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/SlicerExecutionModel/blob/983d2112ec431af20cafa49ca6cf7bd1a777869a/CMake/SEMMacroBuildCLI.cmake#L65-L69" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/SlicerExecutionModel/blob/983d2112ec431af20cafa49ca6cf7bd1a777869a/CMake/SEMMacroBuildCLI.cmake#L65-L69" target="_blank" rel="nofollow noopener">Slicer/SlicerExecutionModel/blob/983d2112ec431af20cafa49ca6cf7bd1a777869a/CMake/SEMMacroBuildCLI.cmake#L65-L69</a></h4>
<pre class="onebox"><code class="lang-cmake"><ol class="start lines" start="65" style="counter-reset: li-counter 64 ;">
<li>if(NOT DEFINED SlicerExecutionModel_CLI_LIBRARY_WRAPPER_CXX)</li>
<li>  set(LOCAL_SEM_CLI_LIBRARY_WRAPPER_CXX ${SlicerExecutionModel_DEFAULT_CLI_LIBRARY_WRAPPER_CXX})</li>
<li>else()</li>
<li>  set(LOCAL_SEM_CLI_LIBRARY_WRAPPER_CXX ${SlicerExecutionModel_CLI_LIBRARY_WRAPPER_CXX})</li>
<li>endif()</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #7 by @mschwier (2017-09-26 13:44 UTC)

<p>Thanks for the explanation <a class="mention" href="/u/jcfr">@jcfr</a></p>
<p>But does this</p>
<aside class="quote no-group" data-username="jcfr" data-post="6" data-topic="1115">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>That said, when building Slicer against Slicer, these extra lines should not be needed. The variable ITK_LIBRARIES  is automatically updated …</p>
</blockquote>
</aside>
<p>mean, that there must be something else fishy about my setup, since I needed to add these lines to make it work? <img src="https://emoji.discourse-cdn.com/twitter/confused.png?v=12" title=":confused:" class="emoji" alt=":confused:" loading="lazy" width="20" height="20"></p>

---
