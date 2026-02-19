---
topic_id: 3010
title: "Slicerrt Extension Build Failure"
date: 2018-05-29
url: https://discourse.slicer.org/t/3010
---

# SlicerRT extension build failure

**Topic ID**: 3010
**Date**: 2018-05-29
**URL**: https://discourse.slicer.org/t/slicerrt-extension-build-failure/3010

---

## Post #1 by @gcsharp (2018-05-29 18:40 UTC)

<p>Any idea why this is happening?</p>
<pre><code>    -- SuperBuild - First pass - done
    -- SuperBuild - inner =&gt; Requires Plastimatch, 
    -- SuperBuild -   Plastimatch[OK]
    CMake Error at SuperBuild/External_Plastimatch.cmake:46 (ExternalProject_Add):
      Unknown CMake command "ExternalProject_Add".
    Call Stack (most recent call first):
      /home/kitware/Dashboards/Package/Slicer-481/CMake/ExternalProjectDependency.cmake:683 (include)
      /home/kitware/Dashboards/Package/Slicer-481/CMake/ExternalProjectDependency.cmake:746 (ExternalProject_Include_Dependencies)
      SuperBuild.cmake:24 (ExternalProject_Include_Dependencies)
      CMakeLists.txt:43 (include)
</code></pre>
<p><a href="http://slicer.cdash.org/buildSummary.php?buildid=1282802" class="onebox" target="_blank" rel="nofollow noopener">http://slicer.cdash.org/buildSummary.php?buildid=1282802</a></p>

---

## Post #2 by @lassoan (2018-05-29 18:53 UTC)

<p>Probably <code>include(ExternalProject)</code> is missed.</p>

---

## Post #3 by @gcsharp (2018-05-29 19:06 UTC)

<p>Yes, that is what a topic on Stack Exchange suggests.  It is easy and harmless to add.  But I have doubts on effectiveness because it was apparently never needed before, and when I build it locally, I don’t get this error.</p>

---

## Post #4 by @jcfr (2018-05-29 23:49 UTC)

<p>Explicitly including the ExternalProject module is only required with Slicer 4.8.1. Since <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26984">r26984</a> it is included through <code>UseSlicer.cmake</code>. This is why it was removed in <a href="https://github.com/SlicerRt/SlicerRT/commit/6495332b380437e4f525018a47842f457afc791f#diff-88b37dcc9267d819b6fabff68a8e5290">SlicerRt/SlicerRT@6495332</a></p>

---

## Post #5 by @gcsharp (2018-05-30 15:17 UTC)

<p>It seems the s4ext points to an older version.  Could someone please update when you get a chance?  Thanks!</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/ExtensionsIndex/pull/1552">
  <header class="source">

      <a href="https://github.com/Slicer/ExtensionsIndex/pull/1552" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/ExtensionsIndex</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/ExtensionsIndex/pull/1552" target="_blank" rel="noopener nofollow ugc">BUG: Bump SlicerRT version to remove reference to SlicerMacroCheckExt…</a>
      </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>gregsharp:slicerrt-build-error</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2018-05-30" data-time="15:12:02" data-timezone="UTC">03:12PM - 30 May 18 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/gregsharp" target="_blank" rel="noopener nofollow ugc">
            <img alt="gregsharp" src="https://avatars.githubusercontent.com/u/327896?v=4" class="onebox-avatar-inline" width="20" height="20">
            gregsharp
          </a>
        </div>

        <div class="lines" title="1 commits changed 1 files with 1 additions and 1 deletions">
          <a href="https://github.com/Slicer/ExtensionsIndex/pull/1552/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+1</span>
            <span class="removed">-1</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">…ernalProjectDependency</p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
