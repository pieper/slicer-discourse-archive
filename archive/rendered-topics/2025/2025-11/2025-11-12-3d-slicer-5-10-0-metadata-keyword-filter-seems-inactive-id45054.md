# 3D Slicer 5.10.0: Metadata keyword filter seems inactive

**Topic ID**: 45054
**Date**: 2025-11-12
**URL**: https://discourse.slicer.org/t/3d-slicer-5-10-0-metadata-keyword-filter-seems-inactive/45054

---

## Post #1 by @jimjllin (2025-11-12 17:23 UTC)

<p>Hi Slicer Developers and Community,</p>
<p>I am currently testing the 3D Slicer version 5.10.0 (tried both Mac and Windows versions).</p>
<p>I seem to have found an issue where the keyword filter in the “Add DICOM Data” module’s “View DICOM Metadata” function is not functioning.</p>
<p>In the “Filter” search box at the pop-out window “DICOM File Metadata”, I type a known keyword (e.g., “Spacing”).</p>
<p>Expected Behavior: The list of metadata keys should dynamically filter to show only the items containing the typed keyword.</p>
<p>Actual Behavior: The list does not change at all. The filter appears to have no effect.</p>
<p>Can anyone else reproduce this? Is this a known issue, or has the functionality changed?</p>
<p>Thank you for your help!</p>

---

## Post #2 by @pieper (2025-11-12 18:01 UTC)

<p>Thanks for reporting this, I can replicate it too.</p>
<p>Maybe it’s related to the recent visual dicom browser work?  <a class="mention" href="/u/davide_punzo">@Davide_Punzo</a></p>

---

## Post #3 by @lassoan (2025-11-12 18:37 UTC)

<p>I’ve added a note to the issuebtracker here: <a href="https://github.com/commontk/CTK/issues/1230#issuecomment-3523384340" class="inline-onebox">Visual DICOM roadmap · Issue #1230 · commontk/CTK · GitHub</a></p>

---

## Post #4 by @Davide_Punzo (2025-11-13 05:16 UTC)

<p>last update to visual dicom browser was on Aug 7, 2025</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/commontk/CTK/commit/fb91447e0e15327341619cc0cda744724408ebc6">
  <header class="source">

      <a href="https://github.com/commontk/CTK/commit/fb91447e0e15327341619cc0cda744724408ebc6" target="_blank" rel="noopener nofollow ugc">github.com/commontk/CTK</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/commontk/CTK/commit/fb91447e0e15327341619cc0cda744724408ebc6" target="_blank" rel="noopener nofollow ugc">COMP: Fix ctkDICOMSchedulerTest1 test</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2025-08-07" data-time="20:19:40" data-timezone="UTC">08:19PM - 07 Aug 25 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/Punzo" target="_blank" rel="noopener nofollow ugc">
          <img alt="" src="https://avatars.githubusercontent.com/u/7985338?v=4" class="onebox-avatar-inline" width="20" height="20">
          Punzo
        </a>
      </div>

      <div class="lines" title="changed 1 files with 4 additions and 1 deletions">
        <a href="https://github.com/commontk/CTK/commit/fb91447e0e15327341619cc0cda744724408ebc6" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+4</span>
          <span class="removed">-1</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This changes the test to check the number of running jobs instead of
the total n<span class="show-more-container"><a href="https://github.com/commontk/CTK/commit/fb91447e0e15327341619cc0cda744724408ebc6" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">umber of jobs. The previous check was incorrect because
jobs are not automatically destroyed when they finish, leading to
a mismatch in the expected number of jobs.

The updated check ensures that the number of running jobs matches
the number of images. This should generally hold true unless an
image retrieval finishes before the check, making the test
non-deterministic in some cases. We can observe this behavior and
adjust if necessary.

