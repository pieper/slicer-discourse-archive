---
topic_id: 29607
title: "Build When Git Commit Is Changed"
date: 2023-05-23
url: https://discourse.slicer.org/t/29607
---

# Build when git commit is changed

**Topic ID**: 29607
**Date**: 2023-05-23
**URL**: https://discourse.slicer.org/t/build-when-git-commit-is-changed/29607

---

## Post #1 by @aymeric.chataigner (2023-05-23 14:12 UTC)

<p>Hi,</p>
<p>3D slicer incremental build takes 8 minutes on my Linux PC if I simply put my git branch on another commit (even if this commit does not change any c++ code).</p>
<ul>
<li>Config: i7 12 cores and 32GB RAM</li>
<li>Build launch with this command in Slicer-build directory: make -j12</li>
</ul>
<p>It is caused by Slicer-build/vtkSlicerVersionConfigure.h which is modified each time the commit is changed in the source directory.</p>
<p>We could store the constants of vtkSlicerVersionConfigure.h in a file read once when Slicer is launched to save build time without any performance drawback.</p>
<p>What do you think ?</p>
<p>Any advice to speed up build is welcome <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>Best regards</p>

---

## Post #2 by @lassoan (2023-05-23 18:06 UTC)

<p>vtkSlicerVersionConfigure.h is needed for some <span class="hashtag">#ifdefs</span> that are used at compile time, so it would not be sufficient to make it available in a resource file only.</p>
<p>That said, a change in <code>vtkSlicerVersionConfigure.h</code> should not cause much rebuilding, as it is just used in a few cxx files (also in <code>qSlicerAbstractModule.h</code>, which could be probably removed), so it will just build and link a handful of libraries.</p>
<p>Could you please check if build takes a long time if you just update <code>vtkSlicerVersionConfigure.h</code>?<br>
If that does not take too long then it may be something else triggers the lenghty recompilations/linkings.</p>

---

## Post #3 by @pieper (2023-05-23 18:20 UTC)

<p>Any fixes that speed up incremental rebuilds would be very welcome.</p>

---

## Post #4 by @aymeric.chataigner (2023-05-24 09:38 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="29607">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>vtkSlicerVersionConfigure.h</p>
</blockquote>
</aside>
<p>Thanks for your quick answer.<br>
Incremental build still takes the same time if I just update vtkSlicerVersionConfigure.h.<br>
The first file recompiled is vtkMRMLVolumeSequenceStorageNode.cxx which is compiled quite quickly but then many linking must be done since it is in libMRMLCore which is used in many libs.<br>
In the next days I will try to minimize the use of <span class="hashtag-raw">#include</span> “vtkSlicerVersionConfigure.h” and propose a pull request.</p>

---

## Post #5 by @lassoan (2023-05-24 10:44 UTC)

<p><code>libMRMLCore</code> is supposed to be just an import library that loads the shared library. If the public interface of the library does not change then the import library does not change and no re-linking should occur. That’s why it is very important to avoid including <code>vtkSlicerVersionConfigure.h</code> in any header file. Try removing the include in <code>qSlicerAbstractModule.h</code>, it might solve the excessive rebuild issue.</p>

---

## Post #6 by @aymeric.chataigner (2023-05-24 13:07 UTC)

<p>Many links are done simply if:</p>
<ul>
<li>I modify vtkMRMLVolumeSequenceStorageNode.cxx (simply add a space to a comment)</li>
<li>launch build in Slicer-build (make -j12)<br>
A log screenshot is attached (I can provide the full log as a text file if you need it)</li>
</ul>
<p>Removing vtkSlicerVersionConfigure.h in qSlicerAbstractModule.h is nice but it does not make significant change because my problem is really linking time of each library which depends on libraries modified by vtkSlicerVersionConfigure.h.</p>
<p>I would like to propose this improvement:</p>
<ul>
<li>use a resource file everywhere it is possible</li>
<li>if information is required at build time: include vtkSlicerVersionConfigureInternal.h rather than vtkSlicerVersionConfigure.h<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/086f665ff1735f6f64d5c63bf535b070a87bb892.png" data-download-href="/uploads/short-url/1cCuyUcNah9InijdgYdetmpLHKG.png?dl=1" title="Screenshot from 2023-05-24 15-10-54" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/086f665ff1735f6f64d5c63bf535b070a87bb892_2_690x360.png" alt="Screenshot from 2023-05-24 15-10-54" data-base62-sha1="1cCuyUcNah9InijdgYdetmpLHKG" width="690" height="360" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/086f665ff1735f6f64d5c63bf535b070a87bb892_2_690x360.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/086f665ff1735f6f64d5c63bf535b070a87bb892_2_1035x540.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/086f665ff1735f6f64d5c63bf535b070a87bb892_2_1380x720.png 2x" data-dominant-color="341227"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2023-05-24 15-10-54</span><span class="informations">1852×967 227 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div>
</li>
</ul>

