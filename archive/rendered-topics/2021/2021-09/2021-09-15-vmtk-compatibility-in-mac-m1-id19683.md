---
topic_id: 19683
title: "Vmtk Compatibility In Mac M1"
date: 2021-09-15
url: https://discourse.slicer.org/t/19683
---

# VMTK compatibility in mac m1

**Topic ID**: 19683
**Date**: 2021-09-15
**URL**: https://discourse.slicer.org/t/vmtk-compatibility-in-mac-m1/19683

---

## Post #1 by @Weiqiang_Liu (2021-09-15 12:45 UTC)

<p>I use 3D slicer extension VMTK to extract the centerline and do diameter analysis. I use my own STL file and follow the guidelines in youtube. But I got: <strong>Failed to compute results: VMTK library is not found</strong>.</p>
<p>I also tried to use VMTK only in mac m1. It looks like there is a compatible issue. I cannot even open VMTK on mac pro with m1 chip. It works in other macs.</p>

---

## Post #2 by @lassoan (2021-09-15 13:05 UTC)

<p>VMTK should work well on M1. This is just a packaging error impacting both Intel/M1 macs:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/vmtk/SlicerExtension-VMTK/issues/37">
  <header class="source">

      <a href="https://github.com/vmtk/SlicerExtension-VMTK/issues/37" target="_blank" rel="noopener">github.com/vmtk/SlicerExtension-VMTK</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/vmtk/SlicerExtension-VMTK/issues/37" target="_blank" rel="noopener">VMTK gone missing recently on macOS in Slicer-4.11.20210226 and latest Slicer-4.13</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-08-09" data-time="19:08:54" data-timezone="UTC">07:08PM - 09 Aug 21 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">The extension installation package does not contain VMTK binaries, only the Slic<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">er module .py files, for both latest Slicer Stable Release and Slicer Preview Release on macOS.

It seems that the recent upgrade to VTK9 broke packaging for VTK-8.2.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p><a class="mention" href="/u/jcfr">@jcfr</a> could you give us an estimate about when this issue will be addressed?</p>

---

## Post #3 by @jcfr (2021-09-21 21:43 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="19683">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a class="mention" href="/u/jcfr">@jcfr</a> could you give us an estimate about when this issue will be addressed?</p>
</blockquote>
</aside>
<p>This has been fixed in <a href="https://github.com/vmtk/SlicerExtension-VMTK/pull/45" class="inline-onebox">COMP: Update VMTK to fix packaging of Python libraries on macOS by jcfr · Pull Request #45 · vmtk/SlicerExtension-VMTK · GitHub</a></p>
<p>Tomorrow preview build should confirm it works as expected.</p>

---
