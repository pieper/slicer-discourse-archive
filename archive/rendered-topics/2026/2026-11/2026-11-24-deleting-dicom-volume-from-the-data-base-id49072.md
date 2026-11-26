---
topic_id: 49072
title: "Deleting dicom volume from the data base"
date: 2026-11-24
url: https://discourse.slicer.org/t/49072
last_bumped: 2026-11-25T20:39:30.232Z
---

# Deleting dicom volume from the data base

**Topic ID**: 49072
**Date**: 2026-11-24
**URL**: https://discourse.slicer.org/t/deleting-dicom-volume-from-the-data-base/49072

---

## Post #1 by @philippepellerin (2026-11-24 15:48 UTC)

<p>Hi, In the 5.13.3 2026-11-16 I can’t delete the folder of dicom data, neither from the main, nor from the secondary list</p>

---

## Post #2 by @lassoan (2026-11-25 20:39 UTC)

<p>Good catch, thanks for reporting. This is due to upgrade from using Qt5 to Qt6. I’ve pushed a fix:</p>
<aside class="onebox githubpullrequest github-onebox" data-onebox-src="https://github.com/commontk/CTK/pull/1465">
    <header class="source github-onebox__header">
  <span class="github-onebox__label" role="img" aria-label="Pull request" title="Pull request">
    <svg width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path fill-rule="evenodd" d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path></svg>
    <span>Pull request</span>
  </span>
    <a class="github-onebox__repo" href="https://github.com/commontk/CTK/pull/1465" target="_blank" rel="noopener">
      <svg width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M6.766 11.328c-2.063-.25-3.516-1.734-3.516-3.656 0-.781.281-1.625.75-2.188-.203-.515-.172-1.609.063-2.062.625-.078 1.468.25 1.968.703.594-.187 1.219-.281 1.985-.281.765 0 1.39.094 1.953.265.484-.437 1.344-.765 1.969-.687.218.422.25 1.515.046 2.047.5.593.766 1.39.766 2.203 0 1.922-1.453 3.375-3.547 3.64.531.344.89 1.094.89 1.954v1.625c0 .468.391.734.86.547C13.781 14.359 16 11.53 16 8.03 16 3.61 12.406 0 7.984 0 3.563 0 0 3.61 0 8.031a7.88 7.88 0 0 0 5.172 7.422c.422.156.828-.125.828-.547v-1.25c-.219.094-.5.156-.75.156-1.031 0-1.64-.562-2.078-1.609-.172-.422-.36-.672-.719-.719-.187-.015-.25-.093-.25-.187 0-.188.313-.328.625-.328.453 0 .844.281 1.25.86.313.452.64.655 1.031.655s.641-.14 1-.5c.266-.265.47-.5.657-.656"></path></svg>
      <span>commontk/CTK</span>
    </a>
</header>


  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <div class="github-info-container">



      <h4>
        <a class="github-pull-request__title" href="https://github.com/commontk/CTK/pull/1465" title="BUG: Fix delete actions having no effect in DICOM browser with Qt6 (#1465)" target="_blank" rel="noopener">BUG: Fix delete actions having no effect in DICOM browser with Qt6 (#1465)</a>
      </h4>

    <div class="branches">
      <code title="master">master</code> ← <code title="lassoan:fix-classic-dicom-browser-delete-qt6">lassoan:fix-classic-dicom-browser-delete-qt6</code>
    </div>

      <div class="github-info">
        <div class="user">
          <a href="https://github.com/lassoan" target="_blank" rel="noopener">
            <img alt="" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
            lassoan
          </a>
        </div>

        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2026-11-25" data-time="20:38:10" data-timezone="UTC">08:38PM - 25 Nov 26 UTC</span>
        </div>

        <div class="lines" title="1 commits changed 1 files with 3 additions and 11 deletions">
          <a href="https://github.com/commontk/CTK/pull/1465/files" target="_blank" rel="noopener">
            <span class="added">+3</span>
            <span class="removed">-11</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">ctkDICOMBrowser::confirmDeleteSelectedUIDs compared the return value of QMessage<span class="show-more-container"><a href="https://github.com/commontk/CTK/pull/1465" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">Box::exec() to QMessageBox::AcceptRole. With custom buttons Qt5 returns the index of the clicked button (which happened to match the role), but Qt6 returns a different value, so the check always failed and patient/study/series delete actions were silently cancelled.

Check the clicked button instead, as ctkDICOMVisualBrowserWidget does.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Until it gets merged, you can use the visual DICOM browser.</p>

---
