---
topic_id: 20497
title: "Speeding Up Slicer Builds With Ccache"
date: 2021-11-05
url: https://discourse.slicer.org/t/20497
---

# Speeding up Slicer builds with CCache

**Topic ID**: 20497
**Date**: 2021-11-05
**URL**: https://discourse.slicer.org/t/speeding-up-slicer-builds-with-ccache/20497

---

## Post #1 by @RafaelPalomar (2021-11-05 13:49 UTC)

<p>Building 3D Slicer is a very slow process. I’ve been experimenting with CCache to try speeding the process up and came up with this <a href="https://github.com/Slicer/Slicer/pull/5998" rel="noopener nofollow ugc">PR #5998</a>. Here some background information for this idea.</p>
<h1><a name="p-69231-what-is-ccache-1" class="anchor" href="#p-69231-what-is-ccache-1" aria-label="Heading link"></a>What is CCache?</h1>
<p>Ccache is a compiler cache. It <a href="https://ccache.dev/performance.html" rel="noopener nofollow ugc">speeds up recompilation</a> by caching previous compilations and detecting when the same compilation is being done again. The first time compilation has no performance benefit, but subsequent compilations will benefit from a performance increase.</p>
<p>CCache is well tested on Linux and MacOS. On Windows, it is not fully supported, though it could work (<a href="https://ccache.dev/platform-compiler-language-support.html" rel="noopener nofollow ugc">CCache support</a>). The proposed Slicer integration only considers Unix systems (Linux/MacOS).</p>
<h1><a name="p-69231-first-results-2" class="anchor" href="#p-69231-first-results-2" aria-label="Heading link"></a>First results</h1>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/ed6aae52ef9c87d0fef7f06cabf8060dc17ca2dd.png" data-download-href="/uploads/short-url/xShIQGGI40a2GSB1bt9oIcQP5Q9.png?dl=1" title="ccache" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/ed6aae52ef9c87d0fef7f06cabf8060dc17ca2dd_2_690x387.png" alt="ccache" data-base62-sha1="xShIQGGI40a2GSB1bt9oIcQP5Q9" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/ed6aae52ef9c87d0fef7f06cabf8060dc17ca2dd_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/ed6aae52ef9c87d0fef7f06cabf8060dc17ca2dd_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/ed6aae52ef9c87d0fef7f06cabf8060dc17ca2dd.png 2x" data-dominant-color="E7ECF1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ccache</span><span class="informations">1141×641 35.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>These results have been obtained with:</p>
<ul>
<li>Intel(R) Xeon(R) CPU E3-1535M v6 @ 3.10GHz</li>
<li>M.2 memory for the cache</li>
</ul>
<h1><a name="p-69231-how-to-use-it-pr-5998httpsgithubcomslicerslicerpull5998-3" class="anchor" href="#p-69231-how-to-use-it-pr-5998httpsgithubcomslicerslicerpull5998-3" aria-label="Heading link"></a>How to use it? <a href="https://github.com/Slicer/Slicer/pull/5998" rel="noopener nofollow ugc">PR #5998</a></h1>
<ul>
<li>Install ccache in your system (e.g., <code>apt install ccache</code> in Ubuntu)</li>
<li>Configure Slicer with <code>-DSlicer_USE_CCACHE=ON</code></li>
<li>Build a fresh Slicer so CCache can do the caching.</li>
<li>Subsequent slicer builds (even from fresh repo clones) will use the cache (given that <code>-DSlicer_USE_CCACHE=ON</code>).</li>
</ul>
<h1><a name="p-69231-discussion-4" class="anchor" href="#p-69231-discussion-4" aria-label="Heading link"></a>Discussion</h1>
<p>Considering the initial results, I think this can be useful for developers who deal with multiple builds of Slicer (e.g., spawning multiple Slicer worktrees from the same repository to attend different issues). If used for the continuous integration process (e.g., nightly build of pre-cached containers that will be used for CI), this could potentially reduce the energy footprint of the project and lead to more agile CI. I think it would be also interesting to publish the pre-cached containers so they can be used as building environment with all the speedup benefits.</p>
<p>Please, feel free to give feedback on this idea.</p>

---

## Post #2 by @lassoan (2021-11-05 15:47 UTC)

