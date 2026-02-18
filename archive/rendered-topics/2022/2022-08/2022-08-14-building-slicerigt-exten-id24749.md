# Building SlicerIGT exten

**Topic ID**: 24749
**Date**: 2022-08-14
**URL**: https://discourse.slicer.org/t/building-slicerigt-exten/24749

---

## Post #1 by @SlicerIsGood (2022-08-14 10:18 UTC)

<p>in windows vs2022</p>
<pre><code class="lang-auto">CMake Error at CMakeLists.txt:25 (find_package):
  By not providing "FindSlicerIGSIO.cmake" in CMAKE_MODULE_PATH this project
  has asked CMake to find a package configuration file provided by
  "SlicerIGSIO", but CMake did not find one.
</code></pre>
<p>Follewed the [<a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#build-an-extension" class="inline-onebox" rel="noopener nofollow ugc">Extensions — 3D Slicer documentation</a>](<a href="https://development" rel="noopener nofollow ugc">https://development</a> doc)</p>

---

## Post #2 by @jamesobutler (2022-08-14 17:19 UTC)

<p>SlicerIGT has a dependency on another extension, SlicerIGSIO. So you need to build SlicerIGSIO and then you can build SlicerIGT.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/IGSIO/SlicerIGSIO">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/IGSIO/SlicerIGSIO" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/396eaf50895dab5e1bfa3a9a28190e8044063ddeb41c9783126f4fb2367a898a/IGSIO/SlicerIGSIO" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/IGSIO/SlicerIGSIO" target="_blank" rel="noopener nofollow ugc">GitHub - IGSIO/SlicerIGSIO: Utility extension for 3D Slicer, containing tools...</a></h3>

  <p>Utility extension for 3D Slicer, containing tools and algorithms for building image guided surgery applications - GitHub - IGSIO/SlicerIGSIO: Utility extension for 3D Slicer, containing tools and a...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @SlicerIsGood (2022-08-15 01:37 UTC)

<p>That’s right, and I build the SlicerIGSIO first, and add this to cmake gui(win10), ’ SlicerIGSIO_DIR  ****/SlicerIGSIO/inner-build ’</p>

---

## Post #4 by @SlicerIsGood (2022-08-15 01:53 UTC)

<p>by the way, I hvae  build the slicer with igt successfully, but the custom version I have built can load the other module, like “openlink” or sth else, should I build this together?</p>

---
