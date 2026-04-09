---
topic_id: 46685
title: "Mac Extension Builds Failing With Cout Error"
date: 2026-04-08
url: https://discourse.slicer.org/t/46685
---

# Mac extension builds failing with cout error

**Topic ID**: 46685
**Date**: 2026-04-08
**URL**: https://discourse.slicer.org/t/mac-extension-builds-failing-with-cout-error/46685

---

## Post #1 by @pieper (2026-04-08 14:18 UTC)

<p>We noticed SlicerDMRI and other mac builds today.  Looks like python extensions are okay but not C++ ones.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f1b61e82543bdac64b56a9b056c8e7927b4f50b0.png" data-download-href="/uploads/short-url/yuhg3gmFdK2c3MOeje9CJuKnoM8.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f1b61e82543bdac64b56a9b056c8e7927b4f50b0_2_690x235.png" alt="image" data-base62-sha1="yuhg3gmFdK2c3MOeje9CJuKnoM8" width="690" height="235" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f1b61e82543bdac64b56a9b056c8e7927b4f50b0_2_690x235.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f1b61e82543bdac64b56a9b056c8e7927b4f50b0_2_1035x352.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f1b61e82543bdac64b56a9b056c8e7927b4f50b0_2_1380x470.png 2x" data-dominant-color="ECEDEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1405×479 63.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Maybe related to the <a href="https://discourse.slicer.org/t/2026-04-07-weekly-meeting/46673/2#p-133052-failing-macos-tests-sam-2">clipboard locale change</a>?   <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> <a class="mention" href="/u/ebrahim">@ebrahim</a> ?</p>

---

## Post #2 by @Sam_Horvath (2026-04-08 14:38 UTC)

<p>DMRI is failing across all platforms and has been since before the locale change</p>

---

## Post #3 by @Sam_Horvath (2026-04-08 14:39 UTC)

<p>Other C++ builds, such as SlicerIGT are fine</p>

---

## Post #4 by @Sam_Horvath (2026-04-08 14:42 UTC)

<p>C++ builds begin to fail after: <a href="https://github.com/Slicer/Slicer/commit/1b21266bf47f126ece58d12b87160e38f55ad258" class="inline-onebox">ENH: Add support for building against VTK version 9.6.0 · Slicer/Slicer@1b21266 · GitHub</a></p>

---

## Post #5 by @pieper (2026-04-08 14:45 UTC)

<p>Thanks <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> !</p>
<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a> do you see why this change would be breaking some extensions?  Maybe we can revert until the underlying issue is understood and fixed?</p>

---

## Post #6 by @Sam_Horvath (2026-04-08 14:52 UTC)

<p>Looking at the errors, many/most are complaining about <code>cout</code> missing from <code>std</code>.  Looking at a file that has errors in SlicerDMRI: <a href="https://github.com/SlicerDMRI/SlicerDMRI/blob/master/Libs/vtkDMRI/vtkSeedTracts.cxx" class="inline-onebox">SlicerDMRI/Libs/vtkDMRI/vtkSeedTracts.cxx at master · SlicerDMRI/SlicerDMRI · GitHub</a>, <code>&lt;iostream&gt;</code> is not included but <code>cout</code> is used, so perhaps a transitive include was cleaned up.</p>

---

## Post #7 by @pieper (2026-04-08 15:00 UTC)

<p>Yes, that makes sense <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> - maybe we should add that include to a core slicer header to fix all the extensions that relied on that at once and avoid the backwards incompatibility.</p>

---

## Post #8 by @Sam_Horvath (2026-04-08 15:11 UTC)

<p>I am not sure how much of the problem that would actually fix?  The <code>vtkSeedTracts</code> one I linked above is a pure vtkObject, it doesn’t include any Slicer headers.</p>

---

## Post #9 by @jamesobutler (2026-04-08 15:16 UTC)

<p>The  related items is a simple fix.</p>
<p>See the following comment:</p>
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

<p>and the following for reference:</p>
<aside class="onebox discoursetopic" data-onebox-src="https://discourse.vtk.org/t/important-update-standard-iostream-availability-from-vtk/16171">
  <header class="source">
      <img src="https://discourse.vtk.org/uploads/default/optimized/1X/6c8eb860cf266ca35755a0f95e95251fbe63514d_2_32x32.png" class="site-icon" alt="" width="32" height="32">

      <a href="https://discourse.vtk.org/t/important-update-standard-iostream-availability-from-vtk/16171" target="_blank" rel="noopener nofollow ugc" title="03:07PM - 03 December 2025">VTK – 3 Dec 25</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/369;"><img src="https://discourse.vtk.org/uploads/default/original/1X/b7d45ff6520965c4fbd148f8d0b1f7720956fa24.png" class="thumbnail" width="690" height="369"></div>

<div class="title-wrapper">
  <h3><a href="https://discourse.vtk.org/t/important-update-standard-iostream-availability-from-vtk/16171" target="_blank" rel="noopener nofollow ugc">Important Update: Standard iostream availability from VTK</a></h3>
  <div class="topic-category">
      <span class="badge-wrapper bullet">
        <span class="badge-category-bg" style="background-color: #0088CC;"></span>
        <span class="badge-category clear-badge">
          <span class="category-name">Development</span>
        </span>
      </span>
    <div class="topic-header-extra">
      <div class="list-tags">
        <div class="discourse-tags">
          <svg class="fa d-icon d-icon-tag svg-icon svg-string"><use href="#tag"></use></svg>
            <span class="discourse-tag simple">code</span>
        </div>
      </div>
    </div>
  </div>
</div>

  <p>Please note a significant change in VTK.  In the changeset from Merge Request !11993, the inclusion of  has been removed from a core header. This change previously caused global constructors to be triggered in every downstream translation unit. ...</p>

  <p>
    <span class="label1">Reading time: 1 mins 🕑</span>
      <span class="label2">Likes: 2 ❤</span>
  </p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #10 by @Sam_Horvath (2026-04-08 15:38 UTC)

<p>Thanks James!</p>
<p>Steve, I don’t think we can avoid doing the fixes at the extension level.</p>

---

## Post #11 by @pieper (2026-04-08 15:47 UTC)

<p>Yes, that’s very clear now, thanks!</p>
<p>Odd to make a backwards incompatible change on a minor release, but that’s the way it goes I guess.</p>
<p>I’ll try to fix SlicerDMRI later today.</p>

---

## Post #12 by @Sam_Horvath (2026-04-08 15:52 UTC)

<p>I’ll get SlicerRT today as well</p>

---

## Post #13 by @pieper (2026-04-08 22:39 UTC)

<p>Okay, SlicerDMRI should be good to go tomorrow.</p>

---