<p>Thank you for working on this.</p>
<p>Based on what you have described above and what is in <a href="https://ccache.dev/">“Why bother?” section</a> it is not clear how ccache could be useful for me. In general I try to avoid working on multiple branches at once. While I have a few build trees on some of my computers that I use for parallel developments, these have to be built only once, and re-compiled hundreds of times, so speeding up the first compilation does not matter much.</p>
<p>Using ccache has several limitations/disadvantages:</p>
<ul>
<li>I don’t see how this could work for debug symbol (pdb) files. If there are no debug symbols then this is completely unusable for debug builds.</li>
<li>There is a slight slowdown of every build for those files that has actually changed due to cache check and update. This happens most of the time during development (when I modify a file, build, and test). I’ve seen 10% slowdown reported for a similar build cache project.</li>
<li>The cache takes disk space, which may matter on the very fast but relatively small SSD drives, especially on laptops.</li>
<li>It complicates the build process and may introduce errors. I very rarely do a clean build and when I do then I want to make sure that it is completely clean and no previously cached content can play any role. I don’t think it is possible to make it robust for changing environment and potential CMake errors (e.g., if dependencies are not handled correctly then ccache make it worse/may expose it more often).</li>
</ul>
<p>Caching could be useful for continuous integration, though. In that use case the above limitations are not relevant and we indeed rebuild the same files in the same build environment potentially many times. While we cache all the dependencies in the docker image, there is no caching of the Slicer build files. Caching could speed up these builds significantly.</p>
<p>The implementation of patching numerous CMakeLists.txt files seems a bit too invasive. In Paraview they enable ccache by <a href="https://www.paraview.org/Wiki/ITK/Release_4/Wrapping/ccache">using symbolic links</a>. We could easily do this in the Slicer’s docker image (a complication could be to share these cache files, but maybe we could store in the image itself). Alternatively, since in Slicer’s build system we already pass the compiler executable (CMAKE_CXX_COMPILER) to all external projects, could we just change the value of this variable to the ccache executable?</p>

---

## Post #3 by @RafaelPalomar (2021-11-05 20:48 UTC)

<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a> for your insights.</p>
<p>I agree with you on that the benefits for continuous integration are more evident than for developers. Different developers have different use cases and workflows, and the only way to say for sure <code>ccache</code> works for you is to use it for a while and look at the cache statistics (<code>ccache -s</code>). There are some other points I’m not completely aligned with:</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="20497">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>There is a slight slowdown of every build for those files that has actually changed due to cache check and update. This happens most of the time during development (when I modify a file, build, and test). I’ve seen 10% slowdown reported for a similar build cache project.</p>
</blockquote>
</aside>
<p>That is true, caching has an overhead. Arguably, more often than not, your code changes are local and 10% increase on quick compilations will not be noticed by the developer. A 5x speedup on large compilations, however, will be noticeable every time. There are also situations where infrastructure code (CMake, etc.) can trigger unnecessary compilations of large portions of the project. an example of this is building a fresh Slicer (<code>make</code>) and hitting <code>make</code> again; even if the project was just built, there will be a substantial recompilation. For these cases, <code>ccache</code> gets you covered.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="20497">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>The cache takes disk space, which may matter on the very fast but relatively small SSD drives, especially on laptops.</p>
</blockquote>
</aside>
<p>In my tests, I have a cache smaller than 4GB for Slicer. I think it is pretty affordable, but I guess this is a use-case consideration.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="20497">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It complicates the build process and may introduce errors. I very rarely do a clean build and when I do then I want to make sure that it is completely clean and no previously cached content can play any role. I don’t think it is possible to make it robust for changing environment and potential CMake errors (e.g., if dependencies are not handled correctly then ccache make it worse/may expose it more often).</p>
</blockquote>
</aside>
<p><code>ccache </code> is very robust. The caching is based on  1) compiler binary and timestamp, 2) compiler options used, 3) contents of the source code file and 4) contents of all the included files. All fo these give a pretty good fingerprint. I have been using <code>ccache</code> to build Gentoo for years; Gentoo compiles every package in the operating system in a rolling-release fashion, and there, changing of environment is very frequent. I would trust more a <code>ccache</code> fresh build than a build directory used over different branches.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="20497">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>The implementation of patching numerous CMakeLists.txt files seems a bit too invasive. In Paraview they enable ccache by <a href="https://www.paraview.org/Wiki/ITK/Release_4/Wrapping/ccache" rel="noopener nofollow ugc">using symbolic links</a>.</p>
</blockquote>
</aside>
<p>I agree that patching <code>CMakeLists.txt</code> wasn’t what I like as a way of doing things. It is also true that the implementation is very succinct (to me it looks just minimally invasive) and it does not alter the behavior of the underlying libraries, just they way they are built. I think the ideal scenario would be to convince the underlying projects to introduce a flag for ccache (SimpleITK, for instance, has it already). I don’t like the symlinking approach because you have to modify globally your OS for one of its projects; it is easy to forget that your compiler is now something else and you may use cache space for projects you are not interested in. This could be a valid approach for continuous integration, though.</p>
<p>I haven’t had a look at changing CMAKE_CXX_COMPILER, maybe that does the trick. I’ll give it a try and let you know.</p>
<p>Maybe using CCache for continuous integration could be a good ProjectWeek project?</p>

