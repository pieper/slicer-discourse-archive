---
topic_id: 47660
title: "Slicer crashes on startup due to SlicerVMTK extension"
date: 2026-07-17
url: https://discourse.slicer.org/t/47660
last_bumped: 2026-07-18T15:35:22.249Z
---

# Slicer crashes on startup due to SlicerVMTK extension

**Topic ID**: 47660
**Date**: 2026-07-17
**URL**: https://discourse.slicer.org/t/slicer-crashes-on-startup-due-to-slicervmtk-extension/47660

---

## Post #1 by @aabrown100-git (2026-07-17 19:08 UTC)

<p><strong>Issue</strong>: On Slicer 5.12.2, Slicer crashes on startup after restarting Slicer following installation of <code>SlicerVMTK</code>. The startup log shows module loading failures in <code>SlicerVMTK</code> due to unresolved dylib dependencies, including <code>libdcmjp2kcs.20.dylib</code> looking for <code>libopenjp2.7.dylib</code> and <code>libssl.1.1.dylib</code> referencing a bad install name (<code>/D/S/A/OpenSSL/libcrypto.1.1.dylib</code>). The crash happens during module instantiation while Slicer is loading extensions.</p>
<p><strong>Specs</strong>: macOS Tahoe on 2026 MacBook Pro with M5 Pro chip</p>
<p><strong>Other</strong>: I also tried installing <code>SlicerVMTK</code> on Slicer 5.10.0 and did not encounter any issues.</p>

---

## Post #2 by @muratmaga (2026-07-17 19:20 UTC)

<p>This macos specific, and related to this bug being tracked: <a href="https://github.com/Slicer/Slicer/pull/9263" class="inline-onebox" rel="noopener nofollow ugc">COMP: Update DCMTKcs to fix OpenJPEG over-linking on macOS by lassoan · Pull Request #9263 · Slicer/Slicer · GitHub</a></p>
<p>Until that’s fixed and a new patch release is cut, your easiest option is to use windows or linux version.</p>

---

## Post #3 by @aabrown100-git (2026-07-17 19:31 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="47660">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>COMP: Update DCMTKcs to fix OpenJPEG over-linking on macOS by lassoan · Pull Request <span class="hashtag-raw">#9263</span> · Slicer/Slicer · GitHub</p>
</blockquote>
</aside>
<p>Thanks <a class="mention" href="/u/muratmaga">@muratmaga</a> for the info. I see that PR is merged and I don’t see any linked issues. Is there other work to be done to fix this bug?</p>

---

## Post #4 by @muratmaga (2026-07-17 19:33 UTC)

<p>I do not know if there are any other work that needs to be done, but cutting a new release from scratch (like this) in itself takes a few days. Meanwhile I think the previews are fine (though I didn’t try it personnally).</p>

---

## Post #5 by @ebrahim (2026-07-17 21:06 UTC)

<p>The PR fixing the original issue is merged, but for some macOS-specific reason that I don’t yet understand there is a further problem that only applies to signed+notarized releases. The preview releases are unsigned, making them okay</p>

---

## Post #6 by @lassoan (2026-07-18 15:27 UTC)

<p>Sorry for the inconvenience. Until Slicer-5.12 is fixed, you can use a Slicer Preview Release (Slicer-5.13) on macOS if you need to use any extensions that contain C++ modules.</p>

---

## Post #7 by @lassoan (2026-07-18 15:35 UTC)

<p>I submitted an issue that we can mention at all related error reports and people can follow to get updates:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/9295">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/9295" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/9295" target="_blank" rel="noopener">Several extensions (MarkupsToModel, VMTK, etc.) fail on Slicer-5.12 on macOS</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2026-07-18" data-time="15:33:40" data-timezone="UTC">03:33PM - 18 Jul 26 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Extensions that contain compiled C++ code, such as MarkupsToModel and VMTK fail <span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">on Slicer-5.12 on macOS.

See for example this error report:
https://discourse.slicer.org/t/slicer-crashes-on-startup-due-to-slicervmtk-extension/47660</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
