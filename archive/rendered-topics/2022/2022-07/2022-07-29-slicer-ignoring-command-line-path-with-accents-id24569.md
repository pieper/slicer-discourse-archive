---
topic_id: 24569
title: "Slicer Ignoring Command Line Path With Accents"
date: 2022-07-29
url: https://discourse.slicer.org/t/24569
---

# Slicer ignoring command line path with accents

**Topic ID**: 24569
**Date**: 2022-07-29
**URL**: https://discourse.slicer.org/t/slicer-ignoring-command-line-path-with-accents/24569

---

## Post #1 by @Ale (2022-07-29 19:03 UTC)

<p>Hi all, I’m getting this error when trying to load a file in command line:</p>
<blockquote>
<p>Slicer /home/mark/Docs/GMM_Cráneos_Armadillos/Models/cvi_24.ply</p>
</blockquote>
<p>Then, the error below shows strange characters where the “á” was in the path.</p>
<blockquote>
<p>Ignore argument received via command-line (not a valid URL or existing local file):  "/home/mark/Docs/GMM_CrÃ¡neos_Armadillos/Models/cvi_24.ply</p>
</blockquote>
<p>My locale output is:</p>
<p>LANG=es_AR.UTF-8<br>
LANGUAGE=es:en_US<br>
LC_CTYPE=“es_AR.UTF-8”<br>
LC_NUMERIC=es_AR.UTF-8<br>
LC_TIME=es_AR.UTF-8<br>
LC_COLLATE=“es_AR.UTF-8”<br>
LC_MONETARY=es_AR.UTF-8<br>
LC_MESSAGES=“es_AR.UTF-8”<br>
LC_PAPER=es_AR.UTF-8<br>
LC_NAME=es_AR.UTF-8<br>
LC_ADDRESS=es_AR.UTF-8<br>
LC_TELEPHONE=es_AR.UTF-8<br>
LC_MEASUREMENT=es_AR.UTF-8<br>
LC_IDENTIFICATION=es_AR.UTF-8<br>
LC_ALL=</p>
<p>System KDE Neon 5.25 (Ubuntu Focal)</p>

---

## Post #2 by @lassoan (2022-07-29 22:33 UTC)

<p>I was able to reproduce this:</p>
<pre><code class="lang-auto">perklab@perklabseg:~/Slicer/Slicer-5.0.2-linux-amd64$ ./Slicer --testing --python-code "print('GMM_Cráneos_Armadillo\n')"
Switch to module:  "Welcome"
GMM_CrÃ¡neos_Armadill
Switch to module:  ""
Switch to module:  ""
</code></pre>
<p>I’ve tried the same command with bypassing the launcher (started <code>bash</code> with the launcher and then  started SlicerApp-real from there) and it worked well:</p>
<pre><code class="lang-auto">perklab@perklabseg:~/Slicer/Slicer-5.0.2-linux-amd64$ ./Slicer --launch bash
perklab@perklabseg:~/Slicer/Slicer-5.0.2-linux-amd64$ ./bin/SlicerApp-real --testing --python-code "print('GMM_Cráneos_Armadillo\n')"
Switch to module:  "Welcome"
GMM_Cráneos_Armadillo
Switch to module:  ""
Switch to module:  ""
</code></pre>
<p>I’ve had a look at the code and found the root cause of the problem. The launcher does not use UTF8 everywhere, but there are <a href="https://github.com/commontk/AppLauncher/search?q=tolatin1">toLatin1</a> calls in it. We should replace those by <code>toLocal8bit</code> or <code>toUtf8</code>. I’ve submitted a pull request with this change:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/commontk/AppLauncher/pull/127">
  <header class="source">

      <a href="https://github.com/commontk/AppLauncher/pull/127" target="_blank" rel="noopener">github.com/commontk/AppLauncher</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/commontk/AppLauncher/pull/127" target="_blank" rel="noopener">Fix passing of non-ASCII characters as command-line arguments</a>
    </h4>

    <div class="branches">
      <code>commontk:master</code> ← <code>lassoan:fix-utf8-args</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-07-29" data-time="22:32:36" data-timezone="UTC">10:32PM - 29 Jul 22 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>

      <div class="lines" title="2 commits changed 5 files with 14 additions and 10 deletions">
        <a href="https://github.com/commontk/AppLauncher/pull/127/files" target="_blank" rel="noopener">
          <span class="added">+14</span>
          <span class="removed">-10</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Should fix the issues described here: https://discourse.slicer.org/t/slicer-igno<span class="show-more-container"><a href="https://github.com/commontk/AppLauncher/pull/127" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ring-command-line-path-with-accents/24569</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @jcfr (2025-08-08 18:17 UTC)

<p>To follow-up, corresponding fixes have been integrated.</p>
<p>See <a href="https://github.com/Slicer/Slicer/pull/8629">PR-8629 (Slicer/Slicer)</a> and <a href="https://github.com/commontk/AppLauncher/pull/127">PR-127 (commontk/AppLauncher)</a> for more details.</p>
<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a> for contributing the fix <img src="https://emoji.discourse-cdn.com/twitter/100.png?v=14" title=":100:" class="emoji" alt=":100:" loading="lazy" width="20" height="20"> &amp; everyone for the patience <img src="https://emoji.discourse-cdn.com/twitter/folded_hands.png?v=14" title=":folded_hands:" class="emoji" alt=":folded_hands:" loading="lazy" width="20" height="20"></p>

---
