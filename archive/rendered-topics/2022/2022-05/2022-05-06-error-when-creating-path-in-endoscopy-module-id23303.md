---
topic_id: 23303
title: "Error When Creating Path In Endoscopy Module"
date: 2022-05-06
url: https://discourse.slicer.org/t/23303
---

# Error when creating path in Endoscopy module

**Topic ID**: 23303
**Date**: 2022-05-06
**URL**: https://discourse.slicer.org/t/error-when-creating-path-in-endoscopy-module/23303

---

## Post #1 by @hherhold (2022-05-06 12:04 UTC)

<p>This is with Slicer preview 5.1.0-2022-05-04 on Windows 10. This is very likely pilot error as I have not used the Endoscopy module in (literally) years.</p>
<p>I’ve created a point list of input fiducials, selected a new model for Output Path, but when I click “Create Path”, nothing happens and I get the following error in the console/error log. Any help would be much appreciated!</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "C:/Users/hherhold/AppData/Local/NA-MIC/Slicer 5.1.0-2022-05-04/bin/../lib/Slicer-5.1/qt-scripted-modules/Endoscopy.py", line 239, in onCreatePathButtonClicked
    model = EndoscopyPathModel(result.path, fiducialsNode, outputPathNode)
  File "C:/Users/hherhold/AppData/Local/NA-MIC/Slicer 5.1.0-2022-05-04/bin/../lib/Slicer-5.1/qt-scripted-modules/Endoscopy.py", line 537, in __init__
    pointsArray = vtk.util.numpy_support(points.GetData())
TypeError: 'module' object is not callable
</code></pre>

---

## Post #2 by @rbumm (2022-05-06 15:01 UTC)

<p>I can confirm that, tested in 5.1.0-2022-05-05 (throws that error) and in a 2021 version of 4.13 (no error).</p>

---

## Post #3 by @sjuejsuj (2023-01-04 15:46 UTC)

<p>I had the same problem, it seems  to be an incompatibility caused by version update…<br>
I will try the older version.<br>
Thank you!</p>

---

## Post #4 by @pieper (2023-01-04 19:38 UTC)

<p><a class="mention" href="/u/sjuejsuj">@sjuejsuj</a> try a newer version rather than old.  This was a temporary regression that has since been fixed.</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/Slicer/Slicer/commit/3d66964c524a58b2583aac051e1310a5019d0039">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/commit/3d66964c524a58b2583aac051e1310a5019d0039" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/commit/3d66964c524a58b2583aac051e1310a5019d0039" target="_blank" rel="noopener">BUG: Fix regression introduced in Endoscopy module</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2022-05-14" data-time="01:49:42" data-timezone="UTC">01:49AM - 14 May 22 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/gaoyi" target="_blank" rel="noopener">
          <img alt="gaoyi" src="https://avatars.githubusercontent.com/u/920557?v=4" class="onebox-avatar-inline" width="20" height="20">
          gaoyi
        </a>
      </div>

      <div class="lines" title="changed 1 files with 2 additions and 2 deletions">
        <a href="https://github.com/Slicer/Slicer/commit/3d66964c524a58b2583aac051e1310a5019d0039" target="_blank" rel="noopener">
          <span class="added">+2</span>
          <span class="removed">-2</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This commit fixes a regression introduced in a258951f4 (BUG: Consolidate
vtk.uti<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/commit/3d66964c524a58b2583aac051e1310a5019d0039" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">l.numpy_support imports to fix UnboundLocalError) where the use
of `vtk_to_numpy` function was inadvertently removed.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #6 by @sjuejsuj (2023-01-06 12:27 UTC)

<p>I try to download the new version of ‘Endoscopy.py’ from Github, and replace current version in ‘.\Slicer 5.0.2\lib\Slicer-5.0\qt-scripted-modules’, then the endoscopy module can operate normally.<br>
Thank you!  <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=12" title=":smile:" class="emoji" alt=":smile:" loading="lazy" width="20" height="20"></p>

---

## Post #7 by @jamesobutler (2023-01-06 13:02 UTC)

<p><a class="mention" href="/u/sjuejsuj">@sjuejsuj</a> instead of manually replacing a single file in Slicer 5.0.2, please download and install latest Slicer stable 5.2.1 from <a href="https://download.slicer.org/" rel="noopener nofollow ugc">https://download.slicer.org/</a>.</p>

---

## Post #8 by @sjuejsuj (2023-01-06 13:09 UTC)

<p>I’ll download the latest Slicer version, thank you!</p>

---