---

## Post #4 by @jcfr (2021-11-05 21:16 UTC)

<p><a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a></p>
<p>Thanks for the thorough description and pull request <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=15" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"></p>
<p>Initiative to improve the developer experience are great <img src="https://emoji.discourse-cdn.com/twitter/fire.png?v=15" title=":fire:" class="emoji" alt=":fire:" loading="lazy" width="20" height="20"></p>
<p>Also, thanks again for your patience and time working through this <img src="https://emoji.discourse-cdn.com/twitter/100.png?v=15" title=":100:" class="emoji" alt=":100:" loading="lazy" width="20" height="20"></p>
<h2><a name="p-69255-alternative-approach-1" class="anchor" href="#p-69255-alternative-approach-1" aria-label="Heading link"></a>Alternative approach</h2>
<p>Did you consider this approach to configure Slicer ?</p>
<pre data-code-wrap="bash"><code class="lang-bash">cd Slicer-build

CC=/path/to/ccache  \
CXX=/path/to/ccache \
cmake -DQt5_DIR:PATH=/path/to/Qt5 ../Slicer
</code></pre>
<h3><a name="p-69255-ctestuselaunchers-2" class="anchor" href="#p-69255-ctestuselaunchers-2" aria-label="Heading link"></a>CTestUseLaunchers</h3>
<p>Setting the property <code>RULE_LAUNCH_COMPILE</code> in projects (as currently proposed in <a href="https://github.com/Slicer/Slicer/pull/5998/files#diff-1e7de1ae2d059d21e1dd75d5812d5a34b0222cef273b7c3a2af62eb747f9d20aR8-R10">PR-5998</a>)  may conflict with the  <a href="https://cmake.org/cmake/help/latest/module/CTestUseLaunchers.html#module:CTestUseLaunchers">CTestUseLaunchers</a></p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Kitware/CMake/blob/463e17b095d062011b8e44993558a95c02f09fb9/Modules/CTestUseLaunchers.cmake#L70">
  <header class="source">

      <a href="https://github.com/Kitware/CMake/blob/463e17b095d062011b8e44993558a95c02f09fb9/Modules/CTestUseLaunchers.cmake#L70" target="_blank" rel="noopener">github.com/Kitware/CMake</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Kitware/CMake/blob/463e17b095d062011b8e44993558a95c02f09fb9/Modules/CTestUseLaunchers.cmake#L70" target="_blank" rel="noopener">Modules/CTestUseLaunchers.cmake</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/Kitware/CMake/blob/463e17b095d062011b8e44993558a95c02f09fb9/Modules/CTestUseLaunchers.cmake#L70" rel="noopener"><code>463e17b09</code></a>