---

## Post #7 by @lassoan (2023-05-24 14:33 UTC)

<p>Removing references to vtkSlicerVersionConfigure.h in implementation (.cxx) files should not matter, as they should not trigger any relinking in other libraries. The .lib file is only modified when the public API (exported symbols in header files) is changed. When you change the content of a .cxx file then only the .so file is updated, which is not used during the linking (the content will only matter at runtime).</p>
<p>That said, I could reproduce the issue: touching <code>vtkMRMLVolumeSequenceStorageNode.cxx</code> and then running <code>make -j20</code> took 52 seconds (while without this change, make took 2 seconds).</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> Do you know what can cause this unnecessary re-linking?</p>

---

## Post #8 by @lassoan (2023-05-25 00:15 UTC)

<p>On Windows, the build works as it is supposed to. After modifying <code>vtkMRMLVolumeSequenceStorageNode.cxx</code> (not just whitespace change but actual implementation change) the build time is just 3 seconds longer. If no file is modified then build takes 14 seconds (due to Python hierarchy files are updated at every build); after modifying the storage node implementation, build takes just slightly longer - 17 seconds.</p>
<p><a class="mention" href="/u/pieper">@pieper</a> could you test it on macOS? How long <code>make -jN</code> takes for you on a non-modified build tree and how long does it take after you make a small change in <code>vtkMRMLVolumeSequenceStorageNode.cxx</code>?</p>

---

## Post #9 by @lassoan (2023-05-25 01:18 UTC)

<p><a class="mention" href="/u/aymeric.chataigner">@aymeric.chataigner</a> The problem can be fixed by adding <code>set(CMAKE_LINK_DEPENDS_NO_SHARED TRUE)</code> to the top-level CMakeLists.txt (near the top, for example right below the C++ standard section)!</p>
<p>If only the implementation (<code>vtkMRMLVolumeSequenceStorageNode.cxx</code>) is changed then rebuild takes a couple of seconds. If the header file (public interface) is changed then the rebuild takes about 30 seconds.</p>
<p>There is a very <a href="https://cmake-developers.cmake.narkive.com/dTGZ68X4/should-cmake-link-depends-no-shared-be-on-by-default">old discussion</a> about enabling this flag by default. Some people brought up some contrived examples and some tests failed (maybe just on Windows?), so at that time they did not enable the <code>CMAKE_LINK_DEPENDS_NO_SHARED</code> flag by default, and it seems that it is still disabled by default.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> do you think we should enable <code>CMAKE_LINK_DEPENDS_NO_SHARED</code> or we should set target linking properties more carefully to prevent the unnecessary relinking on linux?</p>

---

## Post #10 by @jcfr (2023-05-25 01:21 UTC)

<blockquote>
<p>[…]<code>vtkSlicerVersionConfigure.h</code> […]  in <code>qSlicerAbstractModule.h</code> […] could be probably removed,</p>
</blockquote>
<p>Indeed, this was added back in 2012 in the context of <a href="https://github.com/Slicer/Slicer/commit/b6aab58a26890b7cba929ce4a8917e51bcae9d1e">Slicer@b6aab58a2</a>.</p>
<p>Since then, in mid-2021, the approach has been revisited in <a href="https://github.com/Slicer/Slicer/commit/ae2e56b493138eaa9d9082951f49bb3d693a2a9d">Slicer@ae2e56b49</a> and there is no need have macro <code>Slicer_VERSION_MAJOR</code> and <code>Slicer_VERSION_MINOR</code> defined for module to compile.</p>
<p>Removing the include of <code>vtkSlicerVersionConfigure.h</code> in  <code>qSlicerAbstractModule.h</code>  should not be an issue for Slicer core.</p>
<p>And while it may affect some extension, it will be easy to fix.</p>

