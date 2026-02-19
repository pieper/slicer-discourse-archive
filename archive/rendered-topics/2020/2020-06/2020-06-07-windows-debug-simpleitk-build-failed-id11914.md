---
topic_id: 11914
title: "Windows Debug Simpleitk Build Failed"
date: 2020-06-07
url: https://discourse.slicer.org/t/11914
---

# [Windows] Debug SimpleITK build failed

**Topic ID**: 11914
**Date**: 2020-06-07
**URL**: https://discourse.slicer.org/t/windows-debug-simpleitk-build-failed/11914

---

## Post #1 by @adamrankin (2020-06-07 17:30 UTC)

<p>Hello all,</p>
<p>My debug build of Slicer fails on SimpleITK looking for python36_d.lib, is this a known issue?</p>
<p>I’ve scanned <a href="https://discourse.slicer.org/t/3d-slicer-windows-10-build-fail-only-simpleitk-project/6727/25" class="inline-onebox">3D slicer Windows 10 Build Fail (only SimpleITK project)</a> and that doesn’t seem to be related.</p>
<p>Qt 5.15.0, CMake 3.17.3, VS2019, v140 toolkit</p>
<p>[Edit: Deleted directories as I ran out of disk space, will get Git hash shortly]</p>
<p>Adam</p>

---

## Post #2 by @jamesobutler (2020-06-07 18:29 UTC)

<p>That seems most like what was discussed in <a href="https://github.com/Slicer/Slicer/issues/4898#issuecomment-623453879" rel="nofollow noopener">https://github.com/Slicer/Slicer/issues/4898#issuecomment-623453879</a> and I don’t believe it was ever fully resolved.</p>

---

## Post #3 by @lassoan (2020-06-07 18:35 UTC)

<p>Yes, it looks like the same issue. It would be better to continue the discussion in the issue tracker to keep all related information in one place.</p>

---

## Post #4 by @adamrankin (2020-06-09 14:42 UTC)

<p>Hi Andras,</p>
<p>After further exploration, I tried reverting this change (<strong>Edit: I reverted only the change to External_SimpleITK.cmake</strong>):<br>
</p><aside class="onebox githubcommit">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/commit/daee0f4ec1431fa44c39388dd82145f44be216f9#diff-109aeb3808fbb9cd5a014863e7556a16R113" target="_blank" rel="nofollow noopener">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/commit/daee0f4ec1431fa44c39388dd82145f44be216f9" target="_blank" rel="nofollow noopener">COMP: Fix build error due to wrong Python library found in debug mode</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2020-05-01" data-time="15:31:50" data-timezone="UTC">03:31PM - 01 May 20 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="nofollow noopener">
          <img alt="lassoan" src="https://avatars0.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
        
      </div>

      <div class="lines" title="changed 3 files with 12 additions and 0 deletions">
        <a href="https://github.com/Slicer/Slicer/commit/daee0f4ec1431fa44c39388dd82145f44be216f9" target="_blank" rel="nofollow noopener">
          <span class="added">+12</span>
          <span class="removed">-0</span>
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

<p>and re-doing a clean build. It succeeded. Somehow having the variable be empty doesn’t trigger the <span class="hashtag">#pragma</span> in the python headers to include the debug .lib</p>
<p>My steps:</p>
<ol>
<li>Checkout latest (<a href="https://github.com/Slicer/Slicer/commit/f665904f69c68710958406c2be4b43bc675e9211" rel="nofollow noopener">f665904</a> at the time)</li>
<li>CMake and superbuild! Fail with “cannot find python36_d.lib”</li>
<li>Delete SimpleITK, SimpleITK-build, etc… (all folders relating to SimpleITK)</li>
<li>CMake superbuild again, recreate fresh SimpleITK and SimpleITK prefix dirs</li>
<li>Build SimpleITK-download from superbuild project</li>
<li>Build SimpleITK from superbuild project, success</li>
</ol>
<p>Any thoughts? Could setting the debug lib variable somehow cause the preprocessor defines to change?</p>

---

## Post #5 by @adamrankin (2020-06-11 01:00 UTC)

<p>Nope! Just did another clean build and it worked. Yay…</p>

---

## Post #6 by @sunshine_boycn (2020-06-23 00:51 UTC)

<aside class="quote no-group" data-username="adamrankin" data-post="4" data-topic="11914">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/adamrankin/48/155_2.png" class="avatar"> adamrankin:</div>
<blockquote>
<p>superbuild</p>
</blockquote>
</aside>
<p>Have you every solve this problem? I met the exactly same problem with you under the same environment setting.</p>
<p>I noticed that there might be several solutions mentioned above, which one could solve the problem?</p>
<p>I was wondering why can’t we just change the linked python lib to the release version of python for simpleITK in CMakeLists.txt to solve the bugs forever?</p>

---

## Post #7 by @lassoan (2020-06-23 01:04 UTC)

<p>The problem is fixed now (in <a href="https://github.com/Slicer/Slicer/commit/49f3f0b8c02621baf6bad4e98c0b45c2ef30cd52">this commit</a>). Update to the latest master version and rebuild Slicer from scratch (delete the entire build folder).</p>

---
