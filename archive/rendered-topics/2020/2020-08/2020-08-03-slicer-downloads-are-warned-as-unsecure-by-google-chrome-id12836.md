---
topic_id: 12836
title: "Slicer Downloads Are Warned As Unsecure By Google Chrome"
date: 2020-08-03
url: https://discourse.slicer.org/t/12836
---

# Slicer downloads are warned as unsecure by Google Chrome

**Topic ID**: 12836
**Date**: 2020-08-03
**URL**: https://discourse.slicer.org/t/slicer-downloads-are-warned-as-unsecure-by-google-chrome/12836

---

## Post #1 by @jamesobutler (2020-08-03 16:28 UTC)

<p>With more recent versions of Google Chrome, downloading Slicer preview results in a warning that it can’t be downloaded securely.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f65a529670710b5a3076fef0101e075891d4b7d9.png" alt="image" data-base62-sha1="z9kYkjgcBhA3Ul2pG0M5C1Fafep" width="643" height="52"></p>
<p>The download link being an HTTP source such as <a href="http://slicer.kitware.com/midas3/api/rest?method=midas.bitstream.download&amp;name=Slicer-4.11.0-2020-08-02-win-amd64.exe&amp;checksum=61a92764f62f7bef212af5a62fb86bfe" rel="noopener nofollow ugc">http://slicer.kitware.com/midas3/api/rest?method=midas.bitstream.download&amp;name=Slicer-4.11.0-2020-08-02-win-amd64.exe&amp;checksum=61a92764f62f7bef212af5a62fb86bfe</a> which is linked from a HTTPS site <a href="http://download.slicer.org" rel="noopener nofollow ugc">download.slicer.org</a>.</p>
<p>Will the updated Extensions Manger framework also serve the Stable/Preview downloads from an HTTPS link?</p>
<p>For more information:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://security.googleblog.com/2020/02/protecting-users-from-insecure_6.html">
  <header class="source">
      <img src="https://security.googleblog.com/favicon.ico" class="site-icon" width="" height="">

      <a href="https://security.googleblog.com/2020/02/protecting-users-from-insecure_6.html" target="_blank" rel="noopener nofollow ugc">Google Online Security Blog</a>
  </header>

  <article class="onebox-body">
    <img width="" height="" src="http://2.bp.blogspot.com/-7bZ5EziliZQ/VynIS9F7OAI/AAAAAAAASQ0/BJFntXCAntstZe6hQuo5KTrhi5Dyz9yHgCK4B/s1600/googlelogo_color_200x200.png" class="thumbnail">

<h3><a href="https://security.googleblog.com/2020/02/protecting-users-from-insecure_6.html" target="_blank" rel="noopener nofollow ugc">Protecting users from insecure downloads in Google Chrome</a></h3>

  <p>Posted by Joe DeBlasio, Chrome security team   Update (April 6, 2020): Chrome was originally scheduled to start user-visible warnings on mix...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<blockquote>
<p>User-visible warnings will start in Chrome 84 (instead of Chrome 82), with warnings ramping up through Chrome 87. Final desktop blocking will be complete by Chrome 88. Android will lag one release behind, with the first user-visual warnings seen in Chrome 85.<br>
[<a href="https://www.chromestatus.com/feature/5691978677223424" rel="noopener nofollow ugc">source</a>]</p>
</blockquote>

---

## Post #2 by @jamesobutler (2020-08-03 17:48 UTC)

<p>I’ve proposed a change to <a href="http://download.slicer.org" rel="nofollow noopener">download.slicer.org</a> to use the HTTPS download links.</p>
<aside class="onebox githubpullrequest">
  <header class="source">
      <a href="https://github.com/mhalle/slicer4-download/pull/18" target="_blank" rel="nofollow noopener">github.com/mhalle/slicer4-download</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/mhalle/slicer4-download/pull/18" target="_blank" rel="nofollow noopener">ENH: Replace non-HTTPS download links with HTTPS links</a>
    </h4>

    <div class="branches">
      <code>mhalle:master</code> ← <code>jamesobutler:https-download-link</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-08-03" data-time="17:46:52" data-timezone="UTC">05:46PM - 03 Aug 20 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/jamesobutler" target="_blank" rel="nofollow noopener">
          <img alt="jamesobutler" src="https://avatars1.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
          jamesobutler
        </a>
      </div>

      <div class="lines" title="1 commits changed 1 files with 2 additions and 2 deletions">
        <a href="https://github.com/mhalle/slicer4-download/pull/18/files" target="_blank" rel="nofollow noopener">
          <span class="added">+2</span>
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


---