---

## Post #11 by @jcfr (2023-05-25 01:31 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="29607">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>should set target linking properties more carefully to prevent the unnecessary relinking on linux?</p>
</blockquote>
</aside>
<p>Ideally yes, this will happen organically as we start transitioning the build system to fully adopt the modern cmake paradigm where the usage requirements are all associated with our targets. See <a href="https://cmake.org/cmake/help/latest/manual/cmake-buildsystem.7.html#build-specification-and-usage-requirements">here</a></p>
<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="29607">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>should enable <code>CMAKE_LINK_DEPENDS_NO_SHARED</code></p>
</blockquote>
</aside>
<p>In the meantime, enabling this option to improve the develop experience seems reasonable.</p>
<p>I just sent a quick note to our Kitware CMake channel to ask if there any caveats folks may be aware of.</p>

---

## Post #12 by @jcfr (2023-05-25 01:52 UTC)

<p>Once the inner-build has been reconfigured with <code>CMAKE_LINK_DEPENDS_NO_SHARED</code> set to <code>ON</code> and at least built once.</p>
<p>After modifying one implementation file</p>
<pre><code class="lang-auto">$ touch ../../Slicer/Libs/MRML/Core/vtkMRMLScene.cxx 
</code></pre>
<p>We can observe (on Linux) that beside the rebuilding of <code>libMRMLCore.so</code> no relinking happen for any of the dependencies:</p>
<pre><code class="lang-auto">$ make -j10 
[...]
[ 24%] Building CXX object Libs/MRML/Core/CMakeFiles/MRMLCore.dir/vtkMRMLScene.cxx.o
[ 24%] Linking CXX shared library ../../../bin/libMRMLCore.so
[ 26%] Built target MRMLCore
[ 26%] Built target MRMLCLI
[...]
[ 98%] Built target qSlicerTablesModuleCxxTests
[ 99%] Built target qSlicerTablesModuleGenericCxxTests
[ 99%] Built target qSlicerMarkupsModuleCxxTests
[ 99%] Built target qSlicerVolumeRenderingModuleGenericCxxTests
[100%] Built target qSlicerVolumeRenderingModuleCxxTests</code></pre>

---

## Post #13 by @aymeric.chataigner (2023-05-25 09:56 UTC)

<p>Thanks a lot for your help.</p>
<p>I set CMAKE_LINK_DEPENDS_NO_SHARED to ON and I removed <span class="hashtag">#include</span> “vtkSlicerVersionConfigure.h” in qSlicerAbstractModule</p>
<p>Now if I build after a change in vtkSlicerVersionConfigure.h (like it is done by cmake when my git branch goes onto the next commit which just changes README.md) it takes 2min30s rather than 8min.</p>
<p>Should I propose a Pull Request for this simple changes ?</p>
<p>Naturally It would be nicer if a simple commit change should cause NO compilation, NO link.</p>
<p>As I said before, could I propose a pull request which:</p>
<ul>
<li>use a resource file everywhere it is possible</li>
<li>if information is required at build time: include vtkSlicerVersionConfigureInternal.h rather than vtkSlicerVersionConfigure.h if it is possible</li>
</ul>

---

## Post #14 by @pieper (2023-05-25 13:31 UTC)

<p>With current source, no cmake changes on Mac pro.  Rebuilding Slicer-build with make -j50:</p>
<p>No changes: 8 seconds</p>
<p>Touching <code>vtkMRMLVolumeSequenceStorageNode.cxx</code>: 45 seconds (lots of relinking).</p>

---

