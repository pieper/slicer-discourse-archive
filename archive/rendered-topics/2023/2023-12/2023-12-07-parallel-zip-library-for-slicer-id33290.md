# Parallel zip library for Slicer

**Topic ID**: 33290
**Date**: 2023-12-07
**URL**: https://discourse.slicer.org/t/parallel-zip-library-for-slicer/33290

---

## Post #1 by @muratmaga (2023-12-07 17:46 UTC)

<p>There is this python library that supports parallel zip and looks like it is MIT license. Would it be possible to incorporate this into Slicer and use it for MRB creation?</p>
<p><a href="https://github.com/fastzip/fastzip">GitHub - fastzip/fastzip: Fast parallel zip file creation</a></p>
<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/jcfr">@jcfr</a></p>

---

## Post #2 by @pieper (2023-12-07 18:08 UTC)

<p>The current implementation of MRB creation is in C++ with libarchive, but it’s very simple (just save everything to a tmp directory and then zip it) so making a python workalike implementation with this could be good.  It would be good to have tests to confirm both methods create the same result.</p>
<p>I’ve been thinking for a while though about making a zarr container for data and scenes, which may have some of the same benefits in a more scalable fashion so we should think about where we want to invest time.</p>

---

## Post #3 by @jcfr (2023-12-07 18:22 UTC)

<p>As a drop-in replacement, we have  plan to  switch <code>zlib</code> with <code>zlib-ng</code>. See <a href="https://github.com/Slicer/Slicer/pull/6708" class="inline-onebox">COMP: Switch to modern maintained zlib-ng fork of zlib by jamesobutler · Pull Request #6708 · Slicer/Slicer · GitHub</a></p>
<p>Instead of transitioning to <code>fastzip</code> (currently unmaintained), we will likely add support for <a href="https://github.com/facebook/zstd" class="inline-onebox">GitHub - facebook/zstd: Zstandard - Fast real-time compression algorithm</a></p>

---

## Post #4 by @jcfr (2023-12-07 18:23 UTC)

<p>Related ITK discussions:</p>
<blockquote>
<p>[…]  giving up on <code>zstd</code> as <code>zlib-ng</code> was integrated via <a href="https://github.com/InsightSoftwareConsortium/ITK/pull/2708">#2708</a> and <a href="https://github.com/InsightSoftwareConsortium/ITK/pull/2803">#2803</a>, adding zstd to NRRD and MetaIO is major undertaking, and there is ongoing OME-Zarr effort.</p>
</blockquote>
<p>See <a href="https://github.com/InsightSoftwareConsortium/ITK/issues/348" class="inline-onebox">Use zstd compression in NRRD and MetaIO · Issue #348 · InsightSoftwareConsortium/ITK · GitHub</a> and <a href="https://github.com/InsightSoftwareConsortium/ITK/issues/416" class="inline-onebox">Integrate modern optimized zlib · Issue #416 · InsightSoftwareConsortium/ITK · GitHub</a></p>

---

## Post #5 by @pieper (2023-12-07 18:27 UTC)

<p>Thanks Jc.  I didn’t see any zip support in zstd, but it looks like zlib-ng provides something we could use:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/zlib-ng/minizip-ng">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/zlib-ng/minizip-ng" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/ab4b53aa06fd6d7303b423caedf859b2ab72aa24bf5c8d78ff8a0f7663fecaa7/zlib-ng/minizip-ng" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/zlib-ng/minizip-ng" target="_blank" rel="noopener">GitHub - zlib-ng/minizip-ng: Fork of the popular zip manipulation library...</a></h3>

  <p>Fork of the popular zip manipulation library found in the zlib distribution. - GitHub - zlib-ng/minizip-ng: Fork of the popular zip manipulation library found in the zlib distribution.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
