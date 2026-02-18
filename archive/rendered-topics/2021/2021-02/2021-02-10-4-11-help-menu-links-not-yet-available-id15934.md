# 4.11 help menu links not yet available

**Topic ID**: 15934
**Date**: 2021-02-10
**URL**: https://discourse.slicer.org/t/4-11-help-menu-links-not-yet-available/15934

---

## Post #1 by @fbordignon (2021-02-10 13:56 UTC)

<p>Hi guys, the Help menu links are pointing to empty pages such as <a href="https://www.slicer.org/w/index.php/Documentation/4.11" rel="noopener nofollow ugc">https://www.slicer.org/w/index.php/Documentation/4.11</a><br>
Can we copy the 4.10 pages and make the necessary changes?<br>
Thanks, Fernando.</p>

---

## Post #2 by @lassoan (2021-02-10 14:04 UTC)

<p>We are moving the documentation to <a href="https://slicer.readthedocs.io">https://slicer.readthedocs.io</a>. Cloning the full documentation for each major release was not sustainable on the wiki (created a lot of duplication yet we still could not keep the documentation in sync with all implementation details; and account management on the wiki has been problematic).</p>
<aside class="quote no-group" data-username="fbordignon" data-post="1" data-topic="15934">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fbordignon/48/5269_2.png" class="avatar"> fbordignon:</div>
<blockquote>
<p>Can we copy the 4.10 pages and make the necessary changes?</p>
</blockquote>
</aside>
<p>Yes, it would be great if you could help with copying over content to the new location, in markdown format (same format as this forum):</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/Slicer/Slicer/tree/main/Docs/user_guide/modules">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/tree/main/Docs/user_guide/modules" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/Slicer/Slicer/tree/main/Docs/user_guide/modules" target="_blank" rel="noopener"></a></h3>

  <p><a href="https://github.com/Slicer/Slicer/tree/main/Docs/user_guide/modules" target="_blank" rel="noopener">//github.com/Slicer/Slicer/tree/main/Docs/user_guide/modules</a></p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>If you send a pull request then we review/integrate the new page and update the link in the module. It is very useful even if you can transfer a few module pages. Thank you!</p>

---

## Post #3 by @jamesobutler (2021-02-13 20:58 UTC)

<aside class="onebox githubpullrequest">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/pull/5456" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/pull/5456" target="_blank" rel="noopener nofollow ugc">DOC: Update old URL links</a>
    </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>jamesobutler:doc-link-updates</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-02-13" data-time="20:57:14" data-timezone="UTC">08:57PM - 13 Feb 21 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/jamesobutler" target="_blank" rel="noopener nofollow ugc">
          <img alt="jamesobutler" src="https://avatars.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
          jamesobutler
        </a>
      </div>

      <div class="lines" title="1 commits changed 9 files with 27 additions and 32 deletions">
        <a href="https://github.com/Slicer/Slicer/pull/5456/files" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+27</span>
          <span class="removed">-32</span>
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

<p>^ This includes addressing the issue of in the Slicer GUI that Help-&gt;Interface Documentation was not pointing to the latest documentation.</p>

---
