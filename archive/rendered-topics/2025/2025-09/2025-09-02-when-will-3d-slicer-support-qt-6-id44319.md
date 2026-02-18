# When will 3D Slicer support Qt 6?

**Topic ID**: 44319
**Date**: 2025-09-02
**URL**: https://discourse.slicer.org/t/when-will-3d-slicer-support-qt-6/44319

---

## Post #1 by @Vincent (2025-09-02 16:24 UTC)

<p>First of all, thank 3D Slicer developers so much for working on supporting Qt 6.<br>
When will 3D Slicer support Qt 6? Will 3D Slicer support Qt 6 in 2025 ?</p>

---

## Post #2 by @jamesobutler (2025-09-02 16:52 UTC)

<p>3D Slicer is actively being worked on (by <a class="mention" href="/u/jcfr">@jcfr</a>) to support Qt 6. See the work being tracked at the below GitHub issue. As of today there has been some work to backport some fixes to the PythonQt upstream. Then with an updated PythonQt, we can update CTK and then finally Slicer to support Qt 6. Expect at least a build option that is using Qt6 in the next few weeks.</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/6388">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/6388" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/6388" target="_blank" rel="noopener nofollow ugc">Update Slicer to use Qt6</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-05-19" data-time="20:35:46" data-timezone="UTC">08:35PM - 19 May 22 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener nofollow ugc">
          <img alt="" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          Type: Bug
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Users are running into issues that are not going to be fixed on Qt5, therefore, <span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">we need to switch to Qt6.

Issues reported by users that would be likely fixed by moving to Qt6:
- Proxy issues on mac (https://discourse.slicer.org/t/proxy-issue-in-extensions-manager/23467)
- Layout selector toolbutton menu appears on primary screen (https://discourse.slicer.org/t/dropdown-menus-spawn-on-other-monitor/13003/14)
- https://github.com/Slicer/Slicer/issues/7206

Unfortunately, Qt6 considerably raises minimum software and hardware requirements - see https://github.com/Slicer/Slicer/pull/6108</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @pieper (2025-09-02 16:53 UTC)

<p>The general plan is to issue one more Qt5 release (5.10) and then switch the preview builds to Qt6 for testing.</p>

---

## Post #4 by @Vincent (2025-09-03 11:45 UTC)

<p>Will 5.10 support both of Qt 5 and Qt 6 ?</p>

---

## Post #5 by @cpinter (2025-09-03 12:31 UTC)

<p>To my understanding 5.10 will be Qt 5 only, and then eventually there will be a 5.11 with Qt 6, and then the next stable Qt 6.</p>

---

## Post #6 by @jamesobutler (2025-09-03 12:42 UTC)

<p>There is a possibility the 5.10 tag has a build option to choose building with Qt5 or Qt6, but the default build option and what the final Slicer 5.10 stable release installer will use is Qt5.</p>

---

## Post #7 by @ssv (2025-11-05 03:45 UTC)

<p>When to expect slicer support with qt6?</p>

---

## Post #8 by @jamesobutler (2025-11-05 04:21 UTC)

<p>Development is actively in progress. See recent work prepping for Qt6. It will be a build option first. Slicer Stable release 5.10.0 is expected to be released this week using Qt5 and Slicer Preview will switch to Qt6 likely soon after that.</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/Slicer/Slicer/commit/8a44717a61b16fa43c3616722375a0eb30950c3a">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/commit/8a44717a61b16fa43c3616722375a0eb30950c3a" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/commit/8a44717a61b16fa43c3616722375a0eb30950c3a" target="_blank" rel="noopener nofollow ugc">COMP: Enable AUTOUIC to simplify UI generation and prep for Qt6</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2025-11-04" data-time="15:05:23" data-timezone="UTC">03:05PM - 04 Nov 25 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/jcfr" target="_blank" rel="noopener nofollow ugc">
          <img alt="" src="https://avatars.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
          jcfr
        </a>
      </div>

      <div class="lines" title="changed 7 files with 136 additions and 27 deletions">
        <a href="https://github.com/Slicer/Slicer/commit/8a44717a61b16fa43c3616722375a0eb30950c3a" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+136</span>
          <span class="removed">-27</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Adopt target-level AUTOUIC and remove legacy UI wiring to reduce boilerplate
and<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/commit/8a44717a61b16fa43c3616722375a0eb30950c3a" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden"> align CTK with Qt6-ready CMake practices.

- Replace all `qt5_wrap_ui()` usage.
- Enable `AUTOUIC` on all Slicer libraries and tests.
- Set `AUTOUIC_SEARCH_PATHS` from declared UI forms (or `Resources/UI`).
- Set global `AUTOGEN_SOURCE_GROUP` to "Generated" for consistent IDE layout.
- Add AUTOGEN include dir so generated `ui_*.h` headers resolve reliably.
- Clean up: remove unused UI wrapping in `Modules/Loadable/Markups/Widgets/Testing/Cxx/CMakeLists.txt`

Co-authored-by: Hans Johnson &lt;hans-johnson@uiowa.edu&gt;</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
