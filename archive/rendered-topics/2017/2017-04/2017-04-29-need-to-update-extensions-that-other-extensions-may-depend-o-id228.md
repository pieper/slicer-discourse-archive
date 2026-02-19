---
topic_id: 228
title: "Need To Update Extensions That Other Extensions May Depend O"
date: 2017-04-29
url: https://discourse.slicer.org/t/228
---

# Need to update extensions that other extensions may depend on

**Topic ID**: 228
**Date**: 2017-04-29
**URL**: https://discourse.slicer.org/t/need-to-update-extensions-that-other-extensions-may-depend-on/228

---

## Post #1 by @lassoan (2017-04-29 12:47 UTC)

<p>Extensions were failed to build last night that depend on extensions that don’t provide a (ExtensionName)Config.cmake file. The error is changed to a warning for now, so extension builds will succeed tomorrow, but developers who maintain extensions that other extensions may depend on, should make a small change in their CMakeLists.txt files.</p>
<p>Reason for the change: For importing path variables (library paths, python paths, etc.) from dependent extensions, find_package() must be able to find the dependent extension.</p>
<p>How to make sure find_package() can find a dependent extension: Add this line near the end of the top-level CMakeLists.txt (just before Slicer_EXTENSION_CPACK configuration, see <a href="https://github.com/Slicer/Slicer/blob/master/Utilities/Templates/Extensions/Default/CMakeLists.txt#L25">this example</a>):</p>
<pre><code>include(${Slicer_EXTENSION_GENERATE_CONFIG})</code></pre>

---

## Post #2 by @che85 (2017-11-17 17:42 UTC)

<p>Hi Andras,</p>
<p>I added the line locally to all dependent extensions and build each one.</p>
<p>When I configure the extensions which has dependencies it still gives the following error:</p>
<pre><code>CMake Warning at /Users/christian/sources/cpp/Slicer/Extensions/CMake/SlicerBlockAdditionalLauncherSettings.cmake:48 (MESSAGE):
  Dependent extension SlicerDevelopmentToolbox DCMQI PETDICOMExtension cannot
  be found by CMake find_package(), therefore paths variables cannot be
  imported from this extension.  The problem can be resolved by generating
  SlicerDevelopmentToolbox DCMQI PETDICOMExtensionConfig.cmake by adding
  include(${Slicer_EXTENSION_GENERATE_CONFIG}) to the top-level
  CMakeLists.txt of the dependent exension.
Call Stack (most recent call first):
  /Users/christian/sources/cpp/Slicer/Build/Slicer-build/UseSlicer.cmake:282 (include)
  CMakeLists.txt:19 (include)
</code></pre>
<p>Am I missing anything?</p>
<p>Christian</p>

---

## Post #3 by @fedorov (2017-11-17 18:17 UTC)

<aside class="quote no-group" data-username="che85" data-post="2" data-topic="228">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/che85/48/636_2.png" class="avatar"> che85:</div>
<blockquote>
<p>I added the line locally to all dependent extensions and build each one.</p>
</blockquote>
</aside>
<p>Note that at least some of those extensions already generate config file (I think dcmqi does, without using the line Andras mentioned), and also it appears that none of the extensions we maintain had build failures (see filtered list <a href="http://slicer.cdash.org/index.php?project=Slicer4&amp;display=project&amp;filtercombine=and&amp;filtercombine=and&amp;filtercombine=or&amp;filtercombine=or&amp;filtercombine=or&amp;filtercombine=or&amp;filtercombine=or&amp;filtercount=8&amp;showfilters=1&amp;filtercombine=or&amp;field1=buildname&amp;compare1=63&amp;value1=DCMQI&amp;field2=buildname&amp;compare2=63&amp;value2=OpenCV&amp;field3=buildname&amp;compare3=63&amp;value3=PkModeling&amp;field4=buildname&amp;compare4=63&amp;value4=SlicerProstate&amp;field5=buildname&amp;compare5=63&amp;value5=-PET&amp;field6=buildname&amp;compare6=63&amp;value6=SliceTracker&amp;field7=buildname&amp;compare7=63&amp;value7=Radiomics&amp;field8=buildname&amp;compare8=63&amp;value8=QuantitativeReporting">here</a>).</p>

---

## Post #4 by @che85 (2017-11-17 18:47 UTC)

<p>I added the line (for now only locally) for testing to all dependent extensions, but cmake still drops that error message when configuring QuantitativeReporting</p>

---

## Post #5 by @lassoan (2017-11-17 20:23 UTC)

<p>The *Config.cmake file that Slicer generates contains directories that has to be added to AdditionalLauncherSettings.ini file. If you generate your own *Config.cmake file already then you may need to disable that mechanism (when you build it as a Slicer extension) and use Slicer’s *Config.cmake generator instead. You can inject your own content into the Slicer-generated *Config.cmake files.</p>

---

## Post #6 by @che85 (2017-11-17 21:29 UTC)

<p>Ok and how do I do that?</p>

---

## Post #7 by @lassoan (2017-11-18 01:10 UTC)

<p>To add custom content to your MyExtensionConfig.cmake file, set MyExtension_CUSTOM_CONFIG variable above <code>include(${Slicer_EXTENSION_GENERATE_CONFIG})</code>. See details and example here:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/CMake/SlicerExtensionGenerateConfig.cmake" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/CMake/SlicerExtensionGenerateConfig.cmake" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/master/CMake/SlicerExtensionGenerateConfig.cmake</a></h4>
<pre><code class="lang-cmake"># Generate the &lt;Extension&gt;Config.cmake file in the build tree.
# This file makes it possible for an extension to depend on targets defined
# in other extensions.
# This file is based on SlicerGenerateSlicerConfig.cmake.
#
# Example:
#
# Add these lines near the end of top-level CMakeLists.txt in Sequences extension
# to allow other extensions to use it.
#
#   # Pass some custom content to the SequencesConfig.cmake file (optional)
#   set(Sequences_CUSTOM_CONFIG "message(STATUS \"Test\")")
#
#   # Generate SequencesConfig.cmake
#   include(${Slicer_EXTENSION_GENERATE_CONFIG})
#
# Add these lines to the CMakeLists.txt to use vtkMRMLSequenceNode
# implemented in Sequences extension:
#
#   find_package(Sequences REQUIRED)
</code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/master/CMake/SlicerExtensionGenerateConfig.cmake" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
