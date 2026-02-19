---
topic_id: 27174
title: "Bug 5 2 1 Data Is Loaded From Database But Doesnt Appear Und"
date: 2023-01-10
url: https://discourse.slicer.org/t/27174
---

# Bug: [5.2.1] Data is loaded from database but doesn't appear under "Loaded data"

**Topic ID**: 27174
**Date**: 2023-01-10
**URL**: https://discourse.slicer.org/t/bug-5-2-1-data-is-loaded-from-database-but-doesnt-appear-under-loaded-data/27174

---

## Post #1 by @Gabriel_WK (2023-01-10 18:03 UTC)

<p>Problem report for Slicer 5.2.1 win-amd64:</p>
<p>Expected behavior: Loaded data appear under “Loaded data” on the DICOM Module<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c4adb12e48633365a33ec6095a7d730377e49618.png" data-download-href="/uploads/short-url/s3TIvo1bnvAejubj6pMe0AUXWFq.png?dl=1" title="Captura de tela_20230110_145731" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c4adb12e48633365a33ec6095a7d730377e49618_2_690x435.png" alt="Captura de tela_20230110_145731" data-base62-sha1="s3TIvo1bnvAejubj6pMe0AUXWFq" width="690" height="435" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c4adb12e48633365a33ec6095a7d730377e49618_2_690x435.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c4adb12e48633365a33ec6095a7d730377e49618_2_1035x652.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c4adb12e48633365a33ec6095a7d730377e49618.png 2x" data-dominant-color="8C8C93"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de tela_20230110_145731</span><span class="informations">1361×859 74.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Actual behavior: Nothing appears under “Loaded data”<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f035a3eb607833edbd549fd1b20b700500733348.png" data-download-href="/uploads/short-url/ygZw2mei2cCs3TJYptkrS9Fg1Cw.png?dl=1" title="Captura de tela_20230110_144658" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f035a3eb607833edbd549fd1b20b700500733348_2_690x490.png" alt="Captura de tela_20230110_144658" data-base62-sha1="ygZw2mei2cCs3TJYptkrS9Fg1Cw" width="690" height="490" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f035a3eb607833edbd549fd1b20b700500733348_2_690x490.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f035a3eb607833edbd549fd1b20b700500733348_2_1035x735.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f035a3eb607833edbd549fd1b20b700500733348.png 2x" data-dominant-color="9E9EA4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de tela_20230110_144658</span><span class="informations">1078×767 60.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Data still showing normally on the Data module.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/12d732f425f64b1ef37430195b265dbc244b95bc.png" data-download-href="/uploads/short-url/2GFEGJZLZxiQUU5Y8LoQjS2yspK.png?dl=1" title="Captura de tela_20230110_145026" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/12d732f425f64b1ef37430195b265dbc244b95bc_2_690x490.png" alt="Captura de tela_20230110_145026" data-base62-sha1="2GFEGJZLZxiQUU5Y8LoQjS2yspK" width="690" height="490" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/12d732f425f64b1ef37430195b265dbc244b95bc_2_690x490.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/12d732f425f64b1ef37430195b265dbc244b95bc_2_1035x735.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/12d732f425f64b1ef37430195b265dbc244b95bc.png 2x" data-dominant-color="9D9DA2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de tela_20230110_145026</span><span class="informations">1078×767 60.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Windows 11. Fresh install of stable 5.2.1 downloaded on the official website and a locally compiled 5.3.0 that used to work nominally now displaying the same buggy behavior.</p>

---

## Post #2 by @pieper (2023-01-10 18:08 UTC)

<p>Yes, I can confirm this.  I know that data used to appear in the DICOM module’s view in older versions of slicer but it seems to have broken.</p>

---

## Post #3 by @lassoan (2023-01-12 17:42 UTC)

<p>The issue is now fixed (available in Slicer Preview Releases from tomorrow).</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/Slicer/Slicer/commit/aa245559e6027c8bf568ff96365dff9aed5be773">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/commit/aa245559e6027c8bf568ff96365dff9aed5be773" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/commit/aa245559e6027c8bf568ff96365dff9aed5be773" target="_blank" rel="noopener">BUG: Fix subject hierarchy tree in DICOM module</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2023-01-12" data-time="17:39:55" data-timezone="UTC">05:39PM - 12 Jan 23 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>

      <div class="lines" title="changed 1 files with 6 additions and 0 deletions">
        <a href="https://github.com/Slicer/Slicer/commit/aa245559e6027c8bf568ff96365dff9aed5be773" target="_blank" rel="noopener">
          <span class="added">+6</span>
          <span class="removed">-0</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">subject hierarchy tree in DICOM module remained empty after loading data.

This <span class="show-more-container"><a href="https://github.com/Slicer/Slicer/commit/aa245559e6027c8bf568ff96365dff9aed5be773" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">was caused by an unintended change in a recent commit (4d1e8c7c89d3cb79048bf3ffcc7fb0ccce57768d on 2022-11-15), which removed setting of the scene in the tree widget.

Fixes the issue reported at https://discourse.slicer.org/t/bug-5-2-1-data-is-loaded-from-database-but-doesnt-appear-under-loaded-data/27174</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