</div>



    <pre class="onebox"><code class="lang-cmake">
      <ol class="start lines" start="60" style="counter-reset: li-counter 59 ;">
          <li></li>
          <li>  set(CTEST_LAUNCH_COMPILE</li>
          <li>    "\"${CMAKE_CTEST_COMMAND}\" --launch ${__launch_compile_options} --")</li>
          <li></li>
          <li>  set(CTEST_LAUNCH_LINK</li>
          <li>    "\"${CMAKE_CTEST_COMMAND}\" --launch ${__launch_link_options} --")</li>
          <li></li>
          <li>  set(CTEST_LAUNCH_CUSTOM</li>
          <li>    "\"${CMAKE_CTEST_COMMAND}\" --launch ${__launch_custom_options} --")</li>
          <li></li>
          <li class="selected">  set_property(GLOBAL PROPERTY RULE_LAUNCH_COMPILE "${CTEST_LAUNCH_COMPILE}")</li>
          <li>  set_property(GLOBAL PROPERTY RULE_LAUNCH_LINK "${CTEST_LAUNCH_LINK}")</li>
          <li>  set_property(GLOBAL PROPERTY RULE_LAUNCH_CUSTOM "${CTEST_LAUNCH_CUSTOM}")</li>
          <li>endif()</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @RafaelPalomar (2021-11-05 21:33 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> thanks a lot for checking this out. Any attempt to change CMAKE_CXX_COMPILER/CMAKE_C_COMPILER or setting CXX/C variables leads to:</p>
<pre><code class="lang-auto">CMake Error at /usr/share/cmake-3.18/Modules/CMakeTestCCompiler.cmake:66 (message):
  The C compiler

    "/usr/bin/ccache"

  is not able to compile a simple test program.

  It fails with the following output:

    Change Dir: /home/rafael/src/Slicer/slicer-ccache/build/CMakeFiles/CMakeTmp
    
    Run Build Command(s):/usr/bin/ninja cmTC_4dcff &amp;&amp; [1/2] Building C object CMakeFiles/cmTC_4dcff.dir/testCCompiler.c.o
    FAILED: CMakeFiles/cmTC_4dcff.dir/testCCompiler.c.o 
    /usr/bin/ccache    -o CMakeFiles/cmTC_4dcff.dir/testCCompiler.c.o -c testCCompiler.c
    ccache: error: missing equal sign in "CMakeFiles/cmTC_4dcff.dir/testCCompiler.c.o"
    ninja: build stopped: subcommand failed. 
</code></pre>

---

## Post #6 by @lassoan (2021-11-05 21:53 UTC)

<p>This may be useful: <a href="https://cristianadam.eu/20200113/speeding-up-c-plus-plus-github-actions-using-ccache/" class="inline-onebox">Speeding up C++ GitHub Actions using ccache - Cristian Adam</a> - it seems that you need to pass <code>CMAKE_C_COMPILER_LAUNCHER</code> and <code>CMAKE_CXX_COMPILER_LAUNCHER</code> flags to the external project.</p>
<p>Based on comments in this page, ccache does not support debug symbols (pdb files), so ccache is not suitable for debug builds (at least on Windows).</p>

---

## Post #7 by @jcfr (2021-11-05 21:59 UTC)

<p>Thanks for the report.</p>
<p>Following these instructions may be helpful. See <a href="https://ccache.dev/manual/4.4.2.html#_run_modes">https://ccache.dev/manual/4.4.2.html#_run_modes</a></p>
<p>After setting up the symlinks into the directory of your choice, you would then set CC and CXX to the relevant"compiler" symlinks.</p>

---

## Post #8 by @RafaelPalomar (2021-11-09 13:36 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> thanks for the info. Symlinking and setting <code>CMAKE_CXX_COMPILER</code> and <code>CMAKE_C_COMPILER</code> seems to do the trick. This approach has the advantage that everything will be “ccached”; in <a href="https://github.com/Slicer/Slicer/pull/5998/files#diff-1e7de1ae2d059d21e1dd75d5812d5a34b0222cef273b7c3a2af62eb747f9d20aR8-R10" rel="noopener nofollow ugc">PR-5998</a> not everything is “ccached” (e.g., subprojects of external dependencies such as PythonQt)</p>
<aside class="quote no-group" data-username="jcfr" data-post="4" data-topic="20497">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<h3>CTestUseLaunchers</h3>
<p>Setting the property <code>RULE_LAUNCH_COMPILE</code> in projects (as currently proposed in <a href="https://github.com/Slicer/Slicer/pull/5998/files#diff-1e7de1ae2d059d21e1dd75d5812d5a34b0222cef273b7c3a2af62eb747f9d20aR8-R10" rel="noopener nofollow ugc">PR-5998</a>) may conflict with the <a href="https://cmake.org/cmake/help/latest/module/CTestUseLaunchers.html#module:CTestUseLaunchers" rel="noopener nofollow ugc">CTestUseLaunchers</a></p>
</blockquote>
</aside>
<p><a class="mention" href="/u/jcfr">@jcfr</a> I have run CTest after a fresh build with ccache and it does not seem to be any problems if that helps on this point.</p>

---

## Post #9 by @RafaelPalomar (2021-11-09 13:37 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> as for now ccache can only be enabled on UNIX systems. It seems ccache has not the same level of support for Windows users. For linux I could debug without problems in a ccached build.</p>

---

## Post #10 by @RafaelPalomar (2021-11-09 13:42 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> , <a class="mention" href="/u/lassoan">@lassoan</a>. Maybe we can discuss this in the next developers meeting. There’s no need to rush this in if there are concerns and available alternatives.</p>
<p>Thank you both for the nice discussion.</p>

---
