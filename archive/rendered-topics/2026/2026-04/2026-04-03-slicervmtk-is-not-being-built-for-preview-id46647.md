---
topic_id: 46647
title: "Slicervmtk Is Not Being Built For Preview"
date: 2026-04-03
url: https://discourse.slicer.org/t/46647
---

# SlicerVMTK is not being built for preview

**Topic ID**: 46647
**Date**: 2026-04-03
**URL**: https://discourse.slicer.org/t/slicervmtk-is-not-being-built-for-preview/46647

---

## Post #1 by @chir.set (2026-04-03 16:43 UTC)

<p>SlicerVMTK fails to build on <a href="https://slicer.cdash.org/builds/4168673/build" rel="noopener nofollow ugc">cdash</a> since a few weeks. The reported errors hint towards an environment problem on the build machines. It builds fine on Arch. Thanks for having a look.</p>

---

## Post #2 by @jamesobutler (2026-04-03 17:39 UTC)

<p>It actually appears like errors about not being compatible with VTK 9.6. When building on Arch did you use VTK 9.6?</p>
<p>See the following for updating details:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/8928#issuecomment-4074903898">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/8928#issuecomment-4074903898" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">

    <div class="github-icon-container" title="Comment">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 16 16" aria-hidden="true"><path fill-rule="evenodd" d="M1.5 2.75a.25.25 0 01.25-.25h8.5a.25.25 0 01.25.25v5.5a.25.25 0 01-.25.25h-3.5a.75.75 0 00-.53.22L3.5 11.44V9.25a.75.75 0 00-.75-.75h-1a.25.25 0 01-.25-.25v-5.5zM1.75 1A1.75 1.75 0 000 2.75v5.5C0 9.216.784 10 1.75 10H2v1.543a1.457 1.457 0 002.487 1.03L7.061 10h3.189A1.75 1.75 0 0012 8.25v-5.5A1.75 1.75 0 0010.25 1h-8.5zM14.5 4.75a.25.25 0 00-.25-.25h-.5a.75.75 0 110-1.5h.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0114.25 12H14v1.543a1.457 1.457 0 01-2.487 1.03L9.22 12.28a.75.75 0 111.06-1.06l2.22 2.22v-2.19a.75.75 0 01.75-.75h1a.25.25 0 00.25-.25v-5.5z"></path></svg>
    </div>



  <div class="github-info-container">

      <h4>
        Comment by
        <a href="https://github.com/jamesobutler" target="_blank" rel="noopener nofollow ugc">
          <img alt="" src="https://avatars.githubusercontent.com/u/15837524?u=77e23f0a30df57a25f193983b30b27790f224a1c&amp;v=4" class="onebox-avatar-inline" width="20" height="20">
          jamesobutler
        </a> - <a href="https://github.com/Slicer/Slicer/pull/8928#issuecomment-4074903898" target="_blank" rel="noopener nofollow ugc">ENH: Add support for building against VTK version 9.6.0</a>
      </h4>



    <div class="branches">
      <code>main</code> ← <code>jamesobutler:vtk-9.6.0-support</code>
    </div>

  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Slicer extension compatibility based on https://github.com/Slicer/Slicer/commit/<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/8928" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">cf471ffd35bd45705a15557001db1aa9e7d263e4:
- [x] https://github.com/lassoan/SlicerSegmentEditorExtraEffects/pull/69
- [x] https://github.com/IGSIO/IGSIO/pull/44
- [x] https://github.com/IGSIO/SlicerIGSIO/pull/33</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @chir.set (2026-04-03 18:19 UTC)

<p>At 1b21266bf47, Slicer built with VTK 9.5.</p>
<p>I’ll try a clean build next time. Thanks.</p>

---

## Post #4 by @chir.set (2026-04-03 21:21 UTC)

<p>A clean build of Slicer used VTK 9.6.</p>
<p>SlicerVMTK could be built after fixing the &lt;iostream&gt; includes, both in VMTK itself and in the C++ modules of SlicerVMTK.</p>
<p>I’ll send a PR in both projects ASAP.</p>

---