## Post #15 by @lassoan (2023-05-25 15:09 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a> thanks for testing!</p>
<p><a class="mention" href="/u/aymeric.chataigner">@aymeric.chataigner</a> Can you confirm that building after touching <code>vtkMRMLVolumeSequenceStorageNode.cxx</code> just takes a couple of seconds now? That means that we solved a large part of the problem!</p>
<aside class="quote no-group" data-username="aymeric.chataigner" data-post="13" data-topic="29607">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/aymeric.chataigner/48/4977_2.png" class="avatar"> aymeric.chataigner:</div>
<blockquote>
<p>As I said before, could I propose a pull request which:</p>
<ul>
<li>use a resource file everywhere it is possible</li>
<li>if information is required at build time: include vtkSlicerVersionConfigureInternal.h rather than vtkSlicerVersionConfigure.h if it is possible</li>
</ul>
</blockquote>
</aside>
<p>Cleaning up <code>vtkSlicerVersionConfigure.h</code> includes would be nice, it would be great if you could work on it. I think there are a couple of places where it is simply not needed.</p>
<p>Using a resource file will probably not be necessary, because it is simpler to get version information at runtime using qSlicerCoreApplication methods.</p>
<p>As its name (and comment in the file header) suggests, <code>vtkSlicerVersionConfigureInternal.h</code> is for internal use - only to be included in <code>vtkSlicerVersionConfigure.h</code> and not to be used in modules. We could rename and repurpose this .h file, but I’m not sure if it is worth it (if it can lead to significant build time reduction). What classes you would replace the include with the internal?</p>

---

## Post #16 by @aymeric.chataigner (2023-05-25 16:05 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="15" data-topic="29607">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Can you confirm that building after touching <code>vtkMRMLVolumeSequenceStorageNode.cxx</code> just takes a couple of seconds now?</p>
</blockquote>
</aside>
<p>Yes !</p>
<aside class="quote no-group" data-username="lassoan" data-post="15" data-topic="29607">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>As its name (and comment in the file header) suggests, <code>vtkSlicerVersionConfigureInternal.h</code> is for internal use - only to be included in <code>vtkSlicerVersionConfigure.h</code> and not to be used in modules. We could rename and repurpose this .h file, but I’m not sure if it is worth it (if it can lead to significant build time reduction). What classes you would replace the include with the internal?</p>
</blockquote>
</aside>
<p>In my wip branch I replaced it in:<br>
vtkMRMLVolumeSequenceStorageNode.cxx<br>
vtkMRMLMarkupsFiducialStorageNode.cxx<br>
qSlicerApplicationHelper.cxx</p>
<p>I will try to continue tomorrow and I will let you know.</p>

---

## Post #17 by @lassoan (2023-05-25 17:09 UTC)

<p>vtkMRMLVolumeSequenceStorageNode → The version check can be removed and we can just use the code snippet in the <code>Slicer_VERSION_MAJOR &gt; 4</code> branch.</p>
<p>vtkMRMLMarkupsFiducialStorageNode → it uses <code>Slicer_VERSION</code>, which is not available in vtkSlicerVersionConfigureInternal.h, so I think we need to keep using vtkSlicerVersionConfigure.h. It is just an implementation file in a small library, so recompiling&amp;linking should not take more than a few seconds anyway.</p>
<p>qSlicerApplicationHelper → it uses <code>Slicer_MAIN_PROJECT_VERSION_FULL</code>, which is not available in vtkSlicerVersionConfigureInternal.h, so I think we need to keep using vtkSlicerVersionConfigure.h. If you find the recompilation of this file makes a huge difference then we can have a look how to avoid it.</p>

---

## Post #18 by @aymeric.chataigner (2023-05-30 14:18 UTC)

<p>Thanks again for <a href="https://github.com/Slicer/Slicer/pull/6983#issuecomment-1567916267" class="inline-onebox" rel="noopener nofollow ugc">COMP: Speed up incremental build on Linux by achataigner · Pull Request #6983 · Slicer/Slicer · GitHub</a></p>
<p>I also had to do that in SlicerRT: <a href="https://github.com/SlicerRt/SlicerRT/pull/230" class="inline-onebox" rel="noopener nofollow ugc">COMP: remove use of constants defined in vtkSlicerVersionConfigure.h by achataigner · Pull Request #230 · SlicerRt/SlicerRT · GitHub</a></p>

---

## Post #19 by @jamesobutler (2023-05-31 22:12 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="10" data-topic="29607">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>And while it may affect some extension, it will be easy to fix.</p>
</blockquote>
</aside>
<ul>
<li>SlicerRT <a href="https://slicer.cdash.org/viewBuildError.php?buildid=3045350" rel="noopener nofollow ugc">build error</a>
<ul>
<li>Fix → <a href="https://github.com/SlicerRt/SlicerRT/pull/230" class="inline-onebox" rel="noopener nofollow ugc">COMP: remove use of constants defined in vtkSlicerVersionConfigure.h by achataigner · Pull Request #230 · SlicerRt/SlicerRT · GitHub</a></li>
</ul>
</li>
<li>SlicerDMRI <a href="https://slicer.cdash.org/viewBuildError.php?buildid=3045378" rel="noopener nofollow ugc">build error</a></li>
<li>Chest_Imaging_Platform <a href="https://slicer.cdash.org/viewBuildError.php?buildid=3045361" rel="noopener nofollow ugc">build error</a></li>
</ul>

