# Install extensions is not working on latest preview release

**Topic ID**: 28316
**Date**: 2023-03-11
**URL**: https://discourse.slicer.org/t/install-extensions-is-not-working-on-latest-preview-release/28316

---

## Post #1 by @mau_igna_06 (2023-03-11 21:57 UTC)

<p>I’m on ubuntu</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8cb1621f24fa8370aec093883e9d08855c9b3a52.jpeg" data-download-href="/uploads/short-url/k4CT2IzupCKpJwBCDwLDRPARAfE.jpeg?dl=1" title="Captura desde 2023-03-11 18-51-03" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8cb1621f24fa8370aec093883e9d08855c9b3a52_2_690x388.jpeg" alt="Captura desde 2023-03-11 18-51-03" data-base62-sha1="k4CT2IzupCKpJwBCDwLDRPARAfE" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8cb1621f24fa8370aec093883e9d08855c9b3a52_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8cb1621f24fa8370aec093883e9d08855c9b3a52_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8cb1621f24fa8370aec093883e9d08855c9b3a52_2_1380x776.jpeg 2x" data-dominant-color="6A6B74"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura desde 2023-03-11 18-51-03</span><span class="informations">1920×1080 210 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4c3bf7665d9cd4ec53ee1e76514c3312082c72c2.jpeg" data-download-href="/uploads/short-url/aSoLrndrqyTiYwopjNE6wfPTJuO.jpeg?dl=1" title="Captura desde 2023-03-11 18-50-31" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4c3bf7665d9cd4ec53ee1e76514c3312082c72c2_2_690x388.jpeg" alt="Captura desde 2023-03-11 18-50-31" data-base62-sha1="aSoLrndrqyTiYwopjNE6wfPTJuO" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4c3bf7665d9cd4ec53ee1e76514c3312082c72c2_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4c3bf7665d9cd4ec53ee1e76514c3312082c72c2_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4c3bf7665d9cd4ec53ee1e76514c3312082c72c2_2_1380x776.jpeg 2x" data-dominant-color="E6E6E6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura desde 2023-03-11 18-50-31</span><span class="informations">1920×1080 101 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thanks for the help</p>

---

## Post #2 by @lassoan (2023-03-12 00:51 UTC)

<p>Does that folder exist and writable for your user?</p>

---

## Post #3 by @muratmaga (2023-03-12 03:25 UTC)

<p>I am also getting a similar error when I start Slicer from the latest preview</p>
<pre><code class="lang-auto">maga@magalab-ML:~/Downloads$ tar zxf Slicer-5.3.0-2023-03-10-linux-amd64.tar.gz 
maga@magalab-ML:~/Downloads/Slicer$ cd .Slicer-5.3.0-2023-03-10-linux-amd64/
maga@magalab-ML:~/Downloads/Slicer-5.3.0-2023-03-10-linux-amd64$ ./Slicer 
"Failed to create extensions directory" "/home/maga/Downloads/Slicer-5.3.0-2023-03-10-linux-amd64/bin/../Slicer/Extensions-31632"
Switch to module:  "Welcome"
</code></pre>

---

## Post #4 by @muratmaga (2023-03-12 03:26 UTC)

<p>It is adding that extra <strong>Slicer</strong> folder (which is now replacing the NA-MIC folder), and that’s where it is failing to create.</p>

---

## Post #5 by @lassoan (2023-03-12 12:06 UTC)

<p>This <code>NA-MIC</code> to <code>Slicer</code> rename is a very recent change, so most likely that causes the problem. Is there a NA-MIC folder, too? Does the problem go away if you create the <code>Slicer</code> folder?</p>

---

## Post #6 by @mau_igna_06 (2023-03-12 13:21 UTC)

<p>Hi. Thanks for the answer</p>
<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="28316">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Is there a NA-MIC folder, too?</p>
</blockquote>
</aside>
<p>Nope</p>
<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="28316">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Does the problem go away if you create the <code>Slicer</code> folder?</p>
</blockquote>
</aside>
<p>You cannot create the Slicer folder you mention because that’s already the name of the executable to launch Slicer. Maybe the folder could be named “Slicer5”?</p>

---

## Post #7 by @lassoan (2023-03-12 13:39 UTC)

<p>You have solved the mystery! There was no issue on Windows, because the Slicer executable name is <code>Slicer.exe</code> and on macOS the folder structure is special, but on linux there is indeed a name clash. The only way to change this is to modify the Slicer executable or the organization name, because the settings subfolder naming logic logic is hardcoded in the constructor of the <code>QSettings</code> class.</p>
<p>Changing the Slicer executable name is probably not a good idea, as it could cause regressions at many places.</p>
<p>Potential ideas for organization name:</p>
<ul>
<li>
<code>slicer</code> - most linux file systems are case sensitive, so the name clash would be resolved, but it could be quite fragile, it may not work on some file systems</li>
<li><code>SlicerCommunity</code></li>
<li>
<code>Slicer5</code> - it would reset settings at each new Slicer major version, which may not what users expect, it is also not an organization name</li>
<li>
<code>slicer.org</code> - looks quite good, it is about the same as the organization domain, but it may be even good (as organization name and domain are sometimes used interchangeably)</li>
</ul>
<p>Are there any other suggestions?</p>
<p>I’ll submit a PR to change the value to <code>slicer.org</code> to resolve the issue until we decide on the final name.</p>
<p>I’ve created an issue in the bugtracker:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/6878">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/6878" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/6878" target="_blank" rel="noopener">Cannot install extensions in latest Slicer Preview Release on Linux</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2023-03-12" data-time="13:43:20" data-timezone="UTC">01:43PM - 12 Mar 23 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          type:bug
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">There is a name clash of the settings folder and Slicer executable since changin<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">g of the `organization name` from `NA-MIC` to `Slicer` (https://github.com/Slicer/Slicer/pull/6750).

There was no issue on Windows, because the Slicer executable name is Slicer.exe and on macOS the folder structure is special, but on linux there is indeed a name clash. The only way to change this is to modify the Slicer executable or the organization name, because the settings subfolder naming logic logic is hardcoded in the constructor of the QSettings class.

See more information here:
https://discourse.slicer.org/t/install-extensions-is-not-working-on-latest-preview-release/28316/7?u=lassoan

Changing the Slicer executable name is probably not a good idea, as it could cause regressions at many places. Therefore, we need to choose a different organization name.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/jcfr">@jcfr</a></p>

---

## Post #8 by @jcfr (2023-03-13 18:01 UTC)

<p>For future reference, thanks to <a class="mention" href="/u/lassoan">@lassoan</a>, the issue has been fixed in <a href="https://github.com/Slicer/Slicer/pull/6879">PR-6879</a>.</p>
<p>After downloading the latest Preview build, I confirm that installing extension works.</p>

---
