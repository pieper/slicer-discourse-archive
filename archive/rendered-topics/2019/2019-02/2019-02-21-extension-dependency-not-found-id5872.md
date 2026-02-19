---
topic_id: 5872
title: "Extension Dependency Not Found"
date: 2019-02-21
url: https://discourse.slicer.org/t/5872
---

# Extension dependency not found

**Topic ID**: 5872
**Date**: 2019-02-21
**URL**: https://discourse.slicer.org/t/extension-dependency-not-found/5872

---

## Post #1 by @adamrankin (2019-02-21 17:41 UTC)

<p>Hello all,</p>
<p>Looking into why our extension didn’t build:<br>
<a href="http://slicer.cdash.org/viewConfigure.php?buildid=1518975" class="onebox" target="_blank" rel="nofollow noopener">http://slicer.cdash.org/viewConfigure.php?buildid=1518975</a></p>
<p>Is there something obvious I’m missing? I added the dependency to SlicerVirtualReality in EXTENSION_DEPENDS</p>

---

## Post #2 by @Sunderlandkyl (2019-02-21 18:15 UTC)

<p>Possibly because SlicerVirtualReality is not listed as a dependency in the ExtensionsIndex?<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/ExtensionsIndex/blob/master/SlicerVASST.s4ext" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/ExtensionsIndex/blob/master/SlicerVASST.s4ext" target="_blank" rel="nofollow noopener">Slicer/ExtensionsIndex/blob/master/SlicerVASST.s4ext</a></h4>
<pre><code class="lang-s4ext">#
# First token of each non-comment line is the keyword and the rest of the line
# (including spaces) is the value.
# - the value can be blank
#

# This is source code manager (i.e. svn)
scm git
scmurl https://github.com/VASST/SlicerVASST.git
scmrevision master

# list dependencies
# - These should be names of other modules that have .s4ext files
# - The dependencies will be built first
depends SlicerIGT VASSTAlgorithms

# Inner build directory (default is ".")
build_subdirectory inner-build

# homepage
</code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/ExtensionsIndex/blob/master/SlicerVASST.s4ext" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---

## Post #3 by @jcfr (2019-02-21 18:17 UTC)

<aside class="quote no-group" data-username="Sunderlandkyl" data-post="2" data-topic="5872">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sunderlandkyl/48/79987_2.png" class="avatar"> Sunderlandkyl:</div>
<blockquote>
<p>Possibly because SlicerVirtualReality is not listed as a dependency in the ExtensionsIndex?</p>
</blockquote>
</aside>
<p>Indeed, without this .. the extension build system doesn’t know which folder to pass along.</p>

---

## Post #4 by @adamrankin (2019-02-21 19:02 UTC)

<p>Ah, I thought the dependencies were detected from EXTENSION_DEPENDS. Ok, I’ll fix that.</p>

---

## Post #5 by @jcfr (2019-02-21 19:18 UTC)

<p>Indirectly yes.</p>
<p>(1) Metadata are listed in CMakeLists.txt -&gt; (2) generate description file in build directory -&gt; (3) description file added to the extension index.</p>
<p>In a nutshell, it is important to keep information consistent between description file and CMakeLists.txt.</p>
<p>Also, since the build system need to know an extension dependency before configuring it … it can not only be in the extension CMakeLists.txt, it needs to be available by some other way.</p>

---
