---
topic_id: 21369
title: "Tbb Libs Are Not Installed During Debug Build"
date: 2022-01-09
url: https://discourse.slicer.org/t/21369
---

# TBB libs are not installed during Debug build

**Topic ID**: 21369
**Date**: 2022-01-09
**URL**: https://discourse.slicer.org/t/tbb-libs-are-not-installed-during-debug-build/21369

---

## Post #1 by @keri (2022-01-09 15:55 UTC)

<p>Hi,</p>
<p>Currently Slicer 3D uses <a href="https://github.com/oneapi-src/oneTBB/releases/tag/2019_U9" rel="noopener nofollow ugc">TBB 2019 u9</a> (the link to the <a href="https://github.com/Slicer/Slicer/blob/4f1e6145ca84e46277e02c061d44e2139d84884e/SuperBuild/External_tbb.cmake#L14-L24" rel="noopener nofollow ugc">Slicer TBB external pkg</a>).</p>
<p>If you tak a looke at TBB assets for Window/Linux/Mac then you will notice that it uses different naming convention for release and debug libraries. Release libs are called <code>libtbb.so</code> and Debug <code>libtbb_debug.so</code>.</p>
<p>In the same time <a href="https://github.com/Slicer/Slicer/blob/4f1e6145ca84e46277e02c061d44e2139d84884e/CMake/SlicerBlockInstallTBB.cmake#L14-L41" rel="noopener nofollow ugc">SlicerBlockInstallTBB.cmake</a> handles only Release mode. So if the Slicer is compiled with TBB in Debug mode then installed Slicer should not work as it is unable to load debug TBB.</p>
<p>I’m not sure but I propose to add something like (UNIX example):</p>
<pre><code class="lang-auto">#----------UNIX CASE--------------#
install(
  FILES
    ${TBB_LIB_DIR}/libtbb.so.2
    ${TBB_LIB_DIR}/libtbbmalloc.so.2
    ${TBB_LIB_DIR}/libtbbmalloc_proxy.so.2
    CONFIGURATIONS Release
    DESTINATION ${TBB_INSTALL_LIB_DIR} COMPONENT Runtime)

install(
  FILES
    ${TBB_LIB_DIR}/libtbb_debug.so.2
    ${TBB_LIB_DIR}/libtbbmalloc_debug.so.2
    ${TBB_LIB_DIR}/libtbbmalloc_proxy_debug.so.2
    CONFIGURATIONS Debug
    DESTINATION ${TBB_INSTALL_LIB_DIR} COMPONENT Runtime)

if (CMAKE_BUILD_TYPE EQUAL "Release")
  slicerStripInstalledLibrary(
    FILES
      "${TBB_INSTALL_LIB_DIR}/libtbb.so.2"
      "${TBB_INSTALL_LIB_DIR}/libtbbmalloc.so.2"
      "${TBB_INSTALL_LIB_DIR}/libtbbmalloc_proxy.so.2"
    COMPONENT Runtime)
else ()
  slicerStripInstalledLibrary(
    FILES
      "${TBB_INSTALL_LIB_DIR}/libtbb_debug.so.2"
      "${TBB_INSTALL_LIB_DIR}/libtbbmalloc_debug.so.2"
      "${TBB_INSTALL_LIB_DIR}/libtbbmalloc_proxy_debug.so.2"
    COMPONENT Runtime)
endif()
</code></pre>
<p>If this is ok I could implement it in PR</p>

---

## Post #2 by @pieper (2022-01-09 15:57 UTC)

<p>That sounds reasonable to me.  Thanks for digging into this <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=10" title=":+1:" class="emoji" alt=":+1:"></p>

---

## Post #3 by @keri (2022-01-12 17:13 UTC)

