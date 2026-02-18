# Ninja build using too many cores

**Topic ID**: 2304
**Date**: 2018-03-13
**URL**: https://discourse.slicer.org/t/ninja-build-using-too-many-cores/2304

---

## Post #1 by @ihnorton (2018-03-13 16:22 UTC)

<p>Is anyone else using ninja to build on mac? Lately I’m noticing that <code>ninja -j2</code> in <code>Slicer-build</code> runs 8 clang processes simultaneously, which floors the (2-core) computer and the build absolutely crawls (one <code>.o</code> file every 2-3 seconds). I expect this for some parallel projects during superbuild, because I don’t think we’re using job pool support. But within <code>Slicer-build</code> I thought it should only be building one project so cmake+ninja should respect <code>-j2</code>.</p>
<p>(CMake 3.9.4, macOS 10.12)</p>

---

## Post #2 by @jcfr (2018-03-13 17:12 UTC)

<p>The way forward could be to:</p>
<ul>
<li>
<p>Use CMake 3.11 to benefit from this fix: <a href="https://github.com/Kitware/CMake/commit/07185055d57f28347a1850a1f06787ac93f20afd">Ninja: add CMAKE_JOB_POOLS variable as default for JOBS_POOLS </a></p>
</li>
<li>
<p>Improve <a href="https://github.com/commontk/Artichoke/blob/master/ExternalProjectDependency.cmake">ExternalProjectDependency</a> (and update the version of the module user in Slicer and CTK) so that it pass the variables <code>CMAKE_JOB_POOLS</code>, <code>CMAKE_JOB_POOL_COMPILE</code> and <code>CMAKE_JOB_POOL_LINK</code> to any CMake based external project project if their are set.</p>
</li>
</ul>
<p>You could then configure the top-level project using <code>-DCMAKE_JOB_POOLS:STRING=compile=5;link=2</code>.</p>
<p>This would mean that each instance of ninja would be limited to 5 compile jobs and 2 linker job.</p>
<p>Would that be helpful ?  It may be worth exploring what would be sensible setup for Slicer.</p>

---

## Post #3 by @ihnorton (2018-03-14 03:52 UTC)

<p>Do you know of other projects using job pools + externalproject? From my understanding, I don’t think it would help because each EP spawns a separate ninja instance, and ninja/cmake don’t have any way to communicate a rate-limit across sub-projects (from what I can tell job pool is designed for rate-limit when a single top-level ninja is in control). I guess fixing this at the superbuild level would need <a href="https://github.com/ninja-build/ninja/issues/1139">job server support in ninja</a>.</p>

---

## Post #4 by @jcfr (2018-03-30 17:09 UTC)

<p>Support for the <code>CMAKE_JOB_*</code> variables was added to Slicer in <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=27117">r27117</a></p>
<p>That alone should help reduce the relative number of link job vs build job, considering that link job are require more memory, it is sensible to set a lower number.</p>
<p>Now, the good news is that I created a project to distribute the version of ninja with Jobserver support, see</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/dockbuild/ninja-jobserver/releases">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/dockbuild/ninja-jobserver/releases" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/0276232c0f580af8bf97b38f0305b21faeec52ed300bf548da98fb8c26337106/dockbuild/ninja-jobserver" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/dockbuild/ninja-jobserver/releases" target="_blank" rel="noopener">Releases · dockbuild/ninja-jobserver</a></h3>

  <p>a small build system with a focus on speed [with GNU make jobserver client support] - dockbuild/ninja-jobserver</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I already have binary for Linux available, the macOS and Windows still need to be generated.</p>
<p>Cc: <a class="mention" href="/u/thewtex">@thewtex</a></p>

---

## Post #5 by @ihnorton (2018-03-30 19:49 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="4" data-topic="2304">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>That alone should help reduce the relative number of link job vs build job</p>
</blockquote>
</aside>
<p><img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji only-emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<aside class="quote no-group" data-username="jcfr" data-post="4" data-topic="2304">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>ninja with Jobserver support</p>
</blockquote>
</aside>
<p>Did you happen to test if it works with the cmake job pool variable already?</p>

---

## Post #6 by @jcfr (2018-03-30 22:52 UTC)

<p>Look like it is working as expected.</p>
<ul>
<li>Install <a href="https://cmake.org/download/">CMake 3.11</a>
</li>
<li>Install <a href="https://github.com/dockbuild/ninja-jobserver/releases">ninja with job server support</a>
</li>
<li>Configure using:</li>
</ul>
<pre><code class="lang-auto">~/Software/cmake-3.11.0-Linux-x86_64/bin/cmake \
  -GNinja \
  -DQt5_DIR:PATH=$Qt5_DIR \
  -DCMAKE_BUILD_TYPE:STRING=Release \
  '-DCMAKE_JOB_POOLS:STRING=compile=4;link=3' \
  -DCMAKE_JOB_POOL_COMPILE:STRING=compile \
  -DCMAKE_JOB_POOL_LINK:STRING=link \
../Slicer-Qt5-VTK9
</code></pre>
<p>Make sure you add the extra quote around <code>-DCMAKE_JOB_POOLS:STRING=compile=4;link=3</code></p>

---

## Post #7 by @jcfr (2018-03-30 22:53 UTC)

<p>All of that should enable us to fixup CircleCI, and also release Slicer on our Linux server using <a href="https://github.com/Slicer/SlicerBuildEnvironment/">https://github.com/Slicer/SlicerBuildEnvironment/</a></p>

---

## Post #8 by @phcerdan (2018-05-24 21:36 UTC)

<p>As a related note, if you use Archlinux, I just uploaded <a href="https://aur.archlinux.org/packages/ninja-kitware/" rel="nofollow noopener">ninja-kitware</a> to the AUR. It is my second package ever, so please, report any issue if you see one.</p>

---
