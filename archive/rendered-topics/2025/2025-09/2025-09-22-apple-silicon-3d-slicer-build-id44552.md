---
topic_id: 44552
title: "Apple Silicon 3D Slicer Build"
date: 2025-09-22
url: https://discourse.slicer.org/t/44552
---

# Apple Silicon 3D Slicer Build

**Topic ID**: 44552
**Date**: 2025-09-22
**URL**: https://discourse.slicer.org/t/apple-silicon-3d-slicer-build/44552

---

## Post #1 by @jfbasquiat (2025-09-22 22:46 UTC)

<p>Hi All - I’m having some difficulty locating the Apple Silicon build of 3D Slicer for macOS Tahoe. Could someone kindly point me in the right direction? (I’ve searched extensively, but all I could find was a build for antiquated Intel Macs.) Thanks in advance!</p>

---

## Post #2 by @jamesobutler (2025-09-23 00:08 UTC)

<aside class="quote quote-modified" data-post="7" data-topic="35699">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/build-3d-slicer-for-macos-arm64/35699/7">Build 3D Slicer for MacOS arm64?</a> <a class="badge-category__wrapper " href="/c/support/feature-requests/9"><span data-category-id="9" style="--category-badge-color: #F1592A; --category-badge-text-color: #FFFFFF; --parent-category-badge-color: #3AB54A;" data-parent-category-id="11" data-drop-close="true" class="badge-category --style-square --has-parent" title="This category is for submitting ideas about what enhancements or new features should be added to 3D Slicer. Make your voice heard by voting on feature requests - by opening the topic and clicking the Vote button or by creating a new topics. Slicer developers will make it a priority to work on feature requests that have more votes."><span class="badge-category__name">Feature requests</span></span></a>
    </div>
  </div>
  <blockquote>
    <a class="mention" href="/u/generisi">@GeneRisi</a> There are some various scripts around that people have tried to build Slicer from source to build a ARM64 variant, but nothing official yet such as Slicer preview build of such a version. 
The below issue is still in progress and various Slicer developers have been actively working on a long chain of dependency updates including Qt5 → Qt6 that is part of bringing in ARM64 support across all the various libraries that Slicer uses. It is currently being worked on and I expect it to conti…
  </blockquote>
</aside>

<p>Short answer is that the work required to update all the dependencies to support native ARM64 builds is actively in progress and we hope to have a native ARM64 build on the macOS platform soon (as well as ARM64 builds for Linux and Windows). For now Slicer is only available to be run through Rosetta 2 on Apple Silicon macs.</p>
<p>Below is the following issue tracking the work towards this effort:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/6811">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/6811" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/6811" target="_blank" rel="noopener nofollow ugc">Support for building/testing/packaging Slicer on Apple arm64</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2023-02-02" data-time="00:01:58" data-timezone="UTC">12:01AM - 02 Feb 23 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/jcfr" target="_blank" rel="noopener nofollow ugc">
          <img alt="" src="https://avatars.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
          jcfr
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          Type: Enhancement
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This is meta issues aiming to organize the sub-tasks associated with arm64 suppo<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">rt. See Sub-issues listed below.


Related issues and pull requests:
* https://github.com/Slicer/Slicer/issues/5944
* https://github.com/Slicer/Slicer/issues/6705
* https://github.com/Slicer/Slicer/issues/6490
* https://github.com/Slicer/Slicer/pull/8097

Related discourse posts:
* https://discourse.slicer.org/t/issues-running-slicer-on-macbook-m1-max/23974/3
* https://discourse.slicer.org/t/slicer-quit-unexpectedly-on-macbook-with-m1-chip/25989
* https://discourse.slicer.org/t/build-arm-32-openssl/31204
* https://discourse.slicer.org/t/developing-for-slicer-on-apple-silicon-build-targeting-x86-64/40686</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