<p><a href="https://github.com/Slicer/Slicer/pull/6110" rel="noopener nofollow ugc">Submitted a PR</a></p>
<p>I only tried to handle <code>Debug</code> and <code>Release</code> modes but cmake also supports <a href="https://cmake.org/cmake/help/latest/variable/CMAKE_BUILD_TYPE.html" rel="noopener nofollow ugc">RelWithDebInfo and MinSizeRel</a>.<br>
I don’t Know whether Slicer uses these build types but I don’t have experience of working with <code>RelWithDebInfo</code> and <code>MinSizeRel</code> thus I don’t know what libraries they need (debug or release).</p>
<p>Anyway I could to try fix this PR to handle <code>RelWithDebInfo</code> and <code>MinSizeRel</code> if needed.</p>

---

## Post #4 by @jamesobutler (2022-01-12 17:16 UTC)

<aside class="quote no-group" data-username="keri" data-post="1" data-topic="21369">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/keri/48/11618_2.png" class="avatar"> keri:</div>
<blockquote>
<p>So if the Slicer is compiled with TBB in Debug mode then installed Slicer should not work as it is unable to load debug TBB.</p>
</blockquote>
</aside>
<p>Can you describe how it doesn’t work? I’m sure others have built Slicer in debug mode, but there haven’t been any reports of things not working.</p>

---

## Post #5 by @keri (2022-01-12 17:42 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="4" data-topic="21369">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>I’m sure others have built Slicer in debug mode, but there haven’t been any reports of things not working.</p>
</blockquote>
</aside>
<p>You are right but I’m talking about installation (and packaging) like executing commands (assuming Slicer is built):</p>
<pre><code class="lang-auto">cd Slicer-build
cpack -B ../..
</code></pre>
<p>If you have built Slicer in <code>Debug</code> mode then Slicer is linked against <code>libtbb_debug.so</code>. That means if you want to install Slicer then you need to install <code>libtbb_debug.so</code> but Slicer installs <code>libtbb.so</code> instead. Thus when you try to run installed Slicer you should see something like <code>libtbb_debug.so not found</code> (but you have <code>libtbb.so</code> in the installation folder) and the app must fails to start. This happened to me on Ubuntu 20.04.</p>
<p>The idea behind <code>cmake install</code> used by me in PR is taken <a href="https://cmake.org/cmake/help/latest/command/install.html#:~:text=install(TARGETS%20target%0A%20%20%20%20%20%20%20%20CONFIGURATIONS%20Debug%0A%20%20%20%20%20%20%20%20RUNTIME%20DESTINATION%20Debug/bin)%0Ainstall(TARGETS%20target%0A%20%20%20%20%20%20%20%20CONFIGURATIONS%20Release%0A%20%20%20%20%20%20%20%20RUNTIME%20DESTINATION%20Release/bin)" rel="noopener nofollow ugc">from cmake the example</a></p>

---

## Post #6 by @pieper (2022-01-12 17:48 UTC)

<p>Generally speaking you aren’t meant to be making packages of debug or other non-release builds - I believe some tools won’t allow it or it’s against the license to redistribute the debug libs.  But I guess there might be times when you’d want to.</p>

---

## Post #7 by @keri (2022-01-12 17:53 UTC)

<p>Yes, and in my case I usually work with SlicerCAT and Debug mode. I needed to check whether I’m able able to correctly package the app or not (are there any bugs in my installation scripts).</p>

---

## Post #8 by @jcfr (2022-06-02 18:58 UTC)

<p>To follow up on this,  TBB version has been updated from <code>2019_U9</code> to <code>2021.5.0</code>.<br>
See <a href="https://github.com/Slicer/Slicer/pull/6405">https://github.com/Slicer/Slicer/pull/6405</a></p>
<p>The install rules have also been tested to make sure tbb release libraries are packaged.</p>
<p>That said, Debug libraries are still excluded. To support this, we would need to set the list of exceptions in  <a href="https://github.com/Slicer/Slicer/blob/177f3b324247de4e77d4497cc9121fe37dd5b3f3/CMake/SlicerFunctionInstallLibrary.cmake#L97-L98">SlicerFunctionInstallLibrary.cmake</a> based on the build type by checking the value of <code>CMAKE_BUILD_TYPE</code> (only  the case of single configuration generator).</p>

---
