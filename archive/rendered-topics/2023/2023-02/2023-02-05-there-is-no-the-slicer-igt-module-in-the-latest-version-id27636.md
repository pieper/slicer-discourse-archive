# There is no the Slicer IGT module in the latest version

**Topic ID**: 27636
**Date**: 2023-02-05
**URL**: https://discourse.slicer.org/t/there-is-no-the-slicer-igt-module-in-the-latest-version/27636

---

## Post #1 by @slicer365 (2023-02-05 00:47 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5a818146b97cbd8c085ef4e6a788370c7a0c2a45.jpeg" data-download-href="/uploads/short-url/cUEr01WBHUOzr4Bne3MqoPy2bid.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5a818146b97cbd8c085ef4e6a788370c7a0c2a45_2_690x310.jpeg" alt="image" data-base62-sha1="cUEr01WBHUOzr4Bne3MqoPy2bid" width="690" height="310" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5a818146b97cbd8c085ef4e6a788370c7a0c2a45_2_690x310.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5a818146b97cbd8c085ef4e6a788370c7a0c2a45_2_1035x465.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5a818146b97cbd8c085ef4e6a788370c7a0c2a45_2_1380x620.jpeg 2x" data-dominant-color="DFE0E2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1887×848 367 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @jamesobutler (2023-02-05 21:21 UTC)

<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> SlicerIGT has been failing to build since your most recent commit</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/SlicerIGT/SlicerIGT/commit/b6fad7f5472fe4f3ac3fa6e1a0fe1febb37ec96d">
  <header class="source">

      <a href="https://github.com/SlicerIGT/SlicerIGT/commit/b6fad7f5472fe4f3ac3fa6e1a0fe1febb37ec96d" target="_blank" rel="noopener nofollow ugc">github.com/SlicerIGT/SlicerIGT</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/SlicerIGT/SlicerIGT/commit/b6fad7f5472fe4f3ac3fa6e1a0fe1febb37ec96d" target="_blank" rel="noopener nofollow ugc">ENH: Move ResliceWithRuler to vtkSlicerPathExplorerLogic from widget</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2023-01-31" data-time="19:25:17" data-timezone="UTC">07:25PM - 31 Jan 23 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/Sunderlandkyl" target="_blank" rel="noopener nofollow ugc">
          <img alt="Sunderlandkyl" src="https://avatars.githubusercontent.com/u/9222709?v=4" class="onebox-avatar-inline" width="20" height="20">
          Sunderlandkyl
        </a>
      </div>

      <div class="lines" title="changed 3 files with 95 additions and 12 deletions">
        <a href="https://github.com/SlicerIGT/SlicerIGT/commit/b6fad7f5472fe4f3ac3fa6e1a0fe1febb37ec96d" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+95</span>
          <span class="removed">-12</span>
        </a>
      </div>
    </div>
  </div>
</div>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>SlicerIGT build error:</p>
<p><a href="https://slicer.cdash.org/viewBuildError.php?buildid=2934080" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.cdash.org/viewBuildError.php?buildid=2934080</a></p>

---

## Post #3 by @Sunderlandkyl (2023-02-05 22:21 UTC)

<p>Thanks, there were some uncommitted changes. Should be fixed in tomorrow’s build.</p>

---
