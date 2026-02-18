# Extension build failing for macos

**Topic ID**: 20438
**Date**: 2021-11-01
**URL**: https://discourse.slicer.org/t/extension-build-failing-for-macos/20438

---

## Post #1 by @Alex_Vergara (2021-11-01 09:42 UTC)

<p>Hi</p>
<p>I have noticed several fails in macos build of my extension, maybe this is happening for others. see <a href="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=Opendose" class="inline-onebox" rel="noopener nofollow ugc">CDash</a></p>
<p>It basically says “Unable to find executable”</p>
<p>For Windows and linux there is no problem at all.</p>

---

## Post #2 by @jamesobutler (2021-11-01 11:37 UTC)

<p>macOS had a build error that resulted in Slicer not being able to run, so no extensions were able to be built either.</p>
<p><a href="https://slicer.cdash.org/viewBuildError.php?buildid=2459187" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.cdash.org/viewBuildError.php?buildid=2459187</a></p>
<p>Build error caused by</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/Slicer/Slicer/commit/a15cbacbb91a3f187a8cd80c00bbb232e881f48b">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/commit/a15cbacbb91a3f187a8cd80c00bbb232e881f48b" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/commit/a15cbacbb91a3f187a8cd80c00bbb232e881f48b" target="_blank" rel="noopener nofollow ugc">ENH: Add "Select by points" tool to Dynamic Modeler module</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2021-10-31" data-time="21:12:04" data-timezone="UTC">09:12PM - 31 Oct 21 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener nofollow ugc">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>

      <div class="lines" title="changed 1 files with 1 additions and 1 deletions">
        <a href="https://github.com/Slicer/Slicer/commit/a15cbacbb91a3f187a8cd80c00bbb232e881f48b" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+1</span>
          <span class="removed">-1</span>
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


---

## Post #3 by @jamesobutler (2021-11-01 13:41 UTC)

<p>Issue reported at</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/SlicerSurfaceToolbox/issues/47">
  <header class="source">

      <a href="https://github.com/Slicer/SlicerSurfaceToolbox/issues/47" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/SlicerSurfaceToolbox</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/SlicerSurfaceToolbox/issues/47" target="_blank" rel="noopener nofollow ugc">Failed to build on macOS</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-11-01" data-time="13:41:15" data-timezone="UTC">01:41PM - 01 Nov 21 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/jamesobutler" target="_blank" rel="noopener nofollow ugc">
          <img alt="jamesobutler" src="https://avatars.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
          jamesobutler
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          bug
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Slicer factory build failed on macOS due to recent updates to SlicerSurfaceToolb<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ox (https://github.com/Slicer/SlicerSurfaceToolbox/commit/3e4245303e1d1599d4ef514373711598d6bd62c6).

https://slicer.cdash.org/viewBuildError.php?buildid=2459187</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @lassoan (2021-11-01 17:03 UTC)

<p>Thanks for reporting, I’ve pushed a fix.</p>

---

## Post #5 by @Alex_Vergara (2021-11-02 07:52 UTC)

<p>the error seems to persist <a href="https://slicer.cdash.org/viewTest.php?onlynotrun&amp;buildid=2460660" class="inline-onebox" rel="noopener nofollow ugc">CDash</a></p>

---

## Post #6 by @jamesobutler (2021-11-02 09:55 UTC)

<p>Yes, that fix was not complete. You can follow this PR of work</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/SlicerSurfaceToolbox/pull/48#event-5552807401">
  <header class="source">

      <a href="https://github.com/Slicer/SlicerSurfaceToolbox/pull/48#event-5552807401" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/SlicerSurfaceToolbox</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/SlicerSurfaceToolbox/pull/48" target="_blank" rel="noopener nofollow ugc">Fix macOS build error, simplify setting of position independent flag and fix warnings</a>
    </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>jcfr:simplify-setting-of-position-independent-code-flag</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-11-01" data-time="17:34:46" data-timezone="UTC">05:34PM - 01 Nov 21 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/jcfr" target="_blank" rel="noopener nofollow ugc">
          <img alt="jcfr" src="https://avatars.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
          jcfr
        </a>
      </div>

      <div class="lines" title="18 commits changed 31 files with 72 additions and 53 deletions">
        <a href="https://github.com/Slicer/SlicerSurfaceToolbox/pull/48/files" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+72</span>
          <span class="removed">-53</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This commit is a follow up of 8dd9ce0 (COMP: Fix linux build) fixing
a regressi<span class="show-more-container"><a href="https://github.com/Slicer/SlicerSurfaceToolbox/pull/48" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">on originally introduced in 3e4245303 (ENH: Add SelectByPoints
tool to DynamicModeler)</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #7 by @Alex_Vergara (2021-11-03 08:32 UTC)

<p>Apparently it is fixed now, no more errors in CDASH, thanks for the good work!!</p>

---