Co-authored-by: Jean-Christophe Fillion-Robin &lt;jchris.fillionr@kitware.com&gt;</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I tested on version Slicer-5.9.0-2025-09-22-linux-amd64 and the filtering is working.</p>
<p>It is also working on my CTK dev branch <a href="https://github.com/Punzo/CTK/tree/visualDICOMBrowserUIRefactor" class="inline-onebox" rel="noopener nofollow ugc">GitHub - Punzo/CTK at visualDICOMBrowserUIRefactor</a></p>
<p>between this branch and CTK master, I see ~90 commits for Qt6, probably the issue is there.<br>
I have to rebase my dev branch to latest CTK anyway. Once I do it, I can check what is broken in latest CTK.</p>

---

## Post #5 by @Davide_Punzo (2025-11-13 05:40 UTC)

<p>the regression was introduced in</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/commontk/CTK/commit/495be9795b46e3707383e7d5302f6cfc5d9e9ffc">
  <header class="source">

      <a href="https://github.com/commontk/CTK/commit/495be9795b46e3707383e7d5302f6cfc5d9e9ffc" target="_blank" rel="noopener nofollow ugc">github.com/commontk/CTK</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/commontk/CTK/commit/495be9795b46e3707383e7d5302f6cfc5d9e9ffc" target="_blank" rel="noopener nofollow ugc">COMP: Prefer FilterRegularExpression setter/getter anticipating Qt6</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2025-11-07" data-time="15:10:07" data-timezone="UTC">03:10PM - 07 Nov 25 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/kislinsk" target="_blank" rel="noopener nofollow ugc">
          <img alt="" src="https://avatars.githubusercontent.com/u/9033034?v=4" class="onebox-avatar-inline" width="20" height="20">
          kislinsk
        </a>
      </div>

      <div class="lines" title="changed 2 files with 7 additions and 7 deletions">
        <a href="https://github.com/commontk/CTK/commit/495be9795b46e3707383e7d5302f6cfc5d9e9ffc" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+7</span>
          <span class="removed">-7</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This changes the usage of `setFilterRegExp` to `setFilterRegularExpression` in
a<span class="show-more-container"><a href="https://github.com/commontk/CTK/commit/495be9795b46e3707383e7d5302f6cfc5d9e9ffc" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">nticipation of the transition to Qt6, where the former method is deprecated.

Co-authored-by: Jean-Christophe Fillion-Robin &lt;jchris.fillionr@kitware.com&gt;</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Fixed in</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/commontk/CTK/commit/011c7afb1dcc8233600979809feaea3a76e52a00">
  <header class="source">

      <a href="https://github.com/commontk/CTK/commit/011c7afb1dcc8233600979809feaea3a76e52a00" target="_blank" rel="noopener nofollow ugc">github.com/commontk/CTK</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/commontk/CTK/commit/011c7afb1dcc8233600979809feaea3a76e52a00" target="_blank" rel="noopener nofollow ugc">BUG: Fix filter expression handling in DICOM object list widget</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2025-11-13" data-time="05:38:47" data-timezone="UTC">05:38AM - 13 Nov 25 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/Punzo" target="_blank" rel="noopener nofollow ugc">
          <img alt="" src="https://avatars.githubusercontent.com/u/7985338?v=4" class="onebox-avatar-inline" width="20" height="20">
          Punzo
        </a>
      </div>

      <div class="lines" title="changed 1 files with 4 additions and 2 deletions">
        <a href="https://github.com/commontk/CTK/commit/011c7afb1dcc8233600979809feaea3a76e52a00" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+4</span>
          <span class="removed">-2</span>
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

<p>I have tested only in Qt5.15. <a class="mention" href="/u/jcfr">@jcfr</a> can you please check it out the fix if it works in Qt6?</p>

---

## Post #6 by @pieper (2025-11-13 13:49 UTC)

<p>Thanks <a class="mention" href="/u/davide_punzo">@Davide_Punzo</a> !</p>

---

## Post #7 by @Davide_Punzo (2025-11-13 16:21 UTC)

<p>np! PR at <a href="https://github.com/commontk/CTK/pull/1318" class="inline-onebox" rel="noopener nofollow ugc">BUG: Fix filter expression handling in DICOM object list widget by Punzo · Pull Request #1318 · commontk/CTK · GitHub</a></p>

---
