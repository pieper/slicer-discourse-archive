# Cannot find Slicer Radiomics in extensions library

**Topic ID**: 35749
**Date**: 2024-04-26
**URL**: https://discourse.slicer.org/t/cannot-find-slicer-radiomics-in-extensions-library/35749

---

## Post #1 by @Celina_Hallal (2024-04-26 14:30 UTC)

<p>I’m trying to install Radiomics extension, but I can’t find it. Tried to install from file also, with no success. I’m currently using v5.7-2024-04-22 in a MacOS.</p>
<p>Thanks in advance!</p>

---

## Post #2 by @pieper (2024-04-26 14:49 UTC)

<p>Yes, unfortunately this is a known issue:</p><aside class="onebox githubissue" data-onebox-src="https://github.com/AIM-Harvard/SlicerRadiomics/issues/77">
  <header class="source">

      <a href="https://github.com/AIM-Harvard/SlicerRadiomics/issues/77" target="_blank" rel="noopener">github.com/AIM-Harvard/SlicerRadiomics</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/AIM-Harvard/SlicerRadiomics/issues/77" target="_blank" rel="noopener">SlicerRadiomics unavailable for macOS since Slicer Preview 5.3.0 as of 2023-03-31</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2023-04-21" data-time="15:25:26" data-timezone="UTC">03:25PM - 21 Apr 23 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/jamesobutler" target="_blank" rel="noopener">
          <img alt="jamesobutler" src="https://avatars.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
          jamesobutler
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">The SlicerRadiomics extension has had build errors since March 31st, 2023 that h<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">as made it unavailable on macOS 
https://slicer.cdash.org/viewBuildError.php?buildid=2985286

It is unable to build a macOS whl of [`pyradiomics`](https://github.com/AIM-Harvard/pyradiomics). Around the time when this extension started to fail,
- The Slicer factory macOS machine was updated from macOS 10.13 (High Sierra) to macOS 13.0 (Ventura). See https://discourse.slicer.org/t/transition-of-macos-preview-build-from-host-10-13-high-sierra-to-13-ventura/28668. 
- Also the minimum required macOS deployment was changed to macOS 11.0 in https://github.com/Slicer/Slicer/commit/592ee0b516cd8cb448ab897c312ee6e4458dbb11.

cc: @JoostJM @fedorov</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>You can use an older version or window or linux for now.</p>

---
