# Build module against Nightly Slicer

**Topic ID**: 5648
**Date**: 2019-02-05
**URL**: https://discourse.slicer.org/t/build-module-against-nightly-slicer/5648

---

## Post #1 by @siaeleni (2019-02-05 20:13 UTC)

<p>Hello,</p>
<p>I want to build a module against Nightly Slicer at Release mode.</p>
<p>When I build the sln at VS I would expect to get generated the files at :<br>
moduleName_build\lib\Slicer-4.11\cli-modules\Release<br>
path, but they are generated under :<br>
Slicer-build\lib\Slicer-4.11\cli-modules\Release</p>
<p>Can you explain me how can I change that path?<br>
Thanks</p>

---

## Post #2 by @lassoan (2019-02-05 20:16 UTC)

<p>The build location for module .dll and .exe files is correct - Slicer-build\lib\Slicer-4.11\cli-modules\Release. Do not attempt to change this path, as the build system relies on finding files in this location.</p>

---

## Post #3 by @siaeleni (2019-02-05 20:23 UTC)

<p>Ok, but why other modules, such as SlicerIGT, could be able to generate those files at<br>
Modules\SlicerIGT_build\lib\Slicer-4.11\qt-loadable-modules\Release ?</p>

---

## Post #4 by @lassoan (2019-02-05 20:39 UTC)

<p>I see, you mean CLI’s from your own extension. You can change the location of those to be within your build tree by adding these 3 lines of code:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/SlicerRt/SlicerRT/blob/master/PlmBspline/CMakeLists.txt#L32-L34" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerRt/SlicerRT/blob/master/PlmBspline/CMakeLists.txt#L32-L34" target="_blank" rel="nofollow noopener">SlicerRt/SlicerRT/blob/master/PlmBspline/CMakeLists.txt#L32-L34</a></h4>
<pre class="onebox"><code class="lang-txt"><ol class="start lines" start="32" style="counter-reset: li-counter 31 ;">
<li>RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/${Slicer_CLIMODULES_BIN_DIR}"
</li>
<li>LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/${Slicer_CLIMODULES_LIB_DIR}"
</li>
<li>ARCHIVE_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/${Slicer_CLIMODULES_LIB_DIR}"
</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p><a class="mention" href="/u/jcfr">@jcfr</a> Should we add these lines to the CLI module template?</p>

---

## Post #5 by @pieper (2019-05-07 19:04 UTC)

<p><a class="mention" href="/u/siaeleni">@siaeleni</a>  and I just ran into this again generating a new cli.  I think adding the OUTPUT_DIRECTORY lines to the CLI template makes sense, but we should also add the corresponding lines to the <a href="https://github.com/Slicer/Slicer/blob/master/Utilities/Templates/Modules/Loadable/CMakeLists.txt#L48-L60" rel="nofollow noopener">Loadable module template too.</a>  This should also include the python directory and any others?</p>

---

## Post #6 by @jcfr (2019-05-07 19:41 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="5648">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>you mean CLI’s from your own extension. You can change the location of those to be within your build tree by adding these 3 lines of code:</p>
</blockquote>
</aside>
<p>I do not recommend specifying output directories directly as parameter of <code>SEMMacroBuildCLI</code>, when building a CLI extensions, reasonable default are already expected to be set.</p>
<p>To address this, I suggest we update the following:</p>
<p><a href="https://github.com/Slicer/Slicer/blob/57613e53bee81b1318c55f624dba46ad101c1bda/CMake/UseSlicer.cmake.in#L304-L306" class="onebox" target="_blank" rel="noopener">https://github.com/Slicer/Slicer/blob/57613e53bee81b1318c55f624dba46ad101c1bda/CMake/UseSlicer.cmake.in#L304-L306</a></p>
<p>It was a regression introduced in <a href="https://github.com/Slicer/Slicer/commit/e93ec804c80a532a8d59a4c945ab4b81ff9a888f">https://github.com/Slicer/Slicer/commit/e93ec804c80a532a8d59a4c945ab4b81ff9a888f</a></p>
<p>I will follow up with the best course of action</p>

---