---

## Post #20 by @aymeric.chataigner (2023-06-05 09:51 UTC)

<p>I proposed these PR to continue to save more time during incremetal build:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/7001">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/7001" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/7001" target="_blank" rel="noopener nofollow ugc">COMP: Speed up incremental build</a>
      </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>achataigner:aymeric/speed-up-incremental-build-after-commit-changing</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2023-06-05" data-time="08:13:33" data-timezone="UTC">08:13AM - 05 Jun 23 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/achataigner" target="_blank" rel="noopener nofollow ugc">
            <img alt="achataigner" src="https://avatars.githubusercontent.com/u/3016648?v=4" class="onebox-avatar-inline" width="20" height="20">
            achataigner
          </a>
        </div>

        <div class="lines" title="1 commits changed 9 files with 29 additions and 40 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/7001/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+29</span>
            <span class="removed">-40</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">vtkSlicerVersionConfigureInternal.h is renamed vtkSlicerVersionConfigureMinimal.<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/7001" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">h.

#include "vtkSlicerVersionConfigure.h" is replaced by #include "vtkSlicerVersionConfigureMinimal.h" when it is possible, therefore no compilation is required if git commit is changed.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/SlicerRt/SlicerRT/pull/231">
  <header class="source">

      <a href="https://github.com/SlicerRt/SlicerRT/pull/231" target="_blank" rel="noopener nofollow ugc">github.com/SlicerRt/SlicerRT</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/SlicerRt/SlicerRT/pull/231" target="_blank" rel="noopener nofollow ugc">Aymeric/speedup incremental build</a>
      </h4>

    <div class="branches">
      <code>SlicerRt:master</code> ← <code>achataigner:aymeric/speedup-incremental-build</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2023-06-05" data-time="08:15:53" data-timezone="UTC">08:15AM - 05 Jun 23 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/achataigner" target="_blank" rel="noopener nofollow ugc">
            <img alt="achataigner" src="https://avatars.githubusercontent.com/u/3016648?v=4" class="onebox-avatar-inline" width="20" height="20">
            achataigner
          </a>
        </div>

        <div class="lines" title="2 commits changed 6 files with 12 additions and 7 deletions">
          <a href="https://github.com/SlicerRt/SlicerRT/pull/231/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+12</span>
            <span class="removed">-7</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Apply required changes from https://github.com/Slicer/Slicer/pull/7001</p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>On my PC with ubuntu 20.04 running an intel i7 6 hyperthreaded cores:<br>
If I do make -j12:<br>
Build slicer incremental: 35 seconds rather than 40 seconds<br>
Build slicerRT incremental: 30 seconds rather than 1 minute</p>

---

## Post #21 by @aymeric.chataigner (2023-06-08 08:06 UTC)

<p>Hi all, could I have some feedback on my github pull request ?</p>

---

## Post #22 by @aymeric.chataigner (2023-08-21 14:35 UTC)

<p>Hi all,</p>
<p>I would like to do the final step: put the content of the new vtkSlicerVersionConfigure.h into a resource file which is read at runtime in /home/aymeric/dev/slicer/Base/QTCore/qSlicerCoreApplication.cxx.<br>
Did you already plan to do it ?<br>
Do you have any idea/advice to implement it correctly ?</p>
<p>Best regards</p>

---

## Post #23 by @jcfr (2023-08-21 14:51 UTC)

<p>Since the current use of the macro is for conditionally including code at compile time, i am not this approach would work here.</p>
<p>That said, i suggest we list the current use of the macros to make the final call.</p>

---

## Post #24 by @aymeric.chataigner (2023-08-21 15:06 UTC)

<p>I have not found code which uses the constant of vtkSlicerVersionConfigure.h (not vtkSlicerVersionConfigureMinimal.h) in <span class="hashtag-raw">#if</span> or <span class="hashtag-raw">#ifdef</span> statements.</p>
<p>Am I wrong ?</p>

