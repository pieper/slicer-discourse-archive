---
topic_id: 17664
title: "Packaging External Projects"
date: 2021-05-17
url: https://discourse.slicer.org/t/17664
---

# Packaging external projects

**Topic ID**: 17664
**Date**: 2021-05-17
**URL**: https://discourse.slicer.org/t/packaging-external-projects/17664

---

## Post #1 by @keri (2021-05-17 20:39 UTC)

<p>Hi,</p>
<p>Setup: Ubuntu 20.04, SlicerCAT</p>
<p>I have external projects in SuperBuild subfolder that I can successively compile. After compilation I want to copy their content to SlicerCAT archive (package them or install - I guess it is almost the same)</p>
<p>For example I want to simply copy folder <code>${CMAKE_BINARY_DIR}/h5geo-install</code> to <code>${Slicer_INSTALL_BIN_DIR}</code> when packaging SlicerCAT. As you noticed I install <code>h5geo</code> while building SlicerCAT (this simplifies some things for me now, probably later I will change it so h5geo will be only built but not installed while SlicerCAT build step).</p>
<p><strong>My attempts were:</strong><br>
<em>1 attempt:</em></p>
<pre><code class="lang-auto">install(
  DIRECTORY ${h5geo_ROOT}    # h5geo_ROOT points to ${CMAKE_BINARY_DIR}/h5geo-install
  DESTINATION ${Slicer_INSTALL_BIN_DIR}
  )
</code></pre>
<p>Packaging is done via command:</p>
<pre><code class="lang-auto">cd d/Slicer-build
cpack -B ../../
</code></pre>
<p>this doesn’t add <code>h5geo</code> to <code>.tar.gz</code> archive.</p>
<p><em>2 attempt:</em><br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ/Extensions#How_to_package_third_party_libraries_.3F" rel="noopener nofollow ugc">From here</a> I tried:</p>
<pre><code class="lang-auto">set(CPACK_INSTALL_CMAKE_PROJECTS "${h5geo_ROOT};h5geo;ALL;/")  # don't completely understand the syntaxis: 1- parameter is the path to folder; 2- name of project??; 3- copy all components? If I copy directory what should be this 3rd param?

# Add Slicer sources
add_subdirectory(${slicersources_SOURCE_DIR} ${slicersources_BINARY_DIR})
</code></pre>
<p>This code snippet doesn’t give the result neither.</p>
<p>I see that most of Slicer’s packaging “magic” can be uncovered in <code>SlicerCPack.cmake</code>, <code>SlicerBlockInstall...</code> and in other SlicerCAT projects like SlicerAstro, AevaSlicer or SlicerSALT but still I have no understanding how it works.</p>
<p>Probably someone could give a little more hints on that.</p>

---

## Post #2 by @lassoan (2021-05-18 00:41 UTC)

<p>Each library is responsible for installing itself. If your set install directory when you configure h5geo then it will be included in the installation package.</p>

---

## Post #3 by @keri (2021-05-18 20:27 UTC)

<p>Thank you.</p>
<p>I think I have found a solution how it works with files:</p>
<pre><code class="lang-auto"># Install libraries
include(${Slicer_SOURCE_DIR}/CMake/SlicerFunctionInstallLibrary.cmake)
slicerInstallLibrary(    # I think this is somehow similar to CMake `install` function
  FILE ${h5geo_ROOT}/lib/libh5geo.so
  DESTINATION ${Slicer_INSTALL_BIN_DIR}
  COMPONENT RuntimeLibraries
  )

set(CPACK_INSTALL_CMAKE_PROJECTS "${CPACK_INSTALL_CMAKE_PROJECTS};${h5geo_ROOT};h5geo;ALL;/")

include(${Slicer_SOURCE_DIR}/CMake/SlicerExtensionGenerateConfig.cmake)
include(${Slicer_SOURCE_DIR}/CMake/SlicerExtensionCPack.cmake)
</code></pre>
<p>Probably some lines are excessive but now I can see that <code>libh5geo.so</code> is copied to the bin folder of SlicerCAT archive.</p>
<p>Now I’m looking for a way to copy/install folder because I need to copy Julia to SlicerCAT install dir.</p>
<p>P.S. <code>slicerInstallLibrary</code> doesnt accept DIRECTORY (instead of FILE) as a parameter</p>

---

## Post #4 by @lassoan (2021-05-19 01:41 UTC)

<p>This looks about right.</p>
<aside class="quote no-group" data-username="keri" data-post="3" data-topic="17664">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/keri/48/11618_2.png" class="avatar"> keri:</div>
<blockquote>
<pre><code class="lang-auto">slicerInstallLibrary(    # I think this is somehow similar to CMake `install` function
  FILE ${h5geo_ROOT}/lib/libh5geo.so
  DESTINATION ${Slicer_INSTALL_BIN_DIR}
  COMPONENT RuntimeLibraries
  )
</code></pre>
</blockquote>
</aside>
<p>This will only work on linux. If you don’t add the <code>.so</code> then it may work on all platforms.</p>
<aside class="quote no-group" data-username="keri" data-post="3" data-topic="17664">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/keri/48/11618_2.png" class="avatar"> keri:</div>
<blockquote>
<p>Now I’m looking for a way to copy/install folder because I need to copy Julia to SlicerCAT install dir.</p>
</blockquote>
</aside>
<p>If your Julia build (or SDK) is set up correctly then all you need is to do is something like <code>find_package(Julia)</code> and then install the appropriate Julia target (the target knows where all the libraries, including different build modes, what files to install and where, etc.). If it is not set up correctly then you can either fix it or create the targets manually. If this does not work out (or you don’t want to learn these CMake techniques) then an an easy hack is to just get the file list using CMake file glob command and use that for file copy commands (for the built tree) and file install commands (for the install tree). There are differences in how this works on linux, macos, and windows, so it is quite a learning curve, but CMake is such an important and widely used build system that it is worth the effort.</p>

---

## Post #5 by @keri (2021-05-19 15:27 UTC)

<p>I’m completely agree with you. Step by step I have some success with cmake. For now I simply copy folder <code>Julia</code> to Slicer Install tree. Probably later I will improve that.</p>
<p>I’ve figured out (or almost) how to install folder <code>Julia</code> to Slicer install tree:</p>
<pre><code class="lang-auto">install(
  DIRECTORY ${julia_ROOT}/  # '/' in the end is necessary
  DESTINATION ${Slicer_INSTALL_ROOT}/julia
  COMPONENT RuntimeLibraries  # 'ALL' instead of `RuntimeLibraries` doesn't work
  )

set(CPACK_INSTALL_CMAKE_PROJECTS "${CPACK_INSTALL_CMAKE_PROJECTS};${julia_ROOT};julia;ALL;/")
</code></pre>
<p>My main mistake was I didn’t use <code>COMPONENT</code> with <code>RuntimeLibraries</code> value (I used to keep it empty).</p>
<p>Now my <code>Julia</code> folder is copied to Slicer install tree (package) but probably this is not the most correct way to do that as <code>RuntimeLibraries</code> should not be applied to a folder with subfolders and different types of files I think.</p>

---
