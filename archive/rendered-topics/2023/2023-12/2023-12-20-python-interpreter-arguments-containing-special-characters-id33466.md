---
topic_id: 33466
title: "Python Interpreter Arguments Containing Special Characters"
date: 2023-12-20
url: https://discourse.slicer.org/t/33466
---

# Python interpreter arguments containing special characters

**Topic ID**: 33466
**Date**: 2023-12-20
**URL**: https://discourse.slicer.org/t/python-interpreter-arguments-containing-special-characters/33466

---

## Post #1 by @aymeric.chataigner (2023-12-20 09:53 UTC)

<p>Hi,</p>
<p>It is probably not a classic use of the python interpreter embedded in 3D Slicer but I would like to inform you about this strange behavior:</p>
<p>I use this interpreter to run a script which requires a file path as parameter.<br>
If the path contains some special characters (like é or €) which requires utf-8 encoding then sys.argv is wrong: these characters are replaced by other ones.</p>
<p>Here is a small script which shows clearly the issue:</p>
<pre><code class="lang-auto">import sys
import os

param = sys.argv[1]
print('param = ' + param)

argvb = list(map(os.fsencode, sys.argv))
param_bytes = argvb[1]
print('param_bytes = ' + str(param_bytes))
</code></pre>
<p>As you guess you have to provide 1 parameter to run it:<br>
/path/to/slicer/install/bin/PythonSlicer €</p>
<p>Result:<br>
param = Ã©<br>
param_bytes = b’\xc3\x83\xc2\xa9’</p>
<p>Expected Result (running ubuntu embedded python3 interpreter)<br>
param = é<br>
param_bytes = b’\xc3\xa9’</p>
<p>We see \x83\xc2 is added to the bytes, and it is caused by a wrong double utf-8 encoding issue (the accepted answer works well):</p><aside class="onebox stackexchange" data-onebox-src="https://stackoverflow.com/questions/4267019/double-decoding-unicode-in-python">
  <header class="source">

      <a href="https://stackoverflow.com/questions/4267019/double-decoding-unicode-in-python" target="_blank" rel="noopener nofollow ugc">stackoverflow.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://stackoverflow.com/users/145307/morten-siebuhr" target="_blank" rel="noopener nofollow ugc">
    <img alt="Morten Siebuhr" src="https://www.gravatar.com/avatar/faf4bc2957d714aed1da2d793ce0845b?s=256&amp;d=identicon&amp;r=PG" class="thumbnail onebox-avatar" width="" height="">
  </a>

<h4>
  <a href="https://stackoverflow.com/questions/4267019/double-decoding-unicode-in-python" target="_blank" rel="noopener nofollow ugc">Double-decoding unicode in python</a>
</h4>

<div class="tags">
  <strong>python, unicode, utf-8</strong>
</div>

<div class="date">
  asked by
  
  <a href="https://stackoverflow.com/users/145307/morten-siebuhr" target="_blank" rel="noopener nofollow ugc">
    Morten Siebuhr
  </a>
  on <a href="https://stackoverflow.com/questions/4267019/double-decoding-unicode-in-python" target="_blank" rel="noopener nofollow ugc">12:56PM - 24 Nov 10 UTC</a>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Do you have any idea why the python interpreter of 3d slicer decodes parameters twice ?</p>
<p>Best regards</p>

---

## Post #2 by @lassoan (2023-12-21 14:31 UTC)

<p>Thanks for reporting. The issue is known, it is caused by a bug in the application launcher. I’ve submitted a fix some time ago:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/commontk/AppLauncher/pull/127">
  <header class="source">

      <a href="https://github.com/commontk/AppLauncher/pull/127" target="_blank" rel="noopener">github.com/commontk/AppLauncher</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/commontk/AppLauncher/pull/127" target="_blank" rel="noopener">Fix passing of non-ASCII characters as command-line arguments</a>
      </h4>

    <div class="branches">
      <code>commontk:main</code> ← <code>lassoan:fix-utf8-args</code>
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

<p>It would be great if you could work with <a class="mention" href="/u/jcfr">@jcfr</a> to get the fix integrated.</p>
<p>Until then you can use a workaround: start bash using the launcher and then start Slicer from that terminal.</p>
<pre><code class="lang-plaintext">./Slicer --launch bash
bin/SlicerApp-real --python-code "print('é')"
</code></pre>

---

## Post #3 by @aymeric.chataigner (2023-12-22 10:08 UTC)

<p>Thank you Andras for this quick answer, I will discuss it with <a class="mention" href="/u/jcfr">@jcfr</a></p>

---

## Post #4 by @aymeric.chataigner (2024-01-03 14:21 UTC)

<p>Another quick question: why is there no completion in this interpreter ?</p>

---