---

## Post #25 by @jcfr (2023-08-21 17:21 UTC)

<p>Inspecting the source files, we can see the following files directly including <code>vtkSlicerVersionConfigure.h</code>:</p>
<pre><code class="lang-auto">$ pwd
/path/to/Slicer
</code></pre>
<pre><code class="lang-auto">$ ack --cpp vtkSlicerVersionConfigure\.h
Base/Logic/Testing/vtkSlicerVersionConfigureTest1.cxx
21:#include "vtkSlicerVersionConfigure.h"

Base/QTGUI/qSlicerApplication.cxx
41:#include &lt;vtkSlicerVersionConfigure.h&gt; // For Slicer_VERSION_FULL

Base/QTApp/qSlicerApplicationHelper.cxx
43:#include "vtkSlicerVersionConfigure.h" // For Slicer_MAIN_PROJECT_VERSION_FULL

Base/QTCore/Testing/Cxx/qSlicerUtilsTest1.cxx
36:#include "vtkSlicerVersionConfigure.h"

Base/QTCore/qSlicerCoreApplication.cxx
138:#include "vtkSlicerVersionConfigure.h"

Applications/SlicerApp/Main.cxx
25:#include "vtkSlicerVersionConfigure.h" // For Slicer_VERSION_FULL
</code></pre>
<p>… then reading the comments in the respective <code>.cxx</code> files you will be able to assess which macro are used.</p>

---

## Post #26 by @jcfr (2023-08-21 18:01 UTC)

<p>After modifying <code>vtkSlicerVersionConfigure.h</code>, the following executable and libraries are rebuilt:</p>
<pre><code class="lang-auto">bin/SlicerBaseLogicCxxTests
bin/libqSlicerBaseQTCore.so
bin/qSlicerBaseQTCoreCxxTests
libqSlicerBaseQTGUI.so
libqSlicerBaseQTApp.so
SlicerApp-real
</code></pre>
<p>Details output:</p>
<pre><code class="lang-auto">$ touch vtkSlicerVersionConfigure.h

$ make 
[  0%] Configuring vtkSlicerVersionConfigure.h
-- Configuring Slicer release type [Experimental]
-- Found Git: /usr/bin/git  
-- Configuring Slicer version [5.5.0-2023-08-21]
-- Configuring Slicer revision [32141]
[  0%] Built target SlicerConfigureVersionHeader
[...]
[ 42%] Building CXX object Base/Logic/Testing/CMakeFiles/SlicerBaseLogicCxxTests.dir/vtkSlicerVersionConfigureTest1.cxx.o
[ 42%] Linking CXX executable ../../../bin/SlicerBaseLogicCxxTests
[...]
[ 42%] Building CXX object Base/QTCore/CMakeFiles/qSlicerBaseQTCore.dir/qSlicerCoreApplication.cxx.o
[ 42%] Linking CXX shared library ../../bin/libqSlicerBaseQTCore.so
[...]
[ 43%] Building CXX object Base/QTCore/Testing/Cxx/CMakeFiles/qSlicerBaseQTCoreCxxTests.dir/qSlicerUtilsTest1.cxx.o
[ 43%] Linking CXX executable ../../../../bin/qSlicerBaseQTCoreCxxTests
[...]
[ 43%] Building CXX object Base/QTGUI/CMakeFiles/qSlicerBaseQTGUI.dir/qSlicerApplication.cxx.o
[ 44%] Linking CXX shared library ../../bin/libqSlicerBaseQTGUI.so
[...]
[ 50%] Building CXX object Base/QTApp/CMakeFiles/qSlicerBaseQTApp.dir/qSlicerApplicationHelper.cxx.o
[ 50%] Linking CXX shared library ../../bin/libqSlicerBaseQTApp.so
[...]
[ 95%] Built target qSlicerApp
Consolidate compiler generated dependencies of target SlicerApp
[ 95%] Building CXX object Applications/SlicerApp/CMakeFiles/SlicerApp.dir/Main.cxx.o
[ 95%] Linking CXX executable ../../bin/SlicerApp-real
[...]
[100%] Built target SlicerDesignerConfigureLauncher
</code></pre>

---
