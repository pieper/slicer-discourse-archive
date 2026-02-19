---
topic_id: 35525
title: "Error Running Radiomics Extension"
date: 2024-04-16
url: https://discourse.slicer.org/t/35525
---

# Error running radiomics extension

**Topic ID**: 35525
**Date**: 2024-04-16
**URL**: https://discourse.slicer.org/t/error-running-radiomics-extension/35525

---

## Post #1 by @conffite (2024-04-16 12:03 UTC)

<p>Hi，everyone-<br>
I recently installed the radiimics extension and have been encountering this error upon my program.<br>
This program was compiled by me, but I cannot use Radiomics. When I click on the function, it immediately crashes. Can you help me?</p>
<p>Best，<br>
Dora</p>

---

## Post #2 by @pieper (2024-04-16 12:31 UTC)

<p>If you compiled the code yourself, a common problem is mismatched library versions or incorrect library paths.  Please try the binaries we provide and install the radiomics extension.</p>

---

## Post #3 by @conffite (2024-04-17 04:27 UTC)

<p>How can I contact you to obtain binary files？</p>

---

## Post #4 by @pieper (2024-04-17 17:56 UTC)

<p>The SlicerRadiomics extension is in the extension manager.  You shouldn’t need to compile anything.</p>

---

## Post #5 by @conffite (2024-04-18 01:57 UTC)

<aside class="quote no-group" data-username="pieper" data-post="4" data-topic="35525">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>SlicerRadiomics</p>
</blockquote>
</aside>
<p>Yes, I found SlicerRadiomics in the expansion. However, the slicer I compiled after installation cannot use this feature, resulting in interface crashes, so I am very confused and actively seek help.</p>

---

## Post #6 by @pieper (2024-04-18 12:35 UTC)

<p>In general if you compile Slicer yourself, then you also need to compile any extensions too so they are compatible at the library level.</p>
<p>On the other hand it might be possible to switch the extension code to use the pypi package as discussed here:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/AIM-Harvard/SlicerRadiomics/issues/77">
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


---
