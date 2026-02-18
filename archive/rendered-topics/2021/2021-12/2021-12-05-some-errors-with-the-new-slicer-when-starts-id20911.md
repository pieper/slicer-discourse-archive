# Some errors with the new Slicer when starts

**Topic ID**: 20911
**Date**: 2021-12-05
**URL**: https://discourse.slicer.org/t/some-errors-with-the-new-slicer-when-starts/20911

---

## Post #1 by @slicer365 (2021-12-05 02:41 UTC)

<p>As is shown in this picture</p>
<p>what’s wrong with the module named ‘EditorLib’</p>
<p>Is it important?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/85aabc305ecef37e10d3284e32286fa62d26948d.png" data-download-href="/uploads/short-url/j4tiImgPceRMVFBYazCSpxREGzX.png?dl=1" title="微信图片_20211205103730" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/85aabc305ecef37e10d3284e32286fa62d26948d.png" alt="微信图片_20211205103730" data-base62-sha1="j4tiImgPceRMVFBYazCSpxREGzX" width="430" height="500" data-dominant-color="F6F2F0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">微信图片_20211205103730</span><span class="informations">580×674 28.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @jamesobutler (2021-12-05 03:53 UTC)

<p>The “Editor” module had been a legacy module and was finally removed.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/retiredmodules.html" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/user_guide/modules/retiredmodules.html</a></p>
<p>It appears that SlicerDMRI still has a reference in a testing module that was using it. It appears <a class="mention" href="/u/simonoxen">@simonoxen</a> has already issued a PR to try to fix the failed import.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/SlicerDMRI/SlicerDMRI/pull/152">
  <header class="source">

      <a href="https://github.com/SlicerDMRI/SlicerDMRI/pull/152" target="_blank" rel="noopener nofollow ugc">github.com/SlicerDMRI/SlicerDMRI</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/SlicerDMRI/SlicerDMRI/pull/152" target="_blank" rel="noopener nofollow ugc">STYLE: remove unused EditorLib import</a>
    </h4>

    <div class="branches">
      <code>SlicerDMRI:master</code> ← <code>simonoxen:master</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-12-01" data-time="21:11:09" data-timezone="UTC">09:11PM - 01 Dec 21 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/simonoxen" target="_blank" rel="noopener nofollow ugc">
          <img alt="simonoxen" src="https://avatars.githubusercontent.com/u/47367230?v=4" class="onebox-avatar-inline" width="20" height="20">
          simonoxen
        </a>
      </div>

      <div class="lines" title="1 commits changed 1 files with 0 additions and 2 deletions">
        <a href="https://github.com/SlicerDMRI/SlicerDMRI/pull/152/files" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+0</span>
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

<p>It appears that maybe <a class="mention" href="/u/pieper">@pieper</a> or <a class="mention" href="/u/ljod">@ljod</a> are helping to maintain SlicerDMRI? Unclear if this extension is still actively maintained, as in, should developers still be spending time trying to fix it up for latest Slicer? Has funding ceased? Has the project concluded?</p>

---

## Post #3 by @pieper (2021-12-05 17:28 UTC)

<p>Thanks for the heads up - I merged that PR.</p>
<aside class="quote no-group" data-username="slicer365" data-post="1" data-topic="20911">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/slicer365/48/67549_2.png" class="avatar"> slicer365:</div>
<blockquote>
<p>what’s wrong with the module named ‘EditorLib’</p>
<p>Is it important?</p>
</blockquote>
</aside>
<p>No, this was just an error message from a self-test of the module.  It shouldn’t have had any impact on using the rest of the extension.</p>

---

## Post #4 by @pieper (2021-12-05 17:29 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="2" data-topic="20911">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Has funding ceased? Has the project concluded?</p>
</blockquote>
</aside>
<p>There are still active and funded projects that use SlicerDMRI, but like a lot of infrastructure code it’s hard to get dedicated support for maintenance.  Community contributions like the PR from <a class="mention" href="/u/simonoxen">@simonoxen</a> are very much appreciated! <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>

---
