---
topic_id: 2565
title: "Building Slicer Against Qt5 Win64"
date: 2018-04-11
url: https://discourse.slicer.org/t/2565
---

# Building Slicer against Qt5, Win64

**Topic ID**: 2565
**Date**: 2018-04-11
**URL**: https://discourse.slicer.org/t/building-slicer-against-qt5-win64/2565

---

## Post #1 by @Nicole_Aucoin (2018-04-11 20:13 UTC)

<p>I was looking at making a fresh build of Slicer against Qt 5, on a 64 bit Windows machine, and was directed from<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions/Prerequisites/Qt#Windows" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions/Prerequisites/Qt#Windows</a><br>
to the one liner build commands here:</p><aside class="onebox githubfolder" data-onebox-src="https://github.com/jcfr/qt-easy-build/tree/5.10.0#readme">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/jcfr/qt-easy-build/tree/5.10.0#readme" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/jcfr/qt-easy-build/tree/5.10.0#readme" target="_blank" rel="noopener nofollow ugc">GitHub - jcfr/qt-easy-build at 5.10.0</a></h3>

  <p><a href="https://github.com/jcfr/qt-easy-build/tree/5.10.0#readme" target="_blank" rel="noopener nofollow ugc">5.10.0</a></p>

  <p><span class="label1">Scripts allowing to easily build Qt with OpenSSL support on Linux, macOS or Windows</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>But all the 5.x branches there haven’t had the windows build commands updated in the readme files - they all have 4.8.7 still in the one liners for Windows (Linux/Mac are updated with the correct version number).</p>
<p>When I tried pointing the one liner to the 5.10.0/windows_build_qt.ps1 file, it triggered a download of Qt 4.8.7.</p>
<p>There’s a Qt 5.7.1 package mirrored on Midas but no 5.10.0. Would you recommend I use 5.7.1 for now?</p>
<p>Nicole</p>

---

## Post #2 by @lassoan (2018-04-11 20:27 UTC)

<p>On Windows, I use Qt5 binaries that I download from <a href="https://www.qt.io/">https://www.qt.io/</a> and it works, but it would be good to know if there is any advantage of building my own Qt. I guess <a class="mention" href="/u/jcfr">@jcfr</a> will be able to answer this when he gets back from vacation.</p>

---

## Post #3 by @Nicole_Aucoin (2018-04-11 20:42 UTC)

<p>Good to know that the binaries work, I’ll use them for now.</p>

---
