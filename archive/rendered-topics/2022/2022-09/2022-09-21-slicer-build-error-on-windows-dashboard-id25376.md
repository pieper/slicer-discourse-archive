---
topic_id: 25376
title: "Slicer Build Error On Windows Dashboard"
date: 2022-09-21
url: https://discourse.slicer.org/t/25376
---

# Slicer build error on Windows dashboard

**Topic ID**: 25376
**Date**: 2022-09-21
**URL**: https://discourse.slicer.org/t/slicer-build-error-on-windows-dashboard/25376

---

## Post #1 by @lassoan (2022-09-21 15:45 UTC)

<p><a href="https://slicer.cdash.org/viewBuildError.php?onlydeltap&amp;buildid=2805894">Slicer build fails on the dashboard due</a> to SimpleITK:</p>
<pre><code class="lang-auto">Performing install step for 'SimpleITK'
  -- SimpleITK: Removing 'install' log files
  -- SimpleITK: SimpleITK_WORKING_DIR: D:/D/P/S-0-build/SimpleITK-build/SimpleITK-build/Wrapping/Python
  -- SimpleITK: D:/D/P/S-0-build/python-install/bin/PythonSlicer.exe;-m;pip;install;.
  -- SimpleITK: Errors detected - See below.
  CMake Error at D:/D/P/S-0/CMake/ExternalProjectForNonCMakeProject.cmake:104 (message):
  Processing d:\d\p\s-0-build\simpleitk-build\simpleitk-build\wrapping\python
  
CUSTOMBUILD : error : Command errored out with exit status 1: [D:\D\P\S-0-build\SimpleITK.vcxproj]
</code></pre>
<p><a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> <a class="mention" href="/u/jcfr">@jcfr</a> Could you have a look?</p>

---

## Post #2 by @Sam_Horvath (2022-09-21 15:56 UTC)

<p>This error seems to be coming up non-deterministically, the 9/20 build succeeded,<br>
<a href="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2022-09-20" class="onebox" target="_blank" rel="noopener">https://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2022-09-20</a></p>
<p>It seems to be related to some temp file stuff, will look at it.</p>

---

## Post #3 by @Sam_Horvath (2022-09-23 15:38 UTC)

<p>Coming back to this, it looks like a number of issues were occurring on the factory machine, most notably that the build directory was not being cleaned before the nightly build, which can cause any number of issues when changing major dependencies.</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/Slicer/DashboardScripts/commit/c741a37eaf545aa91084cbbd7114bd8a500b2ff2">
  <header class="source">

      <a href="https://github.com/Slicer/DashboardScripts/commit/c741a37eaf545aa91084cbbd7114bd8a500b2ff2" target="_blank" rel="noopener">github.com/Slicer/DashboardScripts</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/DashboardScripts/commit/c741a37eaf545aa91084cbbd7114bd8a500b2ff2" target="_blank" rel="noopener">BUG:  Nightly build not cleaned due to name change</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2022-09-21" data-time="19:15:09" data-timezone="UTC">07:15PM - 21 Sep 22 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/sjh26" target="_blank" rel="noopener">
          <img alt="sjh26" src="https://avatars.githubusercontent.com/u/25040869?v=4" class="onebox-avatar-inline" width="20" height="20">
          sjh26
        </a>
      </div>

      <div class="lines" title="changed 1 files with 1 additions and 1 deletions">
        <a href="https://github.com/Slicer/DashboardScripts/commit/c741a37eaf545aa91084cbbd7114bd8a500b2ff2" target="_blank" rel="noopener">
          <span class="added">+1</span>
          <span class="removed">-1</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Name was shortened here: https://github.com/Slicer/DashboardScripts/commit/7725b<span class="show-more-container"><a href="https://github.com/Slicer/DashboardScripts/commit/c741a37eaf545aa91084cbbd7114bd8a500b2ff2" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">a39efd526b6ea903f8ceff705c48f3da602
but batch file was not updated</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
