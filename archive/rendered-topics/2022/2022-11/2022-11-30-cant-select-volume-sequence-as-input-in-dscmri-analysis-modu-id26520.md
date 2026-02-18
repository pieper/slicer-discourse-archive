# Can't select Volume Sequence as input in DSCMRI Analysis module

**Topic ID**: 26520
**Date**: 2022-11-30
**URL**: https://discourse.slicer.org/t/cant-select-volume-sequence-as-input-in-dscmri-analysis-module/26520

---

## Post #1 by @mikebind (2022-11-30 19:52 UTC)

<p>Back in July, <a class="mention" href="/u/lassoan">@lassoan</a> submitted a PR which I believe was supposed to allow the replacement of MultiVolumes with Volume Sequences as inputs to CLI modules (see <a href="https://discourse.slicer.org/t/convert-between-multivolume-and-volume-sequence/24504/5" class="inline-onebox">Convert between MultiVolume and Volume Sequence? - #5 by lassoan</a>).  I wasn’t able to test it right away (see <a href="https://discourse.slicer.org/t/windows-preview-build-failing-yesterday-and-today/24567" class="inline-onebox">Windows preview build failing yesterday and today</a>), but have finally gotten back around to this topic, and tested this functionality with Slicer 5.2.1, downloaded today.  I am not able to select a Volume Sequence as in input for the DSCMRI Analysis module, only MultiVolumes.  Specifically, Volume Sequences do not appear in the dropdown menu as options for the “Input 4D Image” parameter, it just says “Select a MRMLMultiVolume” and has options to “Rename current MRMLMultiVolume” and “Delete current MRMLMultiVolume”. I’m not sure what is not working, and would be happy to help troubleshoot if there are steps I could try. Thanks!</p>

---

## Post #3 by @lassoan (2022-11-30 20:39 UTC)

<p>Thanks for testing. You are right, I’ve implemented this and it should work.</p>
<p>I was able reproduce the problem, I will look it.</p>

---

## Post #4 by @lassoan (2022-11-30 21:21 UTC)

<p>Fixed in:</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/Slicer/Slicer/commit/f6a911153ceaaef8b264beb4d943a14dcfc26958">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/commit/f6a911153ceaaef8b264beb4d943a14dcfc26958" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/commit/f6a911153ceaaef8b264beb4d943a14dcfc26958" target="_blank" rel="noopener">BUG: Fix volume sequence support in CLI modules</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2022-11-30" data-time="21:20:39" data-timezone="UTC">09:20PM - 30 Nov 22 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>

      <div class="lines" title="changed 1 files with 1 additions and 1 deletions">
        <a href="https://github.com/Slicer/Slicer/commit/f6a911153ceaaef8b264beb4d943a14dcfc26958" target="_blank" rel="noopener">
          <span class="added">+1</span>
          <span class="removed">-1</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Volume sequences were not possible to select in CLI modules.
It was a regressio<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/commit/f6a911153ceaaef8b264beb4d943a14dcfc26958" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">n caused by a recent change.

Fixes the error reported at https://discourse.slicer.org/t/cant-select-volume-sequence-as-input-in-dscmri-analysis-module/26520.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
